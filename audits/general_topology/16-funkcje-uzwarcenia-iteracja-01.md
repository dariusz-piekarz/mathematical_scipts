# Topologia ogólna — rozdział 16: audyt iteracja 01

Data: 2026-11-22; gałąź `biblioteka-matematyczna-iteracja-6`.

## Nowy rozdział i zakres

Plik `chapters/pl/general_topology/16-funkcje-ciagle-i-uzwarcenia.tex`.
Rozdział nie dubluje twierdzenia o zanurzaniu przestrzeni Tychonoffa w kostkę ani konstrukcji jej zwartego domknięcia, które zostały już w pełni udowodnione w rozdziale 07 (etykiety `thm:topog-zwartosc-zanurzenie-kostka` i `cor:topog-zwartosc-uzwarcenie`). Nie powtarza również definicji całkowitej regularności z rozdziału 05.

Zawartość nowa: (1) topologia początkowa rodziny funkcji i jej kryterium uniwersalne; (2) równoważne funkcjonalne kryterium całkowitej regularności w przestrzeni T₁; (3) formalna definicja uzwarcenia Hausdorffa i kryterium jego istnienia; (4) równoważność uzwarceń, jednoznaczność odpowiedniego homeomorfizmu, przypadek zwartego X; (5) porównywanie uzwarceń przez ciągłe odwzorowania zgodne z zanurzeniami i porządek częściowy na ich klasach równoważności; (6) dwa nierównoważne uzwarcenia przedziału otwartego, powiązane odwzorowaniem ilorazowym; (7) wskazanie zależności od rozdziału 17, w którym zostaną opracowane konkretne uzwarcenia Aleksandrowa oraz Čecha–Stone’a.

## Kontrola definicji i dowodów

1. **Topologia początkowa:** rodzina przeciwobrazów otwartych jest podbazą, a skończone przecięcia generują najmniejszą topologię. Kryterium ciągłości `g:Z→X` wynika przez przeciwobrazy zbiorów podbazowych, bez użycia nieudowodnionych implikacji.
2. **Całkowita regularność i funkcje:** (i)⇒(iii) stosuje `1-h` z definicji dla `F=X\setminus U`; T₁ pozwala oddzielać różne punkty przez funkcje. (iii)⇒(ii) korzysta z podbazowych zbiorów `f^{-1}((1/2,1])` i pokazuje dwie inkluzje topologii. (ii)⇒(i) wykorzystuje skończone bazowe przecięcie i ciągłe funkcje odcinające na `[0,1]`; maksimum skończonej rodziny jest ciągłe. Przypadek `F=∅` jest rozwiązany osobno, więc nie zachodzi problem pustego przecięcia indeksów.
3. **Niewystarczające oddzielanie punktów:** przykład `R` z topologią dyskretną i jedną injektywną funkcją arctan daje topologię początkową euklidesową, a nie dyskretną; wyjaśnia różnicę między rodziną rozdzielającą punkty i rodziną wyznaczającą topologię.
4. **Uzwarcenie:** wymagana jest para `(K,e)` ze zwartym `K` Hausdorffa oraz zanurzeniem `e` o gęstym obrazie, bez niejawnego utożsamienia struktur. Konieczność aksjomatu Tychonoffa wynika z jego dziedziczenia na podprzestrzenie zwartych przestrzeni Hausdorffa; wystarczalność jest jawnie wskazana jako dowiedziona w rozdziale 07.
5. **Jednoznaczność:** jeśli dwa ciągłe odwzorowania na przestrzeń Hausdorffa są zgodne na gęstym `e_1(X)`, to zgadzają się wszędzie. Dowód przez domkniętość przeciwobrazu przekątnej jest poprawny.
6. **Zwarta przestrzeń:** ciągły obraz przestrzeni zwartej jest zwarty, w przestrzeni Hausdorffa również domknięty; gęstość obrazu daje surjektywność zanurzenia.
7. **Porządek uzwarceń:** ciągłe odwzorowanie zgodne z zanurzeniami jest automatycznie surjektywne, gdyż jego zwarty obraz w przestrzeni Hausdorffa jest domknięty i zawiera gęsty obraz X. Jednoznaczność wynika z gęstości. Jeśli odwzorowania zgodne z zanurzeniami istnieją w obie strony, ich złożenia są identycznościami przez jednoznaczność przedłużenia, więc są homeomorfizmami. Relacja indukuje porządek częściowy na klasach równoważności.
8. **Dwa uzwarcenia:** `(0,1)⊂[0,1]` i `e(t)=exp(2πit)` w okręgu `S¹` są zanurzeniami o gęstych obrazach. Brak homeomorfizmu zgodnego z zanurzeniami wykazuje jednoznaczność granic w okręgu: ciągłość wymusza utożsamienie 0 i 1, co przeczy injektywności homeomorfizmu.

## Integracja i testy

Utworzono samodzielny punkt wejścia `books/pl/general_topology_ch16.tex`; zmodyfikowano `books/pl/general_topology.tex`, `catalog/books.json`, plan i workflow. Otworzono test `tools/tests/test_general_topology_ch16.py`, który bada równoważne topologie początkowe w skończonych modelach oraz etykiety, rozdziały i domknięcie odsyłaczy. Test rozdziału 15 przestawiono ze sztywnego warunku `len(chapters)==15` na kontrolę jego pozycji (indeks 14) i dolnej granicy liczby rozdziałów, aby nie uniemożliwiał rozbudowy książki.

Podczas integracji wystąpił konflikt zapisu do GitHuba z powodu współbieżnego przesunięcia głowicy gałęzi. Wykonano ponowny odczyt aktualnych plików i zapis po jednym pliku; żadne równoległe zmiany nie zostały nadpisane.

## Wynik iteracji 01

| Kontrola | Status |
|---|---|
| Matematyka i uzasadnienie kroków | PASS — wstępny audyt |
| Spójność zależności i brak zbędnego duplikowania rozdziału 07 | PASS |
| Definicje, przykłady, kontrprzykłady | PASS — wstępny audyt |
| Katalog, pliki główne i testy | Wdrożone |
| CI i samodzielny PDF | Weryfikacja bieżącego przebiegu |
| Stabilizacja | **OTWARTA** — nie oznaczać rozdziału jako stabilny |

Następna iteracja: ponowna niezależna kontrola wszystkich dowodów i wyników CI wraz z renderem PDF; dopiero potem ewentualna stabilizacja. Nie przenosić własności uniwersalnej uzwarcenia Čecha–Stone’a z rozdziału 17 do rozdziału 16.

## Kontrola CI po uzupełnieniu

Pierwsza kompletna wersja bez porządku uzwarceń przeszła GitHub Actions: [run 45011766280](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011766280), `completed/success`. Pobrano PDF samodzielnego rozdziału 16: trzy strony A4, logi bez ostrzeżeń i widocznych problemów składu. Następnie dodano porządek uzwarceń (commit `2008dcb8026223b4cd64e4ad4013540eb6a29b04`) i zastosowanie do przedziału/okręgu (`2dc06a8ba5398795bcabaf5570b828aa2ea48763`), a test rozszerzono (`03187105b922fe0b3b22efbfc10cd1aff6418b4a`). Ostatni przebieg dla tej wersji: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45012081743 . Weryfikację nowego PDF i logu należy odnotować po zakończeniu.
