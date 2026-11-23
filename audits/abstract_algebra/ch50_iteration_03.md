# AA-50 — audyt III: niezależne sprawdzenie rekurencji, hipotez i regresji

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**HEAD przed kontrolą:** `8743da3cd22b450145a4431d4612e12363e2b9c6`; **HEAD ponownie przed publikacją:** `5c295e99821d1ebb9d7fa98b68829c55a5b3656a` (równoległe zmiany w innych obszarach).  
**Źródło:** `chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex`, blob `4661b8577ed96b126a2fa8e5be8e7004c31d572c`.  
**Werdykt:** audyt matematyczny III w sprawdzonym zakresie bez nowej usterki; **NIE STABILNY**, dopóki nie zostanie wykonana i udokumentowana wizualna kontrola wszystkich stron PDF oraz pełna bramka końcowa.

## 1. Weryfikacja stanu i standardów

Odczytano aktualną gałąź, listing 50 źródeł AA-01–AA-50, listing 96 raportów audytu, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `docs/pl/zakres_aa50_kovacic_skonczone_grupy.md`, `catalog/books.json`, źródło AA-50 oraz raporty I–II. AA-51 nie występuje w spisie źródeł. Nie dodano nowych twierdzeń ani nie zmieniono etykiet.

## 2. Niezależna kontrola matematyczna

- Warunki wstępne dla trzeciego przypadku są jasno ograniczone do `q≠0`, biegunów rzędu najwyżej 2 i `ord∞q≥2`. Osobny przypadek `q=0` nie jest błędnie klasyfikowany.
- Listy lokalne `E_c(n)` i `E_∞(n)`, parametry `n=4,6,12` i wyczerpujący charakter klasyfikacji są jawnie **cytowane**, a nie rzekomo wyprowadzone z przykładów. Testy nie stanowią dowodu ich kompletności.
- Dla `S=∏(x-c)` zarówno `Sθ`, jak i `S²q` są wielomianami. Rekurencja ma współczynnik `(n-i)(i+1)`, a w `F` występuje `(n-i)!`; sprawdzono zgodność wyrazów przy `T^0` i `T^{n+1}`. Dla `T^0` otrzymuje się dokładnie `P_{-1}=0`, a dla `T^{n+1}` nie powstaje nowy warunek.
- W lemacie o pierwiastkach algebraicznych poprawnie użyto charakterystyki 0, separowalności czynnika nierozkładalnego i jego dzielności przez `𝒟f`; nie wymaga się bezkwadratowości całego `F`.
- Dodatni wynik rekurencji zapewnia rozwiązanie Riccatiego, lecz nie klasyfikuje sam w sobie grupy jako `A4/S4/A5`; źródło wyraźnie rozróżnia tę implikację.
- Sprawdzono graniczne przykłady `q=2/x²` (istnieją wymierne rozwiązania Riccatiego) oraz `q=x` (trzecia gałąź odpada przez rząd w nieskończoności). Wniosek o całym algorytmie pozostaje warunkowy od wykluczenia pozostałych gałęzi.

## 3. Nowy niezależny test dokładny (lokalne wykonanie)

W odrębnym skrypcie SymPy, bez korzystania z testów repozytorium, wykonano pełną rekurencję dla rodziny
`q_m=-3/(16x²)-2/(9(x-1)²)+C_m/[x(x-1)]`, z `(n,C_m)=(4,3/16),(6,101/576),(12,611/3600)`, `S=x(x-1)`, `e_0=3,e_1=4,e_∞=7`, `d=0`, `P=1`. Wyniki dla **wszystkich trzech** przypadków: `P_{-1}=0` oraz dokładna tożsamość `𝒟F=(-nT+nS'/S-θ)F`. Liczba wygenerowanych indeksów `P_i`: odpowiednio **7, 9, 15** (od `n+1` do `-1`). Test wykonany lokalnie i zakończony bez błędów. Nie jest dowodem klasyfikacji grup skończonych.

## 4. Skład, odsyłacze i CI — osobny status

- W aktualnym drzewie katalog obejmuje 50 rozdziałów, w tym AA-50; dwa zestawy testów AA-50 istnieją w `tools/tests/test_abstract_algebra_ch50.py` i `tools/tests/test_abstract_algebra_ch50_independent.py`.
- GitHub Actions: istniejący przebieg [45183171359](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45183171359) ma stan `completed/success` dla SHA `218947dd38d904b5d100d13cf8bf87e303ff10fb`. Nowszy przebieg [45184219678](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45184219678) przy odczycie miał stan `in_progress` dla SHA `4103a830163f9abcebca492d26e58f33e9784f82`. **Nie przypisujemy żadnego z tych wyników bezpośrednio aktualnemu HEAD.**
- Lokalny `git ls-remote` zakończył się błędem DNS `Could not resolve host: github.com`; nie sklonowano repozytorium, nie uruchomiono lokalnej kompilacji pełnej książki i **nie obejrzano PDF**. Zatem brak podstaw do zadeklarowania nowego LaTeX/PDF PASS.
- Przeprowadzono kontrolę treści i nazw odsyłaczy w źródle, lecz nie przeprowadzono niezależnego pełnego testu odsyłaczy na świeżym buildzie.

## 5. Decyzja i następny krok

**Bez zmian w zatwierdzonym źródle; brak resetu licznika czystych audytów z powodu korekty.** Audyt III stanowi niezależne sprawdzenie merytoryczne, ale **nie zamyka AA-50**. Następny krok: pobrać PDF z właściwego zielonego przebiegu CI, obejrzeć wszystkie strony AA-50 i log kompilacji, zweryfikować wyniki dwóch testów oraz status na bieżącym HEAD. Dopiero potem wykonać dodatkowy pełny audyt potwierdzający i rozstrzygnąć stabilność; nie otwierać AA-51 wcześniej.
