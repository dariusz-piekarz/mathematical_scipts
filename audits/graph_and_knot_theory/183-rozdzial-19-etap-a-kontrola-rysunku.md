# Audyt 183 — drukowany rozdział 19, etap A (kontrola rysunku i łamania)

Data: 2026-11-25. Kontynuacja 182, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Wejściowy commit c6e414ee83436b8c819ae1aa6a59550197f9a554, blob 777cd22e94d442434277ccf2351df76795c3e9e7.
Korekta f8eb8d88cd4adce8327754455dde2594e1e78d4e, blob 2472339133f7c28a618e3fd47dbbc1ba46658755.

## CI i rzeczywista kontrola PDF
Dla wejściowego SHA: pełny audyt 45569308284, algorytmy 45569308187, terminologia 45569309717, aplikacja 45569308418 — wszystkie SUCCESS przy końcowej kontroli.
Pobrano artefakt 15001252802, rzeczywisty PDF (341 stron, plik ostrzeżeń 0 bajtów). Rozdział 19: PDF 165–171, druk 155–161; 7 stron, 9 odsyłaczy. Wyrenderowano każdą stronę w skali 1.5, obejrzano dwa arkusze kontaktowe i pełną stronę PDF 167. Schemat rekurencji poprawny: widoczne znaki równości i plus, podpisy usunięcia i kontrakcji, brak nakładania tekstu i krawędzi. Ostatnia strona zawiera jedynie końcówkę akapitu bibliograficznego; jest niemal pusta. Skrócono przejście i bibliografię do jednej sekcji nienumerowanej z zachowaniem trzech wskazań literaturowych oraz informacji o dalszych tematach. Nie oglądano PDF po tej korekcie, więc jej wpływ na liczbę stron niepotwierdzony.

## Kontrola matematyczna
Ponownie sprawdzono dowód przez las rozpinający, rekurencję i wykładniki, specjalizacje, ważoną redukcję Kirchhoffa, dopełniające podzbiory i dualność przepływów. Nie znaleziono nowych błędów matematycznych. Nie zmieniono twierdzeń, dowodów ani rysunku z audytu 182. Zachowano 12 etykiet i 32 poprawnie zagnieżdżone pary środowisk.

## Trwałe regresje
Wszystkie trzy zapisane skrypty odczytano i ponownie wykonano po korekcie w izolacie JS (nie proces Node):
- GKT-19-REC-01 PASS: 3528 grafów, 89217 podzbiorów, 15855 rekurencji, 14112 porównań kolorowań.
- GKT-19-DUAL-01 PASS: 747 układów, 453 sferyczne, 3533 par podzbiorów, 1812 porównań przepływów i kolorowań (906 dla złożonych q).
- GKT-19-KIRCH-01 PASS: 3527 multigrafów, 954 spójne, 3532 dokładne wyznaczniki minorów BigInt.
Zbiory prób częściowo się pokrywają, nie jest to formalizacja Lean.

## Bramka
Dla nowego SHA: pełny audyt 45569719965, terminologia 45569719896, aplikacja 45569720006, algorytmy 45569720000 — w toku przy kontroli. Nie przenosimy PASS PDF na nowy blob. Etap A otwarty jedynie do ponownej kontroli stabilności i PDF; po bramce niezależny etap B. Nie przechodzimy do rozdziału 20.
