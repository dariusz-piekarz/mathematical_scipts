# Algebra liniowa — rozdział 29, audyt II

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/29-grassmanniany.tex`.  
**Źródło przed korektą:** `967bc1908541c7ec56c66528a34b301b30ad672c`.

## Znaleziona usterka CI i korekta
- [Pierwszy workflow LA-29](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44954172079) zakończył się FAILURE na kroku **Validate linear algebra chapters, imports, catalog and terminology**, konkretnie na wierszu 551: dawna nazwa `Relacja Plückera` została odrzucona przez kontrolę słowa „relacja”.
- W rozdziale opisano w istocie jedno równanie Plückera w Gr(2,4), więc użyto precyzyjnego określenia **„równanie Plückera”** i odpowiednich odmian w treści dowodu; nie zmieniono formuł, znaków ani tez.
- Poprawiono odziedziczoną niepoprawną polską postać `injektywna` na `iniektywna`.
- Nie rozszerzano zatwierdzonego zakresu matematycznego; nowy chapter jest wciąż kopią trzech sekcji DG-04 z własnymi odsyłaczami i etykietami.

## Matematyka i testy
- Zweryfikowano równanie `p12 p34 - p13 p24 + p14 p23=0` dla decomposable bivectors przez rozwinięcie \(\xi\wedge\xi\).
- Wykonano 500 niezależnych dokładnych testów Gr(2,4) na macierzach całkowitych (klasy Plückera, mapy wykresowe i zmiana bazy), wszystkie PASS.
- Kontrola rysunków i pełnego PDF nastąpi po nowym poprawnym przebiegu CI.

## Decyzja
Audyt II wykrył poprawkę językową i problem CI, więc **nie jest czysty**. Wymagane kolejne audyty.
