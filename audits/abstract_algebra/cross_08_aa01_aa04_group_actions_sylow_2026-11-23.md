# AA-X08 — niezależna kontrola przekrojowa AA-01–AA-04: działania grup i twierdzenia Sylowa

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Baza:** `7b0ce25633c32a6b205cb649424d8a783a0b337f`.

## Zakres i podstawa
Odczytano bieżące drzewo `chapters/pl/abstract_algebra` (42 źródła, bez AA-43), wykaz `audits/abstract_algebra`, `catalog/books.json`, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` i źródła AA-01–AA-04. Sprawdzono, że wcześniejsze raporty przekrojowe obejmują m.in. AA-25–27, AA-28/32/33, AA-31–36, AA-37–40 i AA-41–42; obecna kontrola dotyczy odrębnego zakresu.

## Integralność odsyłaczy
W AA-01–AA-04 jest odpowiednio **24, 33, 21 i 18** deklaracji `\\label`, a więc **96** deklaracji. Referencje `\\ref`/`\\eqref`/`\\cref`/`\\autoref`: odpowiednio **0, 1, 4 i 2**. Wszystkie siedem wskazanych celów jest zadeklarowanych w tej samej czwórce rozdziałów: `aa:lem:bezout`, `aa:ch:grupy`, `aa:tw:lagrange`, `aa:ch:lagrange-ilorazy`, `aa:tw:orbita-stabilizator`, `aa:tw:centrum-pgrupy`, `aa:prz:akcja-kosety`. Liczby odnoszą się wyłącznie do tych czterech plików, nie do całej książki. Odczytane deklaracje etykiet nie zawierają powtórzeń w tym zakresie.

## Niezależny test skończonych grup
Uruchomiono lokalny skrypt Pythona, generujący wszystkie permutacje `S_3` i `S_4`, obliczający składanie i domknięcie podgrup generowanych przez jedną lub dwie permutacje, a następnie deduplikujący podgrupy Sylowa. Wyniki:
- `S_3`: `n_2=3`, `n_3=1`;
- `S_4`: `n_2=3`, `n_3=4`.
Dla wszystkich czterech przypadków program potwierdził kongruencję `n_p ≡ 1 (mod p)` i podzielność `n_p | |G|/p^a`. Jest to niezależne sprawdzenie konkretnych przykładów AA-04, **nie** komputerowy dowód ogólnych twierdzeń Sylowa. Analiza treści dowodów AA-04: w dowodzie pierwszego twierdzenia Sylowa poprawnie uzasadniono swobodę działania stabilizatora na podzbiorze; w drugim wykorzystano punkt stały na `G/P` bez założenia normalności `P`; w trzecim poprawnie wyprowadzono jedyność punktu stałego działania `P` na zbiorze podgrup Sylowa, używając normalizatora. Nie wykryto sprzeczności w tych sprawdzonych argumentach.

## Kompilacja, PDF, CI i ograniczenia
`pdflatex` jest dostępny lokalnie, lecz pełne źródła repozytorium nie są dostępne w środowisku wykonawczym: `git ls-remote` zakończył się `Could not resolve host: github.com`. Z tego powodu **nie wykonano** kompilacji rozdziałów ani wizualnej inspekcji PDF. **Nie uruchomiono ani nie potwierdzono GitHub Actions.** Kontrola jest przekrojowa i nie zastępuje pełnych iteracji stabilizacyjnych pojedynczych rozdziałów. Nie zmieniano źródeł, etykiet ani twierdzeń; nie deklaruje się nowej stabilności. Brak propozycji nowych twierdzeń.

## Następny krok
Ponownie sprawdzić HEAD i obecność AA-43. Jeśli AA-43 nie ma, wykonać nową, nieredundantną kontrolę przekrojową innych rozdziałów. Po uzyskaniu dostępu do kompletnego checkoutu przeprowadzić kompilację i oględziny PDF. Raport sporządzono na wskazanej bazie; status CI jest niezweryfikowany.
