# AF 15B — audyt kontrolny reorganizacji całek wektorowych

28 listopada 2026, gałąź biblioteka-matematyczna-iteracja-6. Źródło: commit 17f9bc31a6fc598cec5bede21e549d94ece13aa0, blob 3ce034449f7298dd37e0e328a8e2b7a5749bf3d3.

## Kontrola
Sprawdzono konstrukcje Birkhoffa, zgodność z Bochnerem i Lebesgue'em, hierarchię całek, domkniętość klasy Pettisa w klasie Dunforda przy zbieżności w półnormie q, niezupełność ilorazów (Rademacher), oba kontrprzykłady Fubiniego, Orlicza–Pettisa, półwariację, kryterium skończonej wariacji przy silnej mierzalności oraz RNP dla dowolnej przestrzeni Hilberta i charakteryzację przez krzywe Lipschitza. W poprzednich przebiegach skontrolowano także operatory całkowania, twierdzenia graniczne, różniczkowanie i przestrzenie Sobolewa. Nie stwierdzono nowej koniecznej poprawki w kontrolowanym zakresie.

Wykonano 416 dodatkowych kontroli: 385 dokładnych równości ortogonalności Rademachera na podziałach diadycznych (poziomy 1–10), 24 dokładne całkowitoliczbowe kontrole norm kwadratowych bloków przykładu Fubiniego i 7 numerycznych kontroli nierówności wariacji współrzędnych dla skończonej miary w R^3. Wszystkie zaliczone; nie zastępują dowodów.

## Integralność i CI
5956 wierszy, 118 unikatowych etykiet, 20 podsekcji, 21 definicji. Zachowane wszystkie 83 etykiety pierwszej iteracji reorganizacji. Zero duplikatów, nierozwiązanych lokalnych odsyłaczy i niezgodności stosu środowisk. Zweryfikowano 8 odsyłaczy między rozdziałami AF i 12 odsyłaczy do ME/AM II.
- Moduł 15B: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46129213799 — PASS, 9/9 etapów joba 140930484554.
- Pełny AF: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46129213841 — PASS.
- Artefakt PDF: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46129213799/artifacts/15256957951.

Nie wykonywano nowych oględzin wizualnych stron PDF. Źródło pozostawiono niezmienione. Cykl stabilizacyjny i kontrolny reorganizacji zakończony w sprawdzonym zakresie, bez deklarowania formalnej weryfikacji wszystkich dowodów. Nie uruchamiano ręcznie dodatkowych workflow ani automatyzacji.
