"""Windows Job Object aggregate-memory limit for trusted local Lean launches.

The Python helper remains blocked on stdin until the controlling process
attaches it to a new Job Object. Its children then inherit the same job.
This is not a sandbox for arbitrary client-supplied code.
"""
from __future__ import annotations

import ctypes
import os
import sys

from ctypes import wintypes

MIN_MEMORY_MB = 512
MAX_MEMORY_MB = 65536
JOB_OBJECT_LIMIT_JOB_MEMORY = 0x00000200
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
JOB_OBJECT_EXTENDED_LIMIT_INFORMATION = 9
JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION = 8
PROCESS_SET_QUOTA = 0x0100
PROCESS_TERMINATE = 0x0001


class JobUnavailable(RuntimeError):
    """A requested Windows Job Object limit could not be enforced."""


class BasicLimitInformation(ctypes.Structure):
    _fields_ = [
        ("PerProcessUserTimeLimit", ctypes.c_int64),
        ("PerJobUserTimeLimit", ctypes.c_int64),
        ("LimitFlags", wintypes.DWORD),
        ("MinimumWorkingSetSize", ctypes.c_size_t),
        ("MaximumWorkingSetSize", ctypes.c_size_t),
        ("ActiveProcessLimit", wintypes.DWORD),
        ("Affinity", ctypes.c_size_t),
        ("PriorityClass", wintypes.DWORD),
        ("SchedulingClass", wintypes.DWORD),
    ]


class IoCounters(ctypes.Structure):
    _fields_ = [
        ("ReadOperationCount", ctypes.c_uint64),
        ("WriteOperationCount", ctypes.c_uint64),
        ("OtherOperationCount", ctypes.c_uint64),
        ("ReadTransferCount", ctypes.c_uint64),
        ("WriteTransferCount", ctypes.c_uint64),
        ("OtherTransferCount", ctypes.c_uint64),
    ]


class ExtendedLimitInformation(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", BasicLimitInformation),
        ("IoInfo", IoCounters),
        ("ProcessMemoryLimit", ctypes.c_size_t),
        ("JobMemoryLimit", ctypes.c_size_t),
        ("PeakProcessMemoryUsed", ctypes.c_size_t),
        ("PeakJobMemoryUsed", ctypes.c_size_t),
    ]


class BasicAccountingInformation(ctypes.Structure):
    _fields_ = [
        ("TotalUserTime", ctypes.c_int64),
        ("TotalKernelTime", ctypes.c_int64),
        ("ThisPeriodTotalUserTime", ctypes.c_int64),
        ("ThisPeriodTotalKernelTime", ctypes.c_int64),
        ("TotalPageFaultCount", wintypes.DWORD),
        ("TotalProcesses", wintypes.DWORD),
        ("ActiveProcesses", wintypes.DWORD),
        ("TotalTerminatedProcesses", wintypes.DWORD),
    ]


def available() -> bool:
    """Windows 8+ supports nested jobs; real permissions are checked on use."""
    return os.name == "nt" and sys.platform == "win32"


def _kernel():
    if not available():
        raise JobUnavailable("Windows Job Objects są niedostępne na tym systemie.")
    try:
        lib = ctypes.WinDLL("kernel32", use_last_error=True)
        definitions = [
            ("CreateJobObjectW", ctypes.c_void_p, [ctypes.c_void_p, wintypes.LPCWSTR]),
            ("SetInformationJobObject", wintypes.BOOL,
             [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]),
            ("QueryInformationJobObject", wintypes.BOOL,
             [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p,
              wintypes.DWORD, ctypes.c_void_p]),
            ("OpenProcess", ctypes.c_void_p,
             [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]),
            ("AssignProcessToJobObject", wintypes.BOOL,
             [ctypes.c_void_p, ctypes.c_void_p]),
            ("CloseHandle", wintypes.BOOL, [ctypes.c_void_p]),
        ]
        for name, result_type, arguments in definitions:
            fn = getattr(lib, name)
            fn.restype = result_type
            fn.argtypes = arguments
        return lib
    except (AttributeError, OSError) as exc:
        raise JobUnavailable("Nie można załadować interfejsu Windows Job Objects.") from exc


def _error(phase: str) -> JobUnavailable:
    # The function is also exercised with simulated Win32 APIs on Linux CI.
    code = ctypes.get_last_error() if hasattr(ctypes, "get_last_error") else 0
    return JobUnavailable(f"{phase}: Windows error {code}.")


class ProcessJob:
    def __init__(self, handle: int, kernel):
        self._handle = handle
        self._kernel = kernel

    @classmethod
    def create(cls, memory_mb: int) -> "ProcessJob":
        if type(memory_mb) is not int or not MIN_MEMORY_MB <= memory_mb <= MAX_MEMORY_MB:
            raise ValueError("Niepoprawny łączny limit pamięci Windows Job Object.")
        lib = _kernel()
        handle = lib.CreateJobObjectW(None, None)
        if not handle:
            raise _error("CreateJobObjectW")
        try:
            info = ExtendedLimitInformation()
            info.BasicLimitInformation.LimitFlags = (
                JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
            )
            info.JobMemoryLimit = memory_mb * 1024 * 1024
            if not lib.SetInformationJobObject(
                handle, JOB_OBJECT_EXTENDED_LIMIT_INFORMATION,
                ctypes.byref(info), ctypes.sizeof(info),
            ):
                raise _error("SetInformationJobObject")
            checked = ExtendedLimitInformation()
            if not lib.QueryInformationJobObject(
                handle, JOB_OBJECT_EXTENDED_LIMIT_INFORMATION,
                ctypes.byref(checked), ctypes.sizeof(checked), None,
            ):
                raise _error("QueryInformationJobObject")
            if (checked.JobMemoryLimit != info.JobMemoryLimit or
                    checked.BasicLimitInformation.LimitFlags &
                    (JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE)
                    != (JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE)):
                raise JobUnavailable("Windows nie przyjął wymaganych ograniczeń Job Object.")
            return cls(handle, lib)
        except Exception:
            lib.CloseHandle(handle)
            raise

    def start(self, process) -> None:
        """Attach blocked helper to the job, THEN unblock its toolchain launch."""
        proc = self._kernel.OpenProcess(
            PROCESS_SET_QUOTA | PROCESS_TERMINATE, False, process.pid
        )
        if not proc:
            raise _error("OpenProcess")
        try:
            if not self._kernel.AssignProcessToJobObject(self._handle, proc):
                raise _error("AssignProcessToJobObject")
        finally:
            self._kernel.CloseHandle(proc)
        if process.stdin is None:
            raise JobUnavailable("Windows launcher nie ma kanału synchronizacji.")
        try:
            process.stdin.write(b"START\n")
            process.stdin.flush()
            process.stdin.close()
        except OSError as exc:
            raise JobUnavailable("Nie można odblokować kompilatora po przypisaniu do Job Object.") from exc

    def active_processes(self) -> int:
        info = BasicAccountingInformation()
        if not self._kernel.QueryInformationJobObject(
            self._handle, JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION,
            ctypes.byref(info), ctypes.sizeof(info), None,
        ):
            raise _error("QueryInformationJobObject(accounting)")
        return info.ActiveProcesses

    def kill_and_close(self) -> bool:
        """Closing the last handle kills all job members, including descendants."""
        if not self._handle:
            return False
        handle, self._handle = self._handle, None
        try:
            active = self.active_processes_for(handle)
        finally:
            if not self._kernel.CloseHandle(handle):
                raise _error("CloseHandle(Job)")
        return active > 0

    def active_processes_for(self, handle: int) -> int:
        info = BasicAccountingInformation()
        if not self._kernel.QueryInformationJobObject(
            handle, JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION,
            ctypes.byref(info), ctypes.sizeof(info), None,
        ):
            raise _error("QueryInformationJobObject(accounting)")
        return info.ActiveProcesses
