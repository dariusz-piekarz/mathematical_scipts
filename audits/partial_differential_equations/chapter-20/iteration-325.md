# RRC 20 — iteracja 325: drugi pełny audyt stabilizacyjny

Commit źródła b47a1a313add758a8ba083ec05a1e5009ebed32a, blob ec71b1fa354af6d5f73fd6e0bb909af0d68a57bc. Ponownie odczytano wszystkie osiem sekcji.

- Jawnie określono normę V* względem normy energetycznej V, wskazano twierdzenie Hahna–Banacha w dowodzie gęstości H w V*, uściślono interpretację warunku Dirichleta i brak wymogu śladu przestrzennego danych początkowych w H.
- Sprawdzono dowód silnej zbieżności całego ciągu Galerkina: równanie błędu względem P_nu, znaki, zerowe dane początkowe, stałą Lambda^2/lambda i oszacowanie pochodnej. Nie stwierdzono nowych usterek matematycznych w tym dowodzie; doprecyzowano sformułowanie odejmowanych równań.
- Rozróżniono konsekwentnie operator L w H i rozszerzenie formowe w V* w twierdzeniach o Duhamelu i maksymalnej regularności; jawnie wskazano zgodność obu operatorów na D(L).
- Wzmocniono twierdzenie o maksymalnej regularności do dokładnej tożsamości całkowej z normami u' oraz Lu. Dowód przez rozwinięcie kwadratu normy równania skończonego, pochodną energii V i silną zbieżność w ustalonych wcześniej przestrzeniach. Uzyskano też kwadratowe oszacowanie Lu bez dodatkowej stałej.
- Sprawdzono obcięcia czasowe, dodatniość, półgrupę, zwartość Aubina–Lionsa, eksplozję i zbieżność wstecznego Eulera; jawnie zdefiniowano defekt aproksymacji i poprawiono redakcję.

Kontrola zapisanego źródła: 1222 wiersze (1183 wcześniej), 23 zachowane unikatowe etykiety, 41 wystąpień odsyłaczy, 12 różnych celów zewnętrznych. Wszystkie cele jednoznaczne w źródle i rozdziałach 4,9,10,11,15,18, brak niezgodności begin/end. Dedykowane CI 45993650919 queued; wcześniejsze 45991021945 i 45991264058 oraz końcowy run rozdziału 19 45989522023 przy pierwszym odczycie queued. Brak potwierdzonej kompilacji aktualnych PDF obu rozdziałów i globalnego CI. Ponowiono zapis raportu po konflikcie równoległych commitów, uprzednio potwierdzając zgodność blobu źródła.

Następny etap: trzecia lektura stabilizacyjna, ze szczególną kontrolą nowej tożsamości energii i składu długich wzorów. Nie deklaruje się stabilizacji.
