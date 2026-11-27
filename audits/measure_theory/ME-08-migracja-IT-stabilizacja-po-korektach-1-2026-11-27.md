# ME-08 — pierwszy czysty przebieg po korektach 3adacb4

27.11.2026. Blob rozdziału f3b6b0a687891c507585dabd9738ef8acad83c7b, 1183 wiersze. Ponownie odczytano pięć zmienionych deklaracji z dowodami.

- Addytywność: aproksymacje proste rosną punktowo; skończona addytywność prostych funkcji wynika z ME-07 (thm:simple-properties), następnie Beppo Levi. Nie wymaga skończoności miary.
- Całka zespolona: części rzeczywista i urojona są mierzalne przez ciągłość rzutów i całkowalne przez oszacowanie modułem. Rozwinięcie iloczynu przez skalar i addytywność dają liniowość, obrót fazy daje oszacowanie modułu.
- Wzór warstwowy dla p>0: a=0 daje całkę po zbiorze pustym; dla a>0 obliczenie na przedziale odciętym oraz Beppo Levi. Końce mają miarę zero; przy nieskończonej masie poziomicy dodatni czynnik jest skończony, a iloczyn na części zerowej interpretuje się zgodnie z konwencją całki nieujemnej. Nie użyto Tonellego. Sprawdzono późniejsze twierdzenie o zgodności Riemanna i Lebesgue'a: nie korzysta ze wzoru warstwowego, więc ten odsyłacz w przód nie tworzy cyklu.
- Zgodność całek: granica górna ograniczonych funkcji prostych daje mierzalnego reprezentanta na całym przedziale; Borel–Cantelli i oszacowanie Darboux dają równość z funkcją poza mierzalnym zbiorem zerowym. Zupełność miary Lebesgue'a pozwala przenieść mierzalność na funkcję pierwotną. Całki ściskają dolne i górne sumy Darboux.

Kontrola strukturalna: 40/40 unikatowych etykiet, 27 dowodów, prawidłowy stos środowisk LaTeX; wszystkie 13 różnych celów ref/eqref poza rozdziałem znaleziono w ME-02, 04, 06, 07, oba różne cele atlasref w AM1-29. Brak nowych usterek wymagających edycji w ponownie odczytanych fragmentach. Źródło niezmienione.

CI dla 3adacb4: ME-08 #45990916338, globalny ME #45990916354 — queued przy odczycie. Brak potwierdzonego aktualnego PDF i pełnego wykonania testów. Następny krok: drugi niezależny przebieg, potem audyt kontrolny. Nie oznaczać technicznego odbioru jako zaliczonego.
