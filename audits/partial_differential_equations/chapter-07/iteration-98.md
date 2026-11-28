# PDE-07 — iteracja 98: druga lektura sekcji 7.5–7.6

Data: 2026-11-25. Przed zmianami blob f551e58ebbf453bf48788ddffd47c1afe3e80e51, po zmianach commit 753b2cfdca7714dc2eec5911c7c5d1c08918b76d, blob 0cd323acdfb2e3b3db39be3df778fe665ff0ec29. Zachowano 36 etykiet, 69 wystąpień odsyłaczy (+3 wewnętrzne), dziewięć dotychczasowych celów zewnętrznych i poprawne zagnieżdżenie środowisk. Zmieniono tylko sekcje 7.5–7.6.

| ID | Wynik drugiej lektury | Uzasadnienie |
|---|---|---|
| PDE-07-031 | PASS po korekcie | Jawny przykład jądra o zwartym nośniku wewnątrz kuli, pełna normalizacja i skalowanie nośnika. |
| PDE-07-032 | PASS po korekcie | Jawny wzór całkowy dla ilorazu różnicowego w każdej półnormie, także dla ujemnego h. |
| PDE-07-033 | PASS | Znaki dwóch pochodnych znoszą się, obie tożsamości splotu poprawne. |
| PDE-07-034 | PASS | Rosnące dziedziny, wspólny zwarty nośnik, zbieżność sum Riemanna we wszystkich półnormach i ciągłość funkcjonału poprawne. |
| PDE-07-035 | PASS | Odbicie jądra, znak przesunięcia, jednostajna zbieżność pochodnych na wspólnym nośniku poprawne. |
| PDE-07-036 | PASS | Obcięcie do zwartego poszerzenia K i zastosowanie całkowej nierówności Minkowskiego poprawne. |
| PDE-07-037 | PASS po korekcie | Przeniesienie dowodu gęstości z L¹ na L^p z jawnymi oszacowaniami zamiast ogólnego odwołania do twierdzenia Fejéra. |
| PDE-07-038 | PASS po korekcie | Uzasadniono przejście od istotnego supremum do punktowych ograniczeń dla funkcji ciągłej po obu stronach skoku. |
| PDE-07-039 | PASS semantyczny po korekcie | Jądro bazowe c eta(2x), parametry epsilon=2 i 4 odpowiadają istniejącym profilom o nośnikach [-1,1] i [-2,2]. Stary podpis używał jądra, którego nośnik nie był zwartym podzbiorem otwartej kuli jednostkowej. Oględziny nowego renderu pozostają otwarte. |
| PDE-07-040 | PASS | Równoważność i jednoznaczność przez iniektywność, niezależność od reprezentanta. |
| PDE-07-041 | PASS po korekcie | Sprecyzowano zastrzeżenie o jednej mieszanej pochodnej, zweryfikowano przez H(x) w dwóch wymiarach i testy iloczynowe. Nie jest to zaprzeczenie twierdzeniom o pochodnych czystych. |
| PDE-07-042 | PASS | Lokalna całkowalność, liniowość i aksjomaty normy poprawne dla całego przedziału p. |
| PDE-07-043 | PASS | H^m=W^{m,2} na całej przestrzeni z równoważnymi normami, brak automatycznej identyfikacji konstrukcji na innych zbiorach. |
| PDE-07-044 | PASS po korekcie | Wyraźnie wskazano, że testy dowodu nieregularności delty mieszczą się także w (-1,1). |
| PDE-07-045 | PASS | Funkcja pierwotna o zwartym nośniku, równość T=T_c, jednoznaczność; usunięto powtórzenie. |
| PDE-07-046 | PASS | Stałość lokalnych wygładzeń i zbieżność stałych przez ustalony test o całce 1. |
| PDE-07-047 | PASS | Sklejenie stałych, spójność, iniektywność i przypadek składowych spójnych poprawne. |

Wynik: 10 kryteriów bez istotnej korekty, 7 po korekcie, 17/17 sprawdzonych semantycznie; 039 wymaga jeszcze kontroli wizualnej. Rejestr nadal zawiera 70 pozycji; wzmocniono 031,032,037–039,041,044. Commit 9f2940fcce989e1380b6e7abe98c63833a259bdd, blob 8fcb2537b2fd43bdd155f97f7d01b15ae7c958b9. Druga lektura 47/70. Zakres tematyczny bez zmian.

Stan poprzedniego CI: {"id":45585815404,"status":"completed","conclusion":"success"}. Nowe przebiegi dla commitu rejestru: [{"id":45586146323,"name":"PDE - chapter 07 audit","status":"in_progress","conclusion":null}]. Nie pobrano nowych logów ani PDF; nie uruchomiono lokalnych testów Python, pełnej kompilacji tomu ani Lean. Kolejna iteracja 99: druga lektura sekcji 7.7–7.8, kryteria 048–060. Rozdział pozostaje nieustabilizowany.
