# Topologia algebraiczna — ponowny audyt TOP-13 i TOP-14 po scaleniu

Data: 21 listopada 2026. Zakres: **dokładnie dwa kompletne rozdziały** ze scalonego źródła. Gałąź docelowa: `biblioteka-matematyczna-iteracja-6`, bez tworzenia nowej gałęzi i bez ingerencji w `main`.

## Stan wejściowy i zakres niezależnej kontroli

Odczytano scalone źródła TOP-13 i TOP-14, poprzedni raport `AUDYT_TOP_13_14_POWTORKA_SCALENIE_2026-11-21.md`, wcześniejsze raporty nocne oraz standard. Zbadano cały tekst obu rozdziałów: sformułowania i kompletność hipotez twierdzeń, ciąg dowodów, obliczenia w przykładach, kontrprzykłady, diagramy, odsyłacze, język i zależności zewnętrzne. Nie pomylono składania plików z kontrolą matematyczną.

## TOP-13 — zidentyfikowane luki i wykonane poprawki

1. **Kocykl pierwszej przeszkody z systemem lokalnym.** Wcześniejsze odwołanie do `\partial^2=0` dla pary dysku nie wyjaśniało, dlaczego suma przeszkód w `\pi_n(F)` ma być zerowa. W dowodzie jawnie użyto izomorfizmu Hurewicza `\pi_n(F)\cong H_n(F;\mathbb Z)` dla `(n-1)`-spójnego `F` i `n\ge2`, sumy obrazów brzegów komórek na sferze `\partial D^{n+2}`, oraz równości `\partial c=0` dla łańcucha fundamentalnego jej podziału. Następnie opisano powrót do lokalnych współczynników przez transport wzdłuż dróg. Nie zakładano trywialnej monodromii.
2. **Niezależność od przekroju niższego szkieletu.** Dodano argument homotopijny z pryzmatami komórek `B^{n-1}\times I`: zanikanie `\pi_j(F)` dla `j\le n-1` pozwala porównać przekroje; w stopniu `n` zmiana przeszkody jest kobrzegiem. Wskazano konieczność identyfikacji systemów lokalnych.
3. **Klasyfikacja wiązek głównych.** Rozwinięto krok iniektywności: homotopia map klasyfikujących daje wiązkę nad `X\times I`, a jej ograniczenia do dwóch końców są izomorficzne na mocy homotopijnej niezmienniczości numerowalnych wiązek. Ten standardowy wynik zapisano jawnie jako używane twierdzenie, bez pozorowania jego dowodu samą homotopią punktową.
4. **Struktura tekstu.** Usunięto robocze określenia „audyt” i „obecna iteracja” z nagłówków rozdziału. Zachowano treści, przykłady z wiązką Möbiusa, Moore'em, klasą Eulera i systemami lokalnymi oraz wszystkie stare etykiety.

## TOP-14 — zidentyfikowane luki i wykonane poprawki

1. **Fibracje Postnikowa o włóknie `K(A,n)`.** Wcześniejszy dowód przechodził od równości kocykli przeszkody do równoważności włóknowej bez wskazania twierdzenia klasyfikacyjnego. Dodano analizę `\operatorname{hAut}(K(A,n))`: składowe odpowiadają `\operatorname{Aut}(A)`, a dla `1\le j\le n` zachodzi `\pi_j\operatorname{Map}(K(A,n),K(A,n))_{\operatorname{id}}\cong H^{n-j}(K(A,n);A)`, co daje składową identyczności typu `K(A,n)`; wskazano wyraźnie konieczność użycia klasyfikacji fibracji przez `B\operatorname{hAut}(F)` i trywialności monodromii w podstawie jednospójnej.
2. **Normalizacja `\smile_i`.** Oddzielono samo istnienie rozwiązań równań dla wyższych diagonalnych od unormowania klasycznej konstrukcji Steenroda. Dla `\Delta_n` zapisano jej składnik bidegree `(n,n)` na pojedynczym sympleksie i wyprowadzono `a\smile_n a=a` nad `\mathbb F_2`. Pełna formuła przedziałowa nadal jest jawnie wskazanym standardowym wejściem konstrukcyjnym, a nie rzekomą konsekwencją acykliczności.
3. **Poprawność definicji kwadratów w stopniu zero.** Uzupełniono przypadek `n=0`, gdy nie ma kołańcucha stopnia `-1`, a grupa `B^0` jest zerowa; dalszy dowód niezależności reprezentanta poprawnie zakłada `n\ge1`.
4. **Wzór Cartana i relacje Adema.** Zamiast dawnych dwóch zdań szkicu wpisano rozbudowany dowód z konstrukcji potęg ekwiwariantnych. Wprowadzono `D_2(Y)`, rozkład całkowitej potęgi przez `\operatorname{Sq}^i`, porównanie iloczynów zewnętrznych, równanie współczynników wynikające z zamiany dwóch czynników `(\mathbb Z/2)^2`, specjalizację `N=2^r-1+b`, argument kryterium Lucasa i redukcję do dowolnego stopnia przez zawieszenie. Jako nieelementarny punkt wejściowy jawnie wydzielono klasyczny **lemat o spójnych potęgach ekwiwariantnych**. Nie jest to niezależna reprodukcja łańcuchowego dowodu tego lematu.
5. **Niezależny test relacji Adema.** Stary rachunek `\operatorname{Sq}^2\operatorname{Sq}^2=\operatorname{Sq}^3\operatorname{Sq}^1` w `H^*(\mathbb RP^\infty;\mathbb F_2)` zawsze dawał `0=0`. Dodano przykład `x=ts\in H^2(\mathbb RP^\infty\times\mathbb RP^\infty;\mathbb F_2)` z niezerową wspólną wartością `t^4s^2+t^2s^4`.

## Testy faktycznie wykonane

- **3/3** kolejne kompilacje `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error` z dokumentem testowym zawierającym oba kompletne rozdziały: kod wyjścia `0` każdego przebiegu, końcowy PDF **24 strony**. W końcowym logu: **0** `Overfull \hbox`, **0** niezdefiniowanych odsyłaczy, **0** powielonych etykiet i **0** błędów LaTeX.
- TOP-13: **995 wierszy, 10 unikalnych etykiet** (zachowano wszystkie 10 z poprzedniego scalonego źródła); TOP-14: **1205 wierszy, 17 unikalnych etykiet** (zachowano 15 poprzednich, dodano 2 do nowo wyprowadzonych wzorów).
- Automatyczne sprawdzenie pełnej składni par `\begin/\end`, unikalności etykiet, wewnętrznych celów wszystkich 15 referencji i braku zależności `\input`, `\include` i `\includegraphics` w obu rozdziałach: bez naruszeń.
- **15 876 sprawdzeń** relacji Adema dla wszystkich jednomianów `t^m s^n`, `0\le m,n<18` oraz par `1\le b\le7`, `1\le a<2b` w pierścieniu `\mathbb F_2[t,s]`, z niezależnym obliczaniem parzystości współczynników dwumianowych według kryterium Lucasa: wszystkie zaliczone. Dodatkowy niezerowy test `t s` zgodny.
- Porównanie nazw etykiet tej pary z **25 innymi** modułami topologii algebraicznej obecnymi w archiwalnej migawce Biblioteki z 19 listopada: brak konfliktów tych etykiet. Nie stanowi to testu wszystkich nowszych zmian pozostałych rozdziałów.
- Wygenerowano pogląd 24 stron i przeprowadzono kontrolę wizualną składu. Bez kolizji podpisów na oglądanym zestawieniu; oznacza to kontrolę poglądową, nie inspekcję w maksymalnej rozdzielczości każdego glifu.

## Rozróżnienie: domknięcie audytu a samodzielność całego wykładu

**Zakończono ponowną krytyczną kontrolę tekstu tych dwóch rozdziałów**, w tym wszystkich miejsc wyznaczonych we wcześniejszych raportach. Wszystkie znane luki w rozumowaniu zostały poprawione albo jawnie zastąpione wskazaniem precyzyjnego standardowego twierdzenia wejściowego. W szczególności nie przedstawiamy konstrukcji potęg ekwiwariantnych na poziomie wszystkich koherentnych homotopii łańcuchowych jako samodzielnie wyprowadzonej w skrypcie. Jeżeli kryterium jest absolutna samowystarczalność dowodu Adema od definicji kompleksu singularnego, potrzebny byłby **dodatkowy specjalistyczny rozdział** o rezolwentach ekwiwariantnych. Nie utożsamiamy tej różnicy z błędem w obecnym wzorze Adema.

Nie udało się zbudować pełnej kanonicznej 31-rozdziałowej książki z aktualnego GitHuba, ponieważ środowisko kompilacyjne nie miało dostępu sieciowego do repozytorium, a lokalna migawka pozostałych rozdziałów była starsza i niekompletna. Test obejmuje dwa całe rozdziały z pełnym pomocniczym dokumentem; wyników nie nazywamy kompilacją całej książki.

Kolejna zwykła iteracja może objąć **TOP-15 i TOP-16** (po uprzednim odczycie najnowszego stanu i potwierdzeniu braku równoległych zmian). Automatyzacji nie włączano.

## Źródła kontroli głębokich zależności

- Allen Hatcher, *Algebraic Topology*, §4.L, twierdzenia 4L.12 i 4L.13: https://math.uchicago.edu/~farb/algtop2023/Hatcher.pdf
- *A cochain level proof of Adem relations in the mod 2 Steenrod algebra*, https://link.springer.com/article/10.1007/s40062-021-00287-3
- *Postnikov system*, Encyclopedia of Mathematics: https://encyclopediaofmath.org/wiki/Postnikov_system