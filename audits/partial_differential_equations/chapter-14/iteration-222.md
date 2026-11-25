# RRC 14 — iteracja 222: pierwsza lektura 021–032

Źródło przed 41aba61f88c06a5bdc877cdd11ac9cca25f5642a, po 15c669e7697a55d2d9310f0bb49b0f700c98ce25; commit 7535789762c7e96dc27760ea7018bb35b5505c18. Odczytano sekcje 4–5 i rzeczywiste tezy RRC 03 dotyczące Poissona, Harnacka, pochodnych, Liouville'a oraz analityczności.

| Kryterium | Wynik |
|---|---|
| PDE-14-021 | Ujednolicono znaczenie symbolu pola sfery z konwencją RRC 03; wskazano dokładne twierdzenie Poissona. |
| PDE-14-022 | Jawne zastosowanie całki Poissona do istniejącej funkcji harmonicznej z ciągłymi danymi brzegowymi przez jednoznaczność. |
| PDE-14-023 | Odtworzono rachunek ilorazu jąder i monotoniczność obu granic względem odległości od środka; wykorzystano mocniejszą górną stałą z RRC 03. |
| PDE-14-024 | Wyprowadzono C=((R+r)/(R-r))^d, bez dzielenia przez wartość funkcji, w tym przypadek zerowy. |
| PDE-14-025 | Usunięcie warunku przedłużenia poza kulę przez promienie rho z r<rho<R i granicę samych stałych. |
| PDE-14-026 | Udowodniono spójność łamaną obszaru przez zbiór osiągalności. |
| PDE-14-027 | Konstrukcja łańcucha kul: dodatnia odległość zwartej łamanej od dopełnienia, jednostajna ciągłość, skończony podział. Osobno U=R^d. |
| PDE-14-028 | Iteracja stałej 3^d, oszacowania w obu kierunkach, otoczenia końców, skończone podpokrycie i stała niezależna od u. |
| PDE-14-029 | Liouville z jednostronnym ograniczeniem, oba przypadki przesunięcia i granica jawnych stałych. |
| PDE-14-030 | Różniczkowanie pod całką: jawna majoranta ilorazów różnicowych, zbieżność zmajoryzowana, rachunek gradientu jądra. |
| PDE-14-031 | Norma euklidesowa gradientu bez dodatkowego czynnika sqrt(d), ciągłość na brzegu i geometria kul wewnętrznych; poprawiono stałą lokalną do d/(R-r), zachowując wcześniejszą słabszą tezę. |
| PDE-14-032 | Gładkość z lematu Weyla, komutacja pochodnych z laplasjanem i jawna iteracja na m równomiernie zagnieżdżonych kulach; oszacowanie (dm/(R-r))^m dla wielowskaźnika długości m. |

10 zamian blokowych, 919 wierszy, 34 etykiety zachowane w kolejności. 38/38 wystąpień odsyłaczy (28 różnych celów) jednoznacznie rozwiązanych na przypiętym commicie w RRC 01,03,07,09,10,13,14,15,17; stos środowisk poprawny. 300/300 pomocniczych skończonych kontroli ilorazu jąder Poissona dla wymiarów 2,3,4,7, trzech względnych promieni i różnych położeń/kątów. Nie są dowodem ani testami CI. Nie wykonano dedykowanej kompilacji, kontroli PDF ani Lean.

Pierwsza lektura 32/64, 5/10 sekcji. Następna: 033–044, subharmoniczność, mocna zasada i Hopf dla superharmonicznych, Caccioppoli.