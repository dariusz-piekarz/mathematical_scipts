# Algebra liniowa — audyt globalny, iteracja 09/09 (22 listopada 2026)

## Stan wejściowy i zakres
HEAD przy rozpoczęciu: `179e90d9da7cdbd0ff062ce6496667dc66b682a0`. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raport `iteration_08.md` i `status.md`. Raporty 01–08 istnieją, raport 09 przed tą iteracją nie istniał. Drzewo Git dla wejściowego HEAD zawiera dokładnie 32 pliki rozdziałów; punkt wejścia książki zawiera 32 `\\input` w prawidłowej kolejności. To potwierdza zgodność struktury, nie kompletność merytoryczną.

## Faktycznie wykonane kontrole
- Odczytano w całości źródła rozdziałów 01, 08, 10, 15, 19, 24, 29 i 32 (łącznie 9822 wiersze), sprawdzając liczbę środowisk dowodów, etykiet i odsyłaczy, oraz występowanie wybranych zakazanych określeń. W rozdziale 01 występuje ciąg `unia` w historycznych etykietach/odsyłaczach; nie dokonano automatycznej zamiany. W pozostałych siedmiu próbkowanych rozdziałach nie znaleziono dosłownych samodzielnych wyrazów `unia`, `tensorowanie`, `sekwencyjny`.
- Potwierdzono istnienie 32 plików rozdziałów w drzewie commitu i odpowiadających im 32 instrukcji `\\input` w `books/pl/linear_algebra.tex`.
- Przejrzano wyniki CI GitHub Actions: dla commitu `22274b5653136fb0452f499b1369911f0bc5b728` (iteracja 08) istnieją ukończone przebiegi `44996683204` i `44996683192` o wyniku SUCCESS. Są to kontrole tego commitu, nie niezależna wizualna inspekcja PDF. Dla nowszego HEAD `179e90d...` odnotowano dwa zakończone sukcesem przebiegi dla jego rodzica `9d2be989...`, a trzeci był `in_progress` w chwili sprawdzenia.
- Przejrzano zakres wcześniejszych raportów 01–08 i ich otwarte kontrole. Poprawki matematyczne w LA08, LA15, LA19, LA23–24 i LA29/LA32 pozostają udokumentowane w odpowiednich raportach.

## Ograniczenia i wynik
Nie wykonano pełnej niezależnej lektury każdego dowodu we wszystkich 32 rozdziałach, pełnego porównania wszystkich `\\label`/`\\ref` i bibliografii ani oględzin stron renderowanego PDF i rysunków TikZ. Nie wygenerowano osobnych PDF. Zatem **nie można uczciwie oznaczyć audytu globalnego jako czystego**. Niniejsza iteracja 09 dokumentuje kontrolę strukturalną i próbkowanie międzyrozdziałowe, nie certyfikuje pełnej poprawności matematycznej.

## Dalsze wymagane kontrole
1. Pełny automatyczny wykaz etykiet i odsyłaczy z 32 plików, z ręczną oceną odsyłaczy spoza książki.
2. Niezależna lektura wszystkich dowodów, ze szczególnym naciskiem na zależności 08–11, 14–20, 22–28 i 29–32.
3. Pobranie z CI i wizualna inspekcja pełnego PDF, szczególnie wszystkich rysunków i stron z poprawkami.
4. Potwierdzenie wszystkich wymaganych jobów CI dla końcowego SHA, bez utożsamiania pojedynczego sukcesu z pełnym PASS.

Nie wprowadzono nieuzasadnionych zmian w źródłach matematycznych. Status: **09 wykonana częściowo, globalne zamknięcie NIEPOTWIERDZONE**.
