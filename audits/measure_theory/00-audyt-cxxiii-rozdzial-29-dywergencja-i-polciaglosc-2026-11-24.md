# Audyt CXXIII (123) — brzeg C^1 i dolna półciągłość
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
HEAD początkowy 4d5ecd38a181f327290485c14362c210ec1e5356, blob f641b77ccbb70df1684b33091ae1b4a85f8f5a77. Commit źródłowy be58566f7c8e4a474c9634664428325dbcb43fdb, blob 8181c2e83fe883e4f90db708c00a57b2c08bd347.
## Wyniki
Sześć zastąpień, 1995 -> 2110 wierszy, zachowano wszystkie 37 etykiet w pierwotnej kolejności.
- Rozróżniono globalną tożsamość miar wektorowych od ograniczenia pochodnej do otwartego Omega; jawne założenie jednostronnego brzegu.
- Pełny dowód twierdzenia o dywergencji dla brzegu C^1 zamiast skrótowego powołania się na nie: przypadek n=1, izometrie i niezmienniczość śladu, zapis pod wykresem, różniczkowanie całek o zmiennym końcu, Fubini, normalna zewnętrzna, wyznacznik Grama i wzór na pole wykresu z rozdziału 28.
- Skończoność miary brzegu wykazana przez zwarte pokrycie mniejszymi fragmentami wykresów. Rozpisano sklejanie przez podział jedności oraz zerowanie całek składników wewnętrznych i zewnętrznych. Wykazano skończoność wariacji przed reprezentacją, znak pochodnej i lokalny wzór obwodu.
- Dowód lematu o dopełnieniu: całka z dywergencji przedłużonego testu, symetria klasy testów, również obwód nieskończony.
- Samodzielne hipotezy twierdzenia o dolnej półciągłości obwodu i wariacji; jawne oszacowanie błędu całek testowych przez lokalną normę L^1.
## Otwarte
Następny audyt: tożsamość pochodnej splotu, oszacowanie translacji oraz dowód zwartości rodzin zbiorów (sumowanie po kostkach bez nadliczania, argument przekątniowy, granica funkcji charakterystycznych). Sprawdzić kompilację i rysunki po utworzeniu CI rozdziału 29. Nie uruchomiono w tej iteracji kompilacji ani regresji. Stan 28/31; rozdział 29 nadal otwarty.
