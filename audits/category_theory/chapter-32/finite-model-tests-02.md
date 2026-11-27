# CAT-32 — uzupełniające wyniki testów modeli skończonych

Data: 27.11.2026  
Źródło: `chapters/pl/category_theory/32-2-kategorie-i-bikategorie.tex`, blob `a6a0d5afb1e80ea2d5fd7d376385f39e2fae21fa`.

Uzupełnienie do `control-01.md`. Model `Span(FinSet)) obejmuje wszystkie zbiory o liczności 0, 1, 2 i wszystkie rozpiętości z obiektami środkowymi o liczności 0, 1, 2 (43 rozpiętości, 211 2-morfizmów).

Dodatkowe kontrole zakończone PASS:

- 422 sprawdzenia lewych i prawych praw jednostki składania pionowego dla 211 morfizmów;
- 4 507 sprawdzeń łączności składania pionowego dla trzech kolejnych 2-morfizmów;
- 27 243 sprawdzenia zachowywania obu skrajnych nóg przez poziome składanie 2-morfizmów.

Wraz z raportem głównym testy pokrywają kategorie morfizmów, funktorialność składania poziomego, prawo wymiany, naturalność unitorów i łączności, pięciokąt, trójkąt oraz przykład sprzężenia rozpiętości wykresu.

Wyniki są skończoną regresją konstrukcji, a nie dowodem ogólnym. Nie zastępują kompilacji TeX/PDF ani walidacji CI.
