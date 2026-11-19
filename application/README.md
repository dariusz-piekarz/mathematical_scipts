# Atlas matematyczny — aplikacja do wspólnej Biblioteki

**Current application version: 0.4 (drafts, save, X-close cleanup); historical 0.3 notes below.**

**Wersja 0.3 — API + Explorer + czytnik + graf zależności + generator skryptów z xr-hyper.**  
**Źródła:** 233 wspólne moduły `.tex` w `rozdzialy/` (migawka z 19.11.2026).  
**Architektura:** Python / FastAPI / SQLite, HTML / CSS / JavaScript (bez frameworka frontendowego), NetworkX do wyznaczania ścieżek. Frontend ma własną wizualizację grafu w SVG; działa offline.

## Uruchamianie (Windows 11)

Rozpakuj cały plik `BIBLIOTEKA_MATEMATYCZNA_APP_03.zip` na dysk. Wejdź do jego katalogu w PowerShellu:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
```

Następnie otwórz **http://127.0.0.1:8765/** w przeglądarce. Możesz też uruchomić `./start.ps1`. Na Linux/macOS analogicznie `./start.sh` lub powyższe polecenie Python.

> Uwaga: pliki w Bibliotece ChatGPT nie są bezpośrednio folderem lokalnym. Do uruchomienia aplikacji trzeba pobrać i rozpakować archiwum. Zawiera ono komplet 233 rozdziałów i gotową bazę SQLite, więc nie trzeba pobierać ich osobno.

## Co jest zaimplementowane

1. **Explorer:** zwijane dziedziny; 233 moduły; rozwijanie rozdziału do sekcji, podsekcji, twierdzeń, definicji, dowodów, przykładów itd.; wybór granularności.
2. **Wyszukiwarka:** tytuły i fragmenty obiektów oraz pełna treść modułów indeksowana przez SQLite FTS5; wyniki otwierają dokładne obiekty lub rozdziały.
3. **Czytnik:** wierny tekst źródłowy TeX; wariant uproszczony nie jest pełnym rendererem TeX-a; `\\ref`, `\\eqref`, `\\cref`, `\\autoref` itd. są klikalne i pokazują dymek z rzeczywistym cytowanym fragmentem.
4. **Graf dwudzielny:** wybór dwóch dziedzin i poziomu (moduły, sekcje, obiekty); krawędzie reprezentują *wyłącznie jawne odsyłacze LaTeX*. Kliknięcie węzła otwiera odpowiedni moduł albo obiekt. Istnieje też wyszukiwanie najkrótszej ścieżki odsyłaczy między modułami (dla ścieżki ignorowany jest kierunek).
5. **Kreator zestawu:** można zbierać całe rozdziały lub obiekty, eksportować manifest JSON, sprawdzać odsyłacze wewnętrzne i brakujące moduły jako plan przyszłego `xr-hyper`.
6. **Generator projektu:** tworzy ZIP z `main.tex`, fragmentami, dokumentami referencyjnymi `aux/*.tex`, skryptami kompilacji i manifestem. API nie wykonuje TeX-a.
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
python -m backend.generator --modules BT-00 --title "Przykładowy skrypt" --output przyklad.zip
python -m backend.generator --entities ALG-09/proof/0004 --title "Wybrany dowód" --output dowod.zip
```

API: `POST /api/generate/manifest` zwraca dokładny plan fragmentów, a `POST /api/generate` — gotowe archiwum ZIP. Przykładowy JSON:

```json
{"title":"Próbny skrypt","modules":["ALG-09"],"entities":[],"closure_depth":0}
```

**Ograniczenia:** serwer nie uruchamia `pdflatex` ani nie modyfikuje kanonicznych źródeł. Nie wszystkie mieszane zestawy różnych dziedzin skompilują się bez ujednolicenia preambuł. Nawet w przypadku poprawnych referencji wybrana sekcja może wymagać definicji niecytowanych jawnie przez `\ref`. Wersja 0.3 generuje poprawny projekt i skrypty kompilacyjne; pełną samowystarczalność matematyczną skryptów ocenią późniejsze audyty.


## Version 0.4 — ephemeral drafts and saved projects

This is a **local browser application**, not an installed desktop application.
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
