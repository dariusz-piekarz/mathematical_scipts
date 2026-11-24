# Iteracja 20 — ostatnie zatwierdzone rozszerzenie rachunku różniczkowego i całkowego

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: raport 19 (059d5a5b69e6f4e612686a2654149a9e8147e980). Użytkownik zatwierdził wszystkie osiem zaproponowanych elementów oraz polecił zakończyć rozszerzanie zakresu i wrócić do audytów. **Nie proponować ani nie wdrażać dalszych opcjonalnych rozszerzeń tej części analizy funkcjonalnej w ramach obecnej rundy.** Konieczne poprawki matematyczne, językowe, redakcyjne i techniczne nadal wykonywać.

## Zrealizowane punkty
1. Rozdział 14: pochodna słaba i słaba-* krzywych, istnienie elementu X'' reprezentującego wszystkie pochodne skalarne przez Banacha–Steinhausa, warunek normowej ciągłości słabej pochodnej zapewniający C1, kontrprzykłady w l2 i c0, definicja Bastianiego oraz dowód liniowości pochodnej. Uściślono samodzielność założeń i dodano odsyłacz do 15B.
2. Rozdział 15: wszystkie pochodne odwrotności jako sumy po permutacjach i eksponenty operatorowej jako całki po sympleksie. Dowody: szereg Neumanna i indukcja, jednostajna zbieżność szeregów pochodnych oraz wzór na całki jednomianów po sympleksie. Przykład macierzy nieprzemiennych.
3. Moduł 15A: Leibniz z ruchomymi granicami, także gdy zmieniają kolejność, z dowodem seminormowym; wielokrotne różniczkowanie całki Riemanna z parametrem.
4. Moduł 15B: wektorowe twierdzenie o punktach Lebesgue'a i różniczkowaniu całki Bochnera, dowód przez przybliżenia proste i skalarną teorię różniczkowania.
5. Moduł 15B: krzywe bezwzględnie ciągłe, reprezentacja przez całkę Bochnera, pełny dowód równoważności RNP (w definicji dla dowolnej skończonej przestrzeni z miarą) z różniczkowalnością krzywych Lipschitza prawie wszędzie. Kierunek odwrotny: funkcje proste związane z partycjami mierzalnymi, kodowanie partycji na przedziale z wymuszonym zmniejszaniem średnic, jednostajna granica krzywych Lipschitza i sprzeczność z brakiem Cauchy'ego w L1. Przykład t -> |t-·| w C([0,1]).
6. Moduł 15B: skalarne pochodne całek nieoznaczonych Pettisa, Dunforda, Gelfanda, przykład e_t w nieośrodkowej przestrzeni Hilberta, wspólny zbiór wyjątkowy przy ośrodkowości przestrzeni testującej i całkowalnej majorancie.
7. Moduł 15B: różniczkowanie pod znakiem całki Lebesgue'a w normie i w słabych topologiach, wspólna dominacja normy różnicy lub indywidualna dominacja skalaryzacji, zbieżność normowa jednostajna po zbiorach, wyższe rzędy w wersji Bochnera.
8. Moduł 15B: wektorowe przestrzenie Sobolewa w czasie W^{1,p}, definicja pochodnej dystrybucyjnej, dowód reprezentacji bezwzględnie ciągłej bez RNP i jednoznaczności pochodnej z przeliczalną rodziną normującą, oszacowania przyrostu i przypadek p=infinity.

## Stan źródeł
- 14: 433 wiersze, 15 dowodów, blob abe9d33dce13a6e884f73da41859ec9f6ed29abb; commity c9d320d84adb80f2d00926223db3a9f33d7b4788, fc54b38ceae8b5fcfada53d0c81703fcdd598fc6.
- 15: 356 wierszy, 14 dowodów, blob cbac319d7a8c2da4e2b5618a72cd96400beee543; commit 37e82e3568393d3a29238ae812fb5986db327134.
- 15A: 515 wierszy, 12 dowodów, blob ec55436f83b04a13ed52a424cda238e43e5b2c16; commit 4ec15283d460fd8694f2ced65e470673da7f5804.
- 15B: 2838 wierszy, 37 dowodów, 11 przykładów, 59 etykiet, blob 5ee3e1bab6a7aa5104b6f7ae290ff8fa389fffcb; commity bc62e6d7888722e4698306efc1674a28f7d56037, c98677d47d647d7959d715011b3f615b88d9858d.
Łącznie 138 unikalnych etykiet w czterech rozdziałach, poprawne zagnieżdżenie środowisk, sprawdzone kontrakty źródłowe.
Regresje: commit 793ae82d1cfa74994964e16c311ef7139e920279, blob 5bb6e912e22f0b20566003d6a842a12d5090ee54. 20 testów w pliku test_functional_analysis_ch15b.py; dwa nowe testy kontraktów czterech rozdziałów i dokładnych rachunków (odwrotność, całki beta, Leibniz, kodowanie partycji). Nie są formalną weryfikacją dowodów.
CI dla wcześniejszych commitów 14, 15, 15A zakończone sukcesem: 45351798086, 45351802223, 45351806932. Przebiegi dla finalnego 15B i poprawionych odsyłaczy jeszcze w toku przy odczycie; nie potwierdzono pełnych 20 testów ani oględzin końcowego PDF.

## Kolejność dalszych audytów — zakres zamknięty
Wszystkie zmodyfikowane rozdziały 14, 15, 15A, 15B wymagają ponownej stabilizacji (każdy 0/2). Następna iteracja: audyt 14, w kolejności 14, 15, 15A, 15B; każdy rozdział audytować aż do dwóch czystych audytów oraz zaliczenia regresji i PDF. Szczególnie sprawdzić długi dowód charakteryzacji RNP, kwantyfikatory, pochodne operatorowe, reprezentację Sobolewa i zgodność odsyłaczy. Nie przeskakiwać rozdziałów, nie wracać do rozszerzania zakresu. Po ustabilizowaniu czterech rozdziałów przejść do rozdziału 16 według wcześniejszego planu.
