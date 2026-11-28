# RRC 21 — iteracja 336

Drugi pełny audyt stabilizacyjny wszystkich dziesięciu sekcji. Odczytano 1594 wiersze. Commit zmian e7d3ebf01f590821d47a0253e50b9d3001378444, blob a9fca6c2bf14978e3328f56671ac66bdfb6e0019.

- Sprawdzono wspólną mierzalność pochodnych współczynników, doprecyzowano przeliczalną sumę przesuniętych zbiorów wyjątkowych oraz konstrukcję reprezentanta wspólnie mierzalnego dla v w lemacie Friedricha. Uzasadniono ograniczoność splotu H^{-1}→H^k przez mnożnik Fouriera.
- Wyodrębniono wniosek o ciągłości w H^s i oszacowaniu energii bez dodatkowej pochodnej dla rozwiązań w L∞(0,T;H^s). Identyfikacja pochodnych w każdej chwili wynika z testowania i ciągłości. Sprawdzono osłabione założenia s>=2 i C([0,T];W^{s,∞}) w dowodzie istnienia, znak defektu, interpolację oraz warunek początkowy. Rozpisano stałą kontrakcji w równaniu regularizowanym i dowód zanurzeń zapewniających klasyczną regularność przez całkowalność transformat pochodnych.
- Sprawdzono bilans ważony i D_S=0 w redukcji równania falowego. Wskazano pełny wektor wymuszenia oraz uzasadniono ciągłość pochodnej energii na ruchomej kuli o dodatnim promieniu; jest to potrzebne do wnioskowania monotoniczności z nierówności prawie wszędzie.
- Uzupełniono argument istnienia śladu w zerze na półprostej. Ponownie sprawdzono znaki strumienia, charakterystyki, oszacowanie z_delta i przypadek zerowego modu. Nie wykryto nowych błędów rachunkowych w głównych dowodach.
- Zastąpiono makro mathscr standardowym mathcal, gdyż nie potwierdzono dostępności pierwszego w preambule Atlasu. Nie zmieniano etykiet.

Kontrola zapisanego źródła: 1681 wierszy, 23 zachowane unikatowe etykiety, 63 wystąpienia odsyłaczy, trzy różne zewnętrzne cele w rozdziałach 5 i 20; brak brakujących lub niejednoznacznych celów oraz błędów zagnieżdżenia środowisk i delimiterów. Dedykowane CI 45999927191 queued. Wcześniejsze CI 45994503573 (20), 45998027841 i 45998988331 (21) przy pierwszym odczycie queued. Brak potwierdzonej kompilacji, odbioru wizualnego i globalnego CI.

Następny etap: trzecia lektura stabilizacyjna ze szczególną kontrolą nowego wniosku i dowodu zanurzenia Fouriera. Przy braku usterek pełna lektura kontrolna; nie deklaruje się jeszcze stabilizacji.
