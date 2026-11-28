# Rozdział 28 — audyt III: arytmetyka ordynałów i jej przykłady

**Data:** 2026-11-22. **Plik:** `chapters/pl/logic_and_set_theory/28-liczby-porzadkowe-i-rekurencja-pozaskonczona.tex`.

## Kontrola działań na ordynałach
1. Rozwinięto rekurencyjną definicję `α+β`, z rozróżnieniem przypadku `0`, następnika i ordynału granicznego. Wprost wyjaśniono istnienie jedynej funkcji na dowolnym ustalonym odcinku ordynałów i zgodność funkcji uzyskanych na dwóch różnych odcinkach.
2. Uzasadniono przez indukcję `1+n=n+1` dla `n∈ω`; stąd obliczenie `1+ω=ω` nie pomija żadnego kroku.
3. Przy mnożeniu ordynałów wyjaśniono, jak rozumieć operację klasową na **wszystkich** funkcjach częściowych wymaganych w twierdzeniu rekurencyjnym: dla niepoprawnych wartości przyjmujemy umownie `0`, a poprawność wybranej gałęzi wynika indukcyjnie. Zachowano rekurencyjną definicję `α·β` i jej jedyność.
4. Uzasadniono ścisłą nierówność `ω+ω>ω` przez to, że `ω+1` jest jednym z elementów rodziny mającej supremum `ω+ω`.
5. Przy porównaniu mocy i typów porządkowych dodano **jawny wzór** bijekcji `f:ω→ω+1`: `f(0)=ω` i `f(n+1)=n`. Uzasadniono, dlaczego nie jest to izomorfizm dobrych porządków.
6. W hierarchii von Neumanna skorygowano minimalne założenie na odcinek `α≥4`, wystarczający do zdefiniowania poziomów `V_0,ldots,V_3`.

**Inwentarz:** 4 definicje, 5 przykładów, 2 lematy, 5 twierdzeń, 1 wniosek, 3 uwagi, 8 dowodów; bez zmian. **Etykiety:** 17. **Odsyłacze:** 20. Zależności ZF i ZFC rozgraniczone jawnie.

## Testy
Rozszerzono kontrolę regresyjną o arytmetykę skończonych ordynałów, formalną rekursję, bijekcję `ω→ω+1` i dowód `ω+ω>ω`. Jeden początkowy przebieg CI ujawnił wyłącznie nieaktualną asercję testową rozdziału 27 po rozwiązaniu odesłania do `ch:ordinals`; zaktualizowano oczekiwanie. Kolejny przebieg ujawnił niezgodność dosłownego fragmentu sprawdzanego przez test rozdziału 28 z poprawną treścią źródłową; poprawiono test, bez zmiany matematyki.

**Wynik:** do audytu stabilizacyjnego po zielonym CI i kontroli PDF.
