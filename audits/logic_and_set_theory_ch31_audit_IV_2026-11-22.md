# Logika matematyczna i teoria mnogości — rozdział 31, audyt IV: kondensacja, GCH i granice założeń

**Data:** 22 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex`.  
**Tryb:** kontrola matematyczna *bez zmian* źródła.

## Kontrola kondensacji

1. **Relacja spełniania.** W definicji `Def(M)` zastosowano relację prawdziwości **ustalonej struktury o zbiorowym uniwersum**, nie globalny predykat prawdy dla klasy `L`. Kod formuły i parametrów przebiega zbiór; schemat zastępowania wyznacza `Def(M)` jako zbiór.
2. **Elementarność odcinków.** Lemat `lem:l-elementary-section-75` wymaga tranzytywności większej struktury `D`, elementarności `X≺D` i `A∈X`; wtedy relatywizacja `φ^A` oraz kryterium Tarskiego–Vaughta rzeczywiście pozwalają otrzymać `X∩A≺A`. Przykład struktury nietranzytywnej pokazuje konieczność warunku.
3. **Definiowalność a kolaps.** Lemat `lem:l-collapse-def-compatibility` nie zakłada bez dowodu `π(L_γ)=L_{π(γ)}`; wymaga tej równości i na jej podstawie dowodzi zgodności `Def` z kolapsem. Nie odwrócono logicznego kierunku.
4. **Ograniczone tablice.** Lemat lokalnych tablic spełniania dotyczy *jednej* ustalonej formuły. Z podanej konstrukcji nie wynika zbiorowa tablica prawdy dla wszystkich formuł w każdym `L_θ` i tekst wyraźnie przestrzega przed takim błędem.
5. **Operacje Gödla.** Zestaw dziesięciu operacji i ich ustalone grafy `Δ₀` zapewniają absolutność skończonych termów w przechodnich strukturach na nie domkniętych. W `lem:l-all-stage-histories-78` przy granicznej `α` każda wcześniejsza historia mieści się w `L_α` ze względu na skończony koszt etapów, a zbiór wszystkich par indeks–poziom jest definiowalny nad `L_α` jedną formułą. Podkreślono brak zastępowania wewnątrz `L_α`.
6. **Skończony pakiet.** W `lem:l-finite-condensation-package` używa się jednej *skończonej* koniunkcji zdań `σ_*`: domknięcia na operacje, brak największego ordynału, istnienie historii dla każdego ordynału oraz pokrycie całej struktury poprawnymi historiami. Wystarczalność do `N=L_β` jest argumentem zewnętrznym w ZF i nie przypisuje `L_θ` wszystkich aksjomatów ZF.
7. **Kolaps dowolnej podstruktury.** Kolaps `X≺L_θ` jest tranzytywny i spełnia ten sam pakiet `σ_*`, co pozwala zidentyfikować go z `L_β`. Wysokość `β≤θ` jest wyprowadzona z porządku na `X∩Ord`; nie wymaga założenia `X∩L_γ=L_γ`.
8. **Wariant języka rozszerzonego.** Niezależna wersja `lem:l-expanded-hull-condensation` jawnie podaje relacje `R,S,D` jako relacje *zewnętrzne* na `L_θ`. Nie przypisuje im niesprawdzonej definiowalności wewnętrznej. Jednoznaczność `D` i relatywizacja spełniania pozwalają przeprowadzić indukcję po poziomach, także w kroku granicznym.

## Kontrola GCH i niesprzeczności względnej

9. **Odpowiedni kadłub.** Dowód GCH najpierw pracuje w `ZFC+V=L`, a dopiero na końcu przenosi rezultat do wewnętrznego `L`. W kadłubie elementarnym o mocy `κ` umieszcza się **każdy element `κ`**, samą liczbę `κ` i parametr `A⊆κ`. W wyniku `π(ξ)=ξ` dla `ξ≤κ`, zatem `π(A)=A`.
10. **Moc obrazu i ograniczenie poziomu.** Skoro `|L_β|=|X|=κ` i `β⊆L_β`, dostajemy `|β|≤κ`, a więc `β<κ⁺`. Dla dowolnego `A⊆κ` mamy `A∈L_β⊆L_{κ⁺}`; z liczności `L_{κ⁺}` wynika `2^κ≤κ⁺`, a z twierdzenia Cantora i porządku liniowego kardynałów w ZFC `2^κ≥κ⁺`.
11. **Wewnętrzne kardynały.** Formuła `L⊨2^κ=κ⁺` posługuje się kardynałami i następnikami kardynałów liczonymi **w `L`**. Nie utożsamia ich z kardynałami w otaczającym `V`.
12. **Relatywizacja dowodu niesprzeczności.** Wniosek `Con(ZF)⇒Con(ZFC+GCH)` korzysta z interpretacji aksjomatów przez definowalną klasę `L`. Argument z dowodami skończonymi nie wymaga istnienia przeliczalnego modelu tranzytywnego.

**Werdykt IV:** bez nowych usterek matematycznych i językowych w części o kondensacji i GCH; nie zmieniono TeX. Inwentarz nadal: 6 definicji, 27 lematów, 9 przykładów, 5 twierdzeń, 16 uwag, 2 wnioski, 34 dowody; 68 etykiet i 87 odsyłaczy. Wstępny PDF obejrzało 24 strony rozdziału; końcowy audyt V wymaga jeszcze zbieżności SHA najnowszego źródła i zielonego pełnego CI.
