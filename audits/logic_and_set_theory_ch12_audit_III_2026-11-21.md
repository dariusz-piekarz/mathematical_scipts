# Logika matematyczna i teoria mnogości — rozdział 12, audyt III

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/12-poprawnosc-logiki-pierwszego-rzedu.tex`.  
**Niezmieniony blob Git po audycie II:** `e6850a7115b66bc4e04fab52fbf7b9a6e9f3b456`.  
**Tryb:** trzeci, niezależny audyt całego rozdziału; bez nowych twierdzeń, lematów, definicji, wniosków i przykładów.

## Konkluzja

**Audyt III jest czysty.** Nie stwierdzono nowego błędu matematycznego ani luki wymagającej zmiany źródła LaTeX. **Nie zmieniono żadnego pliku rozdziału**, jego odsyłaczy, środowisk matematycznych ani rysunków. Zgodnie z przyjętą metodą pracy rozdział uznajemy za stabilny matematycznie, a jego formalne zamknięcie następuje po zielonym CI na commicie z niniejszym raportem.

Ponownie sprawdzono **3 twierdzenia, 3 lematy, 2 wnioski, 1 definicję, 4 przykłady, 3 uwagi i 8 dowodów**, w tym pełną indukcję po drzewie dedukcji w twierdzeniu o poprawności.

## Trzeci niezależny przegląd dowodów i założeń

1. **Konsekwencja semantyczna dla formuł.** Kwantyfikatory obejmują wszystkie struktury danego języka o niepustym uniwersum i wszystkie wartościowania. Dlatego definicja obejmuje także formuły ze zmiennymi wolnymi. W przypadku zbioru zdań zachodzi zgodność z wcześniejszą definicją konsekwencji dla zdań.
2. **Lemat o zmiennej niewolnej (`lem:soundness-fresh`).** Dwa wartościowania różniące się tylko na zmiennej niewolnej w formule mają identyczną wartość logiczną tej formuły; dowód jest prawidłowym zastosowaniem twierdzenia o zgodności wartościowań z rozdziału 10.
3. **Lemat o podstawieniu (`lem:soundness-subst`).** Jawnie zakłada się dopuszczalność podstawienia i wspólny język termu i formuły. Odsyłacz do udowodnionego twierdzenia semantycznego jest prawidłowy również przy zagnieżdżonych kwantyfikatorach.
4. **Zastępowanie równych termów (`lem:soundness-equality`).** Równość interpretacji termów `t,u` przy ustalonym `s` oraz dwa zastosowania lematu o podstawieniu dają poprawną regułę `=E`. Nie zakłada się identyczności składniowej termów i nie pomija warunku dopuszczalności żadnego podstawienia.
5. **Przypadek bazowy głównej indukcji (`thm:soundness`).** Poprawka audytu I obejmuje wszystkie liście będące aktualnymi otwartymi założeniami poddedukcji, **również tymczasowymi**. Dopiero w korzeniu pełnego drzewa korzystamy z zawierania się otwartych założeń w zbiorze `Γ`. To usuwa wcześniejszą lukę bez zmiany hipotezy indukcyjnej.
6. **Spójniki zdaniowe.** Wprowadzenie i eliminacja `∧,∨,→,↔,¬`, reguły dla `⊥` i klasyczne `RAA` zachowują prawdę w odpowiednich kontekstach otwartych założeń. W szczególności `→I` i `∨E` rzeczywiście rozładowują tylko właściwe wystąpienia założeń.
7. **Reguły `∀E` i `∃I`.** Lemat o podstawieniu przenosi prawdziwość między `α[x:=t]` oraz `α` przy zmodyfikowanym wartościowaniu; wartość termu `t` jest poprawnym świadkiem wprowadzenia egzystencjalnego.
8. **Reguła `∀I`.** Świeżość uogólnianej zmiennej względem wszystkich rzeczywiście otwartych założeń poddedukcji gwarantuje zachowanie tych założeń przy zmianie wartości tej zmiennej na dowolny element uniwersum. Zastosowanie hipotezy indukcyjnej dla każdego elementu dowodzi formuły ogólnej.
9. **Reguła `∃E`.** Świeża zmienna `y` nie występuje w formule kwantyfikowanej ani w końcowym wniosku i nie jest wolna w pozostałych otwartych założeniach obu gałęzi. Po wybraniu świadka `a` konstruujemy `r=s[y↦a]`; zgodność wartościowań, lemat o podstawieniu i hipoteza indukcyjna pozwalają przenieść wniosek z `r` do `s`. Argument nie wymaga nieskończonego zbioru `Γ` pozbawionego pewnej nazwy zmiennej.
10. **Dwa wnioski z poprawności.** Istnienie kontrmodelu wyklucza formalny dowód **formuły**, nie tylko zdania; spełnialność `Γ` wyklucza dowód sprzeczności. Doprecyzowany w audycie II tytuł pierwszego wniosku jest zgodny z tezą.
11. **Semantyczne twierdzenie o dedukcji.** `Γ∪{α}⊨β` jest równoważne `Γ⊨α→β` dla zdań i dla formuł z wolnymi zmiennymi; w obu stronach używane jest to samo wartościowanie i ten sam język.
12. **Syntaktyczna skończoność wyprowadzalności.** Dowód przez skończone drzewo formalne nie wymaga semantycznej zwartości. Uwaga wyraźnie nie wyprowadza zwartości semantycznej bez twierdzenia o pełności.

## Niezależne testy audytu III

Oprócz przeglądu ogólnych dowodów wykonano nową enumerację **840 struktur skończonych** z uniwersami 1-, 2- i 3-elementowymi oraz **17 608 wartościowań**. Użyto różnych interpretacji dwóch predykatów jednoargumentowych i relacji binarnej. W semantycznym twierdzeniu o dedukcji sprawdzono **sześć formuł testowych** (w tym atomy, równość i formuły z kwantyfikatorami) i wszystkie **16** rozważanych podzbiorów kontekstu czterech formuł.

| Kontrola | Liczba przypadków | Wynik |
|---|---:|---|
| Semantyczne twierdzenie o dedukcji z otwartymi formułami | 483 840 | PASS |
| `∀I` przy niewystępowaniu uogólnianej zmiennej w otwartych założeniach | 17 608 | PASS |
| `∃E` przy właściwej niezależności wniosku od zmiennej świadka | 17 608 | PASS |
| Zastępowanie równych wartości w formule zawierającej kwantyfikator | 633 888 | PASS |
| Dwie dualności kwantyfikatorów | 35 216 | PASS |

**Zero kontrprzykładów** dla poprawnych reguł i twierdzeń. Testy na strukturach skończonych nie stanowią dowodu ogólnej poprawności dla wszystkich struktur, dlatego każdy istniejący dowód skontrolowano również matematycznie.

## Integralność i CI

- Zachowano inwentarz rozdziału: **10 etykiet**, **24 odsyłacze**, 3 twierdzenia, 3 lematy, 2 wnioski, 1 definicja, 4 przykłady, 3 uwagi i 8 dowodów.
- Książka obejmująca rozdziały 01–12 ma **319 unikatowych etykiet**, **143 wystąpienia odsyłaczy** i jeden udokumentowany cel przyszły `ch:zf-axioms`.
- Po audycie II dedykowany workflow [44932073636](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932073636) zakończył się sukcesem: **108 stron PDF**, **24 testy regresyjne**, brak nieoczekiwanych brakujących referencji, brak przepełnionych wierszy LaTeX. Globalny workflow aplikacji [44932073519](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932073519) również zakończył się sukcesem, włącznie z testami przeglądarkowymi.
- Niniejszy raport uruchamia kolejną walidację CI. Jej pozytywny wynik trzeba potwierdzić na commicie raportu, zanim rozdział zostanie formalnie zamknięty.

## Status

**Audyt III czysty: rozdział 12 stabilny merytorycznie, bez zmian pliku źródłowego.** Po zielonym CI na tym raporcie rozdział można zamknąć. Następny etap to audyt I istniejącego rozdziału **13 — „Twierdzenie o pełności i konstrukcja Henkina”**, nadal bez rozszerzania materiału.
