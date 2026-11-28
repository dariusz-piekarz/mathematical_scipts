# Algebra liniowa — rozdział 32, audyt V (pierwszy czysty po korekcie)

**Data:** 22 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/32-twistory.tex`, blob `4f79d392bcebfcd81b5e973857fd60fe9e98ed4b` — **bez modyfikacji**.

## Niezależne przejście merytoryczne
1. Forma \(q(X)=\det X\) jest kwadratowa i niezdegenerowana w sensie polaryzacji; jądro podanego działania \(SL_2(\mathbb C)^2\) ma dokładnie dwa elementy.
2. Dowód osadzenia Segrego zawiera zarówno bijektywność na kwadrykę rzędu jeden, jak i lokalne odwrotności holomorficzne.
3. Klasyfikacja płaszczyzn izotropowych oparta jest na rachunku \(\det(u\alpha^T+\lambda v\beta^T)\) oraz warunku \(W\subset W^{\perp_B}\). Nie ma niejawnego założenia maksymalności.
4. Warunek przecięcia prostych jest udowodniony bez pominięcia skalowania projektowego; przypadek \(X=Y\) i \(X\ne Y\) rozdzielono.
5. Incydencja jednego twistoru ma włókno wymiaru dwa dzięki surjektywności \(X\mapsto X\pi\); podano jawny przykład.
6. Wyznaczniki wszystkich minorów \(2\times2\) wykresu \(W_X\) dają współrzędne na kwadryce Kleina, a mapa \(p_{34}\ne0\) jest odwracalna.
7. Dla struktur kwaternionowych \(J^2=-I\), bezpunktowa inwolucja \([z]\mapsto[Jz]\), prawostronne działanie \(\mathbb H\) i rzut \(\tau\) są poprawnie rozróżnione.
8. Lokalny wzór \([a:b:sa-\bar tb:ta+\bar sb]\) jest zgodny z lewym mnożeniem kwaternionów, a kwaternionowe mapy podstawy odpowiadają stereografii \(S^4\).

## Kontrole wykonane
- [CI #44960675442](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44960675442): **SUCCESS**, w tym testy matematyczne, katalog, kontrola języka i odsyłaczy oraz końcowy log LaTeX bez Underfull/Overfull.
- Z workflow pobrano artefakt `linear-algebra-current-chapter` ID `14729517524`.
- PDF w \(`/mnt/data/algebra_liniowa_rozdzial_32.pdf`\) ma **6 stron A4**, zero pustych stron i zero bloków tekstu poza granicami.
- Wyrenderowano wszystkie strony (montaż 3×2), obejrzano je w całości, a strony 2, 4 i 6 osobno w powiększeniu; dwa diagramy TikZ są czytelne, bez kolizji z opisami.
- Sprawdzono 27 unikatowych etykiet i brak nieobjętych wcześniejszymi rozdziałami odsyłaczy.
- Testy matematyczne w CI obejmują 7 625 dokładnych zestawów kontrolnych; wyniki PASS.

## Decyzja
**Audyt V czysty.** Brak poprawek do źródła. Do stabilizacji konieczny drugi niezależny czysty audyt VI identycznego bloba.
