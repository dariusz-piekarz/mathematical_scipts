# Algebra liniowa — rozdział 20, audyt IV (stabilizacyjny)

**Data:** 21 listopada 2026  
**Źródło:** \`chapters/pl/linear_algebra/20-dzielniki-elementarne-i-bloki-pierwotne.tex\`.  
**Poprzednie audyty:** I (nowy rozdział i poprawa tytułu), II (korekta przykładu), III (czysty).

## Ostateczna kontrola

1. **Poprawność i kompletność.** Twierdzenie CRT, istnienie i jednoznaczność bloków pierwotnych, rekonstrukcja czynników niezmienniczych oraz formuły na jądra \`p(T)^k\` zachowują wszystkie założenia. Nigdzie nie założono algebraicznego domknięcia \`K\`.
2. **Dopasowanie do wcześniejszych rozdziałów.** Nie powielono dowodu ogólnego rozkładu pierwotnego z 16 ani klasyfikacji Jordana z 17. Wykorzystano już dowiedzioną postać Frobeniusa z 19, zachowując dotychczasowe etykiety.
3. **Przypadki graniczne.** Wymiar zero, brak bloków określonego \`p\`, \`k=0\`, pojedynczy składnik CRT, bloki stopnia 1, wielomiany nierozkładalne wyższego stopnia i dodatnia charakterystyka są obsłużone.
4. **Przykłady.** Dla \`diag(1,1,2)\` niepoprawna propozycja \`p²,q\` ma wprawdzie prawidłowy iloczyn \`p²q\`, ale nie tworzy łańcucha podzielności oraz daje błędne \`m=p²q\` zamiast \`pq\`. Obecny tekst to wyjaśnia; pozostałe rachunki nie wymagają poprawek.
5. **LaTeX i referencje.** 22 różne etykiety, 23 odsyłacze, 7 otwarć i 7 zamknięć środowiska \`proof\`, brak niezdefiniowanych odsyłaczy w kompilacji. Tytuł z \`K[t]\` ma poprawnie zgrupowany nawias.
6. **Regresje i wydruk.** GitHub Actions [44943090831](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943090831) zakończył się **SUCCESS**, także dla testu nowych dzielników elementarnych. Finalny eksport zawiera **7 stron**, wszystkie niepuste; analiza PyMuPDF nie wykazała bloków wychodzących poza obszar stron. Weryfikacja tekstu PDF potwierdza obecność poprawionego argumentu \`p²,q\`.

## Decyzja

**Audyt IV czysty** — drugi kolejny pełny przebieg bez nowych poprawek po audycie II. **Rozdział 20 STABILNY po czterech audytach.** Stan algebry liniowej: **01–20 stabilne**. Następny etap: przygotowanie rozdziału 21 w osobnym cyklu, bez rozszerzania zamkniętych rozdziałów.
