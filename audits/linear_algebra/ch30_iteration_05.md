# Algebra liniowa — rozdział 30, audyt V (pierwszy czysty po korekcie LaTeX)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/30-algebry-clifforda.tex`, blob `7a0a02da8836336cb43df52e4dc41d6697600bd4` — nie zmieniono.

## Drugi niezależny audyt algebraiczny
1. Odrębnie sprawdzono parzystość ideału obustronnego \(I_q\): mnożniki jednorodne parzyste lub nieparzyste nie mieszają klas modulo 2, mimo że relacje są niejednorodne w stopniowaniu całkowitoliczbowym. Wniosek o rozkładzie \(\operatorname{Cl}^0\oplus\operatorname{Cl}^1\) jest uzasadniony.
2. Stwierdzenie o bazie ma prawidłowe założenia: \(n=0\) włącza jedynkę jako jedyny monom, natomiast podział na podprzestrzenie równego wymiaru sformułowano tylko dla \(n\ge1\).
3. Wykazano alternowanie operatora kontrakcji \(\iota_v\), w tym wyzerowanie pary składników po transpozycji argumentów. Relacje \(\iota_v^2=0\) i \(\varepsilon(v)^2=0\) prowadzą do poprawnego równania \(c(v)^2=-\|v\|^2 I\).
4. Dla każdej uporządkowanej wielokrotności indeksów z bazy ortonormalnej \(c(e_I)1=e_{i_1}\wedge\cdots\wedge e_{i_r}\); daje to niezależność monomów, bez użycia klasyfikacji algebr Clifforda.
5. Antysymetryzacja \(\Lambda V\to\operatorname{Cl}(V)\) jest wieloliniowa i alternująca; norma \(1/r!\) jest poprawna, a na monomach ortogonalnych daje zadaną bazę. Nie utożsamiono mnożeń obu algebr.
6. Przeliczono \(\operatorname{Cl}(\R^1)\cong\C\), \(\operatorname{Cl}(\R^2)\cong\mathbb H\), \(e_2e_1e_2=e_1\), \((e_1e_2)^2=-1\) oraz rozkład \(vw=-\langle v,w\rangle+v\wedge w\).
7. Zależności między wcześniejszymi rozdziałami LA-11 i nowym LA-30 są jawne; komplet 11 etykiet jest unikatowy, a 11 odsyłaczy wskazuje sekcje wewnętrzne lub znane etykiety LA-11.
8. Wzór antysymetryzacji po audycie IV zapisano w osobnym środowisku matematycznym, co eliminuje wcześniejszą długą formułę inline. Kontrola wynikowego PDF i logu LaTeX trwa w bieżącym workflow.

## Obliczenia
Niezależne testy lokalne: 5 461 iloczynów, 6 681 przypadków łączności, 3 450 relacji reprezentacji — wszystkie **PASS**. Regresja w workflow przechodziła do etapu kompilacji PDF.

## Decyzja
**Audyt V matematycznie i redakcyjnie czysty.** Źródło nie uległo zmianie. Przed stabilizacją potrzebny jeszcze audyt VI obejmujący wynik kompilacji i oględziny PDF, bez zmiany tekstu.
