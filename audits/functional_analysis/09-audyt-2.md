# Analiza funkcjonalna — rozdział 09 — audyt 02 (niezależny przegląd oraz przypadki brzegowe)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/09-banach-alaoglu-krein-milman-i-topologia-mackeya.tex`.  
**Blob źródła wejściowego:** `b633df1875b710c361912a39bee277b11eca26e5`.  
**Blob źródła po korektach:** `d0a20b01bdabfa4e85d9c00ebe11c8c41bea650a`.  
**Werdykt:** **AUDYT Z POPRAWKAMI, NIE CZYSTY — stabilizacja 0/2.** Kolejny krok: niezależny audyt 09/03 tej poprawionej wersji; nie otwierać rozdziału 10 przed dwoma kolejnymi czystymi przeglądami.

## Metoda kontroli

Ponownie skontrolowano rozdział 09, pierwotny raport `09-audyt-1.md`, stabilną podstawę rozdziałów 01–08, ograniczenia terminologiczne i wcześniej dodane testy regresyjne. Analiza obejmuje **14 dowodów i 8 przykładów**: w szczególności sprawdzono przypadki zerowymiarowe, puste rodziny warunków, obie wersje nad `R` i `C`, założenia topologiczne, status własności sieci i użycie zwartości wobec dowolnie wielu ograniczeń.

## Matematyka: kontrola 14 dowodów

1. **Równociągłość a polary.** Skalowanie otoczenia i pochłanianie przez otoczenia zera dają równoważność równociągłości z zawarciem w polarnym zbiorze oraz punktową ograniczoność. Działa też dla `H=∅`.
2. **Banach–Alaoglu–Bourbaki.** Dla dowolnej TVS `U` jest pochłaniające, więc każda współrzędna `f(x)` ma jednolite ograniczenie na `U°`. Warunki liniowości i polarności są domknięte w produkcie skalarnych dysków, a wynik należy do `E'` przez ograniczenie w otoczeniu zera. Nie potrzeba Hausdorffa ani lokalnej wypukłości.
3. **Kula normowego sprzężenia.** Przy `R>0` polar otwartej kuli promienia `1/R` to `B_R'`. Dla `R=0` kula sprzężona jest singletonem, więc zwarta.
4. **Domknięty podzbiór kuli.** Zwartość dziedziczy się po domknięciu w zwartych przestrzeniach, w tym dla zbioru pustego.
5. **Metryka wartościowań na równociągłej rodzinie.** Zbiór gęsty `D` jest rozdzielający przez ciągłość funkcjonałów; równociągłość `H` gwarantuje jednostajną kontrolę `f(x-x_n)`, stąd zbieżność na `D` jest dokładnie zbieżnością słabą-* na `H`.
6. **Ośrodkowość równoważna metryzowalności słabo-* kuli.** Pierwszy kierunek wykorzystuje równociągłość kuli; dla odwrotnego z przeliczalnej bazy otoczeń zera i Hahna–Banacha wynika gęstość rozpiętości przeliczalnego układu wektorów.
7. **Ściana poziomicy maksymalnej.** Zwartość i ciągłość dają maksimum; liniowość i średnie wypukłe gwarantują własność ściany, również jej przechodniość.
8. **Istnienie punktu ekstremalnego.** Dla zagnieżdżonych niepustych domkniętych ścian zwartość daje niepuste przecięcie. Minimalną ścianę z Zorna oddzielenie dwóch różnych punktów czyni singletonem.
9. **Krein–Milman.** Odseparowanie punktu od domkniętej otoczki wypukłej punktów ekstremalnych daje ścianę maksimum z ekstremalnym punktem naruszającym nierówność. Rozróżniono rzeczywiste funkcjonały i części rzeczywiste funkcjonałów zespolonych.
10. **Zasada maksimum Bauera.** Zbiór maksimów górnie półciągłej wypukłej funkcji jest niepusty, domknięty i ekstremalny, niekoniecznie wypukły. Argument minimalnego ekstremalnego zbioru jest poprawny.
11. **Zwartość i dominacja funkcjonału.** Skończone projekcje zwartych absolutnie wypukłych `K` są zwarte. Oddzielenie i zrównoważenie `K` dają sprzeczność z `|g(x)|≤p_K(x)`; przecięcie `K_S` jest niepuste przez zwartość.
12. **Mackey–Arens.** Funkcjonał ciągły dla `τ(E,F)` jest dominowany `p_{CK}` dla absolutnie wypukłego zwartego `CK`, więc należy do `F`. Dla zgodnej `ρ` dowolna ciągła seminorma jest supremum po `K_p` dzięki Hahn–Banachowi i polarnemu twierdzeniu zwartości, stąd `ρ⊂τ(E,F)`.
13. **Najsłabsza i najsilniejsza zgodna topologia.** Poprzednie twierdzenie daje górną granicę `τ`; minimalność topologii początkowej daje `σ`.
14. **Interpolacja dla dowolnie wielu warunków.** Warunek na wszystkie skończone kombinacje zapewnia jednoznaczność `g_J` i `||g_J||≤R`, także przy powtarzających się indeksach. Hahn–Banach i własność skończonych przecięć w `B_R'` kończą dowód.

**Wynik:** brak nowych błędów w tych dowodach. Testy numeryczne i finite-dimensional models są wyłącznie regresjami, nie formalnym poświadczeniem twierdzeń.

## Przykłady i korekty z audytu 09/02

1. **Kula `ℓ¹` jako słabo-* zwarta.** Norma odróżnia od zwartości normowej: `||e_n-e_m||_1=2`. PASS.
2. **Nieprzeliczalny produkt dysków.** Sieć `χ_F` po skończonych `F⊂I` dąży do `χ_I`, lecz żaden ciąg z tej rodziny nie ma tej granicy. **Korekta redakcyjna:** ostatnie pozostawione `\\mathbf 1_I` zastąpiono `\\chi_I` w commicie `3c033df47fc69e15196179febf8e3c96c2bb1c6a`; dotychczasowe `χ_F` i `χ_I` w poprzednich zdaniach pozostają niezmienione.
3. **Słabo-* zwarty lecz nierównociągły zbiór `{0}∪{nx_n^*}` na niezupełnym `c_{00}`.** Punktowo zbieżny do zera ciąg funkcjonałów o normach `n`. PASS.
4. **Punkty ekstremalne wielokąta i kuli Hilberta.** Przy hipotezie wypukłego wielokąta argument jest prawidłowy. **Nowa konieczna korekta matematyczna:** zdanie „Jeżeli `H` jest rzeczywistą przestrzenią Hilberta, to `Ext(B_H)=S_H`” jest **fałszywe dla `H={0}`**, ponieważ `Ext({0})={0}`, lecz sfera jednostkowa jest pusta. Dopisano „niezerową rzeczywistą przestrzenią Hilberta” w commicie `d5341dcafaa1f1c59a61815d43c703be3b70b4ae`. Sam dowód również potrzebuje `h≠0` w `H`, więc założenie jest nieusuwalne.
5. **Produkt przedziałów `[-1,1]^I`.** Punkt jest ekstremalny wtedy i tylko wtedy, gdy każda współrzędna jest `±1`; dla pustego `I` rozdział jawnie zakłada `I≠∅`. PASS.
6. **Słabo-* zwarta rzeczywista kula `ℓ¹`.** Ekstremalne punkty to dokładnie `±e_n`; możliwość przekazania masy między współrzędnymi pokazuje, że inne punkty sfery nie są ekstremalne. PASS.
7. **Rozróżnienie `σ(E,E')` i `τ(E,E')`.** Na nieskończenie wymiarowej przestrzeni Banacha topologia normowa jest zgodna, a słaba nie jest normowalna. PASS.
8. **Wartości na bazie współrzędnych `ℓ¹`.** Test z powtarzającymi się indeksami redukuje się do zgrupowanych współczynników; `b∈ℓ∞` z `||b||∞≤R` daje przedłużenie. PASS.

**Dodatkowo doprecyzowano wstęp:** „W nieskończenie wymiarowej przestrzeni unormowanej...” zamiast niejawnego używania kuli jednostkowej w dowolnej przestrzeni liniowej.

## Kontrola techniczna i testy

- Na niezmienionej strukturze rozdziału: **14 par `proof`**, **8 par `przyklad`**, **23 etykiety** i **14 odsyłaczy**. Cele są obecne w kontekście 01–09, bez duplikatów. Korekty nie zmieniły etykiet ani odsyłaczy.
- Powtórny audyt pliku źródła pod kątem nadużywania terminów „dual”, „sekwencyjny” oraz oznaczeń wskaźnikowych `\\mathbf 1` wykrył i usunął ostatnie wystąpienie tego ostatniego w rozdziale 09.
- W `tools/tests/test_functional_analysis_ch09.py` uzupełniono kontrakt notacji `χ_I` i dodano test **przypadku zerowej przestrzeni Hilberta**. Łącznie obecnie **19 testów**. Nowe testy nie stanowią dowodu w ogólnej klasie przestrzeni Hilberta, lecz chronią tekst przed regresją wyeliminowanej hipotezy.
- Dotychczasowe CI [#45208704564](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208704564) miało status SUCCESS dla poprzedniego SHA; nie certyfikuje automatycznie nowego pliku i nowego testu. **Po zmianach należy sprawdzić osobny CI** dla commita `54c211369e4b9ce59d62066cef184df747d53aa8`.
- Niezależnie powtórzono wizualną analizę PDF poprzedniej, poprawnie skompilowanej wersji: strony **48–55** w 55-stronicowym PDF, 0 bloków wychodzących poza granice strony, brak widocznej kolizji rysunku TikZ na stronie 51. Po zmianie źródła PDF wymaga powtórnej walidacji aktualnego CI.

## Werdykt i następny krok

**Audyt 09/02 jest NIE CZYSTY, 0/2**, pomimo prawidłowych dowodów głównych. Wprowadzono jedną konieczną hipotezę matematyczną, jedną korektę notacji i uściślenie wstępu. Nie przechodzić do rozdziału 10. Najpierw potwierdzić zielony CI aktualnego commita, potem wykonać niezależny audyt 09/03 na niezmienionej wersji i dążyć do dwóch kolejnych czystych audytów.
