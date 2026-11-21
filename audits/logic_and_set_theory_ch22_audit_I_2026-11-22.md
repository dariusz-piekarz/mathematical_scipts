# Logika matematyczna i teoria mnogości — rozdział 22, audyt I

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/logic_and_set_theory/22-drugie-twierdzenie-godla-i-twierdzenie-loba.tex`

## Materiał wyjściowy i integracja
Źródłem była wcześniejsza wersja rozdziału 22 w pełnym skrypcie (rozdziały 01–44) oraz odrębne źródła LaTeX modułów „Drugie twierdzenie o niezupełności” i „Twierdzenie Löba”. Zintegrowano je z przyjętą numeracją, składem i odsyłaczami obecnego skryptu. Nie dodawano nowych wyników matematycznych.

Rozdział został dołączony do `books/pl/logic_and_set_theory.tex` i `catalog/books.json`. Zaktualizowano workflow `.github/workflows/logic-and-set-theory-chapter.yml`, który obejmuje rozdziały 01–22, oraz dodano `tools/tests/test_logic_and_set_theory_ch22.py`.

## Kontrola matematyczna
1. **Zdanie niesprzeczności:** `Con_T = ¬Bew_T(overline(b))`, gdzie `b` jest kodem zdania `0=S(0)`. Odróżniono liczbę `b` od jej numerału; wskazano związek z klasą `Π₁` i interpretacją w modelu standardowym.
2. **Znaczenie metamatematyczne:** udowodniono równoważność prawdziwości `Con_T` w standardowej arytmetyce i niesprzeczności `T`, wykorzystując definicję kodu dowodu i zasadę eksplozji.
3. **Wewnętrzne `□G→□⊥`:** każde zastosowanie (D1), (D2), (D3) jest rozpisane; rozdzielono `□¬□G` od `□□G`; nie zastosowano nieuprawnionego `□φ→φ`.
4. **Drugie twierdzenie Gödla:** jawnie zastosowano lemat diagonalny z `Q`, wyprowadzono `Con_T→G`, a następnie sprzeczność z niesprzecznością `T` przy użyciu (D1). Nie jest wymagane ani założenie `ω`-niesprzeczności, ani poprawność semantyczna `T`.
5. **Twierdzenie Löba:** formalna formuła punktu stałego ma postać `Bew_T(x)→φ`, a nie niepoprawny zapis `□x`; szczegółowo uzasadniono etapy `□L→□φ`, `L`, `φ`. Niesprzeczność nie jest założeniem tego twierdzenia.
6. **Modele niestandardowe:** z niedowodliwości `Con_T` wykazano niesprzeczność `T+¬Con_T`, istnienie modelu z twierdzenia o pełności i niemożliwość istnienia standardowego świadka kodu dowodu sprzeczności.
7. **Zakres twierdzeń:** odróżniono niesprzeczność od poprawności semantycznej, formalnego predykatu dowodliwości od arbitralnej reprezentacji oraz wyniki wewnętrzne od założeń metateorii.

## Usterki skorygowane
- Stara samodzielna wersja modułu używała niedokładnego zapisu predykatu dowodu zastosowanego do kodu, bez jawnego numerału. W scalonym rozdziale zastosowano konsekwentnie `\overline b`.
- Podczas integracji dwie odrębne uwagi o zakresie wyników i algorytmach zostały pierwotnie połączone. W ramach audytu I rozdzielono je ponownie, zachowując pięć uwag z wcześniejszego rozdziału.
- Usunięto nieaktualny cel odsyłacza do twierdzenia o pełności; właściwa etykieta to `thm:godel-completeness`.

## Inwentarz i walidacja
- 3 twierdzenia, 2 lematy, 1 wniosek, 1 definicja, 2 przykłady, 5 uwag, 6 dowodów.
- 13 unikatowych etykiet, 24 odsyłacze do istniejących celów.
- Test struktury, katalogu i odsyłaczy w GitHub Actions: PASS.
- Testy regresyjne rozdziału 22: PASS.
- Pełna kompilacja i oględziny nowego PDF wymagają końcowego potwierdzenia w workflow; nie deklarujemy sukcesu na podstawie samych testów.

**Status:** źródło po audycie I; po zakończeniu pełnego CI i kontroli PDF przeprowadzić audyt II.
