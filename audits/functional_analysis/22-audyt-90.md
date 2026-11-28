# Rozdział 22 — audyt 90 (stabilizacja III, 3/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Przegląd końcowy
Źródło niezmienione od audytu 87 (blob acfd4698d6a8148985cea876bcf56259275abcd6). Ponownie sprawdzono cztery podsekcje i dziewięć dowodów: kryterium wzrostu seminormowego, przedłużenie dystrybucji o zwartym nośniku, biliniowe parowanie i włożenia, oszacowania mnożników, zwartość domknięć zbiorów ograniczonych, równociągłość i rozróżnienie topologii słabej-* i silnej, znaki transpozycji Fouriera i jej odwrotność, konstrukcję przedłużenia Plancherela, ciągłość przesunięć, całkowalne majoranty i sumy Riemanna w S, stałą splotową i oszacowanie wzrostu wszystkich pochodnych transformaty dystrybucji o zwartym nośniku. Nie stwierdzono nowych istotnych usterek wymagających zmian źródła.

## Bramki
16/16 etykiet unikatowych, 26/26 rozwiązanych odsyłaczy w kontekście 17–22, 49/49 fragmentów regresyjnych, poprawny stos środowisk. Wszystkie 24 pliki rozdziałów 01–22 (z 15A/15B), plik główny, workflow i plik regresji identyczne z wersją 038620b9dcf184105f0d2b60f0f987f9f82d8b87. Potwierdzono sukces wszystkich kroków biegu 45430736181, w tym sześciu metod regresyjnych. W audycie 88 obejrzano aktualny PDF, strony 178–185 (artefakt 14937134732); nie powtarzano kompilacji ani oględzin identycznego źródła. Lean nie uruchamiano.

## Kontrola pomocnicza FA22-SYM-90-01
Poniższy kod rzeczywiście wykonano lokalnie w Pythonie: 432 kontrole stopnia wielomianu oraz 1296 tożsamości pochodnych transformaty przesuniętej delty w dwóch wymiarach, razem 1728/1728. Wykorzystano małe współczynniki całkowite zespolone dokładnie reprezentowalne w Python complex. Po usunięciu wspólnej fazy i normalizacji porównano iteracyjne różniczkowanie transformaty z niezależnym rozwinięciem Leibniza w działaniu dystrybucji na wykładniczą funkcję gładką. Nie stanowi to dowodu ogólnego ani dodatkowej metody CI.

```python
from itertools import product
from math import comb, factorial

def step(p,j,a):
    q={}
    for ij,c in p.items():
        q[ij]=q.get(ij,0)-1j*a[j]*c
        if ij[j]:
            k=list(ij); k[j]-=1; k=tuple(k)
            q[k]=q.get(k,0)+ij[j]*c
    return {k:v for k,v in q.items() if v}
def falling(n,k): return factorial(n)//factorial(n-k)
def val(p,z): return sum(c*z[0]**i*z[1]**j for (i,j),c in p.items())
count=0
for alpha,beta,a in product(product(range(3),repeat=2),
                            product(range(4),repeat=2),
                            [(-2,1),(0,0),(1,3)]):
    p={alpha:1j**sum(alpha)}
    for j in range(2):
        for _ in range(beta[j]): p=step(p,j,a)
    assert all(sum(k)<=sum(alpha) for k in p)
    count+=1
    for z in [(-1,2),(0,0),(3,-2)]:
        expected=0j
        for g in product(*(range(min(alpha[j],beta[j])+1) for j in range(2))):
            term=(-1)**sum(alpha)*(-1j)**(sum(beta)+sum(alpha)-sum(g))
            for j in range(2):
                term*=comb(alpha[j],g[j])*falling(beta[j],g[j])*a[j]**(beta[j]-g[j])*z[j]**(alpha[j]-g[j])
            expected+=term
        assert val(p,z)==expected
        count+=1
assert count==1728
```

## Decyzja
Trzy kolejne czyste przebiegi 88–90: 3/3. Rozdział 22 zamknięty. Następny audyt 91: pierwszy blok istniejącego rozdziału 23 (23-przestrzenie-montela-i-nuklearne-twierdzenie-o-jadrze-schwartza.tex), w szczególności definicje, zależności pojęciowe i założenia twierdzeń. Bez zmiany źródeł rozdziału 22 i istniejących regresji.
