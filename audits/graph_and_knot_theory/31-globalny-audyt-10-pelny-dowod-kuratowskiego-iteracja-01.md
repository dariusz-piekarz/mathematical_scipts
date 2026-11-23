# Teoria grafów i węzłów — globalny audyt 10: pełny dowód Kuratowskiego, pierwsza iteracja

Data: 2026-11-23. Repozytorium: \`dariusz-piekarz/mathematical_scipts\`,
gałąź: \`biblioteka-matematyczna-iteracja-6\`.

**Status przed CI: opracowano pełny łańcuch dowodowy, wymaga niezależnej walidacji matematycznej, testów i składania PDF.**
Nie stanowi to jeszcze poświadczenia formalnego w Lean ani końcowego audytu rozdziału.

## Zamykana luka

W audycie 09 (\`30-globalny-audyt-09-rozdzialy-10-12-testy-pdf-i-luka-kuratowskiego.md\`)
pozostawiono otwartą odwrotną implikację:
graf prosty bez podgrafu będącego subdywizją \`K_5\` i \`K_{3,3}\`
jest planarny. Przed tą iteracją tekst zawierał tylko
łatwą implikację oraz odsyłał do źródeł klasycznych.
Nie wolno było na tej podstawie przyznawać statusu
matematycznej stabilizacji rozdziału 10.

## Wprowadzone pełne argumenty matematyczne

W \`10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex\`
umieszczono odrębną sekcję
\`sec:tg-kuratowski-full-proof\`, zawierającą:

1. \`lem:tg-kuratowski-model-minor\`: dowód równoważności
   modelu minora przez rozłączne spójne zbiory rozgałęzienia
   i operacji usuwania/kontrakcji.
2. \`lem:tg-kuratowski-tree-terminals\`: lemat o trzech lub
   czterech etykietach na drzewie; alternatywa centrum,
   od którego wychodzą wewnętrznie rozłączne drogi,
   albo podziału czterech etykiet na \`2+2\`.
3. \`lem:tg-kuratowski-minor-to-subdivision\`: pełne przejście
   od \`K_{3,3}\`-minora do subdywizji \`K_{3,3}\`
   i od \`K_5\`-minora do subdywizji \`K_5\`
   lub \`K_{3,3}\`, z jawną konstrukcją
   sześciu zbiorów modelu w przypadku \`2+2\`.
4. \`cor:tg-kuratowski-minor-heredity\`:
   dziedziczenie braku zabronionych
   subdywizji przez minory.
5. \`lem:tg-kuratowski-threecut\` i
   \`lem:tg-kuratowski-contractible-edge\`:
   dowód istnienia kontrakcji zachowującej
   trójspójność w każdym grafie trójspójnym
   innym niż \`K_4\`, z minimalizacją
   wielkości składowej po rozcięciu przez
   trzy wierzchołki.
6. \`lem:tg-kuratowski-gluing\`:
   sklejanie osadzeń sferycznych przy
   separatorze o jednym lub dwóch końcach
   za pomocą pomocniczej krawędzi.
7. \`lem:tg-kuratowski-face-cycle\`:
   granica ściany grafu dwuspójnego jako
   cykl i wstawianie nowego wierzchołka
   wraz z łukami do punktów cyklu.
8. Dowód przez najmniejszy
   kontrprzykład względem \`|V|+|E|\`:
   wykluczenie separatorów 0-,1- i
   2-wierzchołkowych, kontrakcja
   trójspójnego grafu, wybór cyklu
   ograniczającego ścianę, a następnie
   pełne rozpatrzenie trzech możliwości
   dla sąsiedztw \`X,Y\` po rozszczepieniu
   skurczonego wierzchołka:
   wspólny łuk umożliwia osadzenie;
   trzy wspólne końce dają minor \`K_5\`;
   naprzemienne końce dają subdywizję \`K_{3,3}\`.
9. Samodzielny dowód kryterium Wagnera
   jako konsekwencji pełnego Kuratowskiego
   i lematu o minorach (bez błędnego
   utożsamiania obu relacji dla dowolnych grafów).

Jako niezależny głęboki fakt topologiczny
przyjęto twierdzenie Jordana–Schönfliesa.
Nie użyto kryterium Wagnera do dowodu
Kuratowskiego, co zapobiega kolistości.

## Nowe testy regresyjne

W \`tools/tests/test_graph_and_knot_kuratowski_proof.py\`
dodano niezależne kontrole:

- całkowitą enumerację grafów prostych do 6 wierzchołków
  i równoważność zabronionych minorów oraz subdywizji,
  obliczaną różnymi algorytmami;
- dla wszystkich trójspójnych grafów w tym zakresie:
  istnienie kontraktowalnej krawędzi poza \`K_4\`
  i sąsiedztwo każdego wierzchołka trójseparatora
  z każdą składową po usunięciu separatora;
- kombinatoryczne wyczerpanie trzech przypadków
  rozłożenia dwóch zbiorów sąsiadów \`X,Y\` na cyklu,
  bez korzystania z planarności;
- cztero- i trójetykietowe warianty lematu drzewnego
  sprawdzone dla wszystkich małych drzew i wszystkich
  umiejscowień etykiet;
- integrację pełnego dowodu w istniejącym rozdziale 10.

Nowy test jest obowiązkowym krokiem istniejącego
\`graph-and-knot-global-audit.yml\`. Zachowano
historyczne testy 01–12, pełny skan struktury 44
rozdziałów i trzykrotną kompilację całej książki.

## Wymagania drugiej iteracji

- Potwierdzić poprawność obliczeń w nowym teście,
  w tym etykietowanie w modelu \`K_5\` i
  dopełnienie ścieżek w subdywizji \`K_{3,3}\`.
- Niezależnie ponownie przejść przez krok
  minimalnego trójseparatora i wszystkie trzy
  przypadki cyklicznych porządków.
- Obejrzeć PDF obejmujący nową, istotnie
  dłuższą sekcję, z uwagą na podziały stron,
  przypadkowe puste strony i czytelność wzorów.
- Zatwierdzić pełny CI i status stabilizacji
  dopiero po rzeczywistych wynikach,
  nie na podstawie samej edycji źródła.
