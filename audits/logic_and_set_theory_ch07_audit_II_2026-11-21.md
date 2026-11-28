# Audyt II — rozdział 07 „Funkcje: jednoznaczność przyporządkowania”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/07-funkcje-i-odwzorowania.tex`, niezmieniony blob Git `fefabc8315e285cf9f92455d34e127c74dd0613a` po audycie I.  
**Zakres:** powtórny, niezależny audyt już istniejącego materiału. Bez dodawania twierdzeń, lematów, przykładów ani rozszerzania zakresu rozdziału.

## Wynik

**Audyt II jest czysty: nie stwierdzono błędu matematycznego wymagającego korekty źródła.** Nie modyfikowano kanonicznego pliku rozdziału 07. Korekty formalne z audytu I są poprawne i nie wprowadzają zmian znaczenia twierdzeń.

Przeprowadzono ponowną kontrolę **11 twierdzeń, 11 dowodów, 5 definicji, 10 przykładów, 9 uwag i jednego diagramu TikZ**. Osobno sprawdzono:

1. Dwa formalizmy funkcji (ustalone `A,B` oraz wykres; trójka `(A,B,G_f)`), istnienie `B^A` z aksjomatów ZF bez wyboru i zależność surjektywności od przeciwdziedziny.
2. Konstrukcję jedynej funkcji `∅→B`, nieistnienie funkcji `A→∅` dla `A≠∅`, indukcję na liczbie argumentów oraz szczególną konwencję `0^0=1` jako liczby funkcji `∅→∅`.
3. Obie równoważności dotyczące włókien, w tym dla pustej przeciwdziedziny, rozłączność niepustych włókien i ich sumę równą dziedzinie; zgodność z definicją podziału w rozdziale 05.
4. Definicję funkcji stałej przy `A=B=∅`, bijekcję między `P(A)` a funkcjami charakterystycznymi `{0,1}^A` oraz odróżnienie wartości od zbioru wartości.
5. Odwracalność dokładnie bijekcji oraz jednoznaczność odwrotności, w szczególności poprawność jej konstrukcji z jedynego przeciwobrazu.
6. Warunek istnienia odwrotności lewostronnej: iniekcja i `(A≠∅ lub B=∅)`, w tym oba przypadki puste i użycie jednej ustalonej wartości poza obrazem.
7. Konstrukcję prawostronnej odwrotności surjekcji na skończoną przeciwdziedzinę bez aksjomatu wyboru.
8. Równoważność nad ZF aksjomatu wyboru z istnieniem przekroju każdej surjekcji; jawność rodziny indeksowanej, rozłączną sumę włókien, poprawność projekcji `p:D→I`, przypadek `I=∅` i brak ukrytego wielokrotnego wyboru przy wykazywaniu surjektywności projekcji.
9. Twierdzenie o wykresie jako relacji z jednoelementowymi włóknami i przykład pierwiastka z wyznaczoną dziedziną i przeciwdziedziną.

## Niezależna weryfikacja skończonych modeli

Przeprowadzono dodatkową enumerację, niezależną od regresji w audycie I:

- Dla `0≤|A|,|B|≤3` sprawdzono wszystkie **689 relacji** `R⊆A×B` (włącznie z przypadkami pustymi); dokładnie **60** spełniało równoważne warunki bycia wykresem funkcji. Nie stwierdzono rozbieżności.
- Dla wszystkich **400** rodzin `(X_i)_{i∈I}` o `0≤|I|≤3`, gdzie niepuste zbiory `X_i` są podzbiorami `{0,1,2}`, sprawdzono niepustość włókien projekcji `D→I` oraz poprawność konstrukcji skończonej funkcji wyboru. Uwzględniono pusty zbiór indeksów. Nie stwierdzono rozbieżności.
- Poprzedni zestaw regresyjny `tools/tests/test_logic_and_set_theory_ch07.py` przebadał 499 funkcji dla `0≤|A|,|B|≤4`; wciąż jest uruchamiany w CI.

Te kontrole **nie są dowodem twierdzeń dla dowolnych zbiorów**: ich rolą jest wykrywanie kontrprzykładów w przypadkach skończonych.

## Integralność dokumentu

- Struktura środowisk i dowodów jest zbilansowana.
- Zachowano **14 etykiet** rozdziału 07. W sumie rozdziały 01–07 obejmują **223 unikatowe etykiety** i **86 odsyłaczy**.
- Cztery niezdefiniowane na tym etapie książki cele są dokumentowanymi odsyłaczami do przyszłych rozdziałów 08, 09, 10 i 25: `ch:function-operations`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`. Nie usuwano ich.
- Diagram włókien nie uległ zmianie od poprzedniego przeglądu wizualnego; nie ma potrzeby ponownie zmieniać układu rysunku.
- Dedykowany workflow `.github/workflows/logic-and-set-theory-chapter.yml` jest rozszerzony o uruchamianie przy zapisie przyszłych raportów audytu rozdziału 07; kompilację PDF, kontrolę etykiet i przepełnień należy potwierdzić wynikiem bieżącego przebiegu CI.

## Konkluzja i następny krok

**Rozdział 07 jest stabilny merytorycznie po dwóch niezależnych iteracjach.** Ponieważ ta iteracja nie wymagała żadnej zmiany pliku `.tex`, można zamknąć audyty rozdziału 07 po zielonej walidacji GitHub Actions. Następny rozdział: **08 — „Obrazy, przeciwobrazy i działania na funkcjach”**. Zgodnie ze strategią audytować istniejący tekst, a nie dodawać nowego materiału.
