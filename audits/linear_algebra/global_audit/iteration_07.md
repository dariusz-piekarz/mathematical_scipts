# Globalny audyt algebry liniowej — iteracja 07/09

**Data:** 22 listopada 2026, 07:00 CET.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Wejściowy HEAD:** `fd4e4a7121c3852b428b1bdeab450dd6257cc79c`.  
**Zakres:** rozdziały 25–28.  
**Wynik:** wykonano audyt źródeł, nie stwierdzono koniecznej poprawki matematycznej; wizualny audyt PDF pozostaje otwarty.

## Materiały i metoda

Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raporty globalnych iteracji 01–06 i `status.md`, pełne źródła LA25–LA28 oraz odpowiadające im cztery testy regresyjne. Sprawdzono strukturę **46 środowisk proof** (17+9+10+10), nagłówki i założenia twierdzeń, jawność odsyłaczy i wybrane kluczowe argumenty matematyczne. Nie jest to formalna weryfikacja każdego zdania linia po linii.

## Kontrola matematyczna

### LA25 — sterowalność i obserwowalność
- Weryfikacja argumentu Cayleya–Hamiltona w dowodzie niezmienniczości przestrzeni osiągalnej i równoważności warunków Kalmana.
- Dla gramiánu ciągłego sprawdzono tożsamość \(\ker W_T=\ker\mathcal K(A,B)^*\) i konstrukcję sterowania \(u(s)=B^*e^{(T-s)A^*}W_T^{-1}(z-e^{TA}x_0)\). W przykładzie łańcucha \(A^2=0\), \(B=e_2\) otrzymuje się \(W_T=\bigl(\begin{smallmatrix}T^3/3&T^2/2\\T^2/2&T\end{smallmatrix}\bigr)\) i \(\det W_T=T^4/12>0\).
- Sprawdzono dualność obserwowalności i sterowalności, argument anihilatora w kryterium PBH oraz rozdzielenie nieosiągalnych trybów stabilnych.
- W konstrukcji rozmieszczania biegunów potwierdzono logiczną rolę rozwinięcia rezolwenty przy nieskończoności: tożsamościowe znikanie \(\varphi(H-\mu I)^{-1}D\) wymusza \(\varphi H^kD=0\) dla wszystkich \(k\), co przeczy sterowalności. Indukcyjny wybór wektorów \(v_j\) jest uzasadniony.

### LA26 — uogólnione równania Riccatiego
- Zweryfikowano jawne założenia \(Q=Q^*\ge0\), \(R=R^*>0\), stabilizowalność i wykrywalność. Nie narzuca się błędnie \(Q>0\).
- Skontrolowano formuły sprzężenia \(K=(R+B^*PB)^{-1}B^*PA\) w DARE i \(K=R^{-1}B^*P\) w CARE, argument monotoniczności skończonego horyzontu i zakres stwierdzeń o jednoznaczności rozwiązania stabilizującego.
- Sprawdzono rozdzielenie kosztu na \(x_0^*Px_0\) oraz nieujemną sumę kwadratów i rolę zaniku wyrazu końcowego. Testy dokładne dla półokreślonego \(Q\) są obecne w repozytorium.

### LA27 — gramiany i realizacje minimalne
- Potwierdzono faktoryzację \(\mathcal H_{n,n}=\mathcal O(C,A)\mathcal K(A,B)\) i wzór na jej rangę przez ograniczenie \(\mathcal O\) do przestrzeni osiągalnej.
- Skontrolowano konstrukcję podobieństwa realizacji minimalnych na bazie parametrów Markowa i warunku obserwowalności.
- W dowodzie równoważenia: \(L=W_c^{1/2}\), \(S=LW_oL\), \(U^*SU=\Sigma^2\), \(T=LU\Sigma^{-1/2}\). Podstawienie do wzorów transformacji daje \(W_c'=W_o'=\Sigma\); \(W_cW_o\) i \(\Sigma^2\) są podobne.
- W oszacowaniu błędu najmniejszych kwadratów poprawnie użyto ortogonalnego rzutu \(\mathcal O_N(\mathcal O_N^*\mathcal O_N)^{-1}\mathcal O_N^*\).

### LA28 — wymuszenie i transmitancje
- Skontrolowano warunki wzoru wariacji stałych, transformacji Laplace'a dla wejścia przedziałami ciągłego o zwartym nośniku oraz transformaty Z dla wejścia o skończonym nośniku. W dowodzie obu transformat uzasadniono zbieżność i odwracalność rezolwenty dla dostatecznie dużego parametru.
- W realizacji towarzyszącej \((\zeta I-A)(1,\zeta,\ldots,\zeta^{n-1})^T=p(\zeta)e_n\); wynika stąd \(C(\zeta I-A)^{-1}B=q(\zeta)/p(\zeta)\). Kryterium minimalności przez \(\gcd(p,q)=1\) jest zgodne z PBH.
- Sprawdzono oszacowania BIBO z \(\int_0^t e^{-\alpha(t-s)}ds\le1/\alpha\) i \(\sum_{j=0}^{k-1}r^j\le1/(1-r)\). Tekst prawidłowo odróżnia stabilność transmitancji od stabilności wewnętrznej.

## Testy, CI, PDF i rysunki

- Istnieją regresje `tools/test_linear_algebra_control.py` (20 instrukcji assert), `test_linear_algebra_general_riccati.py` (44), `test_linear_algebra_minimal_realizations.py` (26) i `test_linear_algebra_transfer_functions.py` (6).
- [GitHub Actions run 44987751791](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44987751791) dla **dokładnie wejściowego HEAD** `fd4e4a7121c3852b428b1bdeab450dd6257cc79c` ma status **completed/success**. Workflow obejmuje te cztery testy, kompilację pełnego PDF, kontrolę niezdefiniowanych odsyłaczy i ostrzeżeń oraz eksport PDF ostatniego rozdziału. Nie należy utożsamiać tego z wizualnym sprawdzeniem wszystkich stron.
- Źródła LA25–LA28 nie zawierają figur wymagających odrębnego renderingu TikZ; nie stwierdzono potrzeby dodania nowych ilustracji.
- Nie pobrano i nie obejrzano wizualnie osobnych PDF rozdziałów 25–28. **Kontrola nakładania napisów i pełna ocena składu są otwarte.**
- Nie wprowadzono zmian do twierdzeń ani dowodów, ponieważ w skontrolowanych argumentach nie znaleziono błędu. Nie należy dopisywać fikcyjnych korekt.

## Status i następny krok

**Audyt 07 wykonany**, ale nie oznaczony jako ostatecznie czysty wobec braku niezależnego przeglądu PDF i pełnej weryfikacji wszystkich kroków wszystkich 46 dowodów. Iteracja 08 obejmie LA29–LA32. W iteracji 09 trzeba domknąć kontrole międzyrozdziałowe, odsyłacze, pełny PDF oraz zaległe kontrole wizualne.
