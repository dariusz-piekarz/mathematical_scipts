# CAT-37 — audyt kontrolny

Weryfikowany blob rozdziału: `9fcb018a2db6f5cc31296b966e1f7596e2e0457a`.
Testy regresyjne: commit `113788b99c5ddfb04281a1a60ee85c83952a6885`.

- Sprawdzono etykiety wszystkich 38 plików rozdziałów CAT-00–CAT-37 (186 + 653 = 839 wystąpień). Wszystkie 36 etykiet CAT-37 oraz wszystkie 18 różnych celów jego odsyłaczy mają dokładnie jedno wystąpienie w zbiorze rozdziałów.
- 22 środowiska proof. Poprzednie kontrole struktury i integracji książki oraz katalogu pozostają aktualne dla tego samego blobu.
- W poprzedniej iteracji niezależne obliczenia skończone dały 2128/2128 przypadków permutacji blokowych, 1111/1111 wewnętrznych oraz 47668/47668 zgodności ze składaniem. Są to kontrole pomocnicze, nie formalne dowody ani wynik wykonania pełnej suity Pythona.
- Kontrola ostatnich poprawek (monada operady symetrycznej, przeszkoda dla morfizmu As -> E1, etykietowane drzewa Liego, operada liniowa zerowa): nie wykryto nowej usterki.
- CI: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46055118274 — status queued, job validate 140695612661 bez wykonanych kroków w chwili kontroli.

Status: część matematyczna i odsyłacze kontrolnie sprawdzone; odbiór końcowy WSTRZYMANY do rzeczywistego sukcesu CI, kompilacji PDF i kontroli wizualnej trzech diagramów. Nie deklarujemy zamknięcia rozdziału ani wykonania testów Python.
