# Algebra liniowa — rozdział 03, audyt 1

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik rozdziału:** `chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex`  
**Temat:** Odwzorowania liniowe, jądro i obraz  
**Status:** pierwszy audyt nowego rozdziału; **nie zamykać** po tej iteracji.

## Powiązanie z poprzednimi rozdziałami

Po zamknięciu rozdziałów 01 i 02 utworzono trzeci rozdział poświęcony teorii odwzorowań liniowych.
Przed rozpoczęciem sprawdzono zawartość istniejących plików: rozdział 01 obejmuje podstawy przestrzeni wektorowych, niezależność, bazy i współrzędne; rozdział 02 — wymiar kardynalny, sumy proste, przestrzenie ilorazowe i dopełnienia.
Rozdział 01 wprost zapowiada pełną teorię odwzorowań liniowych. Nowy rozdział 03 podejmuje ten wątek, bez dublowania wcześniejszych pełnych dowodów. Reprezentację macierzową pozostawiono na osobny etap.

Nowy plik włączono do:
- `books/pl/linear_algebra.tex` przez `\\input{../../chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex}`;
- `catalog/books.json` jako trzeci rozdział książki `linear_algebra`;
- `.github/workflows/linear-algebra-chapter.yml` przez rozszerzenie wymaganej listy i kolejności rozdziałów na 01–03.

## Zawartość i audyt matematyczny

### 1. Definicja odwzorowania liniowego

Sprawdzono równoważność addytywności i jednorodności z zachowywaniem kombinacji \(av+bw\).
W dowodzie wykazano jawnie \(T(0_V)=0_W\), zachowywanie wektorów przeciwnych i dowolnych **skończonych** kombinacji; przypadek sumy pustej pozostaje poprawny.
Przykłady współrzędnych rozpatrzono nad dowolnym ciałem, włącznie z charakterystyką \(2\).

### 2. Odwzorowanie wyznaczone przez wartości na bazie

Zweryfikowano istnienie i jednoznaczność przedłużenia dowolnej zadanej rodziny wartości na bazie Hamela, niezależność definicji od przedstawienia oraz przypadek bazy pustej.
Twierdzenie przy **wskazanej bazie** nie wymaga aksjomatu wyboru.
Zgodność odwzorowań na zbiorze rozpinającym poprawnie implikuje ich równość.

### 3. Jądro i obraz

Sprawdzono kryterium podprzestrzeni dla jądra i obrazu, wzór \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\), własność przeciwobrazu podprzestrzeni oraz równoważność iniektywności i \(\ker T=\{0_V\}\).
Przykłady mnożenia wielomianów przez \(X\) i usuwania wyrazu stałego są poprawne **dla każdej charakterystyki**.

### 4. Twierdzenie o wymiarze jądra i obrazu

Przy założeniu AC wybiera się bazę \(C\) jądra i rozszerza ją do \(C\sqcup D\) bazy \(V\).
Dowód pokazuje, że \(T(D)\) rozpina obraz oraz spełnia warunek niezależności liniowej, stąd
\[
\dim_KV=\dim_K\ker T+\dim_K\operatorname{im}T.
\]
Przy wymiarze skończonym konstrukcję baz wykonuje się bez aksjomatu wyboru.
Nie dokonuje się nieuzasadnionego odejmowania nieskończonych liczb kardynalnych.

### 5. Pierwsze twierdzenie o izomorfizmie i faktoryzacja

Sprawdzono dobrą określoność
\(\widetilde T(v+\ker T)=T(v)\), liniowość, iniektywność, surjektywność i niezależność od wyboru bazy lub dopełnienia.
Skontrolowano diagram TikZ ilustrujący \(T=\widetilde T\circ\pi_{\ker T}\).
W osobnym istniejącym stwierdzeniu dowiedziono, że \(T\) przechodzi do \(V/U\) dokładnie przy \(U\subseteq\ker T\).

### 6. Składanie i izomorfizmy

Ponownie sprawdzono, że złożenie odwzorowań liniowych jest liniowe, a jądro i obraz zachowują wskazane zawierania.
Wykazano liniowość odwrotności bijektywnego odwzorowania liniowego.
Kryterium \(\dim V=\dim W<\infty\) uzasadnia równoważność iniektywności i surjektywności.
Operatory na \(K[X]\) prawidłowo pokazują, dlaczego analogiczna teza zawodzi w nieskończonym wymiarze.

### 7. Przestrzenie \(\operatorname{Hom}\), \(\operatorname{End}\) i projekcje

Sprawdzono punktowe działania w \(\operatorname{Hom}_K(V,W)\) oraz dowód
\(\dim_K\operatorname{Hom}_K(V,W)=mn\) dla wymiarów skończonych, w tym \(m=0\), \(n=0\).
Rodziny odwzorowań \(E_{ji}\) rzeczywiście stanowią bazę przestrzeni \(\operatorname{Hom}\).
Zweryfikowano dwuliniowość i łączność składania w \(\operatorname{End}_K(V)\), brak przemienności na przykładzie oraz przypadek \(V=\{0_V\}\).
Dla projekcji \(P^2=P\) udowodniono dokładnie \(V=\operatorname{im}P\oplus\ker P\) wraz z wymaganą identycznością na obrazie. Odwrotnie, suma prosta wyznacza jednoznaczną projekcję na pierwszy składnik wzdłuż drugiego.

## Poprawki pierwszego audytu

1. **Niejednoznaczny skalar w przykładzie**: dopisano \(2_K:=1_K+1_K\), aby wzór był precyzyjny nad ciałami dowolnej charakterystyki.
2. **Przypadek przestrzeni zerowej dla algebry endomorfizmów**: doprecyzowano, co oznacza algebra (dwuliniowe, łączne mnożenie) oraz że w przypadku \(V=\{0_V\}\) jedyny endomorfizm jest zarazem zerem i jedynką.
3. **Skład PDF**: pierwsza kompilacja dała 37-stronicowy plik z prawie pustą ostatnią stroną. Skrócono tylko końcowe podsumowanie bez usuwania treści matematycznej; końcowe sprawdzenie składu po tej poprawce wymaga jeszcze finalnego PDF.

Nie dodano osobnych nowych twierdzeń lub lematów podczas audytu; poprawki dotyczą istniejącej treści.

## Niezależne testy skończone

Dla wszystkich liniowych odwzorowań \(\mathbb F_2^3\to\mathbb F_2^2\), otrzymanych przez wybór obrazów trzech wektorów standardowych, wykonano **64 testy** wzoru na wymiar jądra i obrazu oraz zgodności mocy ilorazu przez jądro z obrazem.
Dla wszystkich **512 endomorfizmów** \(\mathbb F_2^3\) sprawdzono równoważność idempotentności z rozkładem \(V=\operatorname{im}P\oplus\ker P\) oraz identycznością na obrazie. Wykryto **58 projekcji**.
**Wynik: zero niezgodności.** Testy są pomocnicze i nie zastępują dowodów.

## Kontrola techniczna i integracja

- Trzy rozdziały zawierają łącznie **150 unikalnych etykiet**: 69 + 39 + 42.
- Zweryfikowano **62 wystąpienia `\\ref`/`\\eqref`** i brak nierozwiązanych odsyłaczy.
- Wszystkie środowiska LaTeX są poprawnie zagnieżdżone.
- Nie występują niedozwolone terminy „unia” i „relacja liniowa” w treści; zachowano historyczne etykiety odsyłaczy.
- Rozdział 03 nie wymaga zewnętrznych plików z rysunkami: diagram powstał bezpośrednio w TikZ.
- Plik główny i katalog zawierają rozdziały 01–03 w poprawnej kolejności.
- Przebieg CI dla integracji: [44902170079](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44902170079) — **success**; wstępny PDF: 37 stron i końcowy log LaTeX bez ostrzeżeń.
- Końcowy przebieg CI dla poprawionej treści: [44902522099](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44902522099) — **success**. Wszystkie etapy kontroli trzech rozdziałów, importów, etykiet, terminologii, kompilacji i eksportu zakończone powodzeniem. Finalny PDF liczy **37 stron A4** i nie zawiera ostrzeżeń w pliku `linear_algebra.log` (`LaTeX Warning`, `Overfull`, `Underfull`, `Missing character`, `Undefined control sequence`, `Fatal error`). Dokonano przeglądu stron 28, 30–37 i diagramu na stronie 33; bez nakładających się elementów. Uwaga redakcyjna: strona 37 zawiera jedynie krótkie podsumowanie rozdziału. Skrócenie podsumowania nie wyeliminowało dodatkowej strony; można ocenić układ w kolejnym audycie, bez obniżania poziomu szczegółowości dowodów.

W nieblokującym globalnym walidatorze repozytorium wciąż występują wcześniejsze problemy z innych skryptów; nie traktujemy ich jako usuniętych.

## Decyzja

**Rozdział 03 utworzony, włączony do książki i poddany pierwszemu audytowi. Pozostaje otwarty.** Kolejna iteracja powinna ponownie sprawdzić istniejącą treść bez rozszerzania zakresu, aż do audytu bez istotnych poprawek i sukcesu CI.
