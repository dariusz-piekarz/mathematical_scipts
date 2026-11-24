# Moduł 15B — audyt 09 (poprawkowy)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: raport 08 (450e3e3d80109426871bbb57f15dc615f14028a7), HEAD 0adfd0d7973e5fb5cd3f65b6918883cd5916f5f1, źródło 6dc01e9a784f62bc794614ee88c69e33a91bef66. Ponownie odczytano całe źródło, raport i plik testów.

## Kontrola
- Uściślono konwencję klas równoważności L1 i podano wzór zanurzenia kanonicznego. Całka Riemanna dotyczy konkretnych funkcji.
- Wszystkie sześć definicji ma jawne określenie przestrzeni i ciała skalarów. W definicji Bochnera podano niezależność całki funkcji prostej od przedstawienia przez wspólne rozdrobnienie; określono notację i normę L1. Dowód kryterium zawiera teraz oszacowanie Cauchy'ego, niezależność od aproksymacji, ograniczenie do A, liniowość i przejście do granicy.
- Twierdzenie Pettisa o mierzalności, DCT Bochnera, Fubini oraz kontrprzykład Riemanna: sprawdzono założenia i konstrukcje z poprzednich audytów; bez dalszych zmian.
- Dunford: zdefiniowano całkowalność i odnotowano, że istnienie funkcjonału wynika z następnego twierdzenia. Pettis: dopisano jednoznaczność z Hahna–Banacha oraz uzasadnienie liniowości użytej w dowodzie zbieżności. Przykłady c0 i nieośrodkowej przestrzeni Hilberta zachowano.
- Gelfand: jawne dane definicji i odesłanie do twierdzenia o istnieniu. Dowód domkniętego wykresu i przykład braku addytywności normowej bez zmian.
- Wariacja: dopisano dowód oszacowania różnicy wariacji przez całkę normy różnicy gęstości. Definicja RNP: jawna bezwzględna ciągłość i uzasadnienie równoważności przy ograniczeniu do miar zupełnych. Rozszerzenie miary wektorowej przez przedstawicieli mierzalnych, rozłącznienie przedstawicieli i konstrukcja silnie mierzalnego przedstawiciela gęstości. Kontrprzykład C([0,1]) zachowany.
- Nie rozszerzano zakresu tematycznego; doprecyzowania dotyczą istniejących definicji i argumentów.

## Kontrola techniczna
Commity źródła e80c59996f4a465da83143c680f9aa8e74369327 i f1abe0d11842e4f2fd6b916b5e98c97906da9b3b. Ponowny odczyt: blob 451e23a40f3c6e3f6596d173547866f3bf31f025, 753 wiersze, 23 zachowane unikalne etykiety, 11 dowodów, poprawne zagnieżdżenie środowisk. Sprawdzono 6/6 definicji pod kątem jawnego określenia ciała oraz 8 nowych kontraktów tekstowych.
Dodano dziesiąty test regresyjny (commit bbde58121b5d4dc96cf527c92c2d27f9c4f9344c, blob 7a1e527da205ca939d305b421d2b85e07ad936cf).
Nie uruchomiono pełnego unittest ani kompilacji LaTeX i nie wykonano oględzin PDF. Lista przebiegów PR dla raportu 08 była pusta, co nie rozstrzyga statusu CI. Nie zaliczać kontroli technicznej jako wykonanej.

## Decyzja
15B/09: poprawkowy, 0/2. Następny krok: niezależny audyt 10, szczególnie sprawdzenie nowych fragmentów RNP i Bochnera, pełne regresje, kompilacja oraz oględziny PDF. Rozdział 16 pozostaje zablokowany.
