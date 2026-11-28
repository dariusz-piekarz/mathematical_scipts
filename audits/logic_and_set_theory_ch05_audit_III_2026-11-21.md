# Audyt III — rozdział 05 „Relacje równoważności i zbiory ilorazowe”

**Data:** 21 listopada 2026 r.  
**Źródło:** kanoniczny plik `chapters/pl/logic_and_set_theory/05-relacje-rownowaznosci-i-zbiory-ilorazowe.tex` z gałęzi `biblioteka-matematyczna-iteracja-6`; stan po audycie II, SHA bloba Git `6a4ed20ecc2484f1102f2835c6c1a8c93fb4d6e8`.  
**Zakres:** niezależny przegląd istniejących definicji, tez, dowodów, przykładów, uwag, rysunku i odsyłaczy. **Nie dodawano żadnych twierdzeń, lematów, przykładów ani sekcji.**

## Znalezione usterki i ich usunięcie

1. **Niezdefiniowany symbol relacji w kontrprzykładzie do zachowywania przecięć przez nasycenie** (`ex:eq-sat-intersection-xliii`). W przykładzie określono kongruencję modulo `2` słownie, ale użyto następnie `\operatorname{Sat}_E` bez uprzedniego nadania tej relacji nazwy `E`. Zmieniono pierwsze zdanie na „Niech `X=\Z`, `E` będzie kongruencją modulo `2`...”. Kontrprzykład i jego uzasadnienie pozostają bez zmian.
2. **Mylący nagłówek przykładu o zgodności działań z równoważnością.** Dawny nagłówek „Działanie, które nie przechodzi na iloraz” obejmował w rzeczywistości dwa działania: `a\star b=a^2+b` (zgodne) i `a\diamond b=\lfloor a/2\rfloor+b` (niezgodne). Tytuł ujednolicono z zawartością: „Działania zgodne i niezgodne z relacją”. Oba obliczenia i ich ocena pozostały bez zmian.
3. **Brak jawnych dziedzin funkcji w przykładzie faktoryzacji** (`ex:lxv-quotient-factorization`). Zapisano `f:\Z\to\{0,1,2\}` i `h:\Z\to\Z`; wcześniej podano jedynie `f(a)` i `h(a)=a`. Dzięki temu przykład jest samodzielny i precyzyjnie wskazuje przeciwdziedziny. Teza przykładu pozostaje identyczna.

Zmiany dotyczą wyłącznie trzech istniejących przykładów. Nie zmodyfikowano formuł, tez ani dowodów żadnego twierdzenia lub wniosku.

## Niezależny audyt matematyczny

Ponownie przeanalizowano **11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów i 5 uwag**. Kontrola obejmowała jednoznaczność klas i ich rozłączność, odpowiedniość podziałów i równoważności (również dla `X=\varnothing`), drobniejsze i grubsze relacje, najmniejszą równoważność generowaną przez dowolną relację, przecięcia równoważności, nasycenie i jego minimalność, działania na ilorazach, jednoznaczność faktoryzacji i arytmetykę ułamków. Zweryfikowano krok po kroku także dowód zgodności działań na klasach ułamków.

Nie znaleziono błędu w żadnej z 12 tez ani ich dowodów. Przeanalizowano przypadki pustych zbiorów, pustej rodziny klas, pustej dziedziny i przeciwdziedziny oraz zerowego mianownika (wykluczonego w konstrukcji).

- **23 542** testy enumeracyjne poprzedniego audytu (`independent_check.py`) ponownie przeszły.
- **280** osobnych testów odpowiedniości podziałów z równoważnościami, zawierania klas i przypadku pustego zbioru (`extra_check.py`) przeszło.
- **2713** kolejnych niezależnych kontroli (`new_independent_check.py`) zweryfikowało istnienie i jednoznaczność faktoryzacji przez iloraz (w tym puste dziedziny i przeciwdziedziny), dopełnienia i przecięcia podzbiorów nasyconych oraz alternatywne reprezentacje ułamków.
- **Łącznie: 26 535 testów, wszystkie pozytywne.** Testy na małych zbiorach wspierają kontrolę, ale nie zastępują dowodów dla zbiorów dowolnych.

## Integralność i kompilacja

- Bez zmian w liczbie i kolejności środowisk: **11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów, 5 uwag**. Wszystkie **29 oryginalnych etykiet** zachowano, bez zmiany nazw.
- Pełny skrypt (44 rozdziały), polecenie `latexmk -g -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **kod 0, 376 stron**, **1075 niepowtarzających się etykiet, 869 odsyłaczy, 0 brakujących celów, 0 zduplikowanych etykiet, 0 ostrzeżeń `Overfull \hbox`**. W skrypcie pozostają **3** nieblokujące ostrzeżenia `Underfull \hbox`.
- Częściowa książka repozytoryjna obejmująca rozdziały 01–05: **kod kompilacji 0, 50 stron**, bez błędów. Odsyłacze `ch:orders`, `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol` i `ch:zf-axioms` oczekują na import rozdziałów 06, 07, 09, 10 i 25; wszystkie mają poprawne cele w pełnym skrypcie.
- Wycięto z pełnego składu **9 stron** rozdziału 05, ponownie wyrenderowano i obejrzano wszystkie. Rysunek dwóch rodzin klas równoważności oraz strony z poprawkami są czytelne; nie zauważono obcięć ani nałożeń tekstu. Rysunek jest wbudowany jako TikZ, bez zależności od plików zewnętrznych.

## Status

**Audyt III zaliczony, ale rozdział 05 pozostaje otwarty**, ponieważ ta iteracja ujawniła faktyczną lukę w nazwaniu relacji i dwa niedopowiedzenia redakcyjne. Następna iteracja to audyt IV całego rozdziału; jeśli nie przyniesie kolejnych usterek, można go zamknąć. Po opublikowaniu zmian należy osobno zweryfikować GitHub Actions.
