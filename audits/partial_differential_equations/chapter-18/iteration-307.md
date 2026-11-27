# RRC 18 — iteracja 307: ślad cieplny, przejście abelowe, perturbacje

Commit źródła: d6afeb748885cf2292b0d8000183b8966676f87f.

- Rozpisano konstrukcję diagonalną półgrupy cieplnej, zwartość i kryterium klasy śladowej przez sumę wartości singularnych. Zbieżność szeregu uzasadniono przez Tonellego i oszacowanie Li–Yau; sama własność klasy śladowej nie wymaga założenia o mierze brzegu.
- Wyprowadzono całkowalną majorantę dla przejścia granicznego, normalizację objętości kuli z całki Gaussa oraz jawne wzory odzyskiwania wymiaru i objętości z widma.
- Uzupełniono argument abelowy z kontrolą reszty i doprecyzowano, czego nie daje samo prawo Weyla.
- Rozpisano dwustronne porównanie min–max dla potencjałów.
- Doprecyzowano wspólną dziedzinę perturbowanych operatorów, normę grafową oraz dowód samosprzężoności przez definicję sprzężenia. Rozpisano różniczkowanie równania własnego i redukcję składników z pochodną wektora własnego.
- Dodano przykład przecięcia gałęzi w wymiarze dwa, pokazujący brak różniczkowalności uporządkowanych wartości własnych; nie deklarujemy twierdzenia o istnieniu różniczkowalnych gałęzi.

Kontrola źródła: 1133 wiersze (wcześniej 1031), 42 zachowane unikatowe etykiety, 51 wystąpień odsyłaczy. Wszystkie cele istnieją jednoznacznie w rozdziale i rozdziałach 7, 9, 10, 12, 14, 20 w commicie 89461b527c2c2c1816893ee243219bac9003b14d; brak błędów zagnieżdżenia środowisk.

Dedykowany workflow .github/workflows/partial-differential-equations-ch18.yml dodano w commicie 89461b527c2c2c1816893ee243219bac9003b14d na podstawie workflow 17. Kontroluje etykiety, manifest, preambuły, kompilację rozdziałów zależnych i rzeczywiste numery odsyłaczy, kompilację rozdziału 18, log i renderowanie stron. Run 45984455701 w kolejce przy ostatnim odczycie. Nie potwierdzono kompilacji ani odbioru wizualnego PDF.

Pierwsza szczegółowa lektura objęła 10/10 sekcji. Następny etap: pełny audyt stabilizacyjny, ze szczególną kontrolą zgodności założeń, terminologii, odsyłaczy, kompletności argumentów i odbiór dedykowanego CI. Rozdział pozostaje nieustabilizowany.
