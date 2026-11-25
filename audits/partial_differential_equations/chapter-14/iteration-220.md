# RRC 14 — iteracja 220: pierwsza lektura 001–020

Rozdział 14: Zasady maksimum i teoria potencjału. Źródło przed 769eb0a329439062f16dd9aac6f3f5899e5ef11e (1143 wiersze), po 50972e18f0224af0bbf7df2f50f4130b08bcc2da (1226 wierszy); commit 2c08753cfd67761a6b5919eaf8c41eb7fe99e426. Odczytano pełny rozdział w celu inwentaryzacji, szczegółowo pierwsze trzy sekcje.

Plan 64 kryteriów: 001–009 słaba zasada maksimum; 010–013 harmoniczność i mocna zasada; 014–020 Hopf i klin; 021–030 Poisson, Harnack, Liouville; 031–035 pochodne; 036–044 subharmoniczność, dystrybucje i Hopf; 045–051 Caccioppoli; 052–062 Green, dodatniość, jawne jądro i reprezentacja; 063–064 rysunek i podsumowanie.

| Kryterium | Pierwsza lektura |
|---|---|
| 001 | Wspólny zbiór pełnej miary, rzeczywistość i eliptyczność bez symetrii. Jawna konwencja nierówności prawie wszędzie i miary brzegu. |
| 002 | Definicja pod/nadrozwiązania; podano stałą ograniczoności formy. |
| 003 | Dodano pełny dowód równoważności testowania nieujemnymi testami gładkimi i w H_0^1: podciąg, zbieżność dodatnich części gradientów, nieujemne wygładzanie z zachowaniem zwartego nośnika, ciągłość formy. |
| 004 | Rozkład dowolnego testu na dodatnią i ujemną część, ślad zero. |
| 005 | Obcięcie poziomowe i jego ślad: wykorzystano RRC 09,10,13. |
| 006 | Test (u-M)^+, znaki, eliptyczność i Poincaré; warunek M>=0, przypadek c=0. |
| 007 | Dodano dokładną granicę przez kres istotny śladu oraz kontrprzykład dla ujemnego M przy c=1, u=-cosh(x)/cosh(1). |
| 008 | Porównanie przez różnicę, odsyłacz do twierdzenia z kontrolowaną dywergencją dryfu. |
| 009 | Kontrprzykład rezonansowy przy ujemnym c; wyjaśniono również słabe znaczenie równania. |
| 010 | Lemat Weyla i rzeczywistość gładkiego reprezentanta, wymiar jeden. |
| 011 | Własność średniej i dodatnia miara fragmentu sfery; jawna dolna granica dodatniej funkcji. |
| 012 | Zbiór poziomowy otwarty i domknięty, spójność, minimum przez zmianę znaku. |
| 013 | Dodatniość; zastąpiono powtórzony dowód jednoznaczności wykorzystaniem cor:dirichlet-stability z RRC 01. |
| 014 | Kula wewnętrzna i jednostkowa normalna do kuli, niekoniecznie do brzegu obszaru. |
| 015 | Odjęcie minimum, dodatniość z wcześniejszego wniosku, ciągłość na domknięciu kuli. |
| 016 | Pochodne bariery i warunek alpha>2d/R². |
| 017 | Dodatnie minimum na wewnętrznej sferze; jawny dodatni mianownik przy wyborze epsilon. |
| 018 | Ścisła nierówność Laplace'a, minimum na brzegu, granica dolna ilorazu i znak pochodnej. |
| 019 | Klin: obliczenie laplasjanu, ciągłość przy wierzchołku i zanik ilorazu różnicowego w każdym wewnętrznym kierunku. |
| 020 | Brak kuli wewnętrznej: odległość środka od obu prostych ograniczających klin. |

11 zamian blokowych; 34 etykiety zachowane w kolejności. 61/61 wystąpień odsyłaczy (40 różnych celów) jednoznacznie rozwiązanych w RRC 01,03,07,09,10,13,14,17; stos środowisk poprawny. Odczytano faktyczne twierdzenie RRC 01 o maksimum oraz wniosek o stabilności, a także tezy RRC 03 o wartości średniej, mocnej zasadzie, Poissonie, Harnacku i Liouville'u. 36/36 pomocniczych skończonych kontroli znaku laplasjanu bariery (nie dowód i nie CI). Pierwsza lektura 20/64, 3/10 sekcji; dalsze lektury 0/64. Rysunek RRC 14 był skompilowany przez backend i obejrzany w audycie 217; dedykowana kompilacja zaktualizowanego rozdziału, PDF, CI i Lean pozostają niepotwierdzone.

Następna iteracja 221: 021–035, Poisson, Harnack, łańcuch kul, Liouville i oszacowania pochodnych. Szczególnie sprawdzić jawne stałe, przypadek zerowej funkcji i zastosowanie ulepszonej stałej gradientowej w iteracji wyższych pochodnych.