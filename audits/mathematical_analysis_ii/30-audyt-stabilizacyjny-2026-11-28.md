# AM II 30 — audyt stabilizacyjny bez nowych uwag

Data: 2026-11-28. Źródło: commit 57ed552d52bcbab1c31b1948526819048ccb8acb, blob 86f4e5e6c7a2f5913f2adf23bc6e6624bb0c9b69, 921 wierszy. Plik na gałęzi roboczej odpowiada temu blobowi.

## Kontrola matematyczna
- Tonelli i Fubini: właściwe rozróżnienie nieujemności i całkowalności, uzupełniona miara produktowa, mierzalne zbiory wyjątkowe miary zero, przedłużanie funkcji zerem, przekroje — poprawne.
- Iterowanie całek Riemanna: hipoteza całkowalności każdego przekroju, ograniczoność funkcji całek przekrojowych, nierówności sum Darboux i argument przez dowolnie małą różnicę sum — poprawne.
- Przykłady wyjątków: niemierzalny przekrój zbioru zerowego, niecałkowalny przekrój Riemanna, obie całki iterowane różne przy nieskończonych całkach części dodatniej i ujemnej — poprawne. Oszacowanie 12/(25x²) na 0<y<x/2 i wyniki ±π/4 sprawdzone.
- Całkowanie w dowolnej kolejności: iterowanie, niezmienniczość względem permutacji i iloczyny nieujemnych funkcji o skończonych całkach — poprawne.
- Zamiana zmiennych: dyfeomorfizm, moduł wyznacznika, mierzalność obrazu, równoważność całkowalności, wersja Riemanna na zwartych zbiorach Jordana — poprawne.
- Podstawienie poza zbiorem wyjątkowym: ograniczenie do dyfeomorfizmu na otwartych zbiorach pełnej miary, uzupełnienie miary i obie strony równości, przykład (u³,v), wynik 2 — poprawne.
- Współrzędne biegunowe i walcowe: zakresy parametrów i pominięte półosie/półpłaszczyzny zerowej miary, jakobian r. Współrzędne sferyczne: ortogonalność znormalizowanych kolumn i jakobian ρ² sin φ. Przykład dwóch pełnych obrotów poprawnie wykazuje dwukrotne liczenie pola.
- Rachunki ponownie sprawdzone: pole między parabolą i prostą 1/6, całka z e^x 3−e, zamiana kolejności z e^(y²) (e−1)/2, pole po usunięciu pasa 5/12, objętość sympleksu t^d/d!, moment czworościanu 1/24, podstawienie (u,uv) 1/2, obszar hiperboliczny 3 log 3, Gauss √π, paraboloida πR⁴/2, stożek i paraboloida 5π/6, kula 4πR³/3, moment radialny 4πR^(p+3)/(p+3), wycinek sferyczny 2πR³(1−cos α)/3 — poprawne.

## Statyka i technika
30 etykiet. 33 odsyłacze wewnętrzne, 14 między skryptami: wszystkie cele istnieją w kontrolowanych źródłach AM II 18,24,26,27,30 oraz ME 04,12,13. Brak duplikatów etykiet rozdziału w kontrolowanych rozdziałach AM II. Bilans klamer 0, minimalny bilans 0; środowiska poprawnie zagnieżdżone. Trzy rysunki bez zmian w niniejszym audycie; nie ponawiano samodzielnej kompilacji.

CI źródła 57ed552: terminologia #46133718789 success; walidacja AM II #46133718722 pending, #46133724045 skipped; aplikacja #46133718724 cancelled. Pełny PDF niepotwierdzony. Nie uruchomiono dodatkowego workflow.

Wynik: zero nowych uwag merytorycznych i statycznych. Źródło pozostawiono bez zmian. Następny etap: niezależny audyt kontrolny rozdziału 30, następnie rozdział 31.
