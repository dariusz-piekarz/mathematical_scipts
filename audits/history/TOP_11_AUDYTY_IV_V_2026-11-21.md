# Topologia algebraiczna — TOP-11, audyty IV–V i kontrola DG-17

**Data:** 2026-11-21  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**AT-11:** `chapters/pl/algebraic_topology/11-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`, blob `a808e458f2e8f447fa00298b34723ed8f9a72837`, 2891 wierszy.  
**DG-17:** `chapters/pl/differential_geometry_and_topology/17-przeciecia-dualnosc-i-klasy-charakterystyczne.tex`, blob `39905ac1d36dcf0a0c99a945e1111007fa660bca`, 3110 wierszy.

## Audyt IV — założenia i rachunki

W istniejącej definicji indeksu zera pola jawnie podano gładką rozmaitość oraz ciągłe pole z izolowanym zerem. Związek indeksu z wyznacznikiem różniczki wymaga dodatkowo regularności `C^1` i odwracalności różniczki. W twierdzeniu Poincarégo–Hopfa zapisano założenie gładkości pola potrzebne do przepływu i perturbacji. Zachowano wszystkie wcześniejsze etykiety i dowody.

Poprawka: `c2db9f9a5ff8e20d3a994e24329820289d6c8549`.

## Porównanie z geometrią różniczkową

Niezależna inspekcja DG-17 potwierdziła, że starszy, równoległy tekst zawierał te same dwie luki matematyczne w wymiarze zero: założenie `e(E)=1` niezależnie od orientacji zerowego włókna oraz skrót `dla n=0 obie strony liczą punkty` bez kontroli znaków. Poprawki AT-11 przeniesiono na odpowiednie miejsca DG-17, wraz z założeniami przy indeksie i chirurgii. Nie zastąpiono ani nie skrócono bogatszego materiału DG-17, nie wykonano automatycznego scalania.

Commit DG-17: `50cbd1327fbd3ed0a228c617e149a80bbe444c02`.  
Test zgodności obu tomów: `58d5bd6e972220cffe120ff872efcd4894701000`, sprawdzający identyczność konwencji rank-zero i indeksu oraz arytmetykę znaków.

## Audyt V — kontrola niezależna źródeł

Po ostatnich poprawkach pobrano aktualne pliki bezpośrednio z istniejącej gałęzi GitHub i ponownie zweryfikowano ich strukturę:

- AT-11: **50 etykiet, 50 unikalnych**, zrównoważone wszystkie środowiska LaTeX.
- DG-17: **57 etykiet, 57 unikalnych**, zrównoważone wszystkie środowiska LaTeX.
- W obu źródłach występują zgodne wzory `u_E=e(E)=ε`, `Σ_x ε_x²=#M=χ(M)`, precyzyjne założenie gładkości pola Poincarégo–Hopfa i osadzenie chirurgiczne we wnętrzu rozmaitości.
- Brak wykrytych dawnych niepożądanych sformułowań terminologicznych („unia”, „sekwencja”, „injekcja”, „tensorowanie”).
- Niezależny test wzoru na brzeg iloczynu kapowego objął 420 kombinacji sympleksów i stopni, bez błędów; regresję dodano do testów rozdziału AT-11.

## GitHub Actions

Dla commita AT-11 `c2db9f9a`, przed synchronizacją DG-17, cztery kontrole miały potwierdzone `completed/success`:
- TeX TOP-01–12: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926456075
- Aplikacja: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926456138
- AT–DG–AG: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926456081
- Porównanie AT11–DG17: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926456116

Kontrole porównawcze i aplikacyjne po zmianie DG-17 oraz nowym teście na commitach `50cbd1327` i `58d5bd6e` pozostawały w toku w chwili ostatniego sprawdzenia. Nie deklarujemy jeszcze ich wyniku.

**Decyzja:** zakończono merytoryczne audyty I–V TOP-11. Stabilność końcową wolno potwierdzić po zaliczeniu CI dla aktualnej pary AT-11/DG-17. Do tego czasu nie należy rozpoczynać TOP-12. Automatyzacje pozostają wyłączone.
