# Rozdział 17 — audyt 54 (4/4 bloków, poprawkowy, 0/2)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Zakres i poprawki
Bloki 3–4: przestrzeń Schwartza, Fourier i splot. Jawne założenia dla ciała skalarów; konkretne stałe i przypadek N=0 w równoważności seminorm; punktowe przejście do granicy przed supremum w dowodzie zupełności; pełny wzór Leibniza dla mnożenia przez jednomian; całkowalność wagi przez szereg pierścieni dyadycznych. W dowodzie braku normowalności wybrano funkcję odcięcia równą 1 na otoczeniu kuli, co uzasadnia także przypadek rzeczywisty. Uściślono język nośników. Rozpisano majoranty różniczkowania Fouriera, całkowanie przez części i Fubiniego, jawne oszacowanie seminormy transformaty, równanie różniczkowe całki Gaussa wraz z warunkiem początkowym, normalizację i zanik masy jądra Gaussa oraz oszacowanie błędu inwersji. W dowodzie splotu jawna całkowalna majoranta, uzasadnienie Tonellego/Fubiniego i współczynnik normalizacji. Nie dodano nowych zagadnień.

## Technika
Źródło 659401e397c3768ad84dc848a8c5a51e695b3e2e, blob 4ea59c4c101f001cc37f8cea9be8cf8a74317cbb, 668 wierszy; 22/22 unikatowych etykiet, 11/11 odsyłaczy, środowiska zbilansowane, 6/6 nowych warunków tekstowych sprawdzonych. Dodano regresję test_fourier_and_schwartz_bounds (41a4b667e9179918df086c20dc6d27f3f4e34293), zawierającą także 81 przypadków kontroli fazy zespolonej; pełnego wykonania nowego testu jeszcze nie potwierdzono. CI 53: 45379165056 zakończone sukcesem (testy, kompilacja, automatyczna kontrola PDF i odsyłaczy, upload artefaktu). CI 54: 45379391791 oraz 45379435055 w toku przy odczycie. Oględzin PDF po zmianach nie wykonano.

## Decyzja o zakresie
Pierwszy przegląd 4/4 zakończony. Nie rekomenduję rozszerzenia: twierdzenie Plancherela jest już w 22, zaś Montel, nuklearność, funkcje Hermite'a i twierdzenie o jądrze w 23 (sprawdzono strukturę źródeł). Nie powielać. Następny audyt 55: stabilizacja całości, kontrola języka, kwantyfikatorów, odsyłaczy, CI i składu, bez nowych tematów. Dwa kolejne czyste audyty wymagane do zamknięcia.
