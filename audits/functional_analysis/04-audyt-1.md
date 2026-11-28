# Analiza funkcjonalna — rozdział 04 — audyt 01

**Data:** 23 listopada 2026 r.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/functional_analysis/04-zbiory-ograniczone-rodziny-operatorow-i-metryzowalnosc.tex.
**Wynik:** audyt z poprawkami w źródle i testach, nie zalicza się jako czysty. **Rozdział 04 NIEUSTABILIZOWANY.**

## Zakres i procedura

Niezależny przegląd pełnych 9 dowodów, 5 środowisk przykładów, 15 etykiet, założeń topologicznych, prawidłowości definicji ograniczoności von Neumanna, równociągłości, dwóch topologii na przestrzeniach operatorów, metryzowalności oraz testów i rysunków. Sprawdzono przypadki brzegowe, m.in. pustą rodzinę operatorów, pusty zbiór, zerowy wymiar i rodzinę produktów nieskończonych.

## Macierz matematyczna — 9/9 dowodów sprawdzonych

1. **Ciągowe kryterium ograniczoności:** z ograniczoności B dostajemy λ_nx_n→0 dla dowolnego λ_n→0 i x_n∈B, korzystając ze zrównoważonego otoczenia. Kontrapozycja: dla zrównoważonego U i dowolnego n wybieramy x_n poza nU, λ_n=1/n, co obala (ii). **PASS**.
2. **Podstawowe działania na zbiorach ograniczonych:** suma, suma zbiorów, skalowanie, podzbiory i domknięcie zachowują ograniczoność. Domknięcie kontrolowane przez otwarte symetryczne V z V+V⊂U i zawieranie cl(V)⊂V+V. Sprawdzono zbiór pusty oraz λ=0. **PASS**.
3. **Kryterium lokalnej ograniczoności:** istniejące ograniczone otoczenie można zastąpić zrównoważonym; rodzina jego homotetii jest bazą otoczeń zera. Z powrotem, jeżeli homotetie U tworzą bazę, U jest ograniczony. **PASS**.
4. **Równociągłość przenosi zbiory ograniczone na ograniczone:** jeden wspólny wybór U dla całej rodziny operatorów, następnie B⊂tU. Dla każdej rodziny równociągłej wynika ograniczoność punktowa. **PASS**.
5. **Równociągłość w przestrzeniach unormowanych:** ekwiwalencja ze skończonym supremum norm operatorowych, przez skalowanie punktów normy ≤1 i wybór promienia ε/(M+1). Dla pustej rodziny operatorów jawnie ustalono supremum równy zero. **PASS**.
6. **Topologie punktowa i jednostajna na zbiorach ograniczonych w L(X,Y):** topologia punktowa jest topologią podprzestrzeni produktu Y^X. Topologia τ_b powstaje z bazowych warunków N(B,V); dodawanie kontrolowane przez W+W⊂V, mnożenie przez skalar przez boundedness T₀(B); singletony są ograniczone, więc τ_b jest silniejsza od τ_s. Hausdorff i charakterystyki zbieżności poprawne. **PASS**.
7. **Ograniczoność rodzin operatorów w τ_s i τ_b:** w τ_s redukcja do wszystkich ewaluacji i kryterium ograniczoności produktu; w τ_b dokładnie ograniczoność połączonego obrazu T(B) dla każdego ograniczonego B. Skończone przecięcia zrównoważonych otoczeń nie zmieniają kwantyfikatorów. **PASS**.
8. **Norma operatorowa jako topologia τ_b:** na przestrzeniach unormowanych kule operatorowe i N(B,V) wyznaczają tę samą topologię; w skończonym wymiarze normy współrzędnych są kontrolowane przez zwartość powierzchni max|a_i|=1, co daje τ_s=τ_b. Przypadek dim X=0 jawny. **PASS**.
9. **Kryterium metryzowalności TVS:** konstrukcja łańcuchowej metryki niezmienniczej względem przesunięć z malejącej bazy U_n, warunek potrójnej sumy U_{n+1}+U_{n+1}+U_{n+1}⊂U_n, indukcja po liczbie odcinków przecinająca połowę wagi i wnioski U_{n+1}⊂B_d(0,2^{-n})⊂U_{n-1}; dodatnia określoność i identyczność kanonicznych struktur jednostajnych. Dodano wprost traktowanie pustego podłańcucha w indukcji. **PASS po doprecyzowaniu**.

## Przykłady — 5/5 skontrolowanych

1. **Otoczka wypukła kuli w L^p, 0<p<1:** rozłączne przedziały I_{n,j}; funkcje n^{1/p} χ_{I_{n,j}} należą do kuli, a ich średnia ma miarę p-tą n^{1-p}→∞. To dowodzi braku lokalnej wypukłości. **PASS**.
2. **Lokalna ograniczoność a normowalność:** produkt K^N nie ma ograniczonego otoczenia, a L^p, 0<p<1, jest lokalnie ograniczona i nienormowalna. **PASS**.
3. **Punktowa ograniczoność bez równociągłości:** w c_{00} z normą supremum T_n(x)=nx_n znika ostatecznie dla każdego x, lecz na ograniczonym zbiorze e_n daje wartości n. **PASS**.
4. **Różne topologie zbieżności operatorów:** T_n→0 w τ_s, ale nie w τ_b dzięki temu samemu zbiorowi B={e_n}. **PASS**.
5. **K^N metryzowalna i zupełna, lecz nienormowalna:** metryka sumy 2^{-n}min(1,|x_n−y_n|) odpowiada topologii i strukturze jednostajnej produktu; brak ograniczonego otoczenia zera. **PASS**.

## Wykonane poprawki w rozdziale 04

1. **Terminologia:** „Sekwencyjne kryterium ograniczoności” zastąpiono „Ciągowe kryterium ograniczoności”.
2. **Terminologia:** w definicji pierwszego aksjomatu przeliczalności usunięto niedopuszczone określenie „pierwszoprzeliczalną”; użyto konstrukcji „spełnia pierwszy aksjomat przeliczalności”.
3. **Funkcje charakterystyczne:** dwa wystąpienia niezgodnego ze standardem zapisu \mathbf1 zmieniono na \chi_A.
4. **Warunki brzegowe:** w stwierdzeniu o równociągłości w przestrzeniach unormowanych doprecyzowano konwencję sup pustej rodziny operatorów (wartość 0).
5. **Dowód metryzowalności:** dodano zdanie o zerowej różnicy końców pustego podłańcucha w indukcji dzielącej łańcuch według połowy łącznej wagi.
6. Uaktualniono metadane źródła („audyt III”); nie zmieniono żadnej z 15 etykiet i zachowano wszystkie 9 dowodów i 5 przykładów.

## Testy, odsyłacze i skład

- Dodano **tools/tests/test_functional_analysis_ch04.py**: 12 testów struktury, referencji, terminologii, skalarnych ciągów, otoczki wypukłej w L^p, rodzin T_n, topologii operatorowych, skończeniewymiarowej kontroli normy, metryki produktu i kroku indukcyjnego.
- Przy dwóch próbach nowego testu ciągowego kryterium ograniczoności CI wykrył **błąd precyzji porównania liczb zmiennoprzecinkowych**, nie błąd twierdzenia. W testach poprawiono porównania na tolerancyjne. Rejestr wcześniejszych nieudanych przebiegów zachowano w historii GitHub Actions; nie są traktowane jako pozytywna walidacja.
- Dodano **.github/workflows/functional-analysis-ch04.yml**: kompilacja w rzeczywistym kontekście rozdziałów 01–05, testy Python, kontrola brakujących odsyłaczy i błędów LaTeX, artefakt PDF. **Przebieg CI [45157298984](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157298984) zakończył się SUCCESS**: 12/12 testów PASS, kompilacja PASS, walidacja PDF i odsyłaczy PASS, zapis artefaktu PASS. Dodatkowo workflow zoptymalizowano, aby pomijał zbędne instalacje narzędzi PDF, gdy są już dostępne na runnerze.
- Rozdział nie zawiera odrębnego rysunku TikZ. Pobrano i sprawdzono rzeczywisty artefakt z przebiegu CI: **33 strony A4, 480542 bajty**; rozdział 04 znajduje się na stronach **22–27**. Przejrzano arkusz kontrolny stron 22–27 oraz stronę 25 w pełnej rozdzielczości. Wzory, odsyłacze, nagłówki i zakończenia dowodów są czytelne; nie stwierdzono kolizji ani obcięć. W końcowym logu LaTeX brak niezdefiniowanych odsyłaczy, przepełnionych wierszy i brakujących znaków.

## Wniosek

**Audyt 04/01: wykonany z korektami, więc NIE JEST CZYSTY.** Po pełnej walidacji CI należy kontynuować osobne, niezależne audyty rozdziału 04 aż do dwóch kolejnych czystych przebiegów, bez przechodzenia wcześniej do rozdziału 05.
