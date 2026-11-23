# Algebra abstrakcyjna — audyt przekrojowy 17: Burnside, Reynolds i charaktery (AA-03 × AA-41 × AA-42)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Poprzedni etap:** AA-X16 zamknięty po potwierdzeniu 7/7 testów i 94/94 kroków workflow [45199128470](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45199128470). AA-51 nadal nieutworzony.
**Źródła:** aktualne AA-03 `b817e09694997218ab1933bc9c7e9972e1274173`, AA-41 `05d87a9b95117069879b58e5c6ea40d71ad4a29c`, AA-42 `f7b662c41bf51d05c03613c879c74b9a7e30040d`. Dla odsyłaczy odczytano także AA-01 `0e731cc5ef69286f613babc46920cf615f9fef65` i AA-02 `36efd06e0da961cc60dadc061ebc43122e4f14f2`.

## 1. Nowy problem przekrojowy i samodzielny dowód

Nie jest to powtórny audyt konstrukcji algebraicznej AA-X16 ani szczegółowej samej tablicy charakterów AA-42. Zestawiono **trzy odrębne wzory na tę samą liczbę**: orbity skończonego zbioru, wymiar przestrzeni wektorów niezmienniczych reprezentacji permutacyjnej i średnią charakteru.

Niech skończona grupa `G` działa na skończonym zbiorze `X`, a `V=\mathbb C^{(X)}` oznacza przestrzeń z bazą `(e_x)_{x\in X}`. Działanie liniowe zadane przez `\rho(g)e_x=e_{g\cdot x}` ma charakter `\chi_\rho(g)=|X^g|`, ponieważ ślad macierzy permutacyjnej jest równy liczbie wektorów bazowych pozostających na swojej pozycji.

Operator Reynoldsa `R_G=\frac1{|G|}\sum_g\rho(g)` jest idempotentem na `V^G` na mocy AA-41. Ponieważ wielomian minimalny idempotentu dzieli `T(T-1)` o dwóch różnych pierwiastkach, jego ślad jest równy rzędowi rzutu, czyli `\dim V^G`. Tym samym
`\dim V^G=\operatorname{tr}R_G=\frac1{|G|}\sum_{g\in G}|X^g|`.
Z kolei `v=\sum_x a_x e_x` jest niezmienniczy dokładnie wtedy, gdy funkcja współczynników `x\mapsto a_x` jest stała na orbitach. Wskaźniki orbit (rozumiane jako wektory będące sumami odpowiednich `e_x`) tworzą bazę `V^G`; stąd `\dim V^G=|X/G|`. Otrzymujemy dokładnie lemat Burnside'a z AA-03, niezależną drogą korzystającą z AA-41 i AA-42.

Przy zespolonym iloczynie skalarnym charakterów z AA-42 zachodzi również `\dim V^G=\langle\chi_\rho,\chi_{triv}\rangle_G`, gdyż `\chi_{triv}=1`, a twierdzenie Maschkego oraz wzór na krotności identyfikują tę wielkość z krotnością reprezentacji trywialnej.

**Hipotezy:** `G` i `X` muszą być skończone dla tej postaci wzoru. Lemat Burnside'a jest twierdzeniem o licznościach zbiorów i zachowuje ważność niezależnie od ciała. Przejście przez średnią `1/|G|` w reprezentacji liniowej wymaga `|G|\cdot1_K\ne0`; przejście do zespolonych charakterów używa `K=\mathbb C`. Zatem brak odwrotności `|G|` w charakterystyce modularnej nie unieważnia samego lematu Burnside'a, lecz zabrania bezpośredniego zastosowania operatora Reynoldsa.

## 2. Konkretne obliczenia — niezależna kontrola

- Naturalne działanie `S_3` na trzech punktach: charakter permutacyjny na klasach `e`, transpozycje, trójcykle jest `(3,1,0)`. Z dokładnego iloczynu skalarnego z charakterami trywialnym, znaku i standardowym otrzymujemy krotności `(1,0,1)`; liczba orbit wynosi 1.
- Symetrie kwadratu `D_4` działające na czterech wierzchołkach: jedna orbita, operator Reynoldsa ma ślad 1.
- Kolorowania kwadratu dwoma kolorami: `|X|=16`, suma liczby punktów stałych po wszystkich symetriach wynosi 48, co daje 6 orbit; dokładny operator Reynoldsa na 16-wymiarowej reprezentacji permutacyjnej ma `R^2=R` i ślad 6.
- Trzy kolory: `D_4` daje sumę punktów stałych 168, czyli 21 orbit spośród 81 kolorowań. Grupa samych obrotów `C_4` daje 24 orbity. W ten sposób test nie sprowadza się jedynie do ponownego sprawdzenia wcześniej wydrukowanego przykładu AA-03.
- Dwie kopie naturalnego działania `S_3` tworzą dwie orbity; rzut na niezmienniki ma ślad 2.
- Działanie trywialne na 5 punktach daje 5 orbit i operator identycznościowy; pusty zbiór daje 0 orbit.
- `\mathbb F_2[C_2]`: stosowanie `1/|C_2|` jest niedopuszczalne, ponieważ `2=0`; natomiast Burnside daje poprawnie 1 orbitę działania zamieniającego dwa punkty.

## 3. Trwała regresja i integralność źródeł

Dodano `tools/tests/test_abstract_algebra_cross_aa03_41_42.py` z 7 testami:
1. zamknięcie i prawa działania `S_3,D_4,C_4`,
2. bezpośrednie wyliczenie orbit i punktów stałych w pięciu modelach,
3. ślad i idempotencja macierzy Reynoldsa nad dokładnymi `fractions.Fraction`,
4. komutowanie i równania `R\rho(g)=\rho(g)R=R`,
5. zespolona teoria charakterów `S_3` w przykładzie o współczynnikach całkowitych,
6. zbiór pusty, działanie trywialne i przeszkoda modularna,
7. kontrola istniejących źródeł, etykiet oraz odsyłaczy.

Niezależnie wykonane dokładne rachunki dla `D_4` dały **6** (dwa kolory) oraz **21** (trzy kolory) orbit; dla `S_3` i `D_4` potwierdzono `R^2=R` i ślad równy liczbie orbit. Odczyt etykiet AA-01, AA-02, AA-03, AA-41, AA-42 dał **118 unikatowych etykiet bez kolizji**; w obrębie AA-03, AA-41, AA-42 było **23 odsyłaczy**, wszystkie z celami w tych pięciu źródłach.

Do `.github/workflows/abstract-algebra-chapter.yml` dodano wyzwalacz ścieżki testowej oraz oddzielny krok `Run AA-X17 Burnside Reynolds and character interface`.

**CI:** [45206650247](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206650247), commit workflow `b0c27d40e4159817c941cc1b489e78c4cab26e7f`; status przy rozpoczęciu `in_progress`. Do zamknięcia potrzebny wynik 7/7 testów w rzeczywistym CI, zielona integralność i kompilacja całej książki.

## 4. Wynik merytoryczny, zakres zmian i propozycja

**AA-X17: W AUDYCIE do końcowej bramki CI.** Badane twierdzenia są ze sobą zgodne. Nie znaleziono koniecznej korekty w już zatwierdzonych rozdziałach. Testy skończone wspierają poprawność wskazanych przykładów i tożsamości, ale nie stanowią samodzielnego dowodu całej teorii reprezentacji.

**Opcjonalne uzupełnienie do decyzji użytkownika:** w AA-41, po operatorze Reynoldsa, można dodać osobne stwierdzenie z powyższym krótkim dowodem: lemat Burnside'a = wymiar przestrzeni niezmienniczej = iloczyn skalarny charakteru permutacyjnego z trywialnym. Jest to wartościowe połączenie trzech działów, lecz **nie jest niezbędną poprawką** i zgodnie z `AGENTS.md` nie zostało automatycznie dodane do zatwierdzonego rozdziału.

**Statusy AA-01–AA-50 pozostają nienaruszone.** AA-51 nie został otwarty.
