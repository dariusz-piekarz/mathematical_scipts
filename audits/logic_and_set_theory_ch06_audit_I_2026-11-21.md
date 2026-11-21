# Audyt I — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Źródło:** plik Biblioteki matematycznej `06-orders-lattices-and-well-orders.tex` (wersja 5), przed importem rozdziału do gałęzi `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** audyt istniejących definicji, twierdzeń, wniosku, dowodów, przykładów, uwag, terminologii, rysunków i odsyłaczy; bez dodawania materiału.

## Wykryte luki i poprawki

1. **Dowód twierdzenia o krańcowych elementach kraty zupełnej (`thm:complete-lattice-bottom-top-xliii`).** Twierdzenie głosiło też, że nie każda krata jest zupełna, natomiast jego dowód wykazywał tylko istnienie `0_L` i `1_L`. Dodano bezpośrednie uzasadnienie ostatniej części: `(\mathbb N,\le)` jest kratą, ponieważ każda para ma minimum i maksimum, ale `\mathbb N` nie ma ograniczenia górnego w `\mathbb N`. Wykorzystano kontrprzykład, który był już w następnym przykładzie. Nie zmieniono tezy.
2. **Samodzielność twierdzeń o produktach porządków.** W `thm:product-poset` zwrot „przy powyższych założeniach” zastąpiono deklaracjami obu uporządkowanych zbiorów; w `thm:lex-order` jawnie wprowadzono porządki czynników. W obu przypadkach określona wcześniej relacja produktu pozostała ta sama.
3. **Niezadeklarowany zbiór w przykładach.** Jawnie wprowadzono `X` w przykładach zawierania podzbiorów i właściwego zawierania oraz w przykładzie identyfikacji sumy i przecięcia z kresem górnym i dolnym.
4. **Precyzja terminologii.** Zastąpiono tytuł „Jedyne minimum lokalne…” poprawnym „Jedyny element minimalny…”, ponieważ lokalne minimum nie było definiowane w rozdziale. Tytuł wniosku o wybieraniu elementów z podzbiorów ustalonego dobrze uporządkowanego zbioru zmieniono tak, aby nie sugerował wybierania reprezentantów klas równoważności.

Nie zmieniono żadnej tezy, pierwotnych etykiet, przykładów matematycznych ani rysunków. Nie dodano żadnego twierdzenia, lematu, wniosku, definicji ani przykładu.

## Niezależny audyt matematyczny

Przeanalizowano wszystkie **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów, 7 uwag i 42 etykiety**. Kontrola obejmuje relacje ostre i nieostre, łańcuchy i antyłańcuchy, poprawność diagramów Hassego, minimum wobec minimalności, istnienie elementów ekstremalnych dla skończonych posetów, kryteria kresów, kraty (w tym `M_3` i `\mathcal P(X)`), porządki współrzędne i leksykograficzne, gęstość, dobre uporządkowania, indukcję po dobrym porządku, wybór najmniejszych elementów oraz iloraz preporządku.

**30 665 sprawdzeń semantycznych**, wszystkie zaliczone, z pliku `independent_check.py`. Wyczerpująco przetestowano wszystkie 243 oznakowane porządki częściowe na zbiorach o licznościach 0–4 (odpowiednio `1,1,3,19,219`) i 390 oznakowanych preporządków (`1,1,4,29,355`), w tym relacje ostre, rekonstrukcję z krawędzi pokrywania, minima i maksima wszystkich podzbiorów, kresy, własności krat, ilorazy preporządków, wybrane produkty oraz wszystkie rodziny podzbiorów uniwersum o co najwyżej trzech elementach. Sprawdzono nie-rozdzielność `M_3` i puste zbiory. Skończone testy nie zastępują dowodów dla dowolnych i nieskończonych zbiorów; te sprawdzono osobno.

W toku ręcznego przeglądu nie wykryto błędu w tezie żadnego z 15 twierdzeń ani wniosku. Uzupełniono pominięty fragment dowodu o niezupełności krat. Przypadki zbioru pustego w dobrym porządku, porządku iloczynowym i kracie potęgowej pozostają poprawne. Uwaga o braku ciągów malejących poprawnie odróżnia ZF od ZFC.

## Kompilacja i rysunki

- Pełny skrypt: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0, 44 rozdziały, 376 stron**; **1075 unikatowych etykiet, 0 brakujących odsyłaczy, 0 duplikatów, 0 `Overfull \hbox`**.
- Import rozdziałów 01–06 do struktury repozytorium: `latexmk` — **kod 0, 62 strony**, bez `Overfull \hbox`. W częściowym imporcie pozostają cztery oczekiwane odsyłacze do niezaimportowanych rozdziałów 07, 09, 10 i 25: `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`; wszystkie są rozwiązane w pełnym skrypcie.
- Zachowano **42/42 oryginalnych etykiet** oraz wszystkie istniejące środowiska LaTeX.
- Wyrenderowano i obejrzano **12 stron** rozdziału 06 (strony 61–72 pełnego PDF), w tym diagram Hassego, nieskończony przykład z jedynym elementem minimalnym i diagram kraty `M_3`. Brak zauważonych nakładań i obcięć.

## Status

**Audyt I wykonany.** Zlikwidowano lukę w kompletnym dowodzie jednego istniejącego twierdzenia oraz lokalne nieścisłości deklaracji i terminologii. Rozdział 06 **pozostaje otwarty do audytu II**. Po publikacji osobno weryfikujemy GitHub Actions (parser, indeksowanie, CLI i Chromium).
