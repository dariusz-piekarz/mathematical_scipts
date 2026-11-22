# Globalny audyt algebry liniowej — status rozdziałów

**Stan po iteracji 10 (pełny audyt odsyłaczy, globalny PDF wciąż otwarty)**, 22 listopada 2026.  
**Aktualizacja:** rozdziały 01–05 zostały ponownie ustabilizowane. W rozdziale 05 poprawiono argument o braku podprzestrzeni dla zgodnego układu z niezerową prawą stroną, następnie wykonano dwa kolejne czyste audyty III–IV na identycznym SHA. Nowy PDF (7 stron) i CI dla poprawionego źródła [45006722306](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006722306) zweryfikowane — SUCCESS. CI uruchomione wyłącznie zapisem końcowego statusu wymaga osobnej kontroli.

| Rozdział | Status |
|---|---|
| 01 | STABILNY: trzy audyty rozdziału, dwa czyste, CI i osobny PDF PASS |
| 02 | STABILNY: audyty stabilizacyjne I–III, dwa kolejne czyste na niezmienionym źródle; 16/16 dowodów, 17/17 odsyłaczy, testy nad F_2 i F_3, 10-stronicowy PDF; CI PASS dla audytu I |
| 03 | STABILNY: audyty stabilizacyjne I–II czyste na identycznym SHA; 17/17 dowodów, 19/19 odsyłaczy, 8 przykładów, 10-stronicowy PDF i regresje 593 map/72 projekcji/8678 faktoryzacji/172544 tożsamości PASS |
| 04 | STABILNY: audyty stabilizacyjne I–III, II i III czyste na niezmienionym SHA; 15/15 dowodów, 24/24 odsyłacze, 10 przykładów, diagram i 12-stronicowy PDF zweryfikowane; dokładne testy F_2 i F_3 PASS |
| 05 | STABILNY: audyty stabilizacyjne I–IV, po precyzyjnej korekcie II dwie kolejne czyste iteracje III–IV na jednym SHA; 10/10 dowodów, 16/16 odsyłaczy, 4 przykłady, testy dokładne 1553 macierzy/12558 układów oraz 800 macierzy nad Q PASS; końcowy 7-stronicowy PDF i CI 45006722306 SUCCESS |
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
| 29 | 08: uzupełniono brakujący dowód własności Hausdorffa w osadzeniu Plückera; CI i wizualny PDF do kontroli |
| 30 | 08: zweryfikowano własność uniwersalną, bazę 2^n i reprezentację na algebrze zewnętrznej; CI i wizualny PDF do kontroli |
| 31 | 08: zweryfikowano nakrycia Pin/Spin, chiralość, warunki przejścia i klasę w2; CI i wizualny PDF do kontroli |
| 32 | 08: dopisano rachunek w mapie przy nieskończoności i sprawdzono incydencję oraz Plückera; CI i wizualny PDF do kontroli |

Iteracje 01–08 mają raporty; iteracja 09 wykonała kontrolę struktury 32 plików, próbkę 8 rozdziałów oraz weryfikację CI dla iteracji 08. Globalny audyt matematyczny i wizualny PDF nadal NIE są zamknięte.


## Wynik iteracji 09
Raport: `iteration_09.md`. Zgodność 32 plików i 32 instrukcji `\\input` potwierdzona; źródła 8 rozdziałów próbkowane; CI dla commitu iteracji 08 SUCCESS. Pełny przegląd wszystkich odsyłaczy, dowodów i renderowanych rysunków nie został wykonany. Żaden rozdział nie uzyskał nowego statusu „ostatecznie czysty” wyłącznie na tej podstawie.

## Aktualizacja globalna — iteracja 10 (22 listopada 2026)

**[Raport iteracji 10](iteration_10.md)** oraz dwa [inwentarze LA01–16](iteration_10_inventory_01_16.json) i [LA17–32](iteration_10_inventory_17_32.json) dokumentują pełny, a nie próbkowany, odczyt 32 aktualnych plików rozdziałów. **Wynik integralności strukturalnej: czysty.**

- Źródła łącznie **37 466 wierszy**, **1083** unikalne etykiety, **659** rozpoznanych odsyłaczy; **0** duplikatów, **0** niezdefiniowanych celów, **0** źle domkniętych/zagnieżdżonych środowisk; **382** środowiska `proof`, **21** rysunków `figure`. Wszystkie **32** instrukcje `\\input` w głównym pliku książki mają oczekiwaną kolejność.
- Jedyny odsyłacz do późniejszego rozdziału: LA-08 → LA-10, zapowiedź bez wcześniejszego użycia wyniku. Wybrane nakładki: 09/12 Grama–Schmidta (realny/zespolony), 22/23 Lapunow (ciągły/dyskretny), 24/26 Riccati (podstawowy/uogólniony), 25/27 gramiany sterowalności/obserwowalności — **bez mechanicznego scalania**.
- Ponowne regresje niezależnych skryptów dla LA30–32: **8961/8961 PASS**. Potwierdzony [CI 45041600675](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041600675) **completed/success**; budowa całego PDF i kroki walidacji odsyłaczy/ostrzeżeń LaTeX przeszły. W przebiegu znajdują się artefakty `linear-algebra-ch01-ch32` (ID 14761539115) oraz `linear-algebra-current-chapter` (ID 14761763450); istnieją i nie były przeterminowane podczas odczytu.
- Po poprzednich raportach ukończono również **oddzielną sekwencję stabilizacyjną LA12–32**: [raport końcowy](../re_audit_from_ch12_final_2026-11-22.md), w tym zatwierdzony dodatek Penrose’a do LA32. **Nie wznawiać od rozdziału 12** tylko z powodu kolejnej iteracji globalnej.
- **Globalny audyt książki nadal OTWARTY:** brak osobnej wizualnej kontroli całego PDF po dodatku Penrose’a, a samo przejście CI nie jest niezależną lekturą wszystkich 382 dowodów. Krok `Report pre-existing global library validation issues` ma w workflow `continue-on-error: true`, więc zielony wynik tego workflow nie dowodzi automatycznie bezbłędności pozostałych części Biblioteki. Wcześniejszy status iteracji 09 pozostaje historycznie prawdziwy dla zakresu wykonanych wtedy czynności.
- Następne zadanie globalne: pobrać z CI artefakt pełnego PDF i wyrenderować/obejrzeć wszystkie strony, ze szczególną uwagą na 21 ilustracji oraz poprawiony fragment LA32; następnie pogłębić przegląd dowodów i zaktualizować tabelę bez przypisywania wykonania nieprzeprowadzonym kontrolom.
