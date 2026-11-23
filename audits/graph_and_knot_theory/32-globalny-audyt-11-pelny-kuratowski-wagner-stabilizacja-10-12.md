# Teoria grafów i węzłów — globalny audyt 11: dowód Kuratowskiego i stabilizacja bloku 10–12

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.

## Werdykt

**PASS — luka w dowodzie odwrotnej implikacji twierdzenia Kuratowskiego została domknięta w tekście rozdziału 10.**
**PASS — matematyczny audyt bloku 10–12, dokładne testy modeli, pełna integracja i pełny skład książki.**

Status **LOKALNIE STABILNY** odnosi się do historycznych rozdziałów 10–12
i do zakresu tego audytu. **Nie** oznacza ukończenia szczegółowego
audytu matematycznego wszystkich 44 rozdziałów.
Zielona kompilacja i testy skończonych grafów nie są formalną
weryfikacją w Lean ani poświadczeniem wszystkich twierdzeń.

Klasyczne twierdzenie **Jordana–Schönfliesa** jest jawnie przyjętą
przesłanką topologiczną dla lematów o ścianach i sklejaniu
osadzeń. Nie jest wyprowadzane w rozdziale 10; dowód jest
samodzielny na poziomie twierdzeń grafowych,
ale nie jest autonomicznym dowodem całej topologii płaszczyzny.

## Commity i artefakty

- [4361c8b58c8228c56822a7bfb93bfd47d127321a](https://github.com/dariusz-piekarz/mathematical_scipts/commit/4361c8b58c8228c56822a7bfb93bfd47d127321a): nowy łańcuch lematów, oba kierunki Kuratowskiego, pełny dowód Wagnera i testy wyczerpujące;
- [09c14c310b34968eefb950d952e776bc5a58e859](https://github.com/dariusz-piekarz/mathematical_scipts/commit/09c14c310b34968eefb950d952e776bc5a58e859): dostosowanie starszej regresji, która przedtem błędnie wymagała, by kierunek Kuratowskiego był tylko cytowany, a nie udowodniony;
- [8709549d8166f8a03ed658b0f632877b79fe9c0a](https://github.com/dariusz-piekarz/mathematical_scipts/commit/8709549d8166f8a03ed658b0f632877b79fe9c0a): niezależne doprecyzowanie implikacji użytej w Wagnerze i wskazanie metody Thomassena.

Główne źródło:
\`chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex\`.
Nowa sekcja \`sec:tg-kuratowski-full-proof\`
po łatwym kierunku Kuratowskiego i przed twierdzeniem Wagnera.

## Audyt matematyczny — cały łańcuch implikacji

1. **Definicja modelu minora**: wierzchołkom celu odpowiadają parami rozłączne niepuste, spójne zbiory pierwotnych wierzchołków; dla każdej krawędzi celu istnieje oryginalna krawędź między odpowiednimi zbiorami. Wykazano równoważność tej definicji z usuwaniem i kontrakcją (\`lem:tg-kuratowski-model-minor\`).
2. **Trzy/cztery etykiety w drzewie**: analizowano rozdział etykiet przez krawędzie i orientację ku części z większością etykiet. Jeżeli brak rozdzielenia \`2+2\` dla czterech etykiet, istnieje środek z parami wewnętrznie rozłącznymi ścieżkami do etykiet (\`lem:tg-kuratowski-tree-terminals\`).
3. **Minor → subdywizja**: dla \`K_{3,3}\` środek istnieje we wszystkich sześciu zbiorach rozgałęzienia i daje bezpośrednio subdywizję. Dla \`K_5\` otrzymuje się albo subdywizję \`K_5\`, albo podział etykiet \`2+2\`, który tworzy sześć zbiorów modelu \`K_{3,3}\`. Nie pominięto sytuacji, w której kilka etykiet leży na jednym wierzchołku.
4. **Dziedziczenie przez minory**: gdy \`G\` nie ma obydwu zabronionych subdywizji, każdy jego minor ma tę samą własność. Użyto przechodniości relacji minorowej i punktu 3, bez kolistego użycia Kuratowskiego lub Wagnera.
5. **Trójspójność i separator trzech wierzchołków**: wykazano, że każdy wierzchołek rozcinającego zbioru trójelementowego ma sąsiada w każdej składowej po jego usunięciu. Pozwala to przeprowadzić argument minimalnej składowej dla krawędzi, której kontrakcja zachowuje trójspójność (\`lem:tg-kuratowski-contractible-edge\`).
6. **Sklejanie**: wyjaśniono gluing planarnego osadzenia po rozcięciu przez jeden lub dwa wierzchołki; w drugim przypadku dodaje się pomocniczą krawędź \`xy\`, ustawia dwa osadzenia po przeciwnych stronach tej krawędzi i usuwa duplikat lub pomocniczą krawędź.
7. **Obwód ściany**: dla dwuspójnego grafu płaskiego granica ściany jest cyklem prostym, a obszar ograniczony cyklem umożliwia poprowadzenie rozłącznych dróg od nowego wierzchołka do wybranych punktów brzegu. W tym kroku zastosowano jawnie wskazane twierdzenie Jordana–Schönfliesa; nie zakładano z góry Kuratowskiego.
8. **Minimalny kontrprzykład**: minimalizując \`|V|+|E|\`, wykluczono rozspójnienie i separatory jedno- i dwuwierzchołkowe, korzystając z mniejszych grafów oraz lematu o sklejaniu. Następnie skurczono krawędź zachowującą trójspójność, otrzymując mniejszy graf planarny, i rozpatrzono jego ścianę po usunięciu skurczonego wierzchołka.
9. **Pełna alternatywa na cyklu**: sąsiedztwa \`X=N(x)\\{y}\` i \`Y=N(y)\\{x}\` leżą na cyklu \`C\`. Jeżeli \`Y\` mieści się między dwiema kolejnymi pozycjami \`X\`, można wstawić \`y\` i otrzymać osadzenie. Jeżeli \`|X∩Y|≥3\`, powstaje model \`K_5\`. W pozostałym przypadku istnieją cztery różne, cyklicznie naprzemienne pozycje \`Y-X-Y-X\`, co daje dziewięć parami wewnętrznie rozłącznych dróg subdywizji \`K_{3,3}\`: cztery łuki cyklu i pięć krawędzi wychodzących z \`x,y\`. Te trzy możliwości wyczerpują konfiguracje.
10. **Wagner**: po zamknięciu dowodu Kuratowskiego dodano osobne środowisko \`proof\`. Planarność jest zachowana przez minory; odwrotnie każda zabroniona subdywizja daje po kontrakcji odpowiedni minor. Nie wykorzystano Wagnera jako wcześniejszej przesłanki.

Wszystkie wskazane kroki zostały ponownie przeczytane niezależnie od testów, w szczególności poprawiono uzasadnienie kierunku \`subdywizja ⇒ minor\` w dowodzie Wagnera.

## Niezależna enumeracja skończonych przypadków

Nowy test:
\`tools/tests/test_graph_and_knot_kuratowski_proof.py\`.

[Globalny audyt — końcowy GitHub Actions 45172221255](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45172221255):
\`structural-audit=success\`, \`full-book-pdf=success\`.

Wcześniejszy przebieg po aktualizacji starszej regresji:
[45171576059](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45171576059)
również potwierdził sukces testów i 268-stronicowego PDF.
Przebieg [45171385449](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45171385449)
miał niepowodzenie strukturalne **niezwiązane z błędem twierdzenia**:
stary test zakładał, że w rozdziale istnieje tekst
„Przyjmujemy ją tutaj jako klasyczne twierdzenie”,
usunięty podczas wprowadzenia dowodu.
Regresję zastąpiono warunkiem wymagającym obecności
wszystkich kluczowych lematów i nowego dowodu.

W świeżym CI potwierdzono:
- **33 867** wszystkich etykietowanych grafów prostych do sześciu wierzchołków (w tym **1795** trójspójnych), z niezależnym sprawdzeniem zabronionych minorów i subdywizji, lema trójspójności i kontrakcji;
- **79 455** par zbiorów sąsiedztwa \`X,Y\` na cyklu długości 4–8, z wyczerpującą kontrolą alternatywy (wspólny łuk / trzy wspólne sąsiedztwa / naprzemienne końce);
- **99 220** konfiguracji trzech i czterech etykiet na wszystkich małych oznaczonych drzewach do pięciu wierzchołków, z niezależną kontrolą rozcięcia \`2+2\` lub istnienia środka;
- wszystkie wcześniejsze testy 01–12, w tym Tutte, Hall, Menger, planarność, nakrycia i Kirchhoff — sukces.

Testowanie skończonych rozmiarów nie zastępuje matematycznego argumentu dla każdego \`n\`.

## Finalny PDF — fizyczna kontrola

Pobrano artefakt \`graph-and-knot-complete-book-audit\`
z [przebiegu 45172221255](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45172221255).
- Książka ma **268 stron A4**;
- wykonano **trzy pełne przebiegi** \`pdflatex\` w CI;
- \`graph_and_knot_full_warnings.txt\` ma **0 wierszy**;
- brak \`LaTeX Warning\`, \`Package Warning\`,
  \`Overfull\` i \`Underfull\` w końcowym logu;
- skontrolowano renderowane strony PDF 101–111,
  w tym cały nowy dowód Kuratowskiego na stronach 103–108,
  dowód Wagnera i dalsze sekcje;
- nie wykryto obciętych wzorów ani
  istotnych kolizji rysunków/podpisów,
  a nowy blok mieści się płynnie w składzie
  bez pustych stron powodowanych przez nową sekcję.

Inne kontrole dla końcowej zmiany:
- [Polish mathematical terminology — 45172221217](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45172221217): **success**;
- [Graph and knot theory — algorithms — 45172221518](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45172221518): **success**;
- [Mathematical library application checks — 45172221275](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45172221275): **success**.

## Status i dalsza kolejność

- **Historyczne rozdziały 10–12: lokalna stabilizacja w zakresie
  szczegółowego audytu i nowych testów — PASS.**
- Poprzednia otwarta pozycja „brak dowodu kierunku \`(ii)⇒(i)\`
  Kuratowskiego” jest teraz **zamknięta w tekście**, lecz
  dowód nadal opiera się na standardowym topologicznym
  twierdzeniu Jordana–Schönfliesa.
- **Globalny audyt wszystkich 44 rozdziałów: w toku**.
- Następny blok: historyczne **13–15**, przy zachowaniu
  zasady sprawdzania każdego istotnego kroku dowodowego,
  diagramów, definicji, odsyłaczy, testów i całego PDF.
