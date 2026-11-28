# PDE-02 — raport zamykający (iteracja 27, 2026-11-24)

Status: USTABILIZOWANY w zakresie rozdziału 02.

Źródło: `chapters/pl/partial_differential_equations/02-charakterystyki-i-pde-pierwszego-rzedu.tex`, blob cede0206acd0e122be62c5bd6af78df97fcf8eeb. Rejestr regresji: blob bebcd9d5e4461c3c6661679eb27f7e461d469e4d.

- Po ostatniej zmianie notacji (iteracja 25) wykonano dwa niezależne przebiegi bez zmian źródła: iteracja 26 (raport iteration-26.md) i 27. W drugim ponownie przejrzano argumenty konstrukcji quasiliniowej, odwracalności charakterystyk i osobliwości gradientu, Rankine'a–Hugoniota, śladu początkowego oraz niejednoznaczności słabych rozwiązań; nie wykryto nowych usterek.
- 33 trwałe kryteria (semantyczne, tekstowe i wizualne), ciągłość ID i istniejące kotwice; 51 unikatowych etykiet, 62 odsyłacze, jeden zewnętrzny cel chap:pde-code sprawdzony w CI; poprawne zagnieżdżenie środowisk; brak starego wzorca notacji całek.
- Aktualny blob źródła jest identyczny z blobem w commicie e7be79442c3d00c5040dad6ee2c904962a2a92dd, dla którego przebieg 45428593690 zakończył się success. W iteracji 27 ponownie pobrano status wszystkich kroków: testy wykonywalne (6/6), struktura, kompilacja, diagnostyka, renderowanie, publikacja artefaktu — success. Nie jest to nowe wykonanie testów.
- Artefakt 14937601427, 16 stron, obejrzany w iteracji 26; oba diagramy i ich podpisy na wspólnych stronach, bez zauważonych kolizji. Nie wykonywano ponownych oględzin w iteracji 27, ponieważ blob pozostał identyczny.
- Testy obliczeniowe sprawdzają wybrane przypadki, nie zastępują dowodów. Lean nie uruchomiono. Kompilacja dotyczy pojedynczego rozdziału z kanoniczną preambułą, nie całej książki; zewnętrzny odsyłacz nie ma w tym PDF działającego hiperłącza do rozdziału 33.
- Nie pozostawiono otwartych istotnych usterek w przyjętym zakresie. Dalsze zmiany źródła wymagają ponownego audytu i regresji.

Następny rozdział: 03 — Równania Laplace'a i Poissona. Stabilizacja 2/33.
