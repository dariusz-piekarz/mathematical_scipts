# Biblioteka matematyczna — parser LaTeX i indeks SQLite

**Wersja pierwszego modułu aplikacji — 19.11.2026.** To działający backend indeksujący LaTeX. **Nie obejmuje jeszcze interaktywnego Explorera, przeglądarki HTML ani generatora PDF.**

## Założenie

- `rozdzialy/*.tex` — kanoniczne źródła treści (233 pliki w tej migawce).
- `backend/latex_parser.py` — statyczny parser sekcji, środowisk matematycznych, `\label`, `\ref`, `\eqref` oraz wybranych wariantów odsyłaczy.
- `data/biblioteka.db` — **odtwarzalny** indeks SQLite: nie zastępuje plików `.tex`.
- `config/ALIASY_PO_SCALENIACH.json` — historyczne mapowania etykiet i rozdziałów (informacyjne, nie są automatycznie używane jako przekierowania podczas rozwiązywania odsyłaczy).
- `tests/` — testy regresyjne.

### Lokalna instalacja (Windows / Linux)

Wymagany Python 3.10+; brak zależności pip. Z katalogu tego projektu (w archiwum ZIP):

```bash
python backend/latex_parser.py index --source rozdzialy --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json --report data/indeksowanie_raport.json
python backend/latex_parser.py stats
python backend/latex_parser.py search --query "Lefschetza"
python backend/latex_parser.py show --label "ch:pierscienie"
python backend/latex_parser.py graph --source ALG-09 --format json
python backend/latex_parser.py plan --modules ALG-09
python backend/latex_parser.py audit
python -m unittest discover -s tests -v
```

Na Windows można użyć też `./build_index.ps1` w PowerShellu. Po każdej zmianie w źródłach należy ponownie uruchomić `index`.

**Jeśli kod jest umieszczony w Bibliotece ChatGPT pod `aplikacja/`, a pliki `.tex` są w sąsiednim katalogu `rozdzialy/`,** uruchom z folderu `aplikacja`:

```powershell
python backend/latex_parser.py index --source ../rozdzialy --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json
```

To działa po pobraniu katalogów na dysk. Foldery Biblioteki ChatGPT nie są automatycznie widoczne jako dysk lokalny przez program Python.

## Model danych

| Tabela | Zawartość |
|---|---|
| `documents` | ID modułu, nazwa, temat, SHA-256, cała treść TeX |
| `entities` | Rozdziały, sekcje i podsekcje, definicje, twierdzenia, lematy, dowody, przykłady, zadania, wzory, rysunki i kod; granice fragmentów (offsety/linie), hierarchia |
| `labels` | Unikatowa etykieta `\label`, jej lokalizacja i obiekt macierzysty |
| `references_tex` | Odsyłacze i ich rozwiązanie do konkretnych etykiet/modułów |
| `historical_aliases` | Historia zmian nazw etykiet ze scaleń |
| `dependency_edges` | Widok skierowanych połączeń między modułami i liczba odsyłaczy |
| `document_fts`, `entity_fts` | Indeksy wyszukiwania pełnotekstowego FTS5 (jeśli dostępne w SQLite) |

ID modułu pochodzi z prefiksu pliku, np. `ALG-09`. **Obiekt oznaczony `\label` dostaje ID `label:...`**, stabilne przy przesunięciu w pliku, o ile etykieta zachowuje swoje znaczenie. Obiekty bez etykiety otrzymują techniczne identyfikatory pozycyjne, np. `ALG-09/example/0007` — nie należy wykorzystywać ich jako trwałych publicznych odsyłaczy, zanim nie dodamy im jawnych ID.

Dymki odsyłaczy będą mogły użyć tabel `references_tex` → `labels` → `entities` i wyświetlać odpowiedni zakres treści `.tex` zapisany w `documents.content`. Późniejszy frontend będzie potrzebował bezpiecznego renderera matematyki (np. KaTeX/MathJax) i osobnego API.

## Wybór rozdziałów i `xr-hyper`

```bash
python backend/latex_parser.py plan --modules ALG-09
```

Zwraca osobno liczbę odsyłaczy wewnętrznych i listę **zewnętrznych celów**, czyli istniejących w Bibliotece etykiet ze skryptów pominiętych w kompilacji. Generator skryptów będzie mógł na tej podstawie włączyć moduł źródłowy lub stworzyć zewnętrzny dokument referencyjny, skompilować jego `.aux` i użyć `xr-hyper`. **Parser nie tworzy jeszcze plików `.aux` i nie wykonuje kompilacji.**

## Migawka i weryfikacja

Dla zestawu 233 rozdziałów z 19.11.2026:

- **233** moduły;
- **8686** obiektów strukturalnych (w tym **1778** obiektów typu twierdzenie/stwierdzenie/lemat/wniosek, **835** definicji i **1706** dowodów);
- **2363** etykiety;
- **1515** odwołań;
- **299** skierowanych połączeń między różnymi modułami;
- **0** nierozwiązanych odwołań i **0** kolizji etykiet w analizowanym zbiorze;
- **14** automatycznych testów zakończonych pomyślnie.

Raport w `data/indeksowanie_raport.json` dokumentuje stan wejścia. Baza jest migawką plików, nie usługą synchronizacji w czasie rzeczywistym.

## Granice parsera

Parser jest **statyczny**. Rozpoznaje typowe polecenia LaTeX i polskie środowiska matematyczne; usuwa komentarze i kod w środowiskach verbatim, zachowując offsety. Nie jest kompletnym interpreterem TeX: nie rozwija `\newcommand`, nie analizuje warunkowej kompilacji ani nie wykryje etykiet generowanych dynamicznie przez makra. Weryfikacja odsyłaczy w bazie jest kontrolą składniową, nie zastępuje kompilacji `latexmk` ani audytu matematycznego.

W katalogu nadrzędnym `Biblioteka matematyczna/rozdzialy` istnieją też robocze podfoldery. Domyślnie indeksowane są **wyłącznie bezpośrednie** pliki `.tex`, aby nie mieszać ich ze wspólnym kanonicznym zbiorem. Można użyć `--recursive`, jeśli świadomie chcemy indeksować również podfoldery.

## Kolejne moduły

Planowane: `backend/api.py` (FastAPI), explorer HTML/CSS/JS, widok grafu (NetworkX/Cytoscape.js), przeglądanie po kliknięciu etykiety, generator skryptów z `xr-hyper`, a także trwałe ID dla fragmentów bez `\label` i analiza zależności matematycznych wykraczająca poza jawne odsyłacze.
