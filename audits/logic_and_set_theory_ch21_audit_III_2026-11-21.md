# Logika matematyczna i teoria mnogości — rozdział 21, audyt III

**Data:** 2026-11-21  
**Rozdział:** Operacje na dowodach i warunki wyprowadzalności  
**Wynik:** audyt III z poprawkami, następnie niezależny audyt IV.

## Usterki i korekty

1. **Nieuprawniony wniosek o czasie programu.** Dotychczasowe stwierdzenie sugerowało, że dla każdego ustalonego programu obliczającego funkcję pierwotnie rekurencyjną można pierwotnie rekurencyjnie wytworzyć ślad jego wykonania. To nie wynika z pierwotnej rekurencyjności samej funkcji; nawet program zwracający stale 0 może zawierać nadmiarowe obliczenie o czasie niepierwotnie rekurencyjnym. Wyraźnie **wybrano** implementację weryfikatora z konstrukcji bazowych, składania i rekursji prostej. Dla tej konkretnej implementacji czas i pełny ślad mają pierwotnie rekurencyjne oszacowanie wyprowadzane indukcją po budowie programu, co pozwala formalizować konstrukcję certyfikatu w PA.
2. **Brak jawnego dowodu wartości ograniczenia.** W kompilatorze formuły `∀u<t(x) η` lub `∃u<t(x) η` oprócz dowodów instancji trzeba otrzymać formalny dowód równości `t(\overline n)=\overline k` i odpowiednich nierówności świadków. Dopisano to i wyjaśniono podstawianie równych termów; bez tego wyprowadzenie dla granicy `\overline k` nie byłoby jeszcze wyprowadzeniem dla oryginalnego termu.
3. **Kompilator ujemny dla implikacji.** Jawnie wskazano połączenie dowodów poprzednika i zaprzeczenia następnika, co domyka równoczesną indukcję obu polaryzacji.
4. **Skrót ograniczenia słabego.** Powiązano konstrukcję z definicją `u≤t` jako rozwinięcia przypadku `u<t` i dodatkowej instancji `u=t` z rozdziału 17.
5. **Zaprzeczenie ograniczonej egzystencji.** Wyjaśniono osobno przejście od negacji wszystkich instancji do dowodu formuły z kwantyfikatorem uniwersalnym i następnie do negacji egzystencji.

Nie dodano twierdzeń, lematów ani przykładów; zachowano 2 twierdzenia, 5 lematów i 7 dowodów.

## Kontrola formalna

- Każdy użyty nowy krok został uzasadniony w tekście albo odwołaniem do wcześniejszych lematów. W szczególności oddzielono obliczalność funkcji od oszacowania czasu wybranej realizacji.
- 8 etykiet, wszystkie unikatowe; 20 odsyłaczy, wszystkie ich cele obecne w lokalnym skrypcie (rozdziały 01–24).
- `latexmk` PASS, pełny lokalny dokument 183 strony; sześciostronicowy PDF wyodrębnionego rozdziału bez przepełnień.
- Dwa zestawy testów z wcześniejszych audytów: 27/27 PASS po dostosowaniu oczekiwanej liczby odsyłaczy do dodanego jawnego odniesienia; 18 nowych testów: 18/18 PASS. Razem **45/45 PASS** (częściowo nakładające się kontrole).
- Sprawdzono render wszystkich 6 stron. Ostrzeżenia o odsyłaczach poza rozdziałem 21 dotyczą wyłącznie rozdziałów przyszłych `ch:zf-axioms`, `ch:axiom-choice`.

**Dalszy krok:** niezależny audyt stabilizacyjny IV. Integracja z GitHubem dopiero po jego czystym wyniku.