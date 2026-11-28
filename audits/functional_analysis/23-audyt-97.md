# Rozdział 23 — audyt 97 (stabilizacja II, 2/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Przegląd
Źródło bez zmian od audytu 95 (blob 96a3c56e20f1570574613dcfbdec3dbc0d1836c5). Szczegółowo ponownie przeanalizowano kryterium hilbertowskie, rozkład VU (w tym zerową seminormę), ograniczenia i kompresje operatorów HS, identyfikacje uzupełnień podprzestrzeni i ilorazów, konstrukcję sumy l1 i ilorazu dla granicy induktywnej. W twierdzeniu o jądrze sprawdzono ustalone odcięcia, lokalną skończoność, oszacowania zbieżności w jednym etapie, przypadek rzeczywisty, faktoryzację na tensorach elementarnych i silną ciągłość przez ograniczoność w D. W dowodzie Hermite'a sprawdzono kompletność, kolejność operatorów i przesunięcia indeksów, kontrolę seminorm i konstrukcję odwrotności H bez założenia uprzedniej gęstości w S. Wcześniejsze podsekcje pozostają identyczne z przejrzanymi w audycie 96. Nie stwierdzono nowych istotnych usterek.

## Bramki
34/34 etykiet unikatowych, 50/50 odsyłaczy rozwiązanych w kontekście 17,18,22,23, 84/84 literalnych warunków regresji, poprawny stos środowisk, 18 środowisk dowodu. Wszystkie 25 plików rozdziałów 01–23 (z 15A/15B), plik główny, workflow i testy identyczne z commitem 37be92352b42e168531d01d959ca0c24d707ec88. Potwierdzono sukces wszystkich kroków biegu 45452978013, w tym wykonanie 11 metod Python. Wykorzystano oględziny PDF z audytu 96 (artefakt 14948872844, strony 186–200); nie powtarzano kompilacji i oględzin identycznej wersji. Lean nie uruchamiano.

## Kontrola pomocnicza FA23-SYM-97-01
Rzeczywiście wykonano poniższy kod lokalnie w Pythonie. 8525/8525 tożsamości na dwuwymiarowych modelach nieznormalizowanych funkcji Hermite'a P_alpha exp(-|x|²/2). Porównano bezpośrednie działanie operatorów na wielomianach z regułami przesunięcia indeksów (w tym anihilację przy indeksie zerowym), dla 25 indeksów początkowych i wszystkich słów długości 0–4 z czterech operatorów. Arytmetyka całkowita dokładna. Jest to kontrola pomocnicza, nie dowód ogólny ani dodatkowa metoda CI.

```python
from itertools import product

def add(p,q):
    r=p.copy()
    for k,v in q.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}
def scale(p,c): return {k:v*c for k,v in p.items() if v*c}
def X(p,j):
    return {tuple(v+(i==j) for i,v in enumerate(k)):c for k,c in p.items()}
def D(p,j):
    return {tuple(v-(i==j) for i,v in enumerate(k)):c*k[j]
            for k,c in p.items() if k[j]}
def apply(p,j,up):
    return add(scale(X(p,j),2),scale(D(p,j),-1)) if up else D(p,j)
P=[{(0,):1}]
for n in range(9): P.append(apply(P[-1],0,True))
def basis(a):
    return {(k[0],l[0]):v*w for k,v in P[a[0]].items()
            for l,w in P[a[1]].items()}
c=0
for a in product(range(5),repeat=2):
    for length in range(5):
        for word in product(product(range(2),[False,True]),repeat=length):
            p=basis(a); b=list(a); coef=1
            for j,up in word:
                p=apply(p,j,up)
                if up: b[j]+=1
                elif b[j]>0: coef*=2*b[j]; b[j]-=1
                else: coef=0
            expect=scale(basis(b),coef) if coef else {}
            assert p==expect,(a,word)
            c+=1
assert c==8525
```

## Decyzja
Drugi czysty przebieg 2/3. Nie zmieniano źródła ani pliku istniejących regresji. Następny audyt 98: stabilizacja III i zamknięcie rozdziału po zaliczeniu wszystkich bramek.
