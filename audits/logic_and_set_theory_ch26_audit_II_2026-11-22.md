# Logika matematyczna i teoria mnogości — rozdział 26, audyt II

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/26-aksjomat-wyboru-i-jego-rownowazne-postacie.tex`  
**Zasada:** audyt istniejącej treści, bez dodawania nowych twierdzeń, lematów, definicji i przykładów.

## Wykryte błędy i poprawki

1. **Rzeczywisty błąd w twierdzeniu o wyborze ze skończonej rodziny:** poprzedni dowód deklarował bijekcję `e:n → I`, a następnie w kroku indukcji używał wartości `e(n)`. Ponieważ `n ∉ n`, wyrażenie było niezdefiniowane. Naprawiono dowód przez indukcję zdania o **dowolnej** rodzinie `(B_k)_{k∈n}` dla każdego `n∈ω`. W kroku indukcji do wyboru z rodziny na `n` dołącza się pojedynczy element `B_n`. Dopiero po zakończeniu indukcji wybiera się bijekcję `e:n→I` i stosuje wynik do rodziny `B_k=A_{e(k)}`. Nie następuje odwołanie do `e(n)`.
2. **Twierdzenie Hartogsa:** jawnie wyznaczono zbiór ograniczający pary dobrych porządków: `P(A)×P(A×A)`. Doprecyzowano separację zbioru takich par, formułę wyrażającą izomorficzność uporządkowań, istnienie poszczególnych klas oraz zbioru ich wszystkich przez zastępowanie (lub separację w `P(W)`). Zapisano odsyłacz do wcześniejszego dowodu istnienia iloczynu kartezjańskiego.
3. **AC implikuje dobre uporządkowanie:** zbiór częściowych funkcji wyboru z regułą Zermela został osadzony w `P(H×A)` i uzyskany przez separację, bez nieuzasadnionego kwantyfikowania po wszystkich klasach funkcji. Zaznaczono obecność funkcji pustej.
4. **Dobre uporządkowanie implikuje Zorna:** podano, dlaczego założenie lematu Zorna wymusza niepustość `P` (ograniczenie górne pustego łańcucha); funkcje podejmujące decyzje należą do zbioru uzyskanego przez separację w `P(P×{0,1})`.
5. **Zorn implikuje AC:** zbiór częściowych funkcji wyboru jawnie skonstruowano przez separację w `P(I×⋃_{i∈I} A_i)`. Ta sama konstrukcja gwarantuje istnienie iloczynu kartezjańskiego rodziny w ZF, choć jego niepustość jest treścią AC.
6. **Język:** poprawiono mylenie indeksowanej rodziny `(A_i)_{i∈I}` ze zbiorem jej wartości; poprawiono zgodność gramatyczną zdania o zanurzeniu dobrego porządku i odwołanie do twierdzenia (wcześniej mylnie nazwanego lematem).

## Ponowna kontrola matematyczna

Sprawdzono istnienie i jednoznaczność porównania dobrych porządków, ścisłe zdefiniowanie `H(A)`, nieistnienie iniekcji `H(A)→A`, konstrukcję dobrego porządku z jednej funkcji wyboru, konstrukcję maksymalnego łańcucha bez użycia Zorna, obie implikacje Hausdorff–Zorn oraz dowód Zorn–AC z częściowych funkcji wyboru. W konstrukcjach poprzedzających przyjęcie AC nie stosowano dowolnych nieskończonych wyborów.

## Inwentarz i testy

Inwentarz bez zmian: 5 definicji, 10 przykładów, 1 lemat, 8 twierdzeń, 1 wniosek, 2 uwagi, 10 dowodów. 20 etykiet; liczba odsyłaczy wzrosła z 17 do 18 w wyniku odesłania do wcześniejszej konstrukcji iloczynu kartezjańskiego. Dodano regresję chroniącą przed użyciem niedozwolonego `A_{e(n)}` oraz sprawdzającą istnienie konstrukcji zbiorowych.

**Werdykt:** audyt II wykrył błąd formalny w dowodzie i poprawił go. Konieczny kolejny niezależny audyt stabilizacyjny po walidacji PDF i CI.
