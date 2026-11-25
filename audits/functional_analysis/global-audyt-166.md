# Audyt globalny 166 — integracja i bramka końcowa

Po zamknięciu rozdziału 33 (dcaf1102566a0d096f8bac6624d9dda594142ee8). Wyłącznie gałąź biblioteka-matematyczna-iteracja-6. Nie zmieniano treści rozdziałów ani mastera.

## Wykonane kontrole
- Odczyt mastera books/pl/functional_analysis.tex (blob a6059c73f9bc776397f73ca20c4b02c763760296) oraz katalogu rozdziałów: 35/35 unikatowych wejść, dokładnie wszystkie istniejące pliki TeX w katalogu functional_analysis, żadnego brakującego ani pominiętego pliku. Kolejność 01–15,15A,15B,16–33 prawidłowa.
- catalog/books.json: identyfikator functional_analysis wskazuje właściwy entrypoint books/pl/functional_analysis.tex. Moduły 15A i 15B definiują osobne numery sekcji i identyfikatory hyperref; rozdział 16 wraca do zwykłej numeracji.
- 35 istniejących plików regresji rozdziałowych. Nowy test integralności tools/tests/test_functional_analysis_book_integrity.py (f34302723e06019ce4ebfcd7f932b46dc0b8d6a2, de2e4d5dcd71d6e61ad9d14855bdd1684b91f62e) obejmuje cztery metody: inwentarz jednostek, wpis katalogu, globalne duplikaty i odsyłacze z pominięciem komentarzy i listingów, stos środowisk. Jeszcze nie wykonano go w CI.
- Próba zbiorczego pobrania 35 źródeł w jednym wywołaniu przekroczyła limit liczby wywołań; nie przypisano jej wyniku globalnej kontroli etykiet ani terminologii.
- Dodano .github/workflows/functional-analysis-book.yml (0bb1d09de292a51c4bcdbd481eac38b939b3cac2). W jednym przebiegu uruchamia wszystkie 36 plików regresji w osobnych procesach, kompiluje bezpośrednio właściwy master z tytułem i spisem treści, kontroluje kolejność sekcji TOC oraz końcowe błędy LaTeX (w tym zduplikowane identyfikatory PDF). Publikuje PDF, tekst, TOC, log kompilacji i log regresji. Wcześniejszy PDF 272 strony to wrapper bez tytułu i spisu treści, nie finalny master.
- CI 45587929282 dla pełnej książki: queued w chwili odczytu. Nie potwierdzono globalnych regresji, kompilacji właściwego mastera, globalnej kontroli odsyłaczy ani oględzin całego PDF. Nie wykonywano Lean.

## Decyzja
Audyty rozdziałowe zakończone, audyt globalny w toku. Następny audyt 167: odczytać wyniki pełnej bramki, naprawić ewentualne problemy, pobrać rzeczywisty PDF, obejrzeć wszystkie strony oraz uzupełnić kontrolę terminologii i powiązań między rozdziałami. Nie zamykać książki przed zaliczeniem tych warunków.
