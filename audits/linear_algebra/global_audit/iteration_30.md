# Algebra liniowa — audyt globalny 30: dodatkowy sceptyczny audyt końcowy LA-29

**Data:** 23 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Zakres:** wyłącznie LA-29 „Grassmanniany i współrzędne Plückera”, 746 wierszy.
**Nieprzerwany blob źródła:** 01213689fb5d2477db25f9ff713608b0171a00c8.
**Historia stabilizacji:** audyt 27 — korekta, następnie audyty 28 i 29 — 2/2 czystych pełnych kontroli. Obecny audyt 30 wykonano oddzielnie jako końcowy sceptyczny audyt +1.
**Wynik:** bez nowych błędów i zmian źródła. **LA-29 STABILNY (2+1)**. Do LA-30 przejść dopiero w kolejnej iteracji.

## Sześć dowodów i pełna kontrola rozdziału

Przeczytano wszystkie cztery twierdzenia, dwa stwierdzenia, dwie definicje, sześć dowodów, sześć przykładów, dwie uwagi i dwa rysunki. Szczegóły per-dowodowe są w iteration_30_proof_review_29.csv.

1. **Atlas Grassmannianu (linie 56–140).** Sprawdzono oba kierunki odwzorowania wykresowego, przejścia między rozkładami także o nieortogonalnych dopełnieniach, formułę rzutowania i jego odwrotność, zwartość modelu rzutów, własność Hausdorffa i drugi aksjomat przeliczalności. Zbadano k=0, k=n, przypadki rzeczywisty i zespolony. Bez błędów.
2. **Przestrzeń styczna (213–249).** Sprawdzono niezależność klasy pochodnej od wybranego podniesienia wektora, zależność wyłącznie od pochodnej współrzędnej wykresu, iniektywność i surjektywność odwzorowania do Hom(L,V/L), a także skrajne wymiary. Bez błędów.
3. **Wiązki (313–332).** Jawne trywializacje, reprezentant klasy modulo wykres, dokładność jądro–obraz i gładkość identyfikacji ilorazu z dopełnieniem ortogonalnym. Bez błędów.
4. **Stiefel i ilorazy O(n), U(n) (462–489).** Przechodniość, stabilizatory blokowe oraz gładkie sekcje konstruowane przez ortonormalizację. Bez błędów.
5. **Plücker (519–589).** Poprawność wyznacznika zmiany bazy, znaków minorów, kryterium przez iloczyn zewnętrzny, rekonstrukcji wykresu, immersji i topologicznego osadzenia. Przykład dla Gr_2(R^4) ma właściwe znaki i wymaga charakterystyki różnej od 2, co gwarantuje założenie o ciele rzeczywistym lub zespolonym. Bez błędów.
6. **Odwzorowanie Gaussa (664–687).** Lokalna postać z niezerowego minora pochodnej, wiązki styczna i normalna jako cofnięcia. Sprawdzono typ dG_p oraz interpretację wartości dG_p(e_1) po korekcie z audytu 27. Bez błędów.

Przykłady skontrolowane krytycznie: dwie mapy RP^1, funkcja przejścia wstęgi Möbiusa, zorientowane płaszczyzny w R^3, równanie kwadryki Plückera i kontrprzykład nieskładalnego wielowektora, parabola, a także konstrukcja klasyfikująca gładkiej wiązki na zwartej rozmaitości. Nie stwierdzono nowych luk, nadużyć hipotez, błędów językowych ani problemów terminologicznych.

## Nowe niezależne testy, rzeczywiście wykonane

Skrypt /mnt/data/la29_global30_final.py (SymPy, seed 202611230030, SHA256 995ade7d318574bcd6d6fe83a357bc4da8f5e2d4f5e897f1952fbc6ff54e8223): **1872/1872 PASS**.
- Przejścia map: 427, różniczki tych przejść weryfikowane niezależnym różniczkowaniem: 427.
- Rzuty ortogonalne: 90; równania pochodnych rzutów: 90; obrazy rzutów: 90.
- Równania Plückera: 100; transformacje przy zmianie bazy: 83; odzyskiwanie wykresu z minorów: 454.
- Wstęga Möbiusa: 30 przejść i 30 testów znaków.
- Parabola: 3 tożsamości; skrajne k=0,n: 48 testów.

To rachunkowa regresja niezależna od wcześniejszych generatorów, nie formalizacja Lean.

## LaTeX, odsyłacze i PDF

W źródle jest 19 etykiet bez duplikatów, 20 odsyłaczy bez brakujących lokalnych celów, 6 poprawnie sparowanych dowodów, 2 rysunki figure i 2 tikzpicture. Katalog książek obejmuje 32 rozdziały w poprawnej kolejności.

Potwierdzone GitHub Actions na tym samym źródle: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079917894, https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081081248 oraz https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081121567 — wszystkie completed/success. W workflow weryfikowano dwa przebiegi kompilacji LaTeX i odsyłacze.

Odczytano rzeczywisty artefakt linear_algebra.pdf ze wskazanego CI: 320 stron (SHA256 9998b964b79eb86bebb6a0b2d7a4b74effc880e0929ec04947206af5bc299f58), rozdział LA-29 na stronach 287–294. Oceniono wszystkie osiem stron, rysunki na 288 i 291 w powiększeniu; nie znaleziono nakładających się etykiet, kolizji podpisów ani elementów poza stroną. Log: 0 ostrzeżeń LaTeX, Overfull, Underfull, Missing character, Undefined control sequence i undefined references. Wyciąg PDF LA-29 (8 stron) ma SHA256 1539a2386a4e3b686fc4e8e599bf4146292d60409619e272c04043a8d8e46cfc.

## Status

**LA-29 stabilny:** dwie osobne czyste kontrole 28–29 oraz dodatkowa pełna sceptyczna kontrola 30 na identycznym blobie, pozytywne rzeczywiste testy i CI, wizualny odbiór PDF. Nie wykonano nieuzasadnionych zmian .tex. Cały audyt globalny pozostaje OTWARTY: **363/382 dowodów**, pozostaje **19** — LA30: 3, LA31: 6, LA32: 10. Następnym etapem jest LA30 w osobnym przebiegu, a po 382/382 dodatkowy globalny audyt przekrojowy książki.

Nowy commit raportu może sam uruchomić CI; wyniki takiego przyszłego przebiegu nie są z góry potwierdzone. Żaden zielony workflow nie jest formalną certyfikacją Lean.
