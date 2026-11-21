# Algebra abstrakcyjna — AA-20, audyt III (stabilizacyjny)

**Rozdział:** „Rozszerzenia ciał i ciała rozkładu wielomianów”.  
**Data:** 22 listopada 2026 r.  
**Status:** stabilny matematycznie po trzech audytach; audyt III bez poprawek źródła.

## Ponowna weryfikacja matematyczna

Skontrolowano ponownie **12 dowodów, 7 przykładów i 4 definicje**. W szczególności sprawdzono:

- twierdzenie o wieży, skończone rozszerzenia algebraiczne i ich przykłady;
- istnienie i jednoznaczność wielomianu minimalnego oraz strukturę $K(\alpha)$;
- konstrukcję $K[X]/(f)$ i jej własność uniwersalną;
- indukcję w dowodzie istnienia ciała rozkładu;
- przykład ciała rozkładu $X^3-2$, w tym wykluczenie pierwiastków rzeczywistych $X^2+X+1$;
- kryterium rozdzielczości przez formalną pochodną, również w dodatniej charakterystyce;
- liczbę elementów ciał skończonych i cykliczność $F^\times$, w tym przypadek $F=\mathbb F_2$.

**Nie wykryto błędnych twierdzeń ani nowych luk.** Źródło zachowano bez zmian; nie dodano nowych twierdzeń ani lematów. SHA-256: `b1691dd7b985a30dda812c8b07591a2b1261ea0462ec85adcde1319367feb324` (takie samo jak po audycie II).

## Testy i kompilacja

- Wykonano 51 testów z audytów I–II i 22 nowe testy niezależne: **73/73 PASS**.
- Przetestowano także układ katalogów odpowiadający repozytorium, z dwiema publikowanymi seriami 51+22: **73/73 PASS**.
- Testy obejmują m.in. arytmetykę i generatory $\mathbb F_4$, $\mathbb F_8$, $\mathbb F_9$, $\mathbb F_{16}$, $\mathbb F_{25}$, Frobeniusa, kryterium Eisensteina, grupy multiplikatywne i przykłady pierwiastków.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **PASS**; 6 stron PDF, 0 ostrzeżeń LaTeX, 0 przepełnionych lub niedopełnionych wierszy.
- **25 unikatowych etykiet i 11 odsyłaczy**. Cztery cele zewnętrzne należą do wcześniejszych AA-11, AA-17 i AA-19.
- Wszystkie strony wyrenderowano i obejrzano: **PASS**, brak kolizji tekstu lub obcięć.

## Publikacja

Gałąź istniejąca: `biblioteka-matematyczna-iteracja-6` w repozytorium `dariusz-piekarz/mathematical_scipts`.

- Źródło: `chapters/pl/abstract_algebra/20-rozszerzenia-cial-i-ciala-rozkladu-wielomianow.tex`.
- Git blob SHA źródła: `8aa1aedc2c07fe032527d2a0b276cf50b0a6dbfd`; zgodny z lokalnym plikiem.
- Testy regresyjne: `tools/tests/test_abstract_algebra_ch20.py` (51) i `tools/tests/test_abstract_algebra_ch20_extra.py` (22).
- Git blob SHA testów: odpowiednio `e0c7301b65fd94a97a73ac8be295ec6a01752d8b` i `db49a4d94d7fc6f72ed69483c417c3b1006f690a`; zgodne z lokalnymi wersjami testowanymi przed publikacją.
- Zaktualizowano `books/pl/abstract_algebra.tex`, `catalog/books.json`, `README.md` oraz workflow CI `.github/workflows/abstract-algebra-chapter.yml` (wraz z instalacją SymPy).

**Ograniczenie CI:** wynik uruchomienia GitHub Actions po push nie został potwierdzony. Lokalny wynik PASS dla pojedynczego rozdziału i testów nie zastępuje pełnej kompilacji książki AA-01–AA-20 w CI.

**Stan globalny:** 20 rozdziałów stabilnych matematycznie, 66 iteracji audytowych. Następny rozdział: AA-21 — przedłużanie zanurzeń i normalność rozszerzeń.
