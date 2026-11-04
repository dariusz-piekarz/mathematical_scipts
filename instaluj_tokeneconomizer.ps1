param(
    [switch]$StartCodex
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

# This checkout stays outside the LaTeX repository because Codex loads it later.
$upstream = 'https://github.com/microsoft/TokenEconomizer.git'
$commit = 'd3e193b8734ec76230da1e08d7929ba9d14640d8'
$pythonVersion = '3.14.8'
$uvBin = Join-Path $env:USERPROFILE '.local\bin'
$pythonExe = Join-Path $uvBin 'python.exe'
$checkout = Join-Path $env:LOCALAPPDATA ('TokenEconomizer\source-' + $commit.Substring(0, 12))

function Invoke-Checked {
    param([string]$Executable, [string[]]$Arguments)
    & $Executable @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Executable failed with exit code $LASTEXITCODE"
    }
}

foreach ($name in @('uv.exe', 'git.exe', 'codex.exe')) {
    if (-not (Get-Command $name -ErrorAction SilentlyContinue)) {
        throw "$name is required on PATH"
    }
}

# --default creates python.exe, which TokenEconomizer's Windows Codex hooks use.
Invoke-Checked 'uv.exe' @('python', 'install', $pythonVersion, '--default')
if (-not (Test-Path -LiteralPath $pythonExe -PathType Leaf)) {
    throw "uv did not create $pythonExe"
}
$pythonWithoutPrefix = Get-Command python.exe -ErrorAction SilentlyContinue

# Keep the user's other PATH entries intact. The process prefix is necessary on
# machines where the Microsoft Store alias in Machine PATH precedes User PATH.
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$entries = @($userPath -split ';' | Where-Object { $_ })
if (-not @($entries | Where-Object { $_.TrimEnd('\') -ieq $uvBin.TrimEnd('\') }).Count) {
    [Environment]::SetEnvironmentVariable('Path', "$uvBin;$userPath", 'User')
}
$env:Path = "$uvBin;$env:Path"
$resolvedPython = (Get-Command python.exe -ErrorAction Stop).Source
if ($resolvedPython -ine $pythonExe) {
    throw "python.exe resolves to $resolvedPython instead of $pythonExe"
}
Invoke-Checked 'python.exe' @('-c', 'import sys; assert sys.version_info >= (3, 10); print(sys.executable, sys.version.split()[0])')

if ($StartCodex) {
    Write-Host 'Starting Codex with uv Python first on PATH.'
    & codex.exe
    return
}

if (-not (Test-Path -LiteralPath $checkout)) {
    New-Item -ItemType Directory -Path (Split-Path -Parent $checkout) -Force | Out-Null
    Invoke-Checked 'git.exe' @('clone', $upstream, $checkout)
}
if (-not (Test-Path -LiteralPath (Join-Path $checkout '.git'))) {
    throw "$checkout exists but is not a Git checkout"
}
$remote = (& git.exe -C $checkout remote get-url origin).Trim()
if ($LASTEXITCODE -ne 0 -or $remote -ne $upstream) {
    throw "Unexpected origin in $checkout`: $remote"
}
$dirty = @(& git.exe -C $checkout status --porcelain)
if ($LASTEXITCODE -ne 0 -or $dirty.Count -gt 0) {
    throw "Checkout has local changes: $checkout"
}
$head = (& git.exe -C $checkout rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) {
    throw "Cannot read HEAD in $checkout"
}
if ($head -ne $commit) {
    Invoke-Checked 'git.exe' @('-C', $checkout, 'checkout', '--detach', $commit)
}
$head = (& git.exe -C $checkout rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0 -or $head -ne $commit) {
    throw "Expected TokenEconomizer commit $commit, got $head"
}

$marketplaces = @(& codex.exe plugin marketplace list)
if ($LASTEXITCODE -ne 0) {
    throw 'Cannot list Codex plugin marketplaces'
}
$registered = @($marketplaces | Where-Object { $_ -match '^tokeneconomizer\s+' })
if ($registered.Count -eq 0) {
    Invoke-Checked 'codex.exe' @('plugin', 'marketplace', 'add', $checkout.Replace('\', '/'))
} elseif ($registered.Count -ne 1 -or $registered[0] -notmatch [regex]::Escape($checkout)) {
    throw "A different tokeneconomizer marketplace is already registered: $($registered -join '; ')"
}
Invoke-Checked 'codex.exe' @('plugin', 'add', 'tokeneconomizer@tokeneconomizer')

$installed = @(& codex.exe plugin list | Where-Object { $_ -match '^tokeneconomizer@tokeneconomizer\s+' })
if ($LASTEXITCODE -ne 0 -or $installed.Count -ne 1) {
    throw 'Codex did not report tokeneconomizer@tokeneconomizer as installed'
}
Write-Host "Pinned upstream commit: $head"
Write-Host "Checkout: $checkout"
Write-Host "Codex: $(& codex.exe --version)"
Write-Host "Plugin: $($installed[0].Trim())"
Write-Host 'Next: start a new Codex CLI session in this repository, review and trust the hooks, exit, then start another session and run $tokeneconomizer:status.'
Write-Host 'For CLI sessions on this Windows setup, use: .\instaluj_tokeneconomizer.ps1 -StartCodex'
if ($null -eq $pythonWithoutPrefix -or $pythonWithoutPrefix.Source -ine $pythonExe) {
    Write-Warning 'A regular new process may still find the Microsoft Store python alias first in Machine PATH. Use -StartCodex for CLI sessions; this script does not edit Machine PATH or disable aliases.'
}
Write-Host 'The current IDE session cannot be verified by this installer.'
