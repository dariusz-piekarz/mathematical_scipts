# Rozdział 22 — audyt 89 (stabilizacja II, 2/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Ponowny przegląd
Źródło bez zmian od audytu 87 (blob acfd4698d6a8148985cea876bcf56259275abcd6). Ponownie sprawdzono cztery podsekcje i dziewięć dowodów: kryterium ciągłości i przedłużenie z D do S, injektywność i ciągłość włożeń bez sprzężenia w parowaniu, oszacowania wzrostu i mnożników, argument diagonalny w dowodzie względnej zwartości i zastosowanie Banacha–Steinhausa, rozróżnienie topologii przez oddzielenie w ilorazie, kolejność składania przy transpozycji i znak pochodnej, konstrukcję unitarnego przedłużenia na L2 i zgodność z dystrybucjami, oszacowania ilorazów różnicowych, ogonów całek i zamianę całkowania z działaniem funkcjonału, współczynnik splotowy i niezależność wykładnika wzrostu transformaty dystrybucji o zwartym nośniku od rzędu różniczkowania względem parametru. Nie stwierdzono nowych istotnych usterek. Bez zmian źródła i zakresu.

## Bramki
16/16 etykiet unikatowych, 26/26 odsyłaczy rozwiązanych w kontekście 17–22, 49/49 fragmentów trwałych regresji, poprawny stos środowisk. Wszystkie 24 pliki rozdziałów 01–22 (z 15A/15B), plik główny, workflow i plik testów identyczne z commitem 038620b9dcf184105f0d2b60f0f987f9f82d8b87. Potwierdzono sukces wszystkich kroków biegu 45430736181, w tym sześciu metod regresyjnych. Wykorzystano oględziny PDF z audytu 88 (artefakt 14937134732, strony 178–185). Nie powtarzano kompilacji ani oględzin identycznego źródła. Lean nie uruchamiano.

## Kontrola pomocnicza FA22-SYM-89-01
Rzeczywiście uruchomiono poniższy kod lokalnie w Pythonie. 250/250 tożsamości dla F(D^a X^b f)=(iX)^a(iD)^b F(f) oraz F(X^b D^a f)=(iD)^b(iX)^a F(f), gdzie X jest mnożeniem przez zmienną, D różniczkowaniem, a f wielomianem pomnożonym przez exp(-x^2/2). Pięć modeli, rzędy a,b od 0 do 4. Współczynniki są małymi liczbami całkowitymi zespolonymi reprezentowalnymi w Python complex. Kontrola zachowania kolejności operatorów, nie dowód ogólny ani dodatkowa metoda CI.

```python
from itertools import product

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(p,q):
    return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
                 for i in range(max(len(p),len(q)))])
def scale(p,c): return trim([c*v for v in p])
def X(p): return trim([0]+p)
def D(p): return add([i*p[i] for i in range(1,len(p))] or [0],scale(X(p),-1))
def iterate(op,p,n):
    for _ in range(n): p=op(p)
    return p
basis=[[1]]
for _ in range(12): basis.append(scale(D(basis[-1]),1j))
def Fourier(p):
    out=[0]
    for n,c in enumerate(p): out=add(out,scale(basis[n],c))
    return out
models=[[1],[0,1],[1,-2,3],[1,2j,0,-1],[2-1j,0,3,0,1]]
count=0
for p,a,b in product(models,range(5),range(5)):
    fp=Fourier(p)
    lhs=Fourier(iterate(D,iterate(X,p,b),a))
    rhs=scale(iterate(X,iterate(D,fp,b),a),1j**(a+b))
    assert lhs==rhs
    lhs=Fourier(iterate(X,iterate(D,p,a),b))
    rhs=scale(iterate(D,iterate(X,fp,a),b),1j**(a+b))
    assert lhs==rhs
    count+=2
assert count==250
```

## Decyzja
Drugi czysty przebieg 2/3. Nie zmieniano źródła ani pliku istniejących regresji. Następny audyt 90 — stabilizacja III i zamknięcie rozdziału tylko po zaliczeniu wszystkich bramek.
