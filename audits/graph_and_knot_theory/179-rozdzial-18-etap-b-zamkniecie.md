# Audyt 179 — drukowany rozdział 18, zamknięcie etapu B

Data: 2026-11-25. Kontynuacja 178; bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.
Commit źródłowy 744631c9cede6046a594bdd0d36b289736984624; aktualny blob 93a01f499f7072022f2fa51805bb81add999da19.

## Ponowna kontrola semantyczna
- GKT-18-CW-01: regularne otoczenie dyskowo-pasowe daje po jednym półotwartym kołnierzu przy każdym okręgu brzegu. Kołnierze nie łączą różnych składowych dopełnienia otoczenia. Retrakcja ściany na zwartą składową zachowuje kontraktowalność. Z 2-2h-b=1 przy b>=1 wynika h=0,b=1; z 2-k-b=1 przy k,b>=1 wynika sprzeczność. Domknięty kołnierz daje ciągłe odwzorowanie charakterystyczne z możliwymi powtórzeniami krawędzi i wierzchołków na brzegu; iloraz po przyklejeniu jest zwarty, bijekcja do powierzchni Hausdorffa jest homeomorfizmem. Nie wymaga regularnej struktury CW. Kryterium semantyczne spełnione.
- GKT-18-EMPTY-01: dla spójnego grafu bez krawędzi n=f=1, powierzchnia jest jednopunktowym uzwarceniem otwartego dysku, czyli sferą; T,T* mają po jednym wierzchołku i zero krawędzi, B=L=pusty, C1=0, d1=d2=0, H0=H2=Z, H1=0. Liczby ścian nie wyliczamy z pustej permutacji. Kryterium semantyczne spełnione.
- Sprawdzono warunek rozłączności wnętrz krawędzi dualnych i konstrukcję promieni, przypadek pętli, znaki obchodów, spójność dualnego grafu przez twierdzenie o dualności komórkowej, prezentację grupy fundamentalnej torusa i jej izomorfizm z Z². Nie wykryto nowych istotnych usterek.
- Ponowny odczyt źródła: 43 poprawnie zagnieżdżone pary środowisk, 14 etykiet. Nie zmieniano źródła.

## Wykonane regresje
Pięć zapisanych funkcji testowych wykonano ponownie w izolacie JS z odpowiednikami asercji Node, nie w procesie Node:
BRIDGE-01 PASS 1067; ROT-01 PASS 7776+64; TC-01 PASS 2546 układów, 2221 spójnych, 4442 rozkłady, 8996 elementów bazy, 12354 relacje; ORIENT-01 PASS 6177 kontroli znaków; FIG-01 PASS separacja 42.501011 stopnia > 24 stopnie. Zbiory prób TC i ORIENT nakładają się. Kontrole semantyczne powyżej nie są automatycznymi testami ani formalizacją Lean.

## CI i PDF
Dla właściwego SHA: pełny audyt 45567894109 SUCCESS, algorytmy 45567894177 SUCCESS, terminologia 45567894098 SUCCESS, aplikacja 45567894113 SUCCESS.
Pobrano ZIP 15001370625 z pełnego audytu. PDF ma 339 stron, plik ostrzeżeń ma 0 bajtów. Rozdział 18 obejmuje PDF 156–164 (druk 146–154), 9 stron, 9 adnotacji odsyłaczy. Wyrenderowano wszystkie strony rozdziału i obejrzano ich układ w dwóch arkuszach kontaktowych; trzy rysunki widoczne, poprawiony graf dualny zachowany, brak zauważalnych obcięć i nachodzenia elementów. Rozdział 19 rozpoczyna się na następnej stronie.

## Decyzja
Brak nowych otwartych istotnych usterek w zakresie audytu rozdziału 18. Etapy A i B zamknięte dla wskazanego blobu. Następny audyt 180: drukowany rozdział 19 (plik źródłowy 12), wielomian Tutte’a, kolorowania i dualność algebraiczna; etap A. Nie oznacza to zamknięcia audytu całego tomu.
