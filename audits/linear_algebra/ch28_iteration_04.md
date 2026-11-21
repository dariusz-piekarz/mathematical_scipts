# Algebra liniowa — rozdział 28, audyt IV (drugi czysty, stabilizacyjny)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/28-uklady-z-wymuszeniem-i-funkcje-przejscia.tex`  
**Nieprzerwany blob źródłowy:** `945b4ecd36bfa2f0ccbffe9c4236d3ba2eafdbf0`, identyczny jak w czystym audycie III.

## Powtórny audyt matematyczny z innym zestawem kontroli

1. **Zgodność reprezentacji.** Wzór (G(z)=D+C(zI-A)^{-1}B), jego rozwinięcie Laurenta i ciąg parametrów Markowa muszą być zgodne z Hankelową faktoryzacją (H=\mathcal O_n\mathcal K_n) z LA-27. Sprawdzono wprost indeksowanie (H_{ij}=CA^{i+j}B) dla (i,j\ge0).
2. **Transformacja podobieństwa.** Dla dowolnej odwracalnej macierzy (T), podstawienia (A'=T^{-1}AT), (B'=T^{-1}B), (C'=CT), (D'=D) nie zmieniają funkcji przejścia ani parametrów Markowa: ((zI-A')^{-1}=T^{-1}(zI-A)^{-1}T). Jest to zgodne z jednoznacznością realizacji minimalnej w LA-27.
3. **Warunki na mianownik.** W rozdziale dobrze rozróżniono występowanie wartości własnej A od występowania bieguna G; redukcja po skróceniu wspólnych czynników p,q wymaga obserwowalności i sterowalności, co zostało wykazane przez PBH bez założenia diagonalizacji.
4. **Przypadki osobliwe.** W twierdzeniu towarzyszącym uwzględniono n=1 i q=0. Gdy q=0 i n>0, realizacja nie jest minimalna, bo układ bez stanów i z D=d realizuje stałą funkcję.
5. **Oszacowanie odpowiedzi.** Dla A Hurwitza albo Schura wyprowadzono właściwą kontrolę normy jądra splotu. Stałe M i α/r nie zależą od sterowania ani od stanu początkowego. W przypadku L∞ nierówność dla y jest poprawnie formułowana prawie wszędzie.
6. **Dowody i cytowania.** Kontrola każdego nieoczywistego przejścia: zastosowanie e^{tA}, zamiana całki i różniczkowania, przesunięcie indeksu przy Z, szereg Neumanna, wzór na adjugowaną macierz, kryterium PBH, bloki Jordana oraz faktoryzacja Hankela. Każde uzasadnione zostało w tekście lub przez wcześniejszy odsyłacz.

## Niezależne testy i skład

- **200** losowych dokładnych przypadków rozmiarów 2,3,4: identyczność transmitancji po podobieństwie, niezmienniczość CA^kB i faktoryzacja H=OK — PASS.
- **60** osobnych kontroli geometrycznego oszacowania dyskretnej odpowiedzi przy stabilnych parametrach wymiernych — PASS.
- Inspekcja stron 3, 5 i 6 w rozdzielczości 150 DPI (oraz całościowego montażu wszystkich 7 stron): poprawny układ równań, pełne marginesy, brak kolizji i przycięć; 0 bloków poza stroną.
- Zielona walidacja dokładnie tego źródła: [GitHub Actions #44953371224](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44953371224), SUCCESS, także pełny PDF i eksport najnowszego rozdziału.

## Wynik i decyzja

**Audyt IV czysty; drugi kolejny czysty audyt po III.**
Źródło rozdziału 28 nie zostało zmienione między III i IV.
**Rozdział 28: STABILNY**. Aktualny status LA-01–28: stabilne.
W pliku głównym książki uaktualniono jedynie komentarz o statusie.
Po tym commicie należy dodatkowo sprawdzić świeży przebieg CI,
aby niezależnie potwierdzić poprawność struktury i kompilacji.
Następna planowana część: LA-29 — grassmanniany, z wykorzystaniem DG-04.
