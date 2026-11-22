# Algebra liniowa — audyt globalny, iteracja 29: LA-29, drugi czysty przebieg

**Data:** 23 listopada 2026 (Europe/Warsaw). **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Przedmiot:** wyłącznie LA-29, `chapters/pl/linear_algebra/29-grassmanniany.tex`. **SHA bloba źródła:** `01213689fb5d2477db25f9ff713608b0171a00c8` (746 wierszy), identyczny jak w audycie 28. **Wynik:** drugi, odrębny czysty audyt po ostatniej poprawce, **2/2**. Wymagany dodatkowy sceptyczny audyt końcowy (+1) **nie został jeszcze wykonany**. Nie przechodzono do LA-30. Nie zmieniano źródła .tex.

## Pełna krytyczna kontrola sześciu dowodów (zasięg: jeden rozdział)

Niezależnie przejrzano źródło i poprzedni raport, wszystkie cztery twierdzenia, dwa stwierdzenia, dwie definicje, sześć dowodów, sześć przykładów, dwie uwagi i rysunki. Wykorzystano weryfikację logiczną hipotez i typów obiektów oraz osobne testy dokładne. Rejestr krytycznych kroków znajduje się w [pliku per-dowodowym](iteration_29_proof_review_29.csv).

1. **Atlas i topologia (dowód 56–140):** przejścia między dowolnymi rozkładami $V=P\oplus Q=P'\oplus Q'$, odwracalność $D_A$ i wzór $A'=\pi_{Q'}T_A D_A^{-1}$; wzory na $\Pi_L$ oraz odzyskiwanie $A$, zwartość zbioru rzutów samosprzężonych. Sprawdzono także $k=0,n$. Bez nowej usterki.
2. **Styczna jako przestrzeń odwzorowań (213–249):** niezależność od przedłużenia $v(t)$, zależność wyłącznie od $A'(0)$, konstrukcja odwrotna $t\mapsto\Gamma(tA)$, niezależność od dopełnienia. Osobno sprawdzono dokładną różniczkę rzutu w $t=0$. Bez nowej usterki.
3. **Wiązka tautologiczna i iloraz (313–332):** lokalne ramki, klasa modulo wykres reprezentowana przez $\pi_Qw-A\pi_Pw$, zgodność jądra i obrazu oraz identyfikacja z dopełnieniem ortogonalnym. Bez nowej usterki.
4. **Modele Stiefela i ilorazy grup (462–489):** przechodniość działań grup, dokładny stabilizator $\mathrm O(k)\times\mathrm O(n-k)$ (zespolony odpowiednik unitarny), gładkość sekcji otrzymanych z ortonormalizacji ramki wykresu i dopełnienia. Bez nowej usterki.
5. **Osadzenie Plückera (519–589):** transformacja przez $\det C$, znak minorów $(-1)^{k-j}$, rekonstrukcja macierzy wykresu, kryterium $L=\{w:w\wedge\xi=0\}$, iniektywność, immersja i osadzenie. Równanie kwadryki dla $\mathrm{Gr}_2(\mathbb R^4)$ wykorzystuje charakterystykę różną od dwóch; w całym rozdziale $\mathbb K\in\{\mathbb R,\mathbb C\}$. Bez nowej usterki.
6. **Odwzorowanie Gaussa (664–687):** gładkość $G(p)=T_pM$, lokalny rachunek $D_QF(D_PF)^{-1}$ i izomorfizmy cofniętych wiązek. Poprawka z iteracji 27 konsekwentnie rozróżnia $dG_p$ oraz wektor styczny $dG_p(e_1)$, utożsamiany z elementem $\operatorname{Hom}(T_pM,\mathbb R^2/T_pM)$. Bez nowej usterki.

**Przykłady i przypadki graniczne:** skontrolowano dwie mapy $\mathbb{RP}^1$ z przejściem $b=1/a$; funkcję przejścia wiązki Möbiusa; identyfikację $\mathrm{Gr}_2^+(\mathbb R^3)\simeq S^2$; kwadrykę Plückera i niedekomponowalny wielowektor $e_1\wedge e_2+e_3\wedge e_4$; różniczkę dla paraboli oraz konstrukcję odwzorowania klasyfikującego wiązkę nad zwartą rozmaitością. Nie znaleziono nowej usterki ani błędnego uogólnienia.

## Niezależna regresja dokładna wykonana w tym przebiegu

Utworzono i uruchomiono `/mnt/data/la29_global29_skeptical.py` z generatorem `random.Random(202611230029)` (SymPy). **1225/1225 PASS**, 0 błędów. Skontrolowano dokładnie:

- 79 przejść map przy zmianie współrzędnych i 79 badań rzędu, 72 przejścia dla ogólnych nieortogonalnych baz;
- 140 relacji kwadrycznych Plückera, 140 rekonstrukcji parametrów wykresu, 140 transformacji minorów po zmianie bazy i 1 kontrprzykład dla nieskładalnego wielowektora;
- 480 sprawdzeń dobrze określonego ilorazu: niezmienniczość reprezentanta, jądro i surjektywność;
- 35 dokładnych rzutów ortogonalnych i 16 złożonych rzutów hermitowskich;
- 16 sprawdzeń pierwszej pochodnej rzutu w przestrzeni stycznej;
- 24 próby brzegowe (k=0) i (k=n);
- 3 tożsamości dla paraboli: nachylenie stycznej, ortogonalność i unormowanie normalnej.

Pierwsze uruchomienie testu hermitowskiego ujawniło różnicę w *syntaktycznej* postaci wyrażeń SymPy (porównanie macierzy bez uproszczenia); kontrolę poprawiono przez sprawdzanie zerowania każdej różnicy po `sympy.simplify`. Ponowne uruchomienie zakończyło się 1225/1225 PASS. Nie była to usterka źródła matematycznego. Jest to weryfikacja rachunkowa, nie formalizacja Lean ani zastępstwo dowodów.

## LaTeX, odsyłacze, PDF i bieżące CI

Źródło pozostaje niezmienione: 19 etykiet bez duplikatów, 20 wystąpień `\ref/`\eqref (12 lokalnych), brak brakujących lokalnych celów; 6/6 par `proof`, 2/2 `figure`, 2/2 `tikzpicture`. Nie wykryto słów „tensorowanie”, „sekwencja” ani „unia”. Manifest i zgodność odsyłaczy przechodzą CI.

**Potwierdzone GitHub Actions:**
- [45079917894](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079917894), `completed/success` dla commitu z dokładnym blobem `01213689fb5d2477db25f9ff713608b0171a00c8`, w tym dwukrotny LaTeX, walidacja i eksport rozdziału.
- Dodatkowe przebiegi [45081081248](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081081248) i [45081121567](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081121567), oba `completed/success`, wyzwolone kolejnymi zapisami raportów przy niezmienionym źródle.

Pobrany z [CI 45079917894](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079917894) artefakt PDF całej książki ma 320 stron. LA-29 zajmuje strony **287–294**. Skontrolowano zawartość i granice bloków tekstu na wszystkich 8 stronach (0 poza stroną), obejrzano montaż całego rozdziału i osobno powiększenia rysunków na stronach **288** i **291** oraz poprawionego przykładu Gaussa na stronie **293**. Nie stwierdzono nałożenia podpisów, obcięć ani pustych stron. W pliku `linear_algebra.log`: 0 wystąpień `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence`, `undefined references`. Zweryfikowana lokalnie kopia ośmiostronicowego PDF: SHA256 `1539a2386a4e3b686fc4e8e599bf4146292d60409619e272c04043a8d8e46cfc`.

## Decyzja

- **LA-29: druga czysta kontrola po ostatniej poprawce, 2/2.**
- **Osobny dodatkowy końcowy audyt sceptyczny (+1): nieprzeprowadzony.** Zgodnie z globalną zasadą etap pozostaje otwarty do następnego, oddzielnego przebiegu LA-29; bez przejścia do LA-30 w tej iteracji.
- Globalny rejestr matematycznie skontrolowanych dowodów bez zmian: **363/382**, zostało **19** (LA-30: 3, LA-31: 6, LA-32: 10).
- Żadna zmiana źródła .tex ani pozostałych rozdziałów nie była uzasadniona; bez resetowania licznika.

**Ograniczenie:** wynik udanego CI dotyczy źródła, a nie formalnej certyfikacji każdego dowodu. Zapis bieżącego raportu tworzy nowy commit; ewentualne kolejne CI tego commitu trzeba sprawdzić osobno.
