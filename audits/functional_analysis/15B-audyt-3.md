# Analiza funkcjonalna — 15B/03 (2026-11-24)

Stan wejściowy gałęzi: bf731f6d2c7fa043be0fe9c06bd6d28719d0ffc5. Raport 15B/02 był najnowszy; 15B/03 i 16/01 nie istniały. Źródło wejściowe 89cc07f494e18ab0d4eba2a7e588c7cec2176de3, test f151fd30e4dd415695444a454462497569fcb852.

Bezpośrednio odczytano job 138122587294 przebiegu 45297824384: completed/success, wszystkie 9 kroków success, w tym regresje, kontekst 01–17, kompilacja, walidacja PDF i publikacja. Dotyczy wersji sprzed niniejszych zmian. Oględziny stron 95–100 udokumentowano w 15B/02; nie powtarzano ich.

## Audyt poprawkowy
- Fubini: wyjaśniono silną mierzalność przekrojów przez przekroje ciągu funkcji prostych i zerowego zbioru wyjątkowego. Zdefiniowano F na zbiorze wyjątkowym i wykazano jej silną mierzalność przed całkowaniem normy różnicy. Usunięto lukę w kolejności argumentów. Ujednolicono terminologię przestrzeni sprzężonej i podwójnie sprzężonej.
- Regresja Fubiniego: generator weighted był konsumowany przy pierwszej współrzędnej, przez co druga zawsze wynosiła zero we wszystkich trzech obliczeniach. Materializacja do krotki oraz niezależna oczekiwana wartość (-53/210, 61/50) naprawiają test obu współrzędnych. Nie uruchomiono nowej wersji testu w tej iteracji.
- Przejrzano 11 dowodów: Pettis (rodzina normująca i ogony), Bochner (aproksymacja i dominacja), DCT (Borel–Cantelli), Fubini (poprawka powyżej), Riemann (jednostajna aproksymacja), Dunford (wykres domknięty), hierarchia (funkcjonały), Pettis DCT (refleksywność i mierzalność norm), Gelfand (wykres domknięty i słaba-* addytywność), wariacja (obie nierówności również dla nieskończoności), miara Bochnera (aproksymacja prostymi). Cztery przykłady: c0, nieośrodkowa przestrzeń Hilberta, ogony w l-infinity, brak RNP w C([0,1]); nie znaleziono dalszych błędów w tych przykładach.
- Kontrola po zapisie: 23/23 unikatowych etykiet, poprawne zagnieżdżenie środowisk, 11 dowodów, 4 przykłady. Odsyłacze do 15A i 16 objęte wcześniejszą bramką; nowa kompilacja niepotwierdzona.

Commity: f4a85983ee369fa7e44a83241af34c7d7b29ee06 (test), de80bf3f05c4125177128ece01f9b3ab4688b268 (źródło). Nowe bloby: 9739c713fd978e14623b96e3fea6c981fa81ca97 oraz a1d3dac82e31cf85ea7f5d5ece538a559f3425dc.

**0/2 czystych audytów.** Następny: 15B/04, potwierdzić CI nowych blobów i skontrolować PDF. Nie przechodzić do 16. Nie deklarujemy PASS dla nowych zmian.
