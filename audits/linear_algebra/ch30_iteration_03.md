# Algebra liniowa — rozdział 30, audyt III (matematycznie czysty)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/30-algebry-clifforda.tex`; źródłowy blob `c5e48050c75b27c31162fba95862b6ecac944971` — niezmieniony.

## Weryfikacja definicji, dowodów i przykładów
1. **Iloraz i stopniowanie:** ideał obustronny generowany przez `v⊗v+||v||²1` jest zgodny z mnożeniem w algebrze tensorowej. Generatory mają parzystość 0, więc iloraz jest \(\mathbb Z/2\mathbb Z\)-stopniowany. Wymagane przejścia zostały wyjaśnione.
2. **Relacja Clifforda:** polaryzacja warunku \(v^2=-\|v\|^2\) daje \(vw+wv=-2\langle v,w\rangle\). Własność uniwersalna jest poprawnie wyprowadzona z uniwersalności algebry tensorowej i faktoryzacji przez ideał zawarty w jądrze homomorfizmu.
3. **Rozpinanie:** zamiana sąsiednich różnych generatorów i redukcja kwadratów \(e_i^2=-1\) prowadzą do uporządkowanych monomów \(e_I\). Zakończenie procedury można ująć przez zmniejszanie liczby inwersji i długości słowa, dlatego nie wymaga założenia o niezależności monomów.
4. **Kontrakcja \(\iota_v\):** operator jest dobrze określony na \(\Lambda^rV\) dzięki wieloliniowości i alternowaniu. Sprawdzono znak w regule \(\iota_v(w\wedge\omega)=\langle v,w\rangle\omega-w\wedge\iota_v\omega\) i znoszenie się dwóch kolejnych kontrakcji.
5. **Reprezentacja:** dla \(c(v)=\varepsilon(v)-\iota_v\) zachodzi \(c(v)^2=-\|v\|^2\operatorname{id}\). Jej działanie na jedynkę realizuje bijekcję między uporządkowanymi monomami Clifforda i bazowymi wielowektorami. Uzyskano niezależność monomów i wymiar \(2^n\), a dla \(n\ge1\) po \(2^{n-1}\) wymiarów obu części.
6. **Antysymetryzacja:** mapę \(\Lambda V\to\operatorname{Cl}(V)\) opisano poprawnie, ma ona na uporządkowanej bazie ortonormalnej obraz monomów \(e_I\); odróżniono izomorfizm przestrzeni liniowych od izomorfizmu algebr.
7. **Przykłady:** sprawdzono dla \(n=0,1,2\) modele \(\R,\C,\mathbb H\). Kwadrat \((e_1e_2)^2=-1\), znaki mnożenia kwaternionów oraz \((e_1+2e_2)^2=-5\) są zgodne z konwencją.

## Dokładne, wykonane niezależnie testy
Uruchomiono w lokalnym interpreterze Python kod kontrolny `/mnt/data/verify_clifford_local.py`, niezależny od testu w repozytorium:
- 5461 par monomów bazowych, z równoczesną kontrolą działania na \(\Lambda V\): **PASS**.
- 6681 trójek dla łączności iloczynu: **PASS**.
- 3450 relacji antykomutacji operatorów \(c(e_i)\) na bazowych wielowektorach: **PASS**.

## Wynik
**Audyt III matematycznie czysty.** Nie zmieniono źródła ani rysunku. Ostateczna ocena pełnego składu i PDF zostanie wykonana po zakończeniu workflow uruchomionego poprawką CI.
