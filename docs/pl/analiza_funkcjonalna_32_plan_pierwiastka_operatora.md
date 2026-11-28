# Analiza funkcjonalna — zatwierdzone uzupełnienie rozdziału 32

**Status: ZAPLANOWANE; do wdrożenia przy szczegółowym audycie rozdziału 32.**
Nie zmieniać rozdziału 32 przed dojściem do niego w ustalonej kolejności audytów.

Użytkownik zatwierdził dodanie osobnego twierdzenia o dodatnim pierwiastku operatora do pliku `chapters/pl/functional_analysis/32-teoria-spektralna-operatorow-ograniczonych.tex`, bezpośrednio **przed twierdzeniem o rozkładzie polarnym** (`thm:polar-decomp32`). Obecnie rozkład polarny posługuje się pierwiastkiem `(T^*T)^{1/2}`, ale nie wyodrębnia pełnego twierdzenia o istnieniu i jednoznaczności.

## Wymagany zakres

1. **Twierdzenie z kompletnymi założeniami:** dla zespolonej przestrzeni Hilberta H i każdego ograniczonego dodatniego operatora A (tj. A=A* oraz `<Ax,x> >= 0` dla każdego x) istnieje dokładnie jeden ograniczony dodatni operator B z B²=A. Definicja A^{1/2}=B.
2. **Dowód istnienia:** samosprzężoność i dodatniość dają `sigma(A) subset [0, infinity)`. Z istniejącego ciągłego rachunku funkcyjnego operatorów normalnych stosujemy funkcję f(t)=sqrt(t) na widmie. Wykazać dodatniość B=f(A) i tożsamość B²=A przy użyciu własności homomorfizmu.
3. **Dowód jednoznaczności:** gdy C>=0 i C²=A, to `sqrt(C²)=C` na mocy ciągłego rachunku funkcyjnego i tożsamości sqrt(t²)=t dla t>=0. Jawnie uzasadnić zgodność z pierwiastkiem skonstruowanym z widma A (albo argument komutowania C z A i rachunek operatorów samosprzężonych). Nie używać tezy dowodzonego twierdzenia jako przesłanki.
4. **Własności:** `||A^{1/2}||²=||A||`, `ker A^{1/2}=ker A`, `<Ax,x>=||A^{1/2}x||²`. Przeanalizować także przypadek A=0, projekcje ortogonalne i macierze diagonalne, w tym dodatni operator o niezerowym jądrze.
5. **Zastosowanie:** wskazać odsyłacz do nowego twierdzenia w dowodzie rozkładu polarnego oraz wyjaśnić konstrukcję `|T|=(T*T)^{1/2}`.
6. **Rozszerzenia tylko we właściwym miejscu:** w audycie rozdziału 33 rozważyć analogiczne twierdzenie o dodatnim pierwiastku nieograniczonego dodatniego operatora samosprzężonego, z poprawnym określeniem dziedziny przez rachunek spektralny. Nie mieszać go bez uzasadnienia z wersją ograniczoną.
7. **Kontrola jakości:** pełny dowód, przykłady i kontrprzykłady (niejednoznaczność pierwiastka bez warunku dodatniości), dokładne odsyłacze, dedykowane regresje, kompilacja LaTeX i rzeczywisty audyt wizualny PDF; stabilizacja 2/2, zanim przejdziemy dalej.

**Terminologia:** „pierwiastek operatora”, „operator dodatni”, „operator samosprzężony”, „przestrzeń sprzężona”, „ciąg”, „forma półtoraliniowa”. Zachować konwencję iloczynu skalarnego liniowego w pierwszym argumencie.

Ten plik jest wyłącznie planem. Nie deklaruje wdrożenia ani audytu rozdziału 32.
