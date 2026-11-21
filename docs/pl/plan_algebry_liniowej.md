# Plan dalszych rozdziałów — algebra liniowa

Stan na 21 listopada 2026. Książka `books/pl/linear_algebra.tex`: rozdziały **01–26 stabilne**. Dla LA-25 kompletny przebieg GitHub Actions [44949428707](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44949428707) zakończył się sukcesem, a samodzielny PDF ma 15 zweryfikowanych stron.

## Plan kolejnych rozdziałów

| Nr roboczy | Temat | Pochodzenie i zależności | Status |
|---|---|---|---|
| 25 | Sterowalność, obserwowalność, stabilizowalność, wykrywalność; kryteria Kalmana i PBH, rozkład Kalmana | Kontynuacja LA-24; nowy rozdział z pełnymi dowodami, testami i PDF | Stabilny po 7 audytach |
| 26 | Uogólnione twierdzenia CARE/DARE dla układów z niestabilną otwartą pętlą | Wykorzystuje LA-24 i LA-25; obejmuje półokreślony koszt i rozwiązania stabilizujące | Stabilny po 3 audytach |
| 27 | Gramiany sterowalności i obserwowalności, realizacje minimalne, rozkład Kalmana w zastosowaniach | Uzupełnienie LA-25 (bez ponownego dowodzenia tych samych wyników) | Do rozważenia |
| 28 | Układy liniowe z wymuszeniem, funkcje przejścia i realizacje | Po LA-25/27; można wydzielić do teorii sterowania | Opcjonalny |
| 29 | Grassmanniany | **Przenieść i zaadaptować istniejący materiał DG-04**, bez ponownego opracowywania od zera | Zatwierdzony do planu |
| 30 | Algebry Clifforda | **Przenieść i zaadaptować istniejący materiał DG-04**, z powiązaniem z LA-09 i LA-11 | Zatwierdzony do planu |

Numery 27–30 są **robocze** i mogą zostać przestawione przy końcowym porządkowaniu książki, bez zmiany numerów stabilnych rozdziałów 01–26.

## Materiał źródłowy z geometrii różniczkowej

**Kanoniczny plik:** `chapters/pl/differential_geometry_and_topology/04-grassmanniany-algebra-clifforda-i-spinory.tex`.

- **Grassmanniany:** sekcje `sec:grass-atlas`, `sec:grass-styczna`, `sec:grass-plucker`; konstrukcja map wykresowych, model rzutów, przestrzeń styczna `Hom(L,V/L)`, wiązka tautologiczna, współrzędne Plückera, odwzorowanie Gaussa i przykłady. Zachować lokalne rysunki TikZ, także `fig:grass-wykres`.
- **Algebry Clifforda:** sekcja `sec:clifford`; `def:clifford`, `thm:cliff-relacje`, `thm:cliff-baza`, `prop:cliff-wedge`; konstrukcja z algebry tensorowej, iloczyn Clifforda i jego relacja do algebry zewnętrznej. Zachować przykłady i `fig:cliff-iloczyn`.
- **Pokrewne sekcje o Pin, Spin i spinorach:** `sec:spin-grupa`, `sec:spinory`, `sec:struktura-spinowa` pozostają w DG-04; ich ewentualny pełny import wymaga osobnej decyzji. Użytkownik zatwierdził obecnie grassmanniany i algebry Clifforda.

## Zasady przeniesienia DG → LA

1. Zachować **sumę całej niepowtarzalnej treści** przenoszonych fragmentów: sformułowania, istotne dowody, przykłady, kontrprzykłady, rysunki TikZ. Nie zastępować gotowego tekstu skróconym streszczeniem.
2. Dostosować wprowadzenie, definicje i odsyłacze do algebry liniowej; w szczególności sprawdzić zależności z `chapters/pl/differential_geometry_and_topology/03-algebra-tensorowa-i-zewnetrzna.tex` oraz wcześniejszych rozdziałów LA o algebrze tensorowej, zewnętrznej, iloczynach skalarnych i formach kwadratowych. Zagadnienia rozmaitościowe wymagają lokalnego przypomnienia niezbędnych pojęć lub poprawnego odsyłacza międzytomowego — nie tworzyć pustych etykiet.
3. Zachować stabilne etykiety źródłowe w DG-04. Dla nowego pliku LA utworzyć unikatowe etykiety z prefiksem `lin29-` i `lin30-` i odpowiednio przepisać lokalne odsyłacze; zapisać mapę pochodzenia etykiet.
4. W plikach LA nie importować bezpośrednio całego rozdziału DG-04 z grupami Spin i spinorami; rozdzielić sekcje tematyczne. Zapobiec kolizjom etykiet, wielokrotnemu `\chapter` i brakującym makrom.
5. Każdy nowy rozdział oddzielnie audytować matematycznie, redakcyjnie, terminologicznie i typograficznie, wykonywać regresje CI, sprawdzać odsyłacze i **eksportować samodzielny PDF**. Stabilizować dopiero po dwóch kolejnych czystych audytach i zielonym CI.
6. W języku polskim „chart” → „mapa”, „mapping” → „odwzorowanie”, „sequence” → „ciąg”; bez nieuzasadnionych skrótów dowodów. Rysunki i podpisy podlegają tej samej kontroli.

## Zakres osobnych skryptów

Blok sterowania (25–28) można docelowo wydzielić do osobnego skryptu o teorii sterowania. Grassmanniany i algebry Clifforda pozostają jednak **również w planie algebry liniowej**, ze wskazaną kanoniczną zawartością DG-04 jako materiałem źródłowym.
