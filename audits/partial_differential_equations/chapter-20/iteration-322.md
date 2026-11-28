# RRC 20 — iteracja 322

Commit źródła 1b4ce9f0c817726b324724980bcba6da684f473e, blob 51deba7a7ccf0154ce5dceebddde22d20d8ab838. Pierwszy audyt szczegółowy sekcji 20.5–20.6.

- Zdefiniowano potęgi spektralne wraz z dziedzinami i odróżniono operator nieograniczony w H od rozszerzenia formowego V→V*. Uzasadniono własność półgrupy i silną ciągłość, także w chwili zero, oraz zbieżność skończonych sum w przestrzeni energii wraz z pochodnymi.
- Rozpisano oszacowanie wygładzające i dokładną całkową tożsamość zaniku energii z twierdzenia Tonellego.
- We wzorze Duhamela uzasadniono silną mierzalność integrandu i istnienie całki Bochnera dla każdego t, ciągłość, rozwiązanie współczynników przez czynnik całkujący, zbieżność pochodnych i warunku początkowego oraz identyczność granic.
- Dowód wyższej regularności energii oparto na oszacowaniu różnic skończonych przybliżeń, uzyskując silną zbieżność w C([0,T];V), H^1(0,T;H) i L^2(0,T;D(L)) z normą grafową. Rozpisano stałe oszacowania i kontrolę Lu. Odsyłacz do identyfikacji D(L) dla brzegu C^{1,1} pozostaje do uzupełnienia w lekturze stabilizacyjnej.
- W modelowym lemacie Aubina–Lionsa uzupełniono jednostajne ograniczenie współczynników, argument Arzelà–Ascoliego, podciąg przekątny i kryterium Cauchy'ego z trzema składnikami. W oszacowaniu przesunięć czasowych uzasadniono tożsamość w V* przez rzuty spektralne.

Kontrola zapisanego źródła: 964 wiersze (847 wcześniej), 23 zachowane unikatowe etykiety, 32 wystąpienia odsyłaczy (9 różnych zewnętrznych), wszystkie cele jednoznaczne w źródle i rozdziałach 9,10,11,18, brak niezgodności begin/end. Nie wykonano kompilacji rozdziału 20. Rozdział 19: cztery przebiegi CI przy odczycie nadal queued; odbiór techniczny pozostaje otwarty.

Postęp pierwszej lektury 6/8 sekcji. Następny etap: eksplozja rozwiązań (porównanie skalarne i czas eksplozji) oraz stabilność wstecznego Eulera; następnie stabilizacja i dedykowana kompilacja.