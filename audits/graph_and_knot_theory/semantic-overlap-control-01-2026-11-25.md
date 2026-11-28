# Kontrola powtórzeń merytorycznych — iteracja 1

Stan porównania: 2cf5b53151e8baa31a619f28520244cc43f004f2.

Zakres: TG-02, 04, 06, 08, 37, 39, 40, 43. Porównano 28 par przez zbiory okien 18 słów po odfiltrowaniu komentarzy, poleceń LaTeX, listingów i TikZ; nie znaleziono wspólnych okien. Ręcznie porównano nagłówki twierdzeń i definicji oraz wybrane fragmenty dowodów. Brak wspólnych okien nie dowodzi braku powtórzeń semantycznych.

- TG-02/04: usunięto powtórzoną definicję przekroju krawędziowego, dodano odsyłacz do def:tg-tree-edge-cut; zachowano odrębną definicję separatora.
- TG-02/37: oznaczono podstawowe twierdzenie BFS jako thm:tg-tree-bfs-distance i powiązano z uogólnieniem na grafy niespójne; zachowano oba dowody ze względu na różne metody i zakres.
- TG-02/39, TG-04/40, TG-08/43: zachowano wyniki o różnych zakresach i zastosowaniach (optymalizacja, przepustowości rzeczywiste, normalizacja Laplasjanu).

Kontrola zmienionych trzech plików przy SHA 6ad68d3e43edf42a0df5fa10d74e517f330e97bb: 57 różnych etykiet, 0 powtórzeń, 0 błędów zagnieżdżenia; oba nowe cele odsyłaczy istnieją i każdy ma jedno wystąpienie odsyłacza w sprawdzanych plikach. Jedna definicja zatytułowana Przekrój krawędziowy w tej trójce. Zachowano istniejące etykiety.

Nie wykonano pełnego --strict, CI, kompilacji PDF ani całościowego audytu semantycznego 44 rozdziałów. Dalsza kontrola: grafy planarne i dualność, przestrzenie cykli i homologia, grafy Taita i wielomian Tutte'a.
