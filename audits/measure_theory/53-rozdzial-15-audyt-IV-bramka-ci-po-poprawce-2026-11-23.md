# Audyt LIII (53) — rozdział 15: wymuszenie technicznej bramki po poprawce LI

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Zakres audytu:** wyłącznie R15 — „Dualność, wypukłość i słaba zbieżność w przestrzeniach Lp”. **Status: W STABILIZACJI**.

## Rzeczywisty punkt wznowienia

Pobrano bieżące źródło R15, raport L (50), trzy raporty LI (51), raport LII (52), istniejący test `tools/tests/test_measure_theory_ch15_li_gate.py`, workflow R15 oraz aktualne commity. Najnowsza poprawka kanonicznego źródła R15 dotyczy przykładu `g=x^{-\alpha}`: rozszerza przypadek `\alpha q\ge1` i podaje jawny ciąg funkcji normujących `f_N`, dla których wartości całek rosną bez ograniczenia. W raporcie LII potwierdzono niezależne testy i odsyłacze, ale nie uzyskano aktualnego, kompletnego CI po tej poprawce. Nie wolno opierać stabilizacji wyłącznie na starszym zielonym przebiegu dla innego bloba.

**Aktualny blob R15 po ponownym odczycie:** `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab`. W tym audycie nie zmieniono tekstu rozdziału ani etykiet.

## Mierzalny postęp — rzeczywista poprawka bramki

Zmieniono wyłącznie `.github/workflows/measure-theory-ch15.yml`:
1. Dodano `tools/tests/test_measure_theory_ch15_li_gate.py` do filtrów `push.paths`, tak aby zmiana nowego testu powodowała uruchomienie kontroli R15.
2. Rozszerzono job `chapter-15-finite-and-source`: po wcześniejszym `python3 tools/test_measure_theory_ch15.py` wykonuje również `python3 -m unittest discover -s tools/tests -p test_measure_theory_ch15_li_gate.py -v`.
3. Pozostawiono istniejący job kompilacji izolowanego R15, pełnej książki, kontroli odsyłaczy, granic stron i publikacji PDF. Zmiana workflow uruchamia oba joby dla aktualnego checkoutu gałęzi.

**Commit zmiany workflow:** [e0ef0e6bfce904d0229e5b83834958851e88ac9d](https://github.com/dariusz-piekarz/mathematical_scipts/commit/e0ef0e6bfce904d0229e5b83834958851e88ac9d). Po zapisie ponownie odczytano plik i zweryfikowano pełną zgodność treści oraz SHA bloba `08d5bcc81eab21cd5030ec4d098eb4779925da66`.

## Weryfikacje i ograniczenia

- Ponownie odczytano najnowszy blob źródła R15: `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab`. Brak edycji źródła podczas tej iteracji.
- Istniejące audyty LI i LII opisują pełne dowody, testy liczbowe, etykiety i poprawiony przykład; nie deklaruje się tutaj ich ponownego wykonania jako własnych testów.
- Wykonano rzeczywisty odczyt listy przebiegów GitHub Actions i próbę odczytu przebiegów dla commita e0ef0e6b. W chwili kontroli nie uzyskano potwierdzonego końcowego PASS **obu jobów dla nowego commita**; pusta lista powiązanych przebiegów nie jest równoznaczna z sukcesem lub porażką.
- W tej iteracji **nie kompilowano lokalnie PDF i nie oglądano nowego renderingu**. Poprzedni PDF z audytu L odpowiada wcześniejszemu źródłu, więc nie zastępuje nowej weryfikacji.
- Nie dodano nowych twierdzeń ani przykładów, nie scalano `books/pl/integration_theory.tex`, nie modyfikowano R01–R14 ani R16–R31.

## Formalna decyzja

**R15 — W STABILIZACJI; techniczna bramka otwarta.** Wprowadzono mierzalną poprawkę infrastruktury, która uruchamia po ostatniej zmianie także niezależną regresję LI/LII. Nie wolno zatwierdzić rozdziału jako stabilnego, dopóki nie będzie potwierdzonego 2/2 SUCCESS, kompletnego PDF dla aktualnego bloba, oględzin wszystkich stron i dodatkowej czystej kontroli bez kolejnych edycji.

**Następna iteracja:** ponownie wyłącznie R15 — odczytać aktualne przebiegi workflow, sprawdzić logi obu jobów, pobrać i obejrzeć aktualny PDF, potwierdzić SHA i dopiero wtedy zdecydować o stabilizacji. Nie przechodzić do R16.
