# Logika matematyczna i teoria mnogości — rozdział 26, audyt III

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex`

## Ponowna niezależna kontrola

1. Ponownie przeanalizowano dowód jedyności izomorfizmu odcinków początkowych, trójpodział możliwych relacji między dobrymi porządkami oraz indukcję po dobrym porządku wykazującą `x ≤ f(x)`.
2. Skontrolowano konstrukcję Hartogsa dla `A=∅` i zbiorów skończonych oraz argument, że `H(A)` sam jest dobrze uporządkowany. Weryfikacja wykazała potrzebę doprecyzowania, że symbole `U,V` reprezentują **uporządkowane pary** `(S,R)`, a nie same podzbiory `A`. Dopisano tę konwencję bez zmiany twierdzenia.
3. W zastosowaniu Zorna do porównania mocy dodano uzasadnienie, że zbiór częściowych iniekcji `f:D→B`, `D⊆A`, istnieje przez separację w `P(A×B)`. W poprzedniej wersji istnienie `P` było tylko zadeklarowane.
4. Sprawdzono poprawioną indukcję dotyczącą skończonych rodzin. Wszystkie wartości funkcji są określone w swoich dziedzinach; wynik dla dowolnego zbioru indeksów `I` uzyskuje się dopiero po zakończeniu indukcji, korzystając z bijekcji `e:n→I`.
5. Skontrolowano logiczne domknięcie cyklu równoważności: `AC⇒dobre uporządkowanie⇒Zorn⇒AC`, `Zorn⇔maksymalność Hausdorffa`, `AC⇔istnienie przekrojów surjekcji⇔istnienie transwersal`.
6. Ponownie sprawdzono argument Zorna dla zbioru liniowo niezależnych podzbiorów przestrzeni wektorowej: istnienie tego zbioru, stabilność niezależności przy sumach łańcuchów, generowanie przez bazę maksymalną, jednoznaczność współczynników o skończonym nośniku, przypadek przestrzeni zerowej.
7. Zachowano pełny inwentarz (5 definicji, 10 przykładów, 1 lemat, 8 twierdzeń, 1 wniosek, 2 uwagi, 10 dowodów), 20 unikalnych etykiet i 18 odsyłaczy. Rozszerzono test o dwa nowe warunki formalne, bez dodawania nowej treści matematycznej.

## Wynik

Audyt III wykrył i poprawił dwa niedoprecyzowane miejsca w istniejących argumentach: zbiór częściowych iniekcji i reprezentanci typów dobrego porządku. **Nie oznaczono jeszcze rozdziału jako stabilnego**, ponieważ po rzeczywistych poprawkach potrzebny jest audyt IV bez kolejnych modyfikacji treści, przy zielonym CI i wizualnej kontroli wszystkich stron rozdziału.
