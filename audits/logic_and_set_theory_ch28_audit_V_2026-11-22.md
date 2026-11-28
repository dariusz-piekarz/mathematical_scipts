# Logika matematyczna i teoria mnogości — rozdział 28, audyt V (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/28-liczby-porzadkowe-i-rekurencja-pozaskonczona.tex`  
**Zakres:** wyłącznie rozdział 28, bez nowego materiału i bez zmian źródła w tej iteracji.

## Niezależna kontrola matematyczna

1. **Definicja ordynału i elementy:** sprawdzono warunki przechodniości zbioru i dobrego porządku przez relację przynależności, ordynały skończone i uzasadnienie, że `ω` jest ordynałem. Lemat o elementach i odcinkach początkowych ma poprawnie określone zbiory, warunki oraz uzasadnienie jednoznaczności.
2. **Trójpodział ordynałów:** dowód wykorzystuje wcześniejszy lemat porównania dobrych porządków oraz własność identyczności izomorfizmów ordynałów z ich odcinkami początkowymi. Rozłączność przypadków wynika z dobrze ufundowanej przynależności.
3. **Suma i następnik:** przechodniość, porównywalność elementów, istnienie minimum dowolnego niepustego podzbioru, własność supremum, minimalność następnika zostały wykazane osobno. Uwzględniono pustą sumę, następnik zerowy i ordynały graniczne.
4. **Indukcja pozaskończona:** kwantyfikacja po `β<α` ma postać formuły ZF z parametrami; zbiór kontrprzykładów istnieje przez separację, a wybór najmniejszego kontrprzykładu jest uzasadniony dobrym porządkiem.
5. **Rekurencja pozaskończona:** zweryfikowano formalnie definiowalne poprawne przybliżenia, ich zgodność przez pierwszy punkt niezgodności, wszystkie trzy przypadki indukcji i zbiór przybliżeń powstający przez zastępowanie. Na etapie granicznym dziedzina sumy przybliżeń jest identyfikowana za pomocą `lem:ordinal-limit-union`. Nie potrzeba aksjomatu wyboru.
6. **Dodawanie i mnożenie ordynałów:** sprawdzono wyraźne określenie operacji rekurencyjnej dla wszystkich wymaganych funkcji częściowych, zgodność wyników z różnych odcinków, przykład `1+ω=ω`, a także `2·ω=ω` i `ω·2=ω+ω>ω`. Różnica między arytmetyką ordynałów i mocy nie jest zacierana.
7. **Hierarchia von Neumanna:** poprawne ograniczenia indeksów `δ+1<α` i `λ<α`; wartości `V_0,V_1,V_2,V_3` mają poprawne definicje. Nie zakłada się istnienia zbioru wszystkich poziomów hierarchii.
8. **Reprezentanci kardynalni:** szczegółowo skontrolowano ZF-konstrukcję izomorfizmu `r:W→γ`, w tym jedyność przybliżeń i schemat zastępowania, tożsamość `u≺v ⇔ r(u)∈r(v)`, przechodniość obrazu i warunek dobrego porządku. Aksjomat wyboru użyty jest tylko do wyposażenia dowolnego `A` w dobry porządek. Separacja w `α+1` daje najmniejszy reprezentant.
9. **Paradoks Buralego–Fortiego:** dowód nie posługuje się zbiorem wszystkich ordynałów jako istniejącym obiektem; jego założenie prowadzi do sprzeczności `γ∈γ` z ufundowaniem.

**Wynik:** powtórny audyt V nie wykazał nowych nieuzasadnionych wzorów, braków kwantyfikatorów ani błędnych odsyłaczy. Nie zmieniono w nim tekstu źródłowego.

## Inwentarz i walidacja

- Struktura: **4 definicje, 5 przykładów, 2 lematy, 5 twierdzeń, 1 wniosek, 3 uwagi, 8 dowodów**.
- **17 etykiet i 20 odsyłaczy**; wszystkie mają istniejące cele w skrypcie liczącym 28 rozdziałów.
- Testy strukturalne, regresje i pełny workflow [GitHub Actions #45007874795](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45007874795): **SUCCESS**.
- Zgodność aktualnego bloba źródłowego z plikiem w zakończonym przebiegu została zweryfikowana przez porównanie SHA.
- Pełna książka: **219 stron**. Samodzielny PDF rozdziału 28: **6 stron**, stanowiących strony 214–219 pełnego pliku.
- Obejrzano wszystkie sześć stron aktualnie wyrenderowanego PDF. Nie występuje nachodzenie tekstu, ucięcie wzorów, utrata podpisów ani przekroczenie marginesów.
- Log kompilacji: **0** `Overfull \hbox`, **0** niezdefiniowanych odsyłaczy, **0** nierozwiązanych cytowań. Pozostaje **1** niegroźne ostrzeżenie `Underfull \hbox` (badness 1406), bez wpływu na czytelność.

## Werdykt

**ROZDZIAŁ 28 — STABILNY po audycie V.** Audyty I–IV przyniosły rzeczywiste rozwinięcia i korekty istniejących dowodów; audyt V jest pierwszą niezależną iteracją bez zmian przy zielonym CI i pełnej kontroli PDF. Kolejny rozdział 29 nie był przedmiotem tej iteracji.
