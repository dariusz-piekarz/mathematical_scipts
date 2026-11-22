# Globalny audyt algebry liniowej — status rozdziałów

**Stan po iteracji 11 (LA-08 poprawiony i ustabilizowany, pełny audyt matematyczny trwa)**, 22 listopada 2026.  
**Aktualizacja:** rozdziały 01–05 zostały ponownie ustabilizowane. W rozdziale 05 poprawiono argument o braku podprzestrzeni dla zgodnego układu z niezerową prawą stroną, następnie wykonano dwa kolejne czyste audyty III–IV na identycznym SHA. Nowy PDF (7 stron) i CI dla poprawionego źródła [45006722306](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006722306) zweryfikowane — SUCCESS. CI uruchomione wyłącznie zapisem końcowego statusu wymaga osobnej kontroli.

| Rozdział | Status |
|---|---|
| 01 | STABILNY: trzy audyty rozdziału, dwa czyste, CI i osobny PDF PASS |
| 02 | STABILNY: audyty stabilizacyjne I–III, dwa kolejne czyste na niezmienionym źródle; 16/16 dowodów, 17/17 odsyłaczy, testy nad F_2 i F_3, 10-stronicowy PDF; CI PASS dla audytu I |
| 03 | STABILNY: audyty stabilizacyjne I–II czyste na identycznym SHA; 17/17 dowodów, 19/19 odsyłaczy, 8 przykładów, 10-stronicowy PDF i regresje 593 map/72 projekcji/8678 faktoryzacji/172544 tożsamości PASS |
| 04 | STABILNY: audyty stabilizacyjne I–III, II i III czyste na niezmienionym SHA; 15/15 dowodów, 24/24 odsyłacze, 10 przykładów, diagram i 12-stronicowy PDF zweryfikowane; dokładne testy F_2 i F_3 PASS |
| 05 | STABILNY: audyty stabilizacyjne I–IV, po precyzyjnej korekcie II dwie kolejne czyste iteracje III–IV na jednym SHA; 10/10 dowodów, 16/16 odsyłaczy, 4 przykłady, testy dokładne 1553 macierzy/12558 układów oraz 800 macierzy nad Q PASS; końcowy 7-stronicowy PDF i CI 45006722306 SUCCESS |
| 06 | Przegląd dowodów i obliczeń LA-06 w globalnej iteracji 11, bez nowych błędów; wspólne CI 45046473869 success; pełny PDF przed zmianą LA08 obejrzany w iteracji 10 |
| 07 | Przegląd bazy dualnej, anihilatorów i naturalności w globalnej iteracji 11, bez nowych błędów w sprawdzonych fragmentach; CI 45046473869 success |
| 08 | STABILNY po rzeczywistej korekcie parowania alternowania: audyt 04 korekcyjny, czyste 05–06 + dodatkowy sceptyczny 07; CI 45046473869 success; SHA `0cd0e91a194700b38862f2f1478a693dcd2e5dd3`; PDF str. 87 obejrzany |
| 09 | Wybrane dowody diagonalizacji, Sylvestera i char. 2 skontrolowane w iteracji 11 bez nowych błędów; CI 45046473869 success; pełna niezależna lektura wszystkich dowodów wciąż otwarta |
| 10 | Własność uniwersalna, iloraz i ranga tensorowa skontrolowane w iteracji 11 bez nowych błędów; CI 45046473869 success; pełna niezależna lektura wszystkich dowodów wciąż otwarta |
| 11 | Algebra zewnętrzna, przetasowania i Cauchy–Binet skontrolowane w iteracji 11 bez nowych błędów; CI 45046473869 success; pełna niezależna lektura wszystkich dowodów wciąż otwarta |
| 12 | STABILNY; iteracje 01 i 02 czyste, CI success; kontrole 2, SHA `ded0c69dc298d00842d4009073e2444e1037952a`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 13 | STABILNY; iteracje 02 i 03 czyste, CI success; kontrole 2, SHA `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 14 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success; kontrole 2, SHA `8216c60505324854e2339928bb9be562724e1db2`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 15 | STABILNY; audyty 02 i 03 czyste po poprawce, dedykowane CI success; kontrole 2, SHA `5a17f877bf3639cebc33ca95c202aca4498bd6c9`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 16 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success; kontrole 2, SHA `4f8da3c4b87b87ee8f8e6f7c7504637485c6e09a`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 17 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success; kontrole 2, SHA `05b93309d0e444f1c3fcbe3489cfd98a0f02846f`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 18 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success; kontrole 2, SHA `ef815633cf3a1f795d912c510fbc8575f21e464d`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 19 | STABILNY; audyty 03 i 04 czyste, CI success; kontrole 2, SHA `dd289d5c86452910a89d60ddfbcc558ef6d5be85`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 20 | STABILNY; audyty 01 i 02 czyste, CI success; kontrole 2, SHA `8d585c7f4c208990ad5f82222cc47f586144c138`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 21 | STABILNY; audyty 01 i 02 czyste, CI success; kontrole 2, SHA `6527ae1a6daca48717e6a5f5e83958271abb16f5`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 22 | STABILNY; audyty 03 i 04 czyste po poprawce, CI success; kontrole 2, SHA `dfa3d790bfed4c92c66642ea626a6213bc06ad3f`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 23 | STABILNY; audyty 01 i 02 czyste, CI success; kontrole 2, SHA `bbd199baed1ee2c1a88843aad9fbfd0eac665d22`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 24 | STABILNY; audyty 01 i 02 czyste, CI success; kontrole 2, SHA `92106feafce495e11f051279733cb34e9d9bed64`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 25 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success; kontrole 2, SHA `6b57fc1b64ef560b98e17f89322c688160376ccf`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 26 | STABILNY; audyty 02 i 03 czyste po poprawce, CI success; kontrole 2, SHA `80032eef1e0e5de817821d97de96aaf86c960e03`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 27 | STABILNY; audyty 01 i 02 czyste, dedykowane CI success; kontrole 2, SHA `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 28 | STABILNY po dodatkowym audycie; 04 korekta, 05–06 czyste, CI success; kontrole 2, SHA `b9507aa2db7eda554446248996e7c0ae241d4e73`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 29 | STABILNY; audyty 01 i 02 czyste oraz dodatkowy końcowy 03 czysty, CI success i PDF obejrzany; kontrole 3 (2+1), SHA `55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 30 | STABILNY; po korekcie czyste audyty 03–04 + sceptyczny 05, CI success i PDF obejrzany; kontrole 3 (2+1), SHA `6d90013dd6c66d347e5ae2ac78b4c1a194aa979e`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 31 | STABILNY; audyty 01–02 czyste + dodatkowy sceptyczny 03 czysty, CI success; kontrole 3 (2+1), SHA `6c1d09b9eaf4083c9ebaa361dbf46fc350eae147`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |
| 32 | STABILNY; zatwierdzony dodatek Penrose’a, audyt 01 korekcyjny, czyste 02–03 + końcowy 04, CI success; kontrole 3 (2+1), SHA `8aea8bd8db02ca8677fb0547f770c9166fdaef88`; szczegółowe raporty w sekwencji `re_audit_from_ch12` |

Iteracje 01–08 mają raporty; iteracja 09 wykonała kontrolę struktury 32 plików, próbkę 8 rozdziałów oraz weryfikację CI dla iteracji 08. Historyczna obserwacja po iteracji 09: audyt matematyczny i wizualny PDF nie były wtedy zamknięte; audyt PDF przeprowadzono później w iteracji 10.


## Wynik iteracji 09
Raport: `iteration_09.md`. Zgodność 32 plików i 32 instrukcji `\\input` potwierdzona; źródła 8 rozdziałów próbkowane; CI dla commitu iteracji 08 SUCCESS. Pełny przegląd wszystkich odsyłaczy, dowodów i renderowanych rysunków nie został wykonany. Żaden rozdział nie uzyskał nowego statusu „ostatecznie czysty” wyłącznie na tej podstawie.

## Aktualizacja globalna — iteracja 10 (22 listopada 2026)

**[Raport iteracji 10](iteration_10.md)** oraz dwa [inwentarze LA01–16](iteration_10_inventory_01_16.json) i [LA17–32](iteration_10_inventory_17_32.json) dokumentują pełny, a nie próbkowany, odczyt 32 aktualnych plików rozdziałów. **Wynik integralności strukturalnej: czysty.**

- Źródła łącznie **37 466 wierszy**, **1083** unikalne etykiety, **659** rozpoznanych odsyłaczy; **0** duplikatów, **0** niezdefiniowanych celów, **0** źle domkniętych/zagnieżdżonych środowisk; **382** środowiska `proof`, **21** rysunków `figure`. Wszystkie **32** instrukcje `\\input` w głównym pliku książki mają oczekiwaną kolejność.
- Jedyny odsyłacz do późniejszego rozdziału: LA-08 → LA-10, zapowiedź bez wcześniejszego użycia wyniku. Wybrane nakładki: 09/12 Grama–Schmidta (realny/zespolony), 22/23 Lapunow (ciągły/dyskretny), 24/26 Riccati (podstawowy/uogólniony), 25/27 gramiany sterowalności/obserwowalności — **bez mechanicznego scalania**.
- Ponowne regresje niezależnych skryptów dla LA30–32: **8961/8961 PASS**. Potwierdzony [CI 45041600675](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041600675) **completed/success**; budowa całego PDF i kroki walidacji odsyłaczy/ostrzeżeń LaTeX przeszły. W przebiegu znajdują się artefakty `linear-algebra-ch01-ch32` (ID 14761539115) oraz `linear-algebra-current-chapter` (ID 14761763450); istnieją i nie były przeterminowane podczas odczytu.
- Po poprzednich raportach ukończono również **oddzielną sekwencję stabilizacyjną LA12–32**: [raport końcowy](../re_audit_from_ch12_final_2026-11-22.md), w tym zatwierdzony dodatek Penrose’a do LA32. **Nie wznawiać od rozdziału 12** tylko z powodu kolejnej iteracji globalnej.
- **Pełna kontrola techniczna i wizualna PDF została wykonana**: pobrano rzeczywisty artefakt CI `linear-algebra-ch01-ch32` (ID **14761539115**) z [run 45041600675](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041600675). Plik `linear_algebra.pdf` ma **318 stron A4**, 32 zakładki rozdziałów, **0 stron pustych**, **0 spośród 7836 bloków tekstowych poza granicami strony**, log bez ostrzeżeń `Overfull/Underfull/Missing character/LaTeX Warning`. Wizualnie obejrzano **14 arkuszy miniatur wszystkich 318 stron**, zestawienia wszystkich **21 rysunków** oraz osobne powiększenia stron z `Spin(2)`, sferą Blocha, fibracją twistorową i **nowym konturem Penrose’a na stronie 315**. Nie wykryto widocznych kolizji etykiet, obcięć ani pustych stron. **Nie każdą stronę oglądano w maksymalnym powiększeniu**; ten wynik nie jest pełną niezależną weryfikacją matematyczną.
- **Globalny audyt książki pozostaje otwarty w zakresie wszystkich 382 dowodów matematycznych**: w przeciwieństwie do integralności źródeł i PDF nie wykonano jeszcze nowej, niezależnej lektury każdego dowodu całej książki. Krok `Report pre-existing global library validation issues` ma `continue-on-error: true`; zielone CI nie poświadcza automatycznie bezbłędności pozostałych części Biblioteki. Historyczny status iteracji 09 opisuje stan ówczesny, a wynik bieżący dokumentuje uzupełnienie.
- **Następne zadanie globalne**: rozpocząć pogłębioną niezależną kontrolę matematyczną nieobjętych pełnym ponownym przebiegiem rozdziałów 06–11, następnie krytyczne powiązania spektralne 14–20 i sterowania 22–28; nie resetować zamkniętej kolejki stabilizacji LA12–32 bez konkretnej nowej usterki.

## Iteracja 11 — 2026-11-22: błąd dowodowy LA-08 poprawiony i ponownie ustabilizowany

**[Raport globalny 11](iteration_11.md)**: krytyczny przegląd kluczowych dowodów i ich zależności w LA06–11 ujawnił w `thm:lin8-operatory-wlasnosci` błędną konstrukcję parowania permutacji `σ↦σ∘(p q)`. Była to rzeczywista luka: dwie wybrane permutacje mogły dawać nierówne wartości `F`, choć `v_p=v_q`. Poprawiono na **`σ↦(p q)∘σ`**, dla którego `v_{((p q)∘σ)(j)}=v_{σ(j)}` przy każdym `j`. Własność `AF` bycia formą naprzemienną pozostaje prawdziwa w dowolnej charakterystyce.

- [Korekta źródła, commit 06c2e0b5](https://github.com/dariusz-piekarz/mathematical_scipts/commit/06c2e0b5eb6dd3c50d15989fcbbbcd141782d55f). Blob LA-08 po poprawce `0cd0e91a194700b38862f2f1478a693dcd2e5dd3`.
- [Audyt LA08-04](../ch08_iteration_04_2026-11-22.md) **nieczysty** — korekta; [audyt 05](../ch08_iteration_05_2026-11-22.md) **czysty 1/2**; [audyt 06](../ch08_iteration_06_2026-11-22.md) **czysty 2/2**; [audyt 07](../ch08_iteration_07_2026-11-22.md) **czysty dodatkowy sceptyczny**. **LA08 ponownie STABILNY** na tym samym blobie.
- [GitHub Actions 45046473869](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45046473869) completed/success na poprawce; pobrany nowy pełny PDF ma **319 stron** i zweryfikowany wizualnie poprawiony dowód na **stronie 87**. Wcześniejsze pełne montażowe oględziny PDF ze starej wersji miały 318 stron; **nie twierdzimy, że powtórzono inspekcję wszystkich 319 stron na nowym PDF**.
- Testy: **118 695** niezależnych sprawdzeń parowań i form w audycie korekcyjnym; **15 209** nowych kontroli niezależnego algorytmu w czystym audycie 05; **1 130 221** kontroli sceptycznych w audycie 06; **18 304** dodatkowych kontroli LA06–11. Powtarzane testy z audytu 07 nie są doliczane jako nowe unikalne przypadki. Duże liczby to powtarzalne sprawdzenia obliczeniowe, nie liczba niezależnych twierdzeń.
- **Pozostałe LA06, LA07, LA09–11**: bez nowej usterki wymagającej zmiany w szczegółowo skontrolowanych argumentach, szczególnie determinanty w char. 2, baza dualna, prawo bezwładności, własność uniwersalna iloczynu tensorowego, algebra zewnętrzna oraz Cauchy–Binet. Nie oznacza to, że wszystkie 98 środowisk `proof` z LA06–11 przeczytano ponownie w pełnym zakresie.
- **Globalny audyt matematyczny całej książki wciąż OTWARTY**; kontrola struktury/odsyłaczy z iteracji 10 pozostaje aktualna (jedyna zmiana źródła to LA-08, bez zmiany etykiet), a ukończone osobne audyty LA12–32 nie są resetowane.

**Kolejne działanie:** kontynuować niezależną lekturę pozostałych dowodów LA07 i LA09–11, następnie zależności spektralne LA14–20 i sterowanie LA22–28; konkretną nową usterkę poprawiać w odpowiednim rozdziale i stabilizować go ponownie.
