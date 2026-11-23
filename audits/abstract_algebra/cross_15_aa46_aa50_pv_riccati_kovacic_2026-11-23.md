# Algebra abstrakcyjna — audyt przekrojowy 15 (AA-X15): interfejs AA-46–AA-50

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Stan wejściowy:** AA-50 już oznaczony jako STABILNY w `audits/abstract_algebra/ch50_iteration_03.md`; ostatni audyt przekrojowy: `cross_14_aa05_aa08_group_structure_2026-11-23.md`.  
**Zakres:** teoria Picarda–Vessiota (AA-46), równania Riccatiego i Risch (AA-47), gałąź wymierna (AA-48), ściśle kwadratowa (AA-49) i skończona prymitywna (AA-50), z kontrolą odsyłaczy do AA-43–AA-45.

## 1. Kontrola zgodności pojęć i hipotez

1. **PV → Riccati (AA-46 ↔ AA-48).** Dla niezerowego rozwiązania `z` równania `z''=qz` element `r=z'/z` spełnia `r'+r²=q`. Gdy `r∈C(x)`, prosta rozwiązań wyznaczona przez `z` jest niezmiennicza względem różniczkowej grupy Galois. Nie utożsamia się testu wymiernego z testem wszystkich rozwiązań liouvillowskich.
2. **PV → przypadek ściśle kwadratowy (AA-46 ↔ AA-49).** Dla sprzężonych `r±` ślad `φ=r₊+r₋` jest wymierny, a `Δ=(r₊-r₋)²=4q-2φ'-φ²`. Konieczny jest warunek `Δ≠0` i `Δ` nie będąca kwadratem w `C(x)`; inaczej wynik należy do gałęzi wymiernej. Przedstawione modele sprawdzono także dla obu znaków pierwiastka.
3. **Przypadek skończony (AA-47 ↔ AA-50).** Parametry `n=4,6,12` i konieczność pełnych list lokalnych wynikają z **cytowanej** klasyfikacji Kovacica, nie ze sprawdzenia rekurencji. Dodatni `P₋₁=0` dostarcza rozwiązania Riccatiego, lecz bez wcześniejszego wykluczenia gałęzi 1 i 2 nie dowodzi prymitywności grupy Galois.
4. **Risch vs Kovacic (AA-44–AA-47).** Elementarność całki i liouvillowskość rozwiązania równania liniowego są odrębnymi problemami. W `r'+hr=s` przy wielomianowym `h` dodatni test dotyczy pierwotnej `s·exp(∫h)`; w Kovacicu badamy algebraiczne pierwiastki Riccatiego. Dowody nie mogą przenosić odpowiedzi negatywnej pomiędzy tymi problemami.
5. **Airy (AA-46–AA-50).** Dla `q=x` przypadek wymierny odpada przez nieparzysty stopień wielomianu; w gałęzi kwadratowej `E∞={-1}` daje `d=-1/2`; w skończonej `ord∞q=-1<2`. Dopiero wyczerpująca klasyczna klasyfikacja prowadzi do globalnego braku niezerowych rozwiązań liouvillowskich; niezależnie AA-46 zawiera argument przez brak algebraicznego Riccatiego.

**Wynik przeglądu tych interfejsów:** nie znaleziono sprzeczności ani nowej koniecznej korekty matematycznej. Nie jest to pełny ponowny dowód wszystkich twierdzeń w pięciu rozdziałach. Klasyczna klasyfikacja lokalna, teoria PV i klasyfikacja skończonych grup pozostają jawnie cytowanymi wejściami.

## 2. Nowa, trwała regresja

Dodano `tools/tests/test_abstract_algebra_cross_aa46_50.py` i podłączono go do `.github/workflows/abstract-algebra-chapter.yml`. Skrypt wykorzystuje dokładną arytmetykę SymPy (bez tolerancji liczbowych) i sprawdza także etykiety/odsyłacze w źródłach.

**Uruchomienie lokalne części rachunkowej (bez drzewa źródeł repozytorium): 44/44 sprawdzenia PASS** w czterech testach:

- 6 sprawdzeń: model PV `z₁=x²,z₂=x⁻¹`, stały Wrońskian `-3`, oba wymierne Riccati i jeden model kroku Rischa.
- 14 sprawdzeń: trzy dodatnie modele AA-49 (sześć podstawień `r±`, trzy wyróżniki, trzy testy niekwadratowości) i dwa testy przypadku zdegenerowanego `q=2/x²`.
- 3 sprawdzenia: oddzielne przeszkody trzech przypadków Kovacica dla Airy'ego.
- 21 sprawdzeń: dla `m=3,4,5` po siedem testów dokładnych, obejmujących lokalne współczynniki `b₀,b₁,b∞`, listy `E₀,E₁,E∞` i kandydat `d=0`.

**Dodatkowe 8 sprawdzeń źródłowych:** 1 kontrola unikatowości etykiet AA-43–AA-50 oraz 7 kontroli zbiorów odsyłaczy w AA-44–AA-50, z których wszystkie rozwiązują się w AA-43–AA-50. Odczytano bezpośrednio źródła z GitHub. W tych ośmiu rozdziałach są **198 etykiet** (20+20+25+30+30+23+25+25), bez duplikatów; AA-44–AA-50 mają **187 wystąpień** odsyłaczy bez brakujących celów w tej grupie rozdziałów.

Nowy test uruchomiony na pełnym checkoutcie przez CI powinien wykonać łącznie **5 testów / 52 asercje**. Nie przedstawia się lokalnego braku drzewa repozytorium jako awarii matematycznej regresji: w środowisku lokalnym cztery testy rachunkowe przeszły, a test plikowy wymaga checkoutu i ma być potwierdzony osobno przez CI.

## 3. Zakres zmian i bramki

- Test: `tools/tests/test_abstract_algebra_cross_aa46_50.py`.
- Workflow: `.github/workflows/abstract-algebra-chapter.yml` — dodano ścieżkę wyzwalającą i osobny krok regresji AA-X15.
- Rozdziały matematyczne i wcześniejsze statusy stabilności: **bez zmian**.
- Nowe definicje, twierdzenia i przykłady do książki: **nie wstawiano**; nie stwierdzono koniecznej poprawki matematycznej.

**CI zainicjowany:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45196378758 (stan początkowy: `in_progress`, commit workflow `9fdeafaf9f859b2f7fd4f922878b70c90ae6d25f`).  
**Status audytu przekrojowego 15:** wykonana kontrola logiczna, 44 lokalne asercje rachunkowe PASS, 8 kontroli źródłowych PASS; **otwarty do potwierdzenia pełnego CI**, w tym kompilacji LaTeX i stanu pliku PDF. Nie przenosić automatycznie historycznego statusu AA-50 na bieżący nowy commit.

## 4. Następny krok

Zweryfikować wynik dokładnie tego uruchomienia workflow, w szczególności krok AA-X15, ogólną integralność i `latexmk`. Jeżeli pełny CI zostanie zielony i nie wykaże nowej usterki, zamknąć AA-X15 jako czysty audyt przekrojowy bez zmiany statusów rozdziałów. Jeżeli pojawi się awaria, poprawić i ponowić walidację przed przejściem do kolejnego zakresu.
