$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $root
try {
    $source = 'rozdzialy'
    if (!(Test-Path $source)) { $source = '..\rozdzialy' }
    python backend/latex_parser.py index --source $source --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json --report data/indeksowanie_raport.json
    if ($LASTEXITCODE -ne 0) { throw "Indeksowanie nie przeszlo kontroli. Exit code: $LASTEXITCODE" }
    python -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { throw "Testy nie przeszly. Exit code: $LASTEXITCODE" }
}
finally { Pop-Location }
