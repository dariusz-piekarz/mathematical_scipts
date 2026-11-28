# Audyt LXX (70) — rozdział 19: niezależna kontrola i zamknięcie

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts.
Istniejąca gałąź: biblioteka-matematyczna-iteracja-6.
Plik źródłowy: chapters/pl/measure_theory/19-zastosowania-twierdzenia-radona-nikodyma.tex.
Zweryfikowany SHA bloba: 7571e99edac729831e83e8061377757874cfb7bc.
Testowany commit: 7fa829c38b3e3b8f005d16f0990801cefd827b80.

## 1. Niezależny trzeci przegląd merytoryczny

Ponownie skontrolowano:
- zmianę miary, jej zasady całkowalności i gęstości miar obrazowych jako warunkową wartość oczekiwaną;
- dwa stosowane znaczenia wariacji całkowitej (odległość na rozkładach i normę miary ze znakiem) oraz przetwarzanie danych;
- lemat Neymana–Pearsona również przy c=0 i α=0, łącznie z istnieniem testu dokładnego poziomu oraz z przykładami wymagającymi randomizacji;
- skończony wzór Bayesa bez założenia gęstości względem miary Lebesgue'a;
- wyciąganie G-mierzalnego czynnika, warunkową nierówność Jensena i kontrakcję w Lp;
- nieujemność entropii względnej i przetwarzanie danych, z rozróżnieniem przypadku entropii nieskończonej;
- nowy przykład niejednoznaczności jądra warunkowego w pojedynczym punkcie obserwacji o zerowej mierze P_Y.

W przykładzie jądra na przestrzeni (0,1), Y=Θ=id oraz K(y,A)=χ_A(y), zmiana K(y0,·)=δ_y0 na dowolną ρ≠δ_y0 zachowuje mierzalność i całkową tożsamość definiującą rozkład warunkowy, ponieważ {y0} jest borelowski i P_Y({y0})=0. Twierdzenie o jednoznaczności P_Y-prawie wszędzie nie twierdzi więc jednoznaczności punktowej. Nie stwierdzono luki wymagającej dalszej zmiany twierdzeń.

## 2. Potwierdzenie wykonania GitHub Actions po ostatniej poprawce

Rzeczywisty przebieg: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45273447471
Commit: 7fa829c38b3e3b8f005d16f0990801cefd827b80.
Dwa klasyczne statusy przypięte do commitu:
- measure-theory/ch19-regressions: success;
- measure-theory/ch19-pdf: success.
Oba wskazują ten sam run.

Odczytano logi zadań:
- regresje, job 138041866297: Ran 8 tests ... OK oraz Ran 4 tests ... OK, czyli 12/12 zaliczonych;
- PDF, job 138041866882: pełna książka 259 stron i 1 897 356 bajtów, samodzielny rozdział 19 — 7 stron i 277 097 bajtów, 4 zewnętrzne etykiety zaimportowane, 19 lokalnych zachowanych, ostatnie odsyłacze rozwiązane;
- publikacja statusów, job 138042579633: zapisano oba wyniki success.

W jednym odczycie metadanych pierwszy job miał niespójne pola status=in_progress i conclusion=success, ale jego pełny log zawiera wszystkie wyniki OK, a końcowy raportujący job otrzymał outcome=success. Uznanie sukcesu opiera się zatem na statusach commitu i pełnych logach, a nie na pojedynczym niespójnym polu.

## 3. Rzeczywisty artefakt, strony i skład

Pobrano ZIP artefaktu 14865913868 (measure-theory-ch19-pdf-and-logs), zawierający oba PDF-y oraz końcowe logi. Z jego oryginalnego PDF rozdziału wyrenderowano wszystkie siedem stron i obejrzano kontaktowy podgląd całości. Osobno zweryfikowano końcową sekcję i tekst ostatniej strony.

Po korekcie z audytu LXIX strona 7 zawiera kompletną sekcję „19.8 Ograniczenia i dalsze kierunki”, w tym uzasadniony przykład jądra warunkowego, a nie osierocone dwa wiersze. Strona jest częściowo niezapełniona, ale tekst nie jest przycięty, a wzory i nagłówki są czytelne. Nie ma potrzeby sztucznego ściśnięcia składu kosztem czytelności.

Programowa inspekcja dwóch finalnych logów:
- pełna książka: 0 Overfull hbox, 0 Underfull hbox, 0 niezdefiniowanych referencji, 0 niepoprawnych cytowań, 0 multiply defined i 56 nieblokujących ostrzeżeń hyperref o zakładkach;
- rozdział: 0 Overfull hbox, 0 Underfull hbox i 0 nierozwiązanych referencji, 0 multiply defined.
Przejściowe ostrzeżenia podczas wielokrotnego uruchamiania latexmk nie są utożsamiane z logiem końcowym.

## 4. Werdykt

**ROZDZIAŁ 19 — STABILNY / ZAMKNIĘTY** dla konkretnego bloba 7571e99edac729831e83e8061377757874cfb7bc; audyty LXVIII–LXX, 8/8 testów źródłowo-matematycznych, 4/4 testy książki, prawdziwe kompilacje i oględziny PDF.

Zamknięcie to wynik szczegółowego procesu audytu, nie automatyczna formalizacja Lean. Rozdziały 15–19 zostały zamknięte osobno. Następna jednostka: rozdział 20 — miary borelowskie, regularność i miary Radona. Nie przechodzić do rozdziału 21 bez ustabilizowania rozdziału 20.
