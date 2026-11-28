# AA-X02 — dodatkowy niezależny audyt potwierdzający (AA-25–AA-27)

**Data:** 23 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**HEAD sprawdzony przed zapisem:** `5362b524f2b7d4216304ab1653e6d4f5d3444a06`.  
**Zakres:** krytyczna kontrola uprzednio audytowanego połączenia 90. twierdzenia Hilberta, teorii Kummera i teorii Artina–Schreiera. Jest to **dodatkowy, oddzielny audyt potwierdzający AA-X02**, nie nowy rozdział i nie audyt całej książki.

## 1. Tożsamość źródeł i niezależność kontroli

Przed rozpoczęciem i przed publikacją zweryfikowano aktualną gałąź i aktualne źródła. Zachowane bloby:
- AA-25: `2524f56e0a4802d28c441ff932ba5399a10eb61c`;
- AA-26: `5bee95fdfedeaaf4fc697dce636e5d82afcd249b`;
- AA-27: `628da680adc66f257511a260df4283db8cb9a7d7`.

W odróżnieniu od pierwszego AA-X02 (2514 sprawdzeń w JavaScript dla `F_2, F_4, F_8, F_3, F_9, F_27, F_5, F_{25}, F_7, F_{343}`), bieżący audyt oparto na **odrębnej implementacji w Pythonie** z redukcją wielomianów czwartego stopnia i niezależnym obliczaniem rzędów macierzy przez eliminację Gaussa nad ciałem pierwszym. Użyto nowych modeli oraz innych generatorów grup Galois. Kontrola nie opiera się wyłącznie na powtórzeniu uprzedniego kodu.

## 2. Testy sceptyczne — 1145/1145 PASS

Wszystkie rachunki wykonano dokładnie, na współczynnikach całkowitych modulo `2` i `3`, bez tolerancji numerycznych:

- `F_{16}=F_2[t]/(t^4+t^3+1)`;
- `F_{81}=F_3[t]/(t^4+t^3+t^2+1)`.

Dla tych ciał sprawdzono pięć par `(L/K,σ)`, gdzie automorfizm `σ` jest odpowiednio potęgą Frobeniusa:

| Model | `[L:K]` | `rank_K(1−σ)` | `rank_K(Tr)` | `|ker Tr|` | `|ker N|` | Testy |
|---|---:|---:|---:|---:|---:|---:|
| `F16/F2, σ(x)=x²` | 4 | 3 | 1 | 8 | 15 | 73 |
| `F16/F2, σ(x)=x⁸` | 4 | 3 | 1 | 8 | 15 | 73 |
| `F81/F3, σ(x)=x³` | 4 | 3 | 1 | 27 | 40 | 333 |
| `F81/F3, σ(x)=x²⁷` | 4 | 3 | 1 | 27 | 40 | 333 |
| `F81/F9, σ(x)=x⁹` | 2 | 1 | 1 | 9 | 10 | 333 |
| **Razem** | | | | | | **1145** |

**Uwaga o rzędach:** Dla `F81/F9` liczby `rank_K` w tabeli wynoszą `1,1` (rangi liczone nad `K=F9`); implementacja oblicza macierze nad `F3`, więc uzyskuje rangi `2,2`. Wynik obliczeniowy jest zgodny z `[F9:F3]=2`.

W każdym modelu sprawdzono:
1. potęgi Frobeniusa, odwracalność każdego niezerowego elementu i rozmiar ciała elementów stałych `L^{<σ>}=K`;
2. niezależnie `\operatorname{im}(1−σ)=\ker\operatorname{Tr}_{L/K}` oraz `\{b/σ(b):b∈L^×\}=\ker N_{L/K}`;
3. niezależne rangi obu operatorów i liczności obrazu/jądra; surjektywność śladu na `K` oraz normy na `K^×`;
4. przypadek `\operatorname{char}K\mid[L:K]` dla `F16/F2`: `Tr(1)=0`, lecz funkcjonał śladu nie jest zerowy, zgodnie z kluczowym argumentem AA-25.

**Krytyczny test Artina–Schreiera:** równanie `x^p−x=a` dla niezerowego `a∈F_p` ma w `F_{p^4}` pierwiastek dokładnie wtedy, gdy `p|4`. Sprawdzono dwa pierwiastki dla `x²−x=1` w `F16` i brak pierwiastków `x³−x=1` oraz `x³−x=2` w `F81`. Zapobiega to fałszywemu utożsamieniu separowalności z istnieniem pierwiastka w dowolnym rozszerzeniu o stopniu `4`.

**Wynik:** 1145/1145 testów właściwych PASS, dodatkowo powyższe kontrole pierwiastków Artina–Schreiera PASS. Nie wykryto błędów w hipotezach dotyczących cykliczności, charakterystyki ani przejść między wynikami AA-25–AA-27. Źródła TeX pozostawiono bez zmian.

## 3. Potwierdzone GitHub Actions i inspekcja rzeczywistego PDF

Zweryfikowano rzeczywisty przebieg **Abstract algebra AA-01 to AA-42 validation**:
<https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083652049>

- SHA commitu testowanego przez CI: `8cd2bb3ed85af64e616071d6b81128f75ce7ffba`.
- Status przebiegu: `completed / success`.
- Nowy krok **Run AA-25 to AA-27 finite-field cross-audit**: `success`.
- **Run repository tool tests**: `success`.
- **Compile AA-01 to AA-42 book with latexmk**: `success`.
- **Verify PDF and references (no undefined refs)**: `success`.
- **Archive build output**: `success`.

Pobrano nie tylko status workflow, lecz **oryginalny artefakt z tego przebiegu** `abstract-algebra-aa01-aa42` (GitHub artifact ID `14778262614`), z plikami `abstract_algebra.pdf` i `abstract_algebra.log`. PDF ma **269 stron**, SHA-256:
`a63d837171926d1ddc848ce6a1e06b2f98fb722cc2480498c62695aa4618539f`.

Niezależnie przeanalizowano log: **0 ostrzeżeń LaTeX**, **0 ostrzeżeń `hyperref`**, **0 `Overfull \\hbox`**, **0 `Overfull \\vbox`**, **0 `Underfull \\hbox`**, **0 zgłoszonych niezdefiniowanych odsyłaczy** i **0 błędów LaTeX**.

Przeprowadzono kontrolę wizualną składu **wszystkich 15 stron PDF 178–192**, na których mieszczą się AA-25 (s. 178–182), AA-26 (s. 183–188) i AA-27 (s. 189–192), oraz szczegółową kontrolę strony PDF 186 z rysunkiem 26.1. Nie stwierdzono obcięć, kolizji podpisu z rysunkiem ani widocznych problemów składu.

Wybiórcza kontrola wizualna PDF nie jest dowodem formalnej poprawności całej książki; osobne testy matematyczne są opisane powyżej.

## 4. Werdykt i następny etap

**AA-X02: STABILNY**. Pierwszy audyt matematyczny AA-X02, osobny sceptyczny audyt potwierdzający, rzeczywiście zakończony sukcesem CI, pobranie artefaktu, analiza logu i wizualna kontrola 15 stron nie wykazały konieczności korekty. Nowy audyt potwierdzający zamyka ten konkretny etap; **liczba zmian źródłowych po jego rozpoczęciu: 0**.

Nie dodano nowych twierdzeń ani definicji, nie zmieniono `\label` / `\ref`, nie utworzono nowej gałęzi. Nie znaleziono źródła AA-43.

**Dalsze działanie:** w nowej, odrębnej iteracji wybrać nieredundantną kontrolę przekrojową spoza AA-X01 i AA-X02, np. dokładny łańcuch zależności AA-31–AA-36. Zachować zasady stabilizacji oraz dodatkowego niezależnego audytu przed przejściem do następnego zakresu.
