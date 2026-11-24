# Rozdział 17 — audyt 56 (4/4, poprawkowy, 0/2)

24 listopada 2026. Istniejąca gałąź biblioteka-matematyczna-iteracja-6. Ponowna kontrola całego rozdziału, bez rozszerzenia zakresu.

## Poprawki
Jawnie ustalono normę euklidesową i miarę Lebesgue'a. Rozpisano konstrukcję V i W jako skończonych sum kul, dodatniość odległości od dopełnień i wybór delta w lemacie o odcięciu. Wyprowadzono 0<=chi<=1 przez podstawienie w całce i wykazano, na jakim otoczeniu K funkcja chi jest równa 1. W przykładach Schwartza uzasadniono ograniczoność ważonych pochodnych funkcji o zwartym nośniku i wielomianu razy Gauss; dla funkcji 1/(1+|x|²) wskazano konkretną rozbieżną seminormę. Uzupełniono wybór funkcji f, konstrukcję odcięcia przez przedłużenie zerem i oszacowanie każdego składnika w dowodzie gęstości w S, wraz z niezależnością stałej od f i R. W końcowej uwadze rozpisano kryterium ciągłości liniowego funkcjonału na S, z jawnymi kwantyfikatorami.

## Weryfikacja
Źródło 4a338dabef109ed369f8aec98650df2961a2adc9, blob f4dd20e99ca5b89973577e545facd2f20e489c15. Odczyt po zapisie: 738 wierszy, 22/22 etykiety, 13/13 odsyłaczy, zbilansowane środowiska, 5/5 nowych warunków tekstowych. Test test_cutoff_density_and_schwartz_examples zapisano w 495e872ea8b2228e9707916233887dc261ad4dc3; pełnego wykonania nie potwierdzono. CI audytu 55 (45379731447, 45379687994, 45379671850) zakończone sukcesem. W 45379731447 potwierdzono regresje, kompilację i automatyczną kontrolę PDF/odsyłaczy oraz artefakt PDF 14913820238. Nie obejrzano stron PDF. CI 56 niepotwierdzony.

## Decyzja
Audyt poprawkowy, licznik 0/2. Następny audyt 57: stabilizacja całości, bez nowych zagadnień, kontrola CI i wizualna PDF.
