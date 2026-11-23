# Analiza funkcjonalna — rozdział 15 — audyt 02 (niezależny przegląd i bramka CI)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez nowej gałęzi).  
**Źródło:** `chapters/pl/functional_analysis/15-pochodne-wyzszych-rzedow-i-lokalne-twierdzenia-analizy-nieliniowej.tex`.  
**Niezmieniony blob źródła 15/01–15/02:** `39f14f53417fd613006032d5cb5e9b7bbdcc6ebe`.  
**Niezmieniony blob testów:** `b077bed8553d8122a86a3d7dd4dab1dc052a73b5`.

## Punkt wyjścia i usterka infrastruktury

Rozdziały 01–14 były stabilne po dwóch czystych audytach i zielonym dedykowanym CI. Raport 15/01 udokumentował przegląd 12 dowodów i 5 przykładów oraz dodanie czterech regresji, ale bez potwierdzonego wykonania testów/kompilacji. Ponowny odczyt rzeczywistego drzewa gałęzi wykazał brak pliku `.github/workflows/functional-analysis-ch15.yml` (istniały jedynie workflow 01–14). Jest to **rzeczywista luka techniczna**, a nie usterka dowodu.

W commicie [84ffe4e](https://github.com/dariusz-piekarz/mathematical_scipts/commit/84ffe4e67cb17d273b95849653a224288dfb22a6) dodano dedykowany workflow 15, bez modyfikacji matematycznego źródła: uruchamia `test_functional_analysis_ch15.py`, tworzy rzeczywisty wrapper LaTeX z **pierwszych 15 rozdziałów** książki, kompiluje go, sprawdza błędy LaTeX i niezdefiniowane odsyłacze, weryfikuje wybrane nagłówki w PDF i publikuje artefakty diagnostyczne. Ścieżki wyzwalające uwzględniają rozdziały 01–15, test 15 i raporty 15.

## Ponowny niezależny audyt matematyczny

1. **Kryterium ograniczoności wieloliniowej:** normalizacja argumentów niezerowych i ciągłość w zerze dają stałą `(2/delta)^m`; przy dowolnym zerowym argumencie wieloliniowość zeruje wartość. Zupełność wymaga i wykorzystuje zupełność F, a nie E.
2. **Utożsamienie wieloliniowe:** dwie normy są równe przez iterowane supremum; operator odwrotny definiuje się przez podstawienie pierwszego argumentu.
3. **Pochodne symetryczne:** podwójny przyrost prostokątny i dwa porządki całkowania dają symetrię `D²f`; indukcja dla `D^mf` obejmuje wszystkie transpozycje sąsiednie.
4. **Druga pochodna złożenia:** typy operatorów w obu składnikach zgadzają się; składanie operatorów jest ciągłym odwzorowaniem dwuliniowym.
5. **Taylor:** `gamma(t)=f(x+th)` ma kolejne pochodne `D^jf(x+th)[h^j]`, a całkowanie iterowane daje wagę `(1-t)^{m-1}/(m-1)!`; po odjęciu stałej pochodnej oszacowanie reszty ma poprawny czynnik `1/m!`.
6. **Minimum:** warunek `D²f(x0)[h,h] >= c||h||²` jest jednostajny po kierunkach; sama ścisła dodatniość bez `c>0` nie wystarcza. Przykład na `l²` dowodzi tej różnicy.
7. **Neumann i otwartość odwracalnych:** sumy częściowe są obustronnymi przybliżonymi odwrotnościami; poprawna faktoryzacja to `A+H=A(I+A^{-1}H)`; błąd pochodnej odwracania ma rząd `O(||H||²)`.
8. **Funkcja odwrotna:** wybrana domknięta kula jest zupełna; `q<1` daje kontrakcję, jednoznaczność i dolne oszacowanie Lipschitzowskie. Otwartość `f(U0)` wynika z zastosowania tej samej kontrakcji na małych kulach wokół każdego punktu, nie z samej ciągłości `f`. W różniczkowaniu odwrotności użyto `||h||<=C||k||`, a nie odwrotnej, nieuzasadnionej nierówności.
9. **Regularność wyższa:** indukcja z `Dg=(Df circ g)^{-1}` jest poprawna lokalnie, z odwracaniem w przestrzeni ograniczonych izomorfizmów.
10. **Funkcja uwikłana:** blokowo trójkątny operator `(h,k)->(h,Bh+Ak)` ma jawną ograniczoną odwrotność; wybór mniejszych prostokątów zapewnia równoważność `F(x,y)=0 iff y=phi(x)`. Wzór na pochodną otrzymuje się po zróżniczkowaniu tożsamości `F(x,phi(x))=0`.

**Werdykt matematyczny:** 12/12 dowodów skontrolowano powtórnie i niezależnie od raportu 15/01; brak nowej poprawki merytorycznej wymagającej zmiany źródła.

## Przykłady i struktura

W pięciu przykładach sprawdzono: wzór na pochodną wielomianu wieloliniowego i czynnik `m!` dla symetrycznego B; symetryczną część `(A+A*)/2` hesjanu; obliczenie `f(te_n)=t²/(2n)-t³<0` dla `t=1/n`, `n>=2`; pochodną `Df(0)=I` dla mapy `x+||x||²v`; oraz `u'(0)=Kg` i `u''(0)=2K²g` z równania `(I-lambda K)u=g`. **5/5 przykładów bez nowej usterki.**

Automatycznie odczytano rzeczywiste źródła **01–15** i porównano wszystkie odsyłacze: **302 etykiety, 0 duplikatów; 124 odwołania, 0 nierozwiązanych**. W samym rozdziale 15: 12 par środowisk `proof`, 4 `twierdzenie`, 4 `stwierdzenie`, 2 `lemat`, 2 `definicja`, 3 `wniosek`, 5 `przyklad`, 1 `uwaga`; wszystkie poprawnie sparowane. Rozdział 15 nie zawiera rysunków TikZ. Kontrola terminologii nie ujawniła niedopuszczonych zapisów.

## Bramki i decyzja

Pierwszy uruchomiony workflow rozdziału 15 to [GitHub Actions #45279699756](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45279699756), na commicie `84ffe4e`. W chwili przygotowania raportu rzeczywiście potwierdzono przejście kroków uruchomienia testów i przygotowania kontekstu 01–15; kompilacja LaTeX wciąż trwała. **Nie przedstawiać przebiegu w toku jako zakończonego sukcesem**.

**15/02: pierwszy niezależny czysty przegląd matematyczno-redakcyjny na niezmienionym blobie, warunkowo 1/2.** Rozdział pozostaje **NIESTABILNY**, dopóki nie zakończy się pozytywnie workflow i nie odbędzie drugi czysty audyt 15/03 (z kontrolą faktycznego PDF). Nie przechodzić do 15A ani 16. Ten audyt nie dodaje nowych twierdzeń ani lematów, a w szczególności nie wdraża przedwcześnie zaplanowanego pierwiastka operatora z rozdziału 32.
