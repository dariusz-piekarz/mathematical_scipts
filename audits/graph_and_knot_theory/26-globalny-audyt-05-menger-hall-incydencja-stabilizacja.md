# Teoria grafów i węzłów — audyt globalny 05: rozdziały 04–06

Data: 2026-11-23. Gałąź: \`biblioteka-matematyczna-iteracja-6\`.

**WYNIK: PASS dla audytowanego bloku historycznych rozdziałów 04–06
w zakresie dowodów, testów skończonych i lokalnej integracji.**

**GLOBALNY AUDYT 44 ROZDZIAŁÓW NADAL TRWA.**
Zielone CI i brak znalezionego kontrprzykładu nie stanowią formalnego
poświadczenia poprawności każdego dowodu dla dowolnego grafu.

## Źródła i kontrolowane commity

Zmiany merytoryczne i testy:
[bbd2f12b504bf752426e1229a4f4b4d49f3974da](https://github.com/dariusz-piekarz/mathematical_scipts/commit/bbd2f12b504bf752426e1229a4f4b4d49f3974da).

Korekta niezależnej kompilacji fragmentu:
[81b9c61be2961cc4c37edee34bcb294791ee11a8](https://github.com/dariusz-piekarz/mathematical_scipts/commit/81b9c61be2961cc4c37edee34bcb294791ee11a8).

Audyt wstępny:
\`audits/graph_and_knot_theory/25-globalny-audyt-04-menger-hall-kirchhoff-wstepny.md\`.

Zakres:
- \`04-spojnosc-przekroje-i-twierdzenie-mengera.tex\`;
- \`05-skojarzenia-systemy-reprezentantow-i-cykle-hamiltona.tex\`;
- \`06-macierze-incydencji-cykle-i-przekroje.tex\`;
- redakcyjne powiązanie z \`08-laplasjan-grafu-dyskretna-teoria-hodge-a-i-twierdzenie-kirchho.tex\`.

## Kontrola matematyczna

**04.** Sprawdzono sformułowania i dowody:
lokalnych i globalnych separatorów, twierdzenia o maksymalnym
przepływie i minimalnym przekroju przy całkowitych przepustowościach,
całkowitoliczbowość przepływu i jego dekompozycję,
obu wersji twierdzenia Mengera (wierzchołkowa dla niesąsiadujących
końców), nierówności Whitneya \`kappa<=lambda<=delta\`.
Uwzględniono grafy rozspójnione i grafy pełne.

**05.** Sprawdzono lemat ścieżki powiększającej,
twierdzenie Bergego, oba przypadki indukcji Halla,
wzór deficytu Halla, konstrukcję pokrycia w dowodzie Kőniga,
kryteria Diraca i Ore'a wraz z rotacją ścieżki Hamiltona.

**06.** Skontrolowano orientację pomocniczą i brzeg łańcucha,
rząd macierzy incydencji \`n-c\`, całkowite bazy
\`H_1(G;Z)\`, strukturę \`H_0(G;Z)\`, opis
przestrzeni cykli i przekrojów nad \`F_2\`,
równości anihilatorów i subtelność niezerowego
przecięcia cykli i przekrojów nad \`F_2\`.
Sprawdzono rzeczywisty ortogonalny rozkład
\`R^E=im B^T ⊕ ker B\`.

Nie wykryto matematycznego kontrprzykładu w tym zakresie.

## Niezależne testy — wyniki rzeczywiste

[Pełny audyt historycznych rozdziałów i kompilacja książki,
GitHub Actions 45156725838](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156725838):
- \`structural-audit\`: **success**;
- \`full-book-pdf\`: **success**;
- \`tools/tests/test_graph_and_knot_advanced_foundations.py\`:
  **1098** wszystkich grafów prostych na 2–5 wierzchołkach,
  niezależne enumeracje ścieżek, separatorów, Hamiltona,
  rzędu incydencji nad \`Q\` i \`F_2\`,
  przestrzeni cykli i cięć, fundamentalnych cykli
  całkowitoliczbowych, energii i ortogonalności;
- **682** grafy dwudzielne z częściami 1–3,
  niezależnie obliczone maksymalne skojarzenia,
  pokrycia, deficyty Halla i ścieżki powiększające;
- testy historycznych rozdziałów 01–03: **1099 grafów**
  i **3413 ciągów stopni**, również **success**.

[Algorytmiczny CI, po poprawie zakresu izolowanej kompilacji,
45157374537](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157374537):
\`finite-models=success\`, \`chapter-pdf=success\`.
Wykonano ponownie także wcześniejsze testy BFS/DFS,
dróg ważonych, A*/CH, MST/DSU, przepływów,
Turána/Ramseya, grafów losowych i ekspanderów.

## Realnie wprowadzone poprawki

1. Rozdział 05 kończy się zgodną z wydrukiem zapowiedzią
   bloku algorytmiczno-probabilistycznego, a dopiero potem
   rozdziału o macierzach incydencji. Dodano właściwe
   odsyłacze \`ch:tg-bfs-dfs\`, \`ch:tg-expanders\`, \`ch:tg-algebra\`.
2. Wstęp rozdziału 06 wskazuje wprost wcześniejszy
   rozdział o drzewach i przejście od algorytmów
   do przestrzeni łańcuchów.
3. Rozdział 08 zawiera matematycznie jednoznaczne
   powiązanie Laplasjanu kombinatorycznego
   \`L_G=D-A\` i znormalizowanego \`I-A/d\`
   z rozdziału 43 przy \`d>=1\`.
   Nie utożsamia się tych operatorów bez normalizacji
   ani nie dzieli przez \`d=0\`.
4. Dodano test \`test_graph_and_knot_advanced_foundations.py\`
   i włączono go do workflow globalnego.

## Dwa rodzaje kompilacji i usunięcie usterki CI

Cała książka ze wszystkich **44 źródeł** kompiluje się
trzykrotnie bez ostrzeżeń \`LaTeX\`, błędów odsyłaczy,
\`Overfull\` i \`Underfull\`; daje
**262 strony A4**. Przejrzano wizualnie strony PDF 35, 41,
82 i 90 (dowody i rysunki, przejście po rozdziale 05,
początek 06 oraz porównanie Laplasjanów w 08).
Żaden z tych przykładów nie wykazuje kolizji lub uciętych tekstów.

Pierwsza skrócona kompilacja
[45156725856](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156725856)
**zakończyła się błędem**: objęła tylko historyczne 00–05
i nowe 37–43, więc nowy poprawny odsyłacz
\`ch:tg-algebra\` z rozdziału 05 był niezdefiniowany
w sztucznie skróconym PDF. Nie był to błąd pełnego wydruku.
Skorygowano zestaw testowy, dodając historyczny rozdział 06
bezpośrednio za 43 i wymagając jego etykiet.
[45157374537](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157374537)
potwierdził ponowny sukces obu zadań;
kontrolny PDF ma **79 stron A4**, brak w nim
ostrzeżeń o odsyłaczach, a fragment 06 jest obecny.

Ponadto dla zmiany merytorycznej:
- [Mathematical library application checks,
  45156726759](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156726759): **success**;
- [Polish mathematical terminology,
  45156726167](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156726167): **success**.

## Kontrola strukturalna całego tomu

W globalnej kontroli nadal:
- **44/44** poprawnych plików;
- **565** etykiet i **145** odsyłaczy;
- **0** zduplikowanych etykiet, **0** niezdefiniowanych referencji,
  **0** błędów środowisk i **0** naruszeń objętych słownikiem terminologii.
Licznik dokładnych wyrażeń nie jest kontrolą semantycznych
powtórzeń twierdzeń.

## Status i następny blok

**Lokalny audyt 04–06: PASS w powyższym zakresie.**
**Globalna stabilizacja 44-rozdziałowej książki: NIEZAKOŃCZONA.**

Następny blok powinien objąć historyczne rozdziały
**07–09**: realizację grafu jako przestrzeni topologicznej,
Laplasjan i teorię Hodge'a/Kirchhoffa oraz planarne
grafy, ściany i wzór Eulera. Kolejne rozdziały
kontrolować matematycznie wraz z przykładami i diagramami
w powtarzalnych, osobno raportowanych iteracjach.
