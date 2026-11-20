# Topologia algebraiczna — szczegółowy audyt rozdziałów 01–02

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** wyłącznie kanoniczne pliki `chapters/pl/algebraic_topology/01-*.tex` i `02-*.tex`, bez scalania skryptów i bez zmian `main`.  
**Standard:** każdy istotny krok uzasadniony tak szczegółowo jak w DG-01; przykłady obliczone, a rysunki poprawne także po wyrenderowaniu. Nie oznacza audytu pozostałych rozdziałów AT.

## 1. Rozdział 01 — język i konstrukcje topologiczne

| Obszar | Stan przed audytem / ryzyko | Korekta |
|---|---|---|
| Spójność | Nieprecyzyjna składnia twierdzenia i brak nieintuicyjnego kontrprzykładu do odwrotnej implikacji | Poprawione sformułowanie; domknięty wykres `sin(1/x)` wraz z dowodem spójności i braku łukowej spójności |
| Ilorazy | Homeomorfizm ilorazu odcinka z okręgiem i ilorazu płaszczyzny z torusem podany bez pełnych sprawdzeń | Uzupełniono włókna odwzorowań, ciągłość, zwartość dziedziny i aksjomat Hausdorffa przeciwdziedziny |
| Twierdzenie pomocnicze | Używano faktu „ciągła bijekcja ze zwartej do Hausdorffa” bez wyjaśnienia | Dodano lemat i dowód: zwarte podzbiory Hausdorffa są domknięte, więc bijekcja jest odwzorowaniem domkniętym |
| Stożek, zawieszenie, smash | Sformułowanie „dobrze bazowane” bez wprowadzenia odpowiedniego pojęcia, niejednoznaczny zapis dwóch końców zawieszenia | Dookreślono relacje równoważności i wyraźnie oddzielono dwa punkty zawieszenia; konstrukcje opisano bez zbędnego założenia |
| Nierozdzielność | Czytelnik mógł błędnie przyjąć, że każdy iloraz jest Hausdorffa | Dodano kontrprzykład `R/(0,1)`, który nie spełnia nawet aksjomatu `T_1` |
| Zawieszenie i dysk | `ΣS^n≅S^{n+1}` bez dowodu, brak jawnego wzoru dla `D^n/∂D^n` | Dodano ciągłe bijekcje i dowody przez zwartość–Hausdorffa, wzór dysk–sfera w czytelnym środowisku `cases` |
| Przestrzenie rzutowe | Same definicje, brak elementarnych identyfikacji | Dowiedziono `RP^1≅S^1` i `CP^1≅S^2` z jawnymi odwzorowaniami |
| Retrakcja | Uwaga o równoważności homotopijnej uprzedzała wyniki późniejszych rozdziałów | Oddzielono bezpośrednie obliczenie od zapowiedzianej niezmienniczości grup homotopii i homologii |

Rysunki: `fig:sinus-topologa-top-intro` i `fig:torus-iloraz-top-intro`, wyłącznie TikZ; sprawdzono ich osobne wyrenderowanie. Podczas przeglądu wizualnego wykryto i usunięto nachodzący na rysunek podpis osi; powtórny render został obejrzany.

Zachowane oryginalne etykiety: `ch:wstep-topologia`, `def:topologia-ilorazowa`. Nowe etykiety mają osobne, opisowe nazwy i nie zastępują żadnej istniejącej.

## 2. Rozdział 02 — grupy, pierścienie, moduły, Tor i Ext

| Obszar | Znaleziona luka / nieścisłość | Korekta |
|---|---|---|
| Przykłady grup | „Zazwyczaj nieabelowe” nie precyzowało ograniczeń wymiaru | Wskazano dokładnie `S_m` dla `m≥3` i `GL_m(R)` dla `m≥2` |
| Iloczyn półprosty | Dowód łączności i wzoru na odwrotność pomijał rachunki | Rozpisano obie strony mnożenia trzech elementów i sprawdzono odwrotność z obu stron |
| Działania grup | Zbyt mało geometrii obliczeniowej | Dodano `D_4 ≅ (Z/4)⋊(Z/2)`, działanie na wierzchołkach, stabilizator rzędu 2 i rysunek symetrii kwadratu |
| Grupy wolne | Unikalność postaci zredukowanej była tylko domyślna | Dodano argument terminowania redukcji i zgodności dwóch konkurujących skreśleń |
| Relacje grupowe | Zwrot „zerowanie relacji” sugerował notację addytywną | Zastąpiono precyzyjnym warunkiem: obrazy relatorów są neutralne |
| Ciało | Definicja nie wykluczała pierścienia zerowego | Dodano jawne założenie, że pierścień jest niezerowy |
| Wolność modułu | Uzasadnienie `2R` nad `Z/4Z` odnosiło się tylko do skończonej rangi | Dowód przez injekcję kopii `R` dla każdego elementu bazy działa dla dowolnej rangi |
| Rozszczepienie ciągu | Implikacja z lewej retrakcji do rozkładu była zbyt skrótowa | Rozpisano sumę prostą, różnowartościowość i surjektywność ograniczenia `p|ker r` |
| Iloczyn tensorowy grup cyklicznych | Pominięta część argumentu o rzędzie i odwrotności | Zastosowano tożsamość Bézouta i jawne odwzorowanie dwuliniowe do `Z/gcd(m,n)Z` |
| Płaskość | Wcześniej dopuszczono nieprzemienne pierścienie i wyłącznie lewe moduły, co nie wystarcza do użytego iloczynu tensorowego | Wyraźnie ograniczono dany paragraf do przemiennego `R` |
| Projektywność implikuje płaskość | Duży przeskok przy sumach prostych i funktorze dokładnym | Dodano mapy dla `M⊗R^{(I)} ≅ M^{(I)}`, a następnie argument z rozkładu `F=P⊕Q` i jąder oraz obrazów |
| Niezależność prezentacji | Skrótowe wyjaśnienie funktorialności homotopii | Doprecyzowano obraz równania homotopii po zastosowaniu `-⊗B` i `Hom(-,B)` |
| Tor i Ext | Tylko symboliczny wzór dla modułu cyklicznego | Dodano obliczenie `Tor_1^Z(Z/12,Z/18)≅Z/6` i `Ext^1_Z(Z/12,Z/18)≅Z/6`, bez fałszywego utożsamienia funktorów |
| Terminologia | Występowało zabronione w polskich skryptach słowo oznaczające operację tworzenia iloczynu tensorowego | Zastąpiono nazwami „iloczyn tensorowy” i „funktor `-⊗_R N`” |

Rysunek: `fig:dihedral-top-algebra`, samodzielny TikZ. Podczas renderowania wykryto nieczytelny tor strzałki obrotu; poprawiono go i sprawdzono ponownie obraz. Zachowano istniejące etykiety `ch:algebra-abstrakcyjna-v5`, `thm:izo-grupy-v5`, `sec:tensor-algebra-v5`, `thm:tensor-uni-v5`.

## 3. Integralność, zakres i regresje

- Oba rozdziały nadal są wpięte przez istniejące `\input` w `books/pl/algebraic_topology.tex`, bez nowych zależności od obcych plików graficznych, danych ani kodu.
- Nowy zestaw `application/tests/test_topology_first_two_chapters.py` sprawdza oryginalne etykiety, ich unikalność w parze, obecność w książce, brak zewnętrznych zasobów w tych rozdziałach, poprawność liczbowych przykładów `D_4`, `Tor` i `Ext` oraz politykę nazewnictwa.
- Nowa praca CI `.github/workflows/algebraic-topology-audit-ch01-02.yml` składa **tylko** rozdziały 01 i 02 z właściwą preambułą książki, wykonuje dwa przebiegi `pdflatex` i kontroluje niezdefiniowane odsyłacze oraz przepełnione wiersze.
- Sprawdzono osobne kompilowanie trzech rysunków jako minimalnego dokumentu LaTeX i obejrzano wyrenderowane obrazy.
- Wszystkie głębokie twierdzenia wykorzystywane w dalszym tekście, np. niezmienniczość homologii i twierdzenie o podgrupach grup wolnych abelowych, pozostają zależnościami wprost nazwanymi lub zapowiedzianymi, a nie niezależnymi dowodami od zera.

## 4. Kryterium zakończenia audytu

Wynik końcowy wymaga równocześnie:
1. sukcesu regresji aplikacji (w tym nowych testów);
2. sukcesu dwukrotnej kompilacji PDF dwóch rozdziałów bez niezdefiniowanych cytowań ani `Overfull \hbox`;
3. zachowania etykiet, wszystkich wcześniejszych dowodów i przykładów;
4. braku nieocenionych kolizji w nowo dodanych rysunkach.

Nie twierdzimy, że dwurozdziałowy PDF dowodzi bezbłędności składu pełnych 31 rozdziałów. Nie przeprowadzono globalnej deduplikacji ani scalania skryptów.
