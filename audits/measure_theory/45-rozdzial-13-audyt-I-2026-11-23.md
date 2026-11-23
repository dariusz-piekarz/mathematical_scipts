# Audyt XLV — rozdział 13 „Zamiana zmiennych w całce Lebesgue'a” — audyt I

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. Wyłącznie R13.

## Punkt wznowienia
Odczytano stan bieżącej gałęzi względem commitu stabilizacyjnego R12 `f96cd75edff5112e686697f2b487be2188457398`. Porównanie wykazało późniejsze zmiany R13 (44 dodane, 19 usuniętych wierszy) i nowy `tools/test_measure_theory_ch13.py`. Raport XLV jeszcze nie istniał. Poprzedni audyt XLIV stabilizował R12. Bieżący blob R13: `ed8e399441bbf76f8f5f5f88943e2d1fa74c0b31`. R01–R12 pozostają stabilne na podstawie wcześniejszych raportów; nie audytowano ich ponownie. R14–R31 nietknięte.

## Zakres rzeczywiście wykonanej kontroli
Odczytano cały rozdział (542 wiersze), `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/measure_theory.tex`, kontekstowo `books/pl/integration_theory.tex` oraz test R13. Zweryfikowano logiczny przebieg ośmiu środowisk dowodów, definicję miary obrazowej, niezmienniczość translacji/ścinania, zachowanie zbiorów zerowych, liniowy wzór objętości, lokalne oszacowanie sześcianu przez twierdzenie Banacha, dowód równości miar przez sześciany diadyczne i twierdzenie π–λ, uzupełnienie miary, przykłady współrzędnych biegunowych/walcowych/sferycznych, transformację gęstości i dwa kontrprzykłady dotyczące hipotez. Weryfikacja opiera się na czytaniu źródła; nie jest to zastępstwo kompilacji ani uruchomienia testów.

## Konkretne ustalenia
1. **Naprawa zastana, nie przypisana temu audytowi:** w bieżącym źródle dowód transformacji gęstości poprawnie stosuje wzór do `h(x)=χ_{Φ^{-1}(B)}(x)w(x)` na `U`, a nie do funkcji na niewłaściwej dziedzinie. Warto zachować ten fragment.
2. **Naprawa zastana:** rozumowanie z klasą π na półotwartych sześcianach diadycznych jest jawnie lokalizowane do skończonych miar `τ_C,ρ_C`. Równość dla `E∩C` i przeliczalne rozłączenie pokrycia `U` są obecne; nie stwierdzono tu błędu wymagającego poprawki.
3. **Naprawa zastana:** lokalny lemat sześcianowy wyprowadza dolne zawieranie przez zwężenie `T_y`, bez zakładania jeszcze twierdzenia o zamianie zmiennych. Pozwala to uniknąć błędnego koła.
4. **Przypadki brzegowe:** dla zbiorów zerowych argument korzysta z miary zewnętrznej i zupełności Lebesgue'a; dla funkcji nieujemnych dopuszcza wartości `+∞`; dla funkcji zespolonych najpierw dowodzi całkowalności modułu. Rozróżnienie wzoru dla dyfeomorfizmu od wzoru z krotnością włókien jest prawidłowe.
5. **Terminologia i odsyłacze:** 16 etykiet w R13, 14 lokalnych lub zewnętrznych użyć `ref/eqref`; brak powtórzonych etykiet wewnątrz R13. Sprawdzono zapis `\\chi_A` i brak alternatywnych oznaczeń funkcji charakterystycznych. Zewnętrzny odsyłacz `thm:tonelli-12` wymaga kontekstu R12 i istnieje w zatwierdzonym rozdziale.
6. **Uwagi redakcyjne, niewymagające samowolnego rozszerzania:** zdanie o „dodatniej odległości od ∂U” w lemacie Lipschitza jest poprawne dla właściwego U, ale dla U=ℝᵈ wymaga zwykłej konwencji `dist(Q,∅)=+∞`. Można zastąpić je precyzyjniejszym `Q_j⊂⊂U` przy następnej korekcie. W opisie klasy π występuje przecinek zamiast kropki po „jeden zawiera się w drugim”; jest to drobna usterka interpunkcyjna.
7. **Weryfikacja techniczna niezamknięta:** nie uruchomiono w tej iteracji kompilacji LaTeX, testów Python ani workflow GitHub Actions. Nie obejrzano wyrenderowanego PDF i podpisów TikZ. Te czynności są otwarte i nie wolno na tej podstawie deklarować stabilności.

## Mierzalny postęp i decyzja
Pierwszy niezależny audyt R13 dokumentuje 542 wierszy źródła, osiem dowodów, 16 etykiet, 14 odsyłaczy i weryfikację trzech wcześniejszych merytorycznych napraw. W tej iteracji **nie edytowano źródła R13**, aby nie kolidować z zastanymi, niedawno zapisanymi poprawkami. Zapisano jeden nowy raport XLV.

**R13 — NIESTABILNY / W AUDYCIE.** Do formalnej stabilizacji potrzebne są testy, rzeczywista kompilacja, kontrola wizualna rysunku i niezależny czysty audyt po ostatniej poprawce. **Następna iteracja: XLVI / R13 II**, nie R14.
