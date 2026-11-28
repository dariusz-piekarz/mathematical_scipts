# Algebra liniowa — rozdział 23, audyt III (niezależny przegląd po korekcie II)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/23-dyskretne-rownanie-lapunowa-i-stabilnosc-schura.tex`  
**Kontrolowany blob:** `8939984648cdd1c38ee57702b3b11ff38d9a4238`.  
**Wcześniej:** audyt I (korekta oszacowania przy \(k=0,d=1\)), audyt II (jawne uzasadnienie \(\lambda^0=1\) przy \(\lambda=0\)).

## Matematyka — powtórna kontrola bez korzystania z wcześniejszych wniosków

1. **Warunki spektralne.** Wszystkie twierdzenia o wartościach własnych sformułowano dla macierzy zespolonych stopnia \(n\ge1\). Nie stosuje się nierozstrzygalnych bez dodatkowych konwencji maksymalizacji po pustym zbiorze wartości własnych.
2. **Równoważność \(\rho(A)<1\) i \(A^k\to0\).** Dla bloku \(\lambda I+N\) wzór dwumianowy ma tylko składniki \(0\le j\le\min(k,d-1)\). Przy \(\lambda=0\) wyraźnie określono czynnik \(\lambda^0\), a \(J_d(0)^k=N^k\). Właściwe jest oszacowanie \((1+k)^{d-1}(\delta/r)^k\), które jest ograniczone dla \(\delta<r\). Powrót przez podobieństwo zachowuje tempo geometryczne po powiększeniu stałej.
3. **Twierdzenie dyskretne Lapunowa.** Dla macierzy Schura każdy wyraz \((A^*)^kQA^k\) jest hermitowski i nieujemnie określony, a pierwszy jest dodatni. Szereg zbiega bezwzględnie z normowego oszacowania geometrycznego. Indeksowe przesunięcie jest zgodne z \(A^*PA=P-Q\). Różnica dowolnych dwóch rozwiązań zeruje się przez iterację; konieczność stabilności wynika ze ścisłej dodatniej określoności \(P,Q\) i wybranego wektora własnego.
4. **Energia i zbieżność.** Nie zakłada się niesłusznie \(E_{k+1}<E_k\) po osiągnięciu stanu zerowego. Dowód oddziela \(x_k=0\) od \(x_k\ne0\). Oszacowanie \(z^*Qz\ge\eta z^*Pz\) i \(P-Q=A^*PA\ge0\) daje \(0<\eta\le1\), stąd \(\gamma=1-\eta\in[0,1)\) i zbieżność geometryczną. Sumowanie teleskopowe jest poprawne.
5. **Operator Steina.** Na podstawie zespolonej postaci Schura \(A=UTU^*\) operator \(X\mapsto A^*XA\) jest sprzężony z \(Y\mapsto T^*YT\). W bazie macierzowych jednostek \(E_{ij}\), współczynniki o parach indeksów wcześniejszych leksykograficznie są zerowe. Diagonalne współczynniki to \(\overline\lambda_i\lambda_j\). Kryterium odwracalności jest więc dokładnie \(\overline\lambda_i\lambda_j\ne1\), niezależnie od stabilności.
6. **Przykłady algebraiczne.** Dla \(\operatorname{diag}(2,1/3)\) wszystkie produkty wartości własnych są różne od 1 i rozwiązanie \(\operatorname{diag}(-1/3,9/8)\) jest poprawne, lecz nie jest dodatnio określone. Dla \(\operatorname{diag}(2,1/2)\) powstają dwie swobodne współrzędne pozadiagonalne. Dla nilpotentnego \(A\) suma szeregu jest skończona.
7. **Przykład nienormalny.** Dla \(A=[[1/2,1/2],[0,1/4]]\) i \(Q=I\) rozwiązanie \(P=[[4/3,8/21],[8/21,32/21]]\) spełnia równanie dokładnie; \(\det P=832/441\), a kwadratowa forma \(\frac43|x+\frac27y|^2+\frac{208}{147}|y|^2\) uzasadnia dodatnią określoność również nad \(\mathbb C\).
8. **Czas ciągły a dyskretny.** Wielomianowa postać \(e^{h(\lambda I+N)}\) ma wyrazy diagonalne \(e^{h\lambda}\); warunek Hurwitza jest więc równoważny Schurowi dokładnego próbkowania dla dowolnego \(h>0\). Dla jawnego Eulera własność wyznacznika daje wartości własne \(1+h\lambda\); warunek \(|1+h\lambda|<1\) prowadzi do właściwego dodatniego progu \(-2\operatorname{Re}\lambda/|\lambda|^2\) przy stabilnym \(H\).

## Integracja i testy

- 965 linii LaTeX, **25 różnych etykiet**, **12 odsyłaczy** oraz **7 poprawnie sparowanych dowodów**.
- Nie znaleziono nazw terminologicznie zabronionych przez `AGENTS.md`, ani nieuzasadnionych nowych symboli.
- Regresja `tools/test_linear_algebra_discrete_lyapunov.py` sprawdza niezależnie wyznacznik operatora Steina przez rangi i względną pierwszość wielomianu charakterystycznego z wielomianem odwrotnym nad małymi ciałami, a także ułamki w przykładach i 12 kroków tożsamości energii.

## Decyzja

**Audyt III czysty matematycznie i redakcyjnie**, bez kolejnych zmian źródła. To **pierwsza czysta iteracja** po poprawce z audytu II. Końcowa walidacja CI, brak ostrzeżeń TeX i kontrola osobnego PDF pozostają niezbędne do stabilizacji.
