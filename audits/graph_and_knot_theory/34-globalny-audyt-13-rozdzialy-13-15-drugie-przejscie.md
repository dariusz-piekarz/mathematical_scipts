# Teoria grafów i węzłów — globalny audyt 13: rozdziały 13–15, niezależne drugie przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Poprzednik: [globalny audyt 12](33-globalny-audyt-12-rozdzialy-13-15-przejscie-pierwsze.md).

## Zakres kontroli

Ponownie zbadano wszystkie główne twierdzenia i argumenty historycznych rozdziałów:

- **13 — triangulacje**: kryterium ogniwa, algebraiczny operator brzegu,
  wzór Eulera--Poincarégo, spójność i trójregularność grafu dualnego,
  ruchy Pachnera `1↔3` i `2↔2`, konstrukcja podziału krawędzi;
- **14 — grafy Reeba**: produkt nad przedziałem regularnym, pas
  zawierający dokładnie jedno siodło, stopnie wierzchołków
  grafu Reeba, rachunek `b_1(R_f)=g`, przypadek nieorientowalny;
- **15 — Forman**: konwencja orientacji krawędzi w grafie Hassego,
  równoważność z zamkniętą `V`-ścieżką, parowania drzewowe,
  wzór barycentryczny na kolaps, kompleks łańcuchowy Morse'a
  i silne nierówności Morse'a.

Uwaga metodologiczna: weryfikacja argumentów jest **audytem
matematycznym**, nie formalnym dowodem w Lean. Testy skończonych
przypadków mogą ujawnić kontrprzykłady, lecz nie poświadczają
nieskończonej rodziny twierdzeń.

## 13 — wyniki drugiej kontroli

1. **Kryterium ogniwa:** jeżeli każde ogniwo wierzchołka
   jest cyklem, jego stożek jest dyskiem. Dla krawędzi,
   link jednego końca koduje dwa przyległe trójkąty.
   W odwrotnym kierunku lokalny model `k` półdysków
   wzdłuż średnicy jest modelem powierzchni bez brzegu
   dokładnie przy `k=2`; ogniwo wierzchołka jest
   wtedy sumą cykli, a spójność małego przebitego dysku
   wymusza jeden cykl. Hipotezy skończoności,
   czystości i spójności nie są pomijane.
2. **Operator brzegu:** znaki dla usunięcia wierzchołków
   `i<j` przy przeciwnych kolejnościach różnią się o minus,
   co daje `∂²=0` nad `Z`; wzór na charakterystykę Eulera
   uzasadnia rozkład `f_p=b_p+r_p+r_{p+1}`.
3. **Graf dualny:** spójność przez ścieżkę poprzeczną do
   krawędzi triangulacji, a `3f_2=2f_1` wynika z
   podwójnego zliczenia incidencji. Modele z identyfikowanymi
   bokami opisane jako kompleksy typu Δ są jawnie odróżniane
   od kompleksów symplicjalnych.
4. **Ruchy bistellarne:** oba są zastąpieniami domkniętego
   dysku z niezmienionym brzegiem. Warunek zabraniający
   już istniejącej nowej przekątnej w ruchu `2→2` jest
   konieczny, aby pozostać w kategorii abstrakcyjnych
   kompleksów symplicjalnych. Dla `1→3` zmiana
   `(f_0,f_1,f_2)=(1,3,2)` daje `Δχ=0`,
   a dla `2→2` wszystkie trzy liczby pozostają bez zmian.
5. **Twierdzenie Pachnera** jest nadal jawnie przyjętym
   wynikiem PL; sprawdzenie operacji lokalnych nie jest
   mylone z jego pełnym dowodem.

W tym rozdziale nie wykryto dalszej luki wymagającej
zmiany tekstu po korektach audytu 12.

## 14 — domknięcie argumentu o siodle

W pierwszym przejściu istniał prawidłowy, lecz opisowy
argument, że orientowalność wymusza rozszczepienie lub
połączenie okręgów regularnej poziomicy.
Zastąpiono go osobnym rachunkiem:

- regularne części pasa są cylindrami o `χ=0`;
- dołączenie jednego uchwytu indeksu 1 daje `χ(W)=-1`;
- składowa `W` spotyka oba regularne poziomy
  `a=c-ε`, `b=c+ε`, więc jej brzeg ma
  przynajmniej dwa okręgi;
- orientowalność oraz klasyczny wzór
  `χ(W)=2-2g-b` dają `2g+b=3`; stąd
  `g=0`, `b=3`, a rozdział brzegów to `(1,2)`
  lub `(2,1)`: pas jest parą spodni.

To dokładnie wskazuje rolę orientowalności.
Przykład funkcji Morse'a na `RP²` z jednym punktem
krytycznym każdego indeksu pokazuje dopuszczalność
siodła stopnia dwa bez tej hipotezy.

Po tym uzupełnieniu rachunek
`2e=c_0+c_2+3c_1` i
`b_1(R_f)=1+(c_1-c_0-c_2)/2=g`
jest poprawny dla spójnej orientowalnej
powierzchni zamkniętej i prostej funkcji Morse'a.
Wykorzystuje jawnie klasyczne równanie
`c_0-c_1+c_2=χ(M)=2-2g`, a nie
dowód dla funkcji zdegenerowanych.

## 15 — nowy dowód algebraiczny

Dodano Stwierdzenie
`thm:tg-forman-algebraic-cancellation`,
które **dowodzi algebraicznej części konstrukcji Morse'a**
dla skończonych kompleksów symplicjalnych nad dowolnym
ciałem. Jest to niezależne od zewnętrznego twierdzenia
o istnieniu homotopijnie równoważnego modelu CW.

**Kontrola eliminacji:**
dla pary `(a^p,b^{p+1})` o współczynniku
`λ≠0` w `∂b` wykonuje się zmianę bazy
`a'=λ^{-1}∂b` oraz
`x'=x-μ_xλ^{-1}b` dla pozostałych generatorów
stopnia `p+1`. Otrzymuje się rozkład na
kontraktowalny składnik dwuwyrazowy
`Fb→Fa'` i pozostały kompleks.
Z powodu `∂²=0` różniczki wyższych stopni
nie mają współczynnika przy `b` w nowej bazie.

**Kontrola acykliczności:**
podmacierz incidencji sparowanych `p`- i
`(p+1)`-sympleksów ma przekątną `±1`;
niezerowe elementy poza przekątną wyznaczają
przejścia `V`-ścieżek. Przy braku cykli
można ją uporządkować trójkątnie, a eliminacje
(dopełnienia Schura) zachowują dozwolone pivoty.
Skończenie wiele eliminacji pozostawia dokładnie
niesparowane generatory.

**Konsekwencja:** dla zredukowanego kompleksu
`c_p=b_p+r_p+r_{p+1}`, co daje słabe, silne
nierówności oraz równość Eulera. Ten krok
nie wymaga przyjęcia topologicznej części
twierdzenia Formana.

## 15 — nowe twierdzenie drzewo--drzewo dualne

Dodano Twierdzenie
`thm:tg-forman-tree-cotree`.
W skończonej triangulacji spójnej zamkniętej
powierzchni drzewo rozpinające pierwotnego
szkieletu daje `f_0-1` par wierzchołek--krawędź.
Usunięcie odpowiadających mu krawędzi z grafu
dualnego nie rozspójnia tego grafu.

Ostatni fakt uzasadniono **algebraicznie nad
`F_2`**: ewentualny niepusty zbiór trójkątów
odcięty w grafie dualnym miałby niezerowy brzeg
będący jednocześnie cyklem jednowymiarowym
w drzewie pierwotnym, co jest niemożliwe.
Drzewo rozpinające pozostałego grafu dualnego
dostarcza kolejnych `f_2-1` par
krawędź--trójkąt.

Dla `V`-ścieżek wymiaru zero odległość
od korzenia drzewa pierwotnego maleje;
dla wymiaru jeden odległość od korzenia
drzewa dualnego rośnie. Parowanie jest acykliczne.
Liczby krytycznych sympleksów:
`(1,f_1-f_0-f_2+2,1)=(1,2-χ(M),1)`.
Dla orientowalnego rodzaju `g` daje
`(1,2g,1)`, czyli parowanie doskonałe
nad dowolnym ciałem.

## Niezależne eksperymenty skończone

Dopisano test
`tools/tests/test_graph_and_knot_morse_chain_reduction.py`
i uruchamianie go w
`.github/workflows/graph-and-knot-global-audit.yml`.

Test stosuje prawdziwe macierze brzegowe
`GF(2)` i na każdym kroku sprawdza:
- zachowanie `∂²=0`,
- niezanikający współczynnik eliminowanej pary,
- zachowanie homologii obliczanych niezależnym
  algorytmem rzędu macierzy,
- słabe i silne nierówności Morse'a,
- zgodność liczby pozostałych generatorów
  z liczbą niesparowanych komórek.

Wynik: **60 wszystkich parowań** rozważanych
dwóch najmniejszych kompleksów, z czego
**56 acyklicznych** i **4 cykliczne**.
Dla sfery (brzeg czworościanu) wykonano
**6 eliminacji**, zostawiając `(1,0,1)`;
dla triangulacji torusa `3×3`
**25 eliminacji**, zostawiając `(1,2,1)`.
To odrębny test od wcześniejszej zgodności
kryteriów grafu Hassego i `V`-ścieżek.

## Wyniki CI i ograniczenia środowiskowe

- [45178567680](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45178567680):
  obie prace `structural-audit`, `full-book-pdf` **success**,
  z nowym testem redukcji łańcuchowej;
- [45179060822](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45179060822):
  obie prace **success**, po wprowadzeniu twierdzenia
  drzewo--drzewo dualne;
- [45179134221](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45179134221):
  `structural-audit=success`, `full-book-pdf=failure`.
  Przyczyną jest **brak pakietów TeX Live** w źródłach
  `apt` na obrazie `ubuntu-latest`; krok kompilacji
  był `skipped`, więc to nie jest niepowodzenie LaTeX;
- Workflow `full-book-pdf` przypięto do
  `ubuntu-24.04`, aby uniezależnić kontrolę od
  zmiennych repozytoriów pakietów obrazu `ubuntu-latest`.

## Końcowy przebieg po przypięciu środowiska

[45179359262](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45179359262)
na commicie `8d6f57cf6ff4ca0a4ad2db394ba8cf1a0193451f`
zakończył obie prace sukcesem:
`structural-audit=success` i `full-book-pdf=success`.
Przebieg zawiera nowy test eliminacji łańcuchowej,
weryfikację `44/44` źródeł, odsyłaczy i wszystkie
wcześniejsze kontrole historycznych rozdziałów.

Pobrano i otwarto rzeczywisty artefakt
`graph-and-knot-complete-book-audit` z tego przebiegu:
- **272 strony A4**, trzy udane przebiegi `pdflatex`;
- końcowy `graph_and_knot_full_warnings.txt`:
  **0 wierszy**;
- zweryfikowano renderowane strony PDF **121–135**,
  obejmujące rozdziały 13–15, nowe dowody
  eliminacji algebraicznej, konstrukcję drzewo--drzewo
  dualne i rysunki;
- brak widocznych kolizji tekstu z rysunkami,
  obcięć wzorów, nakładania podpisów oraz
  problemów marginesów w tym zakresie.

Numeracja stron całej książki może się nieznacznie
zmieniać przy zmianie dystrybucji TeX
(ostatni PDF ma 272 strony, poprzedni 271).
Stąd liczba stron nie jest sama w sobie
wskaźnikiem defektu składu.

## Werdykt i bramka stabilizacji

**Historyczne rozdziały 13–15: LOKALNIE STABILNE (PASS)**
w zakresie dwóch szczegółowych przejść matematycznych,
regresji algebraicznej, kontroli struktury i
rzeczywistego składu PDF. Wszystkie bramki
z tego audytu są zakończone sukcesem.
Następny blok szczegółowego audytu: **16–18**.

**Wszystkie 44 rozdziały nadal nie przeszły globalnego
szczegółowego audytu matematycznego.**
Twierdzenie Pachnera i topologiczna część
twierdzenia Formana pozostają jawnie przyjęte.
