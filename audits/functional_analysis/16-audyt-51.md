# Rozdział 16 — audyt 51 (5/5, czysty źródłowo, 1/2 warunkowo)

24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6. Źródło bez zmian od audytu 50, blob eee4c982d1dfdd23d932e432c7328eb9ce33f264.

## Ponowna kontrola
1. Wypukłość rozszerzona: końce odcinka, dziedzina efektywna, oba kierunki nierówności stycznej, warunek minimum, znaki i współczynniki w nierówności silnej wypukłości, kryterium hesjanu i odsyłacz do 15.
2. Półciągłość: liminf sieci i względna topologia, domknięcie podpoziomów, wybór diagonalny w ośrodkowej podprzestrzeni, oszacowanie 2M, reprezentacja Riesza, słaba domkniętość C i jednoznaczność tylko przy ścisłej wypukłości.
3. Subgradient: skończoność wartości, oba znaki t, reprezentacja gradientu, norma w zerze; prox: koercywność, wypukłość, oba kierunki charakterystyki, nieekspansywność i przypadki brzegowe.
4. Dirichlet: związanie kwantyfikatorów w H_0^1, niezależność reprezentanta L², zupełność, stała Poincarégo, ścisła wypukłość energii, reszta Frécheta, warunki brzegowe i całkowanie przez części.
5. Miary probabilistyczne: normowanie, słabe-* domknięcie, Banach–Alaoglu, pełna masa nośnika, nietrywialna dekompozycja miary i zasada Bauera.
Nie znaleziono istotnych usterek wymagających zmian źródła. Nie dodano tematów ani sztucznych zmian.

## Technika
19 unikatowych etykiet, 18 wystąpień odsyłaczy (14 różnych), wszystkie rozwiązane na podstawie plików 07,09,13,14,15,16; środowiska poprawnie zagnieżdżone. Potwierdzono obecność twierdzenia Eberleina–Šmuliana w 26. CI 45376983069 dla audytu 50: etap regresji i przygotowania kontekstu zakończony sukcesem, kompilacja w toku w chwili odczytu. Poprzedni pełny CI 49 zielony. Oględzin stron PDF nie wykonano.

## Decyzja
Pierwszy czysty audyt źródłowy (1/2), warunkowo do potwierdzenia całego CI dla niezmienionego źródła. Audyt 52: niezależne przejście przez dowody i kontrolę końcową CI; ewentualna istotna usterka zeruje licznik. Nie uznawać kontroli automatycznej PDF za oględziny wizualne.
