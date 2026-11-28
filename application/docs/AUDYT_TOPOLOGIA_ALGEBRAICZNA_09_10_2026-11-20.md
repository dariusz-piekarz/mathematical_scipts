# Topologia algebraiczna — szczegółowy audyt rozdziałów AT-09 i AT-10

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Zakres:** dwa kanoniczne źródła: `chapters/pl/algebraic_topology/09-formy-rozniczkowe-orientacja-i-kohomologia-de-rhama.tex` i `10-homologia-i-kohomologia-c-echa-od-pokryc-do-granic-przestrzeni.tex`.  
**Kryteria:** poprawność matematyczna, wszystkie założenia, poziom szczegółowości DG-01, język polski, samodzielne przykłady/kontrprzykłady, rysunki, etykiety, zależności, faktyczna kompilacja PDF.

## 1. AT-09 — formy różniczkowe, orientacja i twierdzenie de Rhama

Przegląd objął lokalne formy różniczkowe i ich cofnięcia, działanie różniczki zewnętrznej, wzór Cartana, lemat Poincarégo, podziały jedności, orientację rozmaitości i brzegów, regularne poziomice, definicję całkowania, dowód Stokesa, przypadki Green–Gauss–Stokes, ciąg Mayera–Vietorisa oraz szczegółowy dowód twierdzenia de Rhama przez gładkie sympleksy i sklejanie kompleksów.

### Dodatki i korekty

1. **Globalna pierwotna dla 1-formy:** nowa samodzielna teza `thm:forma-okresy-pierwotna` podaje równoważność `ω=df` i znikania okresów po wszystkich kawałkami gładkich pętlach w spójnej gładkiej rozmaitości. Dowód w obie strony: rachunek przyrostów funkcji, niezależność całki od wyboru drogi przy zerowych okresach, lokalna gładkość funkcji `f(p)=∫_{p₀}^pω` oraz sprawdzenie `df=ω`. Dla formy zamkniętej na przestrzeni jednospójnej wyjaśniono dodatkowy wniosek przy użyciu homotopii.
2. **Kontrprzykład do odwrotnej implikacji `dω=0`:** forma kąta `(x dy-y dx)/(x²+y²)` na `R²\{0}` ma okres `2π` po okręgu, mimo że jest zamknięta i lokalnie dokładna. Nowy `prz:okres-1-formy-pierwotna`.
3. **Orientacja przy dwóch składowych brzegu:** na pierścieniu `A={1≤x²+y²≤4}` obliczono `d((x dy-y dx)/2)=dx∧dy`, `∫_A dα=3π`, `∫_{C₂}α=4π`, `∫_{C₁}α=-π`. Pokazano równocześnie, że zamknięta forma kąta ma wkłady `2π` i `-2π`, co daje zero po całym brzegu, ale nie dowodzi dokładności. Nowy `prz:stokes-pierscien-dwa-brzegi`.
4. **Ilustracja orientacji:** nowy `fig:stokes-pierscien` (samodzielny TikZ) oddziela kolorem i strzałkami orientacje brzegu zewnętrznego i wewnętrznego. W pierwszym przeglądzie 120-stronicowego PDF wykryto wizualne nachodzenie napisu `n_{wew}` na `dziura`; poprawiono położenie obu napisów osobnym commitem `024b0ea` i uruchomiono ponowną kompilację.
5. **Zachowane źródła:** nie zmieniono historycznych deklaracji `\label` ani istniejących dowodów de Rhama i Stokesa; dołączono dodatkowe wyniki i przykłady. Rozdział zachowuje szczegółowy dowód porównania kołańcuchów gładkich i ciągłych w twierdzeniu de Rhama, a nie jedynie jego sformułowanie.

## 2. AT-10 — homologia i kohomologia Čecha

Przeanalizowano nerwy pokryć, rozdrobnienia i przyległość odwzorowań symplicjalnych, granice odwrotne/proste, funktorialność, porównanie z teorią singularną na wielościanach, kolczyk hawajski, solenoid, otoczenia zwartych zbiorów w sferze i brak prawostronnej dokładności granic odwrotnych.

### Dodatki i korekty

1. **Lemat ciągłości Čecha:** nowy `lem:cech-ciaglosc-odwrotna` precyzuje hipotezy (niepuste zwarte wielościany i surjektywne mapy wiążące) i dowodzi `check H_n(lim P_j)=lim H_n(P_j)`, `check H^n(lim P_j)=colim H^n(P_j)`. Szczegółowo uzasadniono surjektywność rzutów, kofinalność pokryć od skończonych poziomów i izomorfizm ich nerwów wynikający z surjektywności projekcji.
2. **Kolczyk hawajski, bez ukrytego skoku:** w miejsce nieudowodnionej deklaracji o „kofinalnych nerwach” skonstruowano ciągłe odwzorowania zgniatające ogon okręgów, wykazano homeomorfizm z granicą skończonych bukietów i zastosowano poprzedni lemat. Wyprowadzono `check H_1(H;Z)=∏ Z` oraz dodatkowo `check H^1(H;Z)=⊕ Z`, objaśniając, dlaczego nieskończenie wiele współrzędnych pojawia się tylko w pierwszej z tych teorii.
3. **Kontrprzykład dla stopnia zero:** domknięcie wykresu `sin(1/x)` jest spójne, lecz ma dwie składowe łukowe: `H_0^{sing}(T;Z)=Z²`, `check H_0(T;Z)=Z`. Dla tej drugiej grupy udowodniono, że nerw każdego pokrycia otwartego spójnej przestrzeni jest spójny. Nowy `prz:cech-sinus-stopien-zero`.
4. **Solenoid:** obliczenie homologii i kohomologii ugruntowano w nowym lemacie ciągłości. Dodatkowy `prz:cech-solenoidy-2-3` odróżnia `Σ₂` i `Σ₃` za pomocą surjektywności mnożenia przez `2` na grupie `Z[1/p]` — w `Z[1/2]` jest surjektywne, w `Z[1/3]` nie.
5. **Brak prawostronnej dokładności — efektywny przykład:** nowy `prz:cech-lim-niedokladnosc`: z dokładnych ciągów `0→2^n Z→Z→Z/2^nZ→0`, kompatybilnych przez inkluzję/identyczność/redukcję, po granicy odwrotnej powstaje `0→0→Z→\Z_2`, gdzie ostatnia strzałka nie jest na. Nieprzeliczalność `\Z_2` wyjaśniono przez zgodne rozwinięcia binarne. Pokazuje to konkretną potrzebę pochodnego funktora `lim¹`.
6. **Rysunki:** `fig:cech-hawajski-granice` pokazuje kierunki strzałek w homologii i kohomologii, a `fig:cech-solenoid-stopnie` pokazuje układ okręgów z mapami stopnia `p`. Zastosowano w pełni samodzielny TikZ. Wykonano przegląd stron 118 i 119 wynikowego PDF; diagramy są czytelne.
7. **Terminologia:** wymieniono polskie użycia słowa „mapa” w znaczeniu mapping na „odwzorowanie”, zachowując symbol `\mapsto` i termin mapy tylko dla układów współrzędnych.

## 3. Integralność i weryfikacja

- Historyczne etykiety i odsyłacze nie zostały przepisane. W AT-01–10 nie występują duplikaty nazw `\label`. **W AT-09 i AT-10 występuje łącznie 68 wywołań standardowych `\ref/\eqref`, wszystkie mają cele w AT-01–10.**
- AT-09 ma 6, a AT-10 2 rysunki TikZ po zmianach. Brak nowych zależności od zewnętrznych grafik, podprogramów i plików danych. Dokument nadal używa kanonicznych rozdziałów przez `\input` w `books/pl/algebraic_topology.tex`.
- Nowe regresje: `application/tests/test_topology_chapters_09_10.py` — historia etykiet, odsyłacze, środowiska, terminologia, rachunek Stokesa, kryterium pierwotnej, arytmetyka solenoidu, konstrukcja granic i efekt torsji.
- Nowy workflow `.github/workflows/algebraic-topology-audit-ch09-10.yml` dwukrotnie kompiluje AT-01–10 i sprawdza niezdefiniowane cytowania, błędy TeX oraz przepełnione wiersze.
- **Pierwszy potwierdzony retest:** [testy aplikacji i Chromium #44768936571](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44768936571) — **SUCCESS**, 158 testów Pythona (1 pominięty), Chromium zaliczone, 355 rozdziałów w indeksie; [LaTeX #44768985261](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44768985261) — **SUCCESS**, 120 stron, dwa przebiegi bez niezdefiniowanych odsyłaczy i przepełnionych wierszy.
- Po korekcie terminologicznej oddzielnie **SUCCESS**: [aplikacja #44769379324](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44769379324), [LaTeX #44769379320](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44769379320).
- **Końcowy retest po korekcie rysunku:** [LaTeX #44769864938](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44769864938) — **SUCCESS**, 120 stron, dwa przebiegi bez niezdefiniowanych odsyłaczy i przepełnionych wierszy; [aplikacja #44769864949](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44769864949) — **SUCCESS**, regresje i przeglądarka. Obejrzano finalny rysunek pierścienia na stronie 103: podpis normalnej i napis „dziura” nie nachodzą już na siebie. Sprawdzono wszystkie osiem ilustracji AT-09 (strony 93, 99, 101, 103, 106, 110) i AT-10 (oba na stronie 118).

## 4. Zakres nieobjęty zatwierdzeniem

Wykonano audyt dwóch wymienionych rozdziałów, nie pełnej książki. Szczegółowa formalna budowa pochodnego funktora `\varprojlim{}^1` oraz pełna dualność Aleksandra są zapowiedziane, nie zostały potajemnie uznane za udowodnione. Nie wykonywano globalnej deduplikacji ani scalania obcych skryptów.

**Kolejna partia:** AT-11 i AT-12 po dwie kolejne jednostki, z tym samym standardem dowodów DG-01, poprawkami źródeł, kontrolą wizualną i CI.
