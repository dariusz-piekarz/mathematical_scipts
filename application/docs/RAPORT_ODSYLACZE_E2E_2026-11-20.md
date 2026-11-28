# Biblioteka matematyczna — podglądy niejednoznaczne, brakujące i wyścigi (20.11.2026)

## Zakres

Zmieniono jedynie `application/frontend/app.js` i `application/tests/browser_ci_e2e.py` w gałęzi `biblioteka-matematyczna-iteracja-6`. Nie zmieniono źródeł `chapters/pl`, żadnego wariantu dowodu ani gałęzi `main`.

- Podgląd brakującego celu prezentuje diagnostykę „Nie znaleziono cytowanej etykiety” zamiast milczącego błędu; przycisk otwierania nieaktywnego celu jest zablokowany.
- Podgląd niejednoznacznej etykiety wymaga jawnego wyboru właściciela. Nie wybiera automatycznie żadnego modułu.
- Zastosowano identyfikator żądania (`tooltipKey`) oraz bieżącą kotwicę (`tooltipAnchor`). Opóźniona odpowiedź HTTP lub wcześniejszy `mouseleave` nie powinny nadpisywać bądź zamykać nowszego podglądu.
- Test Chromium korzysta z rzeczywistych etykiet z przebudowanej bazy SQLite, sprawdza zarówno dodatnią ścieżkę nawigacji, jak i oba przypadki negatywne oraz sztucznie opóźnioną odpowiedź.

## Wynik zweryfikowany na GitHubie

GitHub Actions [#44711138252](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44711138252), commit `e6ac161577e69f16b48e53b72eece38d0d78a092`: **success**. Zbudowano indeks kanonicznych rozdziałów. Testy Python: **85 uruchomionych, 84 zaliczone, 1 pominięty**, bez błędów. Oba testy Chromium zaliczone (Explorer/czytnik/graf/odsyłacze oraz draft/save/page-leave).

Użyte rzeczywiste etykiety: jednoznaczna `tw:korzenie` w `ALG-00`; niejednoznaczna `ch:algebra-homologiczna` z dwoma kandydatami `DG-06` i `TOP-03`; brakująca `I-ch:clt`. Potwierdzono poprawną obsługę odpowiedzi opóźnionej i brak błędów JavaScript. Indeks obejmował 355 rozdziałów i 16 dziedzin.

## Ograniczenia i następne zadania

Zielone CI nie usuwa rzeczywistych konfliktów etykiet z rozdziałów ani nie rozstrzyga matematycznej poprawności odsyłaczy. Wciąż wymagają audytu brakujące, niejednoznaczne i zduplikowane etykiety, międzydziedzinowa kompilacja `xr-hyper` oraz przypadek bezpośredniego zamknięcia karty X (test `pagehide` nie jest gwarancją dostarczenia beacon). Kolejna iteracja: raport źródeł niejednoznaczności i klasyfikacja brakujących celów z mapą pochodzenia, bez automatycznego przepisywania rozdziałów.