# Algebra liniowa — rozdział 27, audyt IV (terminologia)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`  
**Blob po korekcie:** `f4503d54238a2c67d96d7e0cc9441db0181d1eac`.

## Wynik kontroli języka

W Stwierdzeniu `prop:lin27-noise` pierwotnie użyto sformułowania „ma jednoznaczny minimizer”, zaczerpniętego z angielskiej terminologii. Poprawiono je na **„ma dokładnie jeden punkt minimum”**. Zmiana nie wpływa na definicję, założenia, równanie normalne, oszacowanie błędu ani dowód rzutowy.

Ponownie sprawdzono przyjęte globalnie reguły: „przestrzeń sprzężona” i „odwzorowanie dualne” w odpowiednim znaczeniu; terminologię „ciąg”, „mapa współrzędnych”, „odwzorowanie”; brak zabronionego „tensorowania” i samodzielnego angielskiego „dual”. W bieżącym rozdziale nie występują niedozwolone sformułowania. Wszystkie etykiety są stabilne.

W poprzednim audycie III naprawiono brakujący krój `\mathscr`; nowa wersja używa `\mathcal H_{r,s}` bez dodatkowych pakietów. W poprzednim audycie II dopisano dokładne uzasadnienie zbieżności wymiarów dwóch realizacji minimalnych.

## Decyzja

**Audyt IV wymagał korekty językowej, dlatego nie jest czysty.** Do stabilizacji należy uzyskać dwa niezależne czyste audyty na aktualnym blobie `f4503d54238a2c67d96d7e0cc9441db0181d1eac` oraz zielone CI i skontrolowany PDF.
