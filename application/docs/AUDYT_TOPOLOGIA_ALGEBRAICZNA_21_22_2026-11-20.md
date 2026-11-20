# Topologia algebraiczna — szczegółowy audyt AT-21 i AT-22

**Data:** 20 listopada 2026.  
**Gałąź robocza:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Zakres matematyczny:** dokładnie dwa kanoniczne rozdziały
`chapters/pl/algebraic_topology/21-indeks-pol-wektorowych-i-twierdzenie-poincarego-hopfa-z-brzegi.tex` i
`chapters/pl/algebraic_topology/22-kohomologia-z-nosnikami-zwartymi-i-homologia-borel-moore-a.tex`.
**Standard:** DG-01 — hipotezy we wszystkich twierdzeniach, jawne rachunki i uzasadnienia, przykłady, kontrprzykłady, rysunki, terminologia polska, zachowanie oryginalnych etykiet, niezależność zasobów.

## AT-21 — indeks pola wektorowego i twierdzenie Poincarégo–Hopfa z brzegiem

Przejrzano lemat porównania indeksu izolowanego zera pola z indeksem punktu stałego lokalnego odwzorowania wykładniczego, dowód dla rozmaitości zamkniętych przez twierdzenie Lefschetza–Hopfa, definicję ściśle zewnętrznego pola, podwojenie rozmaitości i formułę sumy indeksów dla pola skierowanego na zewnątrz.

1. **Doprecyzowanie hipotez:** w lemacie porównującym indeksy wpisano explicite `p∈int M`, gdyż przy zerze na brzegu nie wolno bez nowej definicji używać indeksu izolowanego zera w pełnej kuli.
2. **Nowy wniosek `cor:PH-inward-boundary`:** dla pola skierowanego **ściśle do wnętrza** na brzegu dowiedziono formuły
   `Σ ind_p(X)=(-1)^n χ(M)`.
   Dowód stosuje twierdzenie zewnętrzne do `-X` oraz oblicza zmianę lokalnego stopnia z wykorzystaniem odwzorowania antypodalnego `S^{n-1}→S^{n-1}` stopnia `(-1)^n`. Rozumowanie działa także dla izolowanych zer osobliwych, bo wykorzystuje definicję przez stopień, nie wyłącznie wyznacznik hesjanu.
3. **Przykład `prz:PH-inward-ball`:** na `D^n` pole `X(x)=-x` ma dokładnie jedno zero indeksu `(-1)^n`; dla odcinka (`n=1`) otrzymujemy `-1`, podczas gdy `χ(D^1)=1`. Jest to istotny kontrprzykład wobec bezwarunkowego stosowania formuły zewnętrznej.
4. **Przykład `prz:PH-annulus-nozeros`:** dla `M={a≤r≤b}` i `r_0=(a+b)/2` skonstruowano gładkie pole
   `X=(r-r_0)e_r+e_θ`.
   Ma ono `||X||²=(r-r_0)²+1>0`, a jego iloczyn skalarny z zewnętrzną normalną jest dodatni zarówno przy `r=a`, gdzie normalna to `-e_r`, jak i przy `r=b`, gdzie normalna to `e_r`. Zatem pole spełnia hipotezę mimo braku zer; wynik `Σ ind=0=χ(M)` jest poprawny.
5. **Rysunek `fig:PH-annulus-field`:** pierścień z przykładowymi zwrotami pola na obu składowych brzegu. Diagram stanowi samodzielny TikZ i nie wymaga zewnętrznego pliku.

**Zależności:** dowód twierdzenia granicznego korzysta z wcześniej opracowanych indeksu Brouwera, twierdzenia Lefschetza–Hopfa i standardowych narzędzi wygładzania na podwojeniu; nie powtarzano w AT-21 pełnej algebry tensorowej ani dowodu Lefschetza z AT-19.

## AT-22 — nośniki zwarte i homologia Borela–Moore’a

Przejrzano definicję `H_c^k(X;G)=colim_K H^k(X,X\\K;G)`, funktorialność kontrawariantną dla odwzorowań właściwych, kompleks kompaktowo podpartych form de Rhama, rachunek `H_{c,dR}^*(R^n)` z jawnym operatorem homotopii, porównanie de Rhama z kohomologią o nośnikach zwartych, lokalnie skończone singularne łańcuchy, właściwą funktorialność homologii Borel–Moore’a, lokalnie skończoną klasę fundamentalną i obie wersje niezwartiej dualności Poincarégo.

1. **Nowy przykład właściwego odwzorowania `prz:BM-proper-inclusion-line`:** `i:R→R², t↦(t,0)` jest właściwym zanurzeniem, a mimo to
   `i_*:H_1^{BM}(R;Z)=Z→H_1^{BM}(R²;Z)=0`
   jest zerowy. Geometrycznie cała zorientowana prosta jest brzegiem lokalnie skończonego łańcucha złożonego z trójkątów triangulacji górnej półpłaszczyzny. Wyjaśniono różnicę między istnieniem poprawnego `i_*` a jego iniektywnością.
2. **Nowy przykład `prz:BM-countable-lines`:** dla `X=⨿_{j∈N} R_j`, który jest drugoprzeliczalną jednowymiarową rozmaitością, udowodniono:
   `H_1^{BM}(X;Z)≅∏_{j∈N}Z`,
   `H_c^1(X;Z)≅⊕_{j∈N}Z`,
   `H^0(X;Z)≅∏_{j∈N}Z`,
   `H_0(X;Z)≅⊕_{j∈N}Z`.
   Każdy zwarty zbiór `K⊂X` przecina tylko skończenie wiele `R_j` (skończone podpokrycie pokrycia przez otwarte składowe). Z kolei lokalnie skończony łańcuch dopuszcza niezależną niezerową rodzinę łańcuchów w każdej składowej. Udowodniono rozkład kompleksów jako sumy prostej i produktu, a następnie rozkład homologii (obrazy operatorów współrzędnych też tworzą produkty). Ciąg `(1,1,1,...)` należy do produktu, ale nie do sumy prostej. Obie wersje dualności mają poprawne, odrębne strony.
3. **Rysunek `fig:BM-countable-lines`:** nieskończona rodzina prostych z ograniczonym obszarem zwartym przecinającym tylko skończenie wiele składowych, wraz z lokalnie skończonymi dodatnimi orientacjami.
4. **Założenia:** nie usuwano definicji lokalnie skończonej homologii ani jej wymogu na \emph{każdym zwartym zbiorze}. Zachowano rozróżnienie `G` jako dowolnej grupy abelowej i `R` jako współczynników de Rhama, a także system orientacji w przypadku nieorientowalnym.

**Jawna, nadal istniejąca zależność:** globalne porównanie de Rhama z nośnikami zwartymi w `thm:compact-deRham-v11` używa standardowego twierdzenia o rezolwentach snopowych i ekscyzji; porównanie homologii lokalnie skończonej komórkowej i singularnej w `thm:noncompact-PD-v11` także jest wcześniej przyjętym standardowym narzędziem. Kontrola nowych przykładów nie oznacza wykonania niezależnych pełnych dowodów wszystkich tych twierdzeń porównawczych.

## Zależności źródłowe i CI

- Historycznych `\label` ani `\ref` nie przemianowywano. AT-22 zawiera oryginalny `\ref{ch:snopy-verdier-v12}` do AT-23. Aby zachować ten odsyłacz w kontrolnej kompilacji, workflow ładuje AT-01–22 **oraz AT-23 wyłącznie jako kontekst**. Audyt matematyczny bieżącej pary \emph{nie} obejmuje AT-23.
- Nowe regresje: `application/tests/test_topology_chapters_21_22.py` — historyczne etykiety, obecność poprzednich i przyszłego kontekstu, kompletność odsyłaczy AT-21/22, bilans środowisk LaTeX i brak zewnętrznych plików, stopień pola wewnętrznego, dodatniość składowych radialnych na obu brzegach pierścienia, rozróżnienie produktu i sumy prostej, właściwa mapa `R→R²`, hipotezy dualności.
- Workflow: `.github/workflows/algebraic-topology-audit-ch21-22.yml`; dwa przebiegi `pdflatex`, kontrola niezdefiniowanych odsyłaczy, kontrola `Overfull \\\hbox`, artefakt PDF i logów.
- [GitHub Actions aplikacji #44797203726](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44797203726) — **SUCCESS**, **228** testów Pythona (1 pominięty) i Chromium, 355 rozdziałów indeksu. **Wynik PDF i oględziny figur zostaną dopisane po faktycznym sprawdzeniu.**

## Status audytu

**AT-21:** oczekuje końcowego wyniku kompilacji i przeglądu nowego rysunku.  
**AT-22:** oczekuje końcowego wyniku kompilacji i przeglądu nowego rysunku; zachować zastrzeżenie dotyczące pełnego niezależnego dowodu globalnych twierdzeń porównawczych.

**Następna para:** AT-23 i AT-24, z pełną kontrolą matematyczną, przykładami i grafiką. Załadowanie AT-23 w bieżącym kontekście kompilacji nie zastępuje jego przyszłego audytu.
