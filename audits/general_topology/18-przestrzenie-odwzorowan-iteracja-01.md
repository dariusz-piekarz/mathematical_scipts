# Topologia ogólna — rozdział 18, audyt iteracja 01

Data: 2026-11-22. Gałąź: biblioteka-matematyczna-iteracja-6.

## Dodane źródło

Plik: chapters/pl/general_topology/18-przestrzenie-odwzorowan-i-topologia-zwarto-otwarta.tex.

Nowy rozdział obejmuje: definicję topologii zwarto-otwartej na C(X,Y); związki z topologią punktową; ciągłość składania z ustalonym odwzorowaniem; topologię zbieżności jednostajnej na zbiorach zwartych; jej zgodność z topologią zwarto-otwartą dla metrycznej przestrzeni wartości; charakterystykę zbieżności sieci; ciągłość ewaluacji przy lokalnej zwartości Hausdorffa dziedziny; prawo wykładnicze dla rodzin parametryzowanych; kontrprzykład braku ciągłości ewaluacji na Q; metrykę z wyczerpania zwartego, jej zgodność z topologią i zupełność przy zupełnej przestrzeni wartości; nieprzeliczalną przestrzeń dyskretną jako przykład braku pierwszego aksjomatu przeliczalności.

Wcześniejsze zależności: rozdział 7 (zwartość i Heine–Borel), rozdział 12 (struktury jednostajne i jednostajna ciągłość), rozdział 14 (otoczenia o zwartym domknięciu, wyczerpania zwarte oraz brak zwartych podzbiorów Q o niepustym wnętrzu).

## Pierwszy audyt matematyczny

1. **Topologia zwarto-otwarta**. Zbiory [K,U] dla zwartego K⊂X i otwartego U⊂Y określono jako podbazę, nie jako samodzielną bazę. Przecięcia skończone wyrażają jednoczesne warunki na obrazy kilku zwartych podzbiorów. Pusty K jest dopuszczony. Zbieżność punktowa pochodzi od ewaluacji na zwartych singletonach, a Hausdorffowość Y zapewnia Hausdorffowość C_k(X,Y).
2. **Składanie z ustaloną funkcją**. Przeciwobrazy [K,U] pod prekompozycją u* i postkompozycją v* obliczono jawnie jako [u(K),U] i [K,v^{-1}(U)]. Zwartość u(K) wynika z ciągłości, otwartość v^{-1}(U) z ciągłości v. Nie są potrzebne dodatkowe warunki na X.
3. **Topologia jednostajnej zbieżności na zwartych**. Zbiory B_K(f,ε) tworzą bazę otoczeń: przecięcia kontroluje zwarta suma K_1∪K_2, a przeniesienie otoczenia z f na g wykorzystuje maksimum ciągłej funkcji d(f,g) na zwartym K. Pusty K traktowany oddzielnie.
4. **Zgodność dwóch topologii**. Dla f(K)⊂U ze zwartym K funkcja odległości od domkniętego D=Y\U ma dodatnie minimum, co daje jednostajne otoczenie zawarte w [K,U]. W przeciwną stronę dla g∈B_K(f,ε) wybiera się margines δ=ε-max_K d(f,g)>0, skończone pokrycie g(K) kulami promienia δ/4 oraz zwarte K_j=K∩g^{-1}(closedball(y_j,δ/4)). Zbiory [K_j,ball(y_j,δ/2)] tworzą otoczenie g zawarte w B_K(f,ε), gdyż suma trzech odległości jest mniejsza niż m+3δ/4<ε. Nie używa się zwartości lokalnej X; dotyczy to dowolnej dziedziny topologicznej i metrycznej przestrzeni wartości.
5. **Sieci i górki uciekające**. Zbieżność sieci odczytano z bazy B_K(f,ε); dla funkcji max(1-|x-n|,0) na R wykazano znikanie na każdym ustalonym zwartym K przy n dostatecznie dużym, mimo niezanikającej globalnej normy supremum.
6. **Ewaluacja**. Dla lokalnie zwartej Hausdorffa X z lematu rozdziału 14 uzyskuje się x_0∈W⊂K⊂f_0^{-1}(V), gdzie K jest zwarty i W otwarty. Otoczenie [K,V]×W funkcji i punktu zostaje przekształcone w V. Wszystkie zmienne i warunki otwartości są jawne.
7. **Prawo wykładnicze**. Poprawiono sformułowanie, aby nie uważać Fhat:Z→C(X,Y) za określone przed sprawdzeniem ciągłości przekrojów F_z. Dla ciągłego F wykorzystuje się zwartość K i skończone podpokrycie prostokątami otwartymi do wykazania ciągłości Fhat na zbiorach podbazowych [K,U]. W przeciwną stronę wykorzystuje się ciągłość ewaluacji przy lokalnej zwartości Hausdorffa X i faktoryzację F=ev∘(Fhat×id_X). Twierdzenie stwierdza naturalną bijekcję zbiorów odwzorowań ciągłych, nie nieudowodniony dodatkowy homeomorfizm przestrzeni funkcji.
8. **Brak ciągłości ewaluacji na Q**. Zwarte podzbiory Q mają puste wnętrze (rozdział 14). Skończona suma zbiorów zwartych K_j użytych w bazowym otoczeniu funkcji zerowej ma więc puste wnętrze. Dla dowolnego otoczenia V⊂Q zera wybiera się r∈V\K i ciągłą funkcję g(q)=min(1,d(q,K)/d(r,K)), o ile K jest niepusty, albo g≡1 gdy K=∅. Funkcja g zeruje się na wszystkich K_j, ale g(r)=1, co dowodzi nieciągłości ewaluacji przy (0,0).
9. **Metryka z wyczerpania**. Dla X lokalnie zwartej, σ-zwartej i Hausdorffa rozdział 14 dostarcza wyczerpanie K_n i współkońcowość względem zbiorów zwartych. Pseudometryki ρ_n(f,g)=sup_{K_n} min(1,d(f,g)) są ograniczone, a ważona suma D(f,g)=∑2^{-n}ρ_n zbiega; ponieważ zbiory K_n pokrywają X, D oddziela funkcje. Zbieżność względem D jest równoważna jednostajnej zbieżności na każdym K_n, a współkońcowość daje zbieżność na każdym zwartym K.
10. **Zupełność**. Ciąg Cauchy'ego w D jest jednostajnie Cauchy'ego na każdym K_n; zupełność Y daje granicę punktową f. Jednostajna zbieżność na K_n i pokrycie X wnętrzami K_n dowodzą ciągłości f w każdym punkcie. Następnie D(f_j,f)→0. Nie wymaga się metryzowalności dziedziny X.
11. **Nieprzeliczalna dyskretna X**. Zwarte podzbiory są skończone, więc C_k(X,R)=R^X z topologią produktową. Każde otoczenie podstawowe ogranicza skończenie wiele współrzędnych; dla hipotetycznej przeliczalnej bazy otoczeń przy funkcji zerowej wybiera się współrzędną poza przeliczalną sumą tych zbiorów, co prowadzi do sprzeczności. To rzeczywiście pokazuje brak pierwszego aksjomatu przeliczalności i metryzowalności.

## Integracja

Dodano books/pl/general_topology_ch18.tex, wpis w books/pl/general_topology.tex, wpis katalogu catalog/books.json i status w docs/pl/plan_topologii_ogolnej.md. Test tools/tests/test_general_topology_ch17.py nie wymaga już dokładnie 17 rozdziałów. Nowy tools/tests/test_general_topology_ch18.py sprawdza 19683 trójek funkcji skończonych dla ważonej metryki, modele uciekających górek, rozdział, etykiety, symbole, odsyłacze i terminologię. Workflow .github/workflows/general-topology-chapter.yml wykonuje test 18 oraz kompiluje pełną książkę i samodzielny rozdział 18.

## Stan pierwszej iteracji

| Kryterium | Status |
| --- | --- |
| Definicje, twierdzenia i szczegółowe dowody | PASS — pierwszy audyt |
| Istotne przykłady i kontrprzykłady | PASS — pierwszy audyt |
| Zgodność zależności z rozdziałami 12 i 14 | PASS |
| Katalog, pliki główne i regresja rozdziału 17 | Wdrożono |
| CI, logi i wizualne oględziny PDF | **PASS — run 45015732921; PDF 5 stron A4** |
| Decyzja | W AUDYCIE — wymagana dalsza niezależna iteracja |

Źródła kontrolne: Munkres, Topology, rozdział o przestrzeniach funkcji; wykłady „Background on function spaces” (University of California Riverside); podręcznikowa własność prawa wykładniczego dla lokalnie zwartych przestrzeni Hausdorffa. Nie powielano fragmentów źródeł; dowody zapisano samodzielnie.


## Końcowa kontrola techniczna audytu 01

Przebieg GitHub Actions [45015732921](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45015732921) dla pełnego źródła i testu rozdziału 18 zakończył się completed/success. Osobno potwierdzono zielone kroki: Verify Chapter 18 compact-open topology and mapping spaces, Build complete book PDF, Build standalone Chapter 18 PDF i Check PDF and LaTeX log.

Artefakt 14751384112 pobrano i rozpakowano do katalogu /mnt/data/topologia18_audyt01. Samodzielny general_topology_ch18.pdf ma **5 stron A4**. Wyrenderowano wszystkie strony i obejrzano je, także przejścia między sekcjami o ewaluacji, prawie wykładniczym i metryce z wyczerpania. Tekst, wzory, numeracja i odsyłacze są czytelne, bez kolizji i ucięć. W logach general_topology_ch18.log oraz general_topology.log nie występują Overfull, Underfull, Missing character, LaTeX Warning, Undefined control sequence ani Fatal error.

**Werdykt audytu 01:** rozdział napisany, zintegrowany i zweryfikowany technicznie; pierwszy audyt matematyczny PASS. Nie oznaczać stabilności przed niezależną ponowną kontrolą nowego materiału w audycie 02.
