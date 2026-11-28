# Logika matematyczna i teoria mnogości — audyt I rozdziału 33

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/logic_and_set_theory/33-relacja-wymuszania-i-twierdzenie-o-wymuszaniu.tex`  
**Tytuł:** „Relacja wymuszania i twierdzenie o wymuszaniu”.

## Zakres audytu

Przeanalizowano cały nowy rozdział, a nie wyłącznie jego spis treści. Audyt objął założenia na przeliczalny tranzytywny model zbiorowy $M$, preorder warunków, lokalną gęstość, równoczesną rekurencję dla relacji $p\Vdash\sigma\in\tau$ i $p\Vdash\sigma=\tau$, właściwe uporządkowanie rang, monotoniczność, domknięcie gęstościowe, klauzule logiczne, schemat definiowalności, pełny lemat prawdy, interpretację wymuszania przez wszystkie rozszerzenia generyczne, aksjomaty ZFC w $M[G]$ oraz minimalność rozszerzenia.

## Wyniki sprawdzenia matematycznego

### 1. Atomowe klauzule i rekurencja

W obydwu klauzulach atomowych zależności zachodzą pomiędzy parami nazw o malejącej sumie naturalnej rang, więc definicja jest dobrze ufundowana. Użycie zwykłego maksimum rang nie wystarczyłoby do uzasadnienia tego kroku. Sprawdzono również, że wszystkie kwantyfikatory po warunkach są ograniczone do $\mathbb P$, a sformułowanie dla preorderu nie zakłada ukrycie antysymetrii.

**Wynik:** nie znaleziono kontrprzykładu ani błędu rekurencji; zapis sumy naturalnej i jego rola zostały jawnie wyjaśnione.

### 2. Generyczność i lemat prawdy

Lemat o lokalnej gęstości jest prawidłowo wyprowadzony z gęstości globalnej zbioru $D\cup I_p$. W indukcyjnym dowodzie atomowego lematu prawdy zweryfikowano osobno oba kierunki przynależności i oba kierunki równości; w trudniejszym kierunku równości używa się gęstego zbioru warunków, które albo wymuszają równość, albo są świadkami niepowodzenia jednej z jej klauzul. Indukcja dla negacji korzysta z definiowalności zbioru warunków rozstrzygających, a dla egzystencji z lokalnej gęstości zbioru warunków z nazwanym świadkiem.

**Wynik:** dowód nie zakłada $M[G]\models\mathrm{ZFC}$ przed uzyskaniem twierdzenia o wymuszaniu.

### 3. Schemat definiowalności i twierdzenie Tarskiego

Dla każdej ustalonej formuły uzyskuje się oddzielną formułę definiującą wymuszanie w $M$, korzystając z rekurencji dla atomów i indukcji po składni. W rozdziale wyraźnie odróżniono ten schemat od niedopuszczalnego jednego predykatu prawdy dla wszystkich kodów zdań w $M$.

**Wynik:** zachowano właściwą różnicę pomiędzy schematem definiowalności a twierdzeniem Tarskiego o niedefiniowalności prawdy.

### 4. Zachowanie ZFC

Oddzielnie sprawdzono: ekstensjonalność, ufundowanie, zbiór pusty, parę, nieskończoność, sumę, wyróżnianie, zbiór potęgowy, zastępowanie i aksjomat wyboru.

**Zbiór potęgowy.** Weryfikacja obejmuje dwa włączenia: każda interpretacja $\theta\in\mathcal S_\tau$ jest podzbiorem $\tau^G$ oraz dla każdego $b=\rho^G\subseteq\tau^G$ konstrukcja $\theta_\rho=\{(\sigma,p):p\Vdash(\sigma\in\tau\land\sigma\in\rho)\}$ reprezentuje $b$. Ograniczenie do zbioru pierwszych współrzędnych nazwy $\tau$ zapewnia, że zbieranie nazw jest operacją zbiorową w $M$.

**Zastępowanie.** Dla każdej pary $(\sigma,t)$ wybiera się świadka o minimalnej randze nazwy, dzięki czemu rodzina wyborów należy do $M$ (nie jest wyborem z właściwej klasy). Dowód surjektywności skonstruowanej nazwy obrazu wykorzystuje gęstość wybranych warunków poniżej warunku wymuszającego przynależność do zbioru wejściowego i istnienie wartości.

**Wybór.** Nazwa funkcji z porządkowej $\kappa$ do interpretacji skończonej rodziny nazw, wraz z funkcją najmniejszego indeksu, zapewnia wewnętrzne dobre uporządkowanie zbioru. Schematy wyróżniania i zastępowania są sprawdzone przed zastosowaniem ich do tej konstrukcji.

**Wynik:** na etapie pierwszego audytu nie wykryto błędu matematycznego wymagającego zmiany tekstu źródłowego; konstrukcje zbioru potęgowego i zastępowania pozostają jednak głównym przedmiotem niezależnego audytu II.

## Testy i integracja

- Rozdział 33 został dodany do `books/pl/logic_and_set_theory.tex`, katalogu `catalog/books.json` i osobnego workflow CI.
- Inwentarz: **4 definicje, 6 lematów, 6 twierdzeń, 3 przykłady, 5 uwag, 12 dowodów**, 25 etykiet i 26 odsyłaczy; wszystkie odsyłacze mają cel.
- Liczba rozdziałów książki: **33**. Łącznie **828 etykiet i 616 odsyłaczy** w jej plikach źródłowych.
- `tools/tests/test_logic_and_set_theory_ch33.py` zawiera **11 testów**, w tym małą obliczeniową realizację atomowej relacji wymuszania w skończonym drzewie Cohena. Testy Python nie stanowią formalnej weryfikacji dowodów w Lean.
- [GitHub Actions — rozdziały 01–33, przebieg #45019079045](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45019079045): **SUCCESS** — testy, struktura, etykiety, odsyłacze, kompilacja i kontrola PDF.
- Artefakt PDF całej książki liczy **288 stron**; nowy rozdział zajmuje strony PDF **281–288** (drukowane numery 272–279). Wszystkie osiem stron wyrenderowano i obejrzano na zestawieniu kontaktowym: wzory, tekst i podpisy są czytelne, bez kolizji oraz ucięć.
- W logu LaTeX jest **0 błędów, 0 przepełnionych wierszy, 0 niezdefiniowanych odsyłaczy i 0 brakujących cytowań**; zachowało się **1 ostrzeżenie `Underfull \\hbox`** w całej książce.
- Ostatnia strona rozdziału jest częściowo pusta, co nie stanowi błędu składu. Nie ścieśniano sztucznie materiału kosztem czytelności.

## Werdykt

**Audyt I: PASS matematyczny i techniczny, bez zmian źródła LaTeX po stworzeniu rozdziału.** Rozdział 33 `NIE JEST JESZCZE OSTATECZNIE STABILNY`: wymaga ponownego niezależnego audytu II, przede wszystkim powtórzenia kontroli definicyjności forcingu, lematu prawdy oraz ograniczania rang w konstrukcjach zbioru potęgowego i zastępowania. Dopiero kolejne powtórzenia bez nowych usterek mogą uzasadnić status stabilny.
