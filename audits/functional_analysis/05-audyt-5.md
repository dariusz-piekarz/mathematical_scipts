# Analiza funkcjonalna — rozdział 05 — audyt 05 (niezależna kontrola stabilizacyjna)

**Data:** 23 listopada 2026 r.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/functional_analysis/05-przestrzenie-lokalnie-wypukle-i-seminormy.tex`.
**SHA źródła:** `2b72d6c88f413021d695024481b1a4a5c466476c`.
**Wynik:** CZYSTY przegląd matematyczny i strukturalny; druga kolejna czysta kontrola po korekcie 05/03. **2/2** dla niezmienionego źródła. Nie wykonano w tej iteracji nowego CI ani ponownego oglądu PDF; wykorzystano zweryfikowany zakończony przebieg dla tej wersji źródła.

## Ustalenie punktu startowego

Odczytano katalog raportów `audits/functional_analysis/`: najnowszy zastany raport to `05-audyt-4.md`, a nie `05-audyt-2.md`. Audyt 05/03 zawierał trzy poprawki i reset licznika do 0/2; audyt 05/04 był czysty (1/2). Przed zapisem tego raportu sprawdzono, że `05-audyt-5.md` nie istnieje. Bieżące źródło ma SHA identyczne z raportem 05/04.

## Niezależna kontrola 13/13 dowodów

1. Kryterium absolutnej wypukłości: obie implikacje, przypadek współczynników zerowych i zespolonych — poprawne.
2. Absolutnie wypukła baza: otwartość otoczki wypukłej z perturbacji składnika o dodatniej wadze — poprawne.
3. Topologia seminorm: ciągłość działań, minimalność, Hausdorff i zbieżność sieci — poprawne.
4. Funkcjonał Minkowskiego: homogeniczność nad C, podaddytywność, inkluzje i równość dla otwartego A — poprawne.
5. Lokalna wypukłość przez seminormy: ciągłe funkcjonały Minkowskiego i rozdzielanie punktów — poprawne.
6. Ciągłość odwzorowania liniowego: oszacowanie jednorodne, w tym przypadek maksimum seminorm równego zero — poprawne.
7. Ograniczoność: równoważność z ograniczeniem wszystkich seminorm, także dla B pustego — poprawne.
8. Ograniczoność otoczki absolutnie wypukłej: oszacowanie przez sumę modułów współczynników — poprawne.
9. Kryterium Kolmogorowa: ograniczone otwarte otoczenie daje normę; jądro seminormy znika dzięki Hausdorffowi — poprawne.
10. Przeliczalne seminormy i metryzowalność: obie implikacje, nierówność trójkąta dla min(1,p) i kontrola ogona szeregu — poprawne.
11. Sieci Cauchy'ego: wspólny indeks dla skończonej liczby seminorm — poprawne.
12. Zupełność C∞([0,1]): granice jednostajne pochodnych, przejście przez całkę i zgodność pochodnych — poprawne.
13. Podprzestrzenie, produkty i ilorazy: zachowanie wypukłości i otwartość rzutowania ilorazowego — poprawne.

## Niezależna kontrola 5/5 przykładów

1. Seminormy współrzędnych, pochodnych i supremum na zwartych K; przypadek K pustego jawnie określony.
2. Pas w R²: seminorma |x| nie jest normą.
3. c00: nieciągły funkcjonał Minkowskiego z ciągiem e_n/n.
4. Produkt K^N: metryzowalność i zupełność bez normowalności.
5. C∞([0,1]): nienormowalność przez funkcje oscylacyjne i dowód zupełności.

Ponadto sprawdzono argument o zerowości ciągłych funkcjonałów na L^p, 0<p<1: podział miary |f|^p dλ na równe części i wykładnik 1-1/p<0 są prawidłowe.

## Struktura i odsyłacze

Bezpośredni odczyt aktualnego pliku: **13** otwarć i **13** zamknięć proof; **5** przykładów; **19** etykiet, bez duplikatów; **14** odsyłaczy. Odsyłacze lokalne znaleziono w AA-05, a trzy różne cele zewnętrzne potwierdzono przez odczyt rozdziałów analizy funkcjonalnej 02–04:
- `sec:konstrukcje` — rozdział 02;
- `sec:zupelnosc` — rozdział 03;
- `sec:rodziny-metryzowalnosc` — rozdział 04.

Terminologia polska i warunek `p_A(x)>0` przy diagramie pozostają poprawne.

## CI, LaTeX, PDF — precyzyjny status

Odczytano rzeczywisty GitHub Actions run [45171617783](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45171617783): **status completed, conclusion success, head SHA 8ecfecb54508cb942e45ac657e06278755d15582**. Raport 05/04 dokumentuje dla tego niezmienionego źródła **18/18 testów PASS**, kompilację oraz inspekcję stron PDF 27–33 (33-stronicowy artefakt). W tej iteracji nie pobrano ponownie PDF i nie uruchomiono nowego CI; nie przedstawia się powtórnej lektury raportu jako nowego testu. Zmiana wyłącznie w raporcie audytowym nie modyfikuje SHA źródła.

## Werdykt i następny rozdział

**Czysty audyt 05/05, 13/13 dowodów, 5/5 przykładów; 2/2 kolejnych czystych audytów po ostatniej korekcie. Rozdział 05 uznany za STABILNY** na źródle `2b72d6c88f413021d695024481b1a4a5c466476c`, w świetle zakończonego CI i dokumentacji PDF z 05/04. Nie wykryto błędu wymagającego poprawki ani resetu licznika. **Następna iteracja:** rozpocząć wyłącznie rozdział 06, twierdzenie Hahna–Banacha; w tej iteracji go nie otwierano.
