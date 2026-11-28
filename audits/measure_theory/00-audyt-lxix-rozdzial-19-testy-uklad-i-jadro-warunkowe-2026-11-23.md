# Audyt LXIX (69) — rozdział 19, regresje, paginacja i jądro warunkowe

Data: 2026-11-23.
Repozytorium: dariusz-piekarz/mathematical_scipts.
Gałąź: biblioteka-matematyczna-iteracja-6 (wyłącznie istniejąca).
Źródło: chapters/pl/measure_theory/19-zastosowania-twierdzenia-radona-nikodyma.tex.
SHA bloba po ostatniej poprawce: 7571e99edac729831e83e8061377757874cfb7bc.

## 1. Niezależny przegląd dowodów

Ponownie zbadano zmianę miary (w tym równoważność całkowalności), obraz miary i warunkową wartość oczekiwaną gęstości, normę wariacji całkowitej na prawdopodobieństwach i monotoniczność po zastosowaniu odwzorowania. Skontrolowano formułę testu progowego Neymana–Pearsona, w tym c=0, losowanie na granicy i dowód istnienia progów o dokładnym poziomie alfa. Przejrzano też wzór Bayesa dla skończonych przestrzeni parametrów, wyciąganie czynnika mierzalnego, warunkową nierówność Jensena, kontrakcję Lp, nierówność Gibbsa oraz zasadę przetwarzania danych dla entropii względnej. Nie stwierdzono nowego błędu w tezach wymagającego ich zmiany.

Weryfikacja dodanego w audycie LXVIII przykładu Neymana–Pearsona: na X={a,b}, P=(7/10,3/10), Q=(1/5,4/5), alfa=3/20, c=8/3 i gamma=1/2, test losowy phi*=1/2 chi_{b} ma poziom 3/20 i moc 2/5; każdy test deterministyczny tego poziomu jest zerowy.

## 2. Pierwszy potwierdzony przebieg CI i wada paginacji

Przebieg: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45271423948
Commit: 92d1b4b9e5404a9e0c283968cbe7f6517b7b0948.
Obydwa statusy GitHub: measure-theory/ch19-regressions=success oraz measure-theory/ch19-pdf=success.
Logi: 8/8 testów rozdziału 19 + 4/4 testy całej książki = 12/12 PASS. Pełna książka 259 stron, izolowany rozdział 19 siedem stron. Zaimportowano 4 odsyłacze zewnętrzne, zachowując 19 etykiet lokalnych.
Rzeczywisty artefakt ZIP 14864579654 pobrano. Finalne logi nie zawierają Overfull hbox ani niezdefiniowanych referencji; w pełnej książce 14 Underfull hbox i 56 nieblokujących ostrzeżeń hyperref. Obrazy wszystkich 7 stron wykazały wyłącznie istotny problem redakcyjny: rozdział kończył się osobną, niemal pustą stroną 7.

## 3. Iteracje poprawy składu

Aby sprawdzić możliwość uniknięcia niemal pustej siódmej strony, commit c27c2614fdffb6289ab73b6ffb3ec947262cd383 dodał lokalne enlargethispage{4 baselineskip}. Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45272762350 zakończył się dwoma statusami success (8+4 testy OK, książka 258 stron, rozdział 19 sześć stron). Jednak rzeczywisty podgląd strony 6 wykazał, że ostatni akapit został przesunięty zbyt blisko fizycznej dolnej krawędzi kartki. Brak Overfull hbox nie usprawiedliwia takiego efektu. Wersji sześcio-stronicowej NIE zaakceptowano jako wizualnie stabilnej.

Zamiast sztucznie zmniejszać dolny margines, usunięto wymuszenie wysokości i rozbudowano sekcję Ograniczenia i dalsze kierunki o ścisły, samodzielny przykład regularnego rozkładu warunkowego:
- Ω=(0,1), P=λ, Y=Θ=id;
- K(y,A)=chi_A(y)=δ_y(A), co spełnia tożsamość warunkowej miary po całkowaniu względem prawa Y;
- w dowolnym ustalonym punkcie y0 można zastąpić δ_{y0} inną miarą probabilistyczną rho, nie naruszając tej tożsamości, ponieważ P_Y({y0})=0;
- jest to konkretna demonstracja, że rozkład warunkowy nie jest wyznaczony punktowo kanonicznie nawet na przestrzeni standardowej borelowskiej.

Commit uzupełnienia: 8e5e3cf8bfbf464383a8c425d940b5f277acb481. Przy niezależnym sprawdzeniu doprecyzowano, że rho ≠ δ_{y0}, aby dwa jądra rzeczywiście się różniły: commit 7fa829c38b3e3b8f005d16f0990801cefd827b80.
Zweryfikowany SHA po obu zmianach: 7571e99edac729831e83e8061377757874cfb7bc. Źródło nie zawiera już enlargethispage, etykiety rozdziału są unikalne (19 deklaracji), wszystkie środowiska są poprawnie domknięte.

## 4. Granica bieżącej weryfikacji

CI dla pierwotnej wersji i dla *odrzuconej wizualnie* wersji sześcio-stronicowej zostały rzeczywiście potwierdzone. Te zielone przebiegi NIE walidują najnowszej wersji zawierającej przykład jądra warunkowego. Dla tej wersji trzeba odczytać aktualne dwa statusy na commicie 7fa829c38b3e3b8f005d16f0990801cefd827b80, logi, pełny PDF i nowy PDF rozdziału, a także obejrzeć wszystkie strony — szczególnie ostatnią. Bez tego nie zamykać rozdziału 19.

Werdykt LXIX: poprawki matematyczne i redakcyjne zapisane, problem zbyt małego marginesu usunięty u źródła; rozdział 19 nadal w stabilizacji do ponownej pełnej walidacji ostatniego bloba. Nie zaczynać rozdziału 20.
