# Algebra liniowa — audyt globalny, iteracja 20: LA06–08

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Kontynuacja:** [iteracja 19](iteration_19.md).

**Wynik matematyczny: CZYSTY w skontrolowanym zakresie**. Przeczytano pełne sformułowania i wszystkie **45 dowodów** LA06–08 oraz **20 przykładów**. Nie stwierdzono usterki wymagającej zmiany źródeł. Wyniki testów skończonych nie są formalnym sprawdzeniem twierdzeń w Lean.

## 1. Zamrożone źródła

| Rozdział | SHA bloba | Wiersze | Dowody | Etykiety | Odsyłacze | Przykłady | Rysunki |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LA06 — wyznaczniki | `ca2041609035de1bbe8ce390ccc23c0369d726fb` | 859 | **11/11** | 32 | 11 | 5 | 1 |
| LA07 — przestrzeń dualna i odwzorowania dualne | `5e320759f55012f807be790214d6ad76119ab544` | 1264 | **20/20** | 45 | 15 | 5 | 1 |
| LA08 — odwzorowania wieloliniowe | `0cd0e91a194700b38862f2f1478a693dcd2e5dd3` | 1367 | **14/14** | 43 | 14 | 10 | 0 |
| **Razem** | | **3490** | **45/45** | **120** | **40** | **20** | **2** |

[Indywidualny rejestr 45 twierdzeń i dowodów](iteration_20_proof_review_06_08.csv) zawiera odrębne notatki o sprawdzonych założeniach i argumentach oraz SHA i zakresy wierszy. Poziom `CZYSTY` oznacza matematyczną lekturę tezy i dowodu, nie uruchomioną weryfikację Lean.

## 2. LA06 — wyznaczniki: 11 dowodów

1. **Znak permutacji, naprzemienność i charakterystyka 2:** zamiana sąsiednich elementów zmienia parzystość liczby inwersji, a parowanie wyrazów wyznacznika daje zero nawet w charakterystyce 2. Dowód aksjomatycznej jednoznaczności wyznacznika osobno wyprowadza zmianę znaku przy przestawieniu wierszy. Poprawne są przypadki (n=0), (n=1).
2. **Operacje wierszowe, trójkątność i transpozycja:** sprawdzono dopuszczalne operacje, znak permutacji odwrotnej i argument, że przy trójkątnej macierzy tylko permutacja identycznościowa może dawać niezerowy wyraz. Pusty iloczyn dla (n=0) to (1_K).
3. **Multiplikatywność:** dla ustalonego (B) funkcja (F(A)=\det(AB)) jest wieloliniowa i naprzemienna w wierszach (A). Z normalizacji (F(I)=\det B) otrzymuje się (\det(AB)=\det A\det B), także dla nieodwracalnych macierzy.
4. **Odwracalność, Laplace, macierz dołączona i Cramer:** wszystkie kroki z użyciem niezerowego wyznacznika mają jawne założenie; wzór Laplace'a obejmuje (n=1) i pusty minor; oba kierunki tożsamości (A\operatorname{adj}(A)=\operatorname{adj}(A)A=\det(A)I) są udowodnione przez zamianę wiersza/kolumny. Wzory Cramera wynikają z wieloliniowości względem kolumn.
5. **Przykłady:** sprawdzono pięć rachunków, w tym wyznacznik 13 z eliminacji, macierz dołączoną (2\times2), oraz rozwiązanie ((2,1)) metodą Cramera.

## 3. LA07 — przestrzeń dualna: 20 dowodów

1. **Baza dualna i transformacje:** z ewaluacji i rozszerzania z bazy otrzymuje się funkcjonały (v^i) oraz naturalną ewaluację (V^*\times V\to K). Przy konwencji ([v]_B=P[v]_C) obowiązuje ([\varphi]_{C^*}=P^{\mathsf T}[\varphi]_{B^*}). Nie wprowadza się sprzężenia zespolonego w formule ewaluacji.
2. **Anihilatory:** skontrolowano (\dim U^\circ=n-\dim U), obydwie równości podwójnego anihilatora, wzór na anihilator przecięcia, rozszerzenie funkcjonału oraz identyfikację ((V/U)^*\cong U^\circ). Przypadki (U=0), (U=V) i wymiar 0 są ujęte.
3. **Odwzorowania dualne:** (T^*\colon W^*\to V^*) jest liniowe, odwraca składanie, a jego macierz w bazach dualnych jest **transpozycją** (A^{\mathsf T}) macierzy (T), nie sprzężoną transpozycją. Zweryfikowano (\ker T^*=(\operatorname{im}T)^\circ) i (\operatorname{im}T^*=(\ker T)^\circ), łącznie z dobrze określoną faktoryzacją i przedłużeniem funkcjonału.
4. **Bidualność i ślad:** odwzorowanie (J_V(v)(\varphi)=\varphi(v)) jest kanonicznym izomorfizmem w skończonym wymiarze i jest naturalne względem (T). Sprawdzono cykliczność śladu oraz wzór (\operatorname{tr}(x\mapsto\varphi(x)v)=\varphi(v)).
5. **Przykłady:** pięć przykładów obejmujących zmianę bazy dualnej, anihilator płaszczyzny i macierz (T^*); wzór (A^{\mathsf T}(2,-1,1)=(6,5)) i jego bezpośrednie obliczenie są zgodne.

## 4. LA08 — odwzorowania wieloliniowe: 14 dowodów

1. **Współrzędne i zmiany baz:** wartość odwzorowania na krotkach wektorów bazowych jednoznacznie wyznacza odwzorowanie wieloliniowe. Wzór zmiany baz zawiera odpowiednie (P_r) na argumentach i (Q^{-1}) na przeciwdziedzinie. Dla formy dwuliniowej macierz zmienia się przez **kongruencję (P^{\mathsf T}AP)**, bez sprzężenia.
2. **Radykały i formy symetryczne:** lewy radykał ma współrzędne w (\ker A^{\mathsf T}), prawy w (\ker A). Liczba współczynników formy symetrycznej wynosi (\binom{n+k-1}{k}), z osobnymi konwencjami dla (n=0), (k=0).
3. **Naprzemienność i charakterystyka 2:** naprzemienność implikuje antysymetrię w każdym ciele, ale odwrotność wymaga (2_K\ne0_K). Baza form naprzemiennych przez minorowe wyznaczniki działa również w charakterystyce 2.
4. **Alternowanie:** w dowodzie (\mathcal AF) jest naprzemienna **także w charakterystyce 2**, co wynika z inwolucji bez punktów stałych parującej permutacje po zamianie dwóch równych argumentów. Dopiero gdy (k!1_K\ne0_K), normalizowane symetryzacja i alternowanie są rzutowaniami. Dowód polaryzacji z włączenia–wyłączenia nie dzieli przez (k!) w charakterystyce, w której nie jest to dozwolone.
5. **Przykłady:** dziesięć przykładów skontrolowanych merytorycznie, m.in. formy trójliniowej (F((1,2),(3,4),(5,6))=92), nieprzemienność zwykłej liniowości iloczynu wielomianów, przykład antysymetrii nienaprzemiennej nad (\mathbb F_2), oraz zanikanie funkcji diagonalnej niezerowej formy naprzemiennej nad (\mathbb F_2).

## 5. Niezależne testy dokładne

Wykonano reprodukowalny, pozbawiony zależności zewnętrznych skrypt [test LA06–08](../../../tools/test_linear_algebra_la06_la08_exhaustive.py) jako lokalny odpowiednik `/mnt/data/la_iter20_test.py`. Zbadano:
- **20 923** macierze kwadratowe nad (mathbb F_2), (mathbb F_3) i (mathbb F_5), w tym wymiar 0: wyznaczniki, rozwinięcia Laplace'a, tożsamości macierzy dołączonej, odwracalność i Cramera;
- **2 182** macierze odwzorowań dualnych z niezależną enumeracją ich jąder, obrazów i anihilatorów, także przy wymiarze zerowym;
- **865** form wieloliniowych nad małymi ciałami, w tym charakterystyka 2: przekształcanie przy permutacjach, symetryzacja i alternowanie, powtarzające się argumenty i warunek dzielenia przez (k!).

**Wynik lokalnego wykonania: 214 892 / 214 892 PASS, 0 FAIL**. Kontrole w kodzie źródłowym testu dzielą się na nazwane grupy, które wypisują liczbę sprawdzeń. Test dodano do repozytorium i jako obowiązkowy krok CI do `.github/workflows/linear-algebra-chapter.yml`, a także do filtra ścieżek uruchamiających workflow. Testy małych modeli nie zastępują ogólnych dowodów i nie stanowią formalizacji Lean.

## 6. LaTeX, ilustracje, CI i ograniczenia

- **120 etykiet, 40 odsyłaczy, 45 poprawnie zamkniętych środowisk `proof`**: brak lokalnych duplikatów etykiet i wykrytych naruszeń przyjętej polskiej terminologii w LA06–08. Odsyłacze do innych rozdziałów podlegają dodatkowo kontroli w workflow.
- **Dwa źródła ilustracji TikZ:** równoległobok i znaczenie wyznacznika (LA06) oraz diagram odwrócenia kierunku przez odwzorowanie dualne (LA07) przedstawiają poprawne zależności. Nie wykonano nowej wizualnej inspekcji wyrenderowanego PDF w tej iteracji.
- Przebieg [CI 45064528288](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064528288) z końca iteracji 19 ma status **completed/success**, łącznie z kompilacją PDF. W chwili przygotowania niniejszego wpisu nowy przebieg [CI 45065176577](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45065176577) dla testu LA06–08 był **w toku**. W osobnej kontroli workflow potwierdzono następnie **`completed/success`** dla: (1) nowego kroku testowego **LA06–LA08**, (2) dwukrotnej kompilacji książki PDF, (3) kontroli pliku PDF i nierozwiązanych odsyłaczy. **Finalnie cały przebieg CI 45065176577 zakończył się `completed/success`.** Potwierdzono też sukces eksportu rozdziału oraz zapisania artefaktu skompilowanej książki. Nie oznacza to wizualnej inspekcji stron PDF.
- Matematyczne źródła LA06–08 nie wymagały zmiany. Nie zresetowano stabilizacji LA12–32 ani nie dopisywano nieuzgodnionych tematów.

## 7. Status i dalszy plan

Po iteracjach 17–20 najnowszy indywidualny rejestr obejmuje **155/382** środowisk dowodowych. Do analogicznego przeglądu pozostaje **227**: LA09–11 (**53**), LA14–16 (**42**), LA17–24 (**61**) i LA25–32 (**71**). Wszystkie były wcześniej kontrolowane rozdziałowo; nowe liczenie oznacza szczegółowy globalny rejestr, nie negację wcześniejszej pracy.

Następnie należy dokończyć pełny audyt globalny i wykonać jeszcze **jedną sceptyczną iterację sprawdzającą**, z odsyłaczami, PDF i kontrolą terminologii.