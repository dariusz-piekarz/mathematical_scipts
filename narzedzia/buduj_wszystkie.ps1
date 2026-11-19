$ErrorActionPreference = "Continue"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location (Join-Path $root "skrypty")
try {
  Get-ChildItem -File -Filter "*.tex" | ForEach-Object {
    Write-Host "Kompiluję $($_.Name)"
    & latexmk -pdf -interaction=nonstopmode -file-line-error $_.Name
    if ($LASTEXITCODE -ne 0) { Write-Warning "Błąd kompilacji: $($_.Name)" }
  }
} finally { Pop-Location }
