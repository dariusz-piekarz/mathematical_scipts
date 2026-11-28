# AA-42 — audyt I: poprawność matematyczna, struktura i regresja

**Data:** 2026-11-22  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Źródło:** \`chapters/pl/abstract_algebra/42-lemat-schura-charaktery-i-ortogonalnosc.tex\`.  
**Temat:** lemat Schura, unitarność, ortogonalność współczynników macierzowych i charakterów, krotności reprezentacji nieprzywiedlnych, funkcje klasowe.

## Szczegółowy audyt matematyczny

1. **Warunki lematu Schura.** Pierwszy lemat prawidłowo korzysta z niezmienniczości jądra i obrazu operatora przeplatającego, bez założenia algebraicznej domkniętości. Drugi potrzebuje algebraicznej domkniętości \(\mathbb C\) i skończonego dodatniego wymiaru. Kontrprzykład rzeczywisty z obrotem o \(120^\circ\) ma wielomian \(T^2+T+1\), więc nie ma rzeczywistej prostej niezmienniczej; komutujący operator \(J\) nie jest skalarny.
2. **Unitarność.** Suma iloczynów hermitowskich jest dodatnio określona, gdyż każdy \(\rho(g)\) jest odwracalny; zmiana indeksu \(k=gh\) uzasadnia niezmienniczość. Użycie tej własności w identyfikacji elementów macierzy odwrotnej z elementami sprzężonymi jest zasadne.
3. **Ortogonalność macierzowa.** Operator \(\mathcal P_{ij}(A)=|G|^{-1}\sum_g\rho_i(g)A\rho_j(g)^{-1}\) przeplata działania. Przy \(i\ne j\) jest zerowy; przy \(i=j\) jest \(\operatorname{tr}(A)I/d_i\). Specjalizacja do macierzy jednostkowej \(A:E_d\mapsto E_b\) daje prawidłowe indeksy \(\delta_{ac}\delta_{bd}/d_i\).
4. **Ortogonalność charakterów.** Podwójna suma po przekątnych współczynników redukuje się do \(d_i/d_i=1\) dla tej samej reprezentacji; dla odmiennych klas daje zero.
5. **Lista wszystkich nieprzywiedlnych.** Z odwzorowania \(\mathbb C[G]\to V\), \([g]\mapsto\rho(g)v\), otrzymujemy surjekcję; Maschke rozszczepia jądro. Każde nieprzywiedlne \(V\) występuje zatem w reprezentacji regularnej, a liczba klas jest skończona.
6. **Krotności i regularna.** Wzór \(m_i=\langle\chi_V,\chi_i\rangle_G\) korzysta z addytywności charakterów i ortogonalności; charakter regularny ma wartość \(|G|\) na jednostce oraz zero poza nią. Stąd \(\mathbb C[G]\simeq\bigoplus_iV_i^{\oplus d_i}\) i \(\sum_i d_i^2=|G|\). Nie wykorzystuje się nieudowodnionego wcześniej twierdzenia Wedderburna.
7. **Rzuty izotypiczne.** Operator \(P_i=(d_i/|G|)\sum_g\overline{\chi_i(g)}\rho(g)\) jest centralną kombinacją operatorów grupy; na każdym składniku \(V_j\) ma ślad \(d_i\delta_{ij}\) i wobec lematu Schura jest tożsamością przy \(i=j\) oraz zerem przy \(i\ne j\).
8. **Zupełność charakterów.** Jeśli funkcja klasowa \(f\) jest ortogonalna do wszystkich \(\chi_i\), operator \(T_f^\rho=\sum_gf(g)\rho(g^{-1})\) jest równoważny z zerem na każdym składniku regularnym. Z równości \(T_f^{\mathrm{reg}}([e])=\sum_g f(g)[g^{-1}]=0\) wynika \(f=0\). Jest to samodzielny dowód liczby klas reprezentacji; nie opiera się na nieudowodnionej klasyfikacji algebr półprostych.
9. **Kolumny tablicy charakterów.** Macierz \(A_{ik}=\sqrt{|C_k|/|G|}\,\chi_i(g_k)\) jest kwadratowa, a ortogonalność wierszy daje \(AA^*=I\). Zatem \(A^*A=I\), skąd \(|G|/|C_k|\) na przekątnej relacji dla kolumn.
10. **Przykłady i ograniczenia.** Tablice \(C_3\) i \(S_3\) mają odpowiednio 3 i 3 kolumny; charakter standardowy \(S_3\) wynosi \((2,0,-1)\), a \(1^2+1^2+2^2=6\). Przeciwprzykład modularny nad \(\mathbb F_2\) prawidłowo ilustruje niemożliwość rozpoznawania nieizomorficznych reprezentacji po zwykłym śladzie.

## Niezależne kontrole arytmetyczne i strukturalne

- Przeprowadzono **78 niezależnych sprawdzeń** w JavaScript obejmujących działania permutacji, wielomiany reprezentacji standardowej \(S_3\), ortogonalność wierszy i kolumn, rozkład regularny oraz uśrednianie Schura dla macierzy jednostkowych.
- Struktura źródła: **21 etykiet**, każda unikatowa; **9 użyć odsyłaczy**, z czego jeden do wcześniej istniejącego \`aa:ch:representations\` z AA-41; pozostałe lokalne. **13 dowodów i 3 przykłady**; wszystkie środowiska LaTeX domknięte.
- Potwierdzono obecność AA-42 w \`books/pl/abstract_algebra.tex\` i jako ostatniego rozdziału w \`catalog/books.json\` (razem 42 rozdziały).
- Włączono moduły \`test_abstract_algebra_ch42.py\` i \`test_abstract_algebra_ch42_independent.py\` do \`.github/workflows/abstract-algebra-chapter.yml\`.
- W trakcie niezależnej analizy testów wykryto i **poprawiono wadliwe początkowe założenie** w teście współczynników: naturalna baza \((e_1-e_2,e_2-e_3)\) reprezentacji standardowej \(S_3\) nie jest ortonormalna. Test zastąpiono bazowo niezależną tożsamością \(\frac1{|G|}\sum_g\rho(g)A\rho(g)^{-1}=(\operatorname{tr}A/2)I\), prawidłową w tej bazie. Samo twierdzenie w rozdziale zakłada bazę ortonormalną i nie wymaga korekty.

## Walidacja zdalna

Po opublikowaniu rozdziału, testów i ich integracji uruchomiły się GitHub Actions. Przebieg dla commitu zawierającego poprawkę niezależnego testu:  
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069712799

**Na moment audytu I stan przebiegu: \`in_progress\`.** Nie uznajemy tego za potwierdzony sukces kompilacji lub testów. Nie wykonano osobnej lokalnej kompilacji ani wizualnej kontroli renderów.

## Werdykt

Audyt matematyczny i strukturalny I: bez potwierdzonych błędów w \`.tex\`, przy poprawionym teście regresyjnym. Status stabilizacyjny uzależniony od pełnego wyniku zdalnego CI oraz ponownego niezależnego audytu.
