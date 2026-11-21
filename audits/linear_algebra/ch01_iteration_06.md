# Algebra liniowa — rozdział 01: audyt 6

Data: 2026-11-21  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Plik: `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`  
Commit treści po audycie 6: `f6a7d8b5fb8a4a32b6ca58adeb12218a4b9dada5`

## Zakres i metoda

Szósty audyt dotyczył wyłącznie rozdziału 01. Ponownie sprawdzono warunki w definicji przestrzeni i podprzestrzeni, przypadki skalarów z ciał o charakterystyce dodatniej, funkcje i wielomiany jako przestrzenie wektorowe, domknięcia na działaniach, zależność i rozpinanie rodzin dowolnej mocy, konstrukcję baz skończonych i dowody Steinitza oraz dwie wersje twierdzenia o istnieniu bazy wykorzystujące lemat Zorna.

Oddzielnie sprawdzono wersję po audycie 5: przebieg CI [44891689186](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44891689186) zakończył się sukcesem. Zweryfikowano, że nie wystąpiły nierozwiązane odsyłacze w finalnym logu PDF. Sprawdzono także skład poprzedniego PDF oraz wyrenderowano strony 4, 5 i 8 aktualnego PDF: oba rysunki, podpisy i nowe fragmenty nie mają widocznych kolizji.

## Usterki i uzupełnienia

### 1. Brak twierdzenia o skończonym charakterze

Dodano `prop:lin-skonczony-charakter`: dla dowolnej rodziny indeksowanej \((v_i)_{i\in I}\) przestrzeń rozpięta jest unią przestrzeni rozpiętych przez jej skończone podrodziny,
\[
\operatorname{span}\{v_i:i\in I\}
=\bigcup_{\substack{J\subseteq I\\J\text{ skończony}}}\operatorname{span}\{v_j:j\in J\}.
\]
Dodatkowo udowodniono równoważność między niezależnością całej rodziny a niezależnością wszystkich jej skończonych podrodzin. Dowód jawnie uwzględnia \(I=\varnothing\), \(J=\varnothing\), skończone nośniki oraz powtarzające się wartości różnych indeksów. Wynik porządkuje logiczny fundament dowodów dotyczących baz Hamela i nieskończonych rodzin wektorów.

### 2. Brak kontrprzykładów do części warunków podprzestrzeni

Dodano `prz:lin-podprzestrzen-warunki`:
- \(A=\{(x,y)\in\mathbb R^2:x\geq0,\ y\geq0\}\) zawiera zero i jest zamknięty na dodawanie, ale nie na mnożenie przez ujemne skalary.
- \(B=(\mathbb R\times\{0\})\cup(\{0\}\times\mathbb R)\) zawiera zero i jest zamknięty na mnożenie przez skalary, ale nie na dodawanie.
To pokazuje niezależną rolę każdego z dwóch warunków domknięcia. Podano konkretne wektory \((1,0)\), \((0,1)\), \((1,1)\).

### 3. Dodatkowy przykład zależności podprzestrzeni od ciała

W przykładzie liczb zespolonych zaznaczono jawnie, że \(\mathbb R\subseteq\mathbb C\) jest podprzestrzenią \(\mathbb C\) jako przestrzeni nad \(\mathbb R\), lecz nie jest podprzestrzenią \(\mathbb C\) jako przestrzeni nad \(\mathbb C\): \(i\cdot1\notin\mathbb R\).

### 4. Uzasadnienie domknięcia przestrzeni wielomianów

Rozszerzono przykład \(K[X]_{\leq d}\): po zadeklarowaniu, że zbiór jest domknięty na dodawanie i mnożenie przez skalar, dopisano rachunkowe uzasadnienie na podstawie stopnia niezerowych wielomianów. Jawnie rozdzielono przypadek sumy lub skalarnej wielokrotności równej zeru.

## Sprawdzenie struktury po poprawkach

- **66 unikalnych etykiet `\\label`**, brak duplikatów lokalnych.
- Wszystkie odsyłacze `\\ref`, `\\eqref` posiadają lokalne cele.
- Brak niezrównoważonych `\\begin` i `\\end`.
- Liczba ilustracji TikZ nie zmieniła się (dwie); brak nowych zewnętrznych plików ilustracji. PDF po audycie 6 obejmuje 15 stron; wyrenderowane strony z nowymi przykładami i twierdzeniem o skończonym charakterze zostały zweryfikowane wizualnie.
- Zaplanowane walidacje aktualnego commita: [GitHub Actions run 44892015946](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44892015946). **Wynik: success.** Wszystkie kroki poświęcone algebrze liniowej, w tym pełna kompilacja LaTeX, kontrola odsyłaczy i eksport PDF, zakończyły się sukcesem. Końcowy plik `linear_algebra.log` nie zawiera `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character` ani błędów środowisk. PDF zawiera **15 stron**. Pierwszy przebieg LaTeX miał przejściowe ostrzeżenia o odsyłaczach; po kolejnych przebiegach zniknęły z końcowego logu.

## Uwaga o testach globalnych

Globalna walidacja repozytorium raportuje wcześniejsze, niepowiązane z tym rozdziałem błędy importów i niezgodności kopii źródłowych. Są świadomie raportowane osobno w CI rozdziału; ich istnienie nie jest przemilczane, a zaliczenie CI algebry liniowej nie oznacza usunięcia zaległości globalnych.

## Status

**Audyt 6 wykrył i uzupełnił braki; rozdział 01 pozostaje otwarty.** Zgodnie z ustalonym cyklem następnym krokiem jest ponowny audyt 7 tego samego rozdziału. Rozdziału 02 nie rozpoczynamy.
