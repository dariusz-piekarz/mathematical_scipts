# ALG-00 — kontrola regresyjna 06, 23.11.2026

**Źródło:** `chapters/pl/algebraic_geometry/00-teoria-pierscieni-od-arytmetyki-do-geometrii-rownan.tex`, blob `daedcd38d31e42c738df7f7d12a66d3994ebda8a` (1727 wierszy). **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Faktycznie sprawdzone

Odczytano aktualny HEAD, manifest `catalog/books.json`, README, standard `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, rejestr `audits/algebraic_geometry/STATUS.md`, raport globalny IV, poprzedni raport regresyjny 05, źródło książki i cały rozdział ALG-00 przez GitHub. Rejestr potwierdza ALG-00–ALG-10 jako wcześniej STABILNE/ZAMKNIĘTE.

Kontrola konstruktywna i niezależna sceptyczna objęły aksjomaty pierścienia, pierścień zerowy, ilorazy, jednostki, dzielniki zera, nilpotenty, charakterystykę, jądra homomorfizmów, generowanie i odpowiedniość ideałów, CRT, ideały pierwsze i maksymalne, pierwiastniki, dzielenie wielomianów, Bézouta, ideał punktu, parabolę, dwie osie oraz lemat Gaussa i UFD. Osobno sprawdzono znaki w CRT, warunki dziedziny i ciała przy skracaniu, rozróżnienie wielomianów formalnych i funkcji nad ciałami skończonymi, poprawność relacji w diagramie ideałów Z/12Z i algebraiczną treść rysunków TikZ. Nie wykryto nowej uzasadnionej usterki matematycznej.

**Reuse:** ALG-00 → AA-09 (CRT, ideały), AA-10 (Bézout, podzielność), AA-11 (Gauss, UFD), AA-12 (pierwiastniki). Sprawdzono zgodność kluczowych hipotez; nie zmieniano źródeł AA i nie przepisywano poprawnych dowodów.

**Testy wykonane:** Python/SymPy, **179636/179636 PASS**. Zakres: odwracalność modulo n dla 2≤n≤150, brak dzielników zera w F₂, F₃, F₅, F₇, F₁₁, 625 podstawień do paraboli, skracanie przez jednostki modulo n dla 2≤n<80. Testy skończone nie są formalnym dowodem.

**CI:** odczytano GitHub Actions: 45140949298 queued, 45140774315 in_progress, 45140774379 success (grafy), 45140774507 success (terminologia), 45140636725 failure (teoria miary). Żaden nie stanowi nowego PASS ALG-00. Historyczne audyty globalne III–IV dokumentują dwukrotny odbiór 184-stronicowego PDF.

**Blokada techniczna:** lokalne `git ls-remote` zakończyło się `Could not resolve host: github.com`. Pomimo dostępnego `pdflatex` brak pełnego lokalnego drzewa do nowej dwukrotnej kompilacji, analizy logu i wizualnego odbioru PDF. **Ten przebieg nie jest nowym pełnym audytem stabilizacyjnym**, a licznik czystych pełnych kontroli pozostaje bez zmian. Nie znaleziono uzasadnionej poprawki .tex.

| Zakres | Status |
|---|---|
| ALG-00 | Wcześniej stabilny/zamknięty; regresja 06 bez nowych usterek; nowy odbiór techniczny nieukończony |
| ALG-01–ALG-10 | Wcześniej stabilne/zamknięte; bez zmian |
| Globalny III–IV | Historycznie zakończone; brak nowego PASS |

**Następny krok:** po odzyskaniu pełnego drzewa wykonać nowy dwukrotny skład i obejrzeć strony PDF ALG-00; nie wprowadzać zmian pozornych.