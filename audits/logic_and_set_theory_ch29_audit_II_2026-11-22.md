# Logika matematyczna i teoria mnogości — rozdział 29, audyt II

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/29-slabsze-zasady-wyboru-i-ich-ograniczenia.tex`.

## Kontrola formalnej poprawności ZF i uzupełnienia

1. **Przeliczalna suma przeliczalnych:** wyjaśniono, dlaczego dla każdego indeksu `n` istnieje zbiór `E_n` wszystkich iniekcji `A_n→ω` (separacja w `P(A_n×ω)`), nawet gdy `A_n=∅`, i jak zastępowanie zapewnia istnienie indeksowanej rodziny `(E_n)`. Dopiero na tej rodzinie stosuje się ACω do jednoczesnego wyboru iniekcji.
2. **Kryterium ultrafiltru:** zapisano jawnie rodzinę `V={c:∃u∈U, u∧b≤c}` generowaną przez `U∪{b}`. Osobno sprawdzono domknięcie ku górze, domknięcie na iloczyn i brak elementu `0_B`, zanim użyto maksymalności filtru `U`.
3. **UF ⇒ zwartość `2^I`:** uzasadniono istnienie właściwego filtru generowanego przez rodzinę domkniętą z własnością przecięcia skończonego. Kostka `2^I` ma zawsze punkt stały zero, także przy `I=∅`, co nie wymaga wyboru.
4. **Pełne twierdzenie Tychonoffa:** poprawiono zdanie `każdy filtr można przedłużyć do ultrafiltru` na poprawne `każdy właściwy filtr`. Dodano jawnie przypadek pustego produktu, który jest zwarty bez dalszych argumentów.

Sprawdzono niezależnie poprawność schematu `AC ⇒ DC ⇒ ACω`; dowód odwracalności reprezentacji BPI i UF nie korzysta z AC; w kierunku BPI ⇒ Tychonoff dla compact Hausdorffa wykorzystuje się jedyność granic ultrafiltrów, a przy przestrzeniach nie-Hausdorffa konieczny jest pełny wybór. Potwierdzono także równoważność pełnego Tychonoffa z AC i Tukeya z AC. Zgodności są udokumentowane m.in. w podręczniku Monk, *Introduction to Set Theory* i źródłach o równoważnikach aksjomatu wyboru.

**Inwentarz bez zmian:** 6 definicji, 7 twierdzeń, 1 lemat, 5 przykładów, 7 uwag, 8 dowodów; 24 etykiety, 10 odsyłaczy. Rozszerzono testy regresyjne o modele skończonych algebr Boole'a, skończone grafy funkcji częściowych, przypadki produktu niehausdorffowskiego i konieczność domkniętych kul w dowodzie Baire'a.

**Werdykt:** poprawiono luki formalne, nie dodając nowych wyników. Do powtórnego audytu i pełnego CI.
