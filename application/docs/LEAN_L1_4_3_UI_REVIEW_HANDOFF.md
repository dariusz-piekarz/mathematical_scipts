# L1.4.3 — odbiór niezależny interfejsu raportu rozdziałowego Lean

Kandydat: `5f3a830c1ee5ae0326375cd3387318891b6800ba` (nie bieżący HEAD). Gałąź: `biblioteka-matematyczna-iteracja-6`.
Status: **stabilizing**, niezależny odbiór nieudzielony, `certificate=false`.
Ten dokument jest pakietem dla recenzenta, a nie jego recenzją ani zatwierdzeniem.

## Zakres

- [Implementacja a0732483](https://github.com/dariusz-piekarz/mathematical_scipts/commit/a073248327a0743c5da137f06fba8fe56707db4f): `application/frontend/app.js`, `application/frontend/index.html`, `application/tests/test_lean_chapter_report_browser.py`.
- [Test integracyjny 5f3a830c](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5f3a830c1ee5ae0326375cd3387318891b6800ba): `application/tests/browser_ci_e2e.py`.
- Istniejący GET /api/lean/chapter-report jest tylko do odczytu; brak zmian runnera, manifestu, źródeł TeX i Lean w implementacji UI.
- Względem obserwowanego HEAD `09a02e74a4253e37e432e5afc47eeccef7b55faf` zmienione pliki: `application/config/atlas_validation_request.json`, `application/docs/ATLAS_DEVELOPMENT_PROGRESS.md`, `audits/functional_analysis/15B-audyt-10.md`, `audits/graph_and_knot_theory/60-rozdzial-01-uzupelnienia-i-kontrola.md`, `chapters/pl/graph_and_knot_theory/01-podstawy-teorii-grafow.tex`. To nie jest potwierdzenie późniejszego HEAD.

## Dowody techniczne

[Workflow 2+1 #45346203621](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621).
[Prepare](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621/job/138281244370) potwierdza dokładny SHA i pochodzenie z gałęzi. Pierwsza pełna runda PASS. Druga: aplikacja, szybkie regresje, Windows PASS, Lean/Mathlib w toku przy sporządzeniu pakietu; trzecia jeszcze niezaliczona.

- [Aplikacja 1](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621/job/138281446939) i [aplikacja 2](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621/job/138284064928): logi 747 testów, 737 passed, 10 sklasyfikowanych skipów, Chromium 511 rozdziałów, 0 błędów JS, nowy test Node ok.
- [Lean 1](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621/job/138281447164): 5 plików, 26 deklaracji, axiom_check=passed, semantic_certificate=false.
- [Raport testów 1](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621/artifacts/14898680928), [raport testów 2](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45346203621/artifacts/14898566886): API GitHub potwierdza istnienie niewygasłych artefaktów. Deklarowane SHA256 ZIP odpowiednio 6c4121bbfa1055a719d42a1b3a1002bff996f7144f7c5a0220148f0a4a1d3fde i fb1f2d5b6565383a716857c24fceee30c63dbb9f4329bb3a974108bfe9e0ee77. W tej iteracji nie pobrano bajtów archiwów, nie twierdzić, że przeliczono ich digest.
- Wymagane jeszcze: kompletna runda 2 i 3, sceptyczny kontrakt oraz końcowy artefakt statusu. Sprawdzić pełne raporty identyfikatorów i klasyfikacje skipów, nie tylko licznik.

## Macierz odbioru

| Przypadek | Oczekiwany wynik | Dowód / zakres |
| --- | --- | --- |
| Bieżący LST-01 | identyfikator, SHA i liczba pozycji zgodne z GET | Chromium |
| Nieistniejący rozdział | jawny błąd, poprzednia lista usunięta | Chromium |
| Ponowienie poprawnego raportu | odzyskanie listy | Chromium |
| Dwie równoległe odpowiedzi | wcześniejsza nie nadpisuje późniejszej | Node |
| Zmiana pola przed błędem | spóźniony błąd ignorowany | Node |
| Pusty raport | jawny brak rejestracji | Node |
| Flaga certificate=true | odrzucenie kontraktu | Node |
| Etykieta z nawiasami HTML | tekst, nie wstawianie HTML | Node stub i przegląd kodu; brak osobnej próby XSS w prawdziwym Chromium |
| Raport nieaktualnego źródła | stale/needs_review, nie status kompilacji | przegląd backendu i istniejące regresje katalogu; ręcznie sprawdzić UI na kontrolowanym indeksie |
| Przypięty SHA, zmiana rozdziału, ponowne wejście | raport opisuje wybrany moduł, nie jest gwarancją aktualności po późniejszej zmianie dysku | ręczna kontrola recenzenta |
| Kontrakt niezgodnych typów liczników/pól | obecnie tylko częściowa walidacja schematu i flag; nie traktować raportu jako zaufanej atestacji | ograniczenie, rozważyć osobną regresję jeśli recenzent uzna za konieczne |

## Odtworzenie

Na osobnym lokalnym checkout dokładnego SHA, bez zmiany gałęzi zdalnej:
1. Uruchomić standardową procedurę indeksowania i pełny CI aplikacji z pliku .github/workflows/mathematical-library-app.yml.
2. W katalogu application, przy zainstalowanym Node, uruchomić `python -m unittest tests.test_lean_chapter_report_browser -v`. Nie zaliczyć skipu Node jako PASS.
3. Uruchomić rzeczywisty Chromium zgodnie z workflow (skrypt tests/browser_ci_e2e.py), dodatkowo ręcznie sprawdzić czytelność na wąskim oknie i klawiaturą.
4. Porównać pełne odpowiedzi API dla wybranego rozdziału, pustego raportu i błędu, skontrolować że nie powstają wykonania Lean ani wpisy historii.
5. Odczytać trzy pełne rundy 2+1 i końcowy artefakt; przejrzeć niezależnie diff i ograniczenia.

## Decyzja recenzenta (nie wypełniona)

Wymagane uwierzytelnione zatwierdzenie niezależnej osoby z podaniem pełnego SHA, zakresu, odtworzonych testów, nierozwiązanych uwag oraz decyzji approve/request changes. [PR #7](https://github.com/dariusz-piekarz/mathematical_scipts/pull/7) jest szkicem i nie ma recenzji. Nie wystarcza niesygnowany dokument, zielony workflow ani autorski przegląd. Nie oznaczać stable i nie rozpoczynać L1.5 przed bramką lub jawną decyzją użytkownika zmieniającą plan.
