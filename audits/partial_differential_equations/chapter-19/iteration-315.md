# RRC 19 — iteracja 315: bariery, pojemność Newtonowska, kryterium Wienera

Commit źródła 30d415c82e3fef0d56fd0150f9c7b10dd3f5bcf0, blob ab4c4b39c253b81bbe072b2a7db4bd4e87612318.

Pierwsza szczegółowa lektura sekcji 19.8–19.9.
- Uściślono warunek oddzielenia bariery od zera; przy wielokrotnym styku zewnętrznej kuli z brzegiem zastosowano mniejszą kulę styczną wewnętrznie, której domknięcie przecina domknięcie obszaru tylko w wyróżnionym punkcie. Rozpisano dowód geometryczny i dodatnie minimum.
- Wprowadzono dowód skalowania, niezmienniczości translacyjnej i dokładnej pojemności Newtonowskiej kuli, wykorzystujący infimum po promieniach zewnętrznych. W porównaniu pojemności względnej i bezwzględnej rozpisano wykładniki Höldera i odsyłacz do Sobolewa.
- Rozpisano geometrię kuli wpisanej w pierścień i stożek, a w przykładzie nieskończonej rodziny kul uzasadniono spójność łukową przez skończoną rodzinę powiększonych kul i omijanie ich po sferach.
- Uzupełniono niezależny dowód Fourierowski usuwalności w wymiarze 2: różniczkowanie pod całką, całkowanie przez części, równanie Eulera i rozwinięcie jądra Poissona.
- Kryterium Wienera i twierdzenie o barierach Perrona pozostają jawnie przywołanymi wynikami, bez pełnego dowodu. W tej iteracji nie dodano zewnętrznej bibliografii; wskazanie dokładnego źródła należy do kontroli stabilizacyjnej.

Kontrola zapisanego źródła: 1202 wiersze (wcześniej 1102), 37 zachowanych unikatowych etykiet, 40 wystąpień odsyłaczy, wszystkie cele jednoznaczne w źródle i rozdziałach 7,9,10,14,18. Brak niezgodności begin/end.
Dodano dedykowany workflow rozdziału 19 w commicie 33228eba2c105ad1aa960e4004f35a9b66ad6b6d: kontrola etykiet, manifestu, rzeczywistych numerów odsyłaczy, kanonicznej preambuły, kompilacja i renderowanie. Stan przebiegów przy odczycie: [{"id":45988465898,"name":"Mathematical analysis II validation","status":"queued","conclusion":null},{"id":45988455742,"name":"PDE - chapter 19 audit","status":"queued","conclusion":null}].
Rozdział 18: końcowy run 45985977450: queued, null. Nie wykonano w tej iteracji odbioru wizualnego aktualnego PDF rozdziału 18.
Pierwsza lektura objęła 9/9 sekcji rozdziału 19. Następny etap: pełna stabilizacja, sprawdzenie twierdzeń przywołanych i ich źródeł, odbiór techniczny oraz kontrolny audyt. Nie deklaruje się stabilizacji ani kompilacji aktualnej wersji rozdziału 19.
