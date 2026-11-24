# AA-52 — audyt IX: niezależna kontrola półniezmienników przez podgrupy komutatorowe

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło bez zmian: blob de35380cb5208b32ebb1bbac165dd554d44228d9.

## Argument matematyczny
Dla skończonej grupy H oraz jej zespolonej reprezentacji W suma wszystkich jednowymiarowych podreprezentacji jest dokładnie W^[H,H]. Każdy charakter jednowymiarowy jest trywialny na podgrupie komutatorowej. Odwrotnie, podprzestrzeń wektorów ustalonych przez [H,H] jest H-niezmiennicza z normalności [H,H], a działanie na niej faktoryzuje się przez skończoną grupę abelową H/[H,H]. Jej reprezentacje zespolone rozkładają się na jednowymiarowe (komutujące diagonalizowalne macierze). Dla W=Sym^d((C²)^*) niezerowość tej przestrzeni jest zatem równoważna istnieniu półniezmiennika stopnia d. Jest to niezależna kontrola AA-52 bez korzystania z rachunku orbit na P¹. Nie dodajemy nowego zakresu do rozdziału.

## Wykonany test dokładny
Uruchomiono lokalnie Python/SymPy w ciałach QQ(sqrt(2)) i QQ(sqrt(5)). Z generatorów kwaternionowych z AA-52 wyznaczono przez BFS grupę H oraz zbiór wszystkich sprzężeń komutatorów generatorów. Domknięcie tego zbioru daje [H,H]: iloraz przez jego normalne domknięcie jest abelowy, a same komutatory należą do [H,H]. Sprawdzono też q q^(-1)=1 dla każdego elementu H.
Wyniki (rząd H, rząd [H,H], rząd abelianizacji):
2T: (24,8,3); 2O: (48,24,2); 2I: (120,120,1).
Dla d=0,...,12 uśredniono po [H,H] dokładne wartości rekurencji s0=1, s1=t, s_d=t s_(d-1)-s_(d-2), t=2 Re(q). Jest to charakter potęgi symetrycznej naturalnej reprezentacji lub przestrzeni sprzężonej, ponieważ wartości własne są wzajemnie odwrotne. Wymiary:
- 2T: [1,0,0,0,2,0,1,0,3,0,2,0,4].
- 2O: [1,0,0,0,0,0,1,0,1,0,0,0,2].
- 2I: [1,0,0,0,0,0,0,0,0,0,0,0,1].
Wszystkie 39 wymiarów są całkowite i nieujemne, minima dodatnie wynoszą 4,6,12; asercje i kod wyjścia 0. Dla 2I brak nietrywialnych charakterów jednowymiarowych, zgodnie z tym, że półniezmienniki są niezmiennikami. Rachunek jest niezależny od dowodu orbitowego, lecz nie zastępuje dowodu ogólnego.
Ponownie sprawdzono, że źródło rozróżnia oba rodzaje wielomianów i nie wyciąga nieuzasadnionych wniosków o pełnym algorytmie Kovacica.

## CI
Run 45345253078, head 7f69140bb0f7c97f4ab46da89718269d3bcf9d31, job 138278146261. Ostatni odczyt: status in_progress, conclusion brak, rozkład kroków {"success":107,"in_progress":1,"pending":5}. Kontrole terminologii i aplikacji success zgodnie z VIII. Oględziny PDF tego bloba nadal niepotwierdzone.

## Werdykt
Drugi czysty przegląd matematyczny po VII, bez zmian źródła. AA-52 pozostaje W AUDYCIE do potwierdzenia końcowego CI i oględzin aktualnego PDF. AA-53 nieotwarty.
