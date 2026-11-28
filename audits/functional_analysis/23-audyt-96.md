# Rozdział 23 — audyt 96 (stabilizacja I, 1/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Przegląd
Źródło pozostaje identyczne z wersją z audytu 95 (blob 96a3c56e20f1570574613dcfbdec3dbc0d1836c5). Ponownie przeanalizowano sześć podsekcji: własność Montela i beczkowość, normę nuklearną i własność ideałową, przejścia kanoniczne i kryterium dla rodziny seminorm, ważone c0 i oszacowania szeregów Fouriera, hilbertowskie kryterium i trwałość nuklearności, konstrukcję jądra Schwartza (w tym ustalone odcięcia i brak innych kopii okresowych, przypadek rzeczywisty, ciągłość na etapach i gęstość tensorów) oraz dowód izomorfizmu Hermite'a (ortonormalność, zupełność, oszacowania norm i odwrotność). Rozdział zawiera 18 środowisk dowodu. Nie stwierdzono nowych istotnych usterek wymagających zmiany źródła.

## Bramki
34/34 etykiet unikatowych, 50/50 rozwiązanych odsyłaczy w kontekście 17,18,22,23, 84/84 literalnych fragmentów regresyjnych, poprawny stos środowisk. Wszystkie 25 plików rozdziałów 01–23 (z 15A/15B), plik główny, workflow i testy identyczne z commitem 37be92352b42e168531d01d959ca0c24d707ec88. Bieg 45452978013 zakończył się sukcesem we wszystkich krokach, w tym wykonaniu 11 metod Python, kompilacji i diagnostyce PDF. Pobrano artefakt 14948872844, PDF ma 200 stron. Wyrenderowano w PyMuPDF strony 186–200 przy skali 1.5 i obejrzano cztery plansze (15 stron). Nie zauważono widocznych kolizji lub obcięć. W logu nie ma dopasowań Overfull, undefined, Missing character ani LaTeX Warning. Nie uruchamiano Lean.

## Kontrola pomocnicza FA23-SYM-96-01
Rzeczywiście uruchomiono poniższy kod lokalnie w Pythonie z Fraction. Sprawdzono 5625 tożsamości niezmienniczości kwadratu normy Hilberta–Schmidta przy zmianie baz oraz 22500 oszacowań jednowymiarowych kompresji, razem 28125/28125. Modele macierzy 2x2 o wpisach całkowitych od -2 do 2 i trzech wymiernych baz ortonormalnych; są to testy pomocnicze, nie dowód ogólny ani dodatkowa metoda CI.

```python
from fractions import Fraction as F
from itertools import product

R=[((F(1),F(0)),(F(0),F(1))),
   ((F(3,5),F(-4,5)),(F(4,5),F(3,5))),
   ((F(5,13),F(12,13)),(F(-12,13),F(5,13)))]
def tr(A): return tuple(zip(*A))
def mm(A,B):
    return tuple(tuple(sum(a*b for a,b in zip(row,col))
                       for col in zip(*B)) for row in A)
def hs(A): return sum(x*x for row in A for x in row)
count=0
for entries,U,V in product(product(range(-2,3),repeat=4),R,R):
    A=(entries[:2],entries[2:])
    C=mm(mm(tr(U),A),V)
    assert hs(C)==hs(A)
    count+=1
    for i,j in product(range(2),repeat=2):
        assert C[i][j]**2<=hs(A)
        count+=1
assert count==28125
```

## Decyzja
Pierwszy czysty przebieg stabilizacyjny 1/3. Bez zmian źródła i istniejącego pliku testów. Następny audyt 97: stabilizacja II, bez rozszerzania zakresu.
