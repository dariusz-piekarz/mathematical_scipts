# PDE-01 — stabilizacja, iteracja 13, 2026-11-24

Status: STABILIZED (audyt matematyczno-redakcyjny i techniczny, nie formalizacja Lean).

Źródło: [rozdział 01](../../../chapters/pl/partial_differential_equations/01-wprowadzenie-do-pde.tex), Git blob aeea9d0a8c39cb2a2049d0cd982688dd370fc874. Zweryfikowano identyczność blobu na bieżącej gałęzi i w commicie CI 9006c80b920787f1931b9b46e1b2255f9f58edbc.

Dwa czyste przebiegi kontrolne (iteracje 9 i 10), 70 trwałych kryteriów, 35 etykiet, 16 wystąpień odsyłaczy. [Rejestr kryteriów](../../../tests/mathematical/partial_differential_equations/chapter-01/regression.md).

[CI 45406319616](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45406319616): zakończone success, wszystkie kroki success (3 testy wykonywalne, struktura, kompilacja z kanoniczną preambułą, diagnostyka, renderowanie, publikacja artefaktu). Artefakt 14925988001 pobrany i rozpakowany; PDF 14 stron, 14 PNG. Ponowna kontrola logu: brak Undefined control sequence, undefined references, Overfull hbox, Missing character. Oględziny układu wszystkich 14 stron na arkuszu kontaktowym, a stron 6, 8 i 11 w pełnej rozdzielczości. Trzy rysunki czytelne, opisy nie przecinają linii, prawidłowe punkty i osie, podpisy przy rysunkach. Nie stwierdzono usterek układu wymagających zmiany.

Zamknięto otwarte kontrole kompilacji i renderowania. Lean nie uruchomiono; kryteria semantyczne nie są automatycznymi testami. Stabilizacja odnosi się do wskazanego blobu i kompilacji pojedynczego rozdziału; nie oznacza weryfikacji całej książki. Przy zmianie rozdziału ponownie uruchomić odpowiednie kontrole.

Następny rozdział: 02 — metoda charakterystyk, zgodnie z preflight.md.
