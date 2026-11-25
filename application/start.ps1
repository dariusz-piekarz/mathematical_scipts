param([switch]$NoBrowser)

$ErrorActionPreference = 'Stop'
$python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
$url = 'http://127.0.0.1:8765/'
Push-Location $PSScriptRoot
try {
    # Do not rebuild the database while another instance is reading it.
    $listener = New-Object System.Net.Sockets.TcpClient
    $portInUse = $false
    try { $listener.Connect('127.0.0.1', 8765); $portInUse = $true } catch { } finally { $listener.Dispose() }
    if ($portInUse) {
        $existingApi = $null
        try { $existingApi = Invoke-RestMethod ($url + 'openapi.json') -TimeoutSec 5 } catch { }
        if ($existingApi.info.title -like 'Biblioteka*API') {
            Write-Host "Atlas is already running: $url"
            if (-not $NoBrowser) { Start-Process $url }
            return
        }
        throw "Port 8765 is already in use. Open $url or stop the existing server before restarting."
    }
    # Never install into a global Python (uv-managed installations forbid it).
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        if (-not (Test-Path $python)) {
            uv venv .venv
            if ($LASTEXITCODE -ne 0) { throw "Could not create .venv (uv exit code $LASTEXITCODE)." }
        }
        uv pip install --python $python -r requirements.txt
    } else {
        if (-not (Test-Path $python)) {
            if (Get-Command python -ErrorAction SilentlyContinue) {
                python -m venv .venv
            } elseif (Get-Command py -ErrorAction SilentlyContinue) {
                py -3 -m venv .venv
            } else {
                throw 'Install Python 3.10+ or uv, then run start.cmd again.'
            }
            if ($LASTEXITCODE -ne 0) { throw "Could not create .venv (exit code $LASTEXITCODE)." }
        }
        & $python -m pip --version *> $null
        if ($LASTEXITCODE -ne 0) {
            & $python -m ensurepip --upgrade
            if ($LASTEXITCODE -ne 0) { throw 'Could not install pip in .venv.' }
        }
        & $python -m pip install -r requirements.txt
    }
    if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed: $LASTEXITCODE" }

    & $python scripts/install_math_renderer.py
    if ($LASTEXITCODE -ne 0) { Write-Warning 'Math renderer unavailable; source view remains available.' }
    # The GitHub checkout uses ../chapters/pl; refresh its SQLite index first.
    if (Test-Path '..\chapters\pl') {
        & $python backend/latex_parser.py index --source '..\chapters\pl' --recursive --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json --report data/index_report_iteration_6.json
        if ($LASTEXITCODE -notin @(0,2)) { throw "Index generation failed: $LASTEXITCODE" }
    }
    Write-Host "Starting Atlas: $url (close the last browser tab to stop)"
    $launchArgs = @('-m', 'backend.desktop')
    if ($NoBrowser) { $launchArgs += '--no-browser' }
    & $python @launchArgs
    if ($LASTEXITCODE -ne 0) { throw "Server stopped with exit code $LASTEXITCODE" }
} finally {
    Pop-Location
}
