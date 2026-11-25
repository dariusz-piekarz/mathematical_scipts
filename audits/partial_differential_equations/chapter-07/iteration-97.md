# PDE-07 — iteracja 97: druga lektura sekcji 7.3–7.4

Data: 2026-11-25. Przed zmianami blob 26e76ef3e6d554997e35ee1df3b61900e09ad16b, po zmianach commit 278629af67e256545aff834f26b447526d050b7c, blob f551e58ebbf453bf48788ddffd47c1afe3e80e51. Zachowano 36 etykiet i 66 odsyłaczy w tej samej kolejności oraz poprawne zagnieżdżenie środowisk. Zmieniono tylko sekcje 7.3–7.4.

| ID | Wynik drugiej lektury | Uzasadnienie |
|---|---|---|
| PDE-07-015 | PASS | Wzór, znaki, oszacowanie lokalne i komutowanie pochodnych poprawne. |
| PDE-07-016 | PASS | Przedłużenie iloczynu u phi zerem i całkowanie po prostych poprawne. |
| PDE-07-017 | PASS | Oszacowanie z 2^m i reguła Leibniza dla zespolonych funkcji poprawne. |
| PDE-07-018 | PASS | Właściwe znaki i zanik wyrazów brzegowych dla H i modułu x. |
| PDE-07-019 | PASS po korekcie | Dopisano jawny wzór pochodnych skalowanego testu i zanik półnorm niższego rzędu; argument o mierze Radona poprawny. |
| PDE-07-020 | PASS po korekcie | Wyjaśniono lokalną ograniczoność przez skończone pokrycie i reprezentantów zerowych na S. Lokalna skończoność sigma wynika ze wzoru powierzchni wykresu. |
| PDE-07-021 | PASS po korekcie | Osobne puste przecięcie, cylindry wybrane z wyprzedzeniem, dokładne dziedziny całkowania i przypadek d=1. Znaki normalnych poprawne. |
| PDE-07-022 | PASS po korekcie | Pokrycie uprzednio wybranymi cylindrami eliminuje nieuzasadnione założenie, że każdy test w dowolnym otoczeniu wykresowym mieści się w jednym cylindrze. |
| PDE-07-023 | PASS | Obie implikacje warunku skoku strumienia, iniektywność, zanik części regularnej i test stałego znaku poprawne. |
| PDE-07-024 | PASS po korekcie | Konwencja dla pustego otwartego zbioru; ograniczanie, rozkład testu, największy otwarty zbiór zanikania i lokalność poprawne. |
| PDE-07-025 | PASS | Iniektywność i przeliczalne podpokrycie dają nośnik istotny. |
| PDE-07-026 | PASS | Inkluzje nośników i testy wykrywające pochodne delty poprawne. |
| PDE-07-027 | PASS po korekcie | Dopisano jawne porównanie kul metrycznych z półnormami oraz warunku Cauchy'ego; argument całkowania po odcinkach i wspólny nośnik poprawne. |
| PDE-07-028 | PASS | Punktowa ograniczoność, Baire, skalowanie i lokalne oszacowanie granicy poprawne; pusty K osobno. |
| PDE-07-029 | PASS | Pochodne i mnożenie przez ustalony gładki czynnik zachowują granice. |
| PDE-07-030 | PASS | Lokalna zbieżność L¹ implikuje dystrybucyjną, aproksymacje delty nie mają granicy w lokalnym L¹. |

Wynik: 10 kryteriów bez korekty, 6 po korekcie, 16/16 zweryfikowanych semantycznie. Wzmocniono kryteria 019–022,024,027 z zachowaniem ID. Rejestr 70 pozycji: commit 800a00fad6eebb47c48bdef9ef7f3fd58cc3ba9b, blob e5ebf5d6899ee5012d646e7a9ffeeb105f228ce2. Łącznie druga lektura 30/70 kryteriów. Nie rozszerzano zakresu.

Poprzedni przebieg 45584928939 (commit dce623092ad436676a820fabb3a337e79be872fd) ma status completed/success, co potwierdzono przez API. Nie pobrano jego logów ani artefaktu. Nowe przebiegi dla commitu rejestru: [{"id":45585815404,"name":"PDE - chapter 07 audit","status":"in_progress","conclusion":null}]. Nowa wersja wymaga osobnego potwierdzenia CI i kontroli PDF. Nie uruchamiano lokalnych testów Python, pełnej kompilacji tomu ani Lean. Kolejna iteracja 98: druga lektura sekcji 7.5–7.6, kryteria 031–047. Rozdział pozostaje nieustabilizowany.
