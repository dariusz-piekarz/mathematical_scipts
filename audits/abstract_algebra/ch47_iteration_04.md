# AA-47 — audyt IV: rzeczywista kontrola katalogu i odsyłaczy

**Data:** 23 listopada 2026 r.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Status:** NIE STABILNY — wykonano kontrolę struktury i odsyłaczy, nie wykonano kompilacji, inspekcji PDF ani pełnego CI.

## Materiał faktycznie odczytany

- `catalog/books.json`;
- `books/pl/abstract_algebra.tex`;
- `chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex`;
- źródła rozdziałów AA-43, AA-44, AA-45, AA-46 (dla kontroli odsyłaczy).

## Wyniki automatycznej kontroli zawartości

1. Wpis `abstract_algebra` w katalogu: **47** plików rozdziałów.
2. Plik główny książki: **47** instrukcji `\\input`.
3. Plik AA-47 obecny zarówno w katalogu, jak i w `\\input`: **PASS**.
4. W AA-47: **30** etykiet `\\label`, wszystkie unikatowe; **0** duplikatów lokalnych.
5. W AA-47: **24** wywołania `\\ref` lub `\\eqref`. Wszystkie odsyłacze lokalne mają cele w AA-47. Pozostałe **5** unikatowych celów znaleziono bezpośrednio w plikach AA-44–AA-46:
   - `aa:ch:liouville-elementary-integration` — AA-44;
   - `aa:ch:picard-vessiot` — AA-46;
   - `aa:lem:exp-polynomial-constant-field` — AA-45;
   - `aa:tw:hyperexponential-criterion` — AA-45;
   - `aa:tw:pv-airy-group` — AA-46.

**Wynik kontroli odsyłaczy AA-47: 24/24 z rozpoznanym celem.** Nie oznacza to sprawdzenia wszystkich odsyłaczy całej książki.

## Ograniczenia i następne bramki

- Repozytorium nie było dostępne do klonowania w lokalnym środowisku (błąd DNS hosta GitHub), dlatego nie uruchomiono lokalnego pełnego zestawu testów ani kompilacji TeX.
- Brak wykonanej inspekcji stron PDF; brak potwierdzonego pełnego GitHub Actions dla końcowego źródła AA-47.
- W kolejnej iteracji należy zweryfikować dwa zestawy testów regresyjnych, wszystkie etykiety i odsyłacze książki, końcowe CI oraz PDF.

**Werdykt:** struktura i odsyłacze AA-47 przechodzą sprawdzoną kontrolę, lecz AA-47 pozostaje **NIE STABILNY**. Nie otwierać AA-48. Nie zmieniano źródeł, katalogu ani statusów wcześniejszych rozdziałów.
