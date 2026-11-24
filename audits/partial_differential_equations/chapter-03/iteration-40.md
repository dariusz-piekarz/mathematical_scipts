# PDE-03 — iteracja stabilizacyjna 40 (2026-11-24)

Źródło: blob 2312e3e42efd784285c58712f17341ed886f5893, rejestr: 09d711b62cb6c28f0c4605472ae3ef67b4bc8c0e.

## Ponowny audyt matematyczny sekcji 3.3–3.5
Przeczytano pełne trzy sekcje. Nie znaleziono nowego istotnego błędu w następujących argumentach:
- PDE-03-006: laplasjan radialny, stała normalizacyjna, znak normalnej na wewnętrznej sferze, całkowalność lokalna w n=2 i n≥3 oraz rachunek w n=1. Granice składników brzegowych i całki objętościowej są niezależnie uzasadnione.
- PDE-03-007: zwartość K-L, wspólna dominacja pochodnych przesuniętego f, zastosowanie tożsamości dystrybucyjnej do f(x-z), dwukrotna zmiana znaku, opis niejednoznaczności.
- PDE-03-007A–007C: znaki obu tożsamości Greena, warunki regularności, harmoniczność poza biegunem oraz rozkład całki brzegowej na trzy składniki. Sprawdzono, że I_epsilon dąży do u(x), a przeniesienie całki z brzegu daje właściwy znak minus w reprezentacji.
- PDE-03-008: tożsamość inwersji, dodatniość Q_R, zgodność poprawki harmonicznej w wymiarze 2 i wyższych, przypadek bieguna w zerze, symetria oraz warunki brzegowe.
- PDE-03-009–009C: rachunek gradientu i pochodnej normalnej, komutacja pochodnych na iloczynie otwartych zbiorów, normalizacja przez funkcję stałą, dominacja pochodnych oraz granica przy brzegu. Sprawdzono wielomian w przykładzie, potęgi i stałe nierówności Harnacka, nieujemność danych oraz skończone łańcuchy kul z wyborem skończonego podpokrycia. Przypadek u(z_0)=0 nie wymaga dzielenia przez u(z_0).

## Kontrola regresji i zakres dowodów
W tej iteracji ponownie sprawdzono 47 unikatowych etykiet, 46 odsyłaczy, 30 unikatowych ID i ich kotwice, poprawność zagnieżdżenia środowisk; trzy zewnętrzne cele pozostają thm:laplace-max, chap:pde-intro, chap:pde19.
Porównano SHA czterech aktualnych plików z wersją w commicie ed7a018fd418ef88f1008da3de02b1f95df3b878: źródło, rejestr, test wykonywalny (ab010d105b9a731d56ad5c7f61be52171270328f) i workflow (c95851be2c4eafe59516b57e571e633ca3f1712c) identyczne. Ponownie odczytano wyniki job 138694173032, przebieg 45464079233: wszystkie kroki zakończone sukcesem. Jest to wykorzystanie wcześniejszego wykonania 7 testów i kompilacji, nie nowy przebieg. Dowód wizualny obu rysunków pochodzi z iteracji 39 i dotyczy tego samego blobu; nie otwierano ponownie obrazów w tej iteracji.
Nie zmieniono źródła ani kryteriów. Ponowny audyt matematyczny objął łącznie 5/10 sekcji (iteracje 39–40); pozostały sekcje 3.6–3.10. Nie kompilowano całej książki, nie uruchamiano Lean. Rozdział pozostaje otwarty.
