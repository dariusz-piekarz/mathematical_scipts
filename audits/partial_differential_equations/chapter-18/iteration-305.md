# RRC 18 — iteracja 305: skalowanie, rozdzielanie Dirichleta–Neumanna, prawo Weyla

Commit źródła: b8a4cc52633b61443af9e20b8da9d7328961f7ce.

- Domknięto sekcję 18.3: hipotezy porównania form, przedłużenie zerowe, widmo odcinka i prostokąta wraz z normalizacją i zupełnością, skalowanie przez izomorfizm izometryczny oraz gęstość.
- W sekcji 18.4 określono funkcję zliczającą dla widma ograniczonego z dołu i dążącego do nieskończoności.
- Wyprowadzono widmo sześcianu dla obu warunków brzegowych z produktów jednowymiarowych układów, wraz z uwzględnieniem krotności.
- Zastąpiono skrót geometryczny zliczania punktów kratowych jawnymi zawieraniami ortantów i półotwartych kostek, oszacowano indeksy zerowe i przypadek d=1.
- Uściślono identyfikację L^2 wielościanu z sumą prostą i trzy dziedziny formowe, zwartość i min–max w przypadku Neumanna oraz kierunki nierówności wartości własnych i funkcji zliczających.
- Uzasadniono przybliżenie obszaru siatką, niepustość dla małego h, zawieranie przy punktach na siatce oraz kontrolę objętości przez otoczenie brzegu.
- Rozpisano oba kierunki równoważności asymptotyki Weyla z uwzględnieniem skoków funkcji zliczającej.

Kontrola źródła: 930 wierszy (wcześniej 790), 42 zachowane unikatowe etykiety, 35 wystąpień odsyłaczy, te same trzy zewnętrzne cele co w 304, poprawne zagnieżdżenie środowisk. Brak dedykowanej kompilacji rozdziału 18; API przy sprawdzeniu nie zwróciło jeszcze przebiegów dla commitu.

Rozdział 17: końcowy run 45981760560 na commicie 1e1d05962bb4ec05d81c0769458ced501d18bd84 zakończony SUCCESS, job 140447146871, wszystkie kroki zaliczone, artefakt 15189778591 (3679006 bajtów). Potwierdza techniczny wynik po korekcie językowej. Odbiór wizualny 11 stron udokumentowany w 302 dotyczył wersji przed dwiema korektami; nowego artefaktu w tej iteracji nie oglądano. Globalne CI niezweryfikowane. Rozdział 17 pozostawiono bez zmian.

Następny etap: Li–Yau, kontrola argumentu Fouriera i optymalizacji momentu, następnie pierwsza wartość własna i Neumann; po pełnej lekturze rozdziału 18 audyty stabilizacyjne i dedykowany odbiór techniczny.
