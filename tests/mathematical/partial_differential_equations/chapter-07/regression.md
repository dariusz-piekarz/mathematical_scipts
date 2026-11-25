# PDE-07 — trwały rejestr kryteriów regresyjnych

Rozdział: Dystrybucje i słabe pochodne. Źródło: chapters/pl/partial_differential_equations/07-dystrybucje-i-slabe-pochodne.tex. Kryteria semantyczne są zobowiązaniami do ponownej kontroli dowodów, a nie wykonanymi testami automatycznymi lub formalizacją Lean.

| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| PDE-07-001 | def:pde7-test | Nośnik jako domknięcie względne zbioru niezerowości, zwartość wewnątrz Omega, jawna notacja wielowskaźników i półnormy, przypadek pustego K. | semantyczna |
| PDE-07-002 | def:pde7-test | Najsilniejsza lokalnie wypukła topologia z ciągłymi włożeniami; półnormy ciągłe na każdym D_K wyznaczają topologię. Zbieżność na wspólnym K daje zbieżność przez ciągłość włożenia. | semantyczna |
| PDE-07-003 | sec:pde7-tests | Wyczerpanie zwartymi zbiorami z uwzględnieniem Omega=R^d, każdy zwarty podzbiór ostatecznie zawarty. Przy braku wspólnego nośnika wybór podciągu i punktów poza kolejnymi K_l; ważona półnorma punktowa ma skończenie wiele składników na każdym D_K, jest ciągła i przeczy zbieżności. | semantyczna |
| PDE-07-004 | sec:pde7-tests | Globalne półnormy pochodnych ograniczają się do półnorm na każdym D_K, ponieważ pochodne znikają poza nośnikiem. Zbieżność w topologii induktywnej daje zanikanie wszystkich półnorm; przypadek granicy niezerowej przez różnicę i sumę zbiorów zwartych. | semantyczna |
| PDE-07-005 | sec:pde7-tests | Dodatnia odległość niepustego zwartego nośnika od dopełnienia właściwego zbioru otwartego; przedłużenie zerem gładkie również na brzegu. Przypadek funkcji zerowej i całej przestrzeni osobno. | semantyczna |
| PDE-07-006 | sec:pde7-tests | Pochodne rho(s)=exp(-1/s) dla s>0 mają postać wielomianu w 1/s razy wykładnik; poprawna rekurencja wielomianów, zanik ilorazów różnicowych i indukcja gładkości w zerze. Złożenie rho(1 minus kwadrat normy x) daje gładką funkcję z nośnikiem w domkniętej kuli, skalowanie i przesunięcie dają funkcję testową na kuli wewnętrznej. | semantyczna |
| PDE-07-007 | sec:pde7-tests | Przesunięcia eta(x-j) mają nośniki [j-1,j+1], wszystkie pochodne ograniczone i ostatecznie zerowe na każdym zwartym zbiorze, ale brak wspólnego zwartego nośnika wyklucza zbieżność w D(R). | semantyczna |

## Iteracja 84 — 2026-11-25

Pierwszy audyt sekcji 7.1 z wprowadzeniem. Uzupełniono dowód charakterystyki zbieżności ciągów w topologii granicy induktywnej, w tym kluczowy argument z ciągłą półnormą wykrywającą uciekające nośniki. Sprecyzowano nośnik, wielowskaźniki, przedłużenie przez zero oraz pełną konstrukcję gładkiej funkcji testowej przez indukcję pochodnych. Poprawiono przykład przesunięć i rozróżnienie zbieżności na zbiorach zwartych od zbieżności w D. Commit źródła 1ad8aaecacdbb8d2bdced74efc5762e3ae68b71b, blob 8dcfb2d76f085e295c5942c2605fd5c1794975e7. Kontrola strukturalna: 36 unikatowych etykiet bez zmian, 10 odsyłaczy bez zmian, poprawne zagnieżdżenie środowisk, 10 sekcji. Dodano 7 kryteriów semantycznych. W tej iteracji nie uruchomiono testów wykonywalnych, CI, kompilacji PDF ani Lean; nie przeprowadzono jeszcze pełnej kontroli zewnętrznych odsyłaczy. Pierwszy audyt 1/10 sekcji. Następny zakres: 7.2 — Dystrybucje jako ciągłe funkcjonały liniowe.
