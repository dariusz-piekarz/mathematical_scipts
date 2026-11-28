# Audyt 181 — drukowany rozdział 19, etap A (stabilizacja)

Data: 2026-11-25. Kontynuacja audytu 180, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Commit korekty 5d73e8551540197863a55a3ff15d5c96784eb15b, blob de9b618fe643ca945ea98c644ee12b843fff916e.

## Kontrola matematyczna i korekty
- Ponownie przejrzano definicję Tutte'a, rekurencję dla zwykłej krawędzi, mostu i pętli, w tym zgodność wykładników i zachowanie krotności przy kontrakcji. Uzupełniono dowód równoważności nu(A)=0 i bycia lasem, również dla pętli, równoległych krawędzi i pustego grafu.
- Twierdzenie Kirchhoffa w rozdziale źródłowym 08 dotyczy prostych grafów ważonych. Uzupełniono brakujący argument dla multigrafów: pętle nie wnoszą kolumny do BB^T ani drzewa, krawędzie równoległe zastępuje jedna z wagą równą krotności; ważona suma drzew liczy dokładnie drzewa rozróżniające kopie. Dodano odsyłacz thm:tg-kirchhoff i przypadek n=1.
- Doprecyzowano znaki i osobne kolumny macierzy incydencji oraz udowodniono niezależność liczby przepływów od pomocniczej orientacji przez zmianę znaku odpowiedniej współrzędnej.
- Ponowna kontrola specjalizacji (1,1), (2,1), (2,2), chromatycznej i obu dowodów dualności nie wykazała błędów rachunkowych. 12 etykiet i 32 pary środowisk zachowane. Nie dodano proponowanego ogólnego wielomianu przepływów.

## Trwałe regresje wykonane
GKT-19-REC-01, test_gkt19_recursion.js, commit 2750d1b6d1d43f3b8dc6e05ccfc8c9791f2bbe66: PASS, 3528 multigrafów (n=0..4, m=0..5, krotności i pętle), 89217 podzbiorów, 15855 tożsamości rekurencji dla wszystkich wystąpień krawędzi (6605 pętli, 3870 mostów, 5380 zwykłych), 14112 porównań z bezpośrednim liczeniem kolorowań dla q=1..4. W tym 2573 grafy niespójne; sprawdzono specjalizacje lasów oraz maksymalnych lasów. Porównanie dokładnych współczynników w bazie przesuniętej.
GKT-19-DUAL-01: ponownie PASS, 747 układów, 453 sferyczne, 3533 pary dopełniających podzbiorów, 1812 porównań przepływów i kolorowań (906 dla q złożonych).
Oba zapisane skrypty pobrano ponownie i wykonano po korekcie w izolacie JS, nie w procesie Node. Modele skończone nie stanowią dowodu ani formalizacji Lean. Kontrola zastosowania Kirchhoffa to audyt semantyczny, nie test wyznacznika.

## CI i PDF
Dla wcześniejszego d24c111: terminologia 45568671124, algorytmy 45568671208, aplikacja 45568670959 SUCCESS; pełny audyt 45568671098 w toku.
Dla właściwego nowego commitu 5d73e85: aplikacja 45568916763, terminologia 45568916770, algorytmy 45568916798, pełny audyt 45568916810 — w toku przy kontroli. Nie oglądano nowego PDF. Etap A otwarty; kolejna iteracja: CI, kontrola PDF i powtórna stabilizacja. Nie przechodzimy do rozdziału 20.
