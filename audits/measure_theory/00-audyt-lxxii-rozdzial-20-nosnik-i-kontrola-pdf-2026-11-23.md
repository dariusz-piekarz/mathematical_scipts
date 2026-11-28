# Audyt LXXII (72) — rozdział 20: drugi przegląd, nośnik przez C_c i PDF

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts.
Istniejąca gałąź: biblioteka-matematyczna-iteracja-6.
Bieżący rozdział: chapters/pl/measure_theory/20-miary-borelowskie-regularnosc-i-miary-radona.tex.

## Kontrola niezależna od LXXI

Ponownie przeanalizowano rozróżnienie regularności zewnętrznej i wewnętrznej na zbiorach zwartych, dowód regularności skończonych miar borelowskich na przestrzeniach metrycznych, ciasność miar na przestrzeniach polskich, uzyskanie miary Radona z lokalnej skończoności na ośrodkowej lokalnie zwartej przestrzeni metrycznej, nośnik miary, funkcje odcinające, jednoznaczność przez całki oraz gęstość C_c(X) w Lp.

W pierwszej iteracji poprawiono dwa błędy terminologiczne i jeden faktycznie nieprecyzyjny fragment argumentacji: obcięcie funkcji Lp znika poza mierzalnym A_n={|f|>1/n} o skończonej mierze z oszacowania Markowa, ale jego topologiczny nośnik nie musi być zawarty w takim zbiorze. Stan po tym poprawieniu: commit 63afe4f0b9c663adc10ec48fff8019ec9c2973fb.

## Rzeczywisty przebieg CI dla pierwszej korekty

Run: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45276140130
Commit: 63afe4f0b9c663adc10ec48fff8019ec9c2973fb.
Dwa statusy: measure-theory/ch20-regressions=success, measure-theory/ch20-pdf=success. Wszystkie trzy joby completed/success. Pełne logi:
- osiem testów rozdziału 20 i cztery testy integralności książki: 8/8 + 4/4 OK;
- cała książka: 259 stron, 1 897 683 bajty; izolowany rozdział 20: 8 stron, 279 190 bajtów;
- zaimportowano 2 zewnętrzne etykiety, zachowując 20 lokalnych; końcowe referencje rozwiązane.

Pobrano rzeczywisty artefakt 14867207351 (measure-theory-ch20-pdf-and-logs, ZIP 2 708 945 bajtów). W rozpakowanych końcowych logach:
- cała książka: 0 Overfull hbox, 14 nieblokujących Underfull hbox, 0 nierozwiązanych referencji, 56 nieblokujących ostrzeżeń hyperref dotyczących zakładek;
- rozdział 20: 0 Overfull hbox, 0 Underfull hbox, 0 nierozwiązanych referencji.

Wyrenderowano wszystkie 8 stron samodzielnego PDF w montażu i obejrzano je. Tekst i wzory są czytelne, nie ma kolizji. Zidentyfikowano jednak krótką stronę 8: zawiera samą sekcję 20.9, około 637 znaków tekstu, bez błędu obcięcia. To uwaga redakcyjna dotycząca kompozycji i motywacja do sprawdzenia rozbudowy matematycznej, nie automatyczny błąd kompilacji.

## Dalsze uzupełnienie matematyczne

Dodano ścisły wniosek „Charakteryzacja nośnika przez funkcje testowe”, commit 3ef178750af9eec03e993c20d4b43eb161a959be.

Dla lokalnie zwartej metrycznej przestrzeni X i miary Radona μ:
x∈supp μ wtedy i tylko wtedy, gdy dla każdej f∈C_c(X), f≥0 i f(x)>0, zachodzi ∫f dμ>0.
Dowód: dla x∈supp μ ciągłość dodatniej w x funkcji f daje otwarte V zawierające x, na którym f≥δ>0, a więc całka ≥δμ(V)>0. Odwrotnie, jeśli x nie należy do nośnika, istnieje U otwarty z μ(U)=0, a udowodniony lemat o funkcji odcinającej dla K={x} daje f∈C_c(X), f(x)=1 i supp f⊂U, zatem ∫f dμ=0. Argument wykorzystuje tylko wcześniejsze wyniki, z jawnym skończonym całkowaniem funkcji o zwartym nośniku.

Bieżący blob rozdziału po uzupełnieniu: 8545b0586adb31dd63a8dba53eb8bc2c51489b01.
Do testu źródłowego dodano weryfikację nowej etykiety cor:support-test-20, commit 8b4040863ab0c84e195d21278b0e43b5d59084c1.
Bieżący blob testu: 353e63c0ad7dde0bd9486c067e5a592d9ceccae0.

Dodatkowo w lokalnym Pythonie sprawdzono model atomów wymiernych wykorzystywany w regresji: 801 punktów, wszystkie wagi dodatnie, suma wag 0.9992415, dodatnie masy czterech testowanych otwartych przedziałów. Sprawdzono również obliczenia funkcji odcinającej przy ±1 i ±1.5, bez naruszeń.

## Werdykt

Przed uzupełnieniem nośnika rzeczywisty CI i PDF zostały potwierdzone dla commitu 63afe4f0.
**Najnowszy tekst i test po uzupełnieniu nośnika mają inne SHA.** W chwili zapisu niniejszego raportu brak jeszcze opublikowanego wyniku CI dla commitu 8b4040863ab0c84e195d21278b0e43b5d59084c1. Brak statusów nie oznacza ani sukcesu, ani porażki. Trzeba ponowić pełne 8+4 testów i obie kompilacje PDF, przejrzeć przede wszystkim rozkład stron końcowych, nie godząc się na kolizje czy ucięty tekst.

**Rozdział 20: W STABILIZACJI, NIEZAMKNIĘTY.** Rozdział 21 jest następną jednostką dopiero po pełnej bramce rozdziału 20.
