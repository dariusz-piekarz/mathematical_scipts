#!/usr/bin/env bash
# CI-only bootstrap in a transient, delegated service. Never reconfigure the host root.
set -euo pipefail
test "$(id -u)" -ne 0
relative="$(awk -F: '$1=="0" && $2=="" {print $3}' /proc/self/cgroup)"
case "$relative" in
  /system.slice/atlas-lean-cgroup-*.service) ;;
  *) echo "Refusing unexpected cgroup: $relative" >&2; exit 1 ;;
esac
parent="/sys/fs/cgroup$relative"
grep -qw memory "$parent/cgroup.controllers"
mkdir "$parent/client"
echo "$$" > "$parent/client/cgroup.procs"
echo '+memory' > "$parent/cgroup.subtree_control"
export MATLIB_LEAN_CGROUP_PARENT="$parent"
exec "$1" -c 'import sys, unittest
suite = unittest.defaultTestLoader.loadTestsFromName("tests.test_lean_cgroup.LeanCgroupTests.test_real_cgroup_is_used_when_delegated")
result = unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(0 if result.wasSuccessful() and result.testsRun == 1 and not result.skipped else 1)'
