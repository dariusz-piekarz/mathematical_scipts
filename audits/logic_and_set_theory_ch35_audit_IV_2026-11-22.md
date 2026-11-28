# Logika matematyczna i teoria mnogości — audyt IV rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Stan:** audyt IV zakończony, poprawki wprowadzone, walidacja CI pomyślna; rozdział NIE jest jeszcze stabilny.

## Znaleziona luka i poprawka matematyczna

Ponownie skontrolowano lemat o przejściu między wymuszaniem przez pojęcie P i wartościami w jego uzupełnieniu B=RO(P), w szczególności przypadek kwantyfikatora egzystencjalnego. Poprzednia wersja konstruowała przekład nazw P na nazwy B, lecz nie uzasadniała, że każdy świadek pełności B ma odpowiednik w języku nazw P. To jest rzeczywista luka dowodowa: przy przejściu od wartości egzystencji do relacji wymuszania przez warunek nie wolno użyć nazwy boolowskiej bez reprezentacji po stronie P.

Dodano przekład wsteczny: dla nazwy boolowskiej tau tworzy się nazwę porządkową z par (rho^P,p), gdzie rho występuje w dziedzinie tau i i(p) <= tau(rho). Jej poprawność zbiorową uzasadnia się rekurencją po rangach. Z gęstości obrazów warunków wynika dla każdego b w B, że b jest kresem górnym tych i(p), które leżą poniżej b. Indukcja i podstawianie dowodzą, że wartość boolowska równości tau z podwójnym przekładem (tau^P)^B jest równa 1.

Dodatkowo wyjaśniono subtelność: nierówność i(r)<=i(p) nie oznacza r<=p. Jeśli jednak i(p)∧b>0, gęstość pozwala wybrać r o dodatnim obrazie poniżej i(p)∧b, po czym wspólne wzmocnienie r,p daje warunek q<=p o i(q)<=b. To domyka indukcję dla negacji i egzystencji w relacji wymuszania. Wskazano, gdzie używa się lematu pełności, podstawiania i gęstości.

## Testy i regresje

Dodano test test_every_fork_boolean_coefficient_has_poset_pullback. Używa czteroelementowej algebry zbiorów regularnie otwartych skończonego pojęcia wymuszania o trzech warunkach: top, left, right. Weryfikuje tożsamość gęstościową dla czterech współczynników boolowskich oraz dokładną rekonstrukcję szesnastu par współczynników. Lokalna kontrola algorytmu 4+16/20 PASS. Cały zestaw rozdziału ma teraz 16 metod testowych; pełny przebieg w CI przeszedł.

Jedyny początkowy błąd CI po poprawce wynikał z twardo zakodowanego poprzedniego inwentarza 670 odsyłaczy: dodanie prawidłowego odsyłacza zwiększyło ich liczbę do 671. Workflow i test rozdziału 35 otrzymały poprawne liczniki (odpowiednio 671 odsyłaczy w książce i 31 w rozdziale).

**Źródła i integracja po audycie:** 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 unikatowych etykiet, 31 odsyłaczy. Wszystkie środowiska LaTeX są prawidłowo domknięte, brak konfliktu etykiet. Aktualny blob źródła: e84949206bd9aea22accd2a168004141a3a2edb7.

**Commity:** 4ef66744ba1e8b83b37dcd111ad906064d9da36a (dowód), ee428b5ac92c2e2182fdc7aa9d94ec12562584cb (test), 0d8a21bb9940fd52324d45a2d40e08cbdbcff794 (workflow), 5703bd1e6fb5a4315078f7588e73a8d9a6dfa9eb (testowy inwentarz).

## CI i kontrola PDF

[GitHub Actions 45047301345](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047301345): SUCCESS. Zakończyły się powodzeniem testy 01–35 (w tym 16 testów rozdziału 35), weryfikacja inwentarza, kompilacja LaTeX, kontrola logu i archiwizacja PDF.

Pobrano rzeczywisty artefakt tego przebiegu. PDF ma 308 stron; rozdział 35 zajmuje strony PDF 296–308, drukowane 287–299 (13 stron). Wszystkie 13 stron wyrenderowano i obejrzano w zbiorczym układzie. Bez widocznych kolizji, uciętych wzorów i nieczytelnego tekstu. W logu: 0 błędów, 0 przepełnionych wierszy, 0 niezdefiniowanych odsyłaczy i cytowań, 1 ostrzeżenie Underfull hbox w całej książce. Ostatnia strona rozdziału jest krótka; nie jest to wada składu.

## Werdykt i następna iteracja

Audyt IV nie jest czysty, ponieważ wykrył i usunął nową lukę matematyczną. Licznik niezależnych czystych audytów: 0. Kolejny audyt V powinien rozpocząć się od tej samej wersji źródła, ponownie sprawdzić matematykę (zwłaszcza pełność, podstawianie, przekształcenie nazw, aksjomat wyboru i względną niesprzeczność), terminologię, LaTeX, przykłady i regresje. Po dwóch niezależnych czystych audytach wykonać osobny potwierdzający audyt końcowy. CI nie jest formalnym dowodem w Lean.
