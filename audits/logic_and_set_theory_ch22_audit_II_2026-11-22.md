# Logika matematyczna i teoria mnogości — rozdział 22, audyt II (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/logic_and_set_theory/22-drugie-twierdzenie-godla-i-twierdzenie-loba.tex` po audycie I.

## Niezależny audyt matematyczny
1. Ponownie rozróżniono zdanie `Con_T` od metamatematycznego stwierdzenia o niesprzeczności `T`. Wykorzystana reprezentacja `Prf_T` pochodzi z wcześniejszych lematów; w formule użyty jest numerał kodu sprzeczności.
2. Zweryfikowano formalne przejścia `□G→□¬□G`, `□G→□□G` i `□¬□G→(□□G→□⊥)`. Dwa zastosowania (D2) oraz (D1) do tautologii zostały podane jawnie. Wniosek `□G→□⊥` nie korzysta z zasady refleksji `□G→G`.
3. Przy drugim twierdzeniu Gödla ustalono przesłanki efektywnej aksjomatyzowalności i niesprzeczności `T⊇PA`. Zdanie Gödla jest otrzymane z lematu diagonalnego, a przejście `Con_T→G` do sprzeczności stosuje tylko (D1) i niesprzeczność; nie ma ukrytego założenia poprawności semantycznej ani `ω`-niesprzeczności.
4. W twierdzeniu Löba na nowo prześledzono indukowane formuły (D1)--(D3) dla ustalonego punktu stałego `L`. Krok `□L→□φ` jest wewnętrznym twierdzeniem `T`, następnie otrzymuje się `T⊢L`, a dopiero potem korzysta z (D1) dla `L`. Nie ma błędnego rozładowania założeń.
5. Zweryfikowano zgodność korolarium Löba z drugim twierdzeniem Gödla dla `φ=⊥`, bez zbędnego założenia o standardowej prawdziwości `T`.
6. Dla `T+¬Con_T` poprawnie wykorzystano twierdzenie o dedukcji, pełność logiki i niestandardowość świadków; wskazano konkretną podstawę wykluczenia każdego standardowego numerału — lemat o rozstrzyganiu ustalonych kodów `Prf_T` w `Q`.
7. Przykłady i uwagi nie odwracają nieuprawnionych implikacji między niesprzecznością, dowodliwością i poprawnością semantyczną.

## Kontrola redakcyjna i formalna
- Inwentarz zachowany: **3 twierdzenia, 2 lematy, 1 wniosek, 1 definicja, 2 przykłady, 5 uwag, 6 dowodów**.
- **13 etykiet** i **24 odsyłacze** rozdziału są poprawne.
- Główny skrypt: 22 rozdziały, 175 stron w nowym PDF.
- Workflow GitHub Actions: **success**, run `44960003583`, commit `5b258b620546631f9768371c4d9165a0c13d1fbf`.
- Nowe testy regresyjne rozdziału 22: **success**; kontrola katalogu, liczby etykiet i wszystkich odsyłaczy: **success**.
- Z pełnego PDF wyodrębniono **4 strony** rozdziału 22 i wykonano oględziny renderów wszystkich stron. Brak nakładających się elementów, uciętych wzorów lub tekstu.
- W logu pełnego PDF brak `Overfull \\hbox`. Tylko trzy udokumentowane odsyłacze do przyszłych rozdziałów: `ch:downward-ls`, `ch:upward-ls`, `ch:zf-axioms`. Nie dotyczą rozdziału 22.

**Werdykt:** audyt II czysty; nie wykryto kolejnych usterek matematycznych, językowych ani redakcyjnych. **Rozdział 22 stabilny.** Nie zmieniono jego źródła po zakończeniu audytu I. Następnym etapem jest integracja rozdziału 23 i analogiczny audyt.
