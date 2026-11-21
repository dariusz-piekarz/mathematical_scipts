# Algebra liniowa — rozdział 09, audyt VI (czysta iteracja stabilizacyjna)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Sprawdzony rozdział:** `chapters/pl/linear_algebra/09-iloczyny-tensorowe.tex`  
**Sprawdzony blob SHA:** `0dc33d1aafb0d24e1346295bc2f6bf33e3455fea`  
**Punkt wyjścia:** [raport audytu V](ch09_iteration_05.md)  
**Źródło porównawcze:** `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex`, blob `7ab3f15ced06e8233f978471c779e343ac5902ca`.

## Zakres i reguła pracy

Przeprowadzono ponownie niezależne sprawdzenie **istniejącej** treści rozdziału 09 po zmianach z audytu V. Oceniono poprawność matematyczną i kwantyfikatory każdego twierdzenia, kroki dowodów, definicje, przykłady, zastosowania, przypadki brzegowe, język, notację, odsyłacze i diagram. Nie dodano nowych wyników ani nie rozszerzono materiału.

## Weryfikacja trzech korekt z audytu V

1. **Dowód rozpiętości w dowolnej realizacji:** niech `(T,τ)` spełnia własność uniwersalną oraz `S=span(τ(V×W))`. Oba liniowe odwzorowania `q:T→T/S` (ilorazowe) i `z:T→T/S` (zerowe) mają zerowe złożenie z `τ`. Jednoznaczność faktoryzacji dla odwzorowania zerowego `b:V×W→T/S` wymusza `q=z`. Ponieważ `q` jest surjektywne, `T/S=0` i `S=T`. Sprawdzono niezależność argumentu od wyboru baz, wymiaru i charakterystyki ciała; dowód jest kompletny.
2. **Bazy w twierdzeniu o rzędzie tensora:** `B=(v_1,...,v_n)` oraz `C=(w_1,...,w_m)` są zadeklarowane w samym twierdzeniu, a rozwinięcie `t=Σ_i Σ_j c_ij v_i⊗w_j` ma jawne granice. Dowód obydwu nierówności przy rozkładzie na tensory proste pozostaje prawidłowy.
3. **Założenia twierdzenia o rzędzie Kroneckera:** wielkości `r,n,s,m` określono jako nieujemne liczby całkowite. Wzór obejmuje macierze o zerowych wymiarach i rzędy zerowe; pozostała część dowodu jest poprawna.

## Niezależna ponowna kontrola całego rozdziału

- **Konstrukcja i uniwersalność:** formalna baza `K^(V×W)`, cztery rodziny generatorów `N`, liniowość kanonicznego odwzorowania w obu argumentach, `N⊂ker L_b`, dobrze określona faktoryzacja i jednoznaczność liniowego przedłużenia są poprawnie udowodnione.
- **Tensory proste:** `v⊗w=0` dokładnie wtedy, gdy co najmniej jeden czynnik jest zerowy; dla dwóch niezerowych czynników rozdzielające funkcjonały istnieją dzięki bazom Hamela, zgodnie z przyjętymi w poprzednich rozdziałach założeniami teoriomnogościowymi.
- **Współrzędne i rząd:** wartości funkcjonałów `L_{pq}` na tensorach bazowych dają liniową niezależność, a ich liczba daje `dim(V⊗W)=dimV·dimW`. Rozkład macierzy współczynników na zewnętrzne iloczyny wektorów kolumnowych i wierszowych dowodzi wzoru na minimalną liczbę prostych składników.
- **Odwzorowania liniowe i Kronecker:** definiowanie `S⊗T` przez własność uniwersalną jest niezależne od przedstawienia tensora. Wzory na macierz, transpozycję, składanie i rząd obowiązują przy podanych rozmiarach, także prostokątnych.
- **Izomorfizmy kanoniczne:** konstrukcje zamiany czynników, łączności i jednostki `K⊗V≅V` są poprawne. Przykład z determinantem nad `R` prawidłowo rozróżnia izomorfizm `γ(v⊗w)=w⊗v` od równości tensorów.
- **Linearyzacja wielu argumentów:** indukcyjne odwzorowania `L_w` są liniowe, a ich zależność od ostatniego argumentu również jest liniowa; gwarantuje to własność uniwersalną `k`-czynnikowego iloczynu tensorowego.
- **Operatory i dualność:** odwzorowanie `W⊗V*→Hom(V,W)` jest iniektywne, ma za obraz dokładnie operatory skończonego rzędu i przy skończonym `dim V` jest surjektywne. W formule `(V⊗W)*≅Hom(V,W*)` nie wymaga się skończonego wymiaru; w formule `V*⊗W*≅(V⊗W)*` użyto wystarczającego założenia skończonego wymiaru.
- **Sumy proste i ilorazy:** po wyborze dopełnienia algebraicznego włożenie `U⊗W→V⊗W` jest iniektywne, `q⊗id` jest surjektywne, a jego jądro zgadza się z obrazem włożenia; ostateczny izomorfizm nie zależy od dopełnienia.
- **Ślad i kontrakcja:** `c_V(v⊗φ)=φ(v)` jest dobrze określone i nie wymaga iloczynu skalarnego; `c_V(Θ^{-1}(T))=tr T` wynika z dualności baz. Notacja `([T]_B)_{ii}` jest jednoznaczna także w przypadku wymiaru zero.
- **Porównanie z geometrią różniczkową:** podstawowe konstrukcje oraz dowody są spójne z rozdziałem 03 tamtego skryptu. Rozdział 09 algebry liniowej zachowuje pełną ogólność nad dowolnym ciałem; nie przenosi bezwarunkowego dzielenia przez `k!`, które może być niedozwolone w dodatniej charakterystyce.

## Kontrole obliczeniowe i repozytoryjne

- Niezależne sprawdzenie niezmienniczości śladu i formuły kontrakcji dla wszystkich macierzy `2×2` nad `F_2` i `F_3` oraz wszystkich odwracalnych zmian baz rozmiaru `2×2`: odpowiednio `16×6=96` i `81×48=3888`, razem **3984 konfiguracje**, bez rozbieżności.
- Wcześniejszy regresyjny test `tools/test_linear_algebra_tensors.py` obejmuje **4** konfiguracje wymiaru ilorazu wolnej przestrzeni, **6817** par iloczynów Kroneckera, **6817** testów ich składania oraz **97** sprawdzeń prostoty tensorów; wszystkie testy przeszły w przebiegu CI audytu V.
- Ponowna kontrola rozdziałów 01–09: **387 unikalnych etykiet**, **154 rozwiązywalne odsyłacze**, poprawne importy i zgodny katalog. Nie znaleziono błędów równoważenia środowisk LaTeX ani naruszeń ustalonej terminologii.
- Dla tekstu o blobie `0dc33d1aafb0d24e1346295bc2f6bf33e3455fea` GitHub Actions zakończył pomyślnie przebieg [44914384898](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44914384898) (kompilacja PDF **96 stron**, bez ostrzeżeń) i [44914384835](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44914384835) (testy aplikacji). Dla raportu V pomyślnie zakończono również przebieg [44914525348](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44914525348).
- Po zapisaniu niniejszego raportu dedykowany workflow powinien zweryfikować również commit raportowy; jego wyniku nie należy zakładać przed potwierdzeniem.

## Decyzja

**Audyt VI — czysty.** Nie wykryto nowych błędów, nieprecyzyjnych twierdzeń, nieuzasadnionych kroków dowodowych ani nowych usterek odsyłaczy. **Treść rozdziału 09 pozostawiono bez zmian.** Po audytach I–V oraz niezależnym, czystym audycie VI rozdział 09 uznaje się za **stabilny i zamknięty**. Zapisano jedynie ten raport; status książki „Rozdziały 01–09: stabilne po audytach” pozostaje aktualny.
