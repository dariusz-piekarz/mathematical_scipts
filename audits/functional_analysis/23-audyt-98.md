# Rozdział 23 — audyt 98 (stabilizacja III, 3/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Przegląd końcowy
Źródło niezmienione od audytu 95 (blob 96a3c56e20f1570574613dcfbdec3dbc0d1836c5). Ponownie skontrolowano pierwsze trzy podsekcje: definicję Montela i beczkowość, przejście od zbieżności punktowej ciągów do silnej, kryterium zwartości operatora nuklearnego, kontrprzykład harmonicznej przekątnej, normę nuklearną, zgodność przejść seminormowych, identyfikację ważonych c0 i oszacowania Fouriera dla C-infinity. Sprawdzono lokalizację szeregu tensorowego, rozróżnienie ciągłości osobnej i łącznej oraz biliniową (bez sprzężenia w parowaniu) konwencję jądra. Dowody kryterium hilbertowskiego, trwałości i izomorfizmu Hermite'a są identyczne z wersją ponownie przeanalizowaną w audycie 97. W trzech przebiegach nie stwierdzono nowych istotnych usterek wymagających zmian źródła.

## Bramki
34/34 unikatowych etykiet, 50/50 rozwiązanych odsyłaczy w kontekście 17,18,22,23, 84/84 fragmentów trwałych regresji, poprawny stos środowisk, 18 środowisk dowodu. Wszystkie 25 plików rozdziałów 01–23 (z 15A/15B), plik główny, workflow i plik testowy identyczne z wersją 37be92352b42e168531d01d959ca0c24d707ec88. Potwierdzono sukces wszystkich kroków biegu 45452978013, w tym wykonanie 11 metod Python. Wykorzystano oględziny stron 186–200 PDF z audytu 96 (artefakt 14948872844). Nie powtarzano kompilacji ani oględzin niezmienionej wersji. Lean nie uruchamiano.

## Kontrola pomocnicza FA23-SYM-98-01
Rzeczywiście wykonano lokalnie poniższy kod Python: 300 rekonstrukcji czteropunktowego dyskretnego szeregu Fouriera oraz 300 tożsamości biliniowego parowania po rozwinięciu drugiego argumentu, z czterema początkami układu współrzędnych i trzema jądrami (jedno zespolone). Łącznie 600/600. Użyte małe liczby całkowite zespolone i dyadyczne są dokładnie reprezentowalne w Python complex. Model skończony kontroluje konwencję sprzężenia jedynie we współczynnikach Fouriera, nie w parowaniu. Nie stanowi dowodu twierdzenia o jądrze ani dodatkowej metody CI.

```python
from itertools import product
N=4
def e(n,j,c): return 1j**((n*(j-c))%4)
def b(f,g,K):
    return sum(f[i]*K[i][j]*g[j] for i in range(N) for j in range(N))
vecs=[(1,0,0,0),(0,1,0,0),(1,-2,3,-1),(1j,2,-1j,3),(0,0,1,-1j)]
Ks=[tuple(tuple(int(i==j) for j in range(N)) for i in range(N)),
    tuple(tuple((i-j)+1j*(i+j) for j in range(N)) for i in range(N)),
    tuple(tuple((i+1)*(j-2) for j in range(N)) for i in range(N))]
count=0
for f,g,K,c in product(vecs,vecs,Ks,range(N)):
    coeff=[sum(g[j]*e(n,j,c).conjugate() for j in range(N))/N for n in range(N)]
    rec=tuple(sum(coeff[n]*e(n,j,c) for n in range(N)) for j in range(N))
    assert rec==g
    assert sum(b(tuple(x*coeff[n] for x in f),
                 tuple(e(n,j,c) for j in range(N)),K)
               for n in range(N))==b(f,g,K)
    count+=2
assert count==600
```

## Decyzja
Trzy kolejne czyste przebiegi 96–98: 3/3. Rozdział 23 zamknięty według przyjętych bramek audytu. Następny audyt 99: pierwszy blok istniejącego rozdziału 24 (24-topologiczne-produkty-tensorowe-przestrzeni-lokalnie-wypuklych.tex), z naciskiem na definicje topologii tensorowych i ich własności uniwersalne. Zachować źródła i regresje rozdziału 23.
