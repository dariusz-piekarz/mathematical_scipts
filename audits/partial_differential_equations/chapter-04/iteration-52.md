# PDE-04 — iteracja 52: niezależny audyt stabilizacyjny, sekcje 4.1–4.3

Data: 2026-11-24. Źródło: chapters/pl/partial_differential_equations/04-rownanie-ciepla.tex, blob abd8dc9eca604f7105a6649cfd961547ef7968c5. Rejestr kryteriów: blob 18e4fb12dba0c352b9bc00e238badd5a919a54f3.

## Ponowna lektura matematyczna

- Wprowadzenie i 4.1 (001–003): wymiary i klasy danych; znaki i współczynniki pochodnej czasowej oraz laplasjanu; normalizacja jednowymiarowej całki Gaussa przez Tonellego i współrzędne biegunowe, zmiana zmiennych w n wymiarach, skalowanie. Równanie dla profilu samopodobnego wynika z reguły łańcuchowej; warunek zaniku pola jest tylko wystarczający, zgodnie z tekstem.
- 4.2 (004–007): dopełnienie kwadratu z przesunięciem s/(s+t) i a=st/(s+t); stała splotu. Bezwzględna zbieżność splotu dla p=1 i p=infty przez Höldera i dla pośrednich p; reprezentanci; ogon Gaussa i zbieżność zdominowana; gęstość i izometria przesunięć, kontrakcja i przybliżona jedność. Tonelli dla modułu daje skończoność podwójnej całki i Fubini bez założenia nieujemności danych. Niezmienniczość BUC i ciągłość z obu stron na podstawie kontrakcji. Przykład półprzestrzeni daje dolne oszacowanie istotnego supremum co najmniej 1/2 dzięki dodatniej mierze półkuli, a nie samej wartości w zerze.
- 4.3 (008–011): indukcja dla mieszanych pochodnych jądra, wspólna całkowalna majoranta na prostokącie z a>0; znak nierówności wykładniczej po zastąpieniu t przez b jest poprawny. Twierdzenie o wartości średniej i zbieżność zdominowana uzasadniają wszystkie pochodne. Ciągłość łączna przy t=0 z ciągłości normowej i przestrzennej; jednoznaczność odłożona do niezależnego dowodu w 4.4. Ścisła dodatniość dzięki dodatniemu minimum jądra na domkniętej kuli i dodatniej mierze. Zachowanie całki z danych ze znakiem przez Tonellego i Fubiniego, równość normy L¹ dla nieujemnych danych, kontrakcja ogólnie. Ponownie przeliczono (4 pi kappa t)^(-n)(2 pi kappa t)^(n/2)=(8 pi kappa t)^(-n/2) i sprawdzono wykładnik normy L².

W ponownie przeczytanych sekcjach nie znaleziono nowej istotnej luki matematycznej. Nie modyfikowano źródła ani kryteriów. Audyt nie obejmuje jeszcze ponownej lektury 4.4–4.10. Kryterium wizualne 037 opiera się na kontroli z iteracji 51; nie powtórzono oględzin PDF w tej iteracji.

## Kontrola techniczna

Przebieg 45486214130 (commit aa8c7b82bf7ea4e1475c39971c629ba2f0da16da), job 138772180199: wszystkie kroki success, w tym testy wykonywalne, kontrola struktury, izolowana kompilacja i render. Porównano wszystkie dziewięć wejść (źródło rozdziału 04 i 03, rejestr, test_heat.py, workflow, księga, manifest, listings, preambuła Atlasu) z blobami w tym commicie: 9/9 identycznych. Ponownie sprawdzono 45 unikatowych etykiet, 44 wystąpienia odsyłaczy, jedyny zewnętrzny cel eq:pde3-green1 występujący dokładnie raz w rozdziale 03, zagnieżdżenie środowisk oraz 37 kolejnych ID z istniejącymi kotwicami. Testy 9/9 na podstawie zakończonego kroku CI; nie powtarzano ich lokalnie. Brak wykonania Lean i kompilacji całego tomu.

Status: 3/10 sekcji ponownie przeczytanych, jeden audyt stabilizacyjny w toku. Następny zakres: 4.4–4.6 (maksimum, wygładzanie, generator, Duhamel). Rozdział pozostaje otwarty.
