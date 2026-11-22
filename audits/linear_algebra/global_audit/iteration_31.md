# Algebra liniowa — globalny audyt 31: LA-30, Algebry Clifforda

**Data:** 23 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Zakres:** dokładnie LA-30 — 309 wierszy, trzy dowody, jeden rysunek.
**Źródło:** chapters/pl/linear_algebra/30-algebry-clifforda.tex, blob 6d90013dd6c66d347e5ae2ac78b4c1a194aa979e (bez zmian).
**Wynik:** niezależny audyt globalny czysty; brak uzasadnionej edycji .tex. Ewidencja globalna **366/382** (poprzednio 363/382). LA-30 pozostaje STABILNY zgodnie ze źródłowymi audytami 03–04 (2 czyste kontrole na tym samym blobie) i audytem sceptycznym 05 (+1). Bieżący audyt globalny stanowi dodatkową kontrolę.

## 1. Dwa niezależne odczyty matematyczne całego rozdziału

Sprawdzono definicję, dwa twierdzenia, jedno stwierdzenie, trzy pełne dowody, uwagę o antysymetryzacji, przykład w wymiarach 0–2, inne rachunki oraz diagram. Zbadano po kolei hipotezy, znaki, typy, istnienie i jednoznaczność konstrukcji, zgodność z wcześniejszym LA-11, przypadki brzegowe i brak koła logicznego. Osobny rejestr każdego dowodu: iteration_31_proof_review_30.csv.

### Dowód 1 — relacja i własność uniwersalna, linie 75–92

Rozwinięcie kwadratu v+w i polaryzacja prawidłowo dają vw+wv = −2⟨v,w⟩. Homomorfizm F:T(V)→A jest unitalny i zabija wszystkich generatorów ideału obustronnego I_q; jądro zawiera I_q, co uzasadnia faktoryzację przez Cl(V) bez wyboru reprezentanta. Jednoznaczność wynika z generatorów V i 1. Nie założono przemienności A. Dla n=0 iloraz to R. Brak nowej usterki.

### Dowód 2 — baza algebry Clifforda, linie 119–198

Rozpinanie uporządkowanymi monomami dowiedziono przez zamiany liter oraz redukcję kwadratów generatorów. Niezależność nie została przyjęta jako własność normalnej postaci: skonstruowano reprezentację na Λ(V) przez c(v)=ε(v)−ι_v. Sprawdzono dobrze określoną kontrakcję, jej znaki, równanie ι_v ε(w)+ε(w)ι_v=⟨v,w⟩I, równości ε(v)²=0, ι_v²=0 i stąd c(v)²=−||v||²I. Działanie uporządkowanych monomów na 1 daje bazę Λ(V), więc monomy są liniowo niezależne. Dla n≥1 podzbiory parzystej i nieparzystej liczności mają ten sam rozmiar; dla n=0 liczba monomów wynosi 1. Wymiar 2^n jest poprawny i nie korzysta z klasyfikacji Clifforda. Brak usterki.

### Dowód 3 — część skalarna i dwuwektor, linie 262–268

Stwierdzenie jawnie kwantyfikuje dowolne v,w∈V. Równość vw = −⟨v,w⟩ + (vw−wv)/2 oraz identyfikacja ostatniego składnika z v∧w przez antysymetryzację stopnia dwa są poprawne. Sprawdzono przykład z v=e1+2e2, w=2e1+e2: wynik −4−3e1e2. Brak usterki.

### Inne fragmenty krytyczne

Generator ideału ma parzystość 0 modulo 2, co pozwala mówić o podprzestrzeniach Cl^0 i Cl^1 mimo utraty pełnego stopniowania. Antysymetryzacja ΛV→Cl(V) jest izomorfizmem przestrzeni liniowych, nie algebr. Przy konwencji e_i²=−1 uzyskujemy Cl(0)=R, Cl(R)≅C i Cl(R²)≅H jako algebry rzeczywiste. Rysunek przedstawia część skalarną −cosα oraz dwuwektor sinα e1e2 dla jednostkowych wektorów. Nie wykryto niespójności definicji, niejawnego uogólnienia na ciało charakterystyki 2 ani naruszenia terminologii.

## 2. Nowe testy dokładne

Zapisano i uruchomiono /mnt/data/la30_global31_independent.py (SHA256 8bfbeb62f94bbb243abd77a783612ce2dea5ddc3e7119885012ccd8ad7646bbf), generator random.Random(202611230031). Testy Fraction, niezależne od implementacji z repozytorium: **8050/8050 PASS**, zero błędów.

| Obszar | Kontrole |
| --- | ---: |
| Kwadraty wektorów w wymiarach n=0..6 | 770 |
| Relacje polaryzacji dla par wektorów | 770 |
| Łączność mnożenia monomów | 1330 |
| Reprezentacja na algebrze zewnętrznej i antykomutatory | 4092 |
| Antysymetryzacja mieszanych wektorów | 180 |
| Zgodność parzystości | 127 |
| Przypadki graniczne | 7 |
| Przykłady i część skalarna iloczynu | 774 |
| **Suma** | **8050** |

Istniejąca regresja narzędziowa tools/test_linear_algebra_clifford.py jest oddzielna. Żaden z testów nie jest formalną weryfikacją Lean.

## 3. Źródło, odsyłacze, CI, PDF

W LA-30 jest **11 etykiet** bez powtórzeń i **12 odsyłaczy**, z czego wszystkie lokalne wskazują istniejące cele; sześć różnych zewnętrznych celów potwierdzono w aktualnym LA-11, blob 17f1bae2db46ac6790f1fc562660393f2f616076. Zbadano parowanie trzech środowisk proof i jednego figure/tikzpicture. Manifest catalog/books.json umieszcza LA-30 na pozycji 30/32 (books/pl/linear_algebra.tex).

Zweryfikowano [CI 45083998648](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083998648), completed/success, commit 57319c972ca6faaeec4404b13fe31a7fe3762b53, obejmujący niezmieniony blob LA-30. Z artefaktu 14778144707 odzyskano 320-stronicową książkę linear_algebra.pdf i jej log. LA-30 to fizyczne strony **295–297**; wyodrębniono PDF rozdziału (3 strony), SHA256 c6a40f2dc2620212f1251c524b13dce656663fc5ba4cdb14c1b7b0c08ac35dca. Wyrenderowano 3/3 strony, obejrzano rysunek na stronie 297, porównano podpis z obiektem: bez widocznej kolizji. Wszystkie bloki tekstowe leżą w obrębie stron. W logu 0 LaTeX Warning, Overfull, Underfull, Missing character, Undefined control sequence i undefined references. Workflow zbudował książkę dwukrotnie. Samodzielny bieżący rozdział z artefaktu CI dotyczył LA-32, dlatego LA-30 wycięto poprawnie z pełnej książki.

## 4. Status globalny i następny etap

Uzgodniona zasada stabilizacji jest spełniona dla dokładnie bieżącego bloba dzięki wcześniejszym czystym audytom re_audit_from_ch12/30_iteration_03–04 i dodatkowemu krytycznemu 05. Pierwotny równoległy audyt korekcyjny 03 nie jest zaliczany jako czysty; dokumentacja odróżnia go od faktycznie czystego audytu 03. Obecny audyt globalny 31 jest czysty, bez poprawki źródła, więc licznik nie jest resetowany.

**LA-30: STABILNY; globalnie skontrolowano 366/382 dowodów.** Pozostało 16, LA-31: 6 i LA-32: 10. W następnej *osobnej* iteracji przejść do LA-31, a po 382/382 przeprowadzić jeszcze dodatkowy sceptyczny przekrojowy audyt całej książki. Na bieżącym commicie dokumentacyjnym nie deklaruje się przyszłego CI przed faktycznym wynikiem.
