# RRC 19 — iteracja 314

Commit źródła af1b36236b4a48c246dbfc7430e07b0068cad4fa, blob 9561d79ce951d0bdae917e4077a489beb0e1b9d8.
Domknięto kontrprzykład z sekcji 19.5 oraz pierwszą szczegółową lekturę 19.6–19.7.

- Podano dokładne stałe i znaki dystrybucyjnego laplasjanu rozwiązania fundamentalnego; sprawdzono normalizację w rozdziale 7 (tam omega_d oznacza pole sfery, tutaj objętość kuli, stąd jawny zapis |S^{d-1}|).
- W dowodzie usuwalności ograniczonej osobliwości wybrano odcięcia z pojemności punktu na malejących kulach, uzasadniono ograniczoność u na nośniku testu i rozpisano oszacowanie energii ze stałą 8. Zastosowano wzmocnione twierdzenie o przedłużaniu H^1 z poprzedniej iteracji, lemat Weyla i sklejenie reprezentantów. Dodano odsyłacz do zasady maksimum.
- Uściślono definicję pojemności otwartych i dowolnych zbiorów, zgodność z definicją dla zwartych, oszacowanie miary zewnętrznej przez pojemność.
- Uzupełniono dowód przeliczalnej podaddytywności: przypadek nieskończonej sumy, silna zbieżność L^2, słaby podciąg w H_0^1, dolna półciągłość i oba przejścia epsilon do zera.
- Uzasadniono wybór szybko zbieżnych prób w konstrukcji reprezentanta quasi-ciągłego i zerową miarę zbioru wyjątkowego. Dodano pełny dowód jednoznaczności quasi-wszędzie przez względną otwartość zbioru różnic poza otwartym zbiorem małej pojemności.

Kontrola: 1102 wiersze (1005 przed zmianami), 37 zachowanych unikatowych etykiet, 36 wystąpień odsyłaczy, wszystkie cele jednoznaczne w źródle oraz rozdziałach 7,9,10,14,18. Brak niezgodności begin/end. Brak dedykowanej kompilacji rozdziału 19.
Rozdział 18: run 45985450719 po 309 zakończył się SUCCESS, końcowy 45985977450 przy odczycie nadal queued. Odbiór aktualnego PDF pozostaje otwarty.
Następny etap: bariera zewnętrznej kuli (w tym przypadek wielokrotnego styku), pojemność Newtonowska, kryterium Wienera i sekcja podsumowująca. Następnie audyty stabilizacyjne.
