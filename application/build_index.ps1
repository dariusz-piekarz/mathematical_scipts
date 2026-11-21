$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $root
try {
    $source = 'rozdzialy'
    $recursive = @()
    if (Test-Path '..\chapters\pl') {
        $source = '..\chapters\pl'
        $recursive = @('--recursive')
    }
    elseif (!(Test-Path $source) -and (Test-Path '..\rozdzialy')) {
        $source = '..\rozdzialy'
    }
    python backend/latex_parser.py index --source $source @recursive --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json --report data/index_report_iteration_6.json
    if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 2) { throw "Indexing failed: $LASTEXITCODE" }
    Write-Host 'Index rebuilt. Check data/index_report_iteration_6.json for unresolved or ambiguous references.'
    python -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { throw "Tests failed: $LASTEXITCODE" }
}
finally { Pop-Location }
