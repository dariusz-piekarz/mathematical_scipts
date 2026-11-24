# Analiza funkcjonalna — 15A/05 — drugi niezależny czysty audyt po poprawce

**Data:** 24 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` — nie utworzono nowej gałęzi.  
**Źródło:** `chapters/pl/functional_analysis/15A-calkowanie-funkcji-w-przestrzeniach-lokalnie-wypuklych.tex`.  
**Blob SHA źródła:** `afe39ee7e7d189d2d15bbf4a81457cc57c63be7a`.  
**Blob SHA testu:** `6f44e390ea07e2e5593c8a0a246fd4060355f727`.  
**Werdykt matematyczny:** **drugi niezależny czysty audyt, 2/2** (15A/04 oraz 15A/05); do ostatecznego statusu STABILNY wymagany zakończony poprawnie workflow po zapisie niniejszego raportu. Materiał i test niezmienione od poprawki w 15A/03.

## Niezależna kontrola dowodów i precyzji sformułowań

1. **Kryterium sum Riemanna**: w dowodzie nie występuje niedozwolone utożsamienie zupełności ciągowej z ogólną zupełnością; ciąg wybranych podziałów daje jedną granicę, a kontrola przez wspólne rozdrobnienie daje zbieżność każdego odpowiednio drobnego podziału do tej samej granicy. Różne `delta_p` dla różnych seminorm nie wymagają jednego wspólnego `delta`.
2. **Liniowość, addytywność i nierówność seminormowa**: założenia dotyczące istnienia całek na obu podprzedziałach są jawne; nie wolno wnioskować z samej całkowalności na [a,b] o całkowalności każdego ograniczenia w przestrzeni niezupełnej. Nierówność `p(int f)<=int p(f)` ma poprawną orientację dla `a<b`.
3. **Ciągłe odwzorowania liniowe**: każdą sumę Riemanna dokładnie przenosi T, a ciągłość T przenosi jej granicę bez założenia zupełności przestrzeni docelowej. Rozdzielanie punktów przez funkcjonały wymaga lokalnej wypukłości Hausdorffa, uwzględnionej w twierdzeniu.
4. **Barycentrum**: współczynniki dodatnich długości przedziałów po podzieleniu przez b-a sumują się do 1, a zamknięcie otoczki wypukłej wystarcza do przejścia do granicy. Nie zakłada się nieprawdziwie, że ta otoczka musi być zwarta.
5. **Całkowanie w uzupełnieniu**: zanurzenie E do E-hat jest topologiczne, zatem zbieżność sum w uzupełnieniu do elementu obrazu E oznacza dokładnie zbieżność w E. Warunek zawierania całki w j(E) jest potrzebny w obu kierunkach.
6. **Całka niewłaściwa**: ogony `int_R^R' p(f)` zapewniają Cauchy'ego dla całek o granicach `a+n`; następnie ta sama nierówność pozwala zastąpić ciąg przez dowolne rzeczywiste R. Zupełność ciągowa jest użyta w legalnym miejscu.
7. **Newton–Leibniz**: oszacowanie po wszystkich seminormach daje pochodną w topologii E, włącznie z jednostronnymi granicami na końcach. Funkcjonały z E' wyznaczają pochodną i całkę, dlatego tożsamość z całką G' zachodzi w E.
8. **Różniczkowanie całki z parametrem**: dla każdej ciągłej seminormy p stosuje się Hahn–Banacha do skalarnego oszacowania przyrostu; użyta jest jednostajna ciągłość `partial_s f` na zwartym prostokącie. Argument nie wymaga nieprawdziwego w ogólnych przestrzeniach wektorowego twierdzenia o wartości średniej.
9. **Fubini dla funkcji ciągłych**: po obu stronach wewnętrzne całki są dobrze określone i ciągłe; ich sumy aproksymują tę samą sumę podwójną z błędem ograniczonym przez odpowiedni moduł ciągłości. Teza nie używa twierdzenia Fubiniego dla funkcji mierzalnych.
10. **Silna całka operatorowa**: silna ciągłość na zwartym odcinku zapewnia punktowe ograniczenie rodziny, a Banach–Steinhaus — ograniczenie jednostajne norm operatorów. Otrzymany operator `A` jest ograniczony, chociaż sama rodzina `T(t)` nie musi być ciągła w normie.

**Wynik: 10/10 dowodów przejrzanych powtórnie; nie wykryto nowej luki matematycznej ani fałszywego założenia.**

## Przykłady i warunki graniczne

- **`c_{00}`**: funkcja z rozłącznymi nośnikami ma całkę w `\ell^2` o wszystkich dodatnich współrzędnych `2^{-2n-1}\int_0^1\eta`; zatem całka nie należy do `c_{00}`. Odbicie o przeciwnym znaku zapewnia zerową całkę na [0,2], ale nie zapewnia istnienia całki po ograniczeniu do [0,1], co potwierdza niezbędność warunku z twierdzenia o addytywności.
- **`C^\infty(\Omega)`**: istnienie całki wynika z zupełności; ciągły operator różniczkowania i ewaluacji przenosi ją na całkę wartości pochodnych.
- **Przestrzeń Schwartza**: `q_{m,k}(\partial^\alpha u)<=q_{m,k+|\alpha|}(u)` zapewnia ciągłość różniczkowania, a oszacowanie seminormowe całki jest zgodne z topologią przestrzeni.
- **Modulacja**: po 15A/03 przykład jawnie pracuje w **zespolonym** `L^2(\mathbb R,\lambda_1;\mathbb C)`; `U_t f=e^{itx}f` jest unitarny, silnie ciągły i `\|U_t-I\|=2` dla każdego `t\ne0`. Równość normy wynika z supremum istotnego, a nie tylko z numerycznej próby w teście regresyjnym.

**Wynik: 4/4 przykłady poprawne, z kontrolą ostrych założeń.**

## Spójność źródła, LaTeX i bramki

Na faktycznym źródle z obecnej gałęzi potwierdzono 443 wiersze, 16 etykiet, osiem odwołań do innych części książki, po 10 początków i końców środowisk `proof`, a także 7 `twierdzenie`, 2 `stwierdzenie`, 1 `wniosek`, 1 `definicja`, 4 `przyklad`, 2 `uwaga`. Każda z 16 etykiet występuje dokładnie przy odrębnej jednostce; odsyłacze obejmują 14, 15B, 16 i 17. Poprawione `H=L^2(\R,\lambda_1;\C)` nadal występuje w źródle. Brak rysunków TikZ i stwierdzonych odstępstw od reguł terminologicznych.

Poprzedni dedykowany [workflow #45294996953](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45294996953) dla commitu `e76449d85b778c795ff6e4034057bf7edfbc96fd` zakończył się **completed/success** na tych samych blobach źródła i regresji. W audycie 15A/03 sprawdzono faktyczny 109-stronicowy PDF po poprawce wraz ze stroną 95 i jej poprawioną notacją; raport 15A/04 wskazał tę samą tożsamość źródeł. Dla końcowego zamknięcia wymagany jest osobny, zakończony zielonym wynikiem workflow po zapisie audytu 15A/05; zanim wynik nastąpi, nie traktować go jako udanego.

## Decyzja

**15A/05 — drugi niezależny czysty przegląd (2/2) na jednym niezmienionym źródle po poprawce.** Dopiero po potwierdzeniu zakończonego CI należy formalnie zapisać **STABILNY** i odblokować **15B**. Bez zmian w rozdziałach historycznych, źródle 15A, testach lub układzie książki.
## Zamknięcie po drugim czystym audycie — końcowe CI

Niezależnie odczytano dedykowany przebieg [#45295648912](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45295648912), wyzwolony commitem raportu 15A/05 `a7082cbc3510cf9d285cf4f53bf2989517ab5d95`. Jego rzeczywisty status to **completed / success**. Wszystkie kroki joba ukończone powodzeniem: regresje modułu 15A, generowanie kompletnego kontekstu 01–17 z modułami 15A i 15B, kompilacja LaTeX, kontrola PDF i odsyłaczy, publikacja PDF oraz logów.

Po potwierdzeniu CI ponownie sprawdzono bloby źródła `afe39ee7e7d189d2d15bbf4a81457cc57c63be7a` i regresji `6f44e390ea07e2e5593c8a0a246fd4060355f727`: pozostają identyczne jak przy poprawce w 15A/03, pierwszym czystym przeglądzie 15A/04 i drugim czystym przeglądzie 15A/05. Rzeczywisty PDF z takiej samej wersji źródła był już niezależnie zweryfikowany wizualnie w 15A/03; najnowszy przebieg potwierdził dodatkowo tworzenie i maszynowe kontrole aktualnego PDF. Nie przedstawiamy kompilacji ani testów regresyjnych jako formalizacji wszystkich dowodów.

**KOŃCOWA DECYZJA: MODUŁ 15A — STABILNY (2/2 czystych audytów na niezmienionym źródle + zakończony zielony workflow).** Odblokowano osobny cykl audytów **15B — Całki Bochnera, Pettisa, Dunforda i Gelfanda oraz miary wektorowe**, bez automatycznego oznaczania 15B albo rozdziału 16 jako stabilnych. Ta końcowa adnotacja zmienia wyłącznie raport audytu.
