# Atlas matematyczny — iteration VI

**352 chapter modules in the bundled offline database:** existing 264 plus 20 differential geometry, 35 functional analysis and 33 PDE I chapters; the 31 measure-theory chapters have been refreshed, not duplicated. Their titles are navigable in Explorer. Book/TeX compilation sources remain canonical in the GitHub repository.

**Reference policy:** the parser indexes all explicit LaTeX labels and references. It records label collisions and does not silently redirect cross-book ambiguous references. The UI offers chapter choices when a label has multiple owners. Current snapshot reports 303 overlapping label names, 159 ambiguous references and 17 unresolved references; this is an audit backlog, not a passed global-reference check. Preserve original labels until the associated mathematical chapters have been deduplicated and their proofs compared.

**Cross-volume reading links:** use `\atlasref{existing-global-label}{visible description with the book/chapter ID}` for mathematically checked related material in another volume. The command's LaTeX fallback is `\providecommand{\atlasref}[2]{#2}`: standalone PDFs print the explicit bibliographic description; Atlas resolves the original label and shows a clickable reader reference and graph edge. Reading links are not proof dependencies or `xr-hyper` imports and must not force generator closure. Do not create placeholder labels or assume matching names prove equivalence. Prefer `\atlasref{TOP-11::thm:poincare-dualnosc-16}{TOP-11: dualność Poincarégo}` for a precise chapter/label occurrence. The qualified form does not rename the original label; a missing or ambiguous explicit target must not fall back to another module. Rebuild the SQLite index after changing canonical chapters. ALG-00–ALG-10 now link to AA and TOP with 38 reading references, including 22 qualified occurrences. The initial GA–AA coverage is GA-00–GA-09; the regression test checks all 14 chapter-pair links at module, section and entity levels.

**Source resolution:** when `../chapters/pl` exists (GitHub checkout), `build_index.ps1` and `start.ps1` index that canonical tree recursively; when it is absent (portable offline ZIP), use the bundled flat `rozdzialy/` snapshots. The index is stored in `data/biblioteka.db` and may be rebuilt without changing any TeX sources.

**Naming:** directory names and code APIs are English, while chapter text remains Polish. Chapter files use a numeric prefix and a human-readable slug; book entrypoints live in `books/pl/` in the repository.

**PDE:** the canonical book `books/pl/partial_differential_equations.tex` imports 33 chapters under `chapters/pl/partial_differential_equations/`. The whole source was split without dropping or rewriting TeX body material; its original monolith is archived in the associated source ZIP.

# Atlas matematyczny — aplikacja do wspólnej Biblioteki

**Current application version: 0.5 (264 indexed chapters, including measure theory and jets, plus drafts/save/X-close cleanup); historical 0.3 notes below.**

**Wersja 0.3 — API + Explorer + czytnik + graf zależności + generator skryptów z xr-hyper.**  
**Źródła:** 233 wspólne moduły `.tex` w `rozdzialy/` (migawka z 19.11.2026).  
**Architektura:** Python / FastAPI / SQLite, HTML / CSS / JavaScript (bez frameworka frontendowego), NetworkX do wyznaczania ścieżek. Frontend ma własną wizualizację grafu w SVG; działa offline.

## Podgląd rozdziałów — ramki

Definicje, twierdzenia, lematy, wnioski, przykłady, uwagi i zadania mają kolorowe, zaokrąglone ramki w **Podglądzie rozdziału**, nie w surowym źródle LaTeX. Szybka kontrola: otwórz AA-01, znajdź „Definicja — Grupa”. Jeżeli po aktualizacji nie ma ramek, sprawdź, czy uruchamiasz aktualny checkout gałęzi `biblioteka-matematyczna-iteracja-6` (a nie dawny ZIP), zamknij wszystkie karty Atlasu i uruchom `application/start.cmd` ponownie. Skrypt startowy może otworzyć już działający serwer zamiast uruchomić nowy. W przeglądarce użyj Ctrl+F5. Nie nadpisuj lokalnych zmian przy aktualizacji repozytorium.

## Uruchamianie (Windows 11)

W repozytorium otwórz katalog `application` i kliknij dwukrotnie **`start.cmd`**.
Skrypt przygotuje lokalne środowisko `.venv`, zainstaluje zależności przez `uv`
(albo `pip` w `.venv`, gdy `uv` nie jest dostępne), odświeży indeks i otworzy
przeglądarkę. Wymagany jest `uv` lub Python 3.10+. Pierwsza instalacja wymaga
internetu. Zamknięcie ostatniej karty aplikacji kończy pracę serwera po około
5 sekundach. Odświeżenie strony i zamknięcie jednej z kilku kart nie kończą
pracy. Można też zatrzymać aplikację przez **Ctrl+C** w oknie serwera.
Ponowne uruchomienie otworzy działającą instancję bez przebudowy indeksu.
Możesz również uruchomić z katalogu repozytorium:

```powershell
.\application\start.ps1
# Bez automatycznego otwierania przeglądarki:
.\application\start.ps1 -NoBrowser
```

Aplikacja jest dostępna pod **http://127.0.0.1:8765/**. `start.cmd` działa również,
gdy polityka PowerShell blokuje bezpośrednie uruchamianie plików `.ps1`.
W przenośnym archiwum uruchom `start.cmd` z katalogu aplikacji.
Na Linux/macOS użyj `./start.sh`.

Czytnik domyślnie otwiera podgląd tekstu i wzorów. Przycisk **Pokaż źródło LaTeX**
udostępnia kod oraz narzędzia wyboru wierszy. Przyciski **A− / A+** zmieniają
wielkość tekstu od 80% do 180%; kliknięcie wartości procentowej przywraca 100%.
Wielkość tekstu i motyw są zapamiętywane w przeglądarce. Przełącznik jasnego
i ciemnego motywu jest stale widoczny w górnym pasku, także na telefonie.

**Ukryj Explorer / Pokaż Explorer** zwalnia miejsce na tekst i zapamiętuje wybór
na komputerze. **Pełny ekran** ukrywa nawigację i wypełnia ekran czytnikiem;
pozostawia regulację tekstu, motyw i przycisk wyjścia. Powrót: **Esc** albo
**Zakończ pełny ekran**. Gdy przeglądarka odmawia pełnego ekranu, ten sam
układ czytania wypełnia okno aplikacji.

Podgląd składa wzory przez KaTeX, a rysunki `tikzpicture`, `tikzcd` i `picture`
przez lokalne `pdflatex` oraz `pdftocairo` (MiKTeX/TeX Live i Poppler).
Pierwsze wyświetlenie rysunku wymaga kompilacji; kolejne korzystają z obrazów
w `data/.figure_cache/`. Rysunki zachowują oryginalne kolory na białym tle
również w ciemnym motywie. Błędy kompilacji są widoczne przy danym rysunku.

> Uwaga: pliki w Bibliotece ChatGPT nie są bezpośrednio folderem lokalnym. Do uruchomienia aplikacji trzeba pobrać i rozpakować archiwum. Zawiera ono komplet 233 rozdziałów i gotową bazę SQLite, więc nie trzeba pobierać ich osobno.

## Co jest zaimplementowane

1. **Explorer:** zwijane dziedziny; 233 moduły; rozwijanie rozdziału do sekcji, podsekcji, twierdzeń, definicji, dowodów, przykładów itd.; wybór granularności.
2. **Wyszukiwarka:** tytuły i fragmenty obiektów oraz pełna treść modułów indeksowana przez SQLite FTS5; wyniki otwierają dokładne obiekty lub rozdziały.
3. **Czytnik:** wierny tekst źródłowy TeX; wariant uproszczony nie jest pełnym rendererem TeX-a; `\\ref`, `\\eqref`, `\\cref`, `\\autoref` itd. są klikalne i pokazują dymek z rzeczywistym cytowanym fragmentem.
4. **Graf dwudzielny:** wybór dwóch dziedzin i poziomu (moduły, sekcje, obiekty); krawędzie reprezentują *wyłącznie jawne odsyłacze LaTeX*. Kliknięcie węzła otwiera odpowiedni moduł albo obiekt. Istnieje też wyszukiwanie najkrótszej ścieżki odsyłaczy między modułami (dla ścieżki ignorowany jest kierunek).
5. **Kreator własnego skryptu:** można zbierać całe rozdziały, sekcje i obiekty albo wybrać dokładne wiersze tekstu LaTeX. Wybrane pozycje można przestawiać strzałkami, eksportować manifest JSON oraz kontrolować odsyłacze. Wycinanie obejmuje całe wskazane wiersze.
6. **Generator projektu:** tworzy ZIP z `main.tex`, fragmentami we wskazanej kolejności, dokumentami referencyjnymi `aux/*.tex`, skryptami kompilacji i manifestem. W `ordered_items` zapisane są źródła, zakresy i pliki wynikowe. API nie wykonuje TeX-a.
7. **API tylko do odczytu:** żadna akcja z poziomu interfejsu nie nadpisuje plików `.tex` ani bazy danych.

### Najważniejsze punkty API

| Endpoint | Znaczenie |
|---|---|
| `GET /api/stats` | Statystyki indeksu |
| `GET /api/domains` | Dziedziny z liczbą rozdziałów |
| `GET /api/modules` | Lista i filtrowanie rozdziałów |
| `GET /api/modules/{id}/outline` | Struktura obiektów wewnątrz rozdziału |
| `GET /api/modules/{id}` | Tekst rozdziału |
| `GET /api/entities/{id}` | Źródło wybranego obiektu |
| `GET /api/labels/{label}` | Cytowany fragment, z lokalizacją |
| `GET /api/search?q=...` | Wyszukiwanie pełnotekstowe |
| `GET /api/graph?left=...&right=...&granularity=...` | Graf dwudzielny, `module`, `section`, `entity` |
| `GET /api/graph/path?source=...&target=...` | Ścieżka przez jawne odsyłacze |
| `POST /api/selection/plan` | Audyt zestawu i plan `xr-hyper` |
| `GET /api/docs` | Automatyczna dokumentacja OpenAPI |

Przykłady:

```text
http://127.0.0.1:8765/api/stats
http://127.0.0.1:8765/api/modules/ALG-09/outline
http://127.0.0.1:8765/api/labels/ch:pierscienie
http://127.0.0.1:8765/api/graph/path?source=ALG-09&target=AT-10
```

## Tworzenie własnego skryptu z dokładnych fragmentów

1. Wybierz rozdział albo obiekt z Explorera. W Czytniku zaznacz tekst LaTeX i kliknij **+ Zaznaczenie**. Dodawane są wszystkie pełne wiersze obejmujące zaznaczenie. Alternatywnie wpisz numery **Od/Do** i kliknij **+ Wiersze**.
2. W **Kreatorze zestawu** połącz wycinki z różnych rozdziałów, zmieniaj ich kolejność strzałkami ↑/↓ i sprawdź odsyłacze.
3. Nadaj tytuł, wybierz domykanie zależności, pobierz ZIP albo utwórz szkic i zapisz go jawnie. Źródłowe .tex oraz SQLite nie są modyfikowane.

Nowy format dla `POST /api/generate`, `POST /api/generate/manifest` i `POST /api/drafts`:

```json
{
  "title": "Mój skrypt",
  "closure_depth": 0,
  "items": [
    {"kind": "entity", "id": "ALG-09/proof/0004"},
    {"kind": "lines", "module": "AA-07", "start_line": 10, "end_line": 20},
    {"kind": "module", "id": "ALG-09"}
  ]
}
```

Pole `items` określa kolejność skryptu, również gdy kolejne fragmenty pochodzą z tego samego rozdziału. Wybór całego rozdziału ma pierwszeństwo przed wycinkami. Duplikaty i fragmenty zawarte w większych są pomijane, a częściowe przecięcia odrzucane. Nie łącz `items` z polami `modules` i `entities` w jednym żądaniu; stary format nadal działa.

Preambuły generatora obejmują wszystkie indeksowane dziedziny, m.in. LA, LST, FA, DG, ME i PDE, oraz rozdziały z przyrostkiem literowym (np. FA-15A). Pominięte pole `items` zachowuje zgodność ze starszym API; jawnie puste `items` nie uruchamia trybu `modules`.

**Ograniczenie TeX:** arbitralny wycinek może pomijać założenia, definicje lub początek i koniec środowiska. Generator zachowuje źródło i analizuje odsyłacze, ale nie gwarantuje matematycznej samowystarczalności ani kompilowalności. Nie rozszerza automatycznie wycinków o kontekst.

## Ponowna indeksacja po zmianach w Bibliotece

Pliki `.tex` są źródłem prawdy. Baza `data/biblioteka.db` jest tylko indeksem. Zmień teksty w `rozdzialy/`, potem uruchom:

```powershell
python backend/latex_parser.py index --source rozdzialy --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json --report data/indeksowanie_raport.json
python backend/latex_parser.py audit
python -m unittest discover -s tests -v
```

Nie uruchamiaj reindeksacji podczas czytania przez serwer: zatrzymaj serwer, przebuduj bazę i uruchom go ponownie. Narzędzie indeksujące podmienia plik bazy atomowo.

## Spójność odsyłaczy i ograniczenia

- W migawce jest **233 moduły**, **8686 obiektów**, **2363 etykiety**, **1515 odsyłaczy** i **299 skierowanych połączeń między modułami**; wszystkie jawne cele są rozwiązane globalnie.
- Dymki działają na podstawie `labels` i `entities`, także dla obiektów spoza aktualnie wybranej listy. Zmienione nazwy etykiet zapisane w rejestrze historycznym **nie są jeszcze automatycznie przekierowywane**.
- **Graf nie wnioskuje jeszcze o związku matematycznym z samego podobieństwa tekstów.** Jeśli dwie dziedziny nie mają jawnych odsyłaczy, wizualizacja może być pusta, mimo że istnieją między nimi ważne związki. Przykładowa dziedzina „analiza zespolona” nie jest jeszcze osobnym modułem w tej migawce.
- Przy wyborze pojedynczego twierdzenia lub sekcji analiza `selection/plan` bierze pod uwagę *cały moduł* zawierający ten fragment. Rezultat jest oznaczony `preliminary` i może zawyżać liczbę brakujących zależności.
- **Nie generujemy jeszcze kompletnego nowego skryptu, PDF ani zewnętrznych plików `.aux`.** `xr-hyper` jest planowany, a nie wykonywany automatycznie.
- Uproszczony podgląd nie interpretuje zdefiniowanych przez autora makr ani całych środowisk matematycznych, więc nie zastępuje LaTeX-a. Podgląd źródłowy zachowuje treść oryginału.
- Parser jest statyczny: brak ekspansji niestandardowych makr, teoretycznych zależności niejawnych i wywołań kodu z `.tex`.
- Serwer domyślnie jest dostępny wyłącznie lokalnie na `127.0.0.1`. Nie udostępniaj go publicznie bez dodatkowego uwierzytelniania, ograniczania ruchu i audytu bezpieczeństwa.

## Testy i kontrola techniczna

```powershell
python -m unittest discover -s tests -v
node --check frontend/app.js  # jeśli masz Node.js
```

**36 testów Python zakończonych pomyślnie** (14 parsera + 22 API). Sprawdzono odpowiedzi HTTP, strukturę danych, pobieranie etykiet, graf bipartite dla trzech poziomów, ścieżki i plany zestawów. Frontend ma poprawną składnię JavaScript (`node --check`); w środowisku tworzenia przeglądarka headless blokowała wszystkie żądania sieciowe, więc **nie przeprowadzono pełnego testu kliknięć w przeglądarce**. Zalecany jest manualny smoke test po uruchomieniu na lokalnym komputerze.

## Struktura

```text
backend/
    latex_parser.py       # indeksacja, walidacja, rejestry
    api.py                # odczytowe REST API FastAPI + NetworkX
frontend/
    index.html
    app.js
    styles.css
rozdzialy/                 # 233 źródła TEX
config/ALIASY_PO_SCALENIACH.json
data/biblioteka.db         # odtwarzalny indeks
    indeksowanie_raport.json
    api_audyt.json
    testy_api_raport.txt
tests/
    test_latex_parser.py
    test_api.py
start.ps1
start.sh
build_index.ps1
requirements.txt
```

**Plan kolejnej iteracji:** pełny parser zależności dla fragmentów i stabilne ID nieoznaczonych obiektów, generator `main.tex` z wybieranych bloków, automatyczne buildy `.aux` oraz `xr-hyper`, semantyczne sugestie połączeń (odróżnione od potwierdzonych), sprawdzanie integralności przy scalaniu.

Szczegóły pierwszej wersji parsera zachowano w `docs/PARSER_01.md`.

## Wersja 0.3 — generator rzeczywistych projektów LaTeX (19.11.2026)

W zakładce **Kreator zestawu** można teraz generować archiwum ZIP zawierające:

- `main.tex` składający wybrane moduły i fragmenty,
- kopie fragmentów `rozdzialy/<ID>.tex`,
- dokumenty referencyjne `aux/<ID>.tex` dla pominiętych celów `\ref` / `\eqref` / `\cref`,
- `build.ps1` / `build.sh`, generujące `.aux` przed dwukrotną kompilacją `main.tex`,
- `manifest.json` z listą obiektów, sumami SHA-256 oryginałów i spisem odsyłaczy,
- `README.md` z instrukcją budowania.

Wybór pojedynczego obiektu używa dokładnych offsetów parsera SQLite. Nadmiarowe fragmenty zawarte w wybranym obiekcie nadrzędnym są odfiltrowywane. Niezdefiniowane odsyłacze powodują błąd 422. Odsyłacze do pominiętych fragmentów *tego samego* rozdziału używają oddzielnych prefiksów `ext-<MODUŁ>-` tak, żeby nie kolidowały z aktywnymi `\label`.

Przykład działania lokalnego bez serwera (w katalogu aplikacji):

```powershell
python -m backend.generator --modules AA-01 --title "Przykładowy skrypt" --output przyklad.zip
python -m backend.generator --entities ALG-09/proof/0004 --title "Wybrany dowód" --output dowod.zip
```

API: `POST /api/generate/manifest` zwraca dokładny plan fragmentów, a `POST /api/generate` — gotowe archiwum ZIP. Przykładowy JSON:

```json
{"title":"Próbny skrypt","modules":["ALG-09"],"entities":[],"closure_depth":0}
```

**Ograniczenia:** serwer nie uruchamia `pdflatex` ani nie modyfikuje kanonicznych źródeł. Nie wszystkie mieszane zestawy różnych dziedzin skompilują się bez ujednolicenia preambuł. Nawet w przypadku poprawnych referencji wybrana sekcja może wymagać definicji niecytowanych jawnie przez `\ref`. Wersja 0.3 generuje poprawny projekt i skrypty kompilacyjne; pełną samowystarczalność matematyczną skryptów ocenią późniejsze audyty.


## Version 0.4 — ephemeral drafts and saved projects

This is a **local browser application**, not an installed desktop application.
The `start.cmd`, `start.ps1` and `start.sh` launchers now run `backend.desktop`:
the server exits gracefully five seconds after the last live page disconnects.
The delay permits page reloads; a second connected tab keeps the server alive.
WebSocket disconnect detection also covers closure without an unload event.
After a browser crash or lost connection, detection may take up to roughly
30 seconds, followed by the five-second grace period. A server launched
directly with `python -m uvicorn backend.api:app` keeps its developer behavior
and does not exit with the browser. Before the first page connects, the desktop
launcher waits for the user to open the application.
Closing the browser tab using **X** sends a best-effort `sendBeacon` to delete
that tab's unsaved generated draft. Browsers do **not guarantee** close events
(e.g. power loss or forced termination), so the backend performs crash recovery:
24-hour stale draft cleanup on startup and every 15 minutes, and cleanup of all
remaining drafts when the API server shuts down cleanly.

- **Create draft**: saves a temporary generated ZIP in `data/.temporary_projects/<session_id>/`.
- **Save permanently**: copies the draft ZIP to `data/saved_projects/<id>.zip`.
- **Download ZIP**: downloads directly to the browser's Downloads folder; the
  application cannot delete or manage files downloaded outside its own directory.
- **Saved projects**: available via the UI and `GET /api/projects`. They are
  **never deleted** by draft cleanup. The SQLite index and canonical TeX files
  remain immutable.
- `MATLIB_DRAFTS_ROOT` and `MATLIB_SAVED_ROOT` can point to separate storage
  locations. Keep saved storage outside app deployments when upgrading.

Endpoints: `POST /api/drafts`, `POST /api/drafts/{id}/save`,
`POST /api/drafts/{id}/close`, `POST /api/drafts/{id}/heartbeat`,
`GET /api/drafts/{id}/download`, `GET /api/projects`,
`GET /api/projects/{id}/download`.

**Important:** no full browser automation suite was run in this environment;
Python API tests and JavaScript syntax checks passed.


## Version 0.5 — measure theory and jets in Explorer

Added 31 audited measure-theory modules (`ME-01` through `ME-31`).
Module `ME-31` is the combined chapter on geometric and measure-theoretic jets.
The SQLite index was rebuilt from 264 canonical .tex source modules, yielding
3,071 labels, 2,121 references, **zero missing references, zero duplicate
labels and zero parse warnings**. The 264 TeX files and the SQLite index are
included in the complete v0.5 distribution. The master measure theory book
and its supplements are maintained in the GitHub repository at
`books/pl/measure_theory.tex` and `chapters/pl/measure_theory/` respectively.

A monolithic measure-theory+jets .tex and matching 256-page PDF are also
available separately in the ChatGPT Library.

### Renderowanie wzorów

`start.ps1` i `start.sh` instalują lokalnie przypiętą wersję KaTeX. Jednorazowe pobranie wymaga dostępu do registry.npmjs.org; kolejne uruchomienia i renderowanie korzystają z lokalnych plików `frontend/vendor/katex`. Przy ręcznym uruchomieniu uvicorn najpierw wykonaj `python scripts/install_math_renderer.py`. Podgląd uproszczony i dymek odsyłacza składają standardowe wzory, bez wykonywania preambuły; nieobsługiwane makra pozostają w źródle. Widok źródłowy zachowuje oryginalny LaTeX.
