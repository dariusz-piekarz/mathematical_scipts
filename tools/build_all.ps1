# Compile every Polish-language LaTeX book in its own working directory.
$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$books = Join-Path $root "books\pl"
Get-ChildItem -Path $books -File -Filter "*.tex" | ForEach-Object {
    Push-Location $books
    try {
        Write-Host "Compiling book $($_.Name)"
        & latexmk -pdf -interaction=nonstopmode -file-line-error -halt-on-error $_.Name
        if ($LASTEXITCODE -ne 0) { throw "Compilation failed: $($_.Name)" }
    } finally { Pop-Location }
}
