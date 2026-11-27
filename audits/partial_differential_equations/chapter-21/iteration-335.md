# RRC 21 — iteracja 335

Pierwszy pełny audyt stabilizacyjny wszystkich dziesięciu sekcji. Odczytano pełne źródło 1513 wierszy. Commit zmian 5086e5538ee81576bfdb6e2bbee9a099ae134efe, blob 3cf90133fedef2acde55b75535eb6f578f091fc4.

- Uściślono normy Sobolewa i definicję H^{-1} przez dualność oraz działanie mnożenia przez macierze. Uzasadniono wspólną mierzalność słabych pochodnych współczynników przez przeliczalny ciąg ilorazów różnicowych; w lemacie Friedricha doprecyzowano silną mierzalność iloczynów, normę współczynnika D_A i oszacowanie różnicy całek kwadratowych.
- Sprawdzono bilans globalny i stożkowy, znaki strumienia, przypadki zerowego promienia i zerowej prędkości oraz rekonstrukcję fal. Uściślono hipotezy wniosku o propagacji nośnika.
- Ponownie sprawdzono komutator splotu (znak w całkowaniu przez części, wyzerowanie całki jądra, zbieżność translacji) oraz identyfikację końców przedziału w lemacie Friedricha. Nie wykryto nowej luki w głównym argumencie silnej ciągłości.
- Osłabiono hipotezy twierdzenia o istnieniu do całkowitego s>=2 i współczynników C([0,T];W^{s,infty}), ponieważ zapisany dowód potrzebuje tylko tych założeń. Dodatkowy warunek s>d/2+1 daje reprezentanta klasy C^1 przez zanurzenia Sobolewa. Uzasadniono nieskończony wymiar przestrzeni obciętych częstotliwości. Sprawdzono znak defektu R_N, globalny argument Cauchy'ego, interpolację oraz identyfikację wszystkich pochodnych w chwili zero.
- W ważonej energii rozpisano oszacowanie różnicy wartości uzasadniające absolutną ciągłość. Sprawdzono kontrprzykład Jordana. Dla falowego symetryzatora diag(1,G) wykazano dokładne znoszenie członów niższego rzędu D_S=0, doprecyzowano krotność zera i skalarne przestrzenie dla u.
- Uściślono regularność aż do brzegu w bilansie na ograniczonym obszarze oraz całkowalność śladu na półprostej. Sprawdzono dowód oszacowania z_delta i przypadek składowych zerowych; bez nowych usterek rachunkowych.

Kontrola zapisanego źródła: 1594 wiersze, 23 zachowane unikatowe etykiety, 58 odsyłaczy, trzy różne zewnętrzne cele (rozdziały 5 i 20). Wszystkie jednoznaczne; brak błędów zagnieżdżenia środowisk i delimiterów. Dedykowane CI 45998988331 queued. Wcześniejsze CI rozdziałów 20 (45994503573) i 21 (45998027841) przy pierwszym odczycie queued. Kompilacja, wizualny odbiór i globalne CI niepotwierdzone.

Następny etap: drugi pełny audyt stabilizacyjny, w tym ponowna kontrola osłabionych założeń istnienia oraz nowego argumentu mierzalności. Nie deklaruje się stabilizacji.
