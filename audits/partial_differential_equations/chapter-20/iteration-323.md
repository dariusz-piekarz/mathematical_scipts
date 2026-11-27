# RRC 20 — iteracja 323

Commit źródła 592909dba1f528e3e7ce110ef6deb0ad0ca68e16, blob f44436d32f615ee5c339c05af482478e11e52e7b. Pierwszy audyt szczegółowy sekcji 20.7–20.8 oraz domknięcie odsyłaczy sekcji 20.5.

- Uściślono klasę regularności rozwiązania reakcji–dyfuzji w przestrzeni Hilberta, uzasadniono normalizację dodatniej pierwszej funkcji własnej, różniczkowanie funkcjonału F i wykorzystanie samosprzężoności operatora. Rozwiązano jawnie skalarne równanie przez podstawienie z=y^{1-p}, wyprowadzono dokładny czas eksplozji i dowód porównania przez część dodatnią. Rozróżniono górną granicę czasu istnienia od twierdzenia o istnieniu aż do tej granicy. Jeśli rozwiązanie istnieje aż do granicy, wykazano rozbieżność normy L^2.
- Zdefiniowano macierz różnicową laplasjanu i iloczyn skalarny siatki, wykazano dodatnią określoność przez sumowanie różnic, odwracalność każdego kroku i sumaryczną tożsamość energii. Dodano dowód zbieżności dla gładkiego rozwiązania jednowymiarowego z dokładnymi wartościami wymuszenia na siatce, defektem Taylora, kontrakcyjnością rezolwenty i błędem O(tau+h^2), bez warunku sprzęgającego kroki. Nie rozszerzono tego wniosku na ogólne współczynniki mierzalne.
- Uzupełniono odsyłacz do regularności brzegowej H^2 (thm:pde15-boundary; sprawdzono hipotezy), oba zawierania dziedzin operatora, zapis ciągłości V-wartościowej w tezie twierdzenia o wyższej regularności i lokalną notację we wzorze Duhamela. Zastąpiono ręczny numer rozdziału 4 odsyłaczem.

Kontrola źródła: 1091 wierszy (964 wcześniej), 23 zachowane unikatowe etykiety, 36 wystąpień odsyłaczy, 12 różnych celów zewnętrznych. Wszystkie cele jednoznaczne w źródle i rozdziałach 4,9,10,11,15,18, brak niezgodności begin/end.

Dedykowany workflow rozdziału 20 w commicie 3de76146609db99751d78d692f5a23ff79a15e25: sprawdzenie struktury, manifestu, preambuły, rzeczywistych numerów zewnętrznych odsyłaczy, kompilacja, diagnostyka i renderowanie. Wyzwalacz ograniczony do rozdziału 20, sześciu bezpośrednich rozdziałów zależnych i plików wspólnych (nie zmieniano pozostałych workflow). Stan przy odczycie: [{"id":45991021945,"status":"queued","conclusion":null}]. Brak potwierdzonej kompilacji i odbioru wizualnego. Cztery przebiegi rozdziału 19 przy pierwszym odczycie nadal queued; jego odbiór techniczny pozostaje otwarty.

Pierwsza szczegółowa lektura 8/8 sekcji zakończona. Następny etap: pierwszy pełny audyt stabilizacyjny, ze szczególną kontrolą nowych dowodów, notacji i hipotez. Nie deklaruje się stabilizacji rozdziału 20.
