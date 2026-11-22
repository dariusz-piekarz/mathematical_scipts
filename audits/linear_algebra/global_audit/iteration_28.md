# Algebra liniowa — audyt globalny, iteracja 28: LA29, pierwsza czysta kontrola

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Rozdział:** `chapters/pl/linear_algebra/29-grassmanniany.tex`.
**Niezmieniony blob źródła:** `01213689fb5d2477db25f9ff713608b0171a00c8` (746 wierszy).
**Poprzedni audyt:** iteracja 27 poprawiła precyzję typu różniczki odwzorowania Gaussa w przykładzie paraboli.
**Werdykt:** brak wykrytych nowych usterek matematycznych i językowych; **pierwsza czysta kontrola po poprawce (1/2)**. Oddzielny sceptyczny audyt końcowy +1 jeszcze niewykonany; rozdział LA29 w ramach audytu globalnego pozostaje OTWARTY.

## 1. Niezależny sceptyczny przegląd pełnego rozdziału

Przeczytano wszystkie 746 wierszy, cztery twierdzenia, dwa stwierdzenia, dwie definicje, sześć dowodów, sześć przykładów, dwie uwagi i oba rysunki. Zarejestrowano każdą pozycję dowodową w [rejestrze per-dowodowym](iteration_28_proof_review_29.csv). Oddzielnie sprawdzono:

1. **Mapy wykresowe i topologia (dowód 56–140).** W obydwie strony kryterium \(\pi_P|_L\) odwracalnego, transformacja współrzędnych przez \(D_A^{-1}\), dziedziny map, odtwarzanie \(A\) z macierzy rzutu, zwartość modelu samosprzężonych idempotentów, własność Hausdorffa i drugi aksjomat przeliczalności. Rozważono \(k=0\), \(k=n\), przypadek zespolony i nieortogonalne dopełnienia. Wniosek: bez koniecznej poprawki.
2. **Styczna grassmannianu (213–249).** Porównano dwie przedłużone krzywe \(v(t)\), redukując różnicę pochodnych modulo \(L\). Przy wykresie \(\Gamma(tA)\) otrzymujemy \(D(v)=[Av]\) i niezależność od dopełnienia. Granice \(k=0,n\) dają zerową przestrzeń styczną. Wniosek: bez poprawki.
3. **Wiązki i dokładność (313–332).** Trywializacje \(\gamma^k\) oraz \(V/\Gamma(A)\) mają wyraźne odwrotności; jądro odwzorowania ilorazowego to \(\gamma^k\). Projekcja ortogonalna identyfikuje \(\mathcal Q\) z wiązką prostopadłą, gładko. Wniosek: bez poprawki.
4. **Stiefel, O(n), U(n) (462–489).** Działania grup są przechodnie, stabilizator rozkłada się blokowo, ortonormalizacja dostarcza gładkich lokalnych przekrojów. Zweryfikowano \(k=0,n\). Wniosek: bez poprawki.
5. **Osadzenie Plückera (519–589).** Z niezerowego iloczynu zewnętrznego odtwarza się \(L\) jako zbiór \(w\wedge\xi=0\). Mniejszy minor kontroluje otwartą mapę i odzyskiwanie macierzy wykresu; sprawdzono znak \((-1)^{k-j}\). Odwrotny wzór daje immersję, a zwartość i własność Hausdorffa zapewniają osadzenie topologiczne. Sprawdzono metrykę na rzeczywistej i zespolonej przestrzeni rzutowej. Wniosek: bez poprawki.
6. **Odwzorowanie Gaussa (664–687).** Gładkość \(A(x)=D_QF(x)(D_PF(x))^{-1}\), cofnięcie \(\gamma^m\) i \(\mathcal Q\) do \(TM\) i wiązki normalnej. W przykładzie paraboli poprawne rozróżnienie \(dG_p:T_pM\to T_{G(p)}\mathrm{Gr}_1(\mathbb R^2)\) oraz jego wartości \(dG_p(e_1)\in\operatorname{Hom}(T_pM,\mathbb R^2/T_pM)\), gdzie \(D(e_1)=2[e_2]\). Wniosek: bez poprawki.

**Pozostałe przypadki i kontrprzykłady:** Mapy \(\mathbb {RP}^1\) z przejściem \(b=1/a\); niebanalna tautologiczna wiązka nad \(\mathbb {RP}^1\) i znak funkcji przejścia; \(\mathrm{Gr}_2^+(\mathbb R^3)\simeq S^2\); równanie Plückera dla \(\mathrm{Gr}_2(\mathbb R^4)\), w tym niedekomponowalny \(\xi=e_1\wedge e_2+e_3\wedge e_4\); uniwersalna konstrukcja wiązki przez funkcje odcięcia na zwartej rozmaitości. Brak wykrytych nowych usterek. Nie dodawano opcjonalnej teorii.

## 2. Nowe, niezależne testy dokładne (nie powtarzano poprzedniego generatora)

Skrypt `/mnt/data/la29_global28_independent.py`, SymPy i `random.Random(202611220028)`, wykonał **2855/2855 PASS**, 0 FAIL. W tym:

- 144+144+144+144 kontroli dokładnych idempotencji, symetrii, niezmienniczości wykresu i rekonstrukcji jego współrzędnych dla macierzy wymiernych;
- 627×3 kontroli mniejszych minorów, tożsamości pivota i rozpiętości wykresu;
- 250 równań Plückera oraz kontrprzykład dla niezłożonego wielowektora;
- 42×3 dokładne kontrole zespolonych rzutów hermitowskich;
- trzy rachunki Gaussa na paraboli;
- 18 testów brzegowych \(k=0\) i \(k=n\).

Wynik rachunkowy nie stanowi formalnej certyfikacji Lean. Poprzednia iteracja 27 miała osobny generator z 10 501 dodatnimi kontrolami numerycznymi.

## 3. Walidacja aktualnego bloba w GitHub Actions i rzeczywisty PDF

**[GitHub Actions 45079917894 — completed/success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079917894)** dla commitu `759ed5a94bb65c8695a9cc16fe4cd9086f515d20`, który zawiera dokładnie bieżący blob LA29 `01213689fb5d2477db25f9ff713608b0171a00c8`. Workflow przeszedł testy rozdziałowe, dwa przebiegi składania LaTeX, kontrolę odsyłaczy i eksport. Osobna [walidacja terminologii 45079917920](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45079917920) zakończyła się sukcesem.

Pobrano rzeczywisty artefakt `14776449318` tego CI, zawierający `linear_algebra.pdf` (320 stron A4) i `linear_algebra.log`. **LA29 zajmuje strony PDF 287–294, wszystkie 8/8 wyrenderowano i obejrzano**, w tym powiększenie strony 293 z poprawioną różniczką Gaussa oraz strony 294. Nie dostrzeżono kolizji podpisów, obciętych wzorów ani błędów rozmieszczenia rysunków. Programowe sprawdzenie prostokątów bloków tekstowych: żadnego poza stroną. W logu: **0** `LaTeX Warning`, `Overfull`, `Underfull`, `Undefined control sequence`, `Missing character`, `undefined references`. W porównaniu z wcześniejszym PDF strony 287–292 są identyczne tekstowo i pikselowo, a strony 293–294 różnią się wskutek celowej zmiany i przeniesienia akapitu; nie ma dodatkowej strony.

W bieżącym źródle są **19 unikalnych etykiet**, **20 odsyłaczy** z prawidłowymi lokalnymi celami, sześć zgodnych par `proof`, dwie `figure` i dwie `tikzpicture`. Rejestr katalogu i kolejność rozdziałów zostały objęte zielonym workflow.

## 4. Decyzja i dalsza sekwencja

W ramach **globalnej ewidencji 363/382 dowodów** pozostaje do osobnej lektury 19: LA30 — 3, LA31 — 6, LA32 — 10. **LA29 ma 1/2 czystych audytów po ostatniej korekcie; nie jest jeszcze zamknięty w tej nowej sekwencji.** Kolejny pełny audyt powinien niezależnie powtórzyć kontrolę LA29 na niezmienionym blobie; po osiągnięciu 2/2 wykonać jeszcze dodatkowy, osobny sceptyczny audyt końcowy +1. Dopiero potem wolno przejść do LA30.

Nie modyfikowano źródeł `.tex`. Raport i ewidencja dowodów są jedynymi nowymi plikami; żaden wynik nie jest przedstawiany jako formalnie sprawdzony w Lean.
