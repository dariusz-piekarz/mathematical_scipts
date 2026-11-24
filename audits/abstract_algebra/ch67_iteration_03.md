# AA-67 — audyt III, etap P (otwarty)

24 listopada 2026 r. Kontynuacja ch67_iteration_02.md, wyłącznie gałąź biblioteka-matematyczna-iteracja-6.

## Audyt potwierdzający
Ponownie sprawdzono uzupełnienie rozkładu wagowego Q: odwzorowanie z sumy prostej ilorazów jest dobrze określone (zmiana reprezentantów daje element N), surjektywne dzięki rozkładowi M, injektywne dzięki rozkładowi N. Każda składowa jest przestrzenią wagową, bo porównanie składowych równania tu=μ(t)u dla wszystkich t eliminuje każdą różną wagę. Najwyższa składowa pozostaje jednowymiarowa. Skończoność wymiarów składowych wynika z ilorazu skończenie wymiarowych przestrzeni. Ponownie sprawdzono argument lokalnej nilpotentności, symetrię wag, średnią Weyla i zastosowanie zupełnej rozkładalności już po dowodzie skończoności Q. Nie stwierdzono nowej usterki matematycznej.

## Usterka składu i poprawka
Starszy run 45453011479, job 138654890515, head 4cff5ecee1bb94614f65188c3054be90ca06b671: odczytano log. 142 kroki success, krok Verify PDF and references (no undefined refs) failure. W końcowym przebiegu pdflatex cztery Overfull hbox po 53.38617 pt while output is active; bramka odrzuciła log. Wstępne ostrzeżenia o odsyłaczach nie stanowiły podanej przyczyny końcowej porażki. Długi tytuł AA-67 bez krótkiego wariantu jest prawdopodobną przyczyną (analogiczne krótkie tytuły w AA-62–65). Dodano krótszy wariant tytułu do spisu treści i nagłówka, zachowano pełny tytuł na początku rozdziału. Dodatkowo rozbito nowy wzór izomorfizmu na dwa wiersze aligned, profilaktycznie dla szerokości składu. Commit a1bb477d92c67b8a7812eec8b69d50f68d3f88af, blob 991e3acb1c390cf37b43be2ee136515cb5b82d53. Porównanie z poprzednim źródłem: wszystkie 8 etykiet i 20 wystąpień odsyłaczy identyczne, PASS. Obowiązująca trwała regresja składu w workflow już odrzuca Overfull hbox/vbox, więc nie dublowano bramki. Skuteczność poprawki wymaga wyniku nowego CI.

## Regresje wykonane ponownie
- test_abstract_algebra_ch67.js, blob c0b8ba0f08e218b870555011654d881a8d2c1a4d: PASS, 21 modeli sl2, 231 kontroli komutatora, 231 jąder, 15 modeli A2, 155 przestrzeni wagowych, 310 symetrii, 30 relacji najwyższej wagi; AA-67-QW-01: PASS, 81 nośników, 405 projekcji, 2565 kontroli współrzędnych.
- test_abstract_algebra_ch67_independent.js, blob ae760b53bd8774a1937eb2f33de5a71d4c837fa4: PASS, 7 układów, 104 elementy grup, 196 wag dominujących, 5096 elementów orbit z krotnościami, 16087 zaakceptowanych i 30981 odrzuconych kandydatów, 138012 kontroli współczynników.
Skrypty rzeczywiście wykonano w środowisku JavaScript. Nie jest to formalizacja Lean.

## Bramka
Run 45454620156 dla a1bb477d92c67b8a7812eec8b69d50f68d3f88af: in_progress przy sprawdzeniu. Brak nowego potwierdzonego PDF i oględzin. AA-67 nie jest jeszcze stabilny, AA-68 nieotwarty. Następnie odczytać końcowy wynik CI, pobrać artefakt, obejrzeć wszystkie strony AA-67 i zweryfikować brak usterek składu. Nie zaliczać audytu na podstawie samego uruchomienia CI.
