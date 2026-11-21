# Algebra liniowa — rozdział 03, audyt 4

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex`  
**Commit treści po poprawce:** `7e793414cf34297ad326bbb0e7e90490d38b7558`

## Kryterium audytu

Czwarty audyt obejmował wyłącznie poprawność istniejącego materiału: definicji, twierdzeń, dowodów, przykładów, założeń, przypadków zerowych, odsyłaczy oraz kompilacji. Zakres rozdziału pozostawiono bez zmian. **Nie dodano żadnych twierdzeń, lematów, definicji ani nowych przykładów.**

## Wykryta rzeczywista usterka

W dowodzie Stwierdzenia `prop:lin3-generatory-przeciwobrazy` (obraz przestrzeni rozpiętej i przeciwobrazy podprzestrzeni) zastosowano niepoprawny zapis
\[
v=\sum_{j=1}^m a_ja_j,\qquad a_j\in A.
\]
Ta sama nazwa \(a_j\) oznaczała jednocześnie skalar i wektor z \(A\), choć w ogólnej przestrzeni wektorowej iloczyn dwóch wektorów nie jest w ogóle określony. Analogiczna dwuznaczność występowała dalej w dowodzie obydwu zawierań.

**Poprawka:** zapisano pełną kwantyfikację: dla \(v\in\operatorname{span}(A)\) istnieją \(m\in\mathbb N_0\), współczynniki \(\lambda_j\in K\) i wektory \(a_j\in A\), takie że
\[
v=\sum_{j=1}^{m}\lambda_ja_j.
\]
Liniowość daje
\[
T(v)=\sum_{j=1}^{m}\lambda_jT(a_j)
\in\operatorname{span}(T(A)).
\]
Odwrotnie każdy \(y=\sum_j\lambda_jT(a_j)\) należy do \(T(\operatorname{span}(A))\), ponieważ \(y=T(\sum_j\lambda_ja_j)\).
Jawnie doprecyzowano także przypadek \(A=\varnothing\), gdy obie strony są podprzestrzeniami zerowymi.

Druga część istniejącego stwierdzenia, dotycząca przeciwobrazu \(T^{-1}(Z)\), była poprawna i nie wymagała zmiany.

## Powtórna kontrola wszystkich rozdziałowych wyników

1. **Definicja i kryteria liniowości:** zachowywanie dodawania, mnożenia przez skalar, wektora zerowego i wszystkich skończonych kombinacji jest uzasadnione; poprawne są przykłady nad ciałami dowolnej charakterystyki.
2. **Wartości na bazie Hamela:** istnienie i jednoznaczność przedłużenia oraz zgodność na generatorach są poprawne, w tym dla bazy pustej; przy wskazanej bazie konstrukcja nie wymaga aksjomatu wyboru.
3. **Jądro i obraz:** podprzestrzenność, kryteria iniektywności/surjektywności, obrazy i przeciwobrazy podprzestrzeni zostały sprawdzone. Naprawiono wyłącznie niepoprawne oznaczenia w dowodzie równości \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\).
4. **Wymiar jądra i obrazu:** rozszerzenie bazy jądra do bazy \(V\) i konstrukcja bazy obrazu przez pozostałe wektory są poprawne; rozdzielono argument z aksjomatem wyboru od skończenie wymiarowego.
5. **Izomorfizm \(V/\ker T\cong\operatorname{im}T\):** dobra określoność, liniowość, iniektywność i surjektywność są uzasadnione. Diagram prawidłowo odróżnia przeciwdziedziny \(\widehat T\colon V\to\operatorname{im}T\) i \(T\colon V\to W\).
6. **Składanie i izomorfizmy:** liniowość złożeń i odwrotności, zachowanie baz oraz skończenie wymiarowe kryterium równoważności iniektywności i surjektywności są poprawne.
7. **Przestrzenie \(\operatorname{Hom}\), \(\operatorname{End}\):** konstrukcja bazy z \(mn\) odwzorowań \(E_{ji}\) obejmuje również przypadki \(m=0\) i \(n=0\); poprawne są łączność i dwuliniowość składania, w tym wyjaśnienie algebry endomorfizmów przestrzeni zerowej.
8. **Projekcje algebraiczne:** warunek \(P^2=P\) jest zgodny z rozkładem na obraz i jądro oraz identycznością na obrazie; projekcja zadana wskazanym dopełnieniem jest liniowa i jednoznaczna. Przykłady na \(K[X]\) i \(\mathbb R^2\) są poprawne.

Nie wykryto innego błędu podważającego istniejące tezy. Nie zmieniono innych dowodów.

## Niezależny test kontrolny

Dla wszystkich **512** liniowych endomorfizmów \(T\colon\mathbb F_2^3\to\mathbb F_2^3\) i wszystkich **256** podzbiorów \(A\subseteq\mathbb F_2^3\) sprawdzono porównaniem zbiorów:
\[
T(\operatorname{span}(A))=\operatorname{span}(T(A)).
\]
Przetestowano **131072 przypadki**, w tym **512 przypadków \(A=\varnothing\)**. **Nie wykryto rozbieżności.** To test dodatkowy, nie substytut dowodu.

## Kontrola statyczna i zależności

- Rozdziały 01–03: **150 unikalnych etykiet**, bez kolizji.
- **62 odsyłacze** `\\ref` i `\\eqref`, wszystkie z istniejącymi celami.
- Środowiska `\\begin`/`\\end` poprawnie zagnieżdżone.
- Zachowano wymagane „suma zbiorów” i „warunek niezależności liniowej” w treści matematycznej, bez zmiany stabilnych nazw `\\label`.
- Wszystkie trzy rozdziały pozostają w katalogu i w pliku głównym we właściwej kolejności.
- Rozdziały nie wymagają zewnętrznych plików graficznych.

**CI dla poprawki:** [44904330466](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44904330466) — **success**. Wszystkie kroki walidacji rozdziałów 01–03, importów, katalogu, terminologii, odsyłaczy, dwukrotnej kompilacji i publikacji artefaktu zakończyły się powodzeniem. Powstał **37-stronicowy PDF A4**. W końcowym pliku `linear_algebra.log` nie ma ostrzeżeń `LaTeX Warning`, `Overfull`, `Underfull`, `Missing character`, `Undefined control sequence` ani `Fatal error`. Wyrenderowano i wizualnie skontrolowano **strony 30–31** z poprawionym dowodem, a także rozkład stron końcowych; zapis współczynników i wektorów jest czytelny, bez ucięć i kolizji. W nieblokującej globalnej walidacji innych skryptów nadal zgłaszane są **24 wcześniejsze problemy** niezwiązane z rozdziałem.

## Status

**Audyt 4 zakończony z rzeczywistą poprawką matematycznego zapisu dowodu. Rozdział 03 pozostaje otwarty.** Kolejny audyt ma ponownie przeanalizować istniejący materiał, bez rozszerzania zakresu; po czystym audycie i poprawnym CI można zamknąć rozdział.
