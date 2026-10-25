# Geometria i topologia różniczkowa

Polski skrypt z geometrii i topologii różniczkowej. Codzienny skład obejmuje
trzy tomy: `geometria_tom1.pdf`, `geometria_tom2.pdf` i `geometria_tom3.pdf`.
Dotychczasowy dokument zbiorczy `geometria_i_topologia_rozniczkowa.tex`
pozostaje dostępny do okazjonalnego składu całej książki.

## Struktura źródeł

```text
geometria_i_topologia_rozniczkowa.tex   kolejność części i początek/koniec dokumentu
geometria_tom1.tex                    tom I: rozdziały 1–10
geometria_tom2.tex                    tom II: rozdziały 11–22
geometria_tom3.tex                    tom III: rozdziały 23–38 i dodatki
buduj_tomy.ps1                        pełny skład trzech tomów i indeksów
tex/
  preambula.tex                      pakiety, makra, kolory, liczniki i nagłówki
  wstep.tex                          spis treści, mapa książki i oznaczenia
  tomy/wstep-tomowy.tex              okładka i nawigacja między tomami
  rozdzialy/01-rozmaitosci.tex         rozdział 1
  rozdzialy/02-pola-wektorowe.tex      rozdział 2
  rozdzialy/...                       pozostałe rozdziały, po jednym na plik
  rozdzialy/27-chern-weil.tex          Chern–Weil
  rozdzialy/28-hodge-bochner.tex       Hodge–Bochner
  rozdzialy/29-grupy-liego.tex         grupy Liego
  rozdzialy/29a-geometria-kleina.tex   geometria Kleina i przestrzenie jednorodne
  rozdzialy/30-potok-ricciego.tex      potok Ricciego
  rozdzialy/30a-poincare-trzy.tex       Poincaré w wymiarze trzy
  rozdzialy/30b-geometrizacja-thurstona.tex  geometrie Thurstona
  rozdzialy/31-freedman-formy-przeciecia.tex  formy w wymiarze cztery
  rozdzialy/32-uchwyty-cassona.tex     uchwyty Cassona
  rozdzialy/33-freedman-klasyfikacja.tex  klasyfikacja Freedmana
  rozdzialy/34-donaldson.tex          przeszkoda Donaldsona
  rozdzialy/35-egzotyczne-r4.tex       egzotyczne R⁴, włączone do składu
  dodatki/a-zaleznosci-zewnetrzne.tex  dodatek o wynikach zewnętrznych
  dodatki/b-homologia-singularna-euler.tex  dodatek o homologii singularnej i cesze Eulera
  dodatki/c-algebry_grupy_macierzowe.tex  grupy macierzowe i ich wymiary
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

Dokument zbiorczy obejmuje 38 rozdziałów w pięciu częściach
i trzy dodatki. Rozdział o Donaldsonie poprzedza rozdział o egzotycznych
strukturach na $\R^4$; oba są na liście importów.
Trzy tomy zachowują numery rozdziałów i etykiety dokumentu zbiorczego.
Tomy czytają pliki `.aux` pozostałych tomów przez `xr-hyper`; odsyłacze
między tomami prowadzą do PDF-ów położonych w tym samym katalogu.
Każdy tom ma własny spis treści i indeks. Dodatki znajdują się w tomie III.
Prefiksy nazw istniejących plików są historyczne; numer rozdziału
w składzie wyznacza wyłącznie kolejność `\input` w pliku głównym.

## Kompilacja

Wszystkie polecenia uruchamiaj z katalogu `geometria i topologia różniczkowa`
w repozytorium. Pliki główne, `tex/`, `build/` i `buduj_tomy.ps1` znajdują się
w nim na tym samym poziomie, więc ścieżki względne w poleceniach pozostają
aktualne.
Potrzebny jest LaTeX z pakietami wymienionymi w preambule, `makeindex`
oraz opcjonalnie `latexmk` i Perl. Pełny skład wraz z indeksem:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\buduj_tomy.ps1
```

Skrypt składa tomy w `build/tomy`, powtarza przebiegi do ustabilizowania
odsyłaczy, sprawdza logi i indeksy, a następnie kopiuje trzy PDF-y do
katalogu głównego. Po zmianie jednego rozdziału można doraźnie złożyć
tylko jego tom poleceniem `latexmk -pdf -interaction=nonstopmode
-halt-on-error -file-line-error -outdir=build/tomy geometria_tomN.tex`.
Przed publikacją trzech tomów uruchom jednak cały skrypt, aby odsyłacze
w pozostałych PDF-ach otrzymały aktualne numery i strony.

Okazjonalny pełny skład dokumentu zbiorczego:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/sklad geometria_i_topologia_rozniczkowa.tex
```

Na bieżącym komputerze Perl jest dostępny w instalacji Git.
Jeśli MiKTeX nie znajduje Perla, przed powyższym poleceniem ustaw w tej sesji:

```powershell
$env:PATH = 'C:\Program Files\Git\usr\bin;' + $env:PATH
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

Dokumentacja właściwa temu skryptowi ma cztery pliki, każdy o osobnej roli:

- [README.md](README.md) — struktura źródeł, kompilacja i współpraca.
- [AGENTS.md](AGENTS.md) — zasady pisania i kontroli.
- [PRZEGLAD.md](PRZEGLAD.md) — chronologiczny log zmian z uzasadnieniami
  i wynikami weryfikacji, także historyczny audyt wersji 18-rozdziałowej.
- [PLAN_DZIALANIA.md](PLAN_DZIALANIA.md) — jedyna aktualna lista zadań,
  pokrycie przeglądem i pozostałe propozycje rozbudowy.

W katalogu głównym repozytorium są ponadto [manual.md](../manual.md)
z odtwarzalnymi poleceniami środowiska, budowania i kontroli oraz
[mods.md](../mods.md) z uzasadnieniami zmian wykonywanych w projektach.

Nie kopiuj statusów zadań do kolejnych plików. Wpis w dzienniku opisuje
konkretną wersję; obecność rozdziału w książce nie oznacza zakończonego audytu.
