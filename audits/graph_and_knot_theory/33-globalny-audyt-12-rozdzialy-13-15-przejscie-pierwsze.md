# Teoria grafów i węzłów — globalny audyt 12: historyczne rozdziały 13–15 (pierwsze przejście)

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Zakres i werdykt

Przeczytano trzy rozdziały źródłowe (łącznie 1179 wierszy po korektach).
Pierwsze przejście matematyczne, językowe i regresyjne: **PASS z doprecyzowaniami**.
**Blok 13–15 pozostaje w stabilizacji:** potrzebne są niezależne drugie przejście
dowodów i kontrola wynikowego składu PDF dla ostatniego commitu.
Historyczne 01–12 pozostają lokalnie stabilne w zakresie poprzednich raportów.
Nie uznajemy ukończenia globalnego audytu 44 rozdziałów.

## Rozdział 13 — triangulacje

Źródło:
`chapters/pl/graph_and_knot_theory/13-triangulacje-i-grafy-dualne-kompleksow-symplicjalnych.tex`.

- **Kryterium ogniwa**: sprawdzono obie implikacje.
  Przy linku będącym jednym cyklem gwiazda wierzchołka jest dyskiem;
  dla zamkniętej powierzchni krawędzie mają dwie incydentne ściany,
  a link wierzchołka nie może mieć wielu rozłącznych cykli.
  Założenia skończoności, czystości, spójności i braku brzegu są jawne.
- **Homologie**: definicja operatorów brzegowych i znoszenie się
  podwójnych usunięć z przeciwnymi znakami; wzór Eulera--Poincarégo
  wynika z rzędu i wymiaru jądra oraz teleskopowania rang.
- **Graf dualny**: zliczenie incidencji `3f_2=2f_1`, trójregularność
  i spójność uzasadnione dla triangulacji zamkniętej powierzchni.
  Przykład dwóch trójkątów opisuje kompleksy typu delta, a nie
  abstrakcyjne kompleksy symplicjalne.
- **Pachner**: lokalne ruchy `1↔3` i `2↔2`, zgodność zmian
  charakterystyki Eulera, wyprowadzenie podziału krawędzi z dwóch ruchów.
  Globalna spójność zbioru triangulacji przez ruchy jest **jawnie
  przyjętym twierdzeniem**, a nie dowodem własnym rozdziału.
- **Korekta**: ograniczono identyfikację grafu z jednowymiarowym
  kompleksem symplicjalnym do grafów prostych (i uwzględniono
  graf bez krawędzi); wyjaśniono, dlaczego w przykładzie
  czworościanu liczby trójkątów i ścian grafowego osadzenia
  akurat się pokrywają.

## Rozdział 14 — grafy Reeba

Źródło:
`chapters/pl/graph_and_knot_theory/14-grafy-reeba-i-funkcje-morse-a-na-powierzchniach.tex`.

- **Przedział bez wartości krytycznych**: pole
  `X=grad(f)/||grad(f)||²` spełnia `df(X)=1`, a zwartość
  pasa zabezpiecza przepływ. Dyfeomorfizm zachowuje poziomy.
- **Istotne uzupełnienie dowodu**: nowy
  `lem:tg-reeb-critical-band` rozdziela lokalny model Morse'a
  od sposobu sklejenia globalnych składowych regularnych poziomic.
  Przy orientowalności siodło zmienia `1↔2` składowe okrężne,
  a jego pas ma typ pary spodni. To uzasadnia stopień trzy
  w grafie Reeba, zamiast wyprowadzać go wyłącznie z hesjanu.
- **Liczba cykli**: przy wierzchołkach krytycznych stopni 1/3
  `2e=c_0+c_2+3c_1`, stąd
  `b_1(R_f)=1+(c_1-c_0-c_2)/2=g` z
  `c_0-c_1+c_2=2-2g`.
  Stosowana jest klasyczna postać wzoru Morse'a dla powierzchni.
- **Test istotności hipotezy**: dodano przykład
  `RP²`, gdzie siodło może mieć stopień dwa w grafie Reeba.
  Wyniku dla powierzchni orientowalnych nie rozciąga się
  bez dowodu na nieorientowalne.

## Rozdział 15 — dyskretna teoria Morse'a

Źródło:
`chapters/pl/graph_and_knot_theory/15-dyskretna-teoria-morse-a-formana.tex`.

- **Ścieżki V**: doprecyzowano zakres indeksów dla niebanalnej
  ścieżki i fakt, że zamknięty spacer skierowany zawiera cykl.
  Sprawdzono oba kierunki równoważności acykliczności parowania
  i skierowanego grafu Hassego.
- **Drzewo rozpinające**: każdy krok ścieżki `V` zmniejsza
  odległość od korzenia; liczby komórek krytycznych wynoszą
  `(1,m-n+1)`.
- **Silna retrakcja przy kolapsie**: wprowadzono jawny wzór
  barycentryczny: dla `m=min(t_0,...,t_p)` homotopia
  odejmuje `um` każdej współrzędnej ściany wolnej i dodaje
  `(p+1)um` współrzędnej wierzchołka przeciwległego.
  Sprawdzono nieujemność, sumę 1, zachowanie pozostałych
  ścian i przedłużenie przez identyczność.
- **Forman**: doprecyzowano znaczenie acyklicznego parowania
  dla skończonego regularnego kompleksu CW.
  Główne twierdzenie o modelu CW **pozostaje jawnie przyjęte**;
  nie jest utożsamiane z kolejnymi elementarnymi kolapsami.
- **Nierówności**: po przyjęciu twierdzenia Formana wzory
  `c_p=b_p+r_p+r_{p+1}` i ich naprzemienne sumowanie
  dowodzą słabych, silnych nierówności oraz równości Eulera.

## Niezależna regresja i CI

Dodano `tools/tests/test_graph_and_knot_triangulation_reeb_forman.py`
i podłączono go do `.github/workflows/graph-and-knot-global-audit.yml`.

W przebiegu [45175903932](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175903932)
(na commicie `db893ffb055f4d12f650d3521d759a6d217d2eab`)
oba zadania zakończyły się **success**, w tym pełny skład książki.
Log `structural-audit` wykazał:
- `44/44` źródeł i zgodność katalogu;
- `0` zdublowanych etykiet, `0` brakujących odsyłaczy,
  `0` błędów środowisk LaTeX;
- `5` jawnych przypadków triangulacji/podziałów
  z kontrolą ogniw, grafów dualnych i homologii nad `GF(2)`;
- `60` małych parowań, dla których niezależne kryteria
  cykli w Hassego i zamkniętych ścieżek `V` są zgodne;
- `20` arytmetycznych przypadków relacji
  stopni grafu Reeba, charakterystyki Eulera i rodzaju.

Zestaw zawiera przykłady sferyczne, torus z siatki okresowej,
przypadki niebędące powierzchniami, ruchy `1→3` i `2→2`,
parowanie brzegu czworościanu i dysku.
Enumeracja nie jest dowodem dla dowolnej triangulacji ani
twierdzeń Pachnera/Formana. Rachunki Reeba sprawdzają
tylko konsekwencje arytmetyczne, nie konstrukcję grafu Reeba.

Po tym przebiegu dodano jeszcze przykład `RP²`
(commit `f08e9f231f0b3c15c83bcffb112195a7eb3451c2`).
**Końcowy przebieg po tej poprawce:**
[45176136460](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45176136460) —
`structural-audit=success`, `full-book-pdf=success`.
Pobrano jego artefakt `graph-and-knot-complete-book-audit`
i sprawdzono rzeczywisty PDF: **269 stron A4**, trzy udane
przebiegi `pdflatex`, **0** ostrzeżeń w końcowym logu.
Wyrenderowano i obejrzano strony PDF **121–136**,
obejmujące wszystkie trzy audytowane rozdziały i rysunki
(z początkiem następnego rozdziału). Nie stwierdzono
uciętych wzorów, nachodzących na siebie podpisów,
rysunków wystających poza margines ani pustych stron
powstałych przez korekty. Ta inspekcja wizualna
nie stanowi weryfikacji poprawności matematycznej.

## Dalsza stabilizacja

1. Powtórnie i niezależnie zweryfikować kryterium ogniwa oraz
   poprawność ruchu `2→2` w otoczeniu całej powierzchni.
2. Przejrzeć argument dla pasa siodłowego oraz zakres założeń
   twierdzenia o `b_1(R_f)=g`.
3. Sprawdzić orientacje strzałek w grafie Hassego i konwencję
   `V`-ścieżek oraz wzór na silną retrakcję.
4. Przejrzeć w następnym przejściu niezależnie wyszczególnione
   punkty matematyczne; kontrola końcowego PDF i CI z obecnej
   iteracji jest już zakończona sukcesem.
5. Dopiero po zamknięciu tych punktów rozważyć oznaczenie
   rozdziałów 13–15 jako lokalnie stabilnych i przejść do 16–18.
