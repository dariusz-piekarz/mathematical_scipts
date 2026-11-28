# RRC 17 — iteracja 298: Harnack, regularność Höldera i kontrprzykłady

Commit źródła: 7e6fe448d3a53056757a48adcb19cd0995ab7bac. Szczegółowa lektura sekcji 17.6–17.8.

1. Uściślono lokalną dziedzinę stosowania Harnacka: wystarcza B_4R zawarta w obszarze, przy H^1 na B_4R; mniejsza kula B_2R jest względnie zwarta w B_4R. Umożliwia to zastosowanie do u-m i M-u bez założenia ich nieujemności poza B_4r.
2. Rozpisano normalizację średnich, odwracanie kresów istotnych, most potęgowy i przejście epsilon do zera.
3. Rozpisano dyskretną redukcję oscylacji i dobór wykładnika, osobne przypadki bliskich i odległych punktów Lebesgue'a, konstrukcję reprezentanta na domkniętej kuli, niezależność wyboru ciągów oraz sklejanie reprezentantów.
4. Mocna zasada maksimum: jawnie chodzi o globalny kres osiągnięty wewnątrz obszaru; dowód otwartości i domkniętości zbioru ekstremum.
5. Przykład skokowego współczynnika: słaba pochodna, stałe eliptyczności i sprawdzenie równania w d wymiarach.
6. Przykład radialny: całkowalność gradientu, identyfikacja słabego gradientu, znikanie dwóch różnych wyrazów brzegowych, dowód regularności gamma-Höldera oraz brak lepszego wykładnika. Doprecyzowano, że przykład nie wyznacza uniwersalnie optymalnego wykładnika dla ustalonej klasy macierzy w dowolnym wymiarze.

Kontrola zapisanego źródła: 852 wiersze (wcześniej 758), 36 etykiet w tej samej kolejności, wszystkie unikatowe, 35 wystąpień odsyłaczy. Wszystkie cele wewnętrzne istnieją; trzy zewnętrzne chap:pde14, chap:pde15, chap:pde16 potwierdzone w źródłach tego samego commitu. Brak niezgodności begin/end. Nie jest to kompilacja ani kontrola wizualna. CI aplikacji 45978404766 i terminologii 45978404857 w kolejce; brak dedykowanego przebiegu rozdziału 17.

Pierwsza szczegółowa lektura wszystkich sekcji zakończona (296–298). Następny etap: pełny audyt stabilizacyjny, ponowna weryfikacja szczególnie zmienionych dowodów, dedykowana kompilacja i odbiór PDF, potem niezależny audyt kontrolny.
