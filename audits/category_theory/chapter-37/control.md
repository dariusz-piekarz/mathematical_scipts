# CAT-37 — audyt kontrolny

Weryfikowany blob rozdziału: `9fcb018a2db6f5cc31296b966e1f7596e2e0457a`.
Testy regresyjne: commit `113788b99c5ddfb04281a1a60ee85c83952a6885`.

- Sprawdzono etykiety wszystkich 38 plików rozdziałów CAT-00–CAT-37 (186 + 653 = 839 wystąpień). Wszystkie 36 etykiet CAT-37 oraz wszystkie 18 różnych celów jego odsyłaczy mają dokładnie jedno wystąpienie w zbiorze rozdziałów.
- 22 środowiska proof. Poprzednie kontrole struktury i integracji książki oraz katalogu pozostają aktualne dla tego samego blobu.
- W poprzedniej iteracji niezależne obliczenia skończone dały 2128/2128 przypadków permutacji blokowych, 1111/1111 wewnętrznych oraz 47668/47668 zgodności ze składaniem. Są to kontrole pomocnicze, nie formalne dowody ani wynik wykonania pełnej suity Pythona.
- Kontrola ostatnich poprawek (monada operady symetrycznej, przeszkoda dla morfizmu As -> E1, etykietowane drzewa Liego, operada liniowa zerowa): nie wykryto nowej usterki.
- CI: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46055118274 — status queued, job validate 140695612661 bez wykonanych kroków w chwili kontroli.

Status: część matematyczna i odsyłacze kontrolnie sprawdzone; odbiór końcowy WSTRZYMANY do rzeczywistego sukcesu CI, kompilacji PDF i kontroli wizualnej trzech diagramów. Nie deklarujemy zamknięcia rozdziału ani wykonania testów Python.

## Uzupełnienie — niezależna kontrola diagramów

Trzy środowiska TikZ z blobu `9fcb018a2db6f5cc31296b966e1f7596e2e0457a` skompilowano bez zmian w lokalnym dokumencie `article` (11 pt, A4, pakiety amsmath i tikz, biblioteki arrows.meta i babel), poleceniem `pdflatex -halt-on-error -interaction=nonstopmode`. Wynik: 1 strona, brak ostrzeżeń i błędów w logu. Render Poppler 150 dpi sprawdzono wizualnie: podstawienie operacji o arności 6, dwa drzewa binarne oraz podstawienie małych prostokątów są czytelne i nie nachodzą na siebie. Nie jest to kompilacja pełnego skryptu ani kontrola renderera aplikacji. CI #46055118274 nadal queued. Odbiór pełnego PDF pozostaje otwarty.

## Uzupełnienie — lokalne wykonanie testów matematycznych

W kontenerze uruchomiono odtworzoną z kodu testowego w commicie `113788b99c5ddfb04281a1a60ee85c83952a6885` kopię czterech metod unittest (001, 002, 003, 005) z tymi samymi funkcjami pomocniczymi i asercjami. Wynik: 4/4 OK (0,282 s). Piąty test struktury 004 wymaga pełnego drzewa repozytorium i nie został lokalnie wykonany jako unittest; odpowiadające mu kontrole struktury i etykiet wykonano wcześniej na plikach pobranych z GitHub. Próba pobrania repozytorium przez git z kontenera zakończyła się błędem DNS (Could not resolve host: github.com). Nie jest to wynik pełnej suity CI. Run #46055118274 nadal queued. Odbiór pełnego PDF i pełnego CI pozostaje otwarty.

## Odbiór CI

Run `46055118274`, head `113788b99c5ddfb04281a1a60ee85c83952a6885`, zakończył się SUCCESS. Job validate `140695612661`: testy regresyjne, kompilacja pełnej książki, weryfikacja PDF i odsyłaczy oraz upload artefaktu — wszystkie kroki SUCCESS. Kontrole matematyczne, strukturalne i samodzielna kompilacja diagramów zostały wcześniej zaliczone. Pozostaje wizualna kontrola rozmieszczenia diagramów w pełnym PDF (nie utożsamiamy jej z samodzielną kompilacją TikZ).

## Odbiór wizualny — zamknięcie

W pełnym PDF z zaliczonego przebiegu CAT-38 #46058308185 (artefakt 15227114544, 343 strony) potwierdzono identyczny blob CAT-37 `9fcb018a2db6f5cc31296b966e1f7596e2e0457a`. Wyrenderowano i obejrzano trzy diagramy na stronach 310, 312 i 325: poprawne rozmieszczenie, bez obcięcia i kolizji. Wcześniejszy dedykowany przebieg CI #46055118274 również SUCCESS. CAT-37 ZAMKNIĘTY. Ostrzeżenia hyperref dotyczące zakładki matematycznego tytułu pozostają nieblokujące.
