# Topologia ogólna — globalny audyt 39: czysta kontrola 1/2 rozdziałów 06 i 21 po korekcie ilustracji

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zakres:** matematyczny i wydawniczy reaudyt **wyłącznie nowych blobów** rozdziałów 06 i 21, po rzeczywistym usunięciu kolizji w rysunkach 6.1 oraz 21.1. Źródła matematyczne nie były w tej iteracji modyfikowane.

## 1. Dokładne porównanie treści matematycznej

Pobrano stare pliki na commicie `73bfc3fb9f83c4e22afad138237a395fe50363ed` oraz nowe pliki po commitach `9352c1be6617a2d031f7d26ead166b8ccc55995a` i `1e0b2003b6a8a24a69400cb896ee5c6a45d99539`. Nie oparto się na samych liczbach:

| Rozdział | Obecny blob Git | Środowiska proof | Test dokładnej zgodności treści proof | `label` | `ref` |
|---|---|---:|---|---|---|
| 06 — Zbieżność topologiczna | `71d7b30abb97286b7c64ddd5e369ec9f69ea1ff5` | 18 | **wszystkie 18 identyczne** z wersją przed rysunkiem | identyczne | identyczne |
| 21 — Topologie na rodzinach podzbiorów | `eae0bef9c2357189e1bdb7c9398b845fe7347c7b` | 15 | **wszystkie 15 identyczne** z wersją przed rysunkiem | identyczne | identyczne |

Zachowano definicje i wyniki matematyczne bez edycji; zmieniono wyłącznie pionowe/poziome położenie podpisów wewnątrz dwóch diagramów. Nie należy mylić pełnej identyczności dowodów z identycznością całych plików: bloby obu rozdziałów rzeczywiście się zmieniły.

## 2. Powtórne kontrole wybranych argumentów rozdziału 06

1. **Kryterium ciągowe pod pierwszym aksjomatem przeliczalności:** dla malejącej bazy otoczeń `W_n` zanegowanie ciągłości daje ciąg `x_n∈W_n\setminus f^{-1}(V)` zbieżny do x, lecz jego obrazy nie są ostatecznie w V. Hipoteza przeliczalności jest potrzebna wyłącznie w tym kierunku.
2. **Punkt skupienia i podsieć:** skierowany zbiór par `(d,U)` wykorzystuje ostateczną współkońcowość φ i nie wymaga jej monotoniczności. Dowód nie stosuje ukrytego przeliczalnego wyboru.
3. **Filtr z bazy oraz zamiana filtrów na sieci:** para `(F,a)` ma właściwą relację na zbiorach i świadków w F. Kluczowy kierunek `F⊆U` wynika z rozważenia **wszystkich** `(F,b)` z b∈F, nie tylko jednego punktu. Środowisko `proof` po definicji filtru jest nazwanym uzasadnieniem konstrukcji, nie błędnie przypisanym dowodem poprzedniego twierdzenia.

Wynik tych niezależnych kontroli merytorycznych po zmianie TikZ: **PASS**, bez kolejnej zmiany źródła. Pełną wcześniejszą kontrolę matematyczną 06 udokumentowano w globalnym audycie 36; bieżące trzy kontrole są odrębnym sprawdzeniem na nowym blobie.

## 3. Powtórne kontrole wybranych argumentów rozdziału 21

1. **Vietoris i odległość Hausdorffa:** dla trafiania U istotny jest jeden punkt `x∈K∩U` i kula otwarta, dla zawierania `K⊂U` dodatnie minimum funkcji odległości od domkniętego dopełnienia na zwartym K. Odwrotna inkluzja topologii korzysta ze skończonej sieci kul promienia r/3 oraz z otoczenia `V^+∩⋂B(x_i,r/3)^-`. Kontrola wykazuje obie inkluzje.
2. **Zupełność `𝒦(X)`:** jednorodne oszacowanie `|d(x,A)-d(x,B)|≤d_H(A,B)` daje graniczną funkcję f; zbiór K={f=0} jest niepusty przez łańcuch punktów Cauchy'ego, następnie całkowicie ograniczony przez skończoną sieć jednego z A_j. Dopiero po tym dowodzi się zwartości K i oblicza `d_H(A_j,K)`; nie użyto kompaktowości przed jej udowodnieniem.
3. **Kompaktowość topologii Fella z pustym zbiorem:** lemat Aleksandra redukuje pokrycia do zbiorów podbazowych. Dla hipotetycznego pokrycia bez skończonego podpokrycia buduje się `F=X\setminus⋃U_i`, które jest domknięte, być może puste. Z własności skończonych przecięć i zwartości `C_j` wynika `F∩C_j≠∅` dla wszystkich j. Stąd F nie trafia żadnego `U_i`, ale nie należy też do `C_j^0`; sprzeczność. Argument faktycznie wykorzystuje dopuszczenie `F=∅`.
4. **Rysunek 21.1 i liczby:** dla A={0,2} i B={1/5,17/10} oba kierunkowe supremum wynoszą 3/10. Przesunięcie etykiet A/B nie zmienia położenia żadnego z czterech punktów ani wartości `d_H`.

Wynik nowej kontroli 21: **PASS matematyczny i graficzny**, bez następnej zmiany źródła.

## 4. PDF, testy regresyjne i rzeczywisty CI

Z post-edycyjnego artefaktu **14798298647**, workflow [45133887910](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133887910), potwierdzono **188 stron** pełnej książki, **27 unikatowych podpisów rysunków** i brak ostrzeżeń w logach całej książki oraz samodzielnych rozdziałów 06 i 21.

Kontrola współrzędnych pól tekstowych post-PDF:
- w **6.1** dolny brzeg ε = 134,18 pt, górny brzeg „wyrazy dalsze” = 139,69 pt; przerwa co najmniej **5,51 pt**;
- w **21.1** dolny brzeg A = 171,69 pt, górny brzeg B = 177,03 pt; przerwa co najmniej **5,34 pt**.

Nowe geometryczne regresje statyczne istnieją w testach `test_general_topology_ch06.py` i `test_general_topology_ch21.py`. **Workflow [45134198801](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45134198801) po naprawie składni obydwu regresji ma stan `completed/success` na commicie `a0dd1d5f10c0d3b47b8ddab59ebc7c04d23e11ef`.** Osobno sprawdzono listę kroków tego workflow: „Verify Chapter 06 nets, filters and convergence” oraz „Verify Chapter 21 hyperspace finite models and references” mają `completed/success`. Błąd SyntaxError z pierwszej implementacji testów jest naprawiony; nie wolno go zatajać w historii audytu. Późniejszy workflow samego raportu 38 `45134587477` był nadal w toku przy wcześniejszej kontroli i jego końcowy stan wymaga odrębnego sprawdzenia.

## 5. Decyzja

**Czysta kontrola po poprawce 1/2 dla nowego źródła rozdziałów 06 i 21.** Obie usterki wizualne naprawione; 33 dowody i wszystkie etykiety/odsyłacze zachowane bez zmian, dodatkowe kluczowe argumenty sprawdzone niezależnie, PDF obejrzany, nowe testy przeszły w rzeczywistym CI.

Zgodnie z rygorem pracy rozdziały 06 i 21 nie odzyskują jeszcze finalnego statusu stabilizacji 2+1 na *nowych* blobach. Pozostaje **drugi czysty audyt niezależny** i **osobna kontrola potwierdzająca (+1)**, najlepiej z oględzinami ich samodzielnych PDF z nowego kompilatora oraz aktualnym CI. Dopiero po tym powinna nastąpić ostateczna walidacja całej książki. Automatyzację pozostawić aktywną.
