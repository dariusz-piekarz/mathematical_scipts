# RRC 14 — iteracja 221: pierwsza lektura 001–020

Rozdział 13 zamknięty zgodnie z uzgodnieniem 220. RRC 14: 10 sekcji, 34 etykiety. Źródło przed 5abe8368d2e2ec82873397259b120324042ceea0 (742 wiersze), po 41aba61f88c06a5bdc877cdd11ac9cca25f5642a (825 wierszy), commit 6fbd20381e88564b9000b0f4b36b9aef8b9c5a7e. Pierwsze trzy sekcje odczytane szczegółowo. Przyjęto 64 kryteria robocze.

| Kryterium | Wynik |
|---|---|
| PDE-14-001 | Jawne konwencje rzeczywiste i wspólny zbiór pełnej miary dla eliptyczności. |
| PDE-14-002 | Ograniczoność formy i poprawność definicji podrozwiązania. |
| PDE-14-003 | Oba kierunki równoważności rozwiązania z pod- i nadrozwiązaniem przez rozkład testu na części dodatnią i ujemną. |
| PDE-14-004 | Obcięcie poziomowe z istniejącego twierdzenia RRC 09, stała w H¹, wzór na gradient. |
| PDE-14-005 | Ślad obcięcia z udowodnionego lematu RRC 13 i charakterystyki H_0¹ w RRC 10, zamiast ogólnego nieuzasadnionego twierdzenia o złożeniach Lipschitzowskich. |
| PDE-14-006 | Dopuszczalność testu i jawne zachowanie poza zbiorem poziomowym. |
| PDE-14-007 | Znak wyrazu zerowego, eliptyczność, Poincaré i wniosek p.w.; c=0 bez ograniczenia znaku M. |
| PDE-14-008 | Porównanie przez różnicę i liniowość, bez symetrii A. |
| PDE-14-009 | Uwzględniono już udowodnioną zasadę porównania z dryfem RRC 13 i warunek c-div(b)/2>=0, stała M jako nadrozwiązanie przy cM>=0. |
| PDE-14-010 | Kontrprzykład rezonansowy z ujemnym c poprawny. |
| PDE-14-011 | Lemat Weyla: poprawne d>=2, rzeczywisty gładki reprezentant, identyfikacja części urojonej; przypadek d=1 osobno. |
| PDE-14-012 | Rozróżnienie globalnego ekstremum w tym dowodzie i lokalnego ekstremum w mocniejszym twierdzeniu RRC 03. |
| PDE-14-013 | Dokładny odsyłacz do wartości średniej, nieujemność i ciągłość na sferze, zbiór otwarty i domknięty. |
| PDE-14-014 | Dodatniość albo identyczne zero; jednoznaczność z ciągłości na domknięciu, niepustego brzegu i obu ekstremów. |
| PDE-14-015 | Geometria kuli wewnętrznej i kierunek normalny do kuli, niekoniecznie do brzegu obszaru. |
| PDE-14-016 | Jednostronna definicja pochodnej konormalnej w sensie kierunkowym Hopfa (normalnej do kuli), znak i związek z gradientem przy przedłużeniu C¹. |
| PDE-14-017 | Jawny rachunek wszystkich drugich pochodnych bariery i warunek alpha>2d/R². |
| PDE-14-018 | Dobór epsilon, oba brzegi pierścienia, ścisła nierówność laplasjanu i argument w punkcie hipotetycznego ujemnego minimum. |
| PDE-14-019 | Położenie punktu na promieniu dla 0<t<R/2, granica ilorazu bariery i dolna granica przyrostu. |
| PDE-14-020 | Klin: dokładny rachunek laplasjanu, ciągłość na domknięciu, jednostajne o(r), dowód braku kuli wewnętrznej przez odległości od prostych. |

16 zamian blokowych. 34 etykiety zachowane w kolejności; 32/32 wystąpienia odsyłaczy (23 cele), jednoznaczne na przypiętym commicie w RRC 01,03,07,09,10,13,14,15,17; stos środowisk poprawny. Odczytano rzeczywiste tezy RRC 01,03,07,09,13. Nie uruchamiano dedykowanego CI, kompilacji, kontroli PDF ani Lean.

Plan pozostałych kryteriów: 021–032 Harnack, łańcuch kul, Liouville i oszacowania pochodnych; 033–044 subharmoniczność, mocna zasada i Hopf dla superharmonicznych, Caccioppoli; 045–058 Green, dodatniość, kula, reprezentacja i porównanie; 059–064 rysunek, zakres wyników, struktura i odsyłacze. Pierwsza lektura 20/64 (3/10 sekcji). Kolejne lektury aż do czystego przebiegu, dedykowana walidacja oraz odrębna kontrola.