# Algebra liniowa — globalny audyt matematyczny, iteracja 14 (LA21–28)

**Data:** 22 listopada 2026 r. **Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Poprzednia iteracja:** [iteracja 13](iteration_13.md), rozdziały LA14–20.  
**Decyzja:** CZYSTY w sprawdzonym zakresie LA21–28; źródła matematyczne bez zmian. Niezależny audyt całej książki pozostaje OTWARTY.

## Zakres i zamrożone wersje

| Rozdział | SHA źródła | Wiersze | Środowiska proof |
|---|---|---:|---:|
| LA21 — komutant operatora | 6527ae1a6daca48717e6a5f5e83958271abb16f5 | 899 | 9 |
| LA22 — Sylvester i Lapunow (ciągły) | dfa3d790bfed4c92c66642ea626a6213bc06ad3f | 936 | 10 |
| LA23 — Stein i stabilność Schura | bbd199baed1ee2c1a88843aad9fbfd0eac665d22 | 965 | 7 |
| LA24 — Riccati i LQR z Q>0 | 92106feafce495e11f051279733cb34e9d9bed64 | 1452 | 8 |
| LA25 — sterowalność, obserwowalność | 6b57fc1b64ef560b98e17f89322c688160376ccf | 2163 | 17 |
| LA26 — Riccati z Q≥0 | 80032eef1e0e5de817821d97de96aaf86c960e03 | 1924 | 9 |
| LA27 — gramiany i realizacje minimalne | a91dfa108d4a6ef4221b9ba24a98c87772c75d4a | 1668 | 10 |
| LA28 — wymuszenie i transmitancje | b9507aa2db7eda554446248996e7c0ae241d4e73 | 664 | 10 |
| **Razem** | | **10 671** | **80** |

Przeczytano źródła ośmiu rozdziałów, ze szczególną analizą przedstawionych dalej twierdzeń, ich hipotez, kroków dowodów i przykładów. Liczba 80 to liczba środowisk dowodu w rozdziałach, a nie deklaracja, że formalnie sprawdzono każdy wiersz każdego z tych dowodów.

## Wyniki niezależnej analizy matematycznej

### LA21 — komutant i klasyfikacja modułowa

Zweryfikowano identyfikację komutanta End_K[t](V_T), konstrukcję przestrzeni Hom między dwoma modułami cyklicznymi i wymiar deg gcd(f,g). Ze wzoru dla czynników niezmienniczych f_1|...|f_r otrzymujemy wymiar Σ_{i,j} deg gcd(f_i,f_j), a z dzielników elementarnych p^a — Σ_p(deg p)Σ_k B_{p,k}². Oba sformułowania pozostają poprawne nad ciałami, w których czynniki nierozkładalne mają stopień większy niż jeden. Oszacowanie n≤dim komutanta≤n² i kryteria równości mają uzasadnione warunki dla n≥1; przypadek n=0 odróżniono.

### LA22–23 — Sylvester, Lapunow i Stein

Dla operatora Sylvestera AX−XB wymiar jądra otrzymujemy z wymiarów Hom modułów, a istnienie i jednoznaczność dla każdego C są równoważne względnej pierwszości χ_A i χ_B. Sprawdzono znak i kolejność mnożenia w wykonawczym wzorze przez h(B)^{-1}. Dla równania A*P+PA=−Q i stabilności Hurwitza rozwiązanie jest całką zbieżną i dodatnio określoną dla Q>0; argument odwrotny bada wartości własne A przez dodatnią formę P.

W wersji dyskretnej P−A*PA=Q szereg Σ(A*)^kQA^k jest poprawny przy ρ(A)<1. Osobno sprawdzono twierdzenie o widmie operatora X↦A*XA: wartości własne to iloczyny sprzężonych i niesprzężonych wartości własnych A; jednoznaczność rozwiązania Steina nie wymaga stabilności Schura. Dokładne próbkowanie H↦exp(hH) zachowuje równoważność Hurwitza i Schura dla h>0, natomiast jawna metoda Eulera ma odmienne ograniczenie na krok.

### LA24 i LA26 — skończony i nieskończony horyzont Riccatiego

W LA24 założenia Q=Q*>0, R=R*>0 i stabilność otwartej pętli zapewniają ograniczenie niemalejącej rekurencji P_N przez koszt sterowania zerowego. Dodatnia określoność M=R+B*PB umożliwia przejście do granicy; równanie energii dla zamkniętej pętli daje stabilność i jednoznaczność rozwiązania stabilizującego. W ciągłym przypadku rozróżniono macierzowe równanie różniczkowe, jego globalne istnienie przez oszacowanie wartości kosztu i przejście do CARE.

W LA26 słabsze założenia Q≥0 oraz stabilizowalność (A,B), wykrywalność (C,A), C*C=Q, nie dają automatycznie P>0. Właśnie dlatego sprawdzono odrębne argumenty oparte na PBH, które z niezerowego wektora własnego niestabilnej pętli wyprowadzają jednocześnie Cv=0, Kv=0 i Av=λv, przeczące wykrywalności. DARE i CARE są odrębnymi równaniami; w ciągłej wersji domykanie kwadratu oraz całkowanie z poprawnym wyrazem brzegowym prowadzą do kosztu nieskończonego horyzontu. Lemat o wykrywalności i wymuszeniu L² zapewnia zanikanie stanu także wtedy, gdy Q ma niezerowe jądro. Nie znaleziono brakującej hipotezy w tych sprawdzonych fragmentach.

### LA25 i LA27 — PBH, Kalmana, gramiany, Hankel

Dla sterowalności ciągłej sprawdzono równość jądra skończonego gramianu sterowalności z jądrem sprzężenia macierzy Kalmana, uzasadnioną różniczkowaniem exp(tA*) i Cayleyem–Hamiltonem. Kryterium PBH sprawdza lewe wektory własne w sterowalności i prawe w obserwowalności. W stabilizowalności/wykrywalności testujemy tylko wartości własne spoza odpowiedniego obszaru stabilności; porównano oba rodzaje czasu.

Skończone gramiany obserwowalności mają postać O_N*O_N. W LA27 minimalna realizacja powstaje z ilorazu R/(R∩N); tożsamość H_{n,n}=O_n K_n daje rangę równą jej wymiarowi, a nie zawsze pełny wymiar początkowego stanu. Dwie minimalne realizacje o tych samych parametrach Markowa są podobne; warunek zerowego stanu początkowego jest podany jawnie. Uwaga o współrzędnych zrównoważonych: Wc Wo i macierz zrównoważona Σ² są podobne; w dowodzie wykorzystano rzeczywiście dodatnie pierwiastki oraz poprawną transformację obu gramianów.

### LA28 — wymuszenie, funkcje przejścia i ukryte tryby

Sprawdzono wzory wariacji stałych i odpowiedzi dyskretnej, człon bezpośredni D i poprawne indeksowanie h_0=D, h_k=CA^{k−1}B. Rozwinięcie funkcji przejścia G(z)=D+C(zI−A)^{-1}B przy nieskończoności odtwarza parametry Markowa. W konstrukcji skalarnej funkcji właściwej z wielomianów p i q użyta macierz sterowalnej postaci towarzyszącej realizuje q/p; minimalność jest równoważna gcd(p,q)=1, a funkcja stała ma realizację zerowymiarową. Wniosek o stabilności ukrytego stanu nie jest wywodzony z samej stabilności transmitancji.

## Nowa niezależna regresja: wynik i ograniczenia

Utworzono i wykonano skrypt **/mnt/data/la_global14_tests.py** w Pythonie, z generatorem o stałym seedzie 20261122; SHA256: **d53176dae2c6d624e5215cc489018e07998adf575a0ca077916ee8e2637b6e15**. Własne testy rang nad F2, F3 i F5 używają modularnej eliminacji Gaussa, a SciPy/SymPy/Numpy służą do niezależnych testów numerycznych i wielomianów. Pierwsza wersja błędnie porównywała kolejność wartości własnych macierzy podobnych; poprawiono **test**, sortując obie listy, bez zmiany źródeł książki.

| Grupa sprawdzeń | PASS |
|---|---:|
| Jądro Sylvestera nad Fp dla bloków liniowych oraz kryterium rozłączności | 1560 |
| Komutant nad Fp dla bloków liniowych | 780 |
| Sylvester nad R: rozwiązanie i rozłączność widm | 700 |
| Ciągłe równanie Lapunowa, dodatniość rozwiązania | 560 |
| Dyskretne równanie Steina, dodatniość rozwiązania | 560 |
| Rezonans Steina — macierz operatora | 680 |
| DARE z Q≥0: równanie, stabilność, P≥0 | 870 |
| CARE z Q≥0: równanie, stabilność, P≥0 | 870 |
| PBH stabilizowalność i wykrywalność w obu czasach | 1800 |
| Faktoryzacja Hankela, minimalność, równoważenie gramianów | 1892 |
| Postać towarzysząca: sterowalność, charakterystyczny, transmitancja | 2400 |
| Jawny przykład transformacji w LA28 | 1 |
| Nierozkładalne kwadraty nad F2/F3/F5: Sylvester i komutant | 81 |
| **Łącznie** | **12 754 PASS, 0 FAIL** |

To testy skończenie wielu przykładów; nie są formalnymi dowodami wszystkich twierdzeń. W części numerycznej korzystano z tolerancji, w arytmetyce modularnej i przy wielomianach z rachunków dokładnych.

## Integracja LaTeX oraz CI

- Źródła: osiem plików o niezmienionych SHA jak w tabeli; **254 etykiety**, **243 odsyłacze**, brak zduplikowanych etykiet w badanym zestawie, brak niedomkniętych środowisk, brak nierozstrzygniętych celów odsyłaczy (sprawdzenie na inwentarzu wszystkich 32 rozdziałów z iteracji 10), brak trafień sprawdzanych zakazanych słów.
- [GitHub Actions — run 45047971276](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047971276): **completed/success** na commicie 3078c9ca833f69d908bddbb616086646898e64e6. Odczytano osobno z tego commitu wszystkie osiem plików LA21–28; ich SHA **dokładnie odpowiadają** źródłom bieżącej gałęzi. W tej iteracji nie uruchamiano nowego procesu kompilacji ani nie pobierano nowego PDF, więc CI jest sukcesem wcześniej zweryfikowanej, lecz identycznej wersji rozdziałów.
- Zakończona sekwencja stabilizacyjna LA12–32 pozostaje zamknięta; brak konkretnej nowej usterki wymagającej jej wznowienia.

## Decyzja i kolejny etap

**ITERACJA 14: CZYSTA** w analizowanym zakresie ośmiu rozdziałów i 12 754 przypadków obliczeniowych. Nie dokonano zmian w plikach rozdziałów.

Globalna pełna, niezależna kontrola każdego kroku wszystkich dowodów nadal OTWARTA. Najbliższy sensowny etap to spójność końcowa LA29–32 z LA01–28 oraz odrębny rejestr nieprzeczytanych jeszcze w całości dowodów, zamiast utożsamiania liczby środowisk proof z liczbą w pełni zweryfikowanych dowodów.
