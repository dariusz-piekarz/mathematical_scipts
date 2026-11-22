# Logika matematyczna i teoria mnogości — audyt IV rozdziału 33

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/33-relacja-wymuszania-i-twierdzenie-o-wymuszaniu.tex`.  
**Cel:** czwarty, niezależny audyt matematyczny, językowy i integracyjny. Priorytetem była próba obalenia twierdzeń przez skonstruowanie małych kontrprzykładów, a nie dalsze przeredagowywanie poprawnego już tekstu.

## Wynik audytu matematycznego

**Nie stwierdzono nowej luki w dowodach ani kontrprzykładu.** W szczególności nie wprowadzono zmian do źródła LaTeX rozdziału 33. Weryfikacja objęła:

1. **Rekurencję atomową:** w definicjach wymuszania równości i przynależności każde odwołanie do relacji pomocniczej dotyczy pary nazw o mniejszej sumie naturalnej $\operatorname{rk}(\sigma)\mathbin{\#}\operatorname{rk}(\tau)$; uwzględniono również nazwę pustą, rangi następcze i pary równoważnych warunków w preorderze.
2. **Definiowalność w $M$:** relacja jest schematem dla każdej ustalonej formuły, ze wszystkimi potrzebnymi parametrami $\mathbb P$ i $\leq$. Rekurencję można obliczać na zbiorze dziedzicznie występujących nazw; wymuszanie egzystencjalne nie wymaga utworzenia zbioru wszystkich nazw. Nie mylono definiowalności wymuszania z wewnętrznym predykatem prawdy.
3. **Monotoniczność i regularność:** dla relacji atomowych i klauzul $\neg$, $\land$, $\exists$ zweryfikowano kierunek wzmacniania $q\leq p$, lokalną gęstość oraz rozstrzyganie każdej formuły przez gęsty zbiór warunków.
4. **Atomowy i pełny lemat prawdy:** osobno sprawdzono oba kierunki przynależności, oba kierunki równości i kroki indukcji dla negacji, koniunkcji i egzystencji. Gęsty zbiór rozstrzygnięć i zbiór $E$ z dowodu równości należą do $M$, dzięki lematowi definiowalności; nie wykorzystuje się przedwcześnie aksjomatów ZFC w $M[G]$.
5. **ZFC w $M[G]$:** dowody aksjomatów sumy, wyróżniania i zbioru potęgowego wykorzystują nazwy ograniczone do zbiorów $B_\tau$ i $A_\tau$ w $M$; nazwa $\Pi_\tau$ obejmuje wszystkie podzbiory $\tau^G$ należące do $M[G]$. Dla zastępowania najpierw tworzy się zbiór $J$ par z kandydatami, przez zastępowanie ogranicza rangi minimalnych świadków jedną liczbą porządkową $\gamma$, a następnie korzysta z aksjomatu wyboru na zbiorze $\mathbb P\times N_{\gamma+1}^M$. W aksjomacie wyboru surjekcja $e:\kappa\to A_\tau$ zapewnia funkcję, której obraz obejmuje $a=\tau^G$, wystarczającą do wyznaczenia dobrego uporządkowania $a$.
6. **Minimalność i granice metamatematyczne:** wyliczenie każdej $\tau^G$ w dowolnym tranzytywnym modelu ZFC zawierającym $M$ i $G$ jest możliwe na mocy rekurencji po rangach. Warunek istnienia przeliczalnego tranzytywnego modelu zbiorowego nie jest utożsamiany z samą niesprzecznością ZFC.

## Nowy, głębszy test semantyczny

Dodano do `tools/tests/test_logic_and_set_theory_ch33.py` test `test_exhaustive_bounded_rank_two_atomic_truth`. W tym teście:

- \(\mathbb P=\{(),(0,),(1,)\}\) jest skończonym drzewem z warunkiem największym;
- generowane są wszystkie 8 nazw pierwszego poziomu oraz 79 nazw drugiego poziomu, złożonych z co najwyżej dwóch par wybranych spośród 12 par z czterech reprezentantów poziomu pierwszego;
- po usunięciu powtórzeń otrzymujemy **80 różnych nazw**, a więc $80^2=6400$ uporządkowanych par;
- dla każdej pary, każdego z dwóch filtrów generycznych i obu atomowych relacji ($\in$, $=$) porównuje się wartość formuły dla interpretacji nazw z istnieniem warunku wymuszającego tę formułę w filtrze: **$80^2\cdot2\cdot2=25\,600$ porównań**;
- wszystkie 25 600 przypadków przeszły niezależną lokalną kontrolę Python, bez kontrprzykładu; implementacja relacji atomowej jest oparta na klauzulach rekurencyjnych i korzysta z cache, nie z założonego z góry lematu prawdy.

Jest to kontrola regresji i skończonych modeli, **a nie formalny dowód lematu prawdy w ogólnym przypadku ani formalizacja w Lean**.

## Kontrola inwentarza

**Źródło rozdziału matematycznego bez zmian w audycie IV.** Pozostaje 4 definicje, 6 lematów, 6 twierdzeń, 3 przykłady, 5 uwag i 12 dowodów; 25 etykiet i 26 odsyłaczy. Książka liczy 33 rozdziały z 828 etykietami i 616 odsyłaczami.

**Testów regresyjnych rozdziału 33:** 17 (w audycie III było 16).

## Walidacja i decyzja

[GitHub Actions — przebieg #45021551172](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45021551172). **Pełny wynik kompilacji i kontroli PDF pozostaje do dopisania po zamknięciu przebiegu.**

**Werdykt matematyczny audytu IV:** nie znaleziono nowych usterek i nie zmieniono tekstu rozdziału 33. Jeżeli bieżąca kontrola CI przejdzie, rozdział można uznać za **stabilny po IV audytach**, zgodnie z przyjętym kryterium czystej iteracji, przy zachowaniu rozróżnienia między stabilnością redakcyjną a formalną weryfikacją dowodów.
