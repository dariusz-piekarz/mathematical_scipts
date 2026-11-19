# Audyt nakładania się materiału — iteracja II

Data: 19 listopada 2026 r.  Zakres: 12 dostarczonych skryptów, 236 rozdziałów i sekcji.

## Metoda i ograniczenia

1. **Przesiew automatyczny**: dla każdego rozdziału przetworzono tekst LaTeX do postaci słownej, pomijając komendy techniczne i komentarze. Porównanie wykonano metodą TF–IDF na 2- i 3-wyrazowych frazach. Wynik `podobienstwo_tfidf` nie jest procentem wspólnej treści; nie oznacza identyczności zdań ani dowodów.
2. **Audyt ręczny**: porównano merytorycznie dwa rozdziały o topologii gładkich odmian projektowych, w szczególności twierdzenie słabe Lefschetza, jego dowód i przykłady. Rozpoznano różne ujęcia, a nie dwa dosłowne duplikaty.
3. **Wdrożona deduplikacja**: odtworzono jedno twierdzenie z dwiema historycznymi etykietami LaTeX, uwzględniając pełny krok topologiczny uzasadniany przez twierdzenie zewnętrzne. Tylko fragment twierdzenia (w geometrii) oraz twierdzenie z dowodem (w topologii) zostały zastąpione wspólnym `\input`.
4. **Zakres kontroli**: pozostałych 234 rozdziałów nie edytowano. Nie przeprowadzono ich pełnego audytu dowodów ani nie zweryfikowano ręcznie wszystkich par. Nie należy utożsamiać tego przesiewu z globalną weryfikacją poprawności matematycznej.

## Rzeczywiste scalenie

- Moduł kanoniczny: `wspolne/slabe_twierdzenie_lefschetza.tex`.
- Użytkownicy modułu: `rozdzialy/geometria_algebraiczna/10-geometria-algebraiczna-a-topologia-od-cykli-do-twierdzen-lefsc.tex` oraz `rozdzialy/topologia_algebraiczna/28-topologia-gladkich-zespolonych-odmian-projektowych-twierdzenia.tex`.
- Zachowane etykiety: `tw:ga10-weak`, `thm:xvii-weak-lefschetz`; w jednym dokumencie obie wskazują na ten sam numer twierdzenia.
- Wariant topologiczny: względne grupy homologii i homotopii, długie ciągi dokładne i wyprowadzenie ograniczenia `q<n-1`; zachowany w module wspólnym.
- Wariant geometryczny: uwaga o uchwytach funkcji Morse'a i zastosowanie do powierzchni w przestrzeni rzutowej; pozostały w pierwotnym rozdziale.
- Wariant topologiczny: przykłady przekroju `P^2` i krzywej na powierzchni; pozostały w pierwotnym rozdziale.
- **Wynik zewnętrzny**: twierdzenie geometryczne Lefschetza o dołączaniu komórek wymiaru co najmniej `n` jest założonym wynikiem głębokim; nie przedstawiono jego samodzielnego dowodu. Zostało to wyraźnie odróżnione od dowodu jego konsekwencji.
- Zabezpieczenie: warunek `\ifcsname` chroni przed drugim składem tego samego twierdzenia, gdy w jednej książce umieszczono oba rozdziały. W drugim wystąpieniu pozostaje odsyłacz do pierwszego.
- Źródła: `zrodla/` zawiera oba oryginały; `manifest_integracji.json` zapisuje dokładnie oba historyczne fragmenty poprzez długości i sumy kontrolne. Żaden inny fragment rozdziałów nie został zmieniony.

## Wyniki kompilacji i integralności

- `narzedzia/sprawdz_podzial.py` (deleguje do `sprawdz_integracje.py`): **12/12 źródeł, 236/236 rozdziałów objętych kontrolą niezamierzonych zmian**; dokładnie dwa celowo zmodyfikowane pliki rozdziałów, jeden nowy wspólny moduł.
- `geometria_algebraiczna.tex`: **pdflatex/latexmk OK**, 180 stron, brak błędów, niezdefiniowanych odsyłaczy, powielonych etykiet i przepełnionych wierszy.
- `topologia_algebraiczna.tex`: **pdflatex/latexmk OK**, 258 stron, brak błędów, niezdefiniowanych odsyłaczy, powielonych etykiet i przepełnionych wierszy; obecne ostrzeżenia `hyperref` o tekstach zakładek PDF, niepowodowane przez to scalenie.
- Osobny eksperyment z dwukrotnym `\input` wspólnego pliku: **OK**, bez powielonych etykiet.
- Nie kompilowano ponownie pozostałych 10 skryptów, których treść pozostaje niezmieniona.

## Mapa priorytetów dalszego przeglądu

| Priorytet | Źródła | Zakres | Decyzja |
|---|---|---|---|
| P1 | Geometria algebraiczna — rozdział 10; topologia algebraiczna — rozdział 28 | Słabe Lefschetza | **Scalone w tej iteracji** |
| P1 | Te same rozdziały | Rozdmuchanie, wyjątkowy dzielnik, przecięcie `E^2=-1`, wzór na kohomologię | Porównać szczegółowo twierdzenia i obie metody dowodu, przenieść tylko naprawdę powtarzalne części do wspólnego modułu |
| P1 | Te same rozdziały; dodatkowo rozdział 9 geometrii algebraicznej | Twarde Lefschetza, formy pierwotne, Hodge–Riemann, indeks Hodge'a | Unifikować warunki i oznaczenia, zachować algebraiczne i topologiczne przykłady |
| P2 | Tom I i tom II prawdopodobieństwa | Filtracje, czasy zatrzymania, martyngały | Nie usuwać rozróżnienia czasu dyskretnego i ciągłego; wynieść tylko identyczne definicje po kontroli zależności |
| P2 | Tom II i tom III prawdopodobieństwa | Proces Wienera, wariacja kwadratowa, całka Itô | Pozostawić własności procesu w tomie II, rachunek stochastyczny w III; wymiana wspólnych definicji i odsyłaczy |
| P2 | Tom I i tom II prawdopodobieństwa | Łańcuchy Markowa | Zachować dwie teorie (dyskretna/ciągła), nie scalać w jeden rozdział |
| P3 | Teoria modeli — fragmenty o Gödlu II i Löbie | Ścisły dowód i objaśnienie znaczenia | Nie są dosłownymi duplikatami; ograniczyć powtarzanie tez przez odpowiednie odsyłacze |
| P3 | Teoria grafów i węzłów; topologia algebraiczna | Grafy Reeba i teoria Morse'a | Wspólny słownik pojęć, zachować inne zastosowania |
| P3 | Teoria Galois, teoria całki | Nieelementarne całki, ciała różniczkowe i sens całkowalności | Wprowadzić most między skryptami; bez utożsamiania całek nieelementarnych z ogólnymi całkami |

## Zasady następnych merge'ów

1. Każde scalenie ma jawnie wskazać fragmenty źródłowe, zachować ich wyłączne argumenty i upewnić się, że nie osłabiono założeń twierdzenia.
2. Wszystkie dotychczasowe etykiety, rysunki, podpisy, programy, zadania i alternatywne dowody muszą pozostać dostępne lub zostać jawnie przeniesione do modułów wspólnych; żaden materiał nie może zniknąć bez audytu.
3. Każde `\input` musi dać się kompilować przy niezależnym składzie danego skryptu; moduły używane w dwóch rozdziałach powinny chronić przed duplikacją etykiet w książce łączonej.
4. Po zmianie uruchomić narzędzie integralności, kompilację wszystkich zmienionych skryptów i kontrolę ostrzeżeń.
5. Mergowanie całych rozdziałów wykonać dopiero po analizie ich zależności i wariantów dowodów; podobieństwo tekstowe jest jedynie sygnałem do przeglądu.

Pełny ranking 150 par między skryptami i 60 par wewnątrz skryptów znajduje się w `audyt/macierz_nakladek.csv`. Wynik podobieństwa jest heurystyczny; nawet wysokie wartości wymagają ręcznej kontroli.
