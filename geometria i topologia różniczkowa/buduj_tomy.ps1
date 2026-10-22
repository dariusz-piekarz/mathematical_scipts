$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$perlGit = 'C:\Program Files\Git\usr\bin'
if (-not (Get-Command perl -ErrorAction SilentlyContinue) -and
    (Test-Path -LiteralPath (Join-Path $perlGit 'perl.exe'))) {
    $env:PATH = "$perlGit;$env:PATH"
}

$buildDir = 'build/tomy'
$volumes = @('geometria_tom1', 'geometria_tom2', 'geometria_tom3')
New-Item -ItemType Directory -Path $buildDir -Force | Out-Null

function Get-AuxHashes {
    foreach ($volume in $volumes) {
        $aux = Join-Path $buildDir "$volume.aux"
        if (Test-Path -LiteralPath $aux) {
            (Get-FileHash -LiteralPath $aux -Algorithm SHA256).Hash
        } else {
            ''
        }
    }
}

$stable = $false
for ($round = 1; $round -le 4; $round++) {
    $before = @(Get-AuxHashes)
    foreach ($volume in $volumes) {
        Write-Host "Przebieg $round`: $volume"
        $transcript = Join-Path $buildDir "$volume-latexmk.txt"
        $previousErrorAction = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        & latexmk -pdf -interaction=nonstopmode -halt-on-error `
            -file-line-error "-outdir=$buildDir" "$volume.tex" *> $transcript
        $buildExitCode = $LASTEXITCODE
        $ErrorActionPreference = $previousErrorAction
        if ($buildExitCode -ne 0) {
            Get-Content -LiteralPath $transcript -Tail 35
            throw "Build failed for $volume."
        }
    }
    $after = @(Get-AuxHashes)
    if ($round -ge 2 -and ($before -join ',') -eq ($after -join ',')) {
        $stable = $true
        break
    }
}

if (-not $stable) {
    throw 'Cross-volume references did not stabilize after four rounds.'
}

foreach ($volume in $volumes) {
    $log = Join-Path $buildDir "$volume.log"
    $indexLog = Join-Path $buildDir "$volume.ilg"
    if (Select-String -LiteralPath $log -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed' -Quiet) {
        throw "Unresolved references in $log."
    }
    if (-not (Select-String -LiteralPath $indexLog -Pattern '0 rejected' -Quiet)) {
        throw "Check the index in $indexLog."
    }
    Copy-Item -LiteralPath (Join-Path $buildDir "$volume.pdf") `
        -Destination "$volume.pdf" -Force
}

Write-Host 'Three volumes built, indexes checked, PDFs copied.'
