# Globalny audyt 35 — odwołania opisowe i kolejność rozdziałów

2026-11-24. Baza f2dc13ffd7f461fa5ab3e001e3fe7ec5c3457c83. Przejrzano wszystkie 44 pliki 00–43 pod kątem wzmianek o rozdziałach oraz kolejność input w książce. 00 nienumerowany; 01–05 zachowują numery; 37–43 drukowane jako 6–12; 06–36 jako 13–43.

- 07: ręczne odwołanie do pierwszego rozdziału zastąpiono etykietą.
- 08: nieaktualne „w szóstym” wskazywało BFS/DFS zamiast macierzy incydencji (drukowany 13); obie liczby zastąpiono etykietami.
- 15: odwołanie do wzoru Eulera–Poincarégo w rozdziale triangulacji.
- 18: wielomian Alexandera jest sekcją tego samego rozdziału, nie osobnym rozdziałem.
- 20: po chirurgii Dehna następuje JSJ, nie teoria 4-rozmaitości; wskazano rozdział 22 i sekcję przesuwania uchwytów.
- 21: etykieta rozdziału Bassa–Serre'a.
- 22: następny rozdział to plumbing, nie homologia Floera; wskazano sekcję sec:kt-hfk w rozdziale 35 (drukowany 42).

Poprawne powiązania 02–03, 05–37–43–06, 06–07, 10–09, 23–24, 26–27–28, 29–30, 31–32, 33–34 pozostawiono. Nie zmieniano kolejności ani twierdzeń.

Rozszerzono test globalny o heurystykę pojedynczych liczbowych odwołań do rozdziałów (w tym polskie liczebniki porządkowe 1–10); raportuje i blokuje strict. Wyjątek: nagłówek uwagi w 01 o zakresie pierwszego rozdziału. Heurystyka nie zastępuje semantycznej kontroli wzmianek względnych. Wymagana ponowna kompilacja i kontrola CI; audyt 35 otwarty.
