# Logika matematyczna i teoria mnogości — rozdział 31, audyt V (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Uniwersum konstruowalne i modele wewnętrzne”.  
**Plik TeX:** `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** jeden rozdział, ponowna niezależna kontrola bez zmian w źródle w iteracji V.

## Audyt matematyczny

1. **Operator definiowalnych podzbiorów:** zweryfikowano, że `Def(M)` definiuje się nad *zbiorem* `M` przez zakodowane formuły i skończone krotki parametrów, bez nieistniejącej zbiorowej relacji prawdy dla klasy `L`. Konwencja `Def(∅)={∅}` jawnie obsługuje przypadek pustej struktury.
2. **Tranzytywność hierarchii i pierwsze etapy:** indukcja `L_α` opiera się na fakcie `L_α⊆L_{α+1}`, na definiowalności `a={x∈L_α:x∈a}` z parametrem `a`, a na etapach granicznych na sumach poziomów. Zmodyfikowany dowód `L_α∩Ord=α` uzasadnia absolutność predykatu `Ord` przez jego postać ograniczoną. Osobno uzasadniono `L_n=V_n` dla skończonych `n` i `ω∈L_{ω+1}`.
3. **Formuły ograniczone i refleksja:** `Δ₀` jest absolutna między strukturami tranzytywnymi dla wspólnych parametrów. Odbicie skończonej rodziny formuł do pewnego `L_θ` konstruuje jedną rosnącą rodzinę indeksów z minimalnych etapów pojawienia się świadków, zbieranych przez zastępowanie. Etapy są wyznaczone jednoznacznie w ZF, bez AC lub DC.
4. **Aksjomaty ZF wewnątrz L:** sprawdzono oddzielnie ekstensjonalność, pustkę, parę, sumę, nieskończoność, wyróżnianie, zbiór potęgowy, zastępowanie i ufundowanie. Wewnętrzny zbiór potęgowy elementu `a` obejmuje dokładnie te podzbiory `a`, które należą do `L`; nie utożsamia się go z pełnym zewnętrznym `P(a)`.
5. **Kanoniczny dobry porządek:** kody definicji i skończone krotki parametrów nadają dobrą kolejność nowym elementom każdego poziomu. Rekurencja zachowuje wcześniejsze porządki, co daje zgodny dobry porządek całej klasy i pozwala wewnętrznie udowodnić AC.
6. **Kolaps Mostowskiego i podstruktury elementarne:** sprawdzono warunki ekstensjonalności, ufundowania i kryterium Tarskiego–Vaughta dla przekrojów `X∩A`. Rozróżniono elementarność przekroju od znacznie silniejszej i osobno uzasadnianej równości `π(L_γ)=L_{π(γ)}`.
7. **Operacje Gödla i kodowanie poziomów:** dziesięć ustalonych operacji, ich ograniczone definicje i absolutność skończonych termów pozwalają kodować `Def` i historie etapów jedną formułą pierwszego rzędu. Zbiorowe tablice spełniania dla ustalonych formuł nie zostały utożsamione z predykatem prawdy dla właściwej klasy `L`. Skończony pakiet `σ_*` jest rzeczywiście pakietem *skończonym*, a nie niejawnie użytym schematem pełnej ZF w `L_θ`.
8. **Lemat kondensacji:** dla dowolnego `X≺L_θ` (graniczne `θ>0`) kolaps `N` przenosi prawdziwość pakietu `σ_*`, który identyfikuje `N=L_β`. W wariancie rozszerzonego języka relacje `R,S,D` są jawnie zewnętrzne, a ich elementarność zapewnia indukcję po poziomach `L`. Różne warianty dowodu nie zakładają bez uzasadnienia tej samej przesłanki.
9. **GCH w L:** kadłub `X` ma moc `κ`, zawiera wszystkie ordynały `ξ<κ`, a także `κ` i `A⊆κ`. Kolaps ustala `A`, dlatego `A∈L_β` dla `β<κ⁺`. Z `|L_{κ⁺}|=κ⁺` oraz twierdzenia Cantora otrzymuje się GCH. Argument przeprowadzony w `ZFC+V=L` jest następnie przeniesiony do *wewnętrznej* klasy `L`, bez utożsamiania jej kardynałów z kardynałami otaczającego uniwersum.
10. **Względna niesprzeczność:** wyprowadzenie `Con(ZF)⇒Con(ZFC+GCH)` opiera się na interpretacji aksjomatów przez definowalną klasę `L` i skończoności formalnego dowodu. Nie zakłada istnienia przeliczalnego modelu tranzytywnego.

**Werdykt matematyczny:** powtórny audyt nie wykazał nowych nieuzasadnionych wzorów, brakujących kwantyfikatorów, istotnych luk ani uchybień terminologicznych wymagających zmiany źródła.

## Kontrola techniczna

- Zachowano **65 ponumerowanych elementów** i oryginalny zakres pełniejszej wersji źródłowej: **6 definicji, 27 lematów, 9 przykładów, 5 twierdzeń, 16 uwag, 2 wnioski i 34 środowiska dowodu**.
- **68 unikatowych etykiet i 87 odsyłaczy** w rozdziale; rozdziały 1–31 mają łącznie **770 etykiet i 579 odsyłaczy**. Żaden odsyłacz nie pozostaje nierozwiązany.
- GitHub Actions [#45011668909](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011668909): **SUCCESS**. W tym testy `test_logic_and_set_theory_ch31.py`, pełna walidacja struktury i kolejności rozdziałów oraz kompilacja i kontrola PDF.
- SHA źródła `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex` na gałęzi jest identyczny ze SHA pliku w pomyślnym przebiegu: `65b73f3dae01c34e0d24f16e439f993d7225c39b`.
- Pełna książka zawiera **272 strony PDF**. Rozdział 31 zajmuje **24 strony** (strony PDF 249–272). Wyrenderowano i wizualnie przejrzano każdą stronę, bez uciętych wzorów, kolizji napisów lub naruszenia marginesów.
- Log TeX: **0** przepełnień `Overfull \\hbox`, **0** niezdefiniowanych referencji, **0** niezdefiniowanych cytowań i **0** błędów LaTeX. W całym skrypcie pozostaje **1** niegroźne `Underfull \\hbox` niewpływające na czytelność.

## Werdykt

**ROZDZIAŁ 31 — STABILNY po audycie V.** Audyty I–III przyniosły rzeczywiste poprawki źródła; audyty IV i V nie wymagały kolejnych zmian. Dostępny jest osobny PDF rozdziału. Rozdział 32 nie był jeszcze audytowany ani włączony do głównej książki w tej iteracji.
