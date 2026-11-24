# Rozdział 21 — audyt 84 (stabilizacja III, 3/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Końcowy przegląd matematyczny
Źródło niezmienione od audytu 81 (blob b1f0eb53c44e2cc014aadd97b2ed4fcfd4b99654). Ponownie sprawdzono pięć podsekcji i dziewięć dowodów: niezależność od odcięcia, identyfikację liniową E' z dualną przestrzenią funkcji gładkich, wspólny zwarty nośnik aproksymacji iloczynowej i oszacowania ciągłości na powiększonym etapie, lokalność oraz znak różnicy Minkowskiego w operatorze testowym, domkniętość sumy nośników, wszystkie trzy ustawienia dwóch zwartych nośników w dowodzie łączności, translacje i przenoszenie pochodnych, zwartość nośnika funkcji G w dowodzie wygładzania, odbicie jądra i jednolitość oszacowania po ograniczonych rodzinach funkcji testowych, brak zbieżności L1_loc do funkcji przy regularyzacji delty oraz sprzeczność przy globalnym rozszerzeniu splotu. Nie stwierdzono nowych istotnych usterek. Nie zmieniano źródła ani zakresu rozdziału.

## Bramki stabilizacji
19/19 unikatowych etykiet, 24/24 odsyłaczy rozwiązanych w kontekście 17–21, 44/44 warunków tekstowych z trwałych regresji, poprawny stos środowisk. Porównanie z commitem be4c17c7efd875d1e1a728c5e2abd9268db8c21e: 23/23 plików rozdziałów 01–21 (w tym 15A/15B), plik główny, workflow i plik sześciu testów identyczne. Wszystkie kroki biegu 45425472472 zakończone sukcesem. W audycie 82 obejrzano aktualny PDF, strony 171–178 (artefakt 14936791805). Nie powtarzano kompilacji ani oględzin tego samego artefaktu w audycie 84. Nie uruchamiano Lean.

## Kontrola pomocnicza FA21-SYM-84-01
Rzeczywiście uruchomiono poniższy kod lokalnie w Pythonie; 1350/1350 dokładnych tożsamości różniczkowania średniej przesunięć wielomianów w dwóch wymiarach, dla dwóch niesymetrycznych rozkładów o gęstościach 2u oraz 2(1-v) na [0,1], trzech punktów, trzech skal i sześciu wielowskaźników. Momenty liczone dokładnie przez Fraction. Model całkowy nie jest gładką funkcją testową ani formalizacją ogólnego twierdzenia. Kod jest utrwalonym pomocniczym sprawdzeniem, a nie nową metodą CI.

```python
from fractions import Fraction as F
from itertools import product
from math import comb

def falling(n,k):
    if k>n: return 0
    v=1
    for i in range(k): v*=n-i
    return v

def moment(k,l):
    return F(2,k+2)*F(2,(l+1)*(l+2))

def average(i,j,x,y,e):
    return sum(comb(i,k)*comb(j,l)*x**(i-k)*y**(j-l)*e**(k+l)*moment(k,l)
               for k in range(i+1) for l in range(j+1))
count=0
for i,j in product(range(5),repeat=2):
    for x,y in [(-2,1),(0,0),(2,-1)]:
        for e in [F(1,2),F(1,4),F(1,8)]:
            for a,b in [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)]:
                lhs=sum(comb(i,k)*comb(j,l)*falling(i-k,a)*falling(j-l,b)
                        *x**(i-k-a)*y**(j-l-b)*e**(k+l)*moment(k,l)
                        for k in range(max(0,i-a+1)) for l in range(max(0,j-b+1)))
                rhs=falling(i,a)*falling(j,b)*average(i-a,j-b,x,y,e) if a<=i and b<=j else 0
                assert lhs==rhs
                count+=1
assert count==1350
```

## Decyzja
Trzy kolejne czyste przebiegi 82–84: 3/3. Rozdział 21 zamknięty na podstawie niezmienionego źródła, zaliczonego CI i oględzin PDF. Następny audyt 85: pierwszy blok istniejącego rozdziału 22 — Dystrybucje temperowane i transformacja Fouriera. Najpierw sprawdzić definicje, konwencję normalizacji transformacji oraz zgodność z przestrzenią Schwartza z rozdziału 17.
