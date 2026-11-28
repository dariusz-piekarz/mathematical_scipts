# Rozdział 20 — audyt 77 (stabilizacja III, 3/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Końcowy przegląd matematyczny
Źródło niezmienione od audytu 74: blob ee15ae2188855df577f6008cd6acdf328e3178d5. Ponownie skontrolowano pięć podsekcji i jedenaście dowodów: ciągłość różniczkowania na etapach D_K i w obu topologiach dystrybucji, znaki i nośniki pochodnych, zgodność z klasycznym różniczkowaniem, całkowanie przez części przy skoku i przejście do granicy, mnożenie i indukcję Leibniza, zależność regularizacji H delta od wyboru jądra, biliniową konwencję transpozycji, normalizację funkcji testowej i oszacowanie ciągłości operatora pierwotnej, czynnik całkujący, przemienność rzutów oraz sklejanie lokalnych stałych. W ostatniej uwadze zweryfikowano zerową całkę włóknową, zwarty nośnik pierwotnej i jednoznaczność reprezentacji. Nie stwierdzono usterek wymagających zmian. Nie rozszerzano rozdziału.

## Bramki stabilizacji
24/24 unikatowych etykiet, 33/33 rozwiązanych odsyłaczy w kontekście 17–20, 45/45 warunków tekstowych istniejących regresji, prawidłowo zagnieżdżone środowiska. Porównano aktualną gałąź z commitem a8c217b2432f17e7ead121c5e7e4e91d231d413b: wszystkie 22 pliki rozdziałów 01–20 (łącznie z 15A/15B) oraz plik siedmiu testów regresyjnych (blob eabfea60ec2e10dad17fbea5a3557fd2c5824c4a) są identyczne. Wszystkie kroki biegu 45411102942 zakończone sukcesem. W audycie 76 obejrzano dziesięć stron aktualnego PDF (artefakt 14927561844). W audycie 77 nie uruchamiano ponownie kompilacji ani nie powtarzano oględzin tego samego artefaktu; wykorzystano potwierdzone wcześniejsze wyniki dla niezmienionych źródeł i testów. Nie wykonywano Lean.

## Dodatkowa kontrola dokładna FA20-SYM-77-01
Lokalnie uruchomiono SymPy: 162/162 dokładnych sprawdzeń tożsamości mnożenia pochodnej delty rzędu n przez g, dla n=0,...,5, trzech punktów, trzech wielomianowych mnożników (w tym zespolonego) i trzech wielomianowych modeli funkcji testowych. Sprawdzono znaki i współczynniki dwumianowe. Modele wielomianowe badają dżety w punkcie (można je lokalnie pomnożyć przez funkcję odcięcia równą 1 przy a); nie są formalizacją ogólnego twierdzenia. Reprodukowalny kod wykonanej kontroli:

```python
import sympy as s
from math import comb
x = s.symbols("x", real=True)
count = 0
for a in [-2, 0, 3]:
    for g in [1+x, x**3-2*x+1, 1+s.I*x**2+x**4]:
        for phi in [1+x+x**2, x**5-2*x**3+1, (1-x**2)**4]:
            for n in range(6):
                lhs = (-1)**n*s.diff(g*phi,x,n).subs(x,a)
                rhs = sum((-1)**k*comb(n,k)*s.diff(g,x,k).subs(x,a)
                          *(-1)**(n-k)*s.diff(phi,x,n-k).subs(x,a)
                          for k in range(n+1))
                assert s.expand(lhs-rhs) == 0
                count += 1
assert count == 162
```

Kod jest utrwaloną kontrolą pomocniczą w raporcie, nie nową metodą uruchamianą w CI. Istniejących testów nie modyfikowano.

## Decyzja
Trzy kolejne czyste przebiegi 75–77: 3/3, rozdział 20 zamknięty. Następny audyt 78: pierwszy blok istniejącego rozdziału 21 — Splot dystrybucji i regularyzacja; najpierw kontrola założeń definicji, warunków nośnikowych i dowodów, bez wyprzedzającej deklaracji stabilizacji.
