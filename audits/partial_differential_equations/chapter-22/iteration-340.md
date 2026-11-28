# RRC 22 — iteracja 340

Pierwszy audyt szczegółowy sekcji 22.4 (postęp 4/8). Commit dc5105ba76a615270debaef51adc6cb6deac004e, blob 60c552d33fe83380194b066da2602333d4c01cb3.

- Rozpisano dowód samosprzężoności ograniczonej perturbacji rzeczywistej: odwrotność H_0 ± iaI odwzorowuje L² do H², faktoryzacja i szereg Neumanna, obie surjekcje i jądro operatora sprzężonego z poprawną konwencją iloczynu skalarnego. Dodano dolne ograniczenie hamiltonianu.
- Wyprowadzono z rachunku spektralnego unitarność, silną ciągłość, niezmienniczość dziedziny, komutację i różniczkowalność na dziedzinie. Udowodniono równoważność norm grafowych, regularność C_t H² i C¹_t L², jednoznaczność i zachowanie energii. Rozszerzono zachowanie energii na H¹ przez dodatnią formę przesuniętą, jej równoważność z kwadratem normy H¹ i aproksymację jednostajną w czasie.
- Lokalny bilans prawdopodobieństwa: reguła iloczynu L² × L² → L¹, aproksymacja H², przejście graniczne w czasoprzestrzeni, rozszerzenie na H¹ z oszacowaniami różnic gęstości i prądu oraz ciągłością w L¹.
- Potencjał zależny od czasu: wybrano wspólny zbiór pełnej miary czasowej, wykazano silną mierzalność działania operatorów na zmiennych wektorach, skonstruowano rozwiązanie obrazu oddziaływania przez kontrakcję na skończonym podziale czasu, uzasadniono równanie w H^{-2}, dokładny bilans kwadratu normy dla dowolnych końców i oszacowanie przez regularizację pierwiastka. Dodano dwuparametrową unitarną ewolucję (odwracalność przez rozwiązanie wstecz) oraz przykład potencjału a(t) pokazujący brak zachowania energii mimo zachowania normy.
- Ujednolicono miary całek. Nie rozszerzano twierdzeń na nieograniczone potencjały.

Kontrola źródła: 949 wierszy (680 wcześniej), 17 zachowanych unikatowych etykiet, 19 odsyłaczy, pięć różnych celów zewnętrznych w rozdziałach 8,18,20,21, wszystkie jednoznaczne; brak błędów zagnieżdżenia środowisk i delimiterów. Wszystkie pozostałe sekcje identyczne. Brak potwierdzonej kompilacji rozdziału 22. Runy 46001463968 (20) i 46001463740 (21) przy odczycie queued.

Następny etap: sekcja 22.5 — jądro swobodnego propagatora, gaussowska regularizacja z kontrolą gałęzi pierwiastka, interpolacja Riesza–Thorina oraz brak skończonej prędkości propagacji dla danych o zwartym nośniku.
