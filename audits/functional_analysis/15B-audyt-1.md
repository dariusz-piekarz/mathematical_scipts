# Analiza funkcjonalna — 15B/01 (24 listopada 2026)

Gałąź: biblioteka-matematyczna-iteracja-6. Stan wejściowy cd3a5eb15891259dd328d522861af009cf03a906. Raport 15A/05 zamyka 15A; bezpośrednio potwierdzono workflow 45295648912 completed/success dla a7082cbc3510cf9d285cf4f53bf2989517ab5d95. Nie jest to CI 15B.

## Kontrola matematyczna (10 dowodów)
1. Pettis: przeliczalna rodzina normująca, mierzalność odległości, obcięcie ogonów i Borel–Cantelli; przypadek Y={0} trywialny.
2. Bochner: aproksymacja w L1, zupełność, obcięcie normy i dominacja 3||f||; naprawiono trzy uszkodzone relacje LaTeX.
3. Zbieżność zmajoryzowana: uzupełniono niejawny wybór przekątnej przez błędy 1/n i miary 2^-n oraz Borel–Cantellego.
4. Fubini: gęstość prostokątów, podciąg z sumowalnymi błędami i skalarne Fubini; w następnym audycie rozwinąć identyfikację granicy przekrojów oraz mierzalność po uzupełnieniu produktu.
5. Riemann–Bochner: jednostajna aproksymacja; funkcja charakterystyczna wymiernych daje kontrprzykład dla niezerowej przestrzeni.
6. Dunford: wykres domknięty Q, ograniczoność i reprezentacja w X''.
7. Hierarchia: przemienność z funkcjonałami, zanurzenie kanoniczne.
8. Pettis DCT: refleksywność, jawna mierzalność norm różnic, oszacowanie supremum.
9. Gelfand: wykres domknięty i skalarna addytywność, nie normowa.
10. Wariacja Bochnera: partycje funkcji prostych, oszacowanie różnicy wariacji. Ogólna addytywność wariacji wymaga osobnego uzasadnienia w następnym audycie.

## Przykłady (4)
c0: całka Dunforda to stały ciąg jedynek; nie należy do c0. Nieośrodkowa przestrzeń Hilberta: każdy wektor ma przeliczalny nośnik, całki skalarne znikają, brak silnej mierzalności. Gelfand w l-infinity: ogony mają normę 1, lecz zbieżność słabą-* do zera. Brak RNP w C([0,1]): ewaluacje wymierne i wspólny zbiór pełnej miary wymuszają nieciągłość.

## Zmiany i status
Źródło po poprawce: 78680e4099da22d4394c3b2944001f3c29a59b1a; commit e01feca353c6adc8f09f9370290c4064bce2b71d. Test regresyjny zapisano w 5f1d57ed5305ee14244ff227384e00baaca6861c; kontroluje uszkodzone relacje i budżet błędów przekątnej. Nie uruchomiono testu ani kompilacji w tej iteracji. Kontrola strukturalna: 22 unikatowe etykiety, sparowane środowiska, trzy poprawione relacje obecne. Pełna kontrola odsyłaczy, terminologii, PDF i dedykowanego CI pozostaje otwarta. Stabilizacja 0/2; nie przechodzić do 16.
