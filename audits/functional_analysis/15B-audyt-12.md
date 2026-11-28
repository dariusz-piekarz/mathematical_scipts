# Moduł 15B — audyt 12

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: raport 11 aec7939f94954cbc1944252db6163ebac1b4a0e4, HEAD e5639454ab1a921e6dda78437cec35d2a0c5fb04. Źródło 3e92f702d7e024b2f7da636afa46d20a23dba764, testy 8e8cd36ed36a1327411f9a51f07a01b788b9c4a9: identyczne z audytem 11. Porównanie commitów wykazuje wyłącznie zmiany dotyczące algebry abstrakcyjnej. 793 wiersze, 23 unikalne etykiety, 6 definicji, 11 twierdzeń i stwierdzeń, 11 dowodów, cztery środowiska przykładów. Zagnieżdżenie środowisk poprawne; we wszystkich 17 definicjach i twierdzeniach jawnie określono ciało skalarów.

## Kontrola matematyczna
- Pettis: rodzina normująca z gęstej sfery, modyfikacja na zbiorze zerowym i Borel–Cantelli poprawne.
- Bochner: wspólne rozdrobnienie podziałów, niezależność aproksymacji, liniowość, przycięcie, przejście przez operator i dominacja poprawne przy skończonej zupełnej mierze.
- Fubini: produktowo mierzalny zbiór Cauchy'ego i przedstawiciel, aproksymacja prostokątami, sumowalność błędów przekrojów oraz obie całki iterowane uzasadnione. Riemann: kontrprzykład dotyczy konkretnego przedstawiciela.
- Dunford i Gelfand: wykresy domknięte, identyfikacje przestrzeni sprzężonych, całkowalność skalarna, addytywność słaba-* oraz kontrprzykłady poprawne.
- Pettis: symetryczny przykład c0, reprezentacja na wszystkich zbiorach i kontrprzykład w nieośrodkowej przestrzeni Hilberta poprawne. Zbieżność normowa całek wynika z dominacji mierzalnej normy różnicy.
- Wariacja: sumowanie po podziałach i nierówność Lipschitza względem normy L1 poprawne.
- RNP: rozłącznienie przedstawicieli zachowuje klasy modulo zbiorów zerowych; norma wariacji nie wzrasta po uzupełnieniu, a ograniczenie daje przeciwną nierówność. Mierzalna gęstość ma przedstawiciela punktowo aproksymowanego funkcjami prostymi. Kontrprzykład C([0,1]) poprawny.
- Brak koniecznych korekt, nie zmieniano źródła ani testów.

## Technika
Poprzednie CI 45346197303 zakończone sukcesem, oględziny PDF opisane w audycie 11 dotyczą identycznego źródła. Ponowny przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45347641128 dla commitu raportu 11: completed/success; wszystkie kroki zakończone sukcesem. Nie wykonano nowych niezależnych oględzin PDF w tej iteracji.

## Propozycje opcjonalne (globalna zasada AGENTS.md)
- Po przykładzie w nieośrodkowej przestrzeni Hilberta: przykład silnie mierzalnej funkcji Pettisa niebędącej całkowalną w sensie Bochnera w ośrodkowej l2. Dla mas atomów 2^(-n) i f(n)=2^n e_n/n: całkowalność skalarna z Cauchy'ego–Schwarza, całki Pettisa po A reprezentuje ciąg chi_A(n)/n w l2, a całka normy to rozbieżny szereg harmoniczny. Pokazuje różnicę niezależną od braku silnej mierzalności.
- Diagram implikacji Bochner => Pettis => Dunford, z odsyłaczami do kontrprzykładów odwrotnych; Gelfanda pokazać oddzielnie, z przestrzenią predualną jako elementem danych.
- Po definicji RNP: pozytywny przykład skończenie wymiarowy z twierdzenia skalarnego Radona–Nikodyma; twierdzenie dla przestrzeni refleksywnych jako opcjonalny dalszy wynik z pełnym dowodem.
Nie dodano materiału bez akceptacji. Propozycje nie resetują stabilizacji.

## Decyzja
Drugi czysty audyt matematyczny (2/2); ponowny CI zaliczony, wcześniejszy PDF dotyczy identycznego źródła. Stabilizacja zamknięta, następna iteracja rozdział 16.
