# Moduł 15B — iteracja 17 (zatwierdzone rozszerzenie Fubiniego)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia raport 16, 24e9ac9bf054553e825f4a02b7bfc7bc1dd63751. Źródło 00d62e2ee66545c0b0ec9e5f1272729bbb932fe0, testy 05b348c91050595148104c829066e8db056a8b75. Rozpoczęto niezależny przegląd nowych argumentów: mnożniki, Orlicz–Pettis (Baire i kryterium Cauchy'ego), półwariacja (ciągłość miary i rozłącznianie), zbieżność i restrykcja Gelfanda. Nie stwierdzono błędu w głównych argumentach; dalszy audyt redakcyjny wymagany. CI dla tej wersji 45349423014: success, 15/15 testów, trzy przebiegi pdflatex, 120 stron kontekstu, kontrola odsyłaczy zaliczona. Artefakt 14900020651 pobrano; nie wykonano nowych oględzin PDF przed rozszerzeniem.

## Nowe rozszerzenie zaakceptowane przez użytkownika
- Fubini Gelfanda: całkowalność na uzupełnionym produkcie i całkowalność prawie wszystkich przekrojów poza wspólnymi mierzalnymi zbiorami zerowymi. Całki iterowane są całkowalne Gelfanda, równości dla wszystkich prostokątów.
- Fubini Dunforda: redukcja do Gelfanda przez J_X i przestrzeń testującą X'. W szczególności zewnętrzna całka jest Gelfanda w X'', nie automatycznie Dunforda w X''''.
- Fubini Pettisa: całkowalność przekrojów oraz produktu. Reprezentacja wszystkich całek po podzbiorach przestrzeni zewnętrznej wynika z prostokątów C x B i A x D, a nie jedynie z równości całek na całej przestrzeni.
- Wystarczający warunek całkowalności przekrojów: ośrodkowa przestrzeń testująca i całkowalny mierzalny majorant normy, z dowodem usuwania przeliczalnej rodziny zbiorów wyjątkowych. Dla Dunforda przestrzenią testującą jest X', a dla Pettisa dodatkowo refleksywność X. Nie zakłada się mierzalności samej normy h.
- Kontrprzykład: f(s,t)=k(t)e_s w l2([0,1]), k(0)=0 i k(t)=1/t dla t>0. Wszystkie skalaryzacje na produkcie znikają poza zerowym zbiorem C_a x T, więc funkcja jest całkowalna Pettisa z całką zero na każdym zbiorze. Żaden przekrój f(s,.) nie jest całkowalny Dunforda, ponieważ testujący funkcjonał x'_s daje k. Drugi porządek istnieje. Przeniesienie przez J_X daje kontrprzykład Gelfanda. Nie pomylono zbiorów wyjątkowych zależnych od funkcjonału ze wspólnym zbiorem wyjątkowym.
- Nie dodawano innych opcjonalnych rozszerzeń.

## Technika
Źródło commit 636eb3151b6ab18fc6d18204264b940a926e97b8, blob 3513b151f381e65723d492171e22b491062a45e9; 277 nowych wierszy, 1791 łącznie, 39 etykiet, 23 dowody, 8 przykładów. Zagnieżdżenie środowisk i unikalność etykiet sprawdzone. Test commit de0f48647bfff9c44daa1f2cf1f6415c279c261a, blob 13d8e506743db20bda1c72d849d97b2ea540d1b8; 16 testów, nowa regresja obejmuje kontrakty, dokładne sumy iterowane na atomach oraz dolne oszacowania całki k na blokach diadycznych. Kontrakty źródłowe sprawdzono, nowego unittest ani PDF jeszcze nie potwierdzono. Status nowych przebiegów: [{"id":45349963163,"sha":"de0f48647bfff9c44daa1f2cf1f6415c279c261a","status":"in_progress","conclusion":null},{"id":45349937995,"sha":"636eb3151b6ab18fc6d18204264b940a926e97b8","status":"in_progress","conclusion":null}].

## Decyzja
Rozszerzenie podczas audytu 17: stan 0/2. Następny audyt 18 obejmuje niezależną kontrolę Fubiniego, poprzednich własności, terminologię i technikę, w tym PDF. Nie przechodzić do rozdziału 16.
