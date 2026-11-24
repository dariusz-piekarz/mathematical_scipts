# Audyt CLIV (154) — skład LaTeX
Data 2026-11-24; gałąź biblioteka-matematyczna-iteracja-6.

## Stan potwierdzony przed zmianami
Globalne CI 45386640193: 156/156 unittest (w tym MTG-006), 16/16 skryptów samodzielnych. Pełny PDF z run 45386640177; artefakt 14915624253, ZIP SHA-256 895d900908ff8f5eab10d8e2d7d683e82fc768596490c27cff05f43ad2fda5da potwierdzony. PDF 308 stron, indeks 495 pozycji. Log: 54 Token not allowed, 13 Underfull, 10 Infinite glue shrinkage, 0 Overfull. Wszystkie Underfull w indeksie, wszystkie infinite glue shrinkage w obu dodatkach. Ostrzeżenia hyperref pochodzą z 16 nagłówków w 9 rozdziałach.

## Zmiany
- Jawne alternatywy tekstowe matematyki w nagłówkach rozdziałów 9, 10, 14, 15, 21, 24, 27, 28, 31; texorpdfstring z literalnymi znakami caret/underscore przez string. Nie zmieniono widocznych wzorów. Ostatni commit nagłówków 649438bdc08a57a4b92e1f17f929ce7ab5864c5f.
- Preambuła array (c81c47ba89f8600e464201eea96e300fa190b58a); dokładna szerokość tabel z uwzględnieniem czterech tabcolsep, wyrównanie tekstu do lewej, liczb do prawej: indeks 8e5a21079978bbc5f1f982e6d69a203295f5466a, spis oznaczeń 9cecb16448fe974cff074ef0a3611bc919e276af.
- Lokalny model 226 wierszy longtable na TeX Live 2025/dev: przed 4 Underfull, po 0; obie wersje 0 Overfull. Model nie reprodukuje infinite glue shrinkage, więc ta usterka pozostaje do weryfikacji na CI. Lokalny model zakładek po użyciu literalnych znaków skompilowany dwa razy, bez Token not allowed, odczytane zakładki L^p, C_c^∞, σ-skończoność, 1 < p < ∞.
- Dodano globalny job PDF w istniejącej bramce, obejmujący także dodatki: a165bdef053fce438f02dc2f7d6ce1603aec257b. Kompilacja latexmk, liczniki ostrzeżeń, archiwum PDF/log, bramka Overfull i odsyłaczy. Nie wyciszono ostrzeżeń.

## Następny krok
CLV: sprawdzić CI i log pełnej wersji po wszystkich zmianach; skontrolować ewentualne regresje testów bazujących na literalnych nagłówkach. W szczególności diagnozować pozostałe infinite glue shrinkage, nie uznawać ich za usunięte bez nowego logu. Przejrzeć spis oznaczeń, indeks i zakładki. Potem pełny przegląd PDF wszystkich stron. Stan rozdziałów 31/31, globalna stabilizacja otwarta.
