# Globalny audyt algebry liniowej — iteracja 05/09

**Data:** 22 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Wejściowy HEAD:** `223afa76c00e9755d98d3873592bd849bec5c8aa`.  
**Zakres:** rozdziały 17–20.  
**Podstawa:** odczytane `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/linear_algebra.tex`, `catalog/books.json`, raporty 01–04 i status; wszystkie cztery pełne źródła (19 637, 21 076, 19 202, 19 992 znaków). Weryfikacja porównawcza pełnego DG-01 nie była wykonywana w tej iteracji.

## Audyt matematyczny

Sprawdzono strukturę **27 dowodów** (7+6+7+7) i szczegółowo wybrane kluczowe kroki, bez deklarowania pełnej formalnej weryfikacji każdego zdania.

- **17:** nilpotentność i stabilizacja jąder; konstrukcja bazy Jordana przez indukcję po wymiarze obrazu; niezależność dołączanych wektorów modulo \(\operatorname{im}N\); liczba bloków długości \(k\) z drugich różnic wymiarów jąder; rozdzielenie przypadków \(V=0\) i \(V\ne0\). W przykładzie \(d=(0,3,5,7,7)\) otrzymano bloki długości \(3,3,1\). Nie znaleziono błędu wymagającego zmiany.
- **18:** konstrukcja rzutów przez tożsamość Bézouta i ich niezależność od wielomianu; jednoznaczność części diagonalizowalnej i nilpotentnej; współczynniki Taylora bez dzielenia przez silnie w dodatniej charakterystyce; teleskopowy wzór na odwrotność; szereg wykładniczy i rozwiązanie układu ODE. Sprawdzono przypadek zerowego wymiaru. Bez koniecznych korekt.
- **19:** prezentacja modułu \(V_T\cong K[t]^n/(tI-A)K[t]^n\), algorytm Smitha, niezmienniki minorowe \(\Delta_k\), postać Frobeniusa, przypadki \(n=0\) i \(n\ge1\). **Zidentyfikowano nieuzasadniony krok** w dowodzie algorytmu Smitha: po dodaniu wiersza do pierwszego wiersza autor przechodził do mniejszego stopnia elementu \((1,1)\) bez wskazania poprawnych operacji na kolumnach. Dopisano dokładne dzielenie \(b=qd+r\), operację \(C_j\leftarrow C_j-qC_1\), zamianę \(C_1\leftrightarrow C_j\), oraz \(0\le\deg r<\deg d\). Dzięki temu argument terminacji jest jawny i poprawny.
- **20:** chińskie twierdzenie o resztach dla parami względnie pierwszych wielomianów; składanie i odzyskiwanie czynników niezmienniczych; dokładny wzór \(D_{p,k}=(\deg p)\sum_j\min(k,a_{p,j})\); weryfikacja przykładów nad \(\mathbb R\), \(\mathbb Q\) i \(\mathbb F_2\). Bez koniecznych korekt.

## Audyt redakcyjny i techniczny

Zachowano wszystkie stabilne etykiety i odsyłacze; poprawka dotyczy tylko jednego fragmentu dowodu. Sprawdzono konwencje \(n=0\), występowanie uzasadnień przy twierdzeniach, wzory na bloki towarzyszące oraz zależności od rozdziałów 16–19. Nie dodano nowych twierdzeń ani rozdziałów. Nie stwierdzono konieczności korekt rysunków w czterech źródłach.

**Kontrole otwarte:** pełny CI nowego commitu, osobny PDF i wizualna inspekcja składu. Do czasu ich rzeczywistego zakończenia nie przyznawać statusu czystego audytu.

## Następna iteracja

06/09 — rozdziały 21–24, z równoległym monitorowaniem otwartych kontroli CI/PDF dla poprzednich bloków.
