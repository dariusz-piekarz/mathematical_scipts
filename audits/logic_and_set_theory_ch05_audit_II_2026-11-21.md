# Audyt II — rozdział 05 „Relacje równoważności i zbiory ilorazowe”

**Data:** 21 listopada 2026 r.  
**Punkt wyjścia:** plik `chapters/pl/logic_and_set_theory/05-relacje-rownowaznosci-i-zbiory-ilorazowe.tex` po audycie I, blob `1e76f61a541a457c70dc1700e8bc0be2aa5fa597`; źródło odpowiada wersji z Biblioteki matematycznej.  
**Zakres:** ponowny niezależny audyt całego istniejącego rozdziału; bez dokładania twierdzeń, lematów, wniosków, definicji, przykładów i sekcji.

## Wykryte i poprawione usterki

1. **Definicja „Relacja drobniejsza i grubsza”.** Dotychczas zdefiniowano jedynie, kiedy relacja `E` jest drobniejsza od `F` (`E\subseteq F`), choć nagłówek obiecywał również relację *grubszą*. Dodano dokładnie odwrotne określenie: w tej samej sytuacji `F` jest grubsza od `E`. Nie zmieniono relacji porządkującej ani żadnego twierdzenia.
2. **Dowód odpowiedniości podziałów i relacji równoważności, `thm:eq-partition`.** Po pokazaniu, że dla każdego bloku `D` i dowolnego `x\in D` zachodzi `[x]=D`, tekst stwierdzał bez jawnego objaśnienia, że także każda klasa jest blokiem. Uzupełniono istotny krok: dla dowolnego `x\in X` pokrycie `X` przez podział dostarcza bloku `D` zawierającego `x`, a poprzedni argument daje `[x]=D`. Wspomniano też przypadek `X=\varnothing`, gdy obie rodziny są puste. Teza i wcześniejsze kroki dowodu pozostały niezmienione.

Innych usterek wymagających poprawy nie stwierdzono. Nie rozszerzano materiału, nie dodano środowisk LaTeX ani nie przemianowano etykiet.

## Niezależna kontrola matematyczna

Ponownie sprawdzono wszystkie **11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów i 5 uwag**, w tym: klasy równoważności, wzajemną odpowiedniość z podziałami, drobniejsze i grubsze relacje, przecięcia równoważności, relację generowaną, minimalne wspólne rozszerzenia, nasycenie, dobrze określone działania, własność uniwersalną odwzorowania ilorazowego oraz konstrukcję liczb wymiernych z par liczb całkowitych.

- Powtórzono **23 542** niezależne testy enumeracyjne wcześniejszego audytu (`independent_check.py`): rozmiary 0–4, podziały, nasycenia, wygenerowane równoważności, zgodność operacji z ilorazem i arytmetyka ułamków także dla ujemnych mianowników. Wszystkie zaliczone.
- Wykonano dodatkowo **280** niezależnych sprawdzeń wzajemnej odpowiedniości podziałów z równoważnościami oraz monotoniczności klas względem zawierania relacji (dla 0–4 elementów); wszystkie zaliczone. Łącznie **23 822** kontrole.
- Przypadki brzegowe `X=\varnothing`, `Y=\varnothing` i pustych rodzin omówiono zgodnie z przyjętym uniwersum; twierdzenie o faktoryzacji pozostaje poprawne także dla pustego ilorazu. Testy skończone są pomocnicze; poprawność dowodów oceniono osobno.

## Kompilacja, odsyłacze i wygląd

- Zachowano **29/29 oryginalnych etykiet** i liczbę środowisk: 11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów, 5 uwag. Brak nowych wyników.
- Pełna książka `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **kod 0, 44 rozdziały, 376 stron**; **1075 unikatowych etykiet, 869 odsyłaczy, 0 brakujących celów, 0 duplikatów, 0 ostrzeżeń `Overfull \\hbox`**. Pozostają trzy nieblokujące ostrzeżenia `Underfull \\hbox`.
- Książka repozytoryjna z rozdziałami 01–05: kompilacja `latexmk` — **kod 0, 50 stron**. Nadal istnieje pięć oczekiwanych nierozwiązanych odsyłaczy do przyszłych rozdziałów 06, 07, 09, 10 i 25: `ch:orders`, `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`. Wszystkie mają cele w pełnym skrypcie; nie zmieniano etykiet.
- Wyrenderowano i obejrzano **9 stron** rozdziału 05, w tym ilustrację klas równoważności i stronę z dwiema poprawkami. Nie zaobserwowano błędów składu, nachodzących napisów ani obciętych rysunków.

## Status

**Audyt II zakończony:** wykryte dwa niedopowiedzenia uzupełniono. Z tego powodu rozdział 05 pozostaje otwarty — następny krok to **audyt III tego samego rozdziału**, bez zwiększania zakresu materiału. Weryfikacja GitHub Actions po wypchnięciu poprawek jest odrębnym krokiem.
