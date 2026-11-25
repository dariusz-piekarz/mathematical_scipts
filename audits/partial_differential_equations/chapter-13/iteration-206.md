# RRC 13 — iteracja 206: pierwsza lektura 015–028

Źródło przed 7a36d0c57c8e5b24f0aebe1896536c2eb9e998d5, po 7b74babdc35cb6b654c0de2698c017f69b9b5354, commit 5b733e02c8fa4f776cad4af80b2fac2e94b7eadb. Szczegółowo odczytano sekcję Dirichleta oraz skorygowano zastosowanie wcześniejszej reguły Leibniza.

| ID | Wynik pierwszej lektury |
|---|---|
| PDE-13-015 | Rozdzielono oszacowanie dla b=0,c≥0 od oszacowania dla ogólnej koercywności ze stałą alpha. |
| PDE-13-016 | Jawne użycie Poincarégo, Laxa–Milgrama, testowanie u i przypadek zerowy. |
| PDE-13-017 | Wyprowadzono stałą koercywności (lambda/2-Gamma C_P²)/(1+C_P²) przy warunku małości. |
| PDE-13-018 | Sprawdzono operator prawostronnie odwrotny do śladu i normę ilorazową z RRC 10. |
| PDE-13-019 | Obie implikacje charakterystyki zbioru funkcji o zadanym śladzie jako G+V. |
| PDE-13-020 | Ciągłość funkcjonału po odjęciu przedłużenia, Lax–Milgram, istnienie. |
| PDE-13-021 | Jawne oszacowanie stałej, jednoznaczność, niezależność od przedłużenia oraz stabilność względem obu danych. |
| PDE-13-022 | Dodano lemat lem:pde13-trace-parts z dowodem komutacji śladu z dodatnią i ujemną częścią: gładkie aproksymacje, ograniczoność H¹, słaba zbieżność, silna zbieżność śladów. |
| PDE-13-023 | Sprawdzono wzór na gradient ujemnej części i dopuszczalność testu w H_0¹. |
| PDE-13-024 | Znak formy, eliptyczność bez symetrii, Poincaré i wniosek o nieujemności. |
| PDE-13-025 | Zasada porównania: różnica, dodatnia część, zerowy ślad i dopuszczalność testu. |
| PDE-13-026 | Jawna reguła Leibniza dla v² w W^{1,1}; rozpisano oba oszacowania zbieżności kwadratów testów w W^{1,1} i przejście do granicy z b oraz div b. |
| PDE-13-027 | Znak efektywnego członu zerowego, Poincaré, jednoznaczność przez porównanie w obie strony. |
| PDE-13-028 | Wyprowadzono koercywność i istnienie przy c-(div b)/2≥0 bez małości dryfu, ze stałą lambda/(1+C_P²). |

11 zamian blokowych, w tym poprawka zależności PDE-13-004: zastosowanie reguły iloczynów RRC 09 z p=q=2 na relatywnie zwartych kulach, a następnie lokalna całkowalność L² obu składników pochodnej. Zachowano kolejność 38 pierwotnych etykiet, dodano jedną. 58/58 wystąpień odsyłaczy, 34 różne cele, jednoznacznie rozwiązane w RRC 07,09,10,11,12,13; stos środowisk poprawny. Odczytano tezy o częściach dodatnich/ujemnych, iloczynach, gęstości przy brzegu, śladzie, prawym odwrotnym śladu, Poincarém i słabej zwartości. 28/28 pomocniczych skończonych kontroli oszacowań P_epsilon, nie stanowią dowodu. Źródło 866 wierszy. Nie wykonano kompilacji, dedykowanego CI, kontroli wizualnej ani Lean.

Pierwsza lektura: 28 kryteriów, 4/9 sekcji. Kolejna: alternatywa Fredholma dla L:V→V*, faktoryzacja przez zwarte zaburzenie, rzeczywista przestrzeń Hilberta, warunek zgodności, wymiar jądra transponowanego i rezonans. W przyszłej lekturze kontrolnej w lemacie o śladzie można jawnie uzasadnić skończoność miary powierzchniowej przez skończone pokrycie wykresami Lipschitzowskimi. Nie uznawać rozdziału za ustabilizowany.
