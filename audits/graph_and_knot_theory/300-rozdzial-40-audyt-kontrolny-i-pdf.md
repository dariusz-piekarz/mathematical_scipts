# GKT40 — drugi audyt kontrolny i odbiór PDF

Źródło: `chapters/pl/graph_and_knot_theory/33-chirurgia-wzdluz-wezla-i-niezmienniki-czterorozmaitosci.tex`, blob `82eea27c3706afbbca8ef9bfd85efac842ebe7c9`, commit `470f33ad0b1125e21be6e740293307daba6680f2`, 1043 wiersze. Źródło niezmienione. 24 etykiety, 7 różnych celów odsyłaczy rozstrzygniętych jednoznacznie w rozdziale, 44 poprawnie zagnieżdżone środowiska.

## Kontrola rachunków

W Pythonie w dokładnej arytmetyce całkowitej, dla n=1,...,100, porównano współczynniki (1-z+z^2)^n z niezależnym wzorem kombinatorycznym sumy po r: (-1)^(k-2r) C(n,r) C(n-r,k-2r), gdzie max(0,k-n)<=r<=floor(k/2). Druga metoda to iteracyjny splot z (1,-1,1). Sprawdzono równość, symetrię, sumę współczynników równą 1, niezerowość wszystkich współczynników i przedostatni współczynnik -n. Dla drugiej rodziny sprawdzono symetrię, normalizację i tożsamość (1+z) sum_{k=0}^{2n} (-1)^k z^k=1+z^(2n+1). Łącznie 100 par i 20400 współczynników. Kontrolowano argument symplektycznej sumy włóknistej i wcześniejsze uzasadnienia topologiczne na podstawie aktualnego źródła. Nie wykonywano nowej weryfikacji bibliograficznej zewnętrznych twierdzeń w tej iteracji.

## PDF i CI

Pobrano artefakt 15183454036 dla run 45968400261, pełny PDF 402 strony, plik ostrzeżeń 0 bajtów. W PyMuPDF wyrenderowano i obejrzano wszystkie 10 stron rozdziału (PDF 374–383, drukowane 364–373), w tym trzy schematy; brak istotnych usterek składu. Full-book-pdf success. Structural-audit, zadania finite-models i chapter-pdf (45968400010), changed-latex (45968400019) oraz oba zadania aplikacji (45968400130) nadal queued przy ostatnim odczycie. Drugi audyt kontrolny nie wykazał nowych istotnych usterek; formalny odbiór GT pozostaje otwarty do potwierdzenia pozostałych dedykowanych kontroli CI.
