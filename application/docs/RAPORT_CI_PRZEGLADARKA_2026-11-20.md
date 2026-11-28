# Biblioteka matematyczna — iteracja przeglądarkowa CI (20.11.2026)

Repozytorium: `dariusz-piekarz/mathematical_scipts`.
Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Rzeczywiste wdrożenie

- Dodano `application/tests/browser_ci_e2e.py` — automatyczny test Playwright z Chromium na lokalnym serwerze FastAPI, bazujący na kanonicznym indeksie z `chapters/pl`.
- Rozszerzono `.github/workflows/mathematical-library-app.yml` o kompilację składniową trzech skryptów testów przeglądarkowych, instalację Chromium i faktyczne wykonanie testu.
- Test weryfikuje zgodność liczby rozdziałów w interfejsie z `/api/stats`, otwarcie rozdziału, treść czytnika i dostępność obu dziedzin grafu oraz brak błędów JavaScript.
- Poprawiono pierwszy regresyjny błąd selektora/licznika wykryty w CI; poprzedni przebieg z tym błędem pozostaje historycznie czerwony.

## Potwierdzony wynik GitHub Actions

Run: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44706291102
Commit: `ec22ab95cf1af80025e995b81c032efbfdd56270`
Status: `completed`, conclusion: `success`.

- Budowanie indeksu z kanonicznych rozdziałów: PASS.
- Regresje Pythona: `Ran 85 tests`, `OK (skipped=1)`.
- Sprawdzenie składni skryptów przeglądarkowych: PASS.
- Instalacja Chromium: PASS.
- Rzeczywisty test przeglądarkowy: PASS.
- Indeks: 355 rozdziałów, UI: „355 rozdziałów”.
- Czytnik otworzył rozdział „Cel, założenia i plan dowodu”.
- Graf: 16 dostępnych dziedzin; błędy JavaScript: `[]`.

## Ograniczenia i kolejny krok

To nie jest całkowity audyt matematyczny biblioteki. Test Playwright sprawdza tylko podstawową nawigację Explorer/czytnik/graf. Nie sprawdza jeszcze bezpośrednio dymków cytowanych fragmentów, wszystkich funkcji generatora w UI ani cyklu życia draftów. W teście unittest jedna pozycja nadal została pominięta — nie należy utożsamiać tego z błędem ani z jej zaliczeniem. Wcześniejsze czerwone uruchomienia GitHub Actions pozostają widoczne w historii, lecz bieżący commit ma zielony przebieg.

Kolejny etap: rozszerzenie testów przeglądarkowych o odsyłacze/cytowane fragmenty oraz przepływ draft/save/close; równolegle osobny matematyczny audyt brakujących i niejednoznacznych etykiet. Nie modyfikowano kanonicznych rozdziałów ani gałęzi `main`.