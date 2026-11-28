# Rozdział 21 — audyt 83 (stabilizacja II, 2/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Ponowny przegląd
Źródło niezmienione od audytu 81: blob b1f0eb53c44e2cc014aadd97b2ed4fcfd4b99654. Przejrzano pięć podsekcji, dziewięć dowodów, ze szczególnym uwzględnieniem zależności oszacowań od zwartych zbiorów i rzędów pochodnych, poprawności usuwania odcięć, odwrócenia kolejności działań i składania operatorów testowych, istnienia splotów przy permutowaniu trzech czynników, znaku translacji i przeniesienia pochodnych, odbicia jądra, jednostajności oszacowań po zbiorach ograniczonych oraz przykładu niemożliwości rozszerzenia splotu. Nie znaleziono nowych istotnych usterek. Bez rozszerzania materiału.

## Bramki
19/19 unikatowych etykiet, 24/24 odsyłaczy rozwiązanych w kontekście 17–21, 44/44 warunków tekstowych, poprawny stos środowisk. Porównano z commitem be4c17c7efd875d1e1a728c5e2abd9268db8c21e: wszystkie 23 pliki rozdziałów 01–21 (z 15A/15B), plik główny (a6059c73f9bc776397f73ca20c4b02c763760296), workflow (8caad39e43f6398d8281cf428ae5ba83f5468838) i plik testów (a63b5f0ff9e6e3ec1a9b5fc70f468c5826bcb17d) identyczne. Wszystkie kroki biegu 45425472472 zakończone sukcesem, w tym sześć metod regresyjnych. Wykorzystano oględziny PDF z audytu 82 (artefakt 14936791805, strony 171–178); nie powtarzano kompilacji ani oględzin identycznego źródła w audycie 83. Nie uruchamiano Lean.

## Kontrola pomocnicza FA21-SYM-83-01
W Pythonie z Fraction rzeczywiście wykonano 135/135 dokładnych tożsamości całkowania przez części: całka rho(z) (-1)^n p^(n)(a+z) po [-1,1] równa całce rho^(n)(z) p(a+z), dla trzech punktów a, trzech wielomianów p, trzech modeli rho i rzędów n=0,...,4. Wielomiany rho mają czynnik (1-z^2)^4, więc wyrazy brzegowe do rzędu 3 znikają. Są to skończone modele przenoszenia pochodnej w formule splotu, nie funkcje testowe klasy C-infinity po przedłużeniu zerem i nie formalizacja ogólnego twierdzenia. Reprodukowalny kod zachowano poniżej; nie stanowi dodatkowej metody CI.

```python
from fractions import Fraction as F
from math import comb

def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return out

def deriv(p,n):
    for _ in range(n):
        p=[i*p[i] for i in range(1,len(p))] or [F(0)]
    return p

def shift(p,a):
    return [sum(p[i]*comb(i,j)*a**(i-j)
                for i in range(j,len(p))) for j in range(len(p))]

def integ(p):
    return sum(F(2)*v/(i+1) for i,v in enumerate(p) if i%2==0)

base=[F(1),F(0),F(-1)]
w=[F(1)]
for _ in range(4):
    w=mul(w,base)
count=0
for a in (-2,0,3):
    for p in ([F(1)],[F(1),F(-2),F(3)],
              [F(0),F(1),F(0),F(-3),F(2),F(1)]):
        for q in ([F(1)],[F(2),F(1)],[F(1),F(-2),F(3)]):
            rho=mul(w,q)
            for n in range(5):
                lhs=(-1)**n*integ(mul(rho,shift(deriv(p,n),a)))
                rhs=integ(mul(deriv(rho,n),shift(p,a)))
                assert lhs==rhs
                count+=1
assert count==135
```

## Decyzja
Drugi czysty przebieg 2/3. Nie zmieniano źródła ani istniejących metod regresyjnych. Następny audyt 84: trzecia stabilizacja i zamknięcie rozdziału wyłącznie w razie zaliczenia wszystkich bramek.
