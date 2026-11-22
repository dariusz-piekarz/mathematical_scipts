# Algebra liniowa — LA-31, dodatkowy niezależny audyt rozpoczęty przed równoległym zamknięciem (2026-11-22)

**Repozytorium/gałąź:** `dariusz-piekarz/mathematical_scipts`, wyłącznie `biblioteka-matematyczna-iteracja-6`. **Źródło:** `chapters/pl/linear_algebra/31-grupy-pin-spin-i-spinory.tex` (1496 wierszy). **Zweryfikowany blob:** `6c1d09b9eaf4083c9ebaa361dbf46fc350eae147`. **Wynik tej niezależnej kontroli: czysty**, bez zmiany źródła.

## Stan współbieżnych prac

Przy rozpoczęciu pobrano HEAD `440c78107c2bd4f94cc8fed541f1c05fd9007b4c`, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, katalog 01–32, katalog audytów i aktualny postęp. Wówczas rejestr wskazywał LA-31, **audyt 02**, po jednym czystym audycie 01. W toku niezależnej kontroli inni wykonawcy zapisali już [audyt 02](31_iteration_02_2026-11-22.md) oraz odrębny [audyt końcowy 03](31_iteration_03_2026-11-22.md) na identycznym blobie i zamknęli LA-31, przesuwając kolejkę do 32. **Niniejszy raport dokumentuje odrębną, rozpoczętą wcześniej kontrolę**, nie udaje wykonania cudzych audytów i nie zmienia kolejki ani liczników stabilizacji. Nie ponawiano zamkniętych etapów po stwierdzeniu równoległego zamknięcia.

## Zakres matematyczny — przeczytany cały rozdział

1. Rewersja i automorfizm parzystości; wzór na odbicia `-uvu^{-1}`, różnica między zwykłym i skręconym sprzężeniem. Sprawdzono konwencję `v^2=-\|v\|^2` i poprawność działania `Pin(n)`.
2. `Spin(n)→SO(n)`: rozkład izometrii na odbicia, obliczenie jądra przez monomy parzyste, jednostkowa norma słowa `s\widetilde{s}=1`, lokalna sekcja rotorowa `R(a,b)=(1-ba)/\|a+b\|`, argument o otwartych płatach i gładkości.
3. Przypadki `Spin(2)`, `Spin(3)`, kwaterniony oraz interpretacja podwojenia kąta. Dokładna kontrola znaków w iloczynach.
4. Klasyfikacja zespolonych algebr Clifforda i modułów przez macierze Pauliego, krok o dwa w wymiarze, algebrę parzystą i dwa moduły w wymiarach nieparzystych.
5. Chiralia `Γ=i^m c(e_1\cdots e_{2m})`, kwadrat i komutowanie, dowód nieredukowalności obu półspinorów i ich nieizomorficzności.
6. Macierze SU(2), wzór na sferę Blocha `b(ψ)`, projektor `ψψ^*=(I+Σb_jσ_j)/2`, ekwiwariantność i mapy `CP¹`.
7. Konstrukcje wiązki głównej `P_Spin`, współrzędne spinorów, wiązka stowarzyszona, działanie Clifforda niezależne od wyboru ramki; spinowość `S²`, cztery znaki torusa i funkcje półokresowe.
8. Wiązka tautologiczna jako przykład braku struktury spinowej, podniesienia na zbiorach ściągalnych, znaki potrójnych przecięć, ich kocykl i przeszkoda `w₂`, oraz ekwiwariantne odwzorowania odpowiadające polom spinorowym. Nie stwierdzono koła logicznego; zewnętrzne twierdzenie o dobrej kohomologii Čech jest jawnie oznaczone.

## Rzeczywiście wykonane testy

- Uruchomiono własny skrypt `/mnt/data/la31_audit/independent_tests.py`: **94 639 PASS, 0 FAIL**. Obejmuje dokładne iloczyny bitmaskowe Clifforda w wymiarach 2–6, automorfizm parzystości, rewersję, kwadraty wektorów, wymierne odbicia Pin, koniugację par generatorów Spin, element objętości i znaki chiralności, testy macierzy `SU(2)` i równań Blocha oraz tożsamość `\delta^2=0` w znakach Čech. Testy wykorzystują `fractions.Fraction` i deterministyczne dane losowe; bez użycia skryptów poprzednich audytów.
- Statyka źródła: **33 unikalne etykiety, 27 rozwiązywalnych odsyłaczy** w LA-29/30/31, **58 poprawnie domkniętych środowisk**, 4 rysunki TikZ (3 w otoczeniach `figure`), bez znalezionych zakazanych form terminologii.
- [CI 45039588413](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45039588413) **completed/success**, commit `d72200bdb24dfd4817aba0c42dcb14c7fc9a7a34` z identycznym blobem LA-31.
- Pobierano **rzeczywisty artefakt** `linear-algebra-ch01-ch32` z tego przebiegu. Z niego wyodrębniono **14 stron LA-31 (fizyczne 296–309)** do `/mnt/data/la31_audit/linear_algebra_ch31.pdf`. Renderowano i obejrzano wizualnie **wszystkie 14 stron**, w tym diagramy dwukrotnego nakrycia, Blocha, torusa i lokalnych ramek. Nie zauważono kolizji lub ucięć.
- W pliku `linear_algebra.log` po CI liczba wystąpień `Overfull \\hbox`, `Overfull \\vbox`, niezdefiniowanych odsyłaczy i `LaTeX Error` wynosi **0**.

## Decyzja

**Kontrola czysta; źródło bez edycji.** Równolegle zaakceptowane raporty 01, 02 i 03 dokumentują wymagane 2+1 czystych audytów oraz zielone CI, więc **LA-31 pozostaje zamknięty**. Dokumentacja niniejsza nie zawyża liczników. **Aktualny następny etap: LA-32**, z zatwierdzonym planem dodatku Penrose’a; nie zaczynać już ponownie LA-31 bez nowej rzeczowej usterki.
