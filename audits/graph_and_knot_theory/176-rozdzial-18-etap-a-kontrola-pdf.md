# Audyt 176 — drukowany rozdział 18, etap A (kontrola PDF)

Data: 2026-11-25. Kontynuacja 175. Bez rozszerzania zakresu.

## Weryfikacja poprzedniej wersji
Źródło b6f205965c0afa792cb1405c14df7d8e1fdecf49, blob b4b3d39301ba2e8f1a70ce8f8f947960b0f07da3.
- Pełny audyt 45566192051 SUCCESS: structural-audit i full-book-pdf SUCCESS, trzy kompilacje rzeczywistego tomu.
- Algorytmy 45566192095, terminologia 45566191980, aplikacja 45566192004: SUCCESS dla tego samego SHA.
- Pobrano ZIP artefaktu 14999657885 (graph-and-knot-complete-book-audit), wydobyto PDF (338 stron), logi i plik ostrzeżeń (0 bajtów).
- Wyrenderowano i obejrzano wszystkie 8 stron drukowanego rozdziału 18: strony PDF 156–163, numeracja drukowana 146–153. Sprawdzono trzy rysunki, tablicę rotacji, wzory, odsyłacze i łamanie stron. Nie stwierdzono obcięć tekstu. Rysunki theta i torusa bez nowych usterek. W PDF jest 7 adnotacji odsyłaczy w zakresie rozdziału.
- Na stronie 150 (PDF 160) wykryto rzeczywisty błąd wizualny: dwa łuki różnego koloru w grafie dualnym przecinają się poza wierzchołkiem F3; w grafie pierwotnym brak oznaczenia ściany zewnętrznej.

## Korekta i regresja
Commit 133d9432b9ad8b28edfa4d5458ebe2b9a2dccbb3, blob b1a926c25e6eb8dea68f79eef1322ea76f10f580. Zmieniono cztery wygięcia łuków z 27 na 12 stopni, oznaczono ścianę F3. Treść twierdzeń i dowodów pozostaje niezmieniona.
GKT-18-FIG-01, test_gkt18_dual_figure.js, commit 317631851bb3f78c28e678abf7be980cb7bb9c12. Wykonano funkcję testową na dwóch pobranych wersjach źródła w izolacie JS. Poprzednia wersja FAIL (nakładające się stożki kierunków stycznych), nowa PASS (suma maksymalnych wygięć 24 stopnie < separacja 42.501011 stopnia; cztery łuki i oznaczenie F3). Jest to kontrola źródłowa, nie dowód bezprzecięciowości całego renderowanego rysunku; wymagane ponowne oględziny PDF.

## Bramka
Dla commitu korekty: terminologia 45567090919 SUCCESS; pełny audyt 45567090921, algorytmy 45567091069 i aplikacja 45567090879 w toku w chwili zapisu. Nie oglądano jeszcze PDF po korekcie i nie przenoszono poprzedniego PASS na nowy blob. Etap A nadal otwarty. Kolejna iteracja: obejrzeć rzeczywisty nowy PDF, w tym poprawiony rysunek, ponowić regresje i dopiero po spełnieniu bramki zamknąć A. Następnie niezależny etap B.
