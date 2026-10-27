# Manual pracy w repozytorium `mathematical_scipts`

Ten plik zapisuje odtwarzalne polecenia środowiska, budowania i kontroli.
Polecenia faktycznie wykonane są oddzielone od instrukcji przygotowanych
do późniejszego użycia.

## Projekt „Geometria i topologia różniczkowa”

Od 27 października 2026 bieżący skład ma cztery tomy:
I (rozdziały 1--10), II (11--22), III (23--30) i IV (31--38
oraz dodatki). Starsze wpisy poniżej dokumentują rzeczywiście
wykonane wówczas polecenia dla dawnego podziału na trzy tomy;
ich numery stron i nazwy PDF-ów są historyczne.

### Katalog roboczy

W PowerShell przejdź do katalogu projektu:

```powershell
Set-Location -LiteralPath 'C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa'
```

Wszystkie poniższe polecenia budowania zakładają ten katalog roboczy.
Wyniki pomocnicze trafiają do `build/tomy`, a sprawdzone PDF-y są
kopiowane do katalogu projektu.

### Sprawdzone środowisko

Audyt dodatków A i B z 25 października 2026 wykonano w następującym
środowisku:

- Windows PowerShell 5.1.19041.6456;
- MiKTeX 25.12 i MiKTeX-pdfTeX 4.23;
- `latexmk` 4.88;
- `makeindex` z MiKTeX 25.12;
- Perl 5.42.3 z Git for Windows;
- Git 2.55.0.windows.5;
- ripgrep 15.2.0.

Są to wersje, na których wykonano i zweryfikowano skład; projekt nie
wyznacza obecnie odrębnych wersji minimalnych.

Skrypt `buduj_tomy.ps1` sam dodaje `C:\Program Files\Git\usr\bin`
do `PATH`, jeżeli polecenie `perl` nie jest już dostępne. Przy użyciu
skryptu nie są wymagane żadne projektowe zmienne środowiskowe.

### Przygotowanie czystego stanowiska — instrukcje niewykonane w audycie

Poniższe polecenia są procedurą dla nowego komputera. Nie wykonywano ich
25 października 2026, ponieważ wymienione wyżej narzędzia były już
zainstalowane. Projekt nie ma ustalonych wersji minimalnych; do powtórzenia
sprawdzonego środowiska należy użyć wersji z poprzedniej sekcji, a poniższe
polecenia bez `--version` instalują bieżące wydania z `winget`.

Zainstaluj Git for Windows, dostarczający również Perl, MiKTeX oraz
`ripgrep` używany do kontroli logów:

```powershell
winget install --exact --id Git.Git --source winget
winget install --exact --id MiKTeX.MiKTeX --source winget
winget install --exact --id BurntSushi.ripgrep.MSVC --source winget
```

Po ponownym otwarciu PowerShell dokończ inicjalizację MiKTeX-a, odśwież
bazę nazw plików i bazę pakietów. Polecenie `miktexsetup finish` jest
potrzebne tylko wtedy, gdy narzędzie zgłasza `fresh TeX installation`:

```powershell
miktexsetup finish
initexmf --update-fndb
mpm --update-db
```

Zainstaluj pakiety użyte w `tex/preambula.tex` oraz narzędzia składu.
Instalacja MiKTeX dla wszystkich użytkowników wymaga uruchomienia tych
poleceń w podniesionym PowerShell i dodania opcji `--admin` do `initexmf`
oraz `mpm`; dla instalacji użytkownika użyj poleceń dokładnie jak poniżej:

```powershell
$projectPackages = @(
  'amscls', 'amsfonts', 'amsmath', 'babel-polish', 'enumitem',
  'fancyhdr', 'float', 'geometry', 'hyperref', 'latexmk', 'lmodern',
  'makeindex', 'mathtools', 'microtype', 'pgf', 'pgfplots', 'tikz-cd',
  'tools', 'xcolor', 'xr-hyper'
)
foreach ($projectPackage in $projectPackages) {
  mpm --install=$projectPackage
}
```

Pobierz repozytorium; projekt nie wymaga osobnego zestawu danych:

```powershell
git clone https://github.com/dariusz-piekarz/mathematical_scipts.git
Set-Location -LiteralPath '.\mathematical_scipts\geometria i topologia różniczkowa'
git switch review/rozdzialy-matematyka
git pull --ff-only
```

### Polecenia faktycznie wykonane 25 października 2026

Przed zmianami pobrano stan gałęzi bez tworzenia merge commita:

```powershell
git pull --ff-only
```

Pełny skład wszystkich tomów, stabilizacja odsyłaczy, wykonanie indeksów
i skopiowanie PDF-ów:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Skrypt zakończył się po dwóch przebiegach. Wynik: tomy mają odpowiednio
216, 182 i 171 stron; indeksy przyjęły 113, 96 i 119 haseł oraz odrzuciły
zero wpisów.

Kontrola logów została wykonana poleceniem równoważnym poniższemu:

```powershell
rg -n -i 'undefined|multiply defined|overfull|underfull|missing character|fatal error|emergency stop|LaTeX Warning|Package .* Warning|pdfTeX warning' .\build\tomy -g '*.log'
```

Nie znaleziono brakujących odsyłaczy, `Overfull`, brakujących znaków ani
błędów składu. Pozostały wcześniejsze ostrzeżenia `Underfull` i po jednym
powtórzonym celu `page.1` na tom, a w tomie I dwa ostrzeżenia o zmianie
specyfikatora położenia rysunku z `h` na `ht`.

Liczby stron sprawdzono przez `pdfinfo`, a strony dodatków A i B
wyrenderowano i odczytano poleceniami:

```powershell
pdfinfo .\geometria_tom3.pdf
pdftoppm -f 150 -l 159 -png -r 110 .\geometria_tom3.pdf .\build\audit-ab-20261025\page
pdftotext -f 150 -l 159 -layout .\geometria_tom3.pdf .\build\audit-ab-20261025\appendices-ab-final.txt
pdftohtml -f 150 -l 159 -xml -hidden -nodrm .\geometria_tom3.pdf .\build\audit-ab-20261025\links\ab.xml
```

Polecenia `pdftotext` i `pdftohtml` powtórzono na finalnym PDF-ie po
ostatniej zmianie źródeł. Kontrola XML potwierdziła odsyłacze międzytomowe do
`geometria_tom1.pdf` i `geometria_tom2.pdf`. Obejrzano fizyczne strony
PDF 150–159, czyli strony drukowane 149–158.

### Instrukcje przygotowane do samodzielnego wykonania

Jeśli `latexmk` jest uruchamiany bezpośrednio zamiast przez skrypt,
a MiKTeX nie znajduje Perla, ustaw `PATH` tylko w bieżącej sesji:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
```

Doraźny skład jednego tomu, nieużyty w tym audycie:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom3.tex
```

Przed publikacją zawsze uruchom jednak pełny `buduj_tomy.ps1`, ponieważ
numery i cele odsyłaczy są współdzielone między tomami.

Opcjonalny skład całej książki do jednego PDF-u, również niewykonany
w tym audycie:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/sklad geometria_i_topologia_rozniczkowa.tex
```

Projekt nie pobiera danych wejściowych z sieci. MiKTeX musi mieć
zainstalowane pakiety użyte w `tex/preambula.tex`; w sprawdzonym
środowisku wszystkie były już dostępne.

## Audyt rozdziału 35 — polecenia wykonane 26 października 2026

Pracę rozpoczęto w katalogu głównym repozytorium i pobrano stan gałęzi
bez tworzenia merge commita:

```powershell
Set-Location -LiteralPath 'C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts'
git pull --ff-only
```

Polecenie zakończyło się komunikatem `Already up to date.`. Następnie
przejście do projektu i pełny skład wszystkich tomów wykonano poleceniami:

```powershell
Set-Location -LiteralPath '.\geometria i topologia różniczkowa'
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Skrypt zakończył dwa przebiegi, ustabilizował odsyłacze, sprawdził indeksy
i skopiował PDF-y z `build/tomy` do katalogu projektu. Sumy SHA-256 każdej
pary plików źródłowego i skopiowanego były identyczne. Tomy mają 216, 182
i 173 strony. `makeindex` przyjął 113, 96 i 119 haseł, odrzucił zero
i nie zgłosił ostrzeżeń.

Logi skontrolowano poleceniem:

```powershell
rg -n -i 'undefined|multiply defined|overfull|underfull|missing character|fatal error|emergency stop|LaTeX Warning|Package .* Warning|pdfTeX warning' .\build\tomy -g '*.log'
```

Nie znaleziono błędów, niezdefiniowanych odsyłaczy, `Overfull` ani
brakujących znaków. Pozostały znane ostrzeżenia `Underfull` poza
rozdziałem 35, powtórzony cel `page.1` w każdym tomie oraz dwa ostrzeżenia
tomu I o zmianie specyfikatora rysunku z `h` na `ht`.

Liczby stron sprawdzono przez `pdfinfo`. Cały rozdział 35 wyodrębniono
z finalnego tomu III, wyrenderowano i odczytano poleceniami:

```powershell
New-Item -ItemType Directory -Force .\build\audit-ch35-20261026
pdfinfo .\geometria_tom1.pdf
pdfinfo .\geometria_tom2.pdf
pdfinfo .\geometria_tom3.pdf
pdftotext -f 131 -l 137 -layout .\geometria_tom3.pdf .\build\audit-ch35-20261026\chapter35.txt
pdftoppm -f 131 -l 137 -png -r 110 .\geometria_tom3.pdf .\build\audit-ch35-20261026\page
pdftohtml -f 131 -l 137 -xml -hidden -nodrm .\geometria_tom3.pdf .\build\audit-ch35-20261026\chapter35.xml
git diff --check
```

Obejrzano fizyczne strony PDF 131--137, czyli strony drukowane 130--136.
Strona 138 rozpoczyna rozdział 36. Nie pobierano danych projektu ani nowych
zależności; źródła matematyczne sprawdzano w publikacjach podlinkowanych
w rozdziale.

## Audyt rozdziału 34 — polecenia wykonane 25 października 2026

Pracę wykonano w katalogu:

```powershell
Set-Location -LiteralPath '.\geometria i topologia różniczkowa'
```

Przed zmianami pobrano stan gałęzi bez tworzenia merge commita:

```powershell
git pull --ff-only
```

Pierwsza próba `buduj_tomy.ps1` ujawniła, że profil MiKTeX 25.12 nie miał
dokończonej inicjalizacji. Wykonano więc następujące polecenia konfiguracji
istniejącej instalacji użytkownika (nie instalowano nowych pakietów):

```powershell
initexmf --update-fndb
initexmf --mkmaps
initexmf --mklangs
initexmf --report
```

Raport po inicjalizacji wskazał MiKTeX 25.12 i datę konfiguracji
2 października 2026. `latexmk` wymagał Perla dostępnego w instalacji Git,
dlatego w sesji użytej do końcowego składu rozszerzono `PATH` i uruchomiono
pełny skrypt:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Skrypt zakończył dwa przebiegi, sprawdził indeksy i skopiował PDF-y. Tomy
mają 216, 182 i 172 strony. `makeindex` przyjął odpowiednio 113, 96 i 119
haseł, odrzucił zero i nie zgłosił ostrzeżeń.

Logi sprawdzono poleceniem:

```powershell
rg -n -i 'undefined|multiply defined|overfull|underfull|missing character|fatal error|emergency stop|LaTeX Warning|Package .* Warning|pdfTeX warning' .\build\tomy -g '*.log'
```

Nie znaleziono błędów, niezdefiniowanych odsyłaczy, `Overfull` ani
brakujących znaków. Pozostały znane komunikaty `Underfull`, powtórzony cel
`page.1` w każdym tomie oraz dwa ostrzeżenia tomu I o zmianie położenia
rysunku z `h` na `ht`; żaden nie dotyczy rozdziału 34.

Cały rozdział 34 wyodrębniono i wyrenderowano z finalnego tomu III:

```powershell
pdftotext -f 125 -l 131 -layout .\geometria_tom3.pdf .\build\audit-ch34-20261025\chapter34.txt
pdftoppm -f 125 -l 131 -png -r 110 .\geometria_tom3.pdf .\build\audit-ch34-20261025\page
pdftohtml -f 125 -l 130 -xml -hidden -nodrm .\geometria_tom3.pdf .\build\audit-ch34-20261025\chapter34.xml
```

Obejrzano fizyczne strony PDF 125--130 (drukowane 124--129). Strona 131
posłużyła tylko do potwierdzenia granicy z rozdziałem 35; jego treści nie
audytowano. XML potwierdził poprawne cele nowych i sąsiednich odsyłaczy.

## Audyty rozdziałów 36–38 i podział na cztery tomy — 27 października 2026

Pracę prowadzono na gałęzi `review/rozdzialy-matematyka`.
Przed zmianami w katalogu głównym repozytorium wykonano:

```powershell
git fetch origin
git pull --ff-only origin review/rozdzialy-matematyka
```

Gałąź była aktualna. Katalog składu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie pobierano danych projektu ani nowych zależności. Użyto
istniejącego środowiska opisanego wyżej; skrypt sam znajduje
Perl dostarczony z Git for Windows. Po podziale źródeł
uruchomiono pełny skład czterech tomów:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Wcześniejsze niedokończone przebiegi składu trzech tomów nie są
podstawą poniższych wniosków. Aktualny skrypt składa kolejno
`geometria_tom1.tex`--`geometria_tom4.tex` w `build/tomy`,
sprawdza cztery indeksy i kopiuje PDF-y do katalogu projektu.

Skrypt zakończył dwa przebiegi. Wyniki końcowe I--IV mają
216, 182, 97 i 80 stron. `makeindex` przyjął odpowiednio
113, 96, 26 i 93 hasła, odrzucił zero i nie zgłosił ostrzeżeń.
Kontrolę logów, stron i zgodności skopiowanych PDF-ów wykonano
w katalogu geometrii poleceniami:

```powershell
rg -n -i 'undefined|multiply defined|overfull|missing character|fatal error|emergency stop' build/tomy -g '*.log'
rg -n -i 'underfull|pdfTeX warning|LaTeX Warning|Package .* Warning' build/tomy -g '*.log'
foreach ($n in 1..4) {
  $name = "geometria_tom$n.pdf"
  $root = Get-FileHash -Algorithm SHA256 -LiteralPath $name
  $built = Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path 'build/tomy' $name)
  $pages = pdfinfo $name | Select-String -Pattern '^Pages:'
  "$name  $($pages.Line.Trim())  hashes_match=$($root.Hash -eq $built.Hash)"
}
foreach ($n in 1..4) {
  Get-Content -Encoding utf8 "build/tomy/geometria_tom$n.ilg" -Tail 6
}
```

Pierwszy `rg` nie znalazł dopasowań; drugi pokazał znane
ostrzeżenia `Underfull`, powtórzony cel `page.1` w każdym
tomie oraz dwa ostrzeżenia tomu I o zmianie `h` na `ht`.
Hashe czterech par plików są równe. Spisy zweryfikowano
w `build/tomy/geometria_tom3.toc` i `geometria_tom4.toc`:
tom III kończy się rozdziałem 30, a IV zaczyna rozdziałem 31
i częścią IV; następne rozdziały mają numery 32--38.

Po końcowym składzie wykonano kontrolę stron i linków:

```powershell
$auditDir = Join-Path $env:TEMP 'geometry-split-final-20261027'
New-Item -ItemType Directory -Force -Path $auditDir | Out-Null
pdftoppm -f 1 -l 1 -png -r 100 geometria_tom3.pdf (Join-Path $auditDir 'tom3')
pdftoppm -f 97 -l 97 -png -r 100 geometria_tom3.pdf (Join-Path $auditDir 'tom3')
pdftoppm -f 56 -l 56 -png -r 100 geometria_tom4.pdf (Join-Path $auditDir 'tom4')
pdftotext -f 51 -l 57 -layout geometria_tom4.pdf -
foreach ($n in 1..4) {
  $pdf = "geometria_tom$n.pdf"
  $xml = Join-Path $auditDir "tom$n-title-links.xml"
  pdftohtml -f 1 -l 1 -xml -hidden -nodrm $pdf $xml | Out-Null
}
git diff --check
```

Ponadto wyrenderowano i obejrzano wybrane strony 44--57 tomu IV,
w tym początki rozdziałów 36--38, nowe obliczenie kraty i rysunek.
XML stron tytułowych potwierdził z każdego tomu łącza do trzech
pozostałych PDF-ów; XML stron 44--56 tomu IV pokazał także
odsyłacze z treści do tomu II. Tekst PDF zawiera cytat do
twierdzeń 9.6--9.7 Freedmana--Quinna i jawną bazę $-E_8$.
Żadna instrukcja instalacji z początku pliku nie była wykonywana
w tym etapie. Do powtórzenia na nowym stanowisku zastosuj tamte
instrukcje, przejdź do katalogu geometrii i uruchom wskazane
wyżej polecenie `buduj_tomy.ps1`.

## Skrypt Banacha--Tarskiego — polecenia wykonane 27 października 2026

Katalog roboczy: `C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\banach_tarski`.
Źródłem jest `banach_tarski_przepisany.tex`, a wynikiem
`banach_tarski_przepisany.pdf`. Skład sprawdzono w tym samym
środowisku MiKTeX 25.12, pdfTeX 4.23 i `latexmk` 4.88, które opisano
wyżej. Wymagany jest Perl z Git for Windows 2.55.0.windows.5;
żadnych danych ani zależności nie pobierano w tej iteracji.
Na własnym stanowisku przejdź do tego katalogu poleceniem
przygotowanym do powtórzenia (agent ustawiał katalog roboczy
bezpośrednio):

```powershell
Set-Location -LiteralPath 'C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\banach_tarski'
```

Pierwsze wywołanie `latexmk` nie uruchomiło składu, ponieważ Perl
nie był w `PATH`. Wykonano więc poniższe polecenia w katalogu
skryptu; pierwsza udana kompilacja odbyła się bez `-silent`, a
końcowa, powtórzona kompilacja z `-silent`:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error banach_tarski_przepisany.tex
latexmk -pdf -silent -interaction=nonstopmode -halt-on-error -file-line-error banach_tarski_przepisany.tex
```

Zmiana `PATH` dotyczyła tylko bieżącej sesji PowerShell. Ostatni
skład zakończył się po dwóch przebiegach i dał 19-stronicowy PDF A4
o wielkości 471361 bajtów. Wykonane kontrole:

```powershell
rg -n 'Overfull|Underfull|LaTeX Warning|Package .* Warning|Undefined control|Emergency stop|Output written' banach_tarski_przepisany.log
pdfinfo banach_tarski_przepisany.pdf | Select-String -Pattern 'Pages:|Page size:|File size:|PDF version:'
$out = Join-Path $env:TEMP 'bt_audit_page_1'
pdftoppm -f 1 -l 1 -singlefile -scale-to 1300 -png banach_tarski_przepisany.pdf $out
pdftotext -f 1 -l 2 -layout banach_tarski_przepisany.pdf -
pdftotext -f 19 -l 19 -layout banach_tarski_przepisany.pdf -
git diff --check
```

Render powtórzono ze zmienionymi numerami `-f`, `-l` i nazwą pliku
dla stron 2, 11, 18 i 19. Obejrzano strony 1, 2, 11, 18 i 19;
log zawiera wyłącznie komunikat `Output written`, bez ostrzeżeń.

### Instrukcja przygotowana do samodzielnego wykonania

Na nowym stanowisku zastosuj instrukcję instalacji MiKTeX i Git
z początku tego pliku. Do skryptu są potrzebne pakiety LaTeX:
`amsmath`, `amssymb`, `amsthm`, `mathtools`, `lmodern`, `microtype`,
`xcolor`, `geometry`, `enumitem`, `fancyhdr`, `hyperref` oraz polski
`babel`. Polecenia instalacji tych pakietów w ramach tego audytu
nie były wykonywane, ponieważ były już dostępne. Po przejściu do
katalogu `banach_tarski` ustaw `PATH` i uruchom końcową komendę
`latexmk` z bloku powyżej.

## Skrypt „Teoria modeli” — polecenia wykonane 27 października 2026

Katalog roboczy: `C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\teoria modeli`.
Źródłem jest `teoria modeli.tex`, a wynikiem `teoria modeli.pdf`.
Skład wykonano w MiKTeX 25.12 i pdfTeX 4.23 z już zainstalowanymi
pakietami. Nie pobierano danych ani zależności. Próba `latexmk`
przed ustawieniem `PATH` nie zadziałała z powodu niedostępnego Perla.

Przygotowane polecenie wejścia do katalogu na tym komputerze:

```powershell
Set-Location -LiteralPath 'C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\teoria modeli'
```

PDF zbudowano dwoma wykonanymi przebiegami:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error 'teoria modeli.tex'
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error 'teoria modeli.tex'
```

Oba polecenia zakończyły się kodem 0. Drugie ustabilizowało
odsyłacze. Wykonane kontrole:

```powershell
rg -n -i 'undefined|multiply defined|overfull|underfull|missing character|fatal error|emergency stop|LaTeX Warning|Package .* Warning|pdfTeX warning' 'teoria modeli.log'
pdfinfo 'teoria modeli.pdf' | Select-String -Pattern 'Pages:|Page size:|File size:|PDF version:'
```

W logu nie znaleziono żadnego dopasowania. PDF ma 36 stron A4,
563408 bajtów i wersję PDF 1.5. Strony 1, 8 i 20 wyrenderowano
i obejrzano. Kontrolny render z katalogu głównego repozytorium:

```powershell
$auditDir = Join-Path $env:TEMP 'models-audit-20261027'
New-Item -ItemType Directory -Force -Path $auditDir | Out-Null
pdftoppm -f 1 -l 1 -png -r 100 'teoria modeli/teoria modeli.pdf' (Join-Path $auditDir 'page')
pdftoppm -f 8 -l 8 -png -r 100 'teoria modeli/teoria modeli.pdf' (Join-Path $auditDir 'page')
pdftoppm -f 20 -l 20 -png -r 100 'teoria modeli/teoria modeli.pdf' (Join-Path $auditDir 'page')
git diff --check
```

### Instrukcja przygotowana do samodzielnego wykonania

Na nowym stanowisku użyj opisanej wyżej procedury instalacji MiKTeX
i pakietów. Ten skrypt wymaga tych samych pakietów typograficznych
co Banach--Tarski; osobno nie pobiera się danych. Z katalogu
`teoria modeli` uruchom dwa przebiegi `pdflatex` z bloku powyżej.
Jeśli Perl z Git for Windows jest w `PATH`, można zamiast tego
użyć `latexmk -pdf`; tej alternatywy nie wykonano w tym audycie.
