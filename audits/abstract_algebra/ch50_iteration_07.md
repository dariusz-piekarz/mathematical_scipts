# AA-50 — audyt VII: nierozkładalny czynnik kwadratowy

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Wykonana niezależna kontrola

W lokalnym środowisku wykonano obliczenia w SymPy 1.14.0 dla q=x+5/(16x²), f=(T+1/(4x))²−x i D=∂x+(q−T²)∂T. Wyróżnik f wynosi 4x. Jego rząd w punkcie x=0 jest nieparzysty, więc nie jest kwadratem w C(x); f jest nierozkładalny. Potwierdzono dokładną tożsamość Df/f=−2T+1/(2x).

Dla u∈{x,x²+1,1/x}, m∈{1,2,3} i F=u f^m sprawdzono H=DF/F=u'/u+m Df/f, niezerowość różnicy między H a m Df/f oraz stopień H względem T równy 1. Wynik: 9/9 kombinacji PASS. Oba pierwiastki w=−1/(4x)±√x spełniają w'+w²=q: 2/2 PASS.

Pierwsza próba testu zakończyła się błędem porównania strukturalnego dwóch równoważnych postaci wymiernych (−4Tx+1)/(2x) oraz −2T+1/(2x). Poprawiono kryterium na s.cancel(różnica)==0, a ponowne wykonanie zakończyło się kodem 0. Nie była to usterka matematyczna.

Jest to test ogólnego lematu o czynnikach wielomianu F, a nie pozytywny przykład trzeciego przypadku algorytmu Kovacica; potencjał ma rząd w nieskończoności −1.

## CI i artefakt

Dwukrotny odczyt uruchomienia 45292640958, job 138105028679: in_progress, 7 kroków success, 1 in_progress, 101 pending. Oba wcześniejsze moduły AA-50, nowa regresja, bramka AA-GLOBAL, kompilacja i archiwizacja są nadal pending. Lista artefaktów jest pusta. Nie przeprowadzono oględzin nowego PDF.

## Werdykt

AA-50 pozostaje W AUDYCIE. Nie zmieniono rozdziału ani konfiguracji trwającego CI. AA-51 nieotwarty. Kolejna iteracja: odczyt zakończonego CI i kontrola wszystkich stron AA-50 w nowym artefakcie.