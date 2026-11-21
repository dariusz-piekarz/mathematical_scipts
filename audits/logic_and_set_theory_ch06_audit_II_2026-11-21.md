# Audyt II — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/06-relacje-porzadku-od-porownywania-do-kresow.tex`, gałąź `biblioteka-matematyczna-iteracja-6`, blob Git przed audytem `abb48c05181f9eff965fd29de288e34d0e274e0d` (identyczny bajtowo z lokalnym źródłem audytu I).  
**Zakres:** niezależna ponowna kontrola *istniejącego* materiału: sformułowań, wszystkich kroków dowodów, przykładów, przypadków pustych zbiorów, etykiet, rysunków, kompilacji, testów. **Nie dodawano twierdzeń, definicji, lematów, wniosków, przykładów ani sekcji.**

## Poprawki do istniejących zapisów

Weryfikacja nie ujawniła nieprawdziwych tez ani błędów rachunkowych w dowodach. Usunięto cztery lokalne niedopowiedzenia dotyczące samodzielności założeń i oznaczeń:

1. **Definicja relacji pokrywania:** przed `a\lessdot b` jawnie określono `a\prec b` jako `a\preceq b` i `a\neq b`. Zbiór `P` i jego porządek pozostają takie same.
2. **Definicja minimum, maksimum i elementów minimalnych/maksymalnych** (`def:order-extrema`): wprowadzono dokładne znaczenie `\prec`, które jest następnie użyte w punktach (iii)–(iv).
3. **Twierdzenie o porządku współrzędnym** (`thm:product-poset`): samo sformułowanie podaje warunek `\big((p,q)\preceq_\times(p',q')\big)\iff(p\preceq_P p'\land q\preceq_Q q')`, zamiast wymagać szukania definicji w poprzednim akapicie. Teza i dowód pozostały niezmienione.
4. **Twierdzenie o porządku leksykograficznym** (`thm:lex-order`): jawnie określono ostry porządek pierwszego czynnika i warunek porównania par. Teza i dowód pozostały niezmienione.

Zmieniono wyłącznie powyższe fragmenty. Liczba i kolejność wszystkich środowisk oraz etykiet są identyczne jak w wersji po audycie I.

## Audyt matematyczny

Ponownie przeanalizowano **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów i 7 uwag**. Skontrolowano przechodzenie między porządkami ostrymi i nieostrymi, diagramy Hassego, odróżnienie elementów minimalnych od najmniejszych, kryteria kresów, prawa krat, zupełność, iloczyny współrzędne i leksykograficzne, gęstość, dobre porządki, indukcję, wybór najmniejszych elementów oraz porządek na ilorazie preporządku. Osobno sprawdzono przypadki pustego zbioru i pustego czynnika iloczynu oraz twierdzenia o minimalności w skończonych i nieskończonych porządkach.

- **30 665** ponowionych testów niezależnych z audytu I (`independent_check.py`): enumeracja wszystkich 243 oznakowanych porządków częściowych i 390 preporządków na zbiorach rozmiaru 0–4, własności krat, kresów i ilorazów, diagramów Hassego oraz rodzin podzbiorów.
- **215 552** dodatkowe testy (`extra_check.py`): wszystkie pary oznakowanych porządków częściowych na 0–3 elementach jako czynniki porządku współrzędnego; wszystkie podzbiory produktów dla kryterium jedynego elementu minimalnego; rekonstrukcja z pokryć; różne skończone porządki liniowe w konstrukcji leksykograficznej, w tym puste czynniki; istnienie najmniejszych elementów podzbiorów oraz niespójność gęstości z dobrym porządkiem przy co najmniej dwóch elementach.
- **Łącznie 246 217 sprawdzeń — wszystkie zaliczone.** Testy na strukturach skończonych są pomocą diagnostyczną, nie zastępują dowodów ogólnych, które skontrolowano oddzielnie.

Nie wykryto nowych błędów w tezach, dowodach, przykładach ani przypadkach brzegowych wymagających zmiany matematycznej treści.

## Struktura, LaTeX, odsyłacze i ilustracje

- **42/42 oryginalnych etykiet**, bez przemianowania i bez zmiany ich kolejności. Liczby środowisk: **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów, 7 uwag**.
- Pełny skrypt, 44 rozdziały: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0, 376 stron**, **1075 różnych etykiet, 869 odsyłaczy, 0 powielonych etykiet, 0 brakujących celów, 0 ostrzeżeń `Overfull \hbox`**.
- Książka repozytoryjna z rozdziałami 01–06: kompilacja `latexmk` — **kod 0, 62 strony**, brak `Overfull \hbox`. Oczekiwane odsyłacze do niezaimportowanych jeszcze rozdziałów 07, 09, 10 i 25 (`ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`) nie rozwiązują się jedynie w tej częściowej wersji; wszystkie istnieją w pełnym skrypcie.
- Ponownie wyrenderowano i obejrzano **12 stron** rozdziału 06 (strony 61–72 pełnego składu); diagram Hassego, przykład nieskończonego porządku i krata `M_3` pozostają czytelne. Brak zauważonych nakładek i obciętych elementów.
- Wersja przetestowana: SHA-256 `464fe0c62035d18f4292611fbcfc39909b35e739f18de0413067e777ccbfb17d`; blob Git po poprawkach powinien wynosić `358d3243c1b345d731613127d1aff44a1977fdcf`. Kontrola bajtowa GitHuba wykonywana osobno po publikacji.

## Status

**Audyt II wykonany.** Doprecyzowano cztery sformułowania bez zmiany zawartości matematycznej. Ponieważ wprowadzono poprawki, **rozdział 06 pozostaje otwarty do audytu III**. Po wypchnięciu pliku i raportu sprawdzamy ponownie GitHub Actions (indeksowanie, CLI, testy regresyjne i Chromium).
