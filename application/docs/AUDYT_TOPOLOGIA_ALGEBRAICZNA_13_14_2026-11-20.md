# Topologia algebraiczna — szczegółowy audyt AT-13 i AT-14

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** wyłącznie `chapters/pl/algebraic_topology/13-przestrzenie-klasyfikujace-i-teoria-przeszkod.tex` i `14-wieze-postnikowa-iloczyny-whiteheada-i-operacje-steenroda.tex`; wcześniejsze rozdziały AT-01–12 służą jako kontekst matematyczny i cele odsyłaczy.  
**Kryteria:** standard dowodów i przykładów DG-01, ścisłe hipotezy, rachunki matematyczne, język polski, rysunki, niezależność zasobów, zachowanie oryginalnych `\label` i zgodność z książką modułową. Gałęzi `main` nie zmieniano.

## AT-13 — przestrzenie klasyfikujące i teoria przeszkód

Audyt obejmował konstrukcje `K(G,n)` i grupy homotopii, reprezentację kohomologii przez `[X,K(A,n)]`, modele `EG\to BG`, klasyfikację wiązek głównych i wektorowych, `BU(1)=CP∞`, obstrukcje rozszerzania przekrojów (z lokalnymi współczynnikami), klasę Eulera i przykład wiązki bez nieznikającego przekroju pomimo zerowej klasy Eulera.

1. **Pełny rachunek przestrzeni Moore’a (`prz:moore-cohomology-Hom-Ext-v6`).** Dla `M=S^n\cup_m e^{n+1}` zapisano oba kompleksy komórkowe, z różniczką mnożenia przez `m`. Dla dowolnej grupy abelowej `A` uzyskano `H^n(M;A)=A[m]` oraz `H^{n+1}(M;A)=A/mA`, z dokładnym objaśnieniem składników `Hom(Z/m,A)` i `Ext¹(Z/m,A)` z twierdzenia o współczynnikach uniwersalnych.
2. Sprawdzono obstrukcję dołączenia komórki do `K(A,n)`: mapa z `S^n` klasy `a∈A` przedłuża się wtedy i tylko wtedy, gdy `ma=0`. Wyprowadzono to z klasy złożenia z odwzorowaniem dołączającym, a nie przez powołanie się wyłącznie na wynik końcowy. Przypadki `A=Z` oraz `A=Z/m` rozróżniają niezerowe stopnie kohomologii i pokazują, dlaczego składnika `Ext` nie wolno pominąć.
3. **Nowy rysunek TikZ (`fig:moore-kernel-cokernel-v6`)** pokazuje przeciwne kierunki różniczki łańcuchowej i koróżniczki oraz odpowiednie jądro i cokernel.
4. **Audyt terminologiczny:** „odwzorowanie” zamiast „mapa” w znaczeniu angielskiego `mapping`, „ekwiwariantny” zamiast niepoprawnej formy; zachowano „mapa” wyłącznie w sensie mapy współrzędnych w innych skryptach. Nie zmieniono historycznych deklaracji `\label`, wzorów klasyfikujących ani mechanizmu lokalnego systemu współczynników.

## AT-14 — Postnikow, Whitehead, Steenrod

Audyt objął konstrukcję etapów Postnikowa, włókna `K(A,n)` i klasy `k_n`, obliczenie `k_3(S²)=±u²`, homotopijny sens iloczynu Whiteheada, niezmiennik Hopfa, równoważność obstrukcji do podniesienia i znikania klasy `f^*k_n`, a także wyższe diagonalne, podstawowe operacje `Sq^i`, wzór Cartana i relacje Adema.

1. **Nieznikająca pierwsza przeszkoda Postnikowa (`prz:postnikow-cp2-nie-ma-liftu`).** Dla generatora `h∈H²(CP²;Z)` klasa `h²∈H⁴(CP²;Z)` jest niezerowa, więc odpowiadająca mapa `CP²→K(Z,2)=P₂S²` nie może zostać podniesiona do `P₃S²`. Niezależny dowód wykorzystuje naturalność iloczynu kubkowego i fakt `u²=0` w `H⁴(S²)`. Geometrycznie przeszkodą dla przedłużenia identyczności z `S²\subset CP²` na 4-komórkę jest niezerowa mapa Hopfa.
2. **Jawne przedłużanie z bukietu (`prz:whitehead-fold-product-v7`).** Mapa składania `S²∨S²→S²`, będąca identycznością na obu składnikach, nie przedłuża się do `S²×S²`. Pierwszy dowód używa `[ι₂,ι₂]=±2η≠0`; drugi używa `(x+y)²=2xy≠0` w `H⁴(S²×S²;Z)`. To matematycznie wyjaśnia współczynnik `2` w kwadracie Whiteheada.
3. **Diagram `fig:whitehead-product-obstruction-v7`:** wizualizacja dołączania 4-komórki do bukietu i braku możliwości przedłużenia odwzorowania składania.
4. **Przykład operacji Steenroda poza zwykłymi potęgami (`prz:steenrod-rp5-obliczenia-v7`).** Dla `x=t³∈H³(RP⁵;F₂)` obliczono `Sq¹(x)=t⁴≠0`, `Sq²(x)=t⁵≠0`, podczas gdy `x²=t⁶=0` ze względu na wymiar. Wyprowadzono bezpośrednią kontrolę `Sq¹Sq¹(t^m)=m(m+1)t^{m+2}=0` w `RP∞`; **jest to weryfikacja konkretnego przykładu, a nie globalny dowód relacji Adema**.
5. Sprostowano konsekwentnie terminologię odwzorowań i zachowano wszystkie historyczne etykiety.

## Zależności, poprawność odsyłaczy i retesty

- W całym zakresie AT-01–14 deklaracje `\label` są unikalne. AT-13 i AT-14 zawierają łącznie **9 wywołań** standardowych odsyłaczy; wszystkie cele istnieją w AT-01–14. Żadnych nazw wcześniejszych `\label` ani `\ref` nie zastąpiono nowymi.
- AT-13 ma **3**, AT-14 **2** diagramy TikZ. Rozdziały są niezależne od zewnętrznych plików graficznych, danych i kodu: figury są osadzone w TeX.
- Nowe testy `application/tests/test_topology_chapters_13_14.py` kontrolują integralność 14 rozdziałów w książce, historyczne etykiety, brak duplikatów i błędnych odsyłaczy, środowiska TeX, terminologię oraz rachunki Moore’a, Postnikowa, Whiteheada i `Sq^i`.
- Nowy workflow `.github/workflows/algebraic-topology-audit-ch13-14.yml` uruchamia dwukrotną kompilację TeX AT-01–14 z kontrolą brakujących odsyłaczy i przepełnionych wierszy.
- **Testy aplikacji i regresji:** [GitHub Actions #44777464928](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44777464928) — **SUCCESS**, 177 testów Pythona (1 pominięty) oraz testy Chromium, 355 rozdziałów w indeksie. Nowe testy obejmują obliczenia Moore'a, kwadratów Steenroda, Postnikowa i Whiteheada.
- **Finalna kompilacja:** [GitHub Actions #44777464845](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44777464845) — **SUCCESS**, 172 strony, dwa przebiegi `pdflatex`, brak niezdefiniowanych odsyłaczy i brak przepełnień `Overfull \\hbox`. Skompilowano rozdziały AT-01–14 jako całość, bez zewnętrznych plików graficznych.
- **Naprawiony rzeczywisty błąd graficzny:** pierwsza kompilacja [#44776522519](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44776522519) wykryła w nowym diagramie AT-14 nieobsługiwany grot `hook->` (błąd `Unknown arrow tip kind 'hook'`). Zmieniono go na obsługiwany `->` w commicie `06e6f492`; kolejna kompilacja oraz finalny retest zakończyły się sukcesem.
- **Rysunki zweryfikowane wizualnie:** pięć diagramów AT-13/14, w tym istniejące modele klasyfikacji i wieży Postnikowa oraz nowe diagramy Moore'a i Whiteheada; strony finalnego PDF odpowiednio 158, 160, 163, 165 i 168. Oględziny na renderach nie wykazały obciętych elementów ani kolizji etykiet. Nowy schemat Whiteheada sprawdzono również w pełnym rozmiarze.
- **Końcowy wynik audytu tej pary:** AT-13 zaakceptowany; AT-14 zaakceptowany w zakresie sprawdzonych twierdzeń i przykładów, z **jawną, nadal otwartą luką** dotyczącą pełnych konstrukcyjnych dowodów formuły Cartana i relacji Adema. Luka pozostaje w rejestrze dalszych uzupełnień i nie jest traktowana jako dowiedziona.

## Precyzyjny zakres ograniczeń

W AT-14 ogólne wzory Cartana i relacje Adema są podane jako klasyczne twierdzenia, ale sam rozdział otwarcie zaznacza, że `thm:steenrod-cartan-v7` **nie zawiera pełnego konstrukcyjnego dowodu**. Uzupełniono obliczenia konkretnych przypadków, lecz nie należy oznaczać nieudowodnionej konstrukcji operadów i spójnych diagonalnych jako zakończonego audytu dowodu. Podobnie nie rościmy sobie prawa do pełnej teorii niestabilnych klasyfikacji fibracji poza podanymi hipotezami.

**Następna para:** AT-15 oraz AT-16, po zamknięciu retestu. Dokumentacja i status zostaną zsynchronizowane z wynikami GitHub Actions.
