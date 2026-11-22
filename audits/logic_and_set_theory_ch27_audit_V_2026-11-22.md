# Logika matematyczna i teoria mnogości — rozdział 27, audyt V

**Data:** 22 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/27-liczby-kardynalne-i-arytmetyka-mocy.tex`

## Uzupełnienie dowodu w ZF

Ponownie skontrolowano diagonalizację w twierdzeniu o nieprzeliczalności liczb rzeczywistych (`thm:card-n-not-r`). W dotychczasowym tekście dla każdego `n∈ω` zdefiniowano jednoznacznie `S_n` jako przeciwobraz `e(n)` przez iniekcję `c:P(ω)→R` albo zbiór pusty. Jednak nie uzasadniono, że jednocześnie określone wartości tworzą **wykres funkcji będący zbiorem**.

Poprawka audytu V: wyrażenie definiujące `S_n` jest formułą ZF z parametrami `e,c` i dla każdego `n∈ω` wyznacza dokładnie jeden zbiór. **Schemat zastępowania** konstruuje zatem zbiór par stanowiący wykres funkcji `n↦S_n`; separacja wyodrębnia następnie `D={n∈ω:n∉S_n}`. Nie występuje ukryty nieskończony wybór.

Weryfikacja struktury: 4 definicje, 11 twierdzeń, 2 wnioski, 5 przykładów, 6 uwag, 13 dowodów, 1 rysunek; 24 etykiety i 16 odsyłaczy. Odesłanie do jeszcze nieutworzonego rozdziału o ordynałach `ch:ordinals` pozostaje jawnie kontrolowanym odsyłaczem przyszłym.

**Werdykt:** poprawiono istniejący argument bez dodawania materiału; do pełnej stabilności potrzebny audyt VI bez poprawek po zielonym CI i przeglądzie PDF.
