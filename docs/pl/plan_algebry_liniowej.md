# Plan dalszych rozdziałów — algebra liniowa

Stan na 21 listopada 2026. Książka `books/pl/linear_algebra.tex`: rozdziały **01–27 stabilne**. Dla LA-25 kompletny przebieg GitHub Actions [44949428707](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44949428707) zakończył się sukcesem, a samodzielny PDF ma 15 zweryfikowanych stron.

## Plan kolejnych rozdziałów

| Nr roboczy | Temat | Pochodzenie i zależności | Status |
|---|---|---|---|
| 25 | Sterowalność, obserwowalność, stabilizowalność, wykrywalność; kryteria Kalmana i PBH, rozkład Kalmana | Kontynuacja LA-24; nowy rozdział z pełnymi dowodami, testami i PDF | Stabilny po 7 audytach |
| 26 | Uogólnione twierdzenia CARE/DARE dla układów z niestabilną otwartą pętlą | Wykorzystuje LA-24 i LA-25; obejmuje półokreślony koszt i rozwiązania stabilizujące | Stabilny po 3 audytach |
| 27 | Gramiany obserwowalności, realizacje minimalne, macierze Hankela, redukcja układów | Kontynuacja LA-25; nowe dowody, bez powielania kryteriów Kalmana | Stabilny po 8 audytach |
| 28 | Układy liniowe z wymuszeniem, funkcje przejścia i realizacje | Po LA-25/27; można wydzielić do teorii sterowania | Opcjonalny |
| 29 | Grassmanniany | **Przenieść i zaadaptować istniejący materiał DG-04**, bez ponownego opracowywania od zera | Zatwierdzony do planu |
| 30 | Algebry Clifforda | **Przenieść i zaadaptować istniejący materiał DG-04**, z powiązaniem z LA-09 i LA-11 | Zatwierdzony do planu |
| 31 | **Grupy Pin i Spin, spinory oraz struktury spinowe** | **Przenieść i zaadaptować z DG-04** sekcje o odbiciach, grupach Pin/Spin, modułach Clifforda, spinorach i wiązkach spinorowych; powiązać z LA-30 | **Zatwierdzony do planu** |
| 32 | **Twistory i podstawy geometrii twistorowej** | **Nowy materiał, nieobecny w DG-04**; opracować od podstaw po LA-29–31, bez kopiowania z DG | **Zatwierdzony do planu** |

Numery 27–32 są **robocze** i mogą zostać przestawione przy końcowym porządkowaniu książki, bez zmiany numerów stabilnych rozdziałów 01–27.

## Materiał źródłowy z geometrii różniczkowej

**Kanoniczny plik:** `chapters/pl/differential_geometry_and_topology/04-grassmanniany-algebra-clifforda-i-spinory.tex`.

- **Grassmanniany:** sekcje `sec:grass-atlas`, `sec:grass-styczna`, `sec:grass-plucker`; konstrukcja map wykresowych, model rzutów, przestrzeń styczna `Hom(L,V/L)`, wiązka tautologiczna, współrzędne Plückera, odwzorowanie Gaussa i przykłady. Zachować lokalne rysunki TikZ, także `fig:grass-wykres`.
- **Algebry Clifforda:** sekcja `sec:clifford`; `def:clifford`, `thm:cliff-relacje`, `thm:cliff-baza`, `prop:cliff-wedge`; konstrukcja z algebry tensorowej, iloczyn Clifforda i jego relacja do algebry zewnętrznej. Zachować przykłady i `fig:cliff-iloczyn`.
- **Grupy Pin i Spin oraz spinory — LA-31:** użytkownik zatwierdził ich pełne przeniesienie i adaptację z DG-04. Obowiązkowe sekcje źródłowe: `sec:spin-grupa` (odbicia, grupy Pin i Spin, nakrycie), `sec:spinory` (moduły algebry Clifforda i reprezentacje spinorowe) i `sec:struktura-spinowa` (struktury spinowe, wiązki spinorów i przykłady). Zachować **wszystkie istotne dowody, kontrprzykłady i rysunki**, w tym `fig:spin-dwukrotne`, `fig:spin-bloch` i `fig:spin-torus-signs`. Materiał rozmaitościowy traktować jako wyraźnie oznaczony fragment geometryczny z niezbędnymi definicjami; nie zmieniać treści źródłowej DG-04.

## Zasady przeniesienia DG → LA

1. Zachować **sumę całej niepowtarzalnej treści** przenoszonych fragmentów: sformułowania, istotne dowody, przykłady, kontrprzykłady, rysunki TikZ. Nie zastępować gotowego tekstu skróconym streszczeniem.
2. Dostosować wprowadzenie, definicje i odsyłacze do algebry liniowej; w szczególności sprawdzić zależności z `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` oraz wcześniejszych rozdziałów LA o algebrze tensorowej, zewnętrznej, iloczynach skalarnych i formach kwadratowych. Zagadnienia rozmaitościowe wymagają lokalnego przypomnienia niezbędnych pojęć lub poprawnego odsyłacza międzytomowego — nie tworzyć pustych etykiet.
3. Zachować stabilne etykiety źródłowe w DG-04. Dla nowych plików LA utworzyć unikatowe etykiety z prefiksami `lin29-`, `lin30-` i `lin31-` i odpowiednio przepisać lokalne odsyłacze; zapisać mapę pochodzenia etykiet.
4. W plikach LA nie importować bezpośrednio całego DG-04: rozdzielić sekcje na LA-29, LA-30 i LA-31. Zapobiec kolizjom etykiet, wielokrotnemu `\chapter` i brakującym makrom.
5. Każdy nowy rozdział oddzielnie audytować matematycznie, redakcyjnie, terminologicznie i typograficznie, wykonywać regresje CI, sprawdzać odsyłacze i **eksportować samodzielny PDF**. Stabilizować dopiero po dwóch kolejnych czystych audytach i zielonym CI.
6. W języku polskim „chart” → „mapa”, „mapping” → „odwzorowanie”, „sequence” → „ciąg”; bez nieuzasadnionych skrótów dowodów. Rysunki i podpisy podlegają tej samej kontroli.

## Zakres osobnych skryptów

Blok sterowania (25–28) można docelowo wydzielić do osobnego skryptu o teorii sterowania. Grassmanniany, algebry Clifforda, grupy Pin/Spin i spinory pozostają **również w planie algebry liniowej**, ze wskazaną kanoniczną zawartością DG-04 jako materiałem źródłowym. Twistory będą **nowym rozdziałem LA-32**, a nie automatycznym importem z geometrii różniczkowej.

## Nowy rozdział LA-32: twistory (materiał do opracowania)

**To nie jest część DG-04; wymaga osobnego, oryginalnego opracowania i audytu.** Przed rozpoczęciem odróżnić konwencje euklidesowe, lorentzowskie i zespolone; nie utożsamiać bez uzasadnienia rzeczywistych struktur w różnych sygnaturach.

1. **Przygotowanie algebraiczne:** przestrzeń spinorowa wymiaru 2 nad \(\mathbb C\), indeksy spinorowe i formy antysymetryczne; związek \(\mathbb C^4\) z tensorowym modelem spinorowym, konforemna grupa i odpowiednia rzeczywista forma po sprecyzowaniu sygnatury.
2. **Przestrzeń twistorowa:** \(\mathbb T\cong\mathbb C^4\), jej przestrzeń projektywna \(\mathbb{PT}\cong\mathbb{CP}^3\), geometryczne znaczenie punktów i prostych, incydencja \(\omega^A= i x^{AA'}\pi_{A'}\) z jawnymi konwencjami dla czynnika \(i\).
3. **Relacja z grassmannianami:** linie w \(\mathbb{CP}^3\), \(\mathrm{Gr}(2,4)\), współrzędne Plückera, kwadryka Kleina i korespondencja incydencji w ujęciu zespolonym; dokładny zakres, kiedy istnieje odpowiednia interpretacja rzeczywista.
4. **Geometria i przykłady:** fibracja twistorowa \(\mathbb{CP}^3\to S^4\) w wersji euklidesowej, geometria konforemna, prostota i ograniczenia modelu; ewentualne dalsze zastosowania do równań pola jako odrębna propozycja, nie automatyczne rozszerzenie.
5. **Standard dowodów:** precyzyjne założenia, pełne kroki rachunków, ilustracje incydencji i diagramy, kilka przykładów oraz kontrprzykładów. Najpierw zweryfikować zgodność terminologii i odsyłaczy do LA-29–31; jak dla pozostałych rozdziałów dwa kolejne czyste audyty i zielony CI z osobnym PDF.
