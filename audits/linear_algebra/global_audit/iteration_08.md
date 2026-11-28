# Globalny audyt algebry liniowej — iteracja 08/09

**Data:** 22 listopada 2026, 08:00 CET.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Wejściowy HEAD:** `de6195ddf77a8b4a10bd5fec81bb7cf1c72ae8fb`.  
**Zakres:** rozdziały 29–32 (grassmanniany, algebry Clifforda, Pin/Spin i spinory, twistory).  
**Wynik:** dwie rzeczywiste poprawki uzasadnień; audyt wizualny i CI po poprawkach otwarte.

## Materiały
Odczytano aktualny HEAD, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raport 07 i tabelę statusów, pełne źródła czterech rozdziałów. Potwierdzono, że raporty 01–07 istnieją, a 08 i 09 nie były wcześniej zapisane. Cztery rozdziały mają odpowiednio 6, 3, 6 i 9 środowisk `proof` (razem 24), a 2, 1, 3 i 2 rysunki w środowiskach `figure`. Przejrzano definicje, twierdzenia, odsyłacze, kluczowe kroki dowodów i konstrukcje TikZ w źródłach. To nie jest formalna weryfikacja każdego zdania ani oględziny każdego renderowanego rysunku.

## LA29 — grassmanniany i Plücker
- Sprawdzono mapy wykresowe i identyfikację \(T_L\operatorname{Gr}_k(V)\cong\operatorname{Hom}(L,V/L)\), konstrukcje wiązki tautologicznej i ilorazowej, osadzenie Plückera, równanie kwadryki w \(\operatorname{Gr}_2(\mathbb K^4)\).
- **Naprawa:** dowód osadzenia Plückera wywodził własność Hausdorffa przestrzeni rzutowej wyłącznie z istnienia atlasu. To logicznie niewystarczające (istnieją rozmaitości lokalnie euklidesowe nie-Hausdorffa). Dodano konkretną metrykę na prostych przez minimum po fazie, dowód nierówności trójkąta i zgodności z topologią map rzutowych. Dopiero z tego i zwartości źródła wynika osadzenie topologiczne.
- W przykładzie \(\operatorname{Gr}_2(\mathbb R^4)\) sprawdzono znaki \(p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}\) i współrzędne wykresu.

## LA30 — algebry Clifforda
- Sprawdzono polaryzację \(vw+wv=-2\langle v,w\rangle\), własność uniwersalną ilorazu \(T(V)/I_q\) i rozpinanie uporządkowanymi monomami.
- Argument niezależności korzysta z \(c(v)=\varepsilon(v)-\iota_v\) na \(\Lambda V\) i wartości \(c(e_{i_1}\cdots e_{i_r})1=e_{i_1}\wedge\cdots\wedge e_{i_r}\); uzasadniono relację antykomutacyjną i anulowanie kontrakcji. W badanych fragmentach nie znaleziono koniecznej korekty.
- Kontrola terminologii nie wykazała niedopuszczonych zamienników w prozie.

## LA31 — Pin/Spin i spinory
- Skontrolowano wzór odbicia \(-uvu^{-1}\), konstrukcję lokalnych podniesień w nakryciu \(\operatorname{Spin}(n)\to\mathrm{SO}(n)\), jądro \(\{\pm1\}\) oraz przykład obrotu o połowę kąta.
- Sprawdzono krok \(\operatorname{Cl}^{\mathbb C}_{n+2}\cong\operatorname{Cl}^{\mathbb C}_n\otimes M_2(\mathbb C)\), działanie elementu chiralości, przejścia wiązki spinorowej i znaków na potrójnych przecięciach. W skontrolowanych argumentach nie wykryto koniecznej korekty.
- Nie deklaruje się pełnego matematycznego domknięcia wszystkich 1496 linii.

## LA32 — twistory
- Skontrolowano formę wyznacznika, macierze rzędu jeden i dwie rodziny płaszczyzn izotropowych, relację \(\ell_X\cap\ell_Y\ne\varnothing\iff\det(X-Y)=0\), współrzędne Plückera wykresów oraz kwaternionową strukturę \(J^2=-I\).
- **Naprawa:** w dowodzie \(\mathbb{HP}^1\cong S^4\) stwierdzano gładkość przy \(\infty\) bez rachunku. Dodano współrzędną \(w=q^{-1}\), jawny wzór \(\Phi(w^{-1})=(2\bar w/(1+|w|^2),(1-|w|^2)/(1+|w|^2))\), obliczenie różniczki w zerze i odwołanie do twierdzenia o funkcji odwrotnej.
- Nie utożsamiano zespolonej relacji incydencji z rozłącznymi włóknami euklidesowej fibracji.

## CI, PDF i rysunki
- Wejściowy HEAD `de6195d` zawierał wcześniejszy udany CI dla `cdf1a096...`: [GitHub Actions 44991538108](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44991538108), `completed/success`; **nie** dotyczy on niniejszych dwóch poprawek.
- Źródła mają łącznie 8 figur; skontrolowano definicje ich środowisk i zawartość TikZ. **Nie potwierdzono wizualnie braku kolizji napisów w PDF.**
- Po commicie należy uruchomić lub sprawdzić CI dla jego SHA. Dopóki wynik nie jest znany, nie oznaczać audytu jako czystego. Nie wygenerowano lokalnie osobnego PDF.

## Następny krok
Iteracja 09: pełny audyt międzyrozdziałowy 01–32, integralność odsyłaczy, terminologia, bibliografia, kontrola pełnego PDF i otwartych oględzin rysunków. Powtórzyć kontrolę LA29 i LA32 po poprawkach, nie deklarować stabilności bez pozytywnego CI i inspekcji.
