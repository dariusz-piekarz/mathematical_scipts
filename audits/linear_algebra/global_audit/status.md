# Globalny audyt algebry liniowej — status rozdziałów

**Stan po iteracji 07/09**, 22 listopada 2026.

| Rozdział | Status |
|---|---|
| 01 | 01: poprawiono dowód; PDF/CI oczekują |
| 02 | 01: poprawiono dowód; PDF/CI oczekują |
| 03 | 01: bez korekt; PDF/CI oczekują |
| 04 | 01: uzupełniono rachunki; PDF/CI oczekują |
| 05 | 02: sprawdzono dowody eliminacji, RREF, rzędu i przykłady; PDF/CI do potwierdzenia |
| 06 | 02: sprawdzono znak permutacji, wyznacznik, Laplace'a i Cramera; PDF/CI do potwierdzenia |
| 07 | 02: sprawdzono bazę dualną, anihilatory, zmianę bazy, ślad; PDF/CI do potwierdzenia |
| 08 | 02: naprawiono parowanie permutacji w dowodzie alternowania i odsyłacz do rozdz. 10; PDF/CI do potwierdzenia |
| 09 | 03: 14 dowodów; formy kwadratowe, Sylvester, char. 2; PDF/CI otwarte |
| 10 | 03: 20 dowodów; własność uniwersalna, operatory skończonego rzędu; poprawiono terminologię; PDF/CI otwarte |
| 11 | 03: 19 dowodów; algebra zewnętrzna, minory, przetasowania; PDF/CI otwarte |
| 12 | 03: 13 dowodów; polaryzacja, Riesz, Gram--Schmidt; poprawiono 8 sformułowań; PDF/CI otwarte |
| 13 | 04: sprawdzono rzuty, operator sprzężony i najmniejsze kwadraty; źródło bez zmian; PDF/CI otwarte |
| 14 | 04: sprawdzono Schura, twierdzenie spektralne i jednoczesną triangularizację; doprecyzowano n=0; PDF/CI otwarte |
| 15 | 04: sprawdzono LU/PLU, Eckarta--Younga i rozkład biegunowy; zdefiniowano zerowe wartości osobliwe i uzupełniono dwa kroki dowodów; PDF/CI otwarte |
| 16 | 04: sprawdzono Cayleya--Hamiltona, rozkład pierwotny i wielomian minimalny; źródło bez zmian; PDF/CI otwarte |
| 17 | 05: 7 dowodów; łańcuchy Jordana, stabilizacja jąder, jednoznaczność bloków; PDF/CI otwarte |
| 18 | 05: 6 dowodów; rzuty CRT, rozkład Jordana--Chevalleya, funkcje holomorficzne i wykładnicza; PDF/CI otwarte |
| 19 | 05: 7 dowodów; uściślono krok algorytmu Smitha i uzasadnienie spadku stopnia; PDF/CI otwarte |
| 20 | 05: 7 dowodów; CRT, bloki pierwotne, wymiary jąder i przypadki nad ciałem skończonym; PDF/CI otwarte |
| 21 | 06: sprawdzono wzory na komutant, Hom modułów cyklicznych i przykłady; bez korekt źródła; PDF/CI otwarte |
| 22 | 06: sprawdzono kryterium Sylvestera, wzór wielomianowy, twierdzenie Lapunowa i przykłady; bez korekt źródła; PDF/CI otwarte |
| 23 | 06: sprawdzono stabilność Schura, operator Steina, próbkowanie; poprawiono kwantyfikację h; PDF/CI otwarte |
| 24 | 06: sprawdzono rekurencję DARE, tożsamości CARE i DRE; poprawiono argument ciągłości dla sterowań przedziałami ciągłych; PDF/CI otwarte |
| 25 | 07: skontrolowano kryteria Kalmana/PBH, gramiany, stabilizowalność i argument rozmieszczania biegunów; testy CI PASS, wizualny PDF otwarty |
| 26 | 07: sprawdzono założenia i kluczowe tożsamości DARE/CARE, granice i przypadek Q≥0; testy CI PASS, wizualny PDF otwarty |
| 27 | 07: sprawdzono faktoryzację Hankela, minimalność, podobieństwo i równoważenie gramianów; testy CI PASS, wizualny PDF otwarty |
| 28 | 07: sprawdzono transformaty, realizację towarzyszącą i oszacowania BIBO; testy CI PASS, wizualny PDF otwarty |
| 29 | oczekuje na globalny audyt |
| 30 | oczekuje na globalny audyt |
| 31 | oczekuje na globalny audyt |
| 32 | oczekuje na globalny audyt |

Iteracje 01–07 wykonane; iteracje 08–09 oczekują. Iteracja 07: audyt kluczowych argumentów i przegląd struktury 46 dowodów w rozdziałach 25–28; bez zmian merytorycznych. Workflow 44987751791 dla wejściowego HEAD fd4e4a7 zakończył się SUCCESS, w tym testy LA25–LA28 i pełny PDF. Wizualna kontrola stron PDF pozostaje niepotwierdzona; nie deklarować pełnej czystości. Wcześniejsze otwarte kontrole wizualne pozostają. Nie utożsamiać audytu źródła z pomyślną kompilacją ani audytem wizualnym.
