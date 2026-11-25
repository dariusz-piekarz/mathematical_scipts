# PDE-05 — iteracja 64: niezależny audyt 5.1–5.2

Data: 2026-11-25. Źródło chapters/pl/partial_differential_equations/05-rownanie-falowe.tex, blob 97d5fa77fa7282ceee6fbf924e77b28d788975f8. Rejestr regresyjny: blob dd58ee2123ea338f210476584868ede0a501efd6.

## Ponowna lektura matematyczna

- PDE-05-001–004: sprawdzono założenia wprowadzenia, rzeczywiste dane i jednostronne pochodne. Odwrotność współrzędnych charakterystycznych i czynnik -4c² są poprawne; przekroje półpłaszczyzny xi<eta są spójne, a funkcje a,b określone na całej prostej mają klasę C¹. Z wypukłości wynika stałość reszty po odjęciu funkcji pierwotnych. Przedłużenie do t=0 przez ciągłość, układ F',G', znikanie sumy stałych, orientacja całki H oraz jawne pochodne u_t,u_x,u_tt,u_xx prowadzą do równania i obu danych. Przykład danych h nieujemnych z nośnikiem w [-R,R] i t≥(|x|+R)/c jest poprawny, zależność od wnętrza odcinka nie jest utożsamiana z zależnością od jego końców.
- PDE-05-005: skończoność energii odróżniona od wspólnego zwartego nośnika pochodnych, stała kula zawiera K we wnętrzu, ograniczoność pochodnych na zwartym cylindrze uzasadnia różniczkowanie; wzór na dywergencję, znak wyrazu brzegowego i przypadek n=1 sprawdzone.
- PDE-05-006–007: reguła Leibniza z czynnikiem r^(n-1), r'=-c, oba ujemne wyrazy końcowe w n=1; e_t=c² div(u_t grad u), normalna zewnętrzna, ortogonalny rozkład gradientu i dopełnienie kwadratu z czynnikiem -c/2. Zerowy gradient zerowych danych w otwartej kuli, nieujemność gęstości i ciągłość uzasadniają E=0 punktowo; zagnieżdżenie kul i całkowanie po pionowym odcinku, ciągłość w wierzchołku.
- PDE-05-008–009: dodatkowa całka u_t f, Cauchy–Schwarz z czynnikiem sqrt(2E), ciągłość normy f przez skalowanie do kuli jednostkowej; regularizacja sqrt(E+delta), stała 1/sqrt(2), przejście delta↓0. Wzór eksponowany wprowadzony w iteracji 63 zachowuje nierówność. Zerowanie różnicy rozwiązań w każdym wierzchołku, również w przypadku zgodnych wymuszeń w stożku; bez założeń globalnej energii. Brak nowych istotnych luk.

Ponownie przeczytano 2/8 sekcji i wprowadzenie, źródło niezmienione. Nie jest to jeszcze pełny audyt stabilizacyjny.

## Kontrola techniczna

Wszystkie 10 plików wejściowych (rozdział 05, rozdziały 01 i 04, rejestr, test, workflow, księga, manifest, listings, preambuła Atlasu) mają identyczne bloby jak w commicie 55060b71c0f281d5aa343dfea4797423fe28f2f6. Sprawdzono 30 unikatowych etykiet, 26 wystąpień odsyłaczy, oba zewnętrzne cele występują dokładnie raz we właściwych rozdziałach, poprawne zagnieżdżenie środowisk, 34 kolejne ID i istniejące kotwice (32 semantyczne i 2 wizualne).

Przebieg 45567364891, job 139045324745: ostatni odczyt in_progress, testy wykonywalne i kontrola struktury success, kompilacja in_progress, diagnostyka i publikacja artefaktu pending. Nie ma jeszcze potwierdzenia przejścia kompilacji i diagnostyki po obu poprawkach. Nie dokonano nowych oględzin PDF, nie uruchomiono Lean ani pełnej kompilacji tomu. Rozdział pozostaje otwarty. Następnie kontrola końcowego wyniku CI i poprawionego renderu, niezależna lektura 5.3–5.5.
