# Algebra abstrakcyjna — AA-23, audyt III (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Ślad, norma i wyróżnik w rozszerzeniach ciał”.  
**Rezultat:** **czysta iteracja, bez zmiany źródła**. AA-23 uznany za stabilny matematycznie, opublikowany na istniejącej gałęzi GitHub `biblioteka-matematyczna-iteracja-6`.

## 1. Źródło, stan, integralność

- Bazą był kompletny plik `AA-23-audyt-II-zrodlo.tex` po dwóch wcześniejszych audytach (11 dowodów, 8 twierdzeń, 3 lematy, 2 definicje, 7 przykładów).
- Ponowna lektura niezależna objęła każdy dowód, wzór, definicję, przykład, kwantyfikatory, założenia, zależności oraz przypadki stopnia jeden i charakterystyki dodatniej.
- Liczba poprawek treści w audycie III: **0**. Nie dopisano twierdzeń, lematów, definicji ani przykładów.
- Identyczny SHA-256 źródła po audycie II i III: `b7e6d7837bc8841db3acae30cda73e4be19e9bac83968bda5cb7f5be7978be15`.
- Publikacja w GitHub została zweryfikowana po odczycie pliku: blob Git `69f5f2c35c3e7179055e0acc06fe95e041d0bc24`.

## 2. Matematyczna kontrola dowodów

1. **Definicje śladu, normy, wielomianu charakterystycznego:** operatory `m_a` są liniowe nad `K`, dobrze określone; podobieństwo macierzy i rachunek śladu `tr(UV)=tr(VU)` zapewniają niezależność od bazy.
2. **Podstawowe własności:** addytywność i `K`-liniowość śladu; multiplikatywność normy, skalarne wartości `Tr(c)=nc` i `N(c)=c^n` oraz niezerowość normy elementu niezerowego.
3. **Macierz towarzysząca:** przypadek `n=1` rozpatrzony osobno; blokowy schemat poprawny dla `n≥2`; znak `(-1)^n a_0` w normie i ślad `-a_{n-1}` skontrolowane.
4. **Wielomian charakterystyczny i minimalny:** baza `a^j u_i` jest bazą `K`-wektorową `L`; operator mnożenia ma `r=[L:K(a)]` bloków, więc `χ_{a,L/K}=m_{a,K}^r`, bez założenia rozdzielczości.
5. **Przykłady kwadratowe i dwukwadratowe:** sprawdzono stopnie rozszerzeń, dwie normy tego samego elementu względem różnych rozszerzeń, związek z macierzami mnożenia.
6. **Przykłady sześcienne i czysto nierozdzielcze:** użycie kryterium Eisensteina, obliczenie wielomianu minimalnego `X^p-a^p`, zerowość śladu i norma `N(a)=a^p` w charakterystyce `p`.
7. **Twierdzenie o elemencie pierwotnym:** dla `K` nieskończonego wybór współczynnika unikającego skończonego zbioru wartości; przedłużanie zanurzeń i liczba obrazów; dla `K` skończonego cykliczność grupy multiplikatywnej.
8. **Wzory przez zanurzenia:** podobieństwo przez odwracalną macierz Vandermonde'a; rozdzielczość jest jawnie wymagana.
9. **Wyznacznik po ograniczeniu skalarów i przechodniość:** weryfikacja trzech rodzajów operacji elementarnych, w tym znaku zamiany bloków rozmiaru `d`, oraz macierzowego uzasadnienia przechodniości śladu i normy bez rozdzielczości.
10. **Forma śladu:** przy rozdzielczości macierz Grama to `V^T V` po rozszerzeniu skalarów; zmiana bazy daje `S^T G S`; wyróżnik kwadratowej bazy `4d`, a dla bazy `(1,(1+√5)/2)` wynosi `5`.
11. **Ciała skończone:** wzory Frobeniusa dla śladu i normy, surjektywność śladu (niezerowy wielomian stopnia mniejszego od liczności ciała) i normy (cykliczność grupy multiplikatywnej); tabela wartości w `F_4`.

Nie wykryto kołowego rozumowania ani błędnego twierdzenia. Wskazane w audytach I i II braki uzasadnień zostały już poprawione i tym razem nie wymagały zmian.

## 3. Testy i integralność

- **134/134 PASS**: 77 kontroli pierwotnych, 27 testów z audytu II i 30 testów dodanych w audycie III.
- Nowe testy obejmują macierze towarzyszące stopni 1–7, charakterystyczne wielomiany operatorów skalarnych, normy i ślady w rozszerzeniu dwukwadratowym, kwadratowe wyróżniki po zmianie bazy, czysto nierozdzielcze rozszerzenia w charakterystykach 2, 3 i 5 oraz nieosobliwość macierzy formy śladu w `F_4`, `F_8`, `F_9`, `F_16`, `F_25`, `F_27`.
- Wstępnie dwa nowe testy zawierały błędne oczekiwania: przypadek `n=1` w sprawdzeniu śladu macierzy towarzyszącej oraz porównanie postaci rozwiniętej z nierozwiniętą. Naprawiono wyłącznie testy, nie źródło matematyczne.
- Wszystkie 134 testy uruchomiono ponownie w odtworzonym układzie katalogów `tools/tests` i `chapters/pl/abstract_algebra`, za pomocą rzeczywistych poleceń `python -m unittest` użytych w CI.
- **30/30 unikatowych etykiet**, 16 użyć `\ref`/`\eqref`; siedem różnych zewnętrznych celów odnalezionych w AA-11 i AA-20–AA-22. Nie stwierdzono kolizji etykiet AA-23 z rozdziałami AA-01–AA-22 (odczyt źródeł z aktualnej gałęzi).

## 4. LaTeX i PDF

- Dwie pełne kompilacje `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error` pomocniczego dokumentu A4: **PASS**.
- Wynik: **5 stron PDF**, brak ostrzeżeń LaTeX, nierozwiązanych odsyłaczy, przepełnionych i niedopełnionych wierszy.
- Wyrenderowano wszystkie strony, obejrzano zestawienie wizualne. Podgląd samodzielny wykorzystuje tymczasowe etykiety wcześniejszych rozdziałów o numeracji zgodnej z ich bieżącymi źródłami.
- Ograniczenie: nie przeprowadzono odtwarzalnej kompilacji **całej książki AA-01–AA-23**; przygotowano i opublikowano jej workflow. Nie potwierdzono wyniku zdalnego uruchomienia GitHub Actions — **nie oznaczamy CI jako PASS**.

## 5. Publikacja, pliki i następny krok

Opublikowane na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6` repozytorium `dariusz-piekarz/mathematical_scipts`:

- `chapters/pl/abstract_algebra/23-slad-norma-i-wyroznik.tex` — bez zmian względem audytu II.
- `tools/tests/test_abstract_algebra_ch23.py`, `tools/tests/test_abstract_algebra_ch23_extra.py`, `tools/tests/test_abstract_algebra_ch23_independent.py` — razem 134 testy.
- `books/pl/abstract_algebra.tex` — dołączenie AA-23.
- `catalog/books.json` — 23 stabilne rozdziały.
- `README.md` — aktualny status.
- `.github/workflows/abstract-algebra-chapter.yml` — testy AA-23 i kompilacja AA-01–AA-23.
- `audits/abstract_algebra/ch23_iteration_03.md` — niniejszy raport.

AA-23 spełnia ustalone kryterium: **cały rozdział poddano kolejnemu niezależnemu audytowi, który nie wykrył żadnej usterki wymagającej korekty**.

**Następny rozdział:** AA-24, audyt I. Należy najpierw odczytać jego aktualne źródło i stan innych iteracji, aby nie dublować pracy automatyzacji.
