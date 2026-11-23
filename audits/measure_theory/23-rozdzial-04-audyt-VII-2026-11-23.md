# Miara i całka — rozdział 04, audyt VII (iteracja XXIII)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Jedyny audytowany rozdział:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.

## Kontynuacja od rzeczywistego stanu

Ponownie odczytano aktualny blob R04 `ce0105f63aa4da494cf5f2f5e9e2b26fc6389fd4`, istniejący raport `22-rozdzial-04-audyt-VI-2026-11-23.md` (blob `c973541d9aaa1d164d8c01e591bde0b873438e60`), obydwa testy R04 i ostatnie commity. Rozdział 04 nie był od raportu XXII zmieniany. R01–R03 pozostają kontekstem odsyłaczy; żadnego innego rozdziału nie audytowano ani nie edytowano. Przejrzano też bieżące reguły `AGENTS.md` i `docs/pl/standardy_terminologiczne.md` z poprzedniego audytu.

## Nowa niezależna kontrola merytoryczna

Wybrano trudny przypadek z dowodu twierdzenia `thm:invariance-lebesgue`, tj. **ujemny współczynnik skalowania**. Dla `Q=[a,b)` i `t<0` obraz `tQ` jest `(tb,ta]`, a nie `[tb,ta)`. Z tego powodu argument pokryciowy z wierszy 368–378 musi używać półotwartych *powiększeń* przedziałów, nie samych obrazów. Sprawdzono poprawność tego kroku: dla każdego `eps>0` zbiór `(tb,ta]` zawiera się w `[tb-eps,ta+eps)`, a długość pokrycia wynosi `|t|(b-a)+2eps`. W wymiarze `d` analogicznie powiększa się boki i rozdziela sumaryczny błąd objętości na `eta_n`; argument z rozdziału pozostaje poprawny. Translacja nie zmienia długości i nie zmienia rodzaju domknięcia końców.

Zbadano także użycie kryterium Carathéodory'ego w wierszach 380–398: dla bijekcji afinicznej `S` preobrazy rozcinają zbiór `T` na rozłączne części, a dodatni czynnik `|t|^d` można wyłączyć z obu składników; nie znaleziono nowej luki w tym dowodzie. Zbadano powiązanie z lematem o hiperpłaszczyznach: końce w wymiarze 1 i ściany w wyższych wymiarach mają miarę zero, więc dopiero po wykazaniu mierzalności można ignorować ich obecność w formule na miarę.

Nie wykryto konieczności modyfikacji matematycznego tekstu R04. Zachowano etykiety, zakres i strukturę.

## Mierzalny postęp: dodatkowy test regresyjny

W `tools/test_measure_theory_ch04_geometry.py` dodano `affine_interval_regression()` dla **36 wymiernych konfiguracji** (3 przedziały × 4 skale, w tym 2 ujemne × 3 translacje), sprawdzający długość obrazu, prawidłowy typ półotwartych końców oraz dwie wartości błędu powiększenia dla ujemnych skal. Test wykorzystuje `fractions.Fraction`, a więc rachunek dokładny. Dotychczasowe testy nie zostały usunięte. Zmiana: commit **`c9f6a3d635ab0c3e96384db09da1d11fd6120d54`**, zweryfikowany ponownym odczytem GitHub, blob **`a432d2f3862181f870bd079622b7ce623c95128b`**.

Niezależnie przeliczono te same 36 konfiguracji w bieżącej sesji narzędziowej (JavaScript): **36/36 zgodnych** z oczekiwaną długością obrazu; zero rozbieżności. Jest to niezależna kontrola arytmetyczna. **Nie należy jej mylić z wykonaniem nowego skryptu Python na runnerze CI.**

## Status kompilacji i pozostałe sprawy

W tej iteracji nie uruchomiono pełnego `pdflatex` dla R04 ani całej książki i nie pobrano artefaktów GitHub Actions. Wobec braku zweryfikowanego końcowego przebiegu obu jobów nie można uznać kompilacji, paginacji i odsyłaczy w pełnej książce za ostatecznie potwierdzone. Poprzedni audyt XXII wykazał poprawną kompilację tylko izolowanego wycinka o funkcji Lipschitzowskiej; nie przenosimy tego wyniku na cały dokument.

**Status R04: NIESTABILNY / w trakcie stabilizacji**, mimo że w bieżącej kontroli merytorycznej nie znaleziono nowych błędów. Wymagane: rzeczywisty pełny przebieg CI, przegląd całego wielostronicowego PDF i dodatkowy czysty audyt po ostatniej poprawce treści. Nie przechodzić do R05. Propozycji nowych twierdzeń i przykładów w tej iteracji nie zgłaszano.
