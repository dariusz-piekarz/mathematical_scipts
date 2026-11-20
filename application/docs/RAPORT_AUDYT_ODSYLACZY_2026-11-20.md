# Biblioteka matematyczna — audyt odsyłaczy i mapy pochodzenia

Data: 20 listopada 2026. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Wykonane prace

- Dodano `application/scripts/audit_reference_provenance.py`, który **tylko czyta** odtworzony indeks SQLite i tworzy kompletne zestawienia JSON i Markdown. Pokazuje źródło odsyłacza (identyfikator, ścieżkę, wiersz, SHA-256), nazwę etykiety, status i wszystkich znanych kandydatów z ich ścieżkami oraz pochodzeniem. Dla brakujących celów nie dopisuje pozornych właścicieli.
- Dodano `application/tests/test_audit_reference_provenance.py` (2 nowe testy, w tym kontrola niezmienności bazy oraz braku arbitralnej rekomendacji właściciela).
- Rozszerzono `.github/workflows/mathematical-library-app.yml`: pełny audyt po każdym indeksowaniu oraz archiwizacja obu raportów jako GitHub Actions artifact `reference-provenance-audit`.
- **Nie** zmieniano kanonicznych `.tex`, nazw etykiet, tekstu dowodów, gałęzi `main` ani innych równoległych skryptów.

## Wynik na aktualnym indeksie GitHuba

| Metryka | Liczba |
|---|---:|
| Dokumenty w indeksie | 355 |
| Nazwy etykiet w indeksie | 5754 |
| Odsyłacze rozwiązane | 4228 |
| Niejednoznaczne wystąpienia odsyłaczy | 166 |
| Brakujące wystąpienia odsyłaczy | 91 |
| Razem nierozwiązane wystąpienia | 257 |
| Różne brakujące nazwy | 49 |
| Różne niejednoznacznie cytowane nazwy | 61 |
| Nazwy o wielu właścicielach (w tym niecytowane niejednoznacznie) | 305 |

Liczby dotyczą bazy zbudowanej przez GitHub Actions z aktualnego `chapters/pl/`; mogą różnić się od migawki 352 rozdziałów przechowywanej wcześniej w Bibliotece. Wyniki nie oznaczają, że wszystkie 305 konfliktów prowadzi do błędnego odsyłacza: część odsyłaczy rozwiązuje się lokalnie.

**Przykłady wymagające audytu matematycznego:**

- Brakujący cel `tw:ga10-weak` — cytowanie w `ALG-10`, wiersz 240, `pl/algebraic_geometry/10-geometria-algebraiczna-a-topologia-od-cykli-do-twierdzen-lefsc.tex`. Brak właściciela tej etykiety w indeksie, nie wolno automatycznie zgadywać odpowiednika.
- Niejednoznaczne `thm:poincare-hopf-16` — cytowanie w `DG-02`, wiersz 238; kandydaci `DG-17` (wiersz 2236) oraz `TOP-11` (wiersz 2186). Porównanie założeń i dowodów jest wymagane przed jakąkolwiek korektą.

## Testy i weryfikacja

GitHub Actions [#44712479054](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44712479054) dla commita `62fcdd117aa2c10ce2f46dcaf2056561f1b9ef54`: **success**; indeksowanie, audyt z artefaktem, zestaw testów Python oraz dwa testy Chromium zaliczone. Dodatkowe dwa testy audytu uruchomiono lokalnie, oba zaliczone.

Pełne wyniki (niezredukowane do przykładów):

- `data/reference_provenance_audit_355.json` w Bibliotece ChatGPT — wszystkie wystąpienia wraz z kandydatami, pochodzeniem, liniami i SHA-256.
- `docs/reference_provenance_audit_355.md` w Bibliotece ChatGPT — kompletna tabela przypadków wymagających audytu oraz 305 konfliktowych nazw.
- [Archiwum pełnych wyników w GitHub Actions](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44712479054/artifacts/14618175691).

## Ograniczenia i dalsze prace

Indeks jest analizą leksykalną LaTeX, nie dowodem semantycznej równoważności twierdzeń. Przed zmianą nazwy odsyłacza należy porównać fragment cytujący i wszystkie kandydujące twierdzenia zgodnie z `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, zachowując różne dowody. W następnej iteracji można zacząć od 10–20 przypadków z największą liczbą nierozwiązanych cytowań i przygotować ręczne, uzasadnione propozycje. Oddzielne otwarte zadania: kompilacje międzydziedzinowe `xr-hyper` i rzeczywisty X-close.