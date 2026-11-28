# Audyt LXXIII (73) — rozdział 20: zamknięcie po CI i PDF

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: chapters/pl/measure_theory/20-miary-borelowskie-regularnosc-i-miary-radona.tex.
**Aktualny blob źródła:** 8545b0586adb31dd63a8dba53eb8bc2c51489b01.
**Blob testu:** 353e63c0ad7dde0bd9486c067e5a592d9ceccae0.
**Zweryfikowany commit:** 8b4040863ab0c84e195d21278b0e43b5d59084c1.

## 1. Niezależny przegląd matematyczny

Po audytach LXXI i LXXII jeszcze raz zbadano:
1. Rozróżnienie regularności zewnętrznej, wewnętrznej względem zbiorów domkniętych i zwartych, ciasności i obu konwencji Radona, w tym uwagę do przyszłego przykładu Haara.
2. Dowód aproksymacji borelowskich E w przestrzeni metrycznej przez F domknięty i U otwarty dla skończonej miary, przez klasę zbiorów aproksymowalnych będącą sigma-algebrą.
3. Ciasność na przestrzeni polskiej: przekrój zamkniętych skończonych pokryć na skalach 2^-n jest zupełny i całkowicie ograniczony, więc zwarty.
4. Dowód regularności lokalnie skończonej miary na ośrodkowej lokalnie zwartej przestrzeni metrycznej przez przeliczalne pokrycie i rozłączne części.
5. Twierdzenie o pełnej mierze nośnika na przestrzeniach spełniających drugi aksjomat przeliczalności oraz kontrprzykład w nieprzeliczalnej przestrzeni dyskretnej.
6. Lemat o funkcji odcinającej, jednoznaczność miary przez całki C_c i gęstość C_c w Lp, 1≤p<∞.
7. Nowy wniosek o nośniku: x∈supp μ wtedy i tylko wtedy, gdy dla każdej f∈C_c(X), f≥0 oraz f(x)>0, całka ∫f dμ jest dodatnia. Dowód używa dodatniego otoczenia x i odwrotnie funkcji odcinającej skupionej w zerowym otoczeniu.
8. W dowodzie gęstości Lp zachowano konieczną poprawkę: obcięcie f_n znika poza A_n={|f|>1/n}, dla którego μ(A_n)≤n^p ∫|f|^p dμ<∞. Nie wynika stąd automatycznie skończoność miary topologicznego nośnika obcięcia.

Poprawki z trzech iteracji obejmują terminologię drugiego aksjomatu przeliczalności, usunięcie błędnego utożsamienia zbioru niezerowości z nośnikiem topologicznym i uzupełniony wniosek. Nie wykryto dalszego błędu matematycznego wymagającego zmiany źródła.

## 2. Potwierdzenie CI aktualnej wersji

Run: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45276811724
Head SHA: 8b4040863ab0c84e195d21278b0e43b5d59084c1.
Statusy commitu: measure-theory/ch20-regressions=success; measure-theory/ch20-pdf=success. Oba odnoszą się do tego samego przebiegu.

Wszystkie trzy joby completed/success:
- testy (138051372767): Ran 8 tests ... OK i Ran 4 tests ... OK; razem 12/12;
- PDF (138051373648): książka 259 stron, 1 899 144 bajty; izolowany rozdział 20: 8 stron, 281 823 bajty; poprawnie zaimportowano 2 etykiety zewnętrzne i zachowano 21 lokalnych; referencje rozwiązane;
- publikacja statusów (138052847559): success.

## 3. Oryginalny PDF i oględziny

Pobrano rzeczywisty artefakt GitHub Actions 14867183519, measure-theory-ch20-pdf-and-logs (ZIP 2 758 391 bajtów). Otworzono oba oryginalne PDF-y, sprawdzono liczbę stron i wykonano montaż wszystkich ośmiu stron samodzielnego rozdziału. Nagłówki, wzory i tekst są czytelne, nie wykryto kolizji ani uciętego tekstu. Nowy wniosek pojawia się czytelnie na stronie szóstej, a strona ósma zawiera dwie całe sekcje (20.8 i 20.9), a nie osierocone dwa wiersze.

Końcowe logi: książka — 0 Overfull hbox, 14 nieblokujących Underfull hbox, 0 nierozwiązanych odsyłaczy, 56 ostrzeżeń hyperref o zakładkach PDF; rozdział 20 — 0 Overfull, 0 Underfull, 0 nierozwiązanych odsyłaczy. Ostrzeżenia wcześniejszych przebiegów latexmk nie są traktowane jako wynik końcowy.

## 4. Werdykt

**ROZDZIAŁ 20: STABILNY / ZAMKNIĘTY** dla bloba 8545b0586adb31dd63a8dba53eb8bc2c51489b01 po audytach LXXI–LXXIII, 8+4 zaliczonych testach i przeglądzie oryginalnego PDF. Nie jest to formalna certyfikacja dowodów.

Rozdziały 15–20 są zamknięte. Kolejna jednostka: rozdział 21 — twierdzenie reprezentacyjne Riesza–Markowa–Kakutaniego. Nie przechodzić do rozdziału 22 bez jego stabilizacji.
