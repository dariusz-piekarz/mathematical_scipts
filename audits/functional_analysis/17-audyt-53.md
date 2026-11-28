# Rozdział 17 — audyt 53 (2/4 bloków, pierwszy przegląd, 0/2 stabilizacji)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Zakres
Pierwsze dwie podsekcje: topologia C^infty i funkcje odcięcia oraz kryterium ciągłości funkcjonału. Przejrzano również strukturę pozostałych dwóch podsekcji, bez zaliczania ich jako szczegółowo zaudytowanych.

## Poprawki
Jawne założenia definicji seminorm i konwencja dla pustego zbioru zwartego. Uściślono argument podciągu w wyczerpaniu, lokalną ciągłość granic, przejście pod całką i obustronny iloraz różnicowy, równoważność warunków Cauchy'ego z metryką niezmienniczą względem przesunięć. Wyprowadzono stałą 2^m ze wzoru Leibniza. Poprawiono konstrukcję funkcji wygładzającej: nośnik w domkniętej kuli o promieniu delta/2, zawartej w otwartej kuli o promieniu delta (poprzednia formuła miała nośnik równy domkniętej kuli o promieniu delta). Uzasadniono gładkość przedłużenia, różniczkowanie pod całką i zwartość nośnika funkcji odcięcia; uwzględniono pusty K. Notacja funkcji charakterystycznej chi_V. Rozpisano skalowanie w kryterium ciągłości funkcjonału oraz oszacowanie ewaluacji pochodnej. Usunięto kalkę „sekwencyjna” w dowodzie zupełności.

## Technika
Commit źródła 96211d9a959c9ce4c6bd29f4909bf242f0567f16, blob 64496595ae791745b0d5435ac6f5998fd66fe436. Odczyt po zapisie: 588 wierszy, 22/22 unikatowych etykiet, 8/8 rozwiązanych odsyłaczy wewnętrznych, zbilansowane środowiska. Cztery testy w tools/tests/test_functional_analysis_ch17.py (0b51525ddb187ae639c8a1eb063b63012acc39b2), osobny workflow kompilacji w kontekście 01–17 (ede801130da0ab6422cc9653a14dfcd79acb4818). W chwili kontroli nowego biegu CI jeszcze nie było na liście; testów nie deklarujemy jako wykonanych, PDF nie obejrzano.

## Następna iteracja
Audyt 54: bloki 3–4, seminormy Schwartza, zupełność, gęstość, brak normowalności, transformacja Fouriera, odwracanie i splot. Po zakończeniu pierwszego przeglądu ewentualna propozycja rozszerzenia (bez automatycznego dodawania), następnie stabilizacja do dwóch czystych audytów.
