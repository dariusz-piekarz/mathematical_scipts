# AA-42 — audyt II: niezależna kontrola postaci kanonicznych i algebraicznej zgodności

**Data:** 2026-11-22.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Źródło:** \`chapters/pl/abstract_algebra/42-lemat-schura-charaktery-i-ortogonalnosc.tex\`.

## Cel niezależnej kontroli

W odróżnieniu od audytu I, który skupiał się na ręcznej analizie dowodów,
kontrola II weryfikuje konsekwencje ich formuł w niezależnym modelu
grupy \(S_3\) i grup cyklicznych. Nie opiera się na obliczeniach
testów Pythona jako jedynym świadectwie poprawności.

## Wynik matematyczny

- **Algebra grupowa i idempotenty centralne.** Dla pełnej rodziny charakterów
  \(\chi_{\mathrm{triv}},\chi_{\mathrm{sgn}},\chi_{\mathrm{std}}\) i wymiarów
  \(1,1,2\) przetestowano elementy
  \(e_i=\frac{d_i}{6}\sum_{g\in S_3}\chi_i(g)[g]\) w \(\mathbb Q[S_3]\).
  Wszystkie spełniają \(e_ie_j=\delta_{ij}e_i\) oraz
  \(\sum_i e_i=[e]\), zgodnie z twierdzeniem o projektorach izotypicznych.
  W tym przypadku wartości charakterów są rzeczywiste, więc
  \(\overline{\chi_i(g)}=\chi_i(g)\); pełny wzór w AA-42
  zachowuje sprzężenie zespolone.
- **Rzut na reprezentację trywialną i standardową.**
  W permutacyjnej reprezentacji na \(\mathbb Q^3\) otrzymano
  \(P_{\mathrm{triv}}=\frac13J_3\),
  \(P_{\mathrm{sgn}}=0\) i
  \(P_{\mathrm{std}}=I_3-\frac13J_3\), gdzie \(J_3\)
  jest macierzą wszystkich jedynek. Zweryfikowano idempotentność,
  ortogonalność parami i sumę równą \(I_3\).
- **Przestrzeń funkcji klasowych.** W \(S_3\) istnieją
  klasy sprzężoności o rozmiarach \(1,3,2\).
  Dla funkcji charakterystycznej każdej z nich zbadano rozwinięcie
  \(f=\sum_i\langle f,\chi_i\rangle_G\chi_i\) we wszystkich sześciu elementach.
  Każde rozwinięcie daje dokładnie początkową funkcję.
- **Relacje Fouriera.** Dla grup \(C_n\), \(2\le n\le16\),
  sprawdzono z tolerancją \(10^{-9}\) relacje ortogonalności
  \(\sum_{j=0}^{n-1}\exp(2\pi i(k-\ell)j/n)=n\delta_{k\ell}\)
  dla wszystkich par \(0\le k,\ell<n\).
- **Zależności między rozdziałami.** AA-41 dowodzi Maschkego,
  co w AA-42 jest użyte jawnie przy rozszczepieniu modułu regularnego
  i rozkładach reprezentacji. AA-15 definiuje algebrę grupową
  \(K[G]\). AA-42 nie zastępuje wcześniejszych twierdzeń
  nieuprawnionym odwołaniem do pełnego twierdzenia Wedderburna.
- **Warunki twierdzeń.** Charakterystyka \(0\) występuje konsekwentnie
  w całej teorii charakterów zespolonych, natomiast pierwszy
  lemat Schura jest poprawnie sformułowany nad dowolnym ciałem.
  W odrębnym przykładzie nad \(\mathbb F_2\) podano realną
  przeszkodę w rozpoznawaniu równoważności po zwykłym śladzie.

## Kontrole liczbowe i techniczne

**1663 niezależne sprawdzenia arytmetyczne zakończone powodzeniem**:
dotyczyły 54 równości mnożenia idempotentów centralnych,
równości projektorów macierzowych, rozwinięć funkcji klasowych
oraz wyczerpującego testowania ortogonalności na \(C_2,\ldots,C_{16}\).
Wspólnie z audytem I daje to **1741 osobnych kontroli**.

**Dwa moduły AA-42 w GitHub Actions** przeszły etap
\`Run AA-42 mathematical regression tests\` ze statusem \`success\`
w przebiegu:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069712799

W momencie publikacji raportu pełny etap
\`Compile AA-01 to AA-42 book with latexmk\` w tym samym przebiegu
był jeszcze \`in_progress\`; nie zgłaszamy pomyślnej kompilacji
ani pełnej kontroli PDF przed zakończeniem kroków zdalnych.

**Źródło \`.tex\` pozostało bez zmian względem audytu I.**
Poprawiono jedynie test dotyczący użycia nieortonormalnej bazy,
opisany w raporcie \`ch42_iteration_01.md\`.

## Werdykt

Wynik kontroli matematycznej II: **bez nowych uchybień merytorycznych**.
Etap stabilizacji źródła oczekuje jedynie na potwierdzenie
pełnego zdalnego CI, wraz z kompilacją i kontrolą odsyłaczy.
