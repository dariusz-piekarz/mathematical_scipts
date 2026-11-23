# Analiza funkcjonalna — rozdział 08 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/08-pary-dualne-i-topologie-slabe.tex.  
**SHA źródła po poprawkach:** a01d4316fdeacef759c89955b14bc062abedbcd4.  
**Werdykt:** audyt 08/01 **Z POPRAWKAMI (NIE CZYSTY)** — rozdział 08 w stabilizacji **0/2**. Nie rozpoczynać rozdziału 09, dopóki 08 nie przejdzie dwóch kolejnych czystych audytów tej samej wersji.

## Zakres i metoda

Odczytano rzeczywisty rozdział 08 na wskazanej gałęzi oraz wcześniejsze rozdziały 01–07 potrzebne dla założeń i odsyłaczy. Matematycznie przeanalizowano **12 dowodów**, **5 przykładów**, definicje oraz uwagi. Szczególnie kontrolowano nieograniczone podprzestrzenie w słabych otoczeniach, przejście od słabych do słabych-* topologii, konstrukcję algebraicznego uzupełnienia, rolę **sieci**, a nie wyłącznie ciągów, oraz zbiory słabo zwarte w definicji topologii Mackeya. Testy regresyjne sprawdzają wybrane modele, nie zastępują pełnych dowodów.

## Wszystkie 12 dowodów — 12/12 PASS po uzupełnieniu

1. **Topologia słaba generowana przez seminormy:** rodzina p_f(x)=|⟨x,f⟩| daje lokalnie wypukłą topologię początkową, nieosobliwe parowanie rozdziela punkty; opis bazy otoczeń i kryterium zbieżności sieci poprawne. PASS.
2. **Słaba ograniczoność:** punktowa ograniczoność dla każdego f∈F jest równoważna ograniczoności względem wszystkich otoczeń zawierających skończone przecięcia podpoziomic. Nie wymaga założenia Banacha–Steinhausa. PASS.
3. **Przestrzeń sprzężona topologii słabej:** ciągły g zeruje się na ker T dla mapy T:E→K^m zbudowanej ze skończenie wielu f_j. Faktoryzuje się przez T(E), a algebraiczne przedłużenie do K^m wyraża g jako skończoną kombinację elementów F. PASS.
4. **Inkluzja topologii słabej i wyjściowej:** wszystkie f∈E' są ciągłe dla τ, więc σ(E,E')⊂τ; przestrzenie sprzężone są identyczne przez wynik z punktu 3. PASS.
5. **Domknięcie podprzestrzeni przez anihilator:** przecięcie jąder funkcjonałów z M⊥ jest słabo i wyjściowo domknięte, a punkt spoza wyjściowego domknięcia M jest oddzielany funkcjonałem przez Hahn–Banacha. PASS.
6. **Otoczenia słabe w nieskończonym wymiarze:** wspólne jądro skończenie wielu f_j ma kowymiar skończony, więc zawiera niezero v, a cała prosta Kv znajduje się w otoczeniu. Niezdegenerowaność F zapewnia funkcjonał nieograniczony na tej prostej; brak ograniczonego otoczenia wyklucza normowalność. PASS.
7. **Słabe domknięcie sfery jednostkowej:** kula domknięta słabo przez funkcjonały normujące Hahna–Banacha. Dla ||x||<1 kierunek v w jądrze skończenie wielu funkcjonałów pozwala dotrzeć do sfery bez zmiany ich wartości. Punkty z ||x||=1 już należą do sfery. PASS.
8. **Słaba i słaba-* topologia na E':** σ(E',E)⊂σ(E',E'') przez J(E)⊂E'', a równość topologii wymusza, że ich przestrzenie sprzężone są jednakowe; z wyniku 3 dostajemy J(E)=E'', czyli refleksywność. PASS.
9. **Uzupełnienie (E,σ(E,F)) w F*:**
   - liniowość warunków definiujących F* opisuje domkniętą podprzestrzeń produktu K^F; dlatego F* jest zupełna i Hausdorffa;
   - J:E→F* jest topologicznym zanurzeniem przez niezdegenerowaność i identyczność definicji topologii;
   - dla skończenie wymiarowego G⊂F mapa T:E→G* jest surjektywna — gdyby nie, istniałby niezerowy element G unicestwiany przez wszystkich x∈E;
   - interpolacja Φ|_G dowodzi gęstości J(E) w F*.
   Wszystkie kwantyfikatory i przejścia kontrolowano. PASS.
10. **Słaba niezupełność przestrzeni nieskończenie wymiarowej:** wynik jest prawdziwy nawet dla przestrzeni Hilberta, ale pierwotny dowód pomijał uzasadnienie nieskończonego wymiaru E' i nie pokazywał, skąd bierze się rozbieżność intuicji dotyczącej ciągów.
   **Poprawiono:** dla niezależnych x_1,…,x_n definiuje się ciągłe współrzędne na ich rozpiętości i przedłuża przez Hahn–Banacha do liniowo niezależnych f_1,…,f_n∈E'; zatem dim E'≥n dla wszystkich n. Na nieskończenie wymiarowej normowanej E' istnieje nieciągły algebraiczny funkcjonał Φ. Każdy J(x) jest normowo ciągły, więc Φ∉J(E). W dodatku jawnie konstruuje się słabo fundamentalną, niezbieżną sieć x_G, indeksowaną skończenie wymiarowymi G⊂E', z f(x_G)=Φ(f) na G. Tym samym nie polegamy wyłącznie na abstrakcyjnym argumentowaniu przez gęstą właściwą podprzestrzeń. PASS **po korekcie**.
11. **Topologia silna na przestrzeni sprzężonej przestrzeni unormowanej:** dla ograniczonego B zachodzi p_B(f)≤(sup_B||x||)||f||, zaś kula jednostkowa daje p_{B_E}(f)=||f||, co dowodzi równoważności topologii. PASS.
12. **Poprawność definicji topologii Mackeya:** p_K jest skończone przez ciągłość parowania i zwartość K w σ(F,E); absolutna wypukłość i podliniowość supremum dają seminormy. Dyski K_f={af:|a|≤1} są zwarte i absolutnie wypukłe, a p_{K_f}=|⟨·,f⟩|, więc τ(E,F) zawiera σ(E,F) i jest Hausdorffa. PASS.

## Wszystkie 5 przykładów — 5/5 PASS

1. **Kanoniczna para (E,E'):** lokalna wypukłość i Hausdorff rozdzielają niezerowe wektory przez Hahn–Banacha, a drugi warunek to niezerowość funkcjonału. PASS.
2. **Para c₀ i ℓ¹:** szereg parowania jest bezwzględnie zbieżny i obie strony są rozdzielane przez wektory jednostkowe. PASS.
3. **e_n w ℓ²:** wektory jednostkowe zbiegają słabo do zera, ale zachowują normę 1. PASS.
4. **e_n w ℓ¹, σ(ℓ¹,c₀):** słaba-* zbieżność wynika z x_n→0 dla każdego x∈c₀, ale słaba zbieżność jest wykluczona przez ciąg (1,1,…)\inℓ∞. PASS.
5. **Topologia produktowa na K^N:** dokładnie σ(K^N,c₀₀), ponieważ wszystkie ciągłe funkcjonały zależą od skończenie wielu współrzędnych. PASS.

## Korekty i nowe testy

1. Dowód niezupełności: dodano samodzielne uzasadnienie nieskończonego wymiaru E' oraz skierowaną rodzinę skończenie wymiarowych podprzestrzeni, pozwalającą skonstruować słabo fundamentalną sieć bez słabej granicy. Wyjaśniono, że nie można mylić zupełności względem sieci z zachowaniem ciągów.
2. Ujednolicono terminologię na „przestrzeń sprzężona” i „przestrzeń algebraicznie sprzężona” w tytułach, sformułowaniach i uwagach. Nazwy pliku i etykiet pozostały niezmienione dla stabilności odsyłaczy.
3. Dodano **17 testów** w tools/tests/test_functional_analysis_ch08.py: strukturę dokumentu i odsyłaczy, niezdegenerowaność, otoczenia słabe, ograniczoność, skończoną reprezentację funkcjonałów, anihilatory, sferę, słabą-* zbieżność, topologię produktu, interpolację skończonego układu liniowego, liniową niezależność przedłużeń, różnicę między siecią a ciągiem, seminormy topologii silnej i Mackeya.
4. Dodano .github/workflows/functional-analysis-ch08.yml — pełny kontekst prawdziwych rozdziałów 01–08, 17 regresji, kompilacja LaTeX i sprawdzenie PDF/odsyłaczy.

## Kontrola strukturalna i techniczna

- Zliczono **12 par środowisk proof, 5 par przyklad, 18 unikatowych etykiet i 9 wystąpień odsyłaczy**; 0 odsyłaczy nierozwiązanych w rzeczywistym zbiorze rozdziałów 01–08.
- Poprawione źródło: SHA a01d4316fdeacef759c89955b14bc062abedbcd4.
- Dedykowany [CI 45196353669](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45196353669): 17 testów i przygotowanie kontekstu 01–08 mają wynik PASS. Końcową kompilację i wizualny przegląd PDF uzupełnić po ukończeniu przebiegu.

## Decyzja

**Rozdział 08 przeszedł pierwszy pełny audyt ze zmianami źródła, więc audyt 08/01 NIE jest czysty i licznik wynosi 0/2.** Do rozdziału 09 przechodzimy dopiero po dwóch kolejnych niezależnych audytach niezmienionej wersji 08 bez nowych korekt.
