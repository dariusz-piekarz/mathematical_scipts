# Audyt VI — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Źródło:** kanoniczny rozdział 06 po audycie V: `chapters/pl/logic_and_set_theory/06-relacje-porzadku-od-porownywania-do-kresow.tex`, Git blob `8c42c1c7e94dc267fed34b7d911254226fca9026`.  
**Zakres:** kolejny niezależny audyt wyłącznie istniejących twierdzeń, wniosku, dowodów, definicji, przykładów, uwag, rysunków i odsyłaczy. Nie rozszerzano materiału i nie dodano wyników matematycznych.

## Wykryte i poprawione niedokładności

1. **Tytuł przykładu o dwóch elementach minimalnych:** nagłówek mówił „na obrazku”, mimo że stojący obok diagram przedstawiał *inny* zbiór częściowo uporządkowany. Zmieniono wyłącznie nagłówek na „Dwa elementy minimalne i brak najmniejszego”.
2. **Twierdzenie o niezgodności dobrego porządku z gęstością** (`thm:well-order-not-dense`): definicja dobrego porządku w rozdziale używa porządku nieostrego, podczas gdy twierdzenie przyjmowało nieobjaśnione `(W,<)` jako „dobrze uporządkowane”. Odtąd założono jasno dobry porządek `(W,\preceq)` i zdefiniowano dla `a,b\in W` odpowiadający mu porządek ostry `<`. Dowód i matematyczna teza są niezmienione.
3. **Samodzielność twierdzenia o przejściu między porządkami ostrym i nieostrym** (`thm:order-strict-correspondence`): w punktach (i) oraz (ii) dopisano, że definiowane relacje są na `P` i podane wzory obowiązują dla `a,b\in P`.
4. **Przykład NWD/NWW jako kresów:** przed użyciem wolnych liter `a,b` wpisano założenie `a,b\in\N_{>0}`.
5. **Przykład gęstości `\Q` w `\R`:** wskazano explicite `a,b\in\R` i `a<b`, nie pomijając dziedziny kwantyfikatorów.
6. **Ten sam przykład — uzasadnienie wyboru liczby całkowitej:** dopisano niepustość i ograniczoność od dołu zbioru liczb całkowitych większych od `na`, a z minimalności wybranej liczby `k` wyprowadzono `k-1\le na`; dopiero stąd otrzymano `na<k\le na+1<nb`. Nie zmieniono konstrukcji liczby wymiernej `d=k/n`.
7. **Twierdzenie o ilorazie preporządku** (`thm:preorder-quotient`): wprowadzono `a,b\in P` bezpośrednio przed definicją relacji równoważności na `P`.

Łącznie **9 lokalnych korekt** w siedmiu grupach powyżej. Nie zmieniono tez, dowodów twierdzeń, przykładów jako obiektów matematycznych, etykiet ani numeracji rozdziału; korekta w przykładzie `\Q\subseteq\R` dotyczy wyłącznie jawnego uzasadnienia istniejącego kroku.

## Kontrola matematyczna i przypadki brzegowe

- Ponownie przeczytano **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów i 7 uwag**. Nie znaleziono błędnych tez ani fałszywych wnioskowań. Sprawdzono przejścia między porządkiem ostrym i nieostrym, różnicę między minimalnością a najmniejszością, zrekonstruowanie porządku z diagramu Hassego, kresy i kompletność krat, prawa działań kresowych, produkt i porządek leksykograficzny, definicje gęstości, dobre porządki i indukcję oraz iloraz preporządku.
- Sprawdzono przypadki pustego zbioru podstawowego i iloczynu z pustym czynnikiem, pustych rodzin w kracie zupełnej, jednoelementowych i dwuelementowych porządków, brak elementów bezpośrednio poprzedzających, wielokrotną minimalność w porządku skończonym, a także twierdzenia o wyborze minimum w ZF. Własności związane z aksjomatem wyboru interpretowano bez niejawnych założeń AC.
- `independent_check.py`: **30 665/30 665** sprawdzeń, wszystkie poprawne. `extra_check.py`: **215 552/215 552**, wszystkie poprawne. Testy obejmują wszystkie porządki częściowe i preporządki na zbiorach 0–4-elementowych oraz niezależne sprawdzenia porządków na małych iloczynach.
- Dodatkowy `new_targeted_check.py`: **13 353/13 353**, w tym **3 200** kontroli NWD/NWW w porządku podzielności i **10 153** kontroli wymiernej konstrukcji punktu pośredniego. Łącznie **259 570/259 570** zaliczonych przypadków. Enumeracja skończona nie zastępuje argumentacji dla dowolnych zbiorów.

## LaTeX, odsyłacze, PDF i grafika

- Zachowano **42/42 etykiety** w tym samym porządku i wszystkie środowiska: **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów, 7 uwag**.
- Kompilacja pełnego skryptu (44 rozdziały): `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod wyjścia 0, 376 stron**, **1075 niepowtarzających się etykiet, 869 odsyłaczy, zero brakujących celów i zero `Overfull \hbox`**.
- Częściowy import repozytoryjny 01–06: `latexmk` — **kod 0, 62 strony**, zero `Overfull \hbox`. Pozostają oczekiwane odsyłacze do rozdziałów 07, 09, 10 i 25, których nie włączono jeszcze do częściowego importu; wszystkie rozwiązują się w pełnym skrypcie.
- Wyrenderowano i obejrzano **12 stron** rozdziału 06 w pełnym PDF, w tym diagramy Hassego, nieskończonego porządku i kratę `M_3`; bez widocznego nakładania napisów, obcięć lub problemów z układem. Wyodrębniono 12-stronicowy PDF rozdziału.

## Status

**Audyt VI wykonany i lokalne walidacje zaliczone.** Ponieważ wykryto dodatkowe niedokładności formalne i redakcyjne, **rozdział 06 pozostaje otwarty do audytu VII**. Zgodnie z przyjętym standardem zostanie zamknięty dopiero po iteracji bez żadnych dalszych poprawek. Po publikacji sprawdzamy także CI na GitHubie.
