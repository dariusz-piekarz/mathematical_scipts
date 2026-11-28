# PDE-01 — iteracja 10, 2026-11-24

Źródło: [rozdział 01](../../../chapters/pl/partial_differential_equations/01-wprowadzenie-do-pde.tex), blob aeea9d0a8c39cb2a2049d0cd982688dd370fc874, bez zmian względem iteracji 9.
Kryteria: [regression.md](../../../tests/mathematical/partial_differential_equations/chapter-01/regression.md).

- Drugi przebieg kontrolny bez nowych istotnych usterek stwierdzonych w treści. Kontrola strukturalna wykonana: 35 unikalnych etykiet, 16 rozwiązywalnych odsyłaczy, zgodne zagnieżdżenie środowisk, 70 kolejnych unikalnych ID kryteriów przypisanych do istniejących etykiet, 13 dowodów i 3 rysunki.
- Lokalnie odtworzono plik test_energy_hadamard.py, potwierdzono SHA blob 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2 i wykonano python test_energy_hadamard.py -v: 3/3 OK.
- Lokalnie skompilowano trzy aktualne bloki tikzpicture w dokumencie kontrolnym klasy book (11pt, A4, margines 2,7 cm, fontenc T1, lmodern, babel polish, te same biblioteki TikZ). Zgodność tekstów bloków z aktualnym źródłem sprawdzono przez długości i FNV-1a na jednostkach znakowych: 452/d4739901, 512/7806e3c0, 590/654dae91. Nie jest to kompilacja całego rozdziału.
- pdflatex -interaction=nonstopmode -halt-on-error: sukces, jedna strona. pdftoppm -r 150 -png: sukces. Oględziny wszystkich trzech rysunków: napisy Tricomiego nad osią, zaznaczone dwa punkty tej samej charakterystyki i czytelna etykieta; widoczna oś czasu w stożku poza tłem napisu, brak nachodzenia tekstu na obramowanie. Kryteria wizualne 048, 061, 062, 064 i 065 zaliczone dla izolowanych rysunków. Układ rysunków na stronach aktualnego pełnego rozdziału pozostaje do sprawdzenia.
- Przebieg [45406319616](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45406319616) nadal queued. Pełna kompilacja aktualnego rozdziału oraz jego układ stron niepotwierdzone. Lean nie uruchomiono. Rozdział otwarty.
- Raport zapisano poza ścieżkami wyzwalającymi workflow PDE, aby sam raport nie generował kolejnej kompilacji bez zmiany źródła lub testów.

Wyniki strukturalne i trzy testy wykonywalne nie są formalizacją 70 kryteriów semantycznych.
