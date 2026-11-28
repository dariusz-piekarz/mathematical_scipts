# CAT-14 — niezależny audyt kontrolny IV

Ponownie przeczytano całe źródło rozdziału (blob a4c89d1f02e067d7603f10e54baea680d214a6b7). Sprawdzono typy morfizmów, naturalność w obu zmiennych, przykłady wolne i topologiczne, oba trójkąty i odwrotności transpozycji, dowody zachowania granic i kogranic, pełną wierność i kontrprzykłady. Brak nowych istotnych błędów i luk w głównych dowodach. Źródło i testy (blob 35601408400968c3e839b9da8f0e7f68795dca41) niezmienione od zweryfikowanej wersji.

Niezależna kontrola JS: wszystkie pary funkcji f,g:X->Y na oznakowanych zbiorach o licznościach 0–3 i zbiór A o liczności 0–3. 3640 modeli koequalizatora zachowywanego przez iloczyn z A; porównano relacje ilorazowe na 108136 parach. 3640 modeli equalizatora zachowywanego przez funktor (-)^A; sprawdzono 33290 kandydatów na funkcje i równość zbiorów funkcji. Brak niezgodności. Są to kontrole modeli, nie dowody ogólne i nie nowy przebieg testów Python.

Potwierdzono CI #45621733546, job 139231369980 SUCCESS (102/102 testów, 6/6 CAT-14, pełna kompilacja i odsyłacze). Wykorzystano rzeczywistą kontrolę wizualną artefaktu 15026205884, PDF 65 stron, strony 56–61 z iteracji III. Nie wykonywano nowej kompilacji ani renderowania w IV; Lean nie uruchamiano. Nie weryfikowano globalnego CI aplikacji.

Wynik: CAT-14 stabilny i zamknięty w zakresie aktualnego materiału skryptu. Kolejny etap CAT-15 — monady.
