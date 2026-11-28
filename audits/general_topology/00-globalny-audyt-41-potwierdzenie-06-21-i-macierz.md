# Topologia ogólna — audyt globalny 41: potwierdzenie +1 po naprawie rysunków 06 i 21

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Badane bloby niezmienione w całym cyklu po korekcie:**
- rozdział 06: `71d7b30abb97286b7c64ddd5e369ec9f69ea1ff5`;
- rozdział 21: `eae0bef9c2357189e1bdb7c9398b845fe7347c7b`.

**Audyt 1/2:** [globalny 39](00-globalny-audyt-39-reaudyt-06-21-czysty-1.md).
**Audyt 2/2:** [globalny 40](00-globalny-audyt-40-reaudyt-06-21-czysty-2.md).
Ten dokument jest **dodatkowym, odrębnym sprawdzeniem +1**. Nie dokonuje kolejnych zmian źródłowych.

## I. Niezależna kontrola kontrprzypadków i zależności

1. **Sieci zamiast ciągów w rozdziale 06:** w topologii koprzeliczalnej na nieprzeliczalnej przestrzeni każdy ciąg zbieżny do x jest ostatecznie stały x; tymczasem skierowanie wszystkich par `(C,a)` z C przeliczalnym oraz a spoza C tworzy sieć, która unika każdego przeliczalnego wyjątku i zbiega do x. Definicja podsieci jest oparta na ostatecznej współkońcowości, nie na monotoniczności φ. Nie wprowadzono tu niejawnie pierwszego aksjomatu przeliczalności.
2. **Właściwe filtry na X=∅:** nie istnieją, bo `X∈𝔽` i `∅∉𝔽` byłyby sprzeczne. W twierdzeniu `thm:topog-sieci-filtry` wybór `(F,a)` jest dokonywany tylko dla rzeczywiście istniejącego filtru właściwego; przypadek pustej dziedziny jest pustą kwantyfikacją, a nie luką.
3. **Hiperprzestrzeń Vietorisa dla X=∅:** `𝒦(∅)=∅`; przestrzeń pusta jest Hausdorffa, zwarta i zupełna w jedynej metryce. Żaden dowód o zwartości i zupełności `𝒦(X)` nie wymaga wybrania elementu tej przestrzeni, jeśli zbiór jest pusty.
4. **Hiperprzestrzeń Fella dla X=∅:** `𝔽(∅)={∅}`; jest zwarta, również dla braku T1. Dowód przez podbazę i własność skończonych przecięć kompaktów `C_j` ma poprawne znaczenie dla `I=∅`, `J=∅` i pustych C_j — hipotetyczne pokrycie bez skończonego podpokrycia nie może istnieć dla singletonu.
5. **Zbieżność Fella nie oznacza zbieżności w metryce Hausdorffa:** dla `K_n={0,n}` w R zachodzi `K_n→{0}` w topologii Fella, lecz `d_H(K_n,{0})=n`. Utrzymano to rozróżnienie i poprawne hipotezy równoważności Vietorisa/Fella w przypadku zwartej Hausdorffa X.
6. **Zgodność odsyłaczy między rozdziałami:** rozdział 21 odsyła do 07 (ultrafiltry), 14 (lokalna zwartość) i 18 (przestrzenie odwzorowań), a użyte etykiety istnieją w bieżącym katalogu 01–26. Rozdział 06 poprzedza te wyniki i nie korzysta z nich w sposób kołowy.
7. **Geometria diagramów:** przesunięte etykiety mają dodatni odstęp tekstowy ok. 5,51 pt (6.1) oraz 5,34 pt (21.1), zmierzony w post-edycyjnym PDF. Ich przesunięcie nie dotyczy twierdzeń ani danych zbiorów w przykładzie Hausdorffa.

## II. Weryfikacja integralności dowodów i macierzy

Na bieżącej gałęzi odczytano ponownie oba kompletne pliki źródłowe i porównano je z commitem przed korektą diagramów `73bfc3fb9f83c4e22afad138237a395fe50363ed`:

| Rozdział | Stary blob | Nowy blob po korekcie rysunku | `proof` | Wszystkie teksty `proof` | Etykiety i odsyłacze |
|---|---|---|---:|---|---|
| 06 | `365204000d0d5b21f213132e58b71aa48db3910e` | `71d7b30abb97286b7c64ddd5e369ec9f69ea1ff5` | 18 | **18/18 identyczne** | 45 etykiet, 16 odsyłaczy — identyczne |
| 21 | `a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b` | `eae0bef9c2357189e1bdb7c9398b845fe7347c7b` | 15 | **15/15 identyczne** | 31 etykiet, 9 odsyłaczy — identyczne |

**Aktualizacja interpretacji historycznych rejestrów:**
- [globalny 33](00-globalny-audyt-33-macierz-dowodow-01-10.md), wiersze **06-01 … 06-18**, wskazuje stary blob, bo był poprawnie zamrożony na wcześniejszym commicie. Przypisanie 18 wierszy do **nowego bloba** uzasadniają: identyczność literalnego tekstu każdego dowodu, brak zmian etykiet i dowodów, bieżący reaudyt matematyczny 39/40 i ten audyt +1.
- [globalny 35](00-globalny-audyt-35-macierz-dowodow-19-26.md), wiersze **21-01 … 21-15**, analogicznie wskazuje stary blob i zachowuje historyczną prawdziwość pomiaru; ten dokument dodaje jawny most między starą a nową wersją.
- **Wszystkie 325 unikatowych ID dowodów są zachowane**; po zmianach geometrycznych przybyło **zero** dowodów i **zero** nowych odsyłaczy. Nie edytujemy starych raportów, aby nie zacierać historii źródeł.

## III. CI i PDF

- [45133887910](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133887910): `completed/success` po obu korektach TikZ; pełna książka 188 stron oraz samodzielne PDF 06 i 21.
- [45134198801](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45134198801): `completed/success` po naprawie składni obu testów regresji; obydwa kroki walidacji 06 i 21 mają `success`.
- [45134587477](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45134587477): `completed/success`, potwierdza także dołączenie raportu globalnego 38 do repozytorium.
- Nowe workflow po raportach 39–41 należy sprawdzić osobno; **nie deklarujemy niezaobserwowanych sukcesów**.

## IV. Werdykt

**Rozdziały 06 i 21: stabilizacja 2 czyste + 1 dodatkowy audit na nowych blobach ZAKOŃCZONA w zakresie matematycznym, źródłowym i wizualnym.** W obu przypadkach nie wykryto nowych błędów matematycznych, a rzeczywisty poprawiony PDF i nowe regresje zostały zweryfikowane w zakończonym sukcesem workflow `45134198801`.

**Końcowy audyt globalny całych 26 rozdziałów pozostaje otwarty** do czasu potwierdzenia CI końcowej głowicy i niezależnego przeglądu pozostałych ryzyk matematycznych. Ten wynik nie oznacza formalizacji w Lean ani dowodu automatycznego 325 twierdzeń.
