# RRC 19 — iteracja 313: pojemność punktu i usuwalność

Commit źródła 3ccbe13c580691e088a7e672699023c252f77727, blob 6224701e2df75b06f9d1b3951795f98a23292e9b.
Domknięto pojemność punktu w sekcji 19.3 i przeprowadzono pierwszą szczegółową lekturę 19.4–19.5 (kontrprzykład odczytano, jego normalizacja pozostaje do kontroli w następnej iteracji).

- Uzasadniono niezmienniczość pojemności względem translacji, dodatnią dolną granicę w d=1 przez absolutną ciągłość i ślad na końcu składowej.
- Doprecyzowano definicję pojemności p-energetycznej dla zbiorów zwartych, otoczenie dopuszczalności i zbiór pusty.
- Dla p<d rozpisano dopuszczalność, skalowanie gradientu i zmianę zmiennych; dla p=d>1 podano jawny profil logarytmiczny i wykazano jego przynależność do W_0^{1,d}.
- Dla p>d (d>=2) zastosowano globalną nierówność Morreya do przedłużenia zerowego i punktu poza domknięciem obszaru. Dla d=1 uwzględniono również p=1. Zweryfikowano dokładne hipotezy twierdzenia Morreya w rozdziale 10.
- Wzmocniono twierdzenie o usuwalności: wystarcza u w H^1(Omega\K), bez apriorycznej przynależności do H^1(Omega). Przedłużenia u i słabych pochodnych przez zero na zbiór miary zero są w L^2; testy z odcięciem i trzy jawne oszacowania dowodzą tożsamości słabych pochodnych, a następnie równania na całym zbiorze. Nie potrzeba symetrii ani eliptyczności A.
- Dowód równości przestrzeni H_0^1 uniezależniono od hipotez dotyczących równania, uzasadniono domkniętość obrazu izometrycznego zanurzenia i zbieżność aproksymacji w normie H^1.

Kontrola zapisanego źródła: 1005 wierszy (wcześniej 923), 37 zachowanych unikatowych etykiet, 31 wystąpień odsyłaczy, wszystkie cele jednoznaczne w źródle oraz rozdziałach 9,10,18; brak błędów begin/end. Brak dedykowanej kompilacji rozdziału 19.
Rozdział 18: run 45985450719 in_progress przy pierwszym odczycie, końcowy 45985977450 nadal queued przy ostatnim odczycie. Nie zmieniano rozdziału 18; jego końcowy odbiór techniczny pozostaje otwarty.
Następny etap: kontrprzykład fundamentalny, usuwalność ograniczonej osobliwości harmonicznej, reprezentanci quasi-ciągli i podaddytywność przeliczalna. Rozdział 19 pozostaje w pierwszym audycie.
