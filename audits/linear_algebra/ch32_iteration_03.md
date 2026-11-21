# Algebra liniowa — rozdział 32, audyt III: niezależny audyt matematyczny (czysty)

**Data:** 22 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/32-twistory.tex`, blob `afab161412aaf5e5d794f64942a65690878af546`. **Brak zmiany źródła.**

## Sprawdzone dowody
1. **Forma wyznacznika:** polaryzacja \(B(X,Y)=ad'+a'd-bc'-b'c\), niezdegenerowanie przez macierze jednostkowe oraz jądro działania par \(SL_2(\C)\times SL_2(\C)\) zostały sprawdzone bez przyjmowania klasyfikacji grup spinowych.
2. **Segre:** współrzędne wszystkich czterech map i ich lokalne odwrotności uzasadniają holomorficzne osadzenie \(\mathbb{CP}^1\times\mathbb{CP}^1\) na kwadryce rzędu jeden.
3. **Dwie rodziny:** niezależne macierze rank-one spełniają \(\det(u\alpha^{\mathsf T}+\lambda v\beta^{\mathsf T})=\lambda\det[u,v]\det[\alpha^{\mathsf T};\beta^{\mathsf T}]\). Obie klasyfikowane rodziny mają wymiar dwa, a nierówność \(\dim W\le2\) wynika z nieosobliwości formy i ortogonalnego dopełnienia.
4. **Incydencja:** w równaniu rzutowym \([X\pi:\pi]=[Y\eta:\eta]\) uwzględniono konieczne skalowanie całego czterowektora; stąd \((X-Y)\pi=0\) i kryterium wyznacznika. Poprawnie rozróżniono przecięcie w jednym punkcie przy \(X\ne Y\) i identyczność prostych przy \(X=Y\).
5. **Przypadek \(\pi=0\):** jawnie opisano prostą \(\ell_\infty\) poza afiniczną relacją incydencji, bez niepoprawnego przypisania jej zwykłemu punktowi \(X\).
6. **Kwadryka Kleina:** minory wykresu dają \([ad-bc:-b:a:-d:c:1]\); podstawienie zeruje równanie Plückera. Otwarta część \(p_{34}\ne0\) ma poprawną odwrotność przez dolny blok jednostkowy.
7. **Flagi:** włókno rzutu na \(\operatorname{Gr}_2\) to \(\mathbb{CP}^1\), a na \(\operatorname{Gr}_1\) to \(\mathbb{CP}^2\). Nie pomylono tych wymiarów z afiniczną płaszczyzną incydencji.
8. **Antyliniowa struktura:** \(J^2=-I\) daje niezależność \(z,Jz\) i brak rzutowych punktów stałych \([Jz]=[z]\). Kwaternionowe prawe działanie przez \(j\) jest spójne z lewym mnożeniem w lokalnym wzorze.
9. **Fibracja:** włókno nad kwaternionową prostą jest \(\mathbb{CP}^1\), lokalna parametryzacja \((q,[v])\mapsto[v,qv]\) jest odwracalna; obliczono jawnie formułę kompleksową i stereografię \(\mathbb{HP}^1\simeq S^4\).
10. **Realności:** nie utożsamiono kwadryki Minkowskiego w hermitowskim \(M_2(\C)\) z euklidesową bazą \(S^4\); nie nazwano gładkiej fibracji holomorficzną.

## Niezależne sprawdzenia
- Wykonany test symboliczny SymPy: \(\det(u\alpha^{\mathsf T}+t v\beta^{\mathsf T})=t\det[u,v]\det[\alpha^{\mathsf T};\beta^{\mathsf T}]\) — **PASS**.
- Wykonany test symboliczny SymPy: równanie Kleina dla wykresu macierzy ogólnej — **PASS**.
- Test CI bezwzględnie liczbowy z etapu wcześniejszego (niezależny od kompilacji LaTeX) objął 7625 kombinacji incydencji, wyznacznika, działania \(J\), mnożenia kwaternionów i postaci hermitowskich — **PASS**.
- Etykiety: 27; sprawdzone: 7 odsyłaczy, wszystkie lokalne lub do stabilnych LA-29 i LA-31.

## Wynik
**Audyt III merytorycznie czysty** i nie spowodował zmian źródła. Po audycie II ponowiony został workflow CI; przed uznaniem całego rozdziału za stabilny należy zakończyć jego kontrolę oraz sprawdzić wszystkie strony samodzielnego PDF.
