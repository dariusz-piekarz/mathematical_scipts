# Audyt II — rozdział 10 „Struktury, wartościowania i prawda”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/10-struktury-wartosciowania-i-prawda.tex`.  
**Zakres:** druga niezależna kontrola istniejącego rozdziału, bez nowych twierdzeń, lematów ani przykładów.

## Wynik audytu matematycznego

Sprawdzono ponownie **5 twierdzeń, 2 lematy, 1 stwierdzenie, 1 wniosek, 9 dowodów, 8 definicji, 16 przykładów i 3 uwagi**. Nie znaleziono fałszywego twierdzenia ani wadliwego dowodu. Skontrolowano także wszystkie założenia dotyczące niepustości uniwersum, zmiennych wolnych, dopuszczalności podstawienia, wartościowań i zmiennych relacyjnych.

### Korekta w semantyce Henkina

W audycie I wymagano, by każde wartościowanie zmiennej relacyjnej arności `n` należało do `S_n`, również dla wystąpień wolnych. Jednak przy **nieskończenie wielu arnościach** i pracy bez aksjomatu wyboru sam warunek `S_n ≠ ∅` dla każdego `n` nie gwarantuje istnienia funkcji wybierającej po jednym `D_n ∈ S_n`. Ponieważ rozdział używa **pełnych wartościowań wszystkich zmiennych**, wymaganie jednoczesnego wartościowania wymaga doprecyzowania.

W istniejącej definicji uzupełniono dane modelu o jedną wskazaną rodzinę `(D_n)`, indeksowaną rozważanymi arnościami i spełniającą `D_n ∈ S_n` przy nieskończonym indeksowaniu w ZF. Przypisanie zmiennym arności `n` wartości `D_n` gwarantuje, że istnieje co najmniej jedno pełne dopuszczalne wartościowanie. Przy skończonej liczbie arności dodatkowy warunek nie jest potrzebny, bo skończony wybór jest twierdzeniem ZF. Nie zmieniono zakresu kwantyfikatorów, twierdzeń ani przykładów.

## Niezależne testy matematyczne

W audycie II przebadano kompletny zestaw **512 modeli dwuelementowych** w jednej sygnaturze (16 interpretacji relacji binarnej, 4 interpretacje relacji jednoargumentowej, 4 funkcje jednoargumentowe i 2 interpretacje stałej), **4096 wartościowań**, **16 384 sprawdzenia praw kwantyfikatorów** oraz **7680** konfiguracji niepustych rodzin dopuszczalnych podzbiorów dla semantyki Henkina. Zarejestrowano **1792 przypadki** prawdziwości badanego zdania indukcji w semantyce Henkina przy jego fałszywości w semantyce pełnej. Ponadto skontrolowano **30 720** przypisań do wolnej zmiennej relacyjnej z właściwym zakresem dopuszczalnych wartości.

**Nie znaleziono kontrprzykładu.** Enumeracja skończona nie jest dowodem dla dowolnej mocy ani dowodem niezależności aksjomatów wyboru. Dotychczasowy plik `tools/tests/test_logic_and_set_theory_ch10.py` został rozszerzony o regresję obecności jawnego warunku `D_n ∈ S_n` w źródle.

## Odsyłacze i CI

W trakcie audytu wykryto niezależną, równoległą korektę z commitu `1f452b862`, która usunęła dwa odsyłacze do jeszcze niezdefiniowanych celów `ch:soundness-fol` i `thm:ls-second-order-categorical`. Samo usunięcie poprawiło globalną kontrolę aplikacji, lecz chwilowo pozostawiło niespójny inwentarz w CI skryptu (przebieg `44926765103` zakończył się błędem).

Następnie równoległy commit `8f21df291` **naprawił inwentarz**, wymagając dokładnie jednego brakującego celu `ch:zf-axioms` i dostosowując drukowaną liczbę odsyłaczy. Potwierdzono zielony przebieg CI skryptu `44926838764` oraz globalnej aplikacji `44926765108`. Nie przywracano nierozwiązanych odsyłaczy ani nie wyłączano kontroli poprawności etykiet.

Aktualny inwentarz rozdziałów 01–10 to **288 unikatowych etykiet i 112 odsyłaczy**, z jednym dokumentowanym przyszłym celem `ch:zf-axioms`. Zmiana w niniejszym audycie nie zmieniła żadnej etykiety ani odsyłacza. Nowe CI uruchamiane na commicie z raportem należy potwierdzić przed formalnym zamknięciem.

## Status

**Audyt II wykonano z jedną istotną korektą definicyjną.** Rozdział 10 nie jest jeszcze stabilny według przyjętej strategii, ponieważ ponownie zmieniono plik źródłowy. Przeprowadzić **audyt III** po zielonym CI, dopiero potem rozważyć zamknięcie rozdziału i przejście do 11.
