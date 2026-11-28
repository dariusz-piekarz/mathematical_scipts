# Globalny audyt algebry liniowej — iteracja 06/09

**Data:** 22 listopada 2026, 06:00 CET.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Wejściowy HEAD:** `576823a8c5888863078fc816892209f33095e537`.  
**Zakres:** rozdziały 21–24.

## Materiał źródłowy
Odczytano bieżące `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raporty iteracji 04 i 05, tabelę statusów oraz pełne pliki rozdziałów 21–24. Katalog zawiera 32 rozdziały, a plik główny 32 instrukcje `\\input`. Sprawdzono strukturę **34 środowisk proof** (9+10+7+8). Pełne formalne sprawdzenie wszystkich zdań nie jest deklarowane.

## Kontrola matematyczna
- **21:** dowód identyfikacji komutanta z `End_{K[t]}(V_T)`; dla modułów cyklicznych sprawdzono warunek `g | fy`, skrócenie przez NWD i zastosowanie lematu Euklidesa; zliczanie par indeksów we wzorze `2(r-i)+1`; wzory z filtracji jąder i przykład dwóch bloków `J_2(0)\oplus J_1(0)` dający wymiar komutanta 5. Bez koniecznych zmian.
- **22:** kryterium Sylvestera, wzór teleskopowy `A^kX-XB^k`, zastosowanie Cayleya–Hamiltona do jawnego rozwiązania, nilpotentność operatora `L-R` dla dwóch bloków Jordana. W twierdzeniu Lapunowa sprawdzono oszacowanie wykładnicze, całkę i implikację z wektora własnego. Bez koniecznych zmian.
- **23:** dowód `\rho(A)<1\iff A^k\to0`, absolutna zbieżność szeregu rozwiązującego równanie Steina, wyznacznik operatora `X\mapsto A^*XA` przez triangularizację Schura, kryterium jawnej metody Eulera. **Korekta:** w twierdzeniu o dokładnym próbkowaniu wcześniej ustalano `h>0`, a potem w samej tezie mówiono „dla pewnego” i „dla każdego” `h>0`; teraz rodzina `A_h` jest jawnie zdefiniowana dla każdego `h>0`, bez niejednoznacznego związania zmiennej.
- **24:** sprawdzono uzupełnienie kwadratu, indukcję DARE, monotoniczność `P_N`, granicę rozwiązań i dyskretną tożsamość `D=A_1^*DA_2`; w części ciągłej wyprowadzenie równania Riccatiego, argument przedłużenia rozwiązania i dowód stabilności CARE. **Korekta:** dowód jednoznaczności sterowania optymalnego na skończonym horyzoncie nie powinien nazywać funkcji `u+R^{-1}B^*Sx` ciągłą globalnie, skoro `u` jest tylko przedziałami ciągłe. Dopisano dokładne uzasadnienie z nieujemności całki i ciągłości na każdym przedziale, z jednoznacznością prawie wszędzie.

## Kontrola redakcyjna i techniczna
Zachowano wszystkie etykiety, odsyłacze, istniejące twierdzenia i przykłady. Nie dodano nowego materiału. Sprawdzono terminologię i zakres założeń, w szczególności `n,m\ge1` w LQR i przypadek `n=0` w komutantach. Cztery rozdziały nie wymagają nowego rysunku na podstawie kontroli tekstowej. Nie wykonano niezależnego renderingu ani wizualnej inspekcji stron PDF; brak kolizji nie jest potwierdzony.

**Wynik:** dwie poprawki źródłowe. Audyt nie jest oznaczony jako ostatecznie czysty, ponieważ wymaga ponownego sprawdzenia po zmianach i potwierdzenia CI oraz PDF.

## Następny krok
Iteracja 07: rozdziały 25–28. Kontynuować kontrolę otwartych wyników CI/PDF dla wcześniejszych bloków.
