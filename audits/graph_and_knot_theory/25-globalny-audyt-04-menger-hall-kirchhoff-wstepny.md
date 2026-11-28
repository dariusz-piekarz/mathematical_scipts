# Teoria grafów i węzłów — audyt globalny 04: rozdziały 04–06

Data: 2026-11-23.
Gałąź: \`biblioteka-matematyczna-iteracja-6\`.
**Status: audyt matematyczny pierwszej iteracji — oczekuje na CI.**
Kontrola dotyczy trzech historycznych plików źródłowych, nie wszystkich
44 rozdziałów naraz.

## Zakres merytoryczny i metoda kontroli

### Rozdział 04 — Menger, separatory i przepływy

Zweryfikowano definicje lokalnych separatorów krawędziowych i
wierzchołkowych, odróżnienie par sąsiadujących i niesąsiadujących,
całkowitoliczbowość pojemności w użytej wersji Forda–Fulkersona,
oraz argument przepływu maksymalnego i przekroju minimalnego.
Przy dowodzie krawędziowej wersji Mengera sprawdzono
redukcję do przeciwnych łuków pojemności jeden, skasowanie
przeciwstawnego przepływu i dekompozycję przepływu
na jednostkowe ścieżki. Wersja wierzchołkowa
wykorzystuje łuki \`v^-→v^+\` pojemności jeden
i łuki sąsiedztwa pojemności \`M=|V|+1\`;
w założeniach wyraźnie zabroniono bezpośredniej krawędzi \`st\`,
aby rzeczywiście istniał separator nieobejmujący końców.
Sprawdzono dowód obu nierówności Whitneya
\`kappa(G)<=lambda(G)<=delta(G)\`, w tym przypadek grafów pełnych.

### Rozdział 05 — Hall, Berge, Kőnig, Dirac, Ore

Zweryfikowano konieczność i oba przypadki indukcji Halla:
ścisłą nierówność dla właściwych niepustych zbiorów
oraz rozkład przy przypadku równości.
Skontrolowano konstrukcję deficytu Halla przez
dodanie \`d\` uniwersalnych wierzchołków po prawej.
W dowodzie Kőniga sprawdzono kierunek ścieżek
naprzemiennych i fakt, że osiągalne wierzchołki prawej
części muszą być skojarzone.
Przeanalizowano dowód Bergego przez składowe
\`M△N\` oraz argument rotacji najdłuższej ścieżki
w twierdzeniach Diraca i Ore'a.

**Znalezisko redakcyjne:** historyczna końcowa sekcja
zapowiadała bezpośrednio przejście do algebry liniowej,
podczas gdy rzeczywista kolejność wydruku po rozdziale 05
prowadzi przez nowe moduły BFS/DFS, przepływów,
grafów losowych i ekspanderów, dopiero potem do rozdziału 06.
Zaktualizowano ten opis, podając jawne odsyłacze.

### Rozdział 06 — incydencja, cykle i przekroje

Sprawdzono łańcuchy całkowite i rachunek brzegu,
rząd macierzy incydencji \`n-c\` także dla
grafów niespójnych, bazy homologii pierwszej
z cykli fundamentalnych oraz \`H_0≅Z^c\`.
Sprawdzono \`ker B_2=C(G)\`,
\`im B_2^T=D(G)=C(G)^perp\`
oraz subtelność, że nad \`F_2\` ortogonalność
nie oznacza automatycznie sumy prostej.
Zanalizowano rzeczywisty rozkład ortogonalny
\`R^E=im B^T ⊕ ker B\`.

**Znalezisko zależności:** rozdział 43 omawia Laplasjan
\`I-A/d\` jeszcze przed historycznym rozdziałem 08
o Laplasjanie kombinatorycznym \`D-A\`.
W rozdziale 08 dodano jednoznaczną uwagę:
dla grafu \`d\`-regularnego z \`d>=1\`
zachodzi \`D-A=d(I-A/d)\`;
dla \`d=0\` normalizacja nie jest określona.
Nie usunięto żadnego z dwóch istotnych ujęć.
Wprowadzenie rozdziału 06 wyjaśnia tę kolejność źródeł.

## Nowy niezależny test skończonych modeli

Plik \`tools/tests/test_graph_and_knot_advanced_foundations.py\`:

1. Dla wszystkich grafów prostych o 2–5 wierzchołkach
   niezależnie enumeruje ścieżki \`s,t\` i wszystkie
   potencjalne separatory oraz porównuje liczby Mengera
   krawędziowe i wierzchołkowe. Ta druga kontrola
   jest ograniczona do nieprzyległych końców.
2. Niezależnie enumeruje usunięcia krawędzi i
   wierzchołków i weryfikuje nierówności Whitneya.
3. Dla małych grafów dwudzielnych (obie części mają
   od 1 do 3 wierzchołków) oblicza maksymalne skojarzenia,
   minimalne pokrycia, deficyt Halla i szuka ścieżek
   powiększających dla różnych skojarzeń.
4. Wyznacza cykle Hamiltona przez enumerację
   permutacji i sprawdza kryteria Diraca i Ore'a.
5. Macierz incydencji ma osobno obliczany rząd
   nad \`Q\` i \`F_2\`. Sprawdza
   liczbę cyklomatyczną, wszystkie przestrzenie
   cykli i cięć, wzajemne anihilatory, tożsamość
   energetyczną i całkowite fundamentalne cykle
   z zerowym brzegiem.

Nowy test jest dołączony do globalnego CI,
zachowującego również niezależne testy rozdziałów
01–03 i trzykrotną kompilację pełnej książki.

## Warunki zamknięcia

Po zatwierdzeniu zmian należy sprawdzić w CI:
- powodzenie nowych modeli skończonych, z dokładnymi licznikami;
- poprzednie regresje, zgodność katalogu 44 źródeł;
- trzy przebiegi pełnej kompilacji LaTeX bez ostrzeżeń i przepełnień;
- przy nowych odsyłaczach brak referencji niezdefiniowanych;
- artefakt pełnego PDF, zwłaszcza redakcyjne połączenia
  rozdziałów 05→37 i 43→06→08.

**Nie nadawać rozdziałom statusu ustabilizowanych,
jeśli którykolwiek z tych warunków pozostanie otwarty.**
