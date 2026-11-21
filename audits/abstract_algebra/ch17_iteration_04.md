# Algebra abstrakcyjna — AA-17, audyt IV (stabilizacyjny)

**Rozdział:** „Moduły nad dziedzinami ideałów głównych i postać Smitha”.  
**Status:** stabilny matematycznie po czterech iteracjach; w audycie IV **nie zmieniono źródła**.

## Audyt matematyczny

Przeprowadzono kolejną niezależną kontrolę dziewięciu dowodów i czterech przykładów. Szczególnie dokładnie sprawdzono:

- Twierdzenie o istnieniu postaci Smitha nad ogólną dziedziną ideałów głównych, z rozdzieleniem odwracalnych bloków Bézouta od trzech typów prostych operacji elementarnych; dowód zakończenia redukcji korzysta z ACC dla ideałów.
- Jednoznaczność postaci Smitha przez ideały minorowe, z uzasadnieniem ich niezmienniczości względem odwracalnych zmian baz.
- Klasyfikację skończenie generowanych modułów: podmoduł torsyjny, wolną rangę, lokalne warstwy $T[p^k]/T[p^{k-1}]$, rekonstrukcję wykładników pierwotnych oraz przypadek bez torsji.
- Przykłady macierzy całkowitych, modułów ilorazowych, wszystkich sześciu klas izomorfizmu grup abelowych rzędu $72$ i ograniczeń hipotez twierdzenia.

W audycie IV nie stwierdzono fałszywych twierdzeń, nowych luk, brakujących hipotez ani usterek redakcyjnych wymagających korekty. Zasada „stabilizacja po iteracji bez poprawek” została spełniona. Nie dodano nowych twierdzeń ani lematów.

## Walidacja lokalna

- 33 testy z audytu I, 12 z audytu II, 18 z audytu III: **63/63 PASS**.
- Odrębny zestaw 18 testów regresyjnych bez zewnętrznych zależności Python, przygotowany do CI: **18/18 PASS**.
- Wspólny przebieg obu grup testów: **81/81 PASS**, przeciwko temu samemu SHA-256 źródła.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **PASS**.
- Samodzielny PDF rozdziału 17 liczy **7 stron**; każda strona została wyrenderowana i skontrolowana wizualnie.
- **16 unikatowych etykiet i 11 poprawnie rozwiązanych odsyłaczy**, przy wykorzystaniu pomocniczych plików `.aux` wcześniejszych rozdziałów.
- Log LaTeX: **0 ostrzeżeń, 0 komunikatów Overfull/Underfull, brak nierozwiązanych odsyłaczy**.
- SHA-256 źródła (identyczny jak w audycie III): `35625b3f581496e6a1e6e87a9235f7e80c4d47abfa8cde92f096ea2d511169f8`.
- SHA identycznego opublikowanego Git blob: `07d654dab3b20ad7016d160b86914f541d8273a5`.

Testy skończonych modeli są testami regresyjnymi, a nie zastępstwem ogólnych dowodów nad dowolną dziedziną ideałów głównych.

## Publikacja

Opublikowano AA-17 na **istniejącej gałęzi** `biblioteka-matematyczna-iteracja-6` repozytorium `dariusz-piekarz/mathematical_scipts`.

Zaktualizowano:

1. `chapters/pl/abstract_algebra/17-moduly-nad-dziedzinami-idealow-glownych-i-postac-smitha.tex`;
2. `books/pl/abstract_algebra.tex` — rozdziały AA-01–AA-17;
3. `catalog/books.json` — 17 wpisów rozdziałów;
4. `tools/tests/test_abstract_algebra_ch17.py` — 18 testów opartych na standardowej bibliotece Python;
5. `.github/workflows/abstract-algebra-chapter.yml` — uruchamianie testów i kompilacja AA-01–AA-17;
6. `README.md` — 17 rozdziałów stabilnych.

**Status GitHub Actions:** niepotwierdzony. Odczyt powiązanych uruchomień z dostępnego konektora jest ograniczony do zdarzeń pull request, natomiast uruchomienia wywołane przez push nie są stąd obserwowalne. Nie należy przedstawiać lokalnego `PASS` jako potwierdzenia pełnego CI książki.

## Status globalny

| Rozdział | Audyty | Status |
|---|---:|---|
| AA-01 | 5 | stabilny |
| AA-02 | 3 | stabilny |
| AA-03 | 3 | stabilny |
| AA-04 | 2 | stabilny |
| AA-05 | 3 | stabilny |
| AA-06 | 2 | stabilny |
| AA-07 | 2 | stabilny |
| AA-08 | 5 | stabilny |
| AA-09 | 4 | stabilny |
| AA-10 | 3 | stabilny |
| AA-11 | 3 | stabilny |
| AA-12 | 3 | stabilny |
| AA-13 | 3 | stabilny |
| AA-14 | 4 | stabilny |
| AA-15 | 3 | stabilny |
| AA-16 | 3 | stabilny |
| AA-17 | 4 | stabilny |

**Łącznie: 55 iteracji audytowych, 17 rozdziałów stabilnych matematycznie.**

Następny rozdział: **AA-18 — „Iloczyn tensorowy modułów i jego własności”**, audyt I.
