# RRC 17 — iteracja 297: energia potęg, iteracja Mosera i most logarytmiczny

Commit źródła: 33959d71becc70e58f81ad30e6aed81a796fd4a1. Szczegółowa lektura sekcji 17.4–17.5.

- Naprawiono lukę w skalowaniu iteracji Mosera w wymiarze 2: przy chi=2 poprzedni argument na zmiennych promieniach prowadził do niewłaściwej potęgi odstępu promieni. Nowy dowód najpierw przeprowadza iterację na ustalonej parze kul B_1, B_2, następnie skaluje do B_t, B_{2t} i korzysta z przeliczalnego pokrycia B_r przy t=(s-r)/2. Otrzymuje właściwy czynnik (s-r)^(-d/q) także w d=2.
- Rozpisano test potęgowy, znak beta-1, absorpcję Younga i zależność stałych wyłącznie od ilorazu eliptyczności.
- Dla 0<q<2 rozpisano interpolację przez punktową nierówność i skończoną sumę iteracji absorpcyjnej; dla q<1 zaznaczono, że zapis L^q nie oznacza normy.
- Uzasadniono dopuszczalność funkcji testowej z odwrotnością i słabą pochodną logarytmu, bez założenia lokalnego ograniczenia z góry nadrozwiązania.
- W dowodzie lematu Johna–Nirenberga skonstruowano jawne pokrycie kostkami, sprawdzono łańcuchy sąsiedztwa, objętości przecięć i zawieranie powiększeń w większej kuli.
- Zapewniono dodatnią stałą M w doborze q_0=c_d/M.

Kontrola zapisanego źródła: 758 wierszy, 36 etykiet zachowanych w tej samej kolejności, 31 wystąpień ref/eqref/cref, brak niezgodności zagnieżdżenia środowisk begin/end. Kontrola strukturalna nie zastępuje kompilacji ani weryfikacji wszystkich odsyłaczy. CI aplikacji 45978120038 i terminologii 45978120130 w kolejce; brak dedykowanego przebiegu rozdziału 17. Nie oznaczać jako ustabilizowany.

Następny etap: sekcja 17.6 (Harnack, oscylacja, reprezentant Hölderowski), 17.7–17.8, następnie ponowna lektura całego rozdziału i dedykowany odbiór techniczny.
