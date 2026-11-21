# Topologia ogólna — rozdział 05 — audyt 2

**Data:** 21 listopada 2026 r.  
**Rozdział:** Aksjomaty oddzielania.  
**Wersja:** 0.1 (źródło niezmienione po audycie 1).  
**SHA-256 źródła:** `f41f5bda8d5af272b3d13c3b94cd2007eabbe77a92452d1dc7e5af5ce107a04b`.  
**Objętość:** 632 wiersze LaTeX; 7 stron osobnego rozdziału i 43 strony pełnej książki.

## Matematyka

Przeprowadzono ponowny audyt wszystkich definicji, twierdzeń, dowodów i przykładów: T0, T1, T2, regularność i T3, całkowita regularność i Tychonoff, normalność i T4, Urysohn, przestrzenie metryczne, dziedziczenie własności i przykłady nieodwracalności implikacji. Uwzględniono przypadki pustych przestrzeni, singletonów, zbiorów domkniętych pustych i niepustych oraz przestrzeni niespełniających T1.

- Skontrolowano dowód kryterium Hausdorffa z użyciem przekątnej i ciągłość pary odwzorowań.
- Dla lematu Urysohna sprawdzono indukcję zbiorów U_r, właściwe uporządkowanie parametrów dyadycznych, obie formuły przeciwobrazów i wartości funkcji na rozłącznych zbiorach domkniętych.
- Skontrolowano wzór z odległościami do rozłącznych domkniętych niepustych zbiorów metrycznych, dodatniość mianownika i jawne potraktowanie przypadku zbioru pustego.
- Dla prostej/płaszczyzny Sorgenfreya sprawdzono bazę otwarto-domkniętą, domkniętą dyskretną antyprzekątną, gęstość Q^2 i argument kardynalny wykluczający normalność.
- Potwierdzono poprawność kontrprzykładów: topologia Sierpińskiego, nieskończona topologia koskończona, K-topologia i iloraz R na przestrzeń Sierpińskiego.

**Wynik:** nie wykryto błędów ani nieścisłości wymagających poprawy. Nie dodano nowych twierdzeń, definicji ani przykładów.

## Weryfikacja techniczna

- `bash tools/validate_general_topology_ch05.sh` — PASS; pełna regresja rozdziałów 01–05.
- Skończone modele: 390 topologii (zbiory o liczności 0–4), 5931 sprawdzeń własności podprzestrzeni oraz 4133 sprawdzeń domkniętych par przy normalności — PASS.
- Kontrola unikalności etykiet, rozwiązywalności referencji i terminologii — PASS.
- `latexmk` rozdziału 05 i pełnej książki — PASS; bez `Overfull`, `Underfull`, `LaTeX Warning`, `Undefined control sequence` i `Missing character`.
- PDF ponownie wyrenderowano do 7 obrazów; przeprowadzono kontrolę wszystkich stron i schematów — PASS.

## Decyzja

Audyt 2 **czysty**. Pierwszy z dwóch wymaganych kolejnych czystych audytów: **1/2**. Rozdział 05 pozostaje w stabilizacji; nie wypychamy go jeszcze na GitHuba. Kolejna iteracja: audyt 3 wersji 0.1.
