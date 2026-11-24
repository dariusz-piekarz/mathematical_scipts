# Globalny audyt 35 — odwołania opisowe i kolejność rozdziałów

2026-11-24. Baza f2dc13ffd7f461fa5ab3e001e3fe7ec5c3457c83. Przejrzano wszystkie 44 pliki 00–43 pod kątem wzmianek o rozdziałach oraz kolejność input w książce. 00 nienumerowany; 01–05 zachowują numery; 37–43 drukowane jako 6–12; 06–36 jako 13–43.

- 07: ręczne odwołanie do pierwszego rozdziału zastąpiono etykietą.
- 08: nieaktualne „w szóstym” wskazywało BFS/DFS zamiast macierzy incydencji (drukowany 13); obie liczby zastąpiono etykietami.
- 15: odwołanie do wzoru Eulera–Poincarégo w rozdziale triangulacji.
- 18: wielomian Alexandera jest sekcją tego samego rozdziału, nie osobnym rozdziałem.
- 20: po chirurgii Dehna następuje JSJ, nie teoria 4-rozmaitości; wskazano rozdział 22 i sekcję przesuwania uchwytów.
- 21: etykieta rozdziału Bassa–Serre'a.
- 22: następny rozdział to plumbing, nie homologia Floera; wskazano sekcję sec:kt-hfk w rozdziale 35 (drukowany 42).

Poprawne powiązania 02–03, 05–37–43–06, 06–07, 10–09, 23–24, 26–27–28, 29–30, 31–32, 33–34 pozostawiono. Nie zmieniano kolejności ani twierdzeń.

Rozszerzono test globalny o heurystykę pojedynczych liczbowych odwołań do rozdziałów (w tym polskie liczebniki porządkowe 1–10); raportuje i blokuje strict. Wyjątek: nagłówek uwagi w 01 o zakresie pierwszego rozdziału. Heurystyka nie zastępuje semantycznej kontroli wzmianek względnych. Wymagana ponowna kompilacja i kontrola CI; audyt 35 otwarty.

## Stabilizacja i naprawa osobnego PDF

Dla SHA 5a3763fc30dc41ce1c3a7af033aae50061f05d45 pełny workflow 45296092941 zakończył się success. Rzeczywiste logi: 44/44 źródeł, duplicate_labels=0, unresolved_references=0, forbidden_language=0, manual_chapter_numbers=0; pełna książka 298 stron, 0 ostrzeżeń. Workflow algorytmiczny 45296092799: finite-models success, chapter-pdf failure. Log jobu 138116728260 wskazuje dwa niezdefiniowane odsyłacze rem:tg-laplacian-conventions i ch:tg-laplacian, wprowadzone w audycie 34. Przyczyną jest ręcznie ograniczony prefiks 14 źródeł, nie brak etykiet w książce.

Naprawa: osobny PDF zachowuje dotychczasowy minimalny prefiks, ale rozszerza go do domknięcia względem rzeczywistych odsyłaczy wszystkich włączonych źródeł, z zachowaniem kolejności i numeracji pełnego tomu. Wykorzystano parser etykiet, odsyłaczy i komentarzy z globalnego audytu, odrzucamy brakujące i powielone etykiety. Nie wyłączono kontroli ostrzeżeń LaTeX. Zmieniono wyłącznie workflow i raport, bez modyfikowania źródeł książki. Ponowny przebieg osobnej kompilacji i oględziny pełnego PDF są wymagane przed zamknięciem.

## Zamknięcie audytu 35

Workflow algorytmiczny 45296788000 dla SHA 64664a1e2d7fda08c566b7505d390108eb17c24c: completed/success, oba joby finite-models (138119107668) i chapter-pdf (138119108112) success. W logu rzeczywisty komunikat „Algorithmic PDF: reference-closed prefix of 16 source files”. Artefakt 14876877532 istnieje. Pełny workflow 45296092941 dla SHA 5a3763fc30dc41ce1c3a7af033aae50061f05d45: success. Pobrano artefakt pełnej książki 14875698541, potwierdzono 298 stron i pusty plik ostrzeżeń. Porównano tekst wszystkich 298 stron z rzeczywistym PDF poprzedniego audytu (14876161294); różnice wystąpiły dokładnie na stronach fizycznych 94, 98, 141, 164, 185, 187, 196. Wyrenderowano i obejrzano wszystkie siedem stron; nie zauważono kolizji ani obcięć. Naprawa 64664a1 nie zmienia źródeł książki. Porównanie tej rewizji z bieżącą gałęzią nie wykazało dalszych zmian grafowych.

**Audyt 35 zamknięty.** Następny blok: spójność przekrojów, skojarzeń, dualności planarnej oraz przepływów (audyt 36). Całościowy audyt nadal otwarty.
