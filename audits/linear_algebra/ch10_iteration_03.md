# Algebra liniowa — rozdział 10, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/10-algebry-tensorowa-symetryczna-i-zewnetrzna.tex`  
**SHA zbadanej treści:** `05a9a359896c434c12f0e06c9764ecf6dab59a4e`  
**Poprzedni audyt:** `audits/linear_algebra/ch10_iteration_02.md`  
**Materiał kontrolny:** `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex`.

## Metodyka

Trzecia, niezależna kontrola istniejącej wersji rozdziału 10 po pojedynczej korekcie z audytu II. Sprawdzono samodzielność sformułowań i kwantyfikatorów, formalne istnienie i jednoznaczność konstrukcji ilorazowych, poprawność przechodzenia między tensorami, funkcjonałami i formami, granice ważności w dodatniej charakterystyce, przykłady i rysunki. Nie dodano nowego materiału ani nie zmieniono żadnego twierdzenia.

## Ponowne sprawdzenie korekty stopnia zerowego

Pierwszy izomorfizm w twierdzeniu `thm:lin10-formy-alt` przy `k=0` ma dziedzinę `(Λ^0(V))^*=K^*` i przeciwdziedzinę `Alt^0(V^*)=K`. Zweryfikowano, że `L↦L(1_K)` jest liniowe, a `a↦(x↦ax)` jest jego liniową odwrotnością. Zmiana wprowadzona w audycie II rozwiązuje nieprecyzyjne utożsamienie tych przestrzeni. Druga identyfikacja `Λ^0(V^*)=K→Alt^0(V^*)=K` pozostaje identycznością.

## Niezależne sprawdzenie wszystkich istniejących twierdzeń

1. **Podstawowe algebry:** algebra tensorowa ma dobrze określone mnożenie przez kanoniczną konkatenację, łączność i jedynkę. Konstrukcja odwzorowania na `⊕_{k≥0}V^{⊗k}` nie wymaga nieskończonych sum; każda składowa jest linearyzowana niezależnie.
2. **Algebra symetryczna:** ideał generowany przez `u⊗v-v⊗u` jest jednorodny. Uniwersalna faktoryzacja do przemiennej algebry zachodzi dla dowolnej charakterystyki. Izomorfizm z pierścieniem wielomianów dowodzi niezależności jednomianów i wzoru wymiarowego, także przy `n=0`.
3. **Algebra zewnętrzna:** ideał kwadratów `v⊗v` daje naprzemienność w każdej charakterystyce. Antykomutacja nie służy jako samodzielna definicja przy `char K=2`. Reguła znaku `(-1)^{pq}` jest poprawna dla wszystkich stopni nieujemnych.
4. **Własność uniwersalna potęgi zewnętrznej:** dowód dokładnie identyfikuje jednorodne generatory ideału w stopniu `k`. Liniowa faktoryzacja formy naprzemiennej nie zależy od przedstawicieli ani od podzielenia przez `k!`.
5. **Bazy:** znikanie powtórzonych indeksów i uporządkowanie rosnące dają rozpiętość, a funkcjonały wyznacznikowe odróżniają współczynniki. Otrzymuje się `dim Λ^k V=binom(n,k)`, `Λ^k V=0` dla `k>n` i `dim Λ(V)=2^n`.
6. **Współrzędne i minory:** rozwinięcie `v_1∧...∧v_k` współczynnikami wyznacznikowymi jest poprawne. Przy zastosowaniu `Λ^k A` elementy macierzy są minorami o indeksach rosnących.
7. **Wyznacznik:** działanie `Λ^n A` na jednowymiarowej przestrzeni jest mnożeniem przez `det A`, zgodnie z wcześniejszą definicją z rozdziału 06. Dla `n=0` `Λ^0 A=id_K` i `det A=1_K`.
8. **Cauchy–Binet:** rachunek `Λ^k(AB)=Λ^k A Λ^k B` wraz z wyborem baz dowodzi formuły sumującej po wszystkich rosnących indeksach pośrednich. W przypadku `k>n` obie strony są zerowe; przy `k=0` wyznaczniki puste są równe jedynce.
9. **Dual i iloczyn form:** `(Λ^k V)^*≅Alt^k(V^*)` wynika z własności uniwersalnej także bez skończonego wymiaru, a `Λ^k(V^*)≅Alt^k(V^*)` udowodniono w skończonym wymiarze. Wzór z przetasowaniami jest odpowiednim rozwinięciem Laplace'a i nie wymaga dzielenia przez silnie.
10. **Rzutowania:** operatory `𝓢_k`, `𝓐_k` spełniają `𝓢_k²=k!𝓢_k`, `𝓐_k²=k!𝓐_k`. Opis ilorazów przez obrazy rzutowań jest poprawnie ograniczony do ciał, w których `k!1_K` jest odwracalne. W przeciwnym przypadku ilorazy nadal istnieją.
11. **Przykłady i rysunki:** przykład nieprostego dwuwektora został sformułowany nad `R`, gdzie `ω∧ω=2e_{1234}≠0`; nie wysuwa fałszywej implikacji z tego rachunku w charakterystyce `2`. Diagram linearyzacji i ilustracja pola równoległoboku odpowiadają wzorom tekstu.

## Weryfikacja techniczna

- W dziesięciu rozdziałach: **429 unikalnych etykiet**, **181 odsyłaczy do istniejących etykiet**, kompletne importy, spójny katalog i brak niezrównoważonych środowisk LaTeX. Terminologia zgodna ze standardami.
- Regresja iloczynów tensorowych `tools/test_linear_algebra_tensors.py`: 4 konfiguracje konstrukcji ilorazu, 6817 par Kroneckera, 6817 testów mnożenia, 97 testów prostoty tensorów.
- Regresja zewnętrzna `tools/test_linear_algebra_exterior.py` na `F_2` i `F_3`: **1190** testów naprzemienności, **29088** porównań współczynników z minorami, **42673** kontroli Cauchy'ego–Bineta, **9600** testów iloczynu przez przetasowania, **30** kontroli wymiaru. Wszystkie zakończyły się sukcesem w [CI 44916801770](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44916801770).
- Pierwszy przebieg po integracji rozdziału: [CI 44916678656](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44916678656) — `success`. Po dodaniu testów uzyskano **108 stron PDF**, bez ostrzeżeń LaTeX, w [CI 44916801770](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44916801770).
- Wykonano walidacje dla aktualnej wersji tekstu po korekcie stopnia zerowego; dalszy wynik GitHub Actions dla niniejszego commitu raportowego weryfikujemy osobno i nie zakładamy go przed zakończeniem.

## Decyzja

**Audyt III — czysty.** Nie wykryto kolejnych błędów, braków kwantyfikacji, niepoprawnych dowodów ani nowych usterek LaTeX. Plik rozdziału 10 pozostawiono bez zmian. Zgodnie z przyjętą procedurą po audycie I, korekcie audytu II oraz czystej iteracji III **rozdział 10 uznaje się za stabilny i zamknięty**. Niniejszy commit zmienia tylko raport i komentarz statusowy książki.
