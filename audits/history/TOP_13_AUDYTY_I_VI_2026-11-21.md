# Topologia algebraiczna — TOP-13, audyty I–VI (cykl stabilizacyjny)

**Data:** 2026-11-21  
**Rozdział:** `chapters/pl/algebraic_topology/13-przestrzenie-klasyfikujace-i-teoria-przeszkod.tex`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` — bez zmian w `main`.  
**Zasady:** wyłącznie korekta i weryfikacja istniejących twierdzeń, definicji, dowodów, przykładów, rysunków i składni. Bez dodawania nowych tematów, twierdzeń i lematów.

## Audyt I — przegląd całego rozdziału i wcześniejszej historii

Przeczytano pełne źródło TOP-13, 995 wierszy przed bieżącymi poprawkami, oraz wcześniejsze raporty `TOP_13_14_FINAL_REAUDIT_2026-11-21.md` i `TOP_13_14_REAUDYT_SCALENIE_2026-11-21.md`. Weryfikowano istnienie i jednoznaczność `K(G,n)`, reprezentację kohomologii, bar-model dla grup dyskretnych, modele Milnora `EG/BG`, klasyfikację wiązek, monodromię, pierwszą przeszkodę, sprzężone klasy Eulera, funkcje sklejające, przestrzenie Moore'a oraz przykłady współczynników lokalnych.

**Wniosek:** wcześniejsza korekta kocyklu pierwszej przeszkody i obliczeń Moore'a zachowała poprawność. Znaleziono jednak luki w dowodzie jednoznaczności `K(A,n)` i w opisie konstrukcji wiązek.

## Audyt II — jednoznaczność K(A,n), prawe działanie grupy

Wcześniejszy dowód sugerował, że dowolny wybór reprezentantów na `n`-komórkach przedłuża się automatycznie, skoro `π_j(L)=0` dla `j>n`. Pomijał istotne przeszkody na komórkach wymiaru `n+1`, które leżą w **niezerowej** grupie `π_n(L)`.

Poprawiono dowód: dla dwóch modeli `K,L` typu `K(A,n)`, `n≥2`, twierdzenie Hurewicza identyfikuje `H_n(K)` i `H_n(L)` z `A`; z twierdzenia o współczynnikach uniwersalnych wynika `H^n(K;A) ≅ Hom(H_n(K),A)`. Wybieramy kocykl `c` reprezentujący żądany izomorfizm, realizujemy go na `n`-komórkach, a **warunek `δc=0`** pozwala przedłużyć mapę na `n+1`-szkielet. Wyższe przeszkody znikają, ponieważ `π_j(L)=0` dla `j>n`. Oddzielnie opisano przypadek `n=1` i zastosowanie twierdzenia Whiteheada.

W homogenicznym modelu bar dyskretnej grupy jawnie rozróżniono lewe działanie przez mnożenie i prawe działanie wymagane przez definicję wiązki głównej: `(g_0,…,g_k)·h=(h^{-1}g_0,…,h^{-1}g_k)`. Orbity nie zmieniają się.

**Commity:** `17db6e279885efb8d6464c79a19010e80b4b645c`, `96d6437a79c9840546b21061fb6518fff5403cda`.

## Audyt III — jawne lokalne trywializacje modelu EG/G

Uzupełniono konstrukcję Milnora o sprawdzenie lokalnej trywialności ilorazu. Na niezmienniczym otwartym zbiorze `V_i={t_i>0}` wybieramy sekcję normalizującą `i`-tą współrzędną: `e↦e·g_i(e)^{-1}`. Jest ona niezmiennicza na orbitach, bo `g_i(eh)=g_i(e)h`, i daje trywializację `V_i≈U_i×G`. Jawnie oddzielono *swobodne działanie* od mocniejszej własności *lokalnie trywialnego rzutowania*.

**Commit:** `6b9dfd26eade5a870d392d7c66e5a9c5da1a66ff`.

## Audyt IV — klasyfikacja przez funkcje sklejające

Rozwinięto oba kierunki istniejącego twierdzenia. Zmiany trywializacji nad półkulami nie zmieniają swobodnej klasy homotopii mapy sklejającej. Homotopia `g_t` dostarcza głównej wiązki nad `S^n×I`, której końce są izomorficzne na mocy homotopijnej niezmienniczości. Ponadto jawnie uzasadniono przejście od swobodnych do punktowanych klas przez normalizację `ĝ(x)=g(x_0)^{-1}g(x)` oraz `H(x_0,t)^{-1}H(x,t)`; korzysta ona z łukowej spójności grupy.

**Commit:** `5e97842ced2139acf366699cf5d330b78fc9f258`.

## Audyt V — ścisłość zastosowania homomorfizmu Hurewicza

Dopisano krok pokazujący, dlaczego mapa z kocyklu realizuje dokładnie wybrany homomorfizm `H_n(K)→H_n(L)`: na cyklu komórkowym obliczamy sumę wartości kocyklu na orientowanych `n`-komórkach. Usunięto techniczny komentarz iteracyjny z końca tekstu, bez usuwania jakiejkolwiek treści matematycznej.

**Commit:** `138d20fc34cfcdfc865cb67f5cb12dcb2f1d124c`.

## Nowe kontrole regresyjne

Rozbudowano `application/tests/test_topology_chapters_13_14.py`:
- Kontrola, czy dowód jednoznaczności opiera się na `H^n(K;A)≅Hom(H_n(K),A)`, `δc=0` i zanikaniu `π_j(L)`, a nie na późniejszym twierdzeniu reprezentacyjnym.
- Sprawdzenie prawego działania na wszystkich permutacjach grupy `S_3`, w tym zgodności `(x·h)·k=x·(hk)` i trywialności stabilizatorów.
- Modularne rachunki jądra `A[m]` i cokernela `A/mA` dla grup cyklicznych `A=Z/k`, `2≤m,k≤11`; oczekiwana liczba elementów obu grup to `gcd(m,k)`.
- Kontrola jawnych przekrojów modelu Milnora oraz normalizacji homotopii w klasyfikacji funkcji sklejających.

**Commity testów:** `a350daf3a8efc6d817b88404dbf78b271ff6c85a`, `929cbc30ebed4a872c8d5b6e60b0ee19883ea315`.

## Audyt VI — ponowna niezależna kontrola źródła

Dla bloba `59af20ec5a267607674a6162d4f436adc9096c14` pobrano źródło z GitHuba i sprawdzono:
- 10 zachowanych etykiet, każda unikalna.
- Zagnieżdżenie wszystkich środowisk `\begin`/`\end`: bez naruszeń.
- Obecność poprawionych wzorów i warunków w dowodach.
- Brak zabronionych wyrażeń terminologicznych i roboczego komentarza końcowego.
- Rozdział nie odwołuje się cyklicznie do późniejszego twierdzenia reprezentacji przy dowodzie jednoznaczności `K(A,n)`.

**Stan CI w chwili rozpoczęcia końcowej kontroli:** wcześniejsze commity z audytu II–III przeszły kompilację TOP-01–14, testy aplikacji i audyt AT–DG–AG. Kontrole dla ostatniego pliku źródła i najnowszego zestawu testów były jeszcze w toku; ich ostateczny wynik należy dopisać osobno.

**Decyzja tymczasowa:** merytoryczny audyt VI nie znalazł dalszych uchybień wymagających zmian; TOP-13 będzie formalnie stabilny po potwierdzeniu CI na aktualnych poprawkach.
