# Manual pracy w repozytorium `mathematical_scipts`

Ten plik zapisuje odtwarzalne polecenia środowiska, budowania i kontroli.
Polecenia faktycznie wykonane są oddzielone od instrukcji przygotowanych
do późniejszego użycia.

## Projekt „Geometria i topologia różniczkowa”

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
  'makeindex', 'mathtools', 'pgf', 'pgfplots', 'tikz-cd', 'tools',
  'xr-hyper'
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
