# Logika niestandardowa — plan

NCL jest osobnym skryptem logik nieklasycznych, nie synonimem analizy niestandardowej. Klasyczna składnia, semantyka i pełność pozostają kanonicznie w MOD; podstawowe pojęcia zbiorowe i rachunek zdań w LST.

## Kolejność robocza
1. NCL-01: Logika rozmyta i zbiory rozmyte — dotychczasowy LST-40, audyty I–VIII zachowane, dokończyć reprezentacje Changa, Aglianò–Montagni i Jeneiego–Montagni oraz stabilizację. Możliwy późniejszy podział tego obszernego rozdziału.
2. Logika intuicjonistyczna: BHK, rachunek, semantyka Kripkego, algebry Heytinga, poprawność i pełność, własność alternatywy, tłumaczenia negatywne.
3. Logika modalna: K, T, D, B, S4, S5; ramy i modele Kripkego, korespondencja, filtracja, pełność; modalności epistemiczne i deontyczne jako dalsze rozwinięcie.
4. Logiki wielowartościowe: Kleene, Łukasiewicz, Post, Belnap; macierze logiczne, wartości wyróżnione, relacje z logiką rozmytą bez dublowania NCL-01.
5. Logiki parakonsystentne i relewantne: eksplozja, LP, FDE, konsekwencja i kontrmodele.
6. Logiki substrukturalne: rachunki sekwentów, logika liniowa, brak kontrakcji lub osłabiania, residuacja; odsyłacze do teorii dowodu.
7. Logiki temporalne i dynamiczne: LTL, CTL, PDL, semantyka ścieżek i programów; rozstrzygalność w odpowiednim zakresie.
8. Logiki niemonotoniczne: logika domyślna, minimalizacja, modele stabilne.
9. Logiki wyższego rzędu i infinitarne: granice z MOD i teorią mnogości, bez przenoszenia twierdzeń o dużych kardynałach bez analizy zależności.
10. Rozszerzenia opcjonalne: logika kwantowa, logiki epistemiczne wieloagentowe, logiki probabilistyczne (odróżnić od stopni prawdy).

Każdy blok: definicje, intuicje, semantyka, rachunki, poprawność i pełność w odpowiednim zakresie, przykłady, kontrprzykłady, odsyłacze, rysunki, testy, audyty do stabilizacji i audyt kontrolny. Priorytet użytkownika: elementarna LST przed dalszym rozwojem NCL.

## NCL-06 — audyt stabilizacyjny, 2026-11-28

Źródło: commit [d809a36](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d809a36bc57ca3bdae2da5f43212bb1dc00f70ce), blob `96f18e679642ace3773c47406886734e856fab3f`. Aktualny katalog i plik główny obejmują 6 rozdziałów, w odróżnieniu od historycznego globalnego snapshotu z 3 rozdziałami.

- Kontrola statyczna NCL-06: 3786 wierszy, 102 etykiety, 128 odsyłaczy z istniejącymi celami, bez odsyłaczy do późniejszych wyników wewnątrz rozdziału. W sześciu rozdziałach 523 unikatowe etykiety. Bilans środowisk, klamer i ograniczników matematycznych poprawny; 5 diagramów sprawdzonych na poziomie kodu.
- CI: [Logic and model theory validation](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46191946666) — in_progress podczas odczytu; wcześniejsze kroki kontroli importów, inwentarza, odsyłaczy i regresji zakończone sukcesem. [Kontrola terminologii](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46191946627) — sukces.
- Weryfikacja wizualna PDF nie została wykonana. Status stabilizacji i audytu kontrolnego pozostaje otwarty do potwierdzenia kompilacji, kontroli logów i osobnego odbioru.
