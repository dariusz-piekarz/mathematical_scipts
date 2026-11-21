# Algebra abstrakcyjna — AA-14, audyt IV (stabilizacyjny)

**Rozdział:** Pierścienie artinowskie i lokalne oraz lemat Nakayamy.

**Status:** STABILNY MATEMATYCZNIE po czterech iteracjach. Bez zmian źródła między audytami III i IV.

## Niezależna kontrola

- Ponownie sprawdzono wszystkie 15 dowodów, w tym:
  - dziedzina artinowska jest ciałem; ideały pierwsze pierścienia artinowskiego są maksymalne;
  - istnienie ideałów maksymalnych przez lemat Kuratowskiego–Zorna i kryterium jednostek dla radykału Jacobsona;
  - skończoność liczby ideałów maksymalnych pierścienia artinowskiego;
  - nilpotentność radykału Jacobsona i rozkład na pierścienie artinowskie lokalne przez chińskie twierdzenie o resztach;
  - artinowskość implikuje noetherowskość, z uzasadnieniem przejścia od filtracji do generatorów;
  - obie wersje lematu Nakayamy i minimalna liczba generatorów modułu.
- Ponownie zbadano 6 przykładów: skończone pierścienie, pierścienie $K[t]/(t^n)$, $\mathbb Z/12\mathbb Z$, dwa przykłady modułów nad $K[x]_{(x)}$ oraz $K[x,y]/(x,y)^2$.
- Sprawdzono w szczególności trzy uzupełnienia audytu III: pusty łańcuch w lemacie Kuratowskiego–Zorna; anihilator całego $R/(x^3)R$; identyfikację zbioru nieodwracalnych elementów w $K[x,y]/(x,y)^2$.
- **Nie stwierdzono nowych błędów ani luk. Nie zmieniano źródła.**

## Walidacja techniczna

- Powtórzono 42 lokalne testy matematyczne: **42/42 PASS**; istniejące pliki testów z iteracji I–III.
- Do CI opublikowano odrębny zestaw 25 testów regresyjnych: `tools/tests/test_abstract_algebra_ch14.py`. Ich wyniku w GitHub Actions nie należy utożsamiać z lokalnymi 42 testami.
- Lokalnie: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **PASS**. Samodzielny PDF AA-14: **7 stron**.
- W logu: **0 ostrzeżeń LaTeX; 0 Overfull/Underfull**.
- **25 unikatowych etykiet, 11 odsyłaczy do istniejących celów**. Wykonano powtórny render i kontrolę wizualną siedmiu stron.
- SHA-256 źródła lokalnego: `293f41800cd825f272aa45f73c12fb47572a87871e4e044b517c3ce535b9fa15`; SHA Git blob `bd327c84847088000195270dab35e40daa2b73a6`. Opublikowany plik na GitHubie ma identyczny SHA Git blob.

## Integracja

Na gałęzi `biblioteka-matematyczna-iteracja-6`:
- `chapters/pl/abstract_algebra/14-pierscienie-artinowskie-lokalne-i-lemat-nakayamy.tex`;
- `books/pl/abstract_algebra.tex` — dodanie AA-14;
- `catalog/books.json` — 14 rozdziałów;
- `tools/tests/test_abstract_algebra_ch14.py` — 25 kontroli regresyjnych w CI;
- `.github/workflows/abstract-algebra-chapter.yml` — kompilacja książki AA-01–AA-14 i testy rozdziału;
- `README.md` — status 14 stabilnych rozdziałów.

**Zastrzeżenie:** lokalnie kompilowano AA-14 jako osobny rozdział, nie pełną książkę AA-01–AA-14. GitHub Actions dla ostatniego commitu należy zweryfikować osobno; lokalny PASS nie jest dowodem zielonego CI.

## Status globalny

Liczba audytów AA-01–AA-14: **5, 3, 3, 2, 3, 2, 2, 5, 4, 3, 3, 3, 3, 4** (łącznie **45 iteracji**). 14 rozdziałów stabilnych matematycznie. Następny w kolejności: AA-15.
