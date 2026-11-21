# Algebra liniowa — rozdział 17, audyt III (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/linear_algebra/17-postac-jordana.tex`  
**Blob kontrolowanego tekstu:** `d116dc8fc69bd8c016ba1ccc536702b33f516ef1`  
**Poprzednie audyty:** `ch17_iteration_01.md` i `ch17_iteration_02.md`.

## Niezależna kontrola całości rozdziału

1. **Definicje i przypadki brzegowe.** Sprawdzono definicję operatora nilpotentnego, indeks nilpotentności, łańcucha Jordana i bloku Jordana, wraz z przypadkami (n=0), (s=1) oraz dowolną charakterystyką ciała. Prawidłowo rozróżniono `N^0=I` oraz `N^m=0`.
2. **Filtracja jąder.** Z `ker N^(k+1)=ker N^k` wynika stabilizacja wszystkich późniejszych jąder; jeżeli `N` jest nilpotentny na przestrzeni niezerowej, pierwsze `m` inkluzji są ścisłe, skąd `m<=dim V`.
3. **Niezależność łańcucha.** W dowodzie sukcesywnie stosuje się `N^(s-1), N^(s-2),...`, co zeruje wcześniejsze wektory i izoluje kolejne współczynniki. Kierunek przesunięcia odpowiada jedynkom na nadprzekątnej.
4. **Istnienie bazy Jordana dla nilpotentnego operatora.** Zweryfikowano kompletną indukcję po `W=im N`: niezależność końcowych wektorów modulo `N(W)`, istnienie preobrazów `v_i`, niezależność modulo `W`, `N(U)=W`, obliczenie `dim(U∩ker N)=r`, uzupełnienie o wektory `z_j∈ker N` i pełen bilans wymiaru. W przypadku `N=0` dowód nie ma wyjątków wymagających dodatkowych założeń.
5. **Liczba i rozmiary bloków nilpotentnych.** Dla rozmiaru `s` wymiar jądra `N^k` wynosi `min(k,s)`; pierwsza różnica ciągu `d_k` zlicza bloki długości co najmniej `k`, a druga daje liczbę bloków dokładnie długości `k`. Podana formuła `2d_k-d_(k-1)-d_(k+1)` jest prawidłowa.
6. **Postać Jordana dla operatora ogólnego.** Każda uogólniona przestrzeń własna jest niezmiennicza, a ograniczenie `(T-λI)` jest nilpotentne. Po połączeniu baz z łańcuchów uzyskuje się `P^{-1}AP=J` w dowolnej wybranej bazie. Warunek rozszczepienia `χ_T` nad `K` jest konieczny i wystarczający; w dowodzie nie zakłada się bez uzasadnienia algebraicznego domknięcia.
7. **Jednoznaczność.** Dla innych wartości własnych `μ≠λ` macierz `(μ-λ)I+N_s` jest odwracalna, z odwrotnością wyrażoną skończonym szeregiem. Jądra potęg `(T-λI)^k` wyznaczają wszystkie rozmiary bloków `λ`. To uzasadnia jednoznaczność z dokładnością do permutacji bloków.
8. **Wielomiany i diagonalizacja.** Właściwie wyliczono `χ_T` jako iloczyn wielomianów bloków i `m_T` jako ich moniczną najmniejszą wspólną wielokrotność. Gdy `V=0`, pusty iloczyn i NWW pustej rodziny są równe `1`. Poprawnie wykazano równoważność diagonalizowalności i bloków rozmiaru `1`.
9. **Przykłady.** Niezależnie sprawdzono konkretne macierze i wzory dla `(0,3,5,7,7)`, dla wartości własnych `1,3` w wymiarze `6` i dla dwóch niediagonalizowalnych macierzy o tym samym wielomianie charakterystycznym. Doprecyzowany w audycie II argument `d_(1,3)+d_(3,3)=6` rzeczywiście wyklucza większe bloki.
10. **Redakcja, skład i odsyłacze.** Wszystkie 21 etykiet są różne, 8 odsyłaczy prowadzi do istniejących etykiet w rozdziałach 16 i 17, 7 środowisk `proof` jest sparowanych. Poprawne są indeksowanie, język, pojęcia, nazewnictwo i rozdzielenie twierdzeń od przykładów. Bez dalszych poprawek treści.

## Automatyzacja i PDF

- [GitHub Actions 44935907983](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935907983) — sukces: kontrola struktury, testy postaci Jordana i filtracji jąder, dwukrotna kompilacja LaTeX, odsyłacze i eksport osobnego PDF rozdziału 17. Kolejne pomyślne przebiegi na tej samej gałęzi nie zmieniły pliku rozdziału.
- Zweryfikowano 6-stronicowy plik PDF `algebra_liniowa_rozdzial_17_audyt_II.pdf` pochodzący z pomyślnego eksportu. Wszystkie strony mają tekst. Za pomocą PyMuPDF sprawdzono współrzędne wszystkich bloków: **0 bloków poza granicami stron**. Wszystkie sześć stron ponownie wyrenderowano i obejrzano; nie wykryto ucięć wzorów, kolizji tekstu ani pustych stron.

## Decyzja

**Audyt III — czysty, bez żadnych poprawek źródła rozdziału.** Po trzech iteracjach rozdział 17 otrzymuje status **STABILNY**. Do zatwierdzonego tekstu nie dodajemy kolejnych twierdzeń przy zwykłym audycie. Następnym etapem prac jest rozdział 18 na dotychczasowej gałęzi.
