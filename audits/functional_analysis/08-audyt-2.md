# Analiza funkcjonalna — rozdział 08 — audyt 02 (niezależny przegląd)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/08-pary-dualne-i-topologie-slabe.tex`.  
**Blob SHA rozdziału 08:** `a01d4316fdeacef759c89955b14bc062abedbcd4`, bez zmiany względem audytu 08/01.  
**Werdykt matematyczno-redakcyjny:** **CZYSTY — pierwszy z dwóch wymaganych niezależnych przeglądów (1/2)**. Nie wprowadza się zmian w treści rozdziału. Do rozdziału 09 nie przechodzić bez drugiego czystego audytu tej samej wersji.

## Podstawa weryfikacji

Ponownie pobrano treść rozdziałów 01–08 z rzeczywistej gałęzi, sprawdzono `08-audyt-1.md`, testy `tools/tests/test_functional_analysis_ch08.py`, konfigurację `functional-analysis-ch08.yml` i zależności od rozdziału 06 (Hahn–Banach) oraz 03 (zupełność i sieci). Kontrola strukturalna była wykonywana niezależnie na pobranych tekstach, a nie przez kopiowanie liczb z poprzedniego raportu. Zależności `E^*`/ `E'`, kompleksowa liniowość, założenia Hausdorffa i lokalnej wypukłości oraz zakres stosowania twierdzeń o uzupełnieniu zostały sprawdzone osobno.

## Niezależna kontrola matematyczna — 12/12 dowodów PASS

1. **Baza słabych otoczeń:** topologia początkowa dla parowania jest generowana przez seminormy `p_f`; skończone przecięcia podpoziomic tworzą bazę, a niezdegenerowaność daje rozdzielanie punktów. Kryterium zbieżności wymaga sieci, nie jedynie ciągów.
2. **Słaba ograniczoność:** ciągłość każdego `x↦⟨x,f⟩` daje konieczność, zaś skończona liczba funkcjonałów definiujących otoczenie daje wspólne `t` w warunku `B⊂tU`. Bez potrzeby twierdzenia Banacha–Steinhausa.
3. **Sprzężenie topologii słabej:** ciągły `g` jest ograniczony na jednym bazowym otoczeniu; liniowość wymusza zerowanie na `ker T`, gdzie `T:E→K^m`; faktoryzacja i przedłużenie z `T(E)` do `K^m` dają `g∈F`. Niezdegenerowaność zapewnia iniektywność.
4. **Porównanie z topologią wyjściową:** każda funkcja w `E'` jest ciągła dla `τ`, więc `σ(E,E')⊂τ`; tożsamość przestrzeni sprzężonych wynika z punktu 3.
5. **Anihilator podprzestrzeni:** ciągłe funkcjonały zerujące się na `M` zerują się na obu domknięciach; oddzielenie punktu spoza `cl_τ(M)` przez funkcjonał z `E'` daje przeciwną inkluzję. Wymagane lokalna wypukłość i Hausdorff są jawne.
6. **Nienormowalność topologii słabej:** wspólne jądro skończonej rodziny funkcjonałów ma skończony kowymiar; dla nieskończenie wymiarowego `E` zawiera niezero `v`; cała prosta `Kv` jest słabo nieograniczona dzięki niezdegenerowanemu parowaniu. Nie istnieje ograniczone otoczenie zera.
7. **Domknięcie słabe sfery:** kula jest słabo domknięta przez oddzielenie normującym funkcjonałem Hahna–Banacha; dla punktu jej wnętrza skończenie wiele ograniczeń funkcjonałowych pozostawia niezerowy kierunek, po którym osiąga się normę jeden.
8. **Topologia słaba i słaba-* na `E'`:** włączenie `J(E)⊂E''` zapewnia inkluzję topologii; równość implikuje równość przestrzeni funkcjonałów ciągłych, a z punktu 3 wynika `J(E)=E''`.
9. **Uzupełnienie słabej przestrzeni:** `F^*` jako podprzestrzeń `K^F` jest przecięciem domkniętych zbiorów równości kodujących liniowość. Produkt jest zupełny, więc `F^*` jest zupełne i Hausdorffa. Dla skończenie wymiarowego `G⊂F` rzut `E→G^*` jest na: inaczej niezerowy `g∈G` znikałby na całym `E`. Skończona interpolacja daje gęstość zanurzenia.
10. **Niezupełność nieskończenie wymiarowego `E` z `σ(E,E')`:** przedłużenia współrzędnych skończenie wymiarowej podprzestrzeni przez Hahn–Banacha dowodzą `dim E'=∞`; na unormowanej przestrzeni `E'` istnieje nieciągły funkcjonał algebraiczny `Φ`, który nie jest `J(x)`. Ukierunkowana inkluzją sieć po skończenie wymiarowych `G⊂E'` interpoluje `Φ|_G`, jest słabo fundamentalna i nie ma granicy w `E`. Nie opiera się na wadliwym argumencie wyłącznie ciągowym.
11. **Topologia silna na `E'` przestrzeni unormowanej:** `p_B(f)≤(sup_B ||x||)||f||` dla każdego ograniczonego `B`, natomiast `p_{B_E}(f)=||f||`; seminormy definiują dokładnie topologię normy operatorowej.
12. **Seminormy Mackeya:** `p_K(x)` jest skończone przez zwartość `K` dla `σ(F,E)`; domknięte dyski `K_f={af:|a|≤1}` są absolutnie wypukłe, zwarte i odtwarzają `p_f`. Wnioski o lokalnej wypukłości, Hausdorffie i inkluzji `σ⊂τ` są poprawne. Charakterystyka Mackeya–Arensa występuje jedynie jako zapowiedź, nie jako nieudowodnione twierdzenie rozdziału.

**Kontrole graniczne:** przypadek przestrzeni zerowej nie narusza definicji pary ani twierdzeń bez hipotezy nieskończonego wymiaru; w części zespolonej parowanie ma jawnie charakter dwuliniowy, a funkcjonały są `K`-liniowe. Własność lokalnej wypukłości i Hausdorffa nie jest milcząco przypisywana dowolnej TVS.

## Przykłady — 5/5 PASS

1. Para `(E,E')` dla lokalnie wypukłej TVS Hausdorffa: niezdegenerowaność z Hahna–Banacha i definicji niezerowego funkcjonału.
2. Para `(c_0,ℓ¹)`: bezwzględna zbieżność przez oszacowanie `||x||∞ ||a||₁`, rozdzielanie współrzędnymi.
3. `e_n→0` słabo w `ℓ²`, mimo `||e_n||₂=1`: każda sekwencja współrzędnych reprezentująca funkcjonał należy do `ℓ²` i zmierza do zera.
4. `e_n→0` w `σ(ℓ¹,c₀)`, lecz nie w `σ(ℓ¹,ℓ∞)`: wektor stały `(1,1,…)` jest funkcjonałem świadczącym o braku słabej zbieżności.
5. `K^N` z topologią produktową jest `σ(K^N,c_{00})` dzięki rodzinie współrzędnych i skończonemu nośnikowi każdego elementu `c_{00}`.

## Kontrola struktury i zautomatyzowana walidacja

Niezależnie zliczono na pobranych plikach: **12** środowisk `proof`, **5** środowisk `przyklad`, **18** etykiet rozdziału 08, **9** odsyłaczy z rozdziału 08, **0** niezdefiniowanych celów wśród rozdziałów 01–08 i **0** duplikatów etykiet w tych rozdziałach. Zewnętrzne odsyłacze rozdziału 08 trafiają tylko do `sec:hahn-banach` (06) i `sec:zupelnosc` (03). Wersja źródła pozostała niezmieniona.

Wcześniej uruchomiony dedykowany [GitHub Actions #45197404525](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45197404525), na commicie `c6fdd743a91591ad1c62f3e16b2b5d44e34868d2` i tym samym blob SHA rozdziału 08, ma status **SUCCESS**: kroki 17 testów regresyjnych, przygotowania kontekstu 01–08, kompilacji LaTeX, kontroli PDF/odsyłaczy i publikacji artefaktu zakończyły się pomyślnie. Osobna kontrola wizualna PDF stron 43–48 została udokumentowana w audycie 08/01; **w bieżącej iteracji nie wykonywano ponownie niezależnego renderingu/oględzin PDF**. Testy dotyczą także skończenie wymiarowych modeli i nie stanowią formalnej weryfikacji twierdzeń nieskończenie wymiarowych.

## Spostrzeżenie dotyczące testów — nie wada treści matematycznej

Test `test_pointwise_cauchy_net_vs_sequence_distinction` zawiera tautologiczną asercję `values[j] == values[j]` i w praktyce przede wszystkim kontroluje obecność znacznika `\\mathcal G` w źródle. Nie należy interpretować go jako samodzielnego komputerowego dowodu istnienia sieci Cauchy'ego bez granicy. Poprawny dowód matematyczny w rozdziale sprawdzono bez polegania na tym teście. **Propozycja na przyszłość, bez zmiany rozdziału:** zastąpić tautologię rzeczywistym modelem skończonej interpolacji z kontrolą zgodności wartości na rosnących zbiorach ograniczeń.

## Decyzja

**Audyt 08/02 czysty; 1/2 audytów stabilizacyjnych.** Nie zmieniano tekstu rozdziału 08, nie poszerzano zakresu rozdziału. Kolejny krok: niezależny audyt **08/03** na tym samym blob SHA, ze szczególnym sprawdzeniem granicznych przypadków topologii Mackeya, słabej zwartości oraz argumentu o niezupełności. Dopiero po jego czystym wyniku — rozdział 09.
