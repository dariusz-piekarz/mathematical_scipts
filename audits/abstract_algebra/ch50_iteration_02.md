# AA-50 — audyt II: niezależne wyprowadzenia i rzeczywiste korekty regresji

**Data:** 23 listopada 2026 r. **Status:** AUDYT W TOKU — NIE STABILNY do pełnego zielonego CI i PDF.
**Rozdział:** chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex.
**Zakres:** docs/pl/zakres_aa50_kovacic_skonczone_grupy.md.

## 1. Niezależne sprawdzenie tożsamości transportowej

Wybieramy n∈{4,6,12}, S=∏(x−c), θ=(n/12)Σe_c/(x−c) i q. Przy skończonych biegunach q rzędu 1 lub 2: zarówno Sθ, jak i S²q są wielomianami. Dlatego rekurencja P_{n+1}=0, P_n=−P, P_{i−1}=−SP_i'+((n−i)S'−Sθ)P_i−(n−i)(i+1)S²qP_{i+1} pozostaje w C[x] przy wielomianowym P i jest liniowa w współczynnikach P.

Niech A_i=S^iP_i/(n−i)!, F=Σ_i A_iT^i. Dla D=∂_x+(q−T²)∂_T porównanie współczynników T^i daje po lewej A_i'+(i+1)q A_{i+1}−(i−1)A_{i−1}, a po prawej (nS'/S−θ)A_i−nA_{i−1}. Po pomnożeniu przez (n−i)!/S^{i−1} odzyskujemy dokładnie wszystkie rekurencje, w tym wymóg P_{−1}=0 dla i=0. Przy T^{n+1} obie strony są równe −nA_n, więc nie ma pominiętego warunku brzegowego.

Należy zwrócić uwagę na **czynnik (n−i)(i+1)** przy S²qP_{i+1}, nie (n−1)(i+1), oraz na mianownik (n−i)! we wzorze na F. Częste błędy w indeksowaniu mogą prowadzić do pozornych pozytywnych wyników rekurencji.

## 2. Niezależna weryfikacja twierdzenia o pierwiastkach algebraicznych

Jeśli D F=H F, rozkład F=∏f_j^{m_j} w K[T] daje Σm_j Df_j/f_j=H. Dla nierozkładalnego f_j lokalizacja przy ideale (f_j) i charakterystyka 0 wymuszają f_j|Df_j. Każdy pierwiastek w czynnika f_j w algebraicznym rozszerzeniu K jest prosty względem f_j (separowalność w char 0). Po różniczkowaniu f_j(x,w)=0 i porównaniu z Df_j(x,w)=0 uzyskujemy (w'−q+w²)f_{j,T}(x,w)=0, czyli Riccatiego w'+w²=q. Nie ma potrzeby przyjmowania, że **cały F jest bezkwadratowy**. W zadanej procedurze współczynnik wiodący przy T^n to −S^nP≠0, więc F jest wielomianem dodatniego stopnia i ma pierwiastek algebraiczny.

## 3. Przykłady potwierdzające wszystkie trzy wartości n

Potencjały Schwarza w jednej rodzinie:
q_m=−3/(16x²)−2/(9(x−1)²)+C_m/(x(x−1)), gdzie C_3=3/16, C_4=101/576, C_5=611/3600. Są to lokalne różnice wykładników (1/2,1/3,1/m). Klasyczne przyporządkowanie typów monodromii (czworo-, ośmio-, dwudziestościan) nie jest samodzielnie dowodzone.

- m=3, **n=4**: b0=−3/16, b1=b∞=−2/9. E0={3,6,9}, E1=E∞={4,5,6,7,8}. Wybory e0=3,e1=4,e∞=7 dają d=0, P=1, θ=1/x+4/(3(x−1)). Sθ=(7/3)x−1, S²q=−(2/9)x²+(3/16)x−3/16. Wykonanie całej rekurencji daje P_{−1}=0, jawne P4,...,P0 podane w rozdziale.
- m=4, **n=6**: b∞=−15/64; E0={3,4,5,6,7,8,9}, E1={4,6,8}, E∞={5,6,7}. Te same e0=3,e1=4,e∞=7: d=0, θ=3/(2x)+2/(x−1), Sθ=(7/2)x−3/2, S²q=−(15/64)x²+(115/576)x−3/16. Exact Fraction test sprawdza rekurencję n=6 i P_{−1}=0.
- m=5, **n=12**: b∞=−6/25; E0={3,4,5,6,7,8,9}, E1={4,5,6,7,8}, E∞={5,6,7}. d=0, θ=3/x+4/(x−1), Sθ=7x−3, S²q=−(6/25)x²+(739/3600)x−3/16. Exact Fraction test sprawdza rekurencję n=12 i P_{−1}=0.

Dla każdego przykładu otrzymujemy F dodatniego stopnia i równanie transportowe, więc każdy wybrany pierwiastek odpowiedniego nierozkładalnego czynnika F jest algebraicznym rozwiązaniem Riccatiego. Nie przypisujemy grupy A4/S4/A5 wyłącznie na podstawie wystąpienia pozytywnego P_{−1}: wcześniej trzeba wykluczyć przypadki pierwszy i drugi.

## 4. Testy graniczne

1. Dla q=2/x² testy dla n=4,6,12 mogą także dawać P_{−1}=0, mimo że r=2/x i r=−1/x są rozwiązaniami **wymiernymi**. To kontrola, że pozytywny wynik stopnia n sam nie klasyfikuje grupy Galois jako prymitywnej.
2. Dla q=x (Airy) ord∞ q=−1<2, trzeci przypadek odpada wstępnie. Negatywny wynik całego algorytmu wynika dopiero z analizy wszystkich przypadków i cytowanej klasyfikacji.
3. Dla ord∞ q>2 lista E∞(n) ma postać {6+12k/n: −n/2≤k≤n/2}∩Z; dla n=4 jest to {0,3,6,9,12}, dla n=6 {0,2,4,6,8,10,12}, dla n=12 {0,1,...,12}. Nie utożsamiać tej listy z samym {0,6,12}.
4. W rozkładzie E_c wolno zatrzymać wyłącznie **dokładne** liczby całkowite. Dla b0=−3/16, n=4 lista pierwotna ma wartości {3,9/2,6,15/2,9}; E0={3,6,9}.

## 5. Wykryte rzeczywiste błędy regresji (nie dowodów)

W pierwszym zintegrowanym CI #45181709411 test test_09_case_two_distinct_from_three wykonywał obliczenie stopnia q przed sprowadzeniem funkcji wymiernej do wspólnego mianownika, co powodowało błąd PolyError dla wyrażenia zawierającego 1/x. Poprawiono test: num,den=s.fraction(s.cancel(q)); stopień jest liczony dla wielomianowego licznika i mianownika. Commit d3bab28670b5a9b0d26dab9be3197de2900b099c.

Drugi pełny przebieg #45182072112 wykrył również dwie nieprawidłowe asercje o długości słownika P_i w testach niezależnych dla n=6 i n=12. Indeksy biegną od P_{n+1} do P_{−1}, a więc liczba elementów to **n+3**, czyli odpowiednio 9 i 15 (a nie 8 i 14). Zmieniono test, bez ingerencji w rekurencję; commit dcb08ced549da4e1d2a7910e8d35ba64887baf9f.

Zależności innych skryptów w ogólnym zadaniu „Validate chapter dependencies” zgłaszały też nierozwiązane importy oraz rozbieżności kopii źródeł w modułach topologii, teorii miary i geometrii różniczkowej. To problemy **poza AA-50**, których nie można arbitralnie „naprawiać” przez zmianę obcych rozdziałów. Końcowy werdykt ma rozróżnić bramkę integralności AA, dedykowane regresje, wynik całego joba i niezależne diagnostyki innych modułów.

## 6. Bramka zamknięcia

AA-50 pozostaje **NIE STABILNY**, dopóki nie będzie zielonego CI na ostatnich źródłach, poprawnych obu zestawów AA-50, kontrolnej kompilacji 50-rozdziałowej książki i oględzin wszystkich nowych stron. Trzeci audyt i decyzja o AA-51 dopiero po zakończeniu tych kontroli.
