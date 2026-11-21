# Algebra liniowa — rozdział 30, audyt IV: korekta składu

**Data:** 21 listopada 2026  
**Poprzedni źródłowy blob:** `c5e48050c75b27c31162fba95862b6ecac944971`.

## Wykryta usterka
[Workflow #44955768439](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44955768439) poprawnie wykonał testy matematyczne, ale zakończył się FAILURE na etapie „Verify compilation artifact and unresolved references”: `Overfull \\hbox (15.57837pt too wide)` w akapicie wierszy 204–218 źródła LA-30.

## Poprawka
- Długą formułę antysymetryzacji z uwagi o izomorfizmie liniowym `ΛV ≅ Cl(V)` wydzielono jako osobne równanie, zachowując skalar `1/r!`, sumę po permutacjach i wszystkie znaki.
- Żaden dowód, założenie ani numer etykiety nie uległ zmianie.
- Ponowny CI sprawdzi układ, log LaTeX i eksport pojedynczego rozdziału.

## Decyzja
**Audyt IV nie jest czysty**, ponieważ poprawiono usterkę składu. Po uzyskaniu zielonego CI należy wykonać pełną inspekcję PDF i dwie niezależne czyste iteracje.
