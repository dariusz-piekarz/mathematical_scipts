# Topologia ogólna — rozdział 20, audyt 03 (kontrola korekcyjna)

**Data:** 2026-11-22. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex`.
**Blob przed poprawką:** `73de106461510c1be14419882d3b617602cca177`.
**Blob po poprawce:** `c7644dae32a49ae9ac1403f4932018d440586e9b`.
**Wynik:** **DWIE USTERKI MERYTORYCZNE W PODSUMOWANIU — POPRAWIONE**.
Jest to audyt **nieczysty**: liczba kolejnych czystych audytów po ostatniej edycji źródła wynosi **0/2**.
Główne twierdzenia i ich dowody nie wymagały edycji.

## Niezależna kontrola matematyczna

1. **Lemat o surjekcji z przestrzeni Baire’a:** dla dowolnej niepustej przestrzeni polskiej X wybór zupełnej metryki d, gęstego przeliczalnego D i domkniętych pokryć F_s z średnicami malejącymi do zera daje pojedynczą granicę na każdej gałęzi. Istnienie gałęzi nad każdym x wynika z pokrycia F_s przez następców; ciągłość z kontroli prefiksów. Przypadku pustego nie obejmuje się tym lematem, co jest konieczne.
2. **Rzuty zbiorów domkniętych:** wykazano obie implikacje: graf ciągłego f jest domknięty, a domknięty podzbiór iloczynu polskich jest polski i jest ciągłym obrazem przestrzeni Baire’a, jeśli nie jest pusty. Szczególny przypadek F=∅ wyodrębniono.
3. **Przeliczalne sumy i przecięcia:** konstrukcje domkniętych zbiorów świadków z dyskretnym znacznikiem i z przeliczalnego produktu świadków są poprawne; podane homeomorfizmy do N^N istnieją. Użycie wyboru przeliczalnego jest zgodne z jawnym założeniem ZFC. Obrazy i przeciwobrazy przy ciągłych mapowaniach zachowują analityczność.
4. **Borelowskość:** klasa zbiorów jednocześnie analitycznych i koanalitycznych jest sigma-algebrą; otwarte należą do niej, ponieważ są F-sigma w metryzowalnej X. Wniosek Borel ⊂ analityczne∩koanalityczne nie zawiera nieuprawnionej implikacji odwrotnej.
5. **Zgodność definicji ze skryptem logiki:** zakodowanie α∈N^N w ciąg binarny z blokami zer zakończonymi jedynką daje homeomorfizm na G-delta podprzestrzeń Cantora. Osadzenie Cantora w R przez sumę trójkową jest homeomorficzne na domknięty obraz, a przeniesiony podzbiór E jest borelowski. Zatem rzut domkniętego F⊂R^n×N^N można przedstawić jako rzut borelowskiego B⊂R^{n+1}. W drugą stronę dowolny borelowski B⊂R^{n+1} jest analityczny jako podzbiór przestrzeni polskiej, a jego rzut pozostaje analityczny. W dowodzie nie zidentyfikowano dodatkowych luk.
6. **Operacja Suslina:** dla domkniętych F_s zbiór par (x,α) z x∈F_{α|n} dla każdego n jest domknięty: cylindry prefiksowe długości n tworzą rozkład na otwarto-domknięte składniki. W drugą stronę domknięte otoczki rzutów H∩(X×[s]) oraz wybór przybliżeń (x_n,u_n) z d(x_n,x)<1/n i u_n∈[α|n] dają przez domkniętość H dokładną równość rzutów.
7. **Uniwersalna rodzina analityczna:** kodowanie przez współrzędne c drzewa par skończonych prefiksów definiuje domknięty H⊂(N^N)^3. Dowolny domknięty F⊂(N^N)^2 odpowiada takiemu drzewu: nieskończona zgodność prefiksów i domkniętość dają przynależność do F, także dla F pustego. W wyniku U=π(H) ma wszystkie analityczne przekroje.
8. **Przekątniowanie:** D={x:(x,x)∉U} nie jest analityczny, bo D=U_c dawałoby c∈D ⇔ c∉D. Zbiór E={x:(x,x)∈U} jest analityczny jako przeciwobraz przez ciągłą przekątną i nieborelowski, ponieważ D jest jego dopełnieniem i nie jest analityczny. Konstrukcja dowodzi ścisłości Borel ⊊ analityczne **w przestrzeni Baire’a**.

## Dwie wykryte nieścisłości i ich korekty

**I. Zbiór pusty.** Podsumowanie mówiło bez zastrzeżenia, że analityczne to dokładnie ciągłe obrazy niepustej przestrzeni Baire’a. To nie obejmuje ∅, choć w Definicji 20.2.1 zbiór pusty jest jawnie analityczny, a obraz każdej niepustej dziedziny jest niepusty. Poprawiono podsumowanie na: zbiór analityczny jest **pusty albo** jest ciągłym obrazem przestrzeni Baire’a. Równoważne opisy przez rzuty i operację Suslina są nadal prawidłowe także dla ∅.

**II. Nieuprawniona ścisłość dla wszystkich przestrzeni polskich.** Podsumowanie sugerowało, że analityczne są zawsze klasą ściśle większą od borelowskich. Jest to fałsz dla przeliczalnych przestrzeni dyskretnych: każda ich podprzestrzeń jest otwarta i borelowska. Udowodnione twierdzenie o zbiorze nieborelowskim analitycznym dotyczy **przestrzeni Baire’a**. Ograniczono do niej stwierdzenie ścisłości i dodano kontrprzykład przeliczalnej przestrzeni dyskretnej.

Obie poprawki wprowadzono w źródle: [commit e9ce798](https://github.com/dariusz-piekarz/mathematical_scipts/commit/e9ce798ade43ff453229f916019686a424917316). Dodano regresyjną kontrolę obu sformułowań w testach: [commit 44f4e22](https://github.com/dariusz-piekarz/mathematical_scipts/commit/44f4e2210d9fb7b8a0a909f3f594e3c26ad12b5b).

## LaTeX, odsyłacze i rzeczywisty przegląd PDF

- Nowy blob źródła ma **852 wiersze**, **23 unikatowe etykiety i 23 użycia ref/eqref/pageref**, wszystkie cele zidentyfikowano w rozdziałach 19 i 20; brak niedomkniętych środowisk i powtórzonych etykiet. Delimitatory matematyczne: **293 par \\(\\)** oraz **26 par \\[\\]**.
- Pobrano **rzeczywisty artefakt ZIP** `general-topology-ch01-ch20` z [udanej walidacji 45022608046](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022608046). Rozpakowano samodzielny `general_topology_ch20.pdf` oraz jego log.
- W pliku PDF **6 stron A4**. Wszystkie sześć wyrenderowano i wizualnie przejrzano; skontrolowano także pełną stronę z dowodem równoważności definicji i stronę końcową. Nie zauważono nachodzących tekstów, uciętych wzorów, pustych stron ani uszkodzonych znaków. Log tego PDF nie zawiera `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning` i błędów poleceń. Przeszły kompilacje całej książki i osobnego rozdziału w workflow.
- **Ważne rozgraniczenie:** pobrany PDF i zielone CI dotyczą **poprzedniego bloba** `73de106461510c1be14419882d3b617602cca177`, zgodnego z raportem 02. Ponieważ niniejszy audyt zmienił podsumowanie rozdziału, wizualna kontrola i zielony CI **nie walidują jeszcze nowego bloba** `c7644dae32a49ae9ac1403f4932018d440586e9b`. Uruchomienia po zmianach: [45023247196](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023247196) i [45023273463](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023273463) były w toku w trakcie sporządzania raportu. Nie deklarujemy ich sukcesu z góry.

## Status i następna iteracja

**Rozdział 20 pozostaje otwarty (0/2).** Audyt 03 wykrył dwie merytoryczne nieścisłości, które poprawiono. W kolejnym niezależnym **audycie 04** należy skontrolować ten sam poprawiony blob, wyniki CI i wygląd PDF po zmianach. Po kolejnych czystych audytach tego samego bloba i pomyślnym CI można dopiero nadać status STABILNY. Zakres rozdziału nadal uzupełnia skrypt logiki, nie powielając jego teorii gier ani determinacji.
