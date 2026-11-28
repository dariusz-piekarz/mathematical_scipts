# Algebra abstrakcyjna — AA-18, audyt IV (stabilizacyjny)

**Rozdział:** „Iloczyn tensorowy modułów i jego własności”.

**Status:** stabilny matematycznie po czterech audytach; audyt IV bez zmiany źródła.

## Niezależna weryfikacja matematyczna

Ponownie sprawdzono wszystkie 12 dowodów i 7 przykładów:

- Konstrukcja iloczynu tensorowego modułów prawostronnych i lewostronnych nad pierścieniem nieprzemiennym oraz własność uniwersalna.
- Działanie pierścienia przemiennego na iloczynie tensorowym.
- Izomorfizmy jednostki, symetrii, łączności i rozdzielności względem dowolnych sum prostych.
- Iloczyny tensorowe modułów ilorazowych i grup cyklicznych.
- Prawostronna dokładność, przykład niezachowania iniekcji i płaskość modułów wolnych i rzutowych.
- Konstrukcja lokalizacji modułu, poprawność działań na klasach i izomorfizm z iloczynem tensorowym przez ciało ułamków.
- Naturalność izomorfizmu, zachowanie dokładności przez lokalizację oraz płaskość ciała ułamków.
- Przykład modułu płaskiego, który nie jest rzutowy, izomorfizm Hom–tensor i baza iloczynu tensorowego przestrzeni wektorowych.

**Wynik:** nie ujawniono nowych błędów, luk ani nieuzasadnionych tożsamości. Nie dodawano twierdzeń ani nie zmieniano źródła.

## Walidacja lokalna

- SHA-256 źródła w audytach III i IV: `bf5a0d9adcafbd66b079d738a832562d3055716d2ab884b5714a8298383bcda0`.
- Wszystkie testy audytów I–III: **64/64 PASS**.
- Opublikowany plik testów `tools/tests/test_abstract_algebra_ch18.py` zawiera 64 kontrole (35 + 14 + 15). Dokładnie te same bajty sprawdzono lokalnie: `python -m unittest discover -s tools/tests -p 'test_abstract_algebra_ch18.py' -q` — **64/64 PASS**.
- Kompilacja `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **PASS**. PDF: **8 stron**, brak błędów i przepełnionych wierszy.
- **Jedno ostrzeżenie hyperref** w samodzielnym podglądzie dotyczy odsyłacza zastępczego do AA-08 w pomocniczym `main.tex`, nie źródła AA-18.
- **20 unikatowych etykiet, 11 odsyłaczy**, w tym do wcześniejszych rozdziałów; kontrola wizualna wszystkich ośmiu stron PASS.

## GitHub

Gałąź: `biblioteka-matematyczna-iteracja-6`.

Zaktualizowano źródło rozdziału, `books/pl/abstract_algebra.tex`, `catalog/books.json`, `README.md`, zestaw testów regresyjnych i `.github/workflows/abstract-algebra-chapter.yml`. Workflow buduje książkę AA-01–AA-18 oraz wymaga rozwiązania wszystkich odsyłaczy; dawny wyjątek dotyczący przyszłego AA-18 usunięto.

SHA Git blob opublikowanego źródła: `faaa972f8d1a7625d42c856d78c6f58ee7ad3564` — zgodny z wersją lokalną. SHA Git blob opublikowanego pliku testów: `ccfc4a0c3f329a22ec7143898d91412fc0b2e9f7` — zgodny z testowanym lokalnie.

**CI GitHub Actions:** wynik uruchomienia wywołanego push nie został potwierdzony. Dostępny odczyt udostępnia uruchomienia PR, nie push. Lokalny PASS pojedynczego rozdziału i 64 testów nie stanowi dowodu pomyślnej kompilacji pełnej książki.

## Status globalny

AA-01–AA-18: 18 rozdziałów stabilnych matematycznie, **59 iteracji audytowych**. Następny: AA-19 — „Ciała ułamków i konstrukcje liczb” (audyt I).
