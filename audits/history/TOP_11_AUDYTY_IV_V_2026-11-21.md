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

## Uzupełnienie: sprawdzone zakończenie porównania AT–DG

Po opracowaniu raportu zakończyły się dodatkowe uruchomienia:
- [AT11–DG17 comparative audit, commit `58d5bd6e`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926606563) — **completed/success**. Obejmuje nowe testy zgodności konwencji w obu tomach i pełną kompilację porównawczą.
- [AT21–DG17 relative Euler and boundary Poincaré–Hopf, commit `50cbd132`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926585115) — **completed/success**.
- [AT–DG–AG, commit `50cbd132`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926585140) — **completed/success**.

Wspólny workflow aplikacji ujawnił osobną regresję w równolegle rozwijanym LST-10: dwa odsyłacze do jeszcze nieistniejących etykiet. Nie wyciszono walidatora: poprawiono źródło LST-10 w `1f452b86`, a następnie zawężono listę dokumentowanych odsyłaczy przyszłych z trzech do jednego w `8f21df29`. Nowe uruchomienia aplikacji i LST pozostawały w toku podczas tej aktualizacji.

**Stan rozdziału:** audyty merytoryczne I–V są czyste; kompilacje TOP-01–12 i porównawcze AT–DG są zielone. Pełne zamknięcie formalne czeka wyłącznie na potwierdzenie wspólnej walidacji po poprawce niezależnego LST-10.

## Domknięcie audytu TOP-11

Ostateczne potwierdzenie: [Mathematical library application checks — commit `1f452b86`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926765108) zakończył się `completed/success` po usunięciu dwóch błędnych odsyłaczy LST-10. Potwierdzono również sukces:
- [TOP-11–12 TeX — `c2db9f9a`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926456075),
- [AT11–DG17 — `58d5bd6e`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926606563),
- [AT21–DG17 — `50cbd132`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926585115),
- [AT–DG–AG — `50cbd132`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44926585140).

**Decyzja matematyczna i techniczna dla TOP-11: stabilny po audycie V.** Jego źródło pozostaje na istniejącej gałęzi. Osobny workflow `Logic and set theory chapters 01-10 validation` po zawężeniu docelowej listy przyszłych etykiet był jeszcze w trakcie kompilacji pełnego skryptu LST-01–10 i nie wpływa na to, że wszystkie kontrole dotyczące TOP-11 zakończyły się sukcesem. Do audytu TOP-12 przechodzimy dopiero po domknięciu bieżącej iteracji.
