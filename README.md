# Geometria i topologia różniczkowa

Polski skrypt z geometrii i topologii różniczkowej. Głównym dokumentem
jest `geometria_i_topologia_rozniczkowa.tex`, a opublikowanym wynikiem
`geometria_i_topologia_rozniczkowa.pdf`.

## Struktura źródeł

```text
geometria_i_topologia_rozniczkowa.tex   kolejność części i początek/koniec dokumentu
tex/
  preambula.tex                      pakiety, makra, kolory, liczniki i nagłówki
  wstep.tex                          spis treści, mapa książki i oznaczenia
  rozdzialy/01-rozmaitosci.tex         rozdział 1
  rozdzialy/02-pola-wektorowe.tex      rozdział 2
  rozdzialy/...                       pozostałe rozdziały, po jednym na plik
  rozdzialy/27-chern-weil.tex          rozdział 27
  dodatki/a-zaleznosci-zewnetrzne.tex  dodatek o wynikach zewnętrznych
  indeks.tex                         indeks pojęć
build/                               ignorowane wyniki pomocnicze
```

Edytuj treść w pliku właściwego rozdziału. Wszystkie części należą do
jednego dokumentu i dzielą makra, liczniki oraz etykiety. Numer rozdziału
wynika z kolejności w pliku głównym; prefiks nazwy pliku pomaga go odnaleźć.
Używamy `\input`, aby podział nie wprowadzał dodatkowych przełamań stron.
Etykiet nie trzeba zmieniać przy przenoszeniu treści; ich nazwy muszą być
unikalne w całej książce. Nowy rozdział wymaga dodania pliku i odpowiedniego
`\input` w pliku głównym. Rysunki TikZ pozostają przy omawiającym je tekście.

## Kompilacja

Wszystkie polecenia uruchamiaj z katalogu głównego repozytorium.
Potrzebny jest LaTeX z pakietami wymienionymi w preambule, `makeindex`
oraz opcjonalnie `latexmk` i Perl. Pełny skład wraz z indeksem:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/sklad geometria_i_topologia_rozniczkowa.tex
```

Na komputerze z PortableGit z dysku E Perl jest już dostępny.
Jeśli MiKTeX nie znajduje Perla, przed powyższym poleceniem ustaw w tej sesji:

```powershell
$env:PATH = 'E:\Programs\Windows\PortableGit\usr\bin;' + $env:PATH
```

Bez `latexmk` można wykonać kolejno:

```powershell
New-Item -ItemType Directory -Force build/sklad | Out-Null
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build/sklad geometria_i_topologia_rozniczkowa.tex
makeindex build/sklad/geometria_i_topologia_rozniczkowa.idx
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build/sklad geometria_i_topologia_rozniczkowa.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build/sklad geometria_i_topologia_rozniczkowa.tex
```

Jeżeli ostatni log żąda kolejnego przebiegu, powtórz `pdflatex`; jeżeli
zmieniły się strony indeksowanych pojęć, uruchom ponownie również
`makeindex`. Po kontroli logu, odsyłaczy, indeksu i wyglądu zmienionych stron
zaktualizuj PDF w katalogu głównym:

```powershell
Copy-Item build/sklad/geometria_i_topologia_rozniczkowa.pdf geometria_i_topologia_rozniczkowa.pdf
```

## Współpraca i historia przeglądu

Przed pracą pobierz aktualny stan gałęzi. Uzgodnij zakres rozdziałów;
zmiany w różnych plikach łatwiej łączyć. Preambułę, plik główny i wspólny
PDF traktuj jako pliki współdzielone. PDF jest wynikiem kompilacji:
w razie konfliktu najpierw połącz źródła, następnie wygeneruj go ponownie.
Poprawki zapisuj z uzasadnieniem w [PRZEGLAD.md](PRZEGLAD.md).

Dokumentacja ma cztery pliki, każdy o osobnej roli:

- [README.md](README.md) — struktura źródeł, kompilacja i współpraca.
- [AGENTS.md](AGENTS.md) — zasady pisania i kontroli.
- [PRZEGLAD.md](PRZEGLAD.md) — chronologiczny log zmian z uzasadnieniami
  i wynikami weryfikacji, także historyczny audyt wersji 18-rozdziałowej.
- [PLAN_DZIALANIA.md](PLAN_DZIALANIA.md) — jedyna aktualna lista zadań,
  pokrycie przeglądem i pozostałe propozycje rozbudowy.

Nie kopiuj statusów zadań do kolejnych plików. Wpis w dzienniku opisuje
konkretną wersję; obecność rozdziału w książce nie oznacza zakończonego audytu.
