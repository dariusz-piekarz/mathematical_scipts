# Rozdział 14 — audyt 21 (poprawkowy, 0/2)

Data: 24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6.
Użytkownik potwierdził kolejność 14, 15, 15A, 15B, 16 itd. Zakres rozszerzeń zamknięty zgodnie z raportem 20 (8e498fbdbedc823f96905ccaedb15ab0e20ac932). Każdy rozdział stabilizować osobno: dwa czyste audyty i potwierdzona technika przed przejściem dalej.

## Audyt całego rozdziału
Źródło wejściowe abe9d33dce13a6e884f73da41859ec9f6ed29abb. Sprawdzono definicje, implikacje, wszystkie kontrprzykłady, reguły rachunku, krzywe klasy C1, normę i gradient, przypadek zespolony, pochodne słabe i rachunek Bastianiego.
21 celowanych korekt: samodzielne założenia trzech podstawowych definicji; jawna kula jednostkowa; wykazanie ciągłości i normy funkcjonału w przykładzie l1; oszacowania reszt kombinacji liniowej i produktu odwzorowań; pełne kryterium Cauchy'ego sum Riemanna przez wspólne rozdrobnienie; jawny ciąg wykazujący nieciągłość pochodnej; dowód surjektywności operatora samosprzężonego z dolnym ograniczeniem oraz jednoznaczności minimizatora energii; jawna definicja pochodnej słabej-* i zakres przyrostów, określenie dziedzin krzywych, użycie Banacha–Steinhausa na przestrzeni Banacha X', pełna reprezentacja przy ciągłej pochodnej słabej i słabej-*; jednorodność, addytywność i jednostajność względem parametru w dowodzie pochodnej Bastianiego. Nie dodano żadnych opcjonalnych tematów.
Weryfikacja pozostałych kontrprzykładów: g(x,x^3)=1/2, f(x,x^2)=x/2, q jednorodna nieliniowa, l1 reszta względna 1, zespolona pochodna modułu kwadratowego w zerze, słabo zbieżne e_n, obcięcia jedynek w c0. Nie stwierdzono błędów w tych argumentach.

## Technika
CI dla wersji wejściowej: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45352330855, job 138301613151, 9 kroków zaliczonych, 20 testów OK, 3 przebiegi pdflatex, 136 stron. Artefakt 14901001991 pobrany i rozpakowany. Log: jedno znane underfull hbox (1127); brak overfull, brakujących znaków, niezdefiniowanych odsyłaczy. Obejrzano strony 78–85 obejmujące cały rozdział 14, w tym rysunek na stronie 80; układ czytelny, brak kolizji. Oględziny dotyczą wersji sprzed korekt.
Źródło commit 8cdb183057a55bad95529a8d1ba25f2532009d1c, blob 4d1688c83f898df4d2f3f0a4cdbaa353242ffb7a; 475 wierszy, 36 etykiet zachowanych, 15 dowodów, środowiska zagnieżdżone poprawnie. Test commit 8ec61d3f445b242bed7f82ef60ca72f0ba349b1c, blob 57d96256979075b09958c6a2927daa16d4f239ae; 21 testów, nowe kontrakty źródła i rachunek energii w R2. Nie potwierdzono jeszcze nowego pełnego wykonania testów i PDF. Odczyt CI: [{"id":45353027827,"sha":"8ec61d3f445b242bed7f82ef60ca72f0ba349b1c","status":"in_progress","conclusion":null},{"id":45352917962,"sha":"8cdb183057a55bad95529a8d1ba25f2532009d1c","status":"in_progress","conclusion":null}].

## Decyzja
14: 0/2, następny audyt 22 nadal rozdziału 14. 15, 15A, 15B: 0/2, oczekują w ustalonej kolejności. 16 i dalsze po stabilizacji poprzedników. Żadnych nowych rozszerzeń w tej rundzie.
