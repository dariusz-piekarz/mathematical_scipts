# Manual pracy w repozytorium `mathematical_scipts`

Ten plik zapisuje odtwarzalne polecenia środowiska, budowania i kontroli.
Polecenia faktycznie wykonane są oddzielone od instrukcji przygotowanych
do późniejszego użycia.

## TokenEconomizer: diagnostyka w bieżącym etapie — 4 listopada 2026

**Polecenia faktycznie wykonane** w katalogu głównym repozytorium
(PowerShell 5.1, Git Bash i Python 3.14.8 z `uv`):

```powershell
$env:TE_PYTHON='/c/Users/DXD/.local/bin/python.exe'
$te=(Join-Path $env:USERPROFILE '.tokeneconomizer\bin\te').Replace('\','/')
& 'C:\Program Files\Git\bin\bash.exe' $te --host codex --cwd (Get-Location).Path status
& 'C:\Program Files\Git\bin\bash.exe' $te --host codex --cwd (Get-Location).Path config show
```

Oba polecenia zakończyły się kodem 0. Konfiguracja zgłasza
`enabled: true`, `toolprune: auto`, `loopguard: nudge` i
`microskills: off`; stan obejmuje dwie zakończone sesje. Próba
bez `TE_PYTHON` zgłosiła `te: no python3 on PATH`, ponieważ
Git Bash w tym procesie nie znajduje Pythona z `uv`.
Nie zmieniano ustawień wtyczki.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na innym koncie zastąp ścieżkę w `TE_PYTHON` rzeczywistą
ścieżką do `python.exe` w zapisie Git Bash, na przykład
`/c/Users/NAZWA/.local/bin/python.exe`, i wykonaj oba
polecenia z bloku. Hooki wtyczki są ładowane przy starcie
sesji Codex CLI, którą uruchamia `instaluj_tokeneconomizer.ps1
-StartCodex`.

## TokenEconomizer: uruchomienie hooków — 4 listopada 2026

**Polecenia faktycznie wykonane** w katalogu repozytorium:

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
codex.exe --no-daemon
powershell -NoProfile -ExecutionPolicy Bypass -File '.\instaluj_tokeneconomizer.ps1' -StartCodex
$te = (Join-Path $env:USERPROFILE '.tokeneconomizer\bin\te').Replace('\','/')
& 'C:\Program Files\Git\bin\bash.exe' $te --host codex --cwd (Get-Location).Path status
```

Pierwsze wywołanie `-StartCodex` sprzed poprawki kończyło się
komunikatem `this CLI has no complete local package`. Ta kopia
Codex CLI z rozszerzenia VS Code wymaga `--no-daemon` do pracy
w terminalu. Skrypt startowy przekazuje teraz tę opcję i kończy
się błędem, jeśli Codex zgłosi niezerowy kod wyjścia.
W poprawnie uruchomionym CLI polecenie `/hooks` pokazało pięć
hooków TokenEconomizer jako aktywne i zaufane. Po wysłaniu
pierwszej zwykłej wiadomości pojawiło się `Running hook` i
powstał plik `%USERPROFILE%\.tokeneconomizer\bin\te`.
Po zamknięciu sesji polecenie `status` wykazało dwie złożone
sesje; nie wykazało jeszcze oszczędności tokenów.

**Instrukcja przygotowana do samodzielnego wykonania.**
Uruchom `powershell -NoProfile -ExecutionPolicy Bypass -File
'.\instaluj_tokeneconomizer.ps1' -StartCodex`, w terminalowym
Codex wpisz `/hooks`, następnie wyślij wiadomość i zakończ
sesję przez `/exit`. W nowej sesji można wywołać
`$tokeneconomizer:status`. Zaufanie do hooków zostało już
zapisane, więc ekran zatwierdzania nie pojawia się ponownie,
dopóki definicja hooka się nie zmieni. Okno czatu VS Code nie
udostępnia terminalowego polecenia `/hooks`.

## Projekt „Geometria i topologia różniczkowa”

Od 27 października 2026 bieżący skład ma cztery tomy:
I (rozdziały 1--10), II (11--22), III (23--30) i IV (31--38
oraz dodatki). Starsze wpisy poniżej dokumentują rzeczywiście
wykonane wówczas polecenia dla dawnego podziału na trzy tomy;
ich numery stron i nazwy PDF-ów są historyczne.

### Rozdział 6, sekcje 1–9 — ukończony etap z 6 listopada 2026

Katalog projektu: `geometria i topologia różniczkowa`; źródło:
`tex/rozdzialy/06-algebra-homologiczna.tex`; plik główny tomu I:
`geometria_tom1.tex`. Użyto istniejącego środowiska Windows
PowerShell, MiKTeX 25.12, `latexmk` 4.88, `pdftoppm` i Perla z
`C:\Program Files\Git\usr\bin`. Nie instalowano zależności ani nie
pobierano danych. Skład uruchomiono dopiero po ukończeniu całego
rozdziału i wyłącznie dla tomu I.

**Polecenia faktycznie wykonane** w katalogu projektu:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom1.tex *> build/tomy/review_ch6_build.txt
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom1.tex
pdfinfo 'build/tomy/geometria_tom1.pdf' | Select-String -Pattern 'Pages|Page size|File size'
rg -n -i 'LaTeX Warning|Overfull|Underfull|undefined references|multiply defined|Fatal error|! LaTeX Error' build/tomy/geometria_tom1.log
$pages=@(160,161,169,170)
foreach($n in $pages){pdftoppm -f $n -l $n -singlefile -png -r 115 'build/tomy/geometria_tom1.pdf' "build/tomy/ch6_p$n"}
pdftoppm -f 161 -l 161 -singlefile -png -r 180 'build/tomy/geometria_tom1.pdf' 'build/tomy/ch6_p161_hi'
Copy-Item -LiteralPath 'build/tomy/geometria_tom1.pdf' -Destination 'geometria_tom1.pdf' -Force
Get-FileHash -Algorithm SHA256 -LiteralPath 'build/tomy/geometria_tom1.pdf'
Get-FileHash -Algorithm SHA256 -LiteralPath 'geometria_tom1.pdf'
```

Pierwsze wywołanie utworzyło końcowy PDF i indeks, ale PowerShell
zwrócił kod 1, gdy komunikat `makeindex` ze stderr zapisał jako
`NativeCommandError`. Drugie wywołanie `latexmk` bez przekierowania
zakończyło się kodem 0 i potwierdziło aktualność wszystkich celów.
PDF ma 239 stron. Końcowy log nie ma błędów, nierozwiązanych
odsyłaczy ani `Overfull`; dwa wcześniejsze ostrzeżenia `h`→`ht`
i jeden `Underfull` leżą poza rozdziałem 6. Indeks przyjął 122 hasła,
0 odrzucił i nie zgłosił ostrzeżeń. Obejrzano wszystkie cztery strony
z rysunkami oraz powiększenie schematu na stronie 161. Suma SHA-256
obu kopii PDF jest identyczna:
`B3C171A5C2FAD9B4E0503CBBC441940D8B04EC394857B4FE2AEE2E4EB2E577DD`.

**Instrukcja przygotowana do samodzielnego wykonania.** Na innym
stanowisku otwórz PowerShell w katalogu projektu, zapewnij MiKTeX,
`latexmk`, Perl, `pdfinfo` i `pdftoppm` w `PATH`, po ukończeniu
rozdziału uruchom skład tomu I bez przekierowania stderr, sprawdź
log, indeks i strony rysunków, a następnie skopiuj PDF i porównaj
sumy SHA-256. Fizyczne numery stron zmienią się po dalszych edycjach.

### Rozdział 5, sekcje 1–5 — ukończony etap z 6 listopada 2026

Katalog projektu: `geometria i topologia różniczkowa`; źródło:
`tex/rozdzialy/05-algebra-abstrakcyjna.tex`; plik główny tomu I:
`geometria_tom1.tex`. Użyto istniejącego środowiska Windows
PowerShell, MiKTeX 25.12, `latexmk` 4.88 i Perla z
`C:\Program Files\Git\usr\bin`. Nie instalowano zależności ani
nie pobierano danych. Zgodnie z ustaloną kolejnością skład
uruchomiono po przejściu całego rozdziału; po kontroli rysunków
i redakcji wzorów wykonano go ponownie dla końcowej wersji.

**Polecenia faktycznie wykonane** w katalogu projektu:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom1.tex *> build/tomy/review_ch5_build.txt
$pages=@(141,143,147,149)
foreach($n in $pages){pdftoppm -f $n -l $n -singlefile -png -r 115 'build/tomy/geometria_tom1.pdf' "build/tomy/ch5_p$n"}
Copy-Item -LiteralPath 'build/tomy/geometria_tom1.pdf' -Destination 'geometria_tom1.pdf' -Force
Get-FileHash -Algorithm SHA256 -LiteralPath 'build/tomy/geometria_tom1.pdf'
Get-FileHash -Algorithm SHA256 -LiteralPath 'geometria_tom1.pdf'
```

Końcowy `latexmk` zakończył się kodem 0; PDF ma 237 stron.
W `build/tomy/geometria_tom1.log` nie ma błędów, nierozwiązanych
odsyłaczy ani `Overfull`; pozostały dwa wcześniejsze ostrzeżenia
o zamianie `h` na `ht` i jeden `Underfull` poza rozdziałem 5.
`build/tomy/geometria_tom1.ilg` wykazuje 122 przyjęte wpisy,
0 odrzuconych i 0 ostrzeżeń. Obejrzano wskazane cztery strony
ze wszystkimi rysunkami rozdziału. Suma SHA-256 obu kopii PDF
jest identyczna:
`94625049941CD80AE4A89D4A192E603522E58DDF6A81A7601E9CEDEBC8875A56`.
Tomów II–IV nie składano, gdyż rozdział 5 należy do tomu I.

**Instrukcja przygotowana do samodzielnego wykonania.** Na innym
stanowisku otwórz PowerShell w katalogu projektu, zapewnij MiKTeX,
`latexmk` i Perl w `PATH`, po ukończeniu rozdziału uruchom powyższy
skład tomu I, sprawdź log, indeks i strony rysunków, a następnie
skopiuj PDF i porównaj sumy SHA-256. Numery fizycznych stron
rysunków mogą się zmienić po dalszych edycjach.

### Rozdział 4, sekcje 1–7 — ukończony etap z 6 listopada 2026

Katalog projektu: `geometria i topologia różniczkowa`; źródło:
`tex/rozdzialy/04-grassmanniany-clifford-spinory.tex`; plik główny
tomu I: `geometria_tom1.tex`. Użyto istniejącego środowiska
Windows PowerShell, MiKTeX 25.12, `latexmk` 4.88 i Perla z
`C:\Program Files\Git\usr\bin`. Nie instalowano zależności ani
nie pobierano danych. Skład wykonano po przejściu całego rozdziału.

**Polecenia faktycznie wykonane** w katalogu projektu:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom1.tex *> build/tomy/review_ch4_build.txt
$pages=@(119,122,127,130,133,136)
foreach($n in $pages){pdftoppm -f $n -l $n -singlefile -png -r 105 'build/tomy/geometria_tom1.pdf' "build/tomy/ch4_p$n"}
Copy-Item -LiteralPath 'build/tomy/geometria_tom1.pdf' -Destination 'geometria_tom1.pdf' -Force
Get-FileHash -Algorithm SHA256 -LiteralPath 'build/tomy/geometria_tom1.pdf'
Get-FileHash -Algorithm SHA256 -LiteralPath 'geometria_tom1.pdf'
```

`latexmk` zakończył się kodem 0; PDF ma 233 strony. W
`build/tomy/geometria_tom1.log` nie ma błędów, nierozwiązanych
odsyłaczy ani `Overfull`; pozostały dwa wcześniejsze ostrzeżenia
o zamianie `h` na `ht` i jeden `Underfull` poza rozdziałem 4.
`build/tomy/geometria_tom1.ilg` wykazuje 117 przyjętych wpisów,
0 odrzuconych i 0 ostrzeżeń. Obejrzano wszystkie sześć wskazanych
stron z rysunkami. Suma SHA-256 obu kopii PDF jest identyczna:
`2FBF1DFF5F2401624034616617F4DEE26D198B99073E400E252CF4D41AFCD86D`.
Nie składano tomów II–IV, ponieważ rozdział 4 należy do tomu I.

**Instrukcja przygotowana do samodzielnego wykonania.** Na innym
stanowisku otwórz PowerShell w katalogu projektu, zapewnij MiKTeX,
`latexmk` i Perl w `PATH`, po ukończeniu rozdziału uruchom powyższy
skład tomu I, sprawdź log, indeks i strony rysunków, a następnie
skopiuj PDF i porównaj sumy SHA-256. Numery fizycznych stron
rysunków mogą się zmienić po dalszych edycjach.

### Rozdział 3, sekcje 1–9 — ukończony etap z 5 listopada 2026

Katalog repozytorium:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts`.
Katalog projektu: `geometria i topologia różniczkowa`.
Edytowane źródło: `tex/rozdzialy/03-algebra-tensorowa.tex`.
Obowiązuje to samo sprawdzone wcześniej środowisko Windows
PowerShell, MiKTeX 25.12, `latexmk` 4.88 i Perl z
`C:\Program Files\Git\usr\bin`; w tym etapie nie
instalowano narzędzi ani nie pobierano danych.

**Polecenia faktycznie wykonane** w katalogu repozytorium
przed i po edycji:

```powershell
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
git fetch origin review/rozdzialy-matematyka
git diff --check
```

Przed edycją porównanie gałęzi dało `0 0`. Przejrzano kolejno
§§3.1–3.9 i niezależnie skontrolowano nowe rachunki oraz rysunki.
Zgodnie z ustaloną kolejnością skład uruchomiono dopiero po
ukończeniu całego rozdziału. W katalogu projektu wykonano
**tylko skład tomu I**:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom1.tex *> build/tomy/review_ch3_build.txt
```

Kod wyjścia wyniósł `0`; otrzymano PDF o 230 stronach.
W `build/tomy/geometria_tom1.log` sprawdzono ostrzeżenia,
brakujące odsyłacze, błędy i przepełnione wiersze: nie ma
błędów, nierozwiązanych odsyłaczy ani `Overfull`. Indeks
`build/tomy/geometria_tom1.ilg` przyjął 117 wpisów, 0 odrzucił
i podał 0 ostrzeżeń. Pozostały dwa ostrzeżenia o zamianie
specyfikatora `h` na `ht` i jeden `Underfull` poza nowym rozdziałem.
Wykonano również:

```powershell
$pages=@(94,97,101,105,108,110,114,115)
foreach($n in $pages){pdftoppm -f $n -l $n -singlefile -png -r 105 'build/tomy/geometria_tom1.pdf' "build/tomy/ch3_p$n"}
Copy-Item -LiteralPath 'build/tomy/geometria_tom1.pdf' -Destination 'geometria_tom1.pdf' -Force
Get-FileHash -Algorithm SHA256 -LiteralPath 'build/tomy/geometria_tom1.pdf'
Get-FileHash -Algorithm SHA256 -LiteralPath 'geometria_tom1.pdf'
```

Obejrzano strony fizyczne 94, 97, 101, 105, 108, 110, 114 i 115,
zawierające wszystkie osiem rysunków rozdziału 3. Wersja robocza
i kopia projektu mają tę samą sumę SHA-256:
`AC4AADCDADD621B4FFDDD80F2B0E0AA48628F244AF2845A402388B8615521157`.

**Instrukcja przygotowana do samodzielnego wykonania.** Na innym
stanowisku otwórz PowerShell w katalogu projektu, dodaj katalog
Perla z Git for Windows do `PATH` i wykonaj wskazane wyżej
polecenie `latexmk`. Następnie sprawdź log oraz indeks, obejrzyj
strony z rysunkami i dopiero po pomyślnej kontroli skopiuj PDF.
Nie ma potrzeby składać pozostałych trzech tomów przy zmianie
dotyczącej wyłącznie rozdziału 3.

### Przegląd rozdziału 2, sekcje 3–7 — 5 listopada 2026

Katalog repozytorium:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts`.
Katalog projektu: `geometria i topologia różniczkowa`.
Źródło rozdziału: `tex/rozdzialy/02-pola-wektorowe.tex`;
plik główny tomu I: `geometria_tom1.tex`.
Środowisko: Windows PowerShell, istniejący MiKTeX 25.12,
`latexmk` 4.88 i Perl z `C:\Program Files\Git\usr\bin`.
Nie instalowano zależności ani nie pobierano danych projektu.

**Polecenia faktycznie wykonane.** W katalogu repozytorium
przed rozpoczęciem edycji:

```powershell
git fetch origin review/rozdzialy-matematyka
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
```

Porównanie gałęzi dało `0 0`. Po przejrzeniu i poprawieniu
wszystkich pięciu sekcji rozdziału, w katalogu projektu
uruchomiono skład wyłącznie tomu I:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom1.tex
```

W katalogu repozytorium wykonano ponadto:

```powershell
pdfinfo 'geometria i topologia różniczkowa/build/tomy/geometria_tom1.pdf' | Select-String '^Pages:'
Select-String -LiteralPath 'geometria i topologia różniczkowa/build/tomy/geometria_tom1.ilg' -Pattern 'entries accepted|rejected'
Select-String -LiteralPath 'geometria i topologia różniczkowa/build/tomy/geometria_tom1.log' -Pattern '^!','Overfull','Missing character','LaTeX Warning: Reference .* undefined','There were undefined references','multiply defined'
```

PDF w `build/tomy` ma 225 stron, a indeks przyjął 117 wpisów
i odrzucił 0. W końcowym logu nie znaleziono błędów,
przepełnionych wierszy, brakujących znaków ani wskazanych
problemów z odsyłaczami. Pierwszą próbę składu
przerwano po doprecyzowaniu przez autora kolejności pracy;
pełny skład uruchomiono dopiero po przejściu całego rozdziału.
W tym etapie zmieniany rozdział należy tylko do tomu I.
Skład pozostałych trzech tomów oraz pliku zbiorczego nie był
potrzebny do sprawdzenia tej zmiany.

W katalogu projektu wyrenderowano `pdftoppm` fizyczne strony
77, 80–82, 85, 87, 89 i 91 do plików PNG w `build/tomy`
i obejrzano na nich rysunki 2.2–2.10. Po kontroli wykonano:

```powershell
Copy-Item -LiteralPath 'build/tomy/geometria_tom1.pdf' -Destination 'geometria_tom1.pdf' -Force
Get-FileHash -Algorithm SHA256 -LiteralPath 'build/tomy/geometria_tom1.pdf'
Get-FileHash -Algorithm SHA256 -LiteralPath 'geometria_tom1.pdf'
```

Obie sumy SHA-256 były równe:
`5CFE50A7EA0819EB8B8A8F0991C068FC3126860A9BDCB86808F423ED073558DD`.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na innym stanowisku przygotuj MiKTeX z `latexmk` i Perl
dostępny w `PATH`; wersje wskazane wyżej są sprawdzone
w tej iteracji. Wejdź do katalogu projektu i wykonaj
oba polecenia z bloku składu. Następnie z katalogu
repozytorium powtórz trzy polecenia kontroli oraz sprawdź
strony z nowymi rysunkami i wynik `git diff --check`.
Po sprawdzeniu skopiuj
`build/tomy/geometria_tom1.pdf` do katalogu projektu.
Dla kolejnych rozdziałów obowiązuje kolejność ustalona
przez autora: przegląd całego rozdziału, skład odpowiedniego
tomu, kontrola, commit i push. Pełny `buduj_tomy.ps1` służy
do okresowej kontroli wszystkich tomów i do publikacji.

### Końcowa kontrola czterech tomów — 4 listopada 2026

**Polecenia faktycznie wykonane** w katalogu
`geometria i topologia różniczkowa` na Windows PowerShell 5.1,
z istniejącymi MiKTeX 25.12, `latexmk` 4.88,
Perlem 5.42.3 z Git for Windows i Popplerem 24.04.0:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\buduj_tomy.ps1'
$names = @('geometria_tom1','geometria_tom2','geometria_tom3','geometria_tom4')
foreach ($n in $names) {
    pdfinfo (Join-Path 'build/tomy' ($n + '.pdf')) | Select-String '^Pages:'
    Select-String -Path (Join-Path 'build/tomy' ($n + '.ilg')) -Pattern 'accepted','rejected'
    Select-String -Path (Join-Path 'build/tomy' ($n + '.log')) -Pattern '^!','Overfull','Missing character','LaTeX Warning: Reference .* undefined','There were undefined references','multiply defined'
    $copy = (Get-FileHash -Algorithm SHA256 ($n + '.pdf')).Hash
    $build = (Get-FileHash -Algorithm SHA256 (Join-Path 'build/tomy' ($n + '.pdf'))).Hash
    $copy -eq $build
    pdftohtml -q -xml -f 1 -l 2 -stdout ($n + '.pdf') |
        Select-String -Pattern 'geometria_tom[1-4]\.pdf'
}
```

Skład zakończył się kodem 0. Tomy mają odpowiednio 219, 193,
104 i 98 stron. Wszystkie cztery indeksy mają `0 rejected`;
kontrola końcowych logów nie znalazła błędów, brakujących ani
powielonych odsyłaczy, `Overfull` lub brakujących znaków.
Sumy SHA-256 czterech PDF-ów w katalogu projektu zgadzają się
z odpowiednikami w `build/tomy`. W XML stron tytułowych
potwierdzono po trzy łącza do pozostałych tomów. Sprawdzono
wizualnie wybrane strony z poprawionymi wzorami i terminologią:
I 144, 210, 212; II 27, 43, 86; III 42, 58, 79;
IV 42, 62, 63. Nie instalowano nowych zależności.

**Polecenie faktycznie wykonane** dla opcjonalnego składu
zbiorczego, także w katalogu projektu:

```powershell
$env:Path = 'C:\Program Files\Git\usr\bin;' + $env:Path
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/sklad geometria_i_topologia_rozniczkowa.tex
```

Przed końcową jednozdaniową korektą odmiany w rozdziale 3
skład zbiorczy zakończył się kodem 0: 606 stron, indeks
350 przyjętych wpisów i `0 rejected`, bez błędów, `Overfull`,
brakujących znaków, niezdefiniowanych ani powielonych etykiet.
Tabela oznaczeń na fizycznej stronie 7 jest czytelna.
Końcową korektę rozdziału 3 sprawdzono już w ponownym pełnym
składzie czterech tomów i w tekstowej ekstrakcji tomu I.
Nie kopiowano PDF-u z `build/sklad` do katalogu projektu,
ponieważ tamtejszy PDF zbiorczy był wcześniej zmieniony przez autora.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na innym stanowisku przygotuj wersje narzędzi podane wyżej,
uruchom `buduj_tomy.ps1` w katalogu projektu i powtórz kontrolę
logów, indeksów, sum oraz wybranych stron. Skrypt sam dodaje
Perl z Git for Windows do `PATH`, jeśli jest potrzebny.

### Tom II, potok Ricciego i TokenEconomizer — 4 listopada 2026

Katalog repozytorium: `C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts`.
Źródła książki: `geometria i topologia różniczkowa\tex\rozdzialy`.
Materiał od autora: `geometria i topologia różniczkowa\do_dodania.tex`;
jest zachowany jako plik wejściowy i nie jest wczytywany przez `\input`.
Nowe fragmenty wstawiono do rozdziałów 11–14, 30, 30a i poprawiono
cytowanie w 26 oraz dodatku A. Nie pobierano danych matematycznych.

Wykorzystane narzędzia: Windows PowerShell 5.1, MiKTeX 25.12,
`latexmk` 4.88, Perl 5.42.3 z `C:\Program Files\Git\usr\bin`, Poppler
24.04.0, Git for Windows, `uv` 0.13.1 i Codex CLI
0.162.0-alpha.17.2. Skrypt `buduj_tomy.ps1` dodaje Perl do `PATH`
przed uruchomieniem `latexmk`; bez tego bezpośrednie
`latexmk -v` w tej sesji zgłasza brak silnika skryptów `perl`.
Pakiet LaTeX `mathrsfs` jest dostępny w obecnym MiKTeX i jest
używany przez rozdział 30. Nie instalowano go osobno.

**Polecenia faktycznie wykonane.** W katalogu repozytorium:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\instaluj_tokeneconomizer.ps1'
git diff --check
```

Instalator uruchomiono ponownie z powodzeniem: wynik wskazuje
Python 3.14.8, upstream TokenEconomizer na commicie
`d3e193b8734ec76230da1e08d7929ba9d14640d8` oraz wtyczkę
`tokeneconomizer@tokeneconomizer` 0.1.0 jako `installed, enabled`.
Źródła wtyczki są poza repozytorium, w
`%LOCALAPPDATA%\TokenEconomizer\source-d3e193b8734e`;
`uv` tworzy `python.exe` w `%USERPROFILE%\.local\bin`.
Instalator umieszcza ten katalog na początku `PATH` bieżącego
procesu oraz, jeśli potrzeba, dodaje go do ścieżki użytkownika.
Na tym Windows alias Python ze sklepu Microsoft może nadal
poprzedzać ścieżkę użytkownika w nowym zwykłym procesie;
wariant `-StartCodex` uruchamia CLI z poprawnym `PATH`.
Nie potwierdzono jeszcze uruchomienia haków w bieżącej sesji IDE.

W katalogu `geometria i topologia różniczkowa` wykonano:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\buduj_tomy.ps1'
pdfinfo '.\geometria_tom2.pdf'
pdftotext -layout -enc UTF-8 '.\geometria_tom2.pdf' "$env:TEMP\mathematical_scipts_tom2_review.txt"
pdftohtml -q -xml -f 1 -l 2 -stdout '.\geometria_tom2.pdf'
```

Pełny skład zakończył się kodem 0 po dwóch przebiegach.
Tomy I–IV mają 219, 193, 104 i 98 stron; indeksy przyjęły
113, 102, 33 i 102 wpisy, każdy z `0 rejected`.
Nie ma błędów LaTeX, brakujących ani powielonych etykiet,
`Overfull` lub brakujących znaków. Każdy PDF ma trzy łącza
do pozostałych tomów i sumę SHA-256 zgodną z kopią
`build/tomy`. Przez `pdftoppm -singlefile -scale-to 1400
-png` wyrenderowano i obejrzano fizyczne strony 10, 43,
67 i 69 tomu II oraz 78 tomu I. Po poprawie podpisu
rysunku konforemnego sprawdzono ponownie stronę 67.
Zbiorczy PDF nie jest objęty tym składem czterech tomów.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na innym stanowisku zainstaluj Git, MiKTeX z `latexmk`, Perl,
Poppler, `uv` i Codex CLI; dla odtworzenia tej instalacji użyj
wersji wskazanych wyżej. W katalogu repozytorium uruchom
`powershell -NoProfile -ExecutionPolicy Bypass -File
'.\instaluj_tokeneconomizer.ps1'`. Skrypt przypina commit
upstream i instaluje Python 3.14.8 przez `uv`.
Następnie z tego katalogu uruchom
`powershell -NoProfile -ExecutionPolicy Bypass -File
'.\instaluj_tokeneconomizer.ps1' -StartCodex`.
W nowej sesji CLI przejrzyj i zaufaj dokładnym hakom wtyczki,
zakończ sesję, uruchom kolejną i wpisz
`$tokeneconomizer:status`. Zaufanie do haków jest operacją
użytkownika w Codex; instalator go nie ustawia. Działania w
sesji IDE trzeba zweryfikować osobno.

W katalogu projektu wykonaj pełny skład poleceniem
`powershell -NoProfile -ExecutionPolicy Bypass -File
'.\buduj_tomy.ps1'`, a następnie sprawdź logi w `build/tomy`,
`0 rejected` w plikach `.ilg`, PDF-y i łącza między nimi.
MiKTeX potrzebuje Perla; skrypt korzysta z wersji z Git for Windows.

### Audyt zmian autora w rozdziale 2 — 4 listopada 2026

Katalog repozytorium: `C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts`.
Projekt: `geometria i topologia różniczkowa`. Użyto istniejącego
MiKTeX 25.12 i `latexmk` 4.88; skrypt `buduj_tomy.ps1` sam dodaje
Perl 5.42.3 z Git for Windows do `PATH`, jeśli go brakuje.
Do kontroli PDF użyto Popplera 24.04.0. Nie pobierano danych
ani nowych zależności rozdziału.

**Polecenia faktycznie wykonane.** W katalogu repozytorium:

```powershell
git fetch origin
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
git diff --check
```

Przed zmianami porównanie gałęzi dało `0 0`. Porównano różnicę
`tex/rozdzialy/02-pola-wektorowe.tex` z `HEAD` i poprawiono
cztery konkretne usterki opisane w `mods.md`.
W katalogu projektu wykonano pełny skład:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\buduj_tomy.ps1'
```

Po składzie sprawdzono `geometria_tom1.pdf` poleceniami
`pdfinfo`, `pdftotext`, `pdftoppm` i `git diff --check`.
Pełny skład czterech tomów dał 219, 193, 104 i 98 stron;
indeksy przyjęły 113, 102, 33 i 102 wpisy, bez odrzuceń.
Logi nie zawierają błędów, brakujących lub powielonych
odsyłaczy, `Overfull` ani brakujących znaków. Sumy SHA-256
PDF-ów w katalogu projektu są zgodne z `build/tomy`.
Obejrzano fizyczną stronę 78 tomu I z rysunkiem składania
przesunięć lokalnego przepływu.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na nowym stanowisku zainstaluj MiKTeX, Perl i Poppler
według instrukcji w dalszej części pliku. W katalogu projektu
uruchom `powershell -NoProfile -ExecutionPolicy Bypass -File
'.\buduj_tomy.ps1'`; sprawdź powyższe logi i stronę rysunku.
Bezpośrednie `latexmk -v` w zwykłej sesji bez Perla w `PATH`
może zakończyć się błędem MiKTeX; użyj skryptu, który dodaje
Perl z `C:\Program Files\Git\usr\bin`.

### Nienumerowane podsekcje indeksowe — przebieg 29 października 2026

Katalog roboczy:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Użyto tego samego środowiska MiKTeX 25.12, `latexmk` 4.88,
Perl 5.42.3 z Git for Windows i Poppler 24.04.0, które
opisano poniżej. Nie pobierano danych ani nie instalowano
nowych zależności.

**Polecenia faktycznie wykonane.** W korzeniu repozytorium
wykonano `git fetch origin`. W katalogu projektu:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\buduj_tomy.ps1'
```

Po składzie wykonano pełną pętlę kontroli czterech PDF-ów
zapisaną w następnej sekcji, poprzedzoną
`$ErrorActionPreference='Stop'`. Pierwsza próba omyłkowo
użyła pojedynczego `\hbox` w wyrażeniu regularnym i nie
stanowiła poprawnej kontroli logów. W pętli zapisanej niżej
uproszczono wzorzec do `Overfull` i dodano
`-ErrorAction Stop`; kontrolę powtórzono. Poprawne
wykonanie dało: 216, 186, 104 i 88 stron;
indeksy przyjęły 113, 101, 33 i 96 wpisów bez odrzuceń.
W logach nie ma błędów, niezdefiniowanych ani powielonych
etykiet, przepełnionych wierszy ani brakujących znaków.
Każdy PDF ma trzy łącza do pozostałych tomów, a kopie
w katalogu projektu mają sumy SHA-256 zgodne z `build/tomy`.

Wykonano ponadto kontrolę odsyłaczy między tomami:

```powershell
pdftohtml -q -xml -f 101 -l 101 -stdout geometria_tom3.pdf | Select-String -Pattern '18.5.4|geometria_tom2.pdf'
pdftohtml -q -xml -f 52 -l 52 -stdout geometria_tom4.pdf | Select-String -Pattern '18.5.5|geometria_tom2.pdf'
git diff --check
```

XML potwierdził łącza do twierdzeń 18.5.4 i 18.5.5 w tomie II.
`pdftotext` potwierdził trzy nienumerowane śródtytuły.
Wyrenderowano przez `pdftoppm -singlefile -scale-to 1400
-png` i obejrzano fizyczne strony 119, 121 i 122 tomu II,
101 tomu III oraz 52 tomu IV.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na nowym stanowisku przygotuj MiKTeX, Perl i Poppler
według następnej sekcji; tej instalacji teraz nie wykonywano.
Z katalogu projektu uruchom skrypt `buduj_tomy.ps1`
przez `powershell -NoProfile -ExecutionPolicy Bypass -File
'.\buduj_tomy.ps1'`, następnie wykonaj pętlę kontroli
oraz dwa polecenia `pdftohtml` z tego wpisu.

### Dowody wzorów indeksowych — przebieg pracy 29 października 2026

Katalog projektu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Środowisko sprawdzone w tej iteracji: Windows PowerShell 5.1.19041.6456,
MiKTeX 25.12, `latexmk` 4.88, Perl 5.42.3 z Git for Windows
i Poppler 24.04.0. `buduj_tomy.ps1` ustawia `PATH` dla Perla,
jeśli potrzeba. Nie pobierano danych projektu ani nie instalowano
nowych zależności. Źródłowy artykuł Getzlera pobrano wyłącznie
do katalogu `$env:TEMP` na potrzeby sprawdzenia dowodu.

**Polecenia faktycznie wykonane.** W korzeniu repozytorium:

```powershell
git fetch origin
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
git diff --check
```

Przed zmianami porównanie gałęzi dało `0 0`. W katalogu
projektu wykonano:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File '.\buduj_tomy.ps1'
```

Bezpośrednie `.\buduj_tomy.ps1` zostało wcześniej odrzucone przez
lokalną politykę wykonywania skryptów PowerShell; wariant z
`-ExecutionPolicy Bypass` uruchomił pełny skład.
Skrypt składa cztery pliki główne, prowadzi do czterech obiegów
odsyłaczy, sprawdza `0 rejected` w indeksach i kopiuje
PDF-y z `build/tomy` do katalogu projektu.

Po składzie wykonano kontrolę:

```powershell
$volNames=@('geometria_tom1','geometria_tom2','geometria_tom3','geometria_tom4')
foreach($volName in $volNames){
  $pageLine=(pdfinfo "$volName.pdf" | Select-String '^Pages:').Line.Trim()
  $indexLine=(Select-String -LiteralPath "build/tomy/$volName.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $badLines=@(Select-String -LiteralPath "build/tomy/$volName.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|multiply defined|Overfull|Missing character|! LaTeX Error' -ErrorAction Stop)
  $linkList=@(pdftohtml -q -xml -f 1 -l 1 -stdout "$volName.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $sameHash=(Get-FileHash "$volName.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$volName.pdf" -Algorithm SHA256).Hash
  if(-not $indexLine -or $badLines.Count -ne 0 -or $linkList.Count -ne 3 -or -not $sameHash){ throw "Kontrola $volName nie powiodła się" }
  '{0}: {1}; {2}; {3} łącza; SHA-256 zgodna' -f $volName,$pageLine,$indexLine,$linkList.Count
}
git diff --check
```

Wynik: tomy I–IV mają 216, 186, 104 i 88 stron; indeksy
przyjęły 113, 101, 33 i 96 wpisów bez odrzuceń.
Każdy tom ma trzy łącza do pozostałych, a sumy kopii PDF
są zgodne. Nie znaleziono wskazanych problemów w logach.
`pdftotext -layout` posłużył do lokalizacji nowych odsyłaczy,
a `pdftoppm -png -r 105` do renderu i obejrzenia stron
119–123 tomu II, 99–101 tomu III oraz 51–52, 69 i 71 tomu IV.
Polecenie `pdftohtml -q -xml -f 99 -l 101 -stdout
'geometria_tom3.pdf'` i analogiczne zakresy 51–52 oraz
69–71 tomu IV potwierdziły łącza oznaczeń 18.5.3–18.5.5
do `geometria_tom2.pdf`.

**Instrukcja przygotowana do samodzielnego wykonania.** Na nowym
stanowisku zainstaluj MiKTeX z `latexmk`, Perl dostępny
w `PATH` (lub Git for Windows w
`C:\Program Files\Git\usr\bin`) oraz Poppler dla kontroli PDF.
Zainstaluj brakujące pakiety MiKTeX według wcześniejszego wpisu
o przygotowaniu czystego stanowiska. W powyższym katalogu projektu
uruchom ten sam skrypt przez `powershell -NoProfile
-ExecutionPolicy Bypass -File '.\buduj_tomy.ps1'`; żadne osobne
dane ani zmienne środowiskowe nie są potrzebne.
Po składzie sprawdź logi w `build/tomy`, strony
nowej sekcji w tomie II, odsyłacze w tomach III i IV oraz indeksy.

### Przestrzeń moduli Donaldsona — przebieg pracy 29 października 2026

Katalog projektu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Środowisko: Windows PowerShell 5.1.19041.6456, MiKTeX 25.12,
`latexmk` 4.88, Perl 5.42.3 z Git for Windows, Poppler 24.04.0.
Nie pobierano danych, nie instalowano zależności i nie ustawiano
nowych zmiennych środowiskowych. `buduj_tomy.ps1` dodaje katalog
`C:\Program Files\Git\usr\bin` do `PATH`, gdy `perl` nie jest dostępny.
Źródła tomu IV to `geometria_tom4.tex`, `tex/rozdzialy/34-donaldson.tex`
i `tex/dodatki/a-zaleznosci-zewnetrzne.tex`; skrypt zapisuje pliki
pomocnicze w `build/tomy`, a sprawdzone PDF-y w katalogu projektu.

**Polecenia wykonane.** W korzeniu repozytorium wykonano:

```powershell
git fetch origin
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
```

Wynik porównania wyniósł `1 0`: lokalny commit `68053da`
dotyczący innego projektu był już przed bieżącą zmianą.
W katalogu projektu uruchomiono pełny skład w tle poleceniem:

```powershell
$donaldsonBuild = Start-Process -FilePath 'powershell.exe' `
  -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File','.\buduj_tomy.ps1') `
  -WorkingDirectory (Get-Location).Path `
  -RedirectStandardOutput 'build\tomy\donaldson-stage3.stdout.txt' `
  -RedirectStandardError 'build\tomy\donaldson-stage3.stderr.txt' `
  -WindowStyle Hidden -PassThru
$donaldsonBuild.Id
```

Proces otrzymał identyfikator `10212`. Po trzech obiegach skrypt
zakończył się komunikatem
`Four volumes built, indexes checked, PDFs copied.`
W katalogu projektu wykonano kontrolę:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|multiply defined|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same -or -not $index) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same, index=$index" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
```

Kontrola zakończyła się kodem `0`. Tomy I–IV mają 216, 182,
104 i 88 stron. Indeksy przyjęły 113, 96, 33 i 96 wpisów,
bez odrzuceń. Nie było brakujących lub powielonych etykiet,
przepełnionych wierszy ani brakujących znaków. Każdy PDF ma
trzy łącza do pozostałych tomów i zgodną z kopią sumę SHA-256.
Wykonano poniższe polecenia dla tomu IV i obejrzano tekst,
wzory, przypisy oraz układ fizycznych stron 52–56 i 71–72:

```powershell
pdftotext -enc UTF-8 -layout build/tomy/geometria_tom4.pdf build/tomy/donaldson-stage3-final.txt
pdftoppm -f 52 -l 56 -scale-to 1500 -png build/tomy/geometria_tom4.pdf build/tomy/donaldson-stage3-final-page
pdftoppm -f 71 -l 72 -scale-to 1500 -png build/tomy/geometria_tom4.pdf build/tomy/donaldson-stage3-appendix
git diff --check
```

`git diff --check` przeszedł bez błędów.

**Instrukcja przygotowana do samodzielnego wykonania.** Po dalszych
zmianach źródła uruchom z katalogu projektu:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/donaldson-stage3-rerun.txt
```

Po komunikacie o zbudowaniu czterech tomów powtórz kontrolę PDF-ów,
indeksów i łączy podaną w następnym wpisie o Freedmanie.

### Przykłady Freedmana — przebieg pracy 29 października 2026

Katalog roboczy składu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Środowisko jak w poprzednim etapie: Windows PowerShell 5.1.19041.6456,
MiKTeX 25.12 (`makeindex` z MiKTeX), `latexmk` 4.88, Perl 5.42.3
z Git for Windows i Poppler 24.04.0. Nie instalowano nowych zależności,
nie pobierano danych i nie ustawiano nowych zmiennych środowiskowych.
`buduj_tomy.ps1` sam dodaje Perla do `PATH`, gdy jest to potrzebne.

**Polecenia wykonane.** W katalogu głównym repozytorium wykonano
`git fetch origin` oraz:

```powershell
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
```

Wynik porównania wyniósł `0 0`. W katalogu projektu podjęto pełny skład:

```powershell
Set-Location -LiteralPath 'C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa'
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/freedman-stage2-build.txt
```

Pierwszy przebieg zakończył się błędem LaTeX w opcjonalnym tytule
przykładu zawierającym `$[1]$`; tytuł poprawiono w źródle.
Wykonano ponowienie:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/freedman-stage2-build-final.txt
```

Ten przebieg przerwano; pozostawił ucięty plik pomocniczy `aux`.
Próba uruchomiona w tle z zapisami
`build/tomy/freedman-stage2-background.stdout.txt` i
`build/tomy/freedman-stage2-background.stderr.txt` zakończyła się
błędem odczytu pliku `aux`. Następnie metodą
`[System.IO.File]::WriteAllText` opróżniono dokładnie sześć
wygenerowanych plików: `geometria_tom2.{aux,toc,out}` i
`geometria_tom4.{aux,toc,out}` w `build/tomy`.
Wykonano dokładnie:

```powershell
$paths = @('build/tomy/geometria_tom2.aux',
  'build/tomy/geometria_tom2.toc',
  'build/tomy/geometria_tom2.out',
  'build/tomy/geometria_tom4.aux',
  'build/tomy/geometria_tom4.toc',
  'build/tomy/geometria_tom4.out')
foreach ($path in $paths) {
  $full = [System.IO.Path]::GetFullPath($path)
  [System.IO.File]::WriteAllText($full, '')
}
```

Kolejny pełny skład uruchomiono w tle poleceniem:

```powershell
$freedmanBuild = Start-Process -FilePath 'powershell.exe' `
  -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File','.\buduj_tomy.ps1') `
  -WorkingDirectory (Get-Location).Path `
  -RedirectStandardOutput 'build\tomy\freedman-stage2-repaired.stdout.txt' `
  -RedirectStandardError 'build\tomy\freedman-stage2-repaired.stderr.txt' `
  -WindowStyle Hidden -PassThru
$freedmanBuild.Id
```

Proces miał identyfikator `9084`. Zakończył się komunikatem
`Four volumes built, indexes checked, PDFs copied.` po dwóch obiegach.

**Kontrola wykonana po składzie.** W katalogu projektu sprawdzono
wszystkie cztery tomy następującym poleceniem:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
```

Kontrola zakończyła się kodem 0. Tomy I–IV mają odpowiednio
216, 182, 104 i 85 stron; indeksy przyjęły 113, 96, 33 i 96 haseł,
wszystkie bez odrzuceń. Nie było niezdefiniowanych odsyłaczy,
przepełnionych wierszy ani brakujących znaków. Każdy tom ma trzy
łącza do pozostałych i sumę SHA-256 zgodną z kopią w `build/tomy`.
Wyrenderowano i obejrzano fizyczne strony 45–48 oraz 68 tomu IV:
teksty, wzory, odsyłacze, tabela i podpisy są czytelne.
Wykonano też `git diff --check` bez błędów.

**Instrukcja przygotowana do samodzielnego wykonania.** Po zakończeniu
zmian w źródle uruchom z powyższego katalogu:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/freedman-stage2-rerun.txt
```

Po udanym składzie powtórz powyższy blok kontroli. Do oglądania
stron użyj `pdftoppm` jak w wykonanych poleceniach:

```powershell
pdftoppm -f 45 -l 48 -scale-to 1700 -png geometria_tom4.pdf build/tomy/freedman-stage2-page
pdftoppm -f 68 -l 68 -scale-to 1700 -png geometria_tom4.pdf build/tomy/freedman-stage2-appendix
```

### Trzy rachunki chirurgii — polecenia wykonane 28 października 2026

Zmiany dotyczą rozdziałów 26–27 i dodatku A na gałęzi
`review/rozdzialy-matematyka`. Katalog projektu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie pobierano danych ani nie instalowano zależności. Użyto Windows
PowerShell 5.1.19041.6456, MiKTeX 25.12, `latexmk` 4.88, Perla 5.42.3
z Git for Windows i Popplera 24.04.0. `makeindex` pochodzi z MiKTeX.
Projekt nie wymaga własnych zmiennych środowiskowych; skrypt budujący
sam dodaje katalog Perla do `PATH`.

**Polecenia wykonane.** W katalogu głównym repozytorium pobrano stan
zdalnej gałęzi i porównano historię. Zdalna gałąź nie miała wtedy nowych
commitów względem lokalnej, która była o jeden commit do przodu:

```powershell
git fetch origin
git rev-list --left-right --count HEAD...origin/review/rozdzialy-matematyka
```

W katalogu projektu złożono wszystkie cztery tomy wraz z indeksami:

```powershell
Set-Location -LiteralPath 'C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa'
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Skrypt zakończył się kodem 0 po trzech przebiegach. Następnie w tym
samym katalogu wykonano kontrolę PDF-ów, indeksów, logów, łączy i kopii:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
```

Tomy I–IV mają 216, 182, 104 i 83 strony; indeksy przyjęły odpowiednio
113, 96, 33 i 94 wpisy bez odrzuceń. Nie znaleziono wskazanych ostrzeżeń
w logach. Każdy tom ma trzy łącza do pozostałych, a kopie PDF w
`build/tomy` są zgodne bitowo. Poleceniem `pdftoppm` wyrenderowano
fizyczne strony 42–43 i 57–59 tomu III oraz 63–64 tomu IV;
obejrzano strony z nowym tekstem i dodatkiem A. W katalogu repozytorium
wykonano `git diff --check` bez błędów.

**Instrukcja przygotowana do samodzielnego wykonania.** Na innym
stanowisku przygotuj wymienione wersje MiKTeX, Perla i Popplera,
przejdź do katalogu projektu poleceniem `Set-Location` powyżej,
uruchom pełny `buduj_tomy.ps1` i powtórz blok kontroli. Do obejrzenia
zmienionych stron służą na przykład:

```powershell
pdftoppm -f 42 -l 43 -scale-to 1500 -png geometria_tom3.pdf "$env:TEMP\geom-stage1-early"
pdftoppm -f 57 -l 59 -scale-to 1500 -png geometria_tom3.pdf "$env:TEMP\geom-stage1-late"
pdftoppm -f 63 -l 64 -scale-to 1500 -png geometria_tom4.pdf "$env:TEMP\geom-stage1-appendix"
```

### Most między wymiarami trzy i cztery — polecenia wykonane 28 października 2026

Praca dotyczy `tex/rozdzialy/31-freedman-formy-przeciecia.tex` na gałęzi
`review/rozdzialy-matematyka`. Katalog roboczy składu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie pobierano danych ani nie instalowano nowych zależności.
Środowisko jak w poprzednim wpisie: Windows PowerShell 5.1,
MiKTeX 25.12, `latexmk` 4.88, `makeindex` z MiKTeX 25.12,
Perl 5.42.3 z Git for Windows i Poppler 24.04.0.
Projekt nie wymaga własnych zmiennych środowiskowych; przy
bezpośrednim wywołaniu `latexmk` dodano katalog Perla do `PATH`.

**Polecenia wykonane.** W katalogu głównym repozytorium wykonano
`git pull --ff-only`; gałąź była aktualna. Następnie z katalogu
projektu wykonano podgląd i pełny skład:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -silent -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom4.tex *> build/tomy/bridge-preview.txt
pdftoppm -f 30 -l 31 -scale-to 1700 -png build/tomy/geometria_tom4.pdf "$env:TEMP\bridge-preview"
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/bridge-full-build.txt
pdftoppm -f 31 -l 31 -scale-to 1700 -png geometria_tom4.pdf "$env:TEMP\bridge-final"
```

Po doprecyzowaniu opisu brzegu wykonano ponownie pełny skład
i wyrenderowano końcową wersję strony:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/bridge-full-build-final.txt
pdftoppm -f 31 -l 31 -scale-to 1700 -png geometria_tom4.pdf "$env:TEMP\bridge-final-corrected"
```

Podgląd oraz oba pełne składy zakończyły się kodem 0.
Obejrzano fizyczną stronę 31 podglądu i końcowego tomu IV.
Po drugim składzie w katalogu projektu powtórzono blok kontroli:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
git diff --check
```

Kontrola zakończyła się kodem 0. Tomy I–IV mają 216, 182,
102 i 83 strony; indeksy przyjęły 113, 96, 30 i 94 wpisy
bez odrzuceń. W logach nie było niezdefiniowanych odsyłaczy,
przepełnionych wierszy ani brakujących znaków. Każdy tom ma
trzy łącza do pozostałych, a kopie PDF w `build/tomy` mają
zgodne sumy SHA-256.

**Instrukcja przygotowana do samodzielnego wykonania.** Na
innym stanowisku zainstaluj wersje narzędzi wymienione wyżej,
przejdź do wskazanego katalogu projektu, uruchom
`buduj_tomy.ps1` i powtórz blok kontroli. Nowy fragment
znajduje się na fizycznej stronie 31 tomu IV.

### Małe i duże egzotyczne $\R^4$ — polecenia wykonane 28 października 2026

Praca dotyczy `tex/rozdzialy/35-egzotyczne-r4.tex` na gałęzi
`review/rozdzialy-matematyka`. Katalog roboczy składu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie pobierano danych ani nie instalowano zależności. Używane wersje:
Windows PowerShell 5.1, MiKTeX 25.12, `latexmk` 4.88,
`makeindex` z MiKTeX 25.12, Perl 5.42.3 z Git for Windows
i Poppler 24.04.0 (`pdfinfo`, `pdftoppm`, `pdftohtml`).
Projekt nie wymaga własnych zmiennych środowiskowych;
bezpośrednie wywołanie `latexmk` wymaga Perla w `PATH`.

**Polecenia wykonane.** W katalogu głównym repozytorium wykonano
`git pull --ff-only`; gałąź była aktualna. W katalogu projektu
złożono podgląd tomu IV po przeniesieniu schematu na początek
sekcji:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -silent -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom4.tex *> build/tomy/r4-preview-final.txt
pdftoppm -f 59 -l 61 -scale-to 1700 -png build/tomy/geometria_tom4.pdf "$env:TEMP\r4-preview2"
```

Podgląd zakończył się kodem 0 i miał 83 strony. Obejrzano fizyczne
strony 59–60, w tym diagram porównawczy i dalszy opis. Następnie
uruchomiono pełny skład czterech tomów:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/r4-full-build.txt
```

Skrypt zakończył się kodem 0 po dwóch przebiegach. Tomy I–IV mają
216, 182, 102 i 83 strony. Po składzie wyrenderowano i obejrzano
strony 59–60 końcowego PDF z poprawioną etykietą węzła:

```powershell
pdftoppm -f 59 -l 60 -scale-to 1700 -png geometria_tom4.pdf "$env:TEMP\r4-final"
```

W katalogu projektu wykonano blok kontroli indeksów, logów,
łączy między tomami i zgodności kopii PDF:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
git diff --check
```

Kontrola zakończyła się kodem 0. Indeksy przyjęły kolejno
113, 96, 30 i 94 wpisy bez odrzuceń. Nie znaleziono
niezdefiniowanych odsyłaczy, przepełnionych wierszy ani
brakujących znaków. Każdy tom ma trzy łącza do pozostałych,
a kopie PDF mają zgodne sumy SHA-256. `git diff --check` przeszedł.

**Instrukcja przygotowana do samodzielnego wykonania.** Na nowym
stanowisku przygotuj środowisko według dalszych wpisów tego pliku,
przejdź do wskazanego katalogu projektu, uruchom `buduj_tomy.ps1`
i powtórz blok kontroli indeksów, odsyłaczy, łączy i sum SHA-256
z poprzedniego wpisu o Donaldsonie. Polecenia `pdftoppm` wyżej
pozwalają odtworzyć oględziny stron zmienionego rozdziału.

### Instanton BPST i analiza Donaldsona — polecenia wykonane 28 października 2026

Pracę nad `tex/rozdzialy/34-donaldson.tex` wykonano na gałęzi
`review/rozdzialy-matematyka`. Katalog roboczy poleceń składu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie pobierano danych ani nie instalowano nowych zależności.
Używane środowisko jest takie jak w zakończonym wpisie poniżej:
Windows PowerShell 5.1, MiKTeX 25.12, `latexmk` 4.88,
`makeindex` z MiKTeX 25.12, Perl 5.42.3 z Git for Windows
i Poppler 24.04.0. Projekt nie wymaga własnych zmiennych
środowiskowych; przy bezpośrednim wywołaniu `latexmk` Perl
musi być w `PATH`.

**Polecenia wykonane.** W katalogu głównym
repozytorium wykonano `git pull --ff-only`; gałąź była aktualna.
Po zmianie rozdziału wykonano doraźny skład tomu IV
z katalogu projektu:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -silent -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom4.tex *> build/tomy/donaldson-preview.txt
```

Doraźny skład zakończył się kodem 0. Do oględzin
wyrenderowano fizyczne strony 49--52:

```powershell
pdftoppm -f 49 -l 52 -scale-to 1700 -png build/tomy/geometria_tom4.pdf "$env:TEMP\donaldson-preview"
```

Na stronach 50--52 przykład BPST i tabela wejść analitycznych
mieszczą się w łamie i są czytelne. Następnie wykonano pełny
skład czterech tomów z katalogu projektu:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/donaldson-full-build.txt
```

Skrypt zakończył się kodem 0 po dwóch przebiegach. Tomy I--IV
mają odpowiednio 216, 182, 102 i 82 strony. W tym samym
katalogu wykonano blok kontroli indeksów, ostrzeżeń logu,
łączy między tomami i zgodności kopii PDF:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
```

Kontrola zakończyła się kodem 0. Indeksy przyjęły kolejno
113, 96, 30 i 94 wpisy bez odrzuceń. W logach nie znaleziono
niezdefiniowanych odwołań, przepełnionych wierszy ani brakujących
znaków. Każda strona tytułowa ma trzy łącza do pozostałych
tomów, a kopia każdego PDF ma zgodną sumę SHA-256.
`git diff --check` zakończył się kodem 0.

**Instrukcja przygotowana do samodzielnego wykonania.**
Na nowym stanowisku przygotuj środowisko według dalszych wpisów
tego pliku, przejdź do wskazanego katalogu projektu, uruchom
`buduj_tomy.ps1` i powtórz powyższy blok kontroli.

### Droga do klasyfikacji TOP w tomie IV — polecenia wykonane 28 października 2026

Pracę wykonano na gałęzi `review/rozdzialy-matematyka`.
W katalogu głównym repozytorium uruchomiono `git pull --ff-only`;
gałąź była aktualna. Nie pobierano danych projektu ani nie
instalowano nowych pakietów. Użyto istniejącego środowiska:
Windows PowerShell 5.1, MiKTeX 25.12, `latexmk` 4.88,
`makeindex` z MiKTeX 25.12, Perl 5.42.3 z Git for Windows
i Poppler 24.04.0
(`pdfinfo`, `pdftoppm`, `pdftohtml`). Katalog roboczy poleceń
składu to
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie są wymagane projektowe zmienne środowiskowe; bezpośrednie
wywołanie `latexmk` wymaga Perla w `PATH`.

Po zmianie rozdziałów 34 i 36 wykonano doraźny skład tomu IV:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom4.tex
```

Po doprecyzowaniu podpisu schematu, strzałki orientacji oraz
etykiet sfer powtórzono skład przez `latexmk -silent` z tymi
samymi opcjami i katalogiem wynikowym. Oba składy zakończyły
się kodem 0; drugi PDF miał 81 stron. Wyrenderowano strony
do oględzin:

```powershell
pdftoppm -f 34 -l 35 -scale-to 1600 -png build/tomy/geometria_tom4.pdf "$env:TEMP\freedman-hopf"
pdftoppm -f 45 -l 47 -scale-to 1600 -png build/tomy/geometria_tom4.pdf "$env:TEMP\freedman-route"
```

Na fizycznej stronie 35 jest diagram obramowanego splotu,
na 46 schemat zależności, a na 47 tabela przykładów.
Po tych oględzinach powiększono jeszcze tabelę; końcowe
sprawdzenie jej układu wykonano po pełnym składzie.

W katalogu projektu uruchomiono pełny skrypt z zapisem wyjścia:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1 *> build/tomy/full-build-run.txt
```

Skrypt zakończył się kodem 0 po dwóch przebiegach. Tomy I--IV
mają 216, 182, 102 i 81 stron. W tym samym katalogu wykonano
następujący blok kontroli indeksów, logów, łączy i kopii PDF:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$($v): $pages; $index; 3 łącza; SHA-256 zgodna"
}
```

Kontrola zakończyła się kodem 0. Indeksy przyjęły kolejno
113, 96, 30 i 93 wpisy bez odrzuceń; logi nie zawierają
wskazanych ostrzeżeń. Każdy tom ma trzy łącza do pozostałych
i kopię o zgodnej sumie SHA-256. Końcową tabelę ponownie
wyrenderowano i obejrzano poleceniem:

```powershell
pdftoppm -f 47 -l 47 -scale-to 1600 -png geometria_tom4.pdf "$env:TEMP\freedman-table-final"
```

Tabela, podpis i sąsiedni tekst są czytelne bez kolizji.
`git diff --check` zakończył się kodem 0 bez błędów białych znaków.

### Instrukcja przygotowana do samodzielnego wykonania

Na nowym stanowisku użyj instrukcji instalacji z dalszej części
tego pliku, przejdź do wskazanego katalogu projektu, uruchom
`buduj_tomy.ps1` i powtórz blok kontroli. Instalacji i pobierania
danych nie wykonywano w tej iteracji.

### Przykłady wizualne w rozdziale 26 — polecenia wykonane 28 października 2026

Pracę prowadzono na gałęzi `review/rozdzialy-matematyka`.
W katalogu głównym repozytorium wykonano `git pull --ff-only`;
gałąź była aktualna. Nie pobierano danych ani nie instalowano
nowych zależności. Użyto MiKTeX 25.12, `latexmk` 4.88,
`makeindex` z MiKTeX 25.12, Perla z Git for Windows oraz
Poppler 24.04.0. Katalog roboczy
poleceń składu to
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Nie są wymagane projektowe zmienne środowiskowe; przy wywołaniu
samego `latexmk` Perl musi być dostępny w `PATH`.

Po zmianie `tex/rozdzialy/22-chirurgia-geometryczna.tex`
uruchomiono doraźny skład tomu III. Pierwsze wywołanie
`latexmk` bez Perla w `PATH` zakończyło się błędem silnika
skryptowego. Powtórzono je po dodaniu Perla z Git for Windows:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom3.tex
```

To wywołanie zakończyło się kodem 0; doraźny PDF miał 102 strony,
a indeks przyjął 30 wpisów bez odrzuceń. Po obejrzeniu nowego
rysunku przypięto go do przykładu specyfikatorem `[H]`.
Następnie uruchomiono pełny skład czterech tomów poleceniem:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Pełny skład zakończył się kodem 0 po dwóch przebiegach.
Tomy I–IV mają 216, 182, 102 i 80 stron; ich indeksy
przyjęły odpowiednio 113, 96, 30 i 93 wpisy, bez odrzuceń.
W tym samym katalogu wykonano następujący blok kontroli:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się: bad=$($bad.Count), links=$($links.Count), same=$same" }
  "$v`: $pages; $index; 3 łącza; SHA-256 zgodna"
}
```

Kontrola zakończyła się kodem 0 dla wszystkich tomów:
nie znaleziono wskazanych ostrzeżeń w logach; każdy PDF
ma trzy łącza do pozostałych tomów na stronie tytułowej,
a kopie mają zgodne sumy SHA-256. Fizyczne strony 39–40
tomu III wyrenderowano i obejrzano poleceniem:

```powershell
pdftoppm -f 39 -l 40 -scale-to 1600 -png .\geometria_tom3.pdf "$env:TEMP\geometry-braid-verified"
```

Na stronie 39 kończy się tekst nowego przykładu, a stronę 40
otwiera rysunek 26.4. Rurki, obrzeża, strzałki, etykiety,
prześwity i podpis są czytelne, bez kolizji lub ucięć.

### Instrukcja przygotowana do samodzielnego wykonania

Na nowym stanowisku wykonaj instrukcje instalacji z dalszej
części tego pliku, przejdź do katalogu projektu i uruchom
`buduj_tomy.ps1` z powyższego bloku. Skrypt sam znajdzie
Perla z Git for Windows, jeśli jest w standardowym katalogu.
Instalacji i pobierania danych nie wykonywano w tej iteracji.

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

## Mapa hipotez chirurgii — 28 października 2026

Pracę wykonano na gałęzi `review/rozdzialy-matematyka`.
Sprawdzone wersje i wymagane narzędzia opisuje powyższa sekcja środowiska:
Windows PowerShell 5.1, MiKTeX 25.12, `latexmk` 4.88,
`makeindex` z MiKTeX 25.12, Perl 5.42.3 z Git for Windows,
Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`, `pdftohtml`) oraz Git.
Skrypt sam ustawia `PATH` dla Perla, jeśli jest potrzebny;
innych zmiennych środowiskowych projekt nie wymaga. Nie
instalowano zależności ani nie pobierano danych wejściowych.

### Polecenia faktycznie wykonane

W katalogu głównym repozytorium wykonano:

```powershell
git status --short --branch
git pull --ff-only
```

Drzewo było czyste przed pracą, a `git pull` zwrócił
`Already up to date.`. Katalog składu:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Podawano go przez parametr katalogu roboczego wykonania.
Po zmianie źródła uruchomiono skrypt pełnego składu:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Po niezależnej kontroli hipotez poprawiono dwie niejednoznaczności
dotyczące końcowego $s$-kobordyzmu i warunku brzegowego, po czym
uruchomiono ten sam skrypt ponownie. Do kontroli wyników służy
poniższy blok, wykonywany z katalogu geometrii:

```powershell
1..4 | ForEach-Object {
  $volName = "geometria_tom$_"
  $pages = (pdfinfo "$volName.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$volName.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$volName.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$volName.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$volName.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$volName.pdf" -Algorithm SHA256).Hash
  if (-not $index -or $bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $volName nie powiodła się" }
  '{0}: {1}; {2}; 3 łącza; SHA-256 zgodna' -f $volName, $pages, $index
}
```

Blok wykonano po końcowym składzie i zwrócił kod 0. Tomy I–IV mają
216, 182, 100 i 80 stron. Indeksy przyjęły 113, 96, 29 i 93 wpisy,
bez odrzuconych. Nie znaleziono niezdefiniowanych odsyłaczy,
`Overfull` ani brakujących znaków; każda strona tytułowa ma trzy
łącza do pozostałych tomów, a kopie PDF są zgodne według SHA-256.
Indeks tomu III powiększył się o hasło dotyczące hipotez.

Wykonano także kontrolę tekstu i wizualną stron fizycznych 78–80
tomu III:

```powershell
pdftotext -f 79 -l 79 -layout geometria_tom3.pdf - | Select-String -Pattern 'Gładkie twierdzenie|W naszym ciągu|twierdzeń 5.6|Crowley' -Context 0,2
pdftohtml -q -xml -f 79 -l 79 -stdout geometria_tom3.pdf | Select-String -Pattern 'href="geometria_tom4.pdf' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique
pdftoppm -f 78 -l 80 -scale-to 1400 -png geometria_tom3.pdf "$env:TEMP\geometry-map-final"
```

Na stronie 79 tabela, przypadek $n=5$ i źródła są czytelne.
Odsyłacz do rozdziału 36 kieruje do tomu IV. Poprzednia i następna
strona są poprawnie złożone; przykład śladu ma obecnie numer 28.6.2
i zaczyna się na stronie fizycznej 80. W katalogu głównym repozytorium
`git diff --check` zakończył się kodem 0 bez błędów białych znaków.

### Instrukcja przygotowana do samodzielnego wykonania

Na innym stanowisku zastosuj instrukcję instalacji narzędzi z początku
tego pliku, przejdź do wskazanego katalogu geometrii i wykonaj skrypt
`buduj_tomy.ps1` oraz blok kontroli powyżej. Ręcznego ustawienia
`PATH` nie potrzeba przy użyciu skryptu. Dodatkowych danych do
pobrania nie ma.

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

## Uzupełnienie rozdziału 28 tomu III — 27 października 2026

Pracę prowadzono na gałęzi `review/rozdzialy-matematyka`.
W katalogu głównym repozytorium wykonano `git status --short --branch`
i `git pull --ff-only`; gałąź była aktualna i czysta.
Nie pobierano danych ani nowych zależności. Obowiązuje środowisko
opisane na początku sekcji geometrii: MiKTeX 25.12, `latexmk` 4.88,
`makeindex` z MiKTeX 25.12 i Perl z Git for Windows.
Katalog roboczy składu to
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`.
Polecenie wejścia do niego podano w pierwszej sekcji tego pliku;
w tej iteracji katalog ustawiono parametrem `workdir` wykonania.

### Polecenia wykonane

Po edycji `tex/rozdzialy/24-ciag-chirurgii.tex` uruchomiono
doraźny skład tomu III:

```powershell
$perlGit = 'C:\Program Files\Git\usr\bin'
if (-not (Get-Command perl -ErrorAction SilentlyContinue) -and
    (Test-Path -LiteralPath (Join-Path $perlGit 'perl.exe'))) {
  $env:PATH = "$perlGit;$env:PATH"
}
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/tomy geometria_tom3.tex
```

Pierwszy przebieg wykrył błędną składnię etykiety w nowym diagramie
`tikzcd` i zatrzymał `pdflatex` na tej linii. Po poprawie źródła
`latexmk` ponowił skład, zakończył się kodem 0 i zbudował tom III.
Indeks przyjął 28 haseł bez odrzuceń. Doraźny PDF miał 99 stron;
ostateczny wynik zapisuje pełny skład poniżej.

Pełny skład wszystkich tomów uruchomiono w tym samym katalogu:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Po doprecyzowaniu warunku na brzegu ponowiono pełny skład tym samym
poleceniem. Ostatni przebieg zakończył się kodem 0 po dwóch rundach.
PDF-y tomów I--IV mają odpowiednio 216, 182, 99 i 80 stron.
Indeksy przyjęły 113, 96, 28 i 93 hasła bez odrzuceń.
W katalogu geometrii wykonano również następującą kontrolę:

```powershell
1..4 | ForEach-Object {
  $v = "geometria_tom$_"
  $pages = (pdfinfo "$v.pdf" | Select-String '^Pages:').Line.Trim()
  $index = (Select-String -Path "build/tomy/$v.ilg" -Pattern 'entries accepted, 0 rejected').Line.Trim()
  $bad = @(Select-String -Path "build/tomy/$v.log" -Pattern 'LaTeX Warning: Reference .* undefined|There were undefined references|Label\(s\) may have changed|Overfull \\hbox|Missing character')
  $links = @(pdftohtml -q -xml -f 1 -l 1 -stdout "$v.pdf" | Select-String 'href="geometria_tom[1-4]\.pdf"' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique)
  $same = (Get-FileHash "$v.pdf" -Algorithm SHA256).Hash -eq (Get-FileHash "build/tomy/$v.pdf" -Algorithm SHA256).Hash
  if ($bad.Count -ne 0 -or $links.Count -ne 3 -or -not $same) { throw "Kontrola $v nie powiodła się" }
  "$v`: $pages; indeks OK; 3 łącza; SHA-256 zgodna"
}
```

Kontrola zakończyła się kodem 0 dla każdego tomu: brak wskazanych
ostrzeżeń w logach, na stronach tytułowych po trzy łącza do pozostałych
PDF-ów, a wyniki składu zgadzają się z kopiami w katalogu projektu.
Strony PDF 75--79 tomu III obejrzano po składzie; nowe diagramy,
ciąg względny i etykiety są czytelne oraz mieszczą się na stronach.

### Instrukcja przygotowana do samodzielnego wykonania

Na nowym stanowisku najpierw użyj instrukcji instalacji narzędzi
z początku sekcji geometrii. Potem przejdź do katalogu projektu,
uruchom `buduj_tomy.ps1` z bloku powyżej i sprawdź logi oraz
indeksy. Instalacji i pobierania nie wykonywano w tej iteracji.

## Śledzony przykład przez rozdziały 26–28 — 27 października 2026

Pracę prowadzono na gałęzi `review/rozdzialy-matematyka`.
W katalogu głównym repozytorium wykonano:

```powershell
git status --short --branch
git pull --ff-only
```

Drzewo było czyste, a gałąź aktualna. Nie pobierano danych ani
nie instalowano zależności. Wymagane narzędzia pozostają jak
w sekcji geometrii: MiKTeX 25.12, `latexmk` 4.88, `makeindex`
z MiKTeX 25.12, Perl z Git for Windows oraz `pdfinfo`,
`pdftohtml`, `pdftoppm` z pakietu Poppler w MiKTeX.
Katalog roboczy składu to
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\geometria i topologia różniczkowa`;
ustawiono go parametrem `workdir` wykonania.

### Polecenia wykonane

Po zmianach w `tex/rozdzialy/22-chirurgia-geometryczna.tex`,
`23-przeszkoda-chirurgiczna.tex` i `24-ciag-chirurgii.tex`
uruchomiono pełny skład:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Po niezależnym przeglądzie doprecyzowano wybór danych normalnych
i ponowiono skład tym samym poleceniem. Dokładne polecenia kontroli
liczby stron, indeksów, logów, łączy i sum SHA-256 znajdują się
w sekcji „Uzupełnienie rozdziału 28 tomu III” powyżej; po ostatnim
składzie wykonano ten sam blok kontroli. Ostatni skład zakończył się
po dwóch przebiegach: tomy I–IV mają 216, 182, 99 i 80 stron.
Indeksy przyjęły odpowiednio 113, 96, 28 i 93 wpisy, odrzuciły zero.
Kontrola logów, trzech łączy do innych tomów na każdej stronie
tytułowej i sum SHA-256 kopii PDF zakończyła się bez błędów.
Wizualnie sprawdzono strony 43 i 51 tomu III. Po dostrzeżeniu
urwanego początku przykładu w rozdziale 28 dodano przed nim
`\clearpage` i wykonano opisany wyżej pełny skład oraz blok kontroli
ponownie. Strony PDF 77–79 wyrenderowano poleceniem:

```powershell
pdftoppm -f 77 -l 79 -scale-to 1400 -png geometria_tom3.pdf "$env:TEMP\geometry-example-final"
```

Na stronie PDF 79 przykład 28.5.2 zaczyna się od góry; tekst,
wzory i dalsze wyniki są czytelne, bez ucięć i kolizji.

### Instrukcja przygotowana do samodzielnego wykonania

Na innym stanowisku wykonaj instrukcję instalacji z początku
sekcji geometrii, przejdź do wskazanego katalogu i uruchom
`buduj_tomy.ps1` oraz blok kontroli z poprzedniej sekcji.
Instalacji i pobierania nie wykonywano w tym etapie.

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

## Skrypt Banacha--Tarskiego — korekta językowa 29 października 2026

Katalog roboczy:
`C:\Users\DXD\Desktop\projekty\Latex\mathematical_scipts\banach_tarski`.
Użyto istniejącego środowiska MiKTeX 25.12, `latexmk` 4.88,
Perla z Git for Windows i Popplera. Nie pobierano danych ani
nie instalowano zależności. Źródłem jest
`banach_tarski_przepisany.tex`; wynik zapisano jako
`banach_tarski_przepisany.pdf`.

**Polecenia faktycznie wykonane w katalogu skryptu:**

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error banach_tarski_przepisany.tex
rg -n 'Overfull|Underfull|LaTeX Warning|Package .* Warning|Undefined control|Emergency stop|Output written' banach_tarski_przepisany.log
pdfinfo banach_tarski_przepisany.pdf | Select-String -Pattern 'Pages:|Page size:|File size:|PDF version:'
pdftotext -f 1 -l 3 -layout banach_tarski_przepisany.pdf -
$out = Join-Path $env:TEMP 'bt-lang-page-3'
pdftoppm -f 3 -l 3 -singlefile -scale-to 1400 -png banach_tarski_przepisany.pdf $out
$out = Join-Path $env:TEMP 'bt-lang-page-17'
pdftoppm -f 17 -l 17 -singlefile -scale-to 1400 -png banach_tarski_przepisany.pdf $out
```

W korzeniu repozytorium wykonano `git fetch origin` i
`git diff --check`. Skład dał 19 stron A4 i plik o wielkości
473525 bajtów. W logu znaleziono wyłącznie `Output written`,
bez błędów i ostrzeżeń. Obejrzano strony 3 i 17.

**Instrukcja przygotowana do samodzielnego wykonania.** Na nowym
stanowisku przygotuj MiKTeX, Git z Perlem i Poppler według
wcześniejszego wpisu z 27 października. Przejdź do katalogu
`banach_tarski`, ustaw `PATH` i uruchom powyższe
polecenia. Tej instalacji w bieżącej iteracji nie wykonywano.

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
