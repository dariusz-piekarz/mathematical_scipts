# AA-61 — audyt V: diagnostyka i korekta składu

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.

Run 45386429026, head 6f2a71396dd9040cf36ae0c80475091d32e5b42d, job 138418420049: 128 success, 1 failure, 2 skipped. Globalne testy repozytorium, bramka AA, pierwszy zestaw AA-61 oraz latexmk zaliczone. Kompilacja dała 394-stronicowy PDF (artefakt 14917276128), ale kontrola końcowego logu wykryła Overfull hbox. Z logu końcowego przebiegu: cztery wystąpienia 9.35445pt podczas składania nagłówka rozdziału 61 oraz jedno 4.75958pt w akapicie linii 102–103 (wzór na a_ij). Nie uznano PDF za zatwierdzony.

W commicie 3c2584be2ebb7256b6e22123822c2a388d7da8a5 skrócono wyłącznie tytuł używany w nagłówkach i spisie treści, zachowując pełny tytuł rozdziału; wzór na a_ij przeniesiono do osobnego równania i dodano odsyłacz do realizacji euklidesowej z AA-60. Blob 76c35df11718f562aa5a6cf121c7e0d4fdb9dcc0. Równanie matematycznie identyczne z poprzednim. Czyste audyty matematyczne III–IV: 2/2; korekta typograficzna nie zmienia ich treści. Oba zestawy regresji wcześniej zaliczone bezpośrednio. Pełny nowy CI 45387901864 w kolejce przy kontroli; wynik i oględziny nowego PDF niepotwierdzone. Nie zmieniono bramki jakości ani innych skryptów. AA-61 W AUDYCIE TECHNICZNYM; AA-62 nieotwarty.
