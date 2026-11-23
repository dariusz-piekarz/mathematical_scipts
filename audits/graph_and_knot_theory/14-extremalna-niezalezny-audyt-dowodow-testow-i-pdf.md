# Teoria grafów i węzłów — niezależny audyt rozdziału ekstremalnego, iteracja 02

Data: 2026-11-23.
Źródło: \`chapters/pl/graph_and_knot_theory/41-twierdzenia-mantela-turana-i-ramseya.tex\`.
Wersja rozdziału: blob \`328790f72943ce7c9ffde6a71deeef65cea93192\`.
Nie oznaczać całego tomu jako stabilnego na podstawie tego raportu.

## Kontrola matematyczna

1. **Mantel** — zweryfikowano równość sumy kwadratów stopni z sumą stopni po końcach krawędzi; rozłączność sąsiedztw końców każdej krawędzi przy braku trójkątów; krok Cauchy'ego–Schwarza i zaokrąglenie do liczby całkowitej. Osobno rozpatrzono \`n=0,1\` i \`m=0\`.
2. **Symetryzacja Zykowa** — sprawdzono, że jednakowe otwarte sąsiedztwa wyznaczają niezależne klasy; klonowanie całej klasy \`B\` do nieprzyległej \`A\` nie tworzy nowego \`K_{r+1}\`; zmiana liczby krawędzi jest \`|B|(d(a)-d(b))\`; przy remisach scala klasy bez rozdzielania klas poza nimi. Jest to kluczowy krok drugiego kryterium maksymalizacyjnego w dowodzie Turána.
3. **Turán** — sprawdzono oba kryteria maksymalizacji: najpierw liczba krawędzi, następnie suma kwadratów liczności klas bliźniaków. Niezależnie oceniono argument rozdzielenia części przy liczbie części mniejszej niż \`min(n,r)\` oraz zmniejszanie \`sum n_i^2\` przy przesuwaniu wierzchołka między częściami. Przypadki \`n=0\`, \`r=1\`, \`r>n\` nie wymagają dodatkowych założeń.
4. **Ramsey** — sprawdzono kwantyfikatory w definicji \`R(s,t)\`, przypadki brzegowe \`s=1\` lub \`t=1\`, pełny argument sąsiedztwa czerwonego/niebieskiego, dwumianową indukcję z tożsamością Pascala oraz dowód równoważny dla kliki i zbioru niezależnego.
5. **Dokładne \`R(3,3)=6\`** — górne ograniczenie przez \`R(2,3)=R(3,2)=3\`, dolne przez dwa dopełniające się pięciocykle w kolorowaniu \`K_5\`.
6. **Ramsey wielobarwny** — skontrolowano redukcję \`q\` kolorów do dwóch grup i krok indukcyjny z \`N=R(M,k_q)\`.

Nie wykryto matematycznej niezgodności tych dowodów w zbadanym zakresie.

## Regresje obliczeniowe

Pierwsza wersja testu została poprawiona po wykryciu błędu kolejności budowania tablicy oszacowań dwumianowych. Była to wada testu, nie dowodu. Naprawa w commicie \`061fbb2f940f21743ad00a6e493cb8754aa24b3d\`.

[GitHub Actions — potwierdzony przebieg 45148475682](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148475682):
- \`finite-models\`: success;
- \`chapter-pdf\`: success;
- 33 868 wszystkich grafów prostych na 0–6 wierzchołkach, porównanie \`ex(n,K_{r+1})\` z dokładnym wzorem Turána, dla \`r=1..5\`;
- 10 650 niezależnych eksperymentów symetryzacyjnych dla wierzchołków niesąsiadujących, sprawdzenie zmiany liczby krawędzi i zachowania braku kliki;
- 33 792 wszystkich dwukolorowań \`K_5\` i \`K_6\`, w szczególności brak kontrprzykładu na sześciu wierzchołkach i istnienie kontrprzykładu pięciowierzchołkowego;
- wcześniejsze testy BFS/DFS, dróg ważonych, A*, CH, MST/DSU i przepływów również przeszły.

## Realny skład

- Dwuformatowy audyt: skontrolowano tekst LaTeX oraz PDF z workflow, zawierający historyczne rozdziały 00–05 i pięć nowych rozdziałów algorytmicznych/ekstremalnych.
- PDF ma **63 strony A4**; nowy rozdział zajmuje strony 59–63, numerowane w druku 55–59.
- Obejrzano osobno wszystkie pięć stron rozdziału. Rysunki \`K_{3,3}\` oraz dwukolorowania \`K_5\` i ich podpisy są czytelne, bez kolizji z tekstem i wierzchołkami.
- Trzy kolejne przebiegi \`pdflatex\`, brak przepełnień \`Overfull\` i brak ostrzeżeń o niestabilnych odsyłaczach (warunki workflow).
- \`catalog/books.json\` ma identyczną kolejność 42 plików jak główny plik \`books/pl/graph_and_knot_theory.tex\`; nowy rozdział znajduje się po czterech rozdziałach algorytmicznych.

## Status

**Wynik kontroli matematyczno-redakcyjnej i PDF: PASS.**
Czekamy jeszcze na ostateczny wynik workflow aplikacji Atlas dla commita integracyjnego (początkowo \`917cace9\`), zanim zostanie nadany końcowy status stabilizacji całego nowego modułu.
Dalszy moduł planu: \`G(n,p)\` i probabilistyczne metody teorii grafów, oddzielnie od ekspanderów.
