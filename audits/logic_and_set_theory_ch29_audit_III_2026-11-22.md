# Logika matematyczna i teoria mnogości — rozdział 29, audyt III

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/29-slabsze-zasady-wyboru-i-ich-ograniczenia.tex`.

## Audyt dowodu pełnego twierdzenia Tychonoffa ⇒ AC

W pierwotnej wersji dowodu dla rodziny `(A_i)` występowało słowne „dołączmy nowy punkt `∞_i`” oraz zapis `A_i⊔{∞_i}`, po czym dowód traktował `A_i` jak literalny podzbiór produktu. Takie utożsamienie jest standardowe, ale nie wyjaśnia konstrukcji punktów nowych równocześnie dla wszystkich indeksów w ZF. Ponieważ właśnie wyprowadzamy AC, należy wykluczyć nawet pozornie ukryty wybór.

Zastąpiono konstrukcję wzorem jednoznacznym:
`Â_i=A_i×{0}`, `∞_i=(i,1)`, `X_i=Â_i∪{∞_i}`.
Rozłączność jest wymuszona przez drugi znacznik. Sprawdzono bezpośrednio, że czteroelementowa topologia `{∅,Â_i,{∞_i},X_i}` jest poprawna, a każdy czynnik jest zwarty; `Â_i` jest domknięto-otwarty. Kanoniczny punkt `i↦∞_i` całego produktu istnieje przez zastępowanie, bez AC. Zbiory `C_i={x:x(i)∈Â_i}` są domknięte. Ich skończone przekroje są niepuste przez dowiedziony wybór dla skończonych rodzin (Twierdzenie `thm:choice-finite-family`). Zwartość produktu daje `x∈⋂_i C_i`; rozkodowanie `x(i)=(a_i,0)` zapewnia jednoznaczną funkcję wyboru `i↦a_i`.

Wynik matematyczny się nie zmienił, ale wszystkie elementy konstrukcji zostały zdefiniowane w ZF i jawnie zweryfikowane. Dodano odsyłacz do wyboru dla rodzin skończonych oraz asercje regresyjne kontrolujące znaczniki i rozkodowanie.

## Sprawdzenie pozostałych fragmentów

Skontrolowano AC ⇒ DC ⇒ ACω, wybór ze skończonej rodziny, przykład jawnej reguły wyboru, dowód Baire'a z DC z nowym warunkiem domkniętych kul, równoważność UF i BPI, oraz implikację Tychonoffa dla zwartych Hausdorffa. Nie stwierdzono nowego zastosowania pełnego AC w żadnym dowodzie deklarowanym jako ZF albo ZF+BPI.

**Inwentarz bez zmian:** 6 definicji, 7 twierdzeń, 1 lemat, 5 przykładów, 7 uwag, 8 dowodów, 24 etykiety; odsyłacze wzrosły z 10 do **11** przez uzasadnioną referencję do rozdziału 26.

**Werdykt:** audyt III przyniósł doprecyzowanie konstrukcji w ZF; dalsza niezależna kontrola potrzebna.
