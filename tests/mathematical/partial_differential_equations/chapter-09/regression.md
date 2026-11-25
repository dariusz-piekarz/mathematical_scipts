# PDE I — rozdział 09: trwały rejestr regresji matematycznych

Źródło: `chapters/pl/partial_differential_equations/09-przestrzenie-sobolewa.tex`. Kryteria semantyczne sprawdza się przez lekturę twierdzeń i dowodów, nie przez samą obecność kotwicy. Testy wykonywalne zostaną przygotowane dla konkretnych przykładów; formalizacja Lean stanowi oddzielny etap i nie jest zastępowana tym rejestrem.

| ID | Kotwica | Kryterium | Metoda |
| --- | --- | --- | --- |
| PDE-09-001 | chap:pde-sobolev | Jawne d>=1, k>=0, 1<=p<=infty, niepusty otwarty Omega bez automatycznej spójności; rozróżnienie klas a.e., pochodnych dystrybucyjnych i reprezentantów; konwencja miary. | semantyczna |
| PDE-09-002 | def:pde9-Wkp | L^p zawiera się lokalnie w L¹ przez Höldera, osobno oba końce zakresu; tożsamość testowa dla wielowskaźnika ze znakiem (-1)^abs(alpha), jednoznaczność reprezentanta a.e., alpha=0 daje u. | semantyczna |
| PDE-09-003 | def:pde9-Wkp | Liniowość, iniektywne odwzorowanie do skończonego produktu L^p; norma dla p skończonego i maksimum dla p=infty, trójkąt, jednorodność i dodatnia określoność, W^0,p=L^p. | semantyczna |
| PDE-09-004 | def:pde9-local-zero | W^k,p_loc przez U relatywnie zwarte, ograniczenie słabych pochodnych do otwartych podzbiorów przez przedłużenie testu przez zero; norma nie rośnie, włożenie globalnej przestrzeni w lokalną. | semantyczna |
| PDE-09-005 | def:pde9-local-zero | Sklejanie lokalnych reprezentantów na przeliczalnym pokryciu, zgodność a.e. na przecięciach, skończone pokrycie zwartego podzbioru, również p=infty; tożsamość na każdym teście globalnym. | semantyczna |
| PDE-09-006 | def:pde9-local-zero | W_0^k,p jako domknięcie C_c^infty dla p<infty w tym rozdziale; brak założenia istnienia śladu i brak przenoszenia gęstości na p=infty. | semantyczna |
| PDE-09-007 | sec:pde9-def | Porównanie norm sumy, l^p i maksimum przez skończone M, poprawne stałe M^(1-1/p) i M; równość norm W^1,2 oraz Bessela H^1 przez Plancherela i transformatę pochodnej, także k=0. | semantyczna |
| PDE-09-008 | sec:pde9-def | abs(x) należy do W^1,p na (-1,1) dla całego zakresu p, H nie należy do W^1,p; druga pochodna abs(x)=2 delta_0 wyklucza W^2,p; poprawne odesłanie do dowodów rozdziału 07. | semantyczna |
| PDE-09-009 | ex:pde9-power | Funkcja odcinająca psi, wartość u w zerze jawna, próg ap<d z całki radialnej, rozbieżność logarytmiczna na granicy i brak L^infty przez zbiory dodatniej miary. | semantyczna |
| PDE-09-010 | ex:pde9-power | Jawny gradient poza zerem, norma gradientu blisko zera, równoważność całkowalności składowych i modułu, próg (a+1)p<d z całki radialnej. | semantyczna |
| PDE-09-011 | ex:pde9-power | Wystarczalność: całkowanie przez części na pierścieniu z poprawną normalną wewnętrznej sfery, granica wyrazu brzegowego przez eps^(d-1-a), zbieżność obu całek objętościowych przez lokalną całkowalność. | semantyczna |
| PDE-09-012 | ex:pde9-power | Konieczność: zgodność słabej i klasycznej pochodnej poza zerem, singleton miary zero, wszystkie składowe muszą być w L^p, co wymusza próg gradientu. | semantyczna |

## Iteracja 128 — 2026-11-25

Pierwsza lektura wprowadzenia i sekcji 9.1. Uszczegółowiono definicje, normy, lokalizację i sklejanie, wykorzystano sprawdzone wyniki rozdziałów 07–08. Dodano konsekwencję abs(x) nie należy do W^2,p i przypadek p=infty w istniejącym przykładzie potęgowym, bez rozbudowywania odrębnego działu. Rozpisano obie implikacje kryterium całkowalności słabego gradientu oraz normalizację normy H¹.

Źródło commit 031906d40233c0c0ed86b992c7144c651eec8d57, blob 9ec0dff354ae3ee8375c680d966f39683ae3e372. Zachowano 36 unikatowych etykiet; 28 wystąpień odsyłaczy, 10 zewnętrznych celów odnalezionych w rozdziałach 07–08 i 10. Stos środowisk poprawny; dalszy tekst identyczny z poprzednim. Rejestr 12 kryteriów, kotwice w źródle. Nie uruchamiano kompilacji, testów wykonawczych ani Lean.

Następna iteracja 129: pierwsza lektura 9.2 (zupełność i zamkniętość) oraz 9.3 (wymiar jeden), o ile zakres dowodów pozwoli na rzetelną kontrolę obu sekcji. Przed zakończeniem pierwszej lektury sprawdzić zasadność dodatkowych przykładów, w tym różnicy pomiędzy gęstością dla p skończonego i p=infty; nie dublować teorii z rozdziałów 07, 08, 10.
