# Algebra abstrakcyjna — AA-15, audyt III (stabilizacyjny)

**Rozdział:** Pierścienie nieprzemienne i algebry grupowe.  
**Status:** stabilny matematycznie po 3 audytach, bez zmian źródła względem audytu II.

## Zakres

- Niezależnie sprawdzono wszystkie **11 dowodów** i **7 przykładów**.
- Szczególnie zweryfikowano poprawki audytu II: trzy rodzaje ideałów generowanych przez element, wyznaczenie jądra i obrazu homomorfizmu, jednostki macierzowe w pierścieniu nieprzemiennym oraz dowód `K⟨x,y⟩/(xy−yx)≅K[x,y]`.
- Potwierdzono własność uniwersalną pierścienia grupowego przy założeniu obrazu skalarów w centrum, własność uniwersalną wolnego pierścienia, poprawność pierścienia przeciwnego i przykład nilpotentności w charakterystyce `p`.
- Nie wykryto nowych błędów ani luk dowodowych. Nie zmieniano pliku źródłowego.

## Walidacja lokalna

- Zestaw testów audytu I–II: **36/36 PASS**.
- Dodatkowe niezależne testy audytu III: **10/10 PASS**; **46/46 PASS** łącznie (`python -m unittest discover -s . -p 'test_aa15*.py' -v`).
- Modelowe kontrole obejmują: `M_2(F_2)`, `M_2(Z/4Z)`, ideały `Ra`, `aR`, `RaR`, pierścienie grupowe `C_p` oraz `Z/4Z[C_2]`, pierścień przeciwny i redukcję słów `yx→xy`.
- Lokalna kompilacja samodzielnego AA-15 (`latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`) — **PASS**; **6 stron**, **0 ostrzeżeń LaTeX**, bez `Overfull`/`Underfull`.
- **25 unikatowych etykiet**, **2 poprawne odsyłacze** i wizualna kontrola wszystkich 6 stron.
- SHA-256 źródła po audycie II i III: `2391ce84e17bf375367f5653f920abffe40102c4232f5a7d5258bf50052decf0`.
- Git blob SHA opublikowanego źródła: `b055965112ca86a86e6d0a88213a8274b9d09a68` — potwierdzono zgodność z wersją lokalną.

## Integracja na GitHubie

Istniejąca gałąź: `biblioteka-matematyczna-iteracja-6`, bez tworzenia nowej gałęzi.

- `chapters/pl/abstract_algebra/15-pierscienie-nieprzemienne-i-algebry-grupowe.tex`
- `books/pl/abstract_algebra.tex` — dodano `\\input` AA-15
- `catalog/books.json` — 15 rozdziałów
- `tools/tests/test_abstract_algebra_ch15.py` — **18 odrębnych testów regresyjnych** dodanych do CI
- `.github/workflows/abstract-algebra-chapter.yml` — kompilacja i testy AA-01–AA-15
- `README.md` — 15 stabilnych rozdziałów

**Granice weryfikacji:** Lokalnie przeprowadzono 46 testów, lecz nowy zestaw 18 testów GitHub jest osobnym plikiem i jego wykonanie w GitHub Actions wymaga potwierdzenia. Nie uruchomiono lokalnej kompilacji pełnej książki AA-01–AA-15. Wynik workflow push CI nie został jeszcze zweryfikowany; lokalny PASS nie stanowi dowodu zielonego GitHub Actions.

## Stan globalny

AA-01–AA-15: liczby audytów odpowiednio `5, 3, 3, 2, 3, 2, 2, 5, 4, 3, 3, 3, 3, 4, 3` — razem **48 iteracji** i **15 rozdziałów stabilnych matematycznie**.
