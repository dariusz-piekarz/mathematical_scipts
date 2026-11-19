$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
python -m pip install -r requirements.txt
# The GitHub checkout uses ../chapters/pl; refresh its SQLite index first.
if (Test-Path '..\chapters\pl') {
    python backend/latex_parser.py index --source '..\chapters\pl' --recursive --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json --report data/index_report_iteration_6.json
    if ($LASTEXITCODE -notin @(0,2)) { throw "Index generation failed: $LASTEXITCODE" }
}
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
