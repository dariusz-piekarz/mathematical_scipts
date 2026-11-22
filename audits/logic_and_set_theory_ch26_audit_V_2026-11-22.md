# Logika matematyczna i teoria mnogości — rozdział 26, audyt V (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex`  
**Zakres:** ponowny pełny audyt istniejących 27 obiektów numerowanych i przykładów w rozdziale, bez wprowadzania nowych twierdzeń i bez modyfikowania tekstu w tej iteracji.

## Ponowna kontrola matematyczna

1. **Definicja aksjomatu wyboru:** dla funkcji indeksowanej `(A_i)_{i∈I}` kwantyfikatory i przeciwdziedzina funkcji wyboru są poprawne, w tym `I=∅`; rozróżniono rodzinę indeksowaną od zbioru wartości.
2. **Porównanie dobrych porządków:** zweryfikowano zgodność izomorfizmów na wspólnych odcinkach początkowych, konstrukcję sumy izomorfizmów, jej maksymalność, trójpodział oraz argument indukcyjny dowodzący `x≤f(x)` dla rosnącego zanurzenia `f:W→W`. Nie korzysta on z AC.
3. **Twierdzenie Hartogsa w ZF:** zweryfikowano istnienie zbioru par `(S,R)` przez separację w `P(A)×P(A×A)`, klasy izomorfizmu przez zastępowanie/separację, niezależność relacji porównania od reprezentantów, trichotomię i przechodniość przez składanie izomorfizmów odcinków początkowych, dobry porządek `H(A)` i sprzeczność z hipotetyczną iniekcją `H(A)→A`. Argument uwzględnia `A=∅` i nie używa liczb porządkowych.
4. **AC ⇒ dobre uporządkowanie:** jedną funkcję wyboru przyjęto na `P(A)\{∅}`; zbiór częściowych, zgodnych konstrukcji istnieje przez separację w `P(H×A)`. Wykazano, że funkcja globalna zatrzymuje się przed wyczerpaniem `H(A)`, a jej obraz pokrywa `A`.
5. **Dobre uporządkowanie ⇒ Zorn:** przypadek pustego łańcucha zapewnia niepustość `P`; zbiór częściowych funkcji decyzyjnych istnieje przez separację w `P(P×{0,1})`. Ich suma daje maksymalny łańcuch, a ograniczenie górne — element maksymalny. Dla hipotetycznego `v>u` wprost wykazano `v∉C`, by otrzymać właściwe powiększenie łańcucha.
6. **Zorn ⇔ Hausdorff:** suma łańcucha łańcuchów jest łańcuchem i należy do `P(P)`; w drugą stronę ograniczenie górne łańcucha maksymalnego daje element maksymalny. Sprawdzono przypadki puste.
7. **Zorn ⇒ AC:** zbiór częściowych funkcji wyboru uzyskano przez separację w `P(I×⋃_{i∈I}A_i)`; sumy łańcuchów należą do tego samego zbioru i nie naruszają warunku wyboru; maksymalność implikuje pełną dziedzinę.
8. **Wybór skończony w ZF:** zweryfikowano po naprawie audytu II indukcję po `n` dla dowolnej rodziny `(B_k)_{k∈n}`; przy przedłużeniu do `S(n)` używa się wyłącznie określonego `B_n`. Bijekcja `e:n→I` pojawia się dopiero po skończeniu indukcji i jest używana tylko w jej dziedzinie. Brak odwołania do niedozwolonego `e(n)`.
9. **Dalsze równoważności:** sprawdzono konstrukcję sumy rozłącznej i przekrojów surjekcji oraz transwersal relacji równoważności; rozróżniono niepustość iloczynu rodziny od istnienia iloczynu jako zbioru.
10. **Istnienie bazy:** zweryfikowano wyrażalność liniowej niezależności, górne ograniczenia łańcuchów, wykazanie generowania przez element maksymalny, jednoznaczność skończenie nośnych współczynników i przypadek przestrzeni zerowej.

**Wynik niezależnego audytu V:** bez nowych błędów matematycznych, luk w uzasadnieniach wymagających zmian, niepoprawnych odsyłaczy i naruszeń przyjętej terminologii. Nie zmieniono treści rozdziału w tej iteracji.

## Inwentarz i walidacja techniczna

- **5 definicji, 10 przykładów, 1 lemat, 8 twierdzeń, 1 wniosek, 2 uwagi, 10 dowodów.**
- **20 etykiet i 18 odsyłaczy**; sprawdzone przez regresję oraz CI całej książki.
- GitHub Actions [45005482287](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45005482287): **SUCCESS** dla dokładnie tych samych bajtów źródłowych rozdziału 26 (potwierdzona identyczność SHA bloba na gałęzi i w przebiegu). Regresje rozdziału 26: **PASS**.
- Pełny PDF: **203 strony**; sam rozdział 26: **9 stron**. Wszystkie 9 stron wyrenderowano i obejrzano wizualnie; nie wykryto nachodzących napisów, przyciętych równań ani naruszeń marginesów.
- Log kompilatora: **0** `Overfull \\hbox`, **0** nierozwiązanych odsyłaczy, **0** nierozwiązanych cytowań, **0** błędów LaTeX. Wystąpiło **1** niewielkie ostrzeżenie `Underfull \\hbox` (badness 1406), bez wpływu na czytelność i bez wymaganego przeskładu.
- Rozdział nie wymaga nowych twierdzeń ani przykładowych konstrukcji; zachowano sumę niepowtarzalnej treści wcześniejszych źródeł.

## Werdykt

**Rozdział 26 — STABILNY po audycie V.** Po poprawkach audytów II–IV kolejna, niezależna iteracja nie wykazała problemów; dokument przeszedł testy, CI i kontrolę wizualną PDF. Można zamknąć rozdział 26 i przejść do następnego dopiero na wyraźne polecenie użytkownika.
