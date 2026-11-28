# Teoria grafów i węzłów — audyt globalny 06: rozdziały 07–09, iteracja 01

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
**Status: W TRAKCIE — pierwsza iteracja matematyczna, pełna weryfikacja CI i PDF jeszcze wymagana.**

## Zakres dowodów skontrolowanych niezależnie

### Rozdział 07: graf jako przestrzeń topologiczna

1. Lematu o zwinięciu kontraktowalnego podkompleksu CW użyto przy
   parze mającej własność przedłużania homotopii. Nie rozciągano
   bezpodstawnie tej tezy na dowolne kontraktowalne podzbiory.
2. Dla spójnego grafu z \`n\` wierzchołkami i \`m\` krawędziami
   zwinięcie drzewa rozpinającego daje bukiet \`m-n+1\` okręgów.
   Dowód \`pi_1(|G|)=F_{m-n+1}\` wykorzystuje twierdzenie van Kampena.
3. Konstrukcja nakrycia uniwersalnego ze zredukowanych spacerów ma
   jednego poprzednika dla niepustego spaceru, przez co uzyskany
   graf nie ma cykli i jest spójny. Warunek lokalnej bijekcji
   incydencji odpowiada warunkowi nakrycia.
4. Dla spójnego nakrycia \`d\`-kartkowego sprawdzono liczenie
   \`n_hat=dn\`, \`m_hat=dm\`, \`r_hat=1+d(r-1)\`.
   Dodano komentarz wyjaśniający przypadek bazowego drzewa
   (\`r=0\`): spójne nakrycia stopnia \`d>1\` nie istnieją.
5. Metryka długości ma na wierzchołkach te same odległości
   co kombinatoryczna najkrótsza ścieżka.

### Rozdział 08: Laplasjan, Hodge i Kirchhoff

1. Dodatniość wag gwarantuje dodatnią półokreśloność
   \`L=BWB^T\`, a jądro stanowią funkcje stałe na
   każdej składowej. W zagadnieniu Dirichleta
   warunek przecięcia każdej składowej przez brzeg
   gwarantuje dodatnią określoność ograniczonego bloku.
2. Laplasjany \`BB^T\` i \`B^TB\` mają identyczne
   dodatnie wartości własne z krotnościami.
   Harmoniczne reprezentanty \`H^1\` wynikają z
   ortogonalnego rozkładu przestrzeni kołańcuchów.
3. W dowodzie twierdzenia macierzowo-drzewowego
   kontrolowano dobór \`n-1\` kolumn macierzy incydencji,
   zastosowanie Cauchy'ego–Bineta oraz przypadki:
   cykl daje wyznacznik zero, drzewo daje \`±1\`.
4. Wzór spektralny \`tau(G)=prod(lambda_2,...,lambda_n)/n\`
   skontrolowano przez dodanie macierzy \`11^T/n\`
   i własności macierzy dopełnień algebraicznych.
5. W twierdzeniu Thomsona
   \`j_0=WB^Tf\` realizuje żądaną dywergencję,
   a różnica z dowolnym innym prądem jest cyklem,
   ortogonalnym do gradientu w metryce energii.
6. Utrzymano wyraźne rozróżnienie Laplasjanu
   kombinatorycznego i znormalizowanego
   przez czynnik \`d\` w grafach \`d\`-regularnych.

### Rozdział 09: grafy planarne

1. Definicja osadzenia grafu w \`S^2\` opiera się
   na ciągłym różnowartościowym odwzorowaniu
   zwartej realizacji do powierzchni Hausdorffa.
2. Wzór Eulera \`n-m+f=1+c\` wynika z dodawania
   krawędzi: połączenie składowych zmniejsza \`c\`,
   zamknięcie cyklu rozcina ścianę.
3. Długości obchodów ścianowych sumują się do \`2m\`
   również przy mostach. Dla spójnych grafów prostych
   \`n>=3\` każde takie obejście ma długość co
   najmniej trzy, a dla grafów dwudzielnych co najmniej cztery.
4. Oszacowania \`m<=3n-6\` i \`m<=2n-4\`
   otrzymano z liczności ścian.
5. Dla spójnego osadzonego grafu o wszystkich parzystych
   stopniach klasy ścian można dwukolorować;
   parzystość przecięć z eulerowskim cyklem
   jest niezależna od drogi na sferze.

## Rzeczywiste znalezisko: kolizja notacji między rozdziałami

**Przed audytem** \`\\tau(G)\` oznaczało
w rozdziale 05 minimalną moc pokrycia
wierzchołkowego, natomiast w rozdziałach 08, 12 i 19
liczbę drzew rozpinających. Są to różne liczby.
**Poprawka:** w rozdziale 05 zastąpiono cztery
wystąpienia przez \`\\tau_V(G)\`, a w rozdziale 08
dodano definicyjną uwagę o rozróżnieniu.
Oznaczenia \`\\tau(G)\` dla drzew zachowano we
wszystkich dalszych twierdzeniach (Kirchhoff, Tutte, grafy Taita)
bez zmiany ich treści.

## Testy skończone

Nowy test
\`tools/tests/test_graph_and_knot_topology_laplacian_planarity.py\`
sprawdza niezależnie:
- budowę pokryć przez przesunięcia arkuszy dla
  wszystkich małych spójnych grafów i
  dwu-/trójkartkowych przykryć; lokalne bijekcje
  incydencji, składowe i wzór Nielsena–Schreiera;
- dokładne wyznaczniki zredukowanych Laplasjanów
  i pełną enumerację drzew rozpinających, również
  dla wag różnych od jedności;
- tożsamość \`det(L+11^T/n)=n tau(G)\`,
  dokładne opory efektywne, energię prądów i
  minimalizację energii Dirichleta;
- orientowalne osadzenia przez enumerację
  porządków cyklicznych półkrawędzi,
  wzór Eulera i ograniczenia planarne;
- planarne dwukolorowanie ścian grafów o
  parzystych stopniach oraz kontrprzykłady
  \`K_5\` i \`K_{3,3}\`.
- właściwe znaczenie \`\\tau_V(G)\`
  oraz unikalność oznaczeń w katalogu wszystkich
  44 źródeł.

Testy zostały dołączone do pełnego workflow globalnego,
obok wcześniejszych audytów 01–06.
Ostateczną ocenę matematyczną i składu zapisać
dopiero po zweryfikowaniu wyników świeżego CI.

## Otwarte warunki

Zebrać wyniki \`structural-audit\` i \`full-book-pdf\`,
skontrolować ewentualne niezgodności numeryczne i
kompilacyjne, obejrzeć wybrane rysunki w rozdziałach
07–09, a następnie ponowić regresję po wszystkich poprawkach.
Nie rozszerzać statusu stabilnego na nieaudytowane
jeszcze rozdziały 10–36.
