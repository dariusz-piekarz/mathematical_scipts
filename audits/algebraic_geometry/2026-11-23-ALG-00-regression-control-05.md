# Geometria algebraiczna — ALG-00, kontrola regresyjna 05 (23.11.2026)

**Stan wejściowy:** źródło ALG-00, blob `daedcd38d31e42c738df7f7d12a66d3994ebda8a` (1727 wierszy), 11 rozdziałów w manifeście. Rejestr STATUS.md i globalne raporty III–IV wskazują ALG-00–ALG-10 jako STABILNE/ZAMKNIĘTE. Ta kontrola nie otwiera rozdziału i nie powiększa licznika pełnych czystych audytów.

## Faktycznie wykonane czynności

Odczytano aktualne: gałąź i drzewo GitHub, katalog źródeł, całe źródło ALG-00, `books/pl/algebraic_geometry.tex`, `catalog/books.json`, README, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, rejestr STATUS i raport regresyjny 04. W źródle policzono 33 środowiska proof, a także rozdzielono 7 bloków lektury odpowiadających zakresom 1–260, 261–520, 521–830, 831–1060, 1061–1268, 1269–1530, 1531–1727. Odczyt potwierdza niezmieniony SHA względem poprzedniej kontroli.

**Matematyka:** ponownie skontrolowano założenia przy jednostkach modulo n, ciele i dziedzinie, rozróżnienie wielomianu formalnego od funkcji nad F₂, niezerowość nilpotentów w ilorazach, argument z ideałem punktu i jądrem podstawienia, wyprowadzenie izomorfizmu k[x,y]/(y-x²) ≅ k[t], kontrprzykład k[x,y]/(xy), kryterium dla ideału (x,y), lemat Gaussa i indukcję UFD. Krytycznie sprawdzono przypadki zerowe i skończonego ciała; nie znaleziono jednoznacznej nowej poprawki. Dla podstaw CRT, Bézouta, UFD i pierwiastników obowiązuje wcześniejsze mapowanie reuse odpowiednio do AA-09, AA-10, AA-11 i AA-12; tych stabilnych źródeł nie zmieniano. Niniejsza kontrola nie oznacza niezależnego nowego dowodu wszystkich 33 twierdzeń z otoczeniami proof.

**Nowe niezależne testy wykonane lokalnie:** Python + SymPy, 5546/5546 zakończonych pomyślnie asercji: brak dzielników zera w F₂, F₃, F₅, F₇, F₁₁ i F₁₃; równoważność odwracalności klasy i gcd(a,n)=1 dla 2≤n≤100; podzielność f(x,y)-f(x,x²) przez y-x² dla 120 wielomianów testowych o niewielkich stopniach i współczynnikach -1,0,1. To testy skończone, nie dowód ogólny ani Lean. Wcześniejsza próba większej liczby testów przekroczyła timeout i nie jest zaliczana.

**CI:** najnowszy zwrócony workflow run 45113110234 miał status FAILURE na commicie 6b20a565; odczytano log zadania chapter-01. Przyczyną jest brak `lmodern.sty` na runnerze w workflow **teorii miary** (measure_theory_ch01_ci.tex), nie wykryta usterka ALG-00. Cztery kolejne zwrócone przebiegi miały success, ale dotyczyły innych commitów. Nie wolno mówić, że całe CI bieżącej gałęzi jest zielone. [Log nieudanego workflow](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45113110234).

**Skład:** lokalny `pdflatex` istnieje, ale `git ls-remote` kończy się `Could not resolve host: github.com`; w kontenerze brak pełnego drzewa repozytorium. W tym przebiegu nie wykonano dwóch kompilacji, nie pobrano nowego PDF i nie dokonano wizualnego odbioru sześciu rysunków. Poprzednie PDF i CI nie zastępują nowego testu na aktualnym przebiegu. Nie modyfikowano źródła .tex, ponieważ nie wykryto uzasadnionej usterki.

## Status i ograniczenia

| Zakres | Status przed | Status po |
|---|---|---|
| ALG-00 | STABILNY/ZAMKNIĘTY, historyczne audyty 15 i globalne III–IV | bez zmian; nowa częściowa kontrola regresyjna 05 |
| ALG-01–ALG-04 | STABILNE/ZAMKNIĘTE | bez zmian, poza zakresem |
| ALG-05–ALG-07 | STABILNE/ZAMKNIĘTE | bez zmian, poza zakresem |
| ALG-08–ALG-10 | STABILNE/ZAMKNIĘTE | bez zmian, poza zakresem |

**Ocena:** nowy przebieg nie spełnia pełnego kryterium dwukrotnej kompilacji i wizualnego PDF, więc **nie jest kolejnym pełnym audytem stabilizacyjnym**. Nie zmieniono liczby czystych pełnych audytów od ostatniej poprawki; niezależny końcowy audyt globalny IV pozostaje w historii. Kolejny sensowny etap to pełny odbiór techniczny aktualnego źródła lub kontrola nowych zmian, bez sztucznego poprawiania niezmienionego ALG-00. Brak podstaw do tworzenia ALG-11.
