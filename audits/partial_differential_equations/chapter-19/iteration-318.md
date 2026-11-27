# RRC 19 — iteracja 318: trzecia lektura stabilizacyjna

Commit źródła da99e4b5e7b28193643df991c71dc2b7bbf2d6fc, blob ed60abea34b4993769337c380d58d6046a7385e2.

Ponownie odczytano wszystkie 9 sekcji. W dowodzie kryterium Wienera wykryto brak jawnego uzasadnienia mierzalności względnej pojemności g(t)=cap_{2,B_{2t}(x_0)}(F_t): porównanie z mierzalną funkcją nie wystarcza do mierzalności. Wykazano górną półciągłość g na (0,infty) przez próbę gładką o energii bliskiej infimum, stabilność zawierania jej nośnika w kuli zewnętrznej i zawierania F_s w otoczeniu F_t (argument zwartościowy). Rozpisano skalowanie klas prób i kontrolę skończonej części całki. Sprawdzono dyadyczne nierówności i sumowanie geometryczne; nie wykryto błędu w tych obliczeniach. Doprecyzowano, że przywołane jest kryterium całkowe, a równoważność postaci całkowej i pierścieniowej udowodniono.

Ponadto rozróżniono równość infimów od równości klas prób, ujednolicono hipotezę d>=1 w twierdzeniu o pojemności punktu i zakres uwagi o krytycznym wymiarze Hausdorffa, poprawiono stwierdzenie o zerowym ogonie szeregu dla przekłutej kuli oraz redakcję odsyłaczy.

Kontrola zapisanego źródła: 1412 wierszy (1380 przed zmianami), 37 zachowanych unikatowych etykiet, 50 wystąpień odsyłaczy, 13 różnych celów zewnętrznych. Wszystkie cele istnieją jednoznacznie w rozdziale oraz rozdziałach 7,9,10,14,18. Brak niezgodności begin/end. Dedykowane runy 45988455742, 45988751946 i 45989155792 na początku iteracji były queued. Run aktualnego commitu przy ostatnim odczycie: [{"id":45989522023,"status":"queued","conclusion":null}]. Brak potwierdzonego odbioru PDF rozdziału 19 oraz globalnego CI. Odbiór rozdziału 18 zamknięto już w 317.

Następny etap: lektura po korektach, sprawdzenie CI, aktualnego PDF i końcowy audyt kontrolny. Rozdział 19 nadal w stabilizacji.
