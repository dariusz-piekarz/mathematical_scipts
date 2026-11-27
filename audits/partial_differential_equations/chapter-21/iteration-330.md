# RRC 21 — iteracja 330

Commit źródła 639721a1281bdbe96598622c2ed4f6cb30918adf, blob 7103160ebfe3a46b16d949a6b17b97beb7e925c1. Pierwszy audyt szczegółowy sekcji 21.3–21.4.

- Uzasadniono mierzalność supremum prędkości symbolu przez przeliczalny gęsty podzbiór sfery, interpretację spektralną i punktowe ograniczenie dla współczynników ciągłych (także na końcach przedziału czasu).
- Wyprowadzono wzór transportu Reynoldsa dla ruchomej kuli przez zmianę zmiennych i twierdzenie Gaussa, z uwagą o d=1. Rozpisano pełny bilans strumienia, jego znak, argument z czynnikiem całkującym i przejście od zerowej energii do punktowego zerowania, również na brzegu. Sprawdzono przypadki R=0, c>0 i c=0. Dodano wniosek o lokalnej zależności od danych i propagacji nośnika dla jednorodnego równania; przy kontroli stabilizacyjnej doprecyzować zapis zamkniętej kuli o promieniu zero jako singleton (nie domknięcie pustej kuli otwartej).
- Uzupełniono rysunek stożka o odległości ct_0 i linie pomocnicze. Nie sprawdzono renderowania.
- Wyprowadzono układ pierwszego rzędu dla równania falowego, obliczono wektory własne, wykazano odwrotną konstrukcję rozwiązania przy zgodnych danych początkowych i jednoznaczność z dokładnością do stałej przy zadanych pochodnych. Rozpisano charakterystyki obu modów i odzyskanie formuły d'Alemberta.
- Kontrola zapisanego źródła: 880 wierszy (737 wcześniej), 23 zachowane unikatowe etykiety, 45 wystąpień odsyłaczy, dwa różne cele zewnętrzne w rozdziałach 5 i 20, brak brakujących lub niejednoznacznych celów i błędów zagnieżdżenia środowisk oraz delimiterów. Brak potwierdzonej kompilacji rozdziału 21.
- CI rozdziału 19 (45989522023) przy ponownym odczycie in_progress; rozdział 20 (45994503573) przy pierwszym odczycie queued. Odbiór techniczny obu nadal otwarty.

Postęp pierwszego audytu: 4/10 sekcji. Następny etap: oszacowania komutatorów i energii H^s, w tym pełna kontrola lematu Friedricha o przedłużeniu tożsamości energii na rozwiązania słabe. Szczególnie sprawdzić identyfikację normy w każdej chwili, nie tylko prawie wszędzie.
