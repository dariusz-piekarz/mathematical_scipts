# Algebra liniowa — rozdział 01, audyt 4

Data: 21 listopada 2026  
Gałąź kanoniczna: \`biblioteka-matematyczna-iteracja-6\`  
Plik: \`chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex\`  
Commit poprawionego rozdziału: \`5a0b1ec176bbd1137288f503439442e0e6e39fd9\`

## Zakres przeglądu

Powtórnie sprawdzono definicje i dowody: aksjomaty przestrzeni wektorowej nad dowolnym ciałem, kryterium podprzestrzeni, przecięcie i sumę, operację rozpinania, niezależność rodzin indeksowanych, lemat Steinitza, konstrukcję baz skończonych, twierdzenie o wymiarze podprzestrzeni, przestrzenie współrzędnych i macierzy, bazy Hamela oraz dowód z lematu Zorna.

Szczególna uwaga: przypadki \(K=\mathbb F_2\), \(V=\{0\}\), pusty zbiór, pusta rodzina i pusty łańcuch; odróżnienie sum skończonych od nieskończonych; poprawność zależności między wprowadzanymi pojęciami; brak niejawnego użycia topologii.

Porównano wcześniejszy PDF ze źródłem: zweryfikowano dwie ilustracje TikZ (podprzestrzeń i zbiór afiniczny; niezależność liniowa), podpisy, współrzędne, odległości etykiet i brak kolizji napisów.

## Znalezione braki i poprawki

### 1. Brak twierdzenia o skończonej unii właściwych podprzestrzeni

Dodano twierdzenie: jeśli \(K\) jest nieskończonym ciałem, a \(U_1,\ldots,U_m\subsetneq V\) właściwymi podprzestrzeniami dla skończonego \(m\ge1\), to \(V\neq U_1\cup\cdots\cup U_m\). Dowód jest samodzielny, obejmuje wybór minimalnego skończonego pokrycia, wybór punktów należących dokładnie do jednej podprzestrzeni w tym pokryciu i analizę prostej \(x+ty\). Wskazuje, że dla każdej dodatkowej podprzestrzeni istnieje co najwyżej jeden niedozwolony skalar, z czego wynika sprzeczność z nieskończonością \(K\).

### 2. Brak kontrprzykładu nad ciałem skończonym

Dodano przykład trzech różnych jednowymiarowych podprzestrzeni \(U,W,Z\subset \mathbb F_2^2\), których unia jest równa całemu \(\mathbb F_2^2\). Zaznaczono, że twierdzenie o **dwóch** podprzestrzeniach obowiązuje nad każdym ciałem, natomiast twierdzenie o dowolnej skończonej unii wymaga nieskończoności ciała.

### 3. Przypadek pustego łańcucha w zastosowaniu lematu Zorna

Poprzednia wersja dowodu stwierdzała ogólnie, że unia wszystkich elementów łańcucha zawiera \(S_0\), a dopiero później osobno wspominała o łańcuchu pustym. To uzasadnienie było niepoprawne dla pustego łańcucha, gdy \(S_0\neq\varnothing\). Obecny dowód od razu rozdziela: dla \(\mathcal C=\varnothing\) ograniczeniem jest \(S_0\), zaś dla \(\mathcal C\neq\varnothing\) ograniczeniem jest unia łańcucha.

### 4. Uwaga o indeksowaniu rodzin

Przepisano wyjaśnienie dołączania wektora pod nowym indeksem tak, aby wprost zaznaczyć: ponowne wystąpienie tego samego wektora w rodzinie indeksowanej wytwarza relację \(v-v=0\). Odróżniono to od unii zbiorów, która nie dodaje duplikatów.

### 5. Spójność założeń i korekta języka

We wprowadzeniu deklarowano, że nie używa się topologii, a jednocześnie podawano przykład podprzestrzeni funkcji ciągłych. Wyjaśniono, że topologia i zbieżność nie są potrzebne do definicji i dowodów algebry liniowej; w przykładzie korzysta się wyłącznie ze znanej z analizy elementarnej własności ciągłości. Poprawiono również sformułowanie „z skończonym nośnikiem” na „o skończonym nośniku”.

## Kontrole techniczne i wizualne

- Statycznie po poprawkach: **60 unikalnych \`\\label\`**, brak powtórzeń w tym rozdziale.
- Wszystkie odsyłacze \`\\ref\` i \`\\eqref\` mają cel w rozdziale.
- Wszystkie środowiska \`\\begin\`/\`\\end\` są sparowane.
- Dwa rysunki pozostają osadzone w źródle TikZ, bez zewnętrznych zależności graficznych.
- PDF sprzed audytu 4 (audyt 3) został wizualnie sprawdzony: obydwa rysunki i podpisy są czytelne, bez kolizji.
- **Nowa kompilacja**: GitHub Actions \`linear-algebra-chapter.yml\`, run [44891248994](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44891248994), stan do aktualizacji po zakończeniu.

## Stan

**Audyt 4 wykrył i usunął istotne braki. Rozdział 01 nadal otwarty.**
Następny krok: audyt 5 tego rozdziału, dopiero po iteracji bez istotnych braków zamknąć rozdział i przejść do rozdziału 02.

Zaległości globalnej walidacji Biblioteki pozostają osobne: nie należy ich przedstawiać jako błędów nowego rozdziału ani jako naprawionych.
