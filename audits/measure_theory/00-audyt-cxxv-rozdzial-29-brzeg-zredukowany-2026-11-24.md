# Audyt CXXV (125) — normalna miarowo-teoretyczna i brzeg zredukowany
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia 91e53ab02cc2542d52630d98507bf0efa4fe7b08, blob 6eaf7319ea314c6005accf19f1718f3f0966df5c. Commit źródłowy 5a27cf170f49d253ead0f2807e5241c7b2c61686, blob 153081cda6ffca637ad064884f1033554611c4a5.
## Wyniki
Dziewięć zastąpień; 2233 -> 2357 wierszy; wszystkie 37 dotychczasowych etykiet zachowane w kolejności.
- Uściślono hipotezy definicji, ujednolicono nazwę rozkład polarny, rozpisano sklejanie lokalnych pól polarnych na warstwach kul i jednoznaczność normalnej.
- Udowodniono borelowskość zbiorów punktów gęstości i brzegu miarowego nawet dla E mierzalnego jedynie w sensie Lebesgue'a: ciągłość średnich i przeliczalne kryterium promieni wymiernych. Jawnie wykazano równoważność prawie wszędzie E i E^(1), niezmienniczość względem zmiany E na zbiorze zerowym.
- Dodano pełne uzasadnienie własności używanych w dowodzie De Giorgiego: borelowskość brzegu zredukowanego, borelowskość punktowej normalnej, skupienie wariacji na brzegu zredukowanym, zgodność normalnej z polem polarnym prawie wszędzie. Uzasadniono mierzalność funkcji kulowych, ciągłość od dołu w promieniu (nie zakładano ciągłości dwustronnej dla miary Radona), kryterium Cauchy'ego z wymiernymi promieniami i pełną miarę nośnika.
- Sprawdzono obecność etykiet thm:lebesgue-diff-25 i thm:relative-lebesgue-25 w rozdziale 25. Skupienie wariacji wynika z różniczkowania względem miary Radona, bez korzystania z twierdzenia strukturalnego; nie utożsamiono jeszcze wariacji z miarą Hausdorffa.
- W Gaussie–Greenie jawne uzasadnienie skończoności całek i możliwość ograniczenia całki do brzegu zredukowanego bez przedwczesnej zmiany miary.
## Otwarte
Następnie niezależna kontrola nierówności Sobolewa, względnej nierówności izoperymetrycznej, aproksymacji BV na kulach, a później kolejnych lematów twierdzenia De Giorgiego. Kompilacja, regresje i PDF pozostają do wykonania. Stan 28/31.
