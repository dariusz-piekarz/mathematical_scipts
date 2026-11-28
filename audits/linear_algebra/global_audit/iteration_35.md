# Algebra liniowa — globalny audyt 35: pierwszy czysty przegląd po ostatecznej korekcie

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Wynik:** CZYSTY (1/2).

## Warunek niezmienności

Na początku tego audytu sprawdzono aktualne pliki kanoniczne i źródła z końcowego artefaktu CI. Bloby ostatecznie poprawionych rozdziałów:
- LA-13: `ddf705004f13f4df7289036d82c13ff64fe89f56`;
- LA-22: `735db5c063d9ac9c148894a8ffdcc681339e9611`;
- LA-23: `0a79284e9d1f0db121800c733ab1fd2cecf0bf5c`;
- LA-32: `9ed35f18a5300f6e9ee70e8654ef0092e260af2f`.

Nie zmieniono podczas audytu źródeł matematycznych, etykiet, formuł ani ilustracji. Końcowe trzy stare wystąpienia `{k\\choose j}` w LA-22 i LA-23 zastąpiono już przed audytem przez `\\binom{k}{j}`. Uprzednio wykryte osiem ostrzeżeń zakładek `hyperref` w LA-13 i LA-32 usunięto przez `\\texorpdfstring`. Te prace należą do wcześniejszych iteracji **korekcyjnych 33–34** i nie są zaliczane jako czyste.

## Niezależna kontrola przyczyn poprzednich usterek

W pierwszym kroku audytu po zmianach pobrano z [CI 45133440134](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133440134) faktyczny artefakt `linear-algebra-ch01-ch32`, obejmujący wszystkie 32 pliki źródłowe, główny TeX, log i PDF. Workflow (`3774f90a56fce37490cb795b381338586984c5c0`) ma status `completed/success`; odrębny krok kontrolny „Verify compilation artifact and unresolved references” również zakończył się sukcesem. W workflow dodatkowo sprawdzono, że testy nie modyfikują źródeł TeX przed składem.

Analiza tego *finalnego*, a nie starszego logu:
- 0 `LaTeX Warning`, 0 `Package ... Warning` (w tym `hyperref` i `amsmath`), 0 `Overfull`, 0 `Underfull`, 0 niezdefiniowanych odsyłaczy, 0 brakujących znaków i błędów;
- PDF 320 stron, 261 wpisów zakładek i 0 bloków tekstu poza stronami; zakładki zawierają „Dopełnienia ortogonalne nad R i C”, „Macierze 2x2” i „Kwaternionowa struktura na C4”;
- `382/382` środowisk dowodu z poprawnymi zakończeniami, 1083 unikalne etykiety, 660/660 rozwiązywanych odsyłaczy, 0 wystąpień starej konstrukcji `\\choose`;
- rzeczywisty plik PDF: 1 928 828 bajtów, SHA256 `c9cfb86da685609100793c0eae7b13069fa8edb8a695cbe86556e219f68065b8`.

Obejrzano również wybrane strony 130, 134, 137, 223, 226, 231, 312, 315, 317 i 319, w tym schemat Penrose’a oraz fibracji twistorowej. Nie znaleziono widocznych kolizji podpisów i rysunków; sprawdzono położenie wszystkich bloków tekstowych w pełnym PDF.

## Matematyka bez modyfikacji

Przy kontrolowanych wcześniej hipotezach zweryfikowano bezpośrednio, że zmiana `\\choose` → `\\binom` jest wyłącznie zmianą sposobu zapisu współczynnika dwumianowego w rozwinięciach potęg bloków Jordana oraz operatorów nilpotentnych. Uruchomiono ponownie niezależne dokładne programy:
- `la22_nilpotent_confirm.py`: **853/853 PASS**, nilpotentność `L(X)-R(X)` i wykładnik `a+b-1`;
- `la23_binomial_confirm.py`: **544/544 PASS**, dwumianowe potęgi macierzy Jordana na liczbach wymiernych;
- `la32_independent_checks.py`: **7019/7019 PASS**, wszystkie dziesięć obszarów matematycznych LA-32;
- `la_global_confirming_fast.py`: **13799/13799 PASS**, konwencja półtoraliniowości, rzuty, równania normalne, `J^2=-I` i stereografia.

Wyniki liczbowe są kontrolami poprawności określonych równości, a nie formalizacją w Lean ani automatycznym dowodem wszystkich twierdzeń książki.

**Decyzja:** pierwszy samodzielny czysty przegląd finalnego bloba, **1/2**, bez potrzeby edycji źródeł. Wymagana druga niezależna kontrola na tym samym stanie, następnie dodatkowy audyt sceptyczny.
