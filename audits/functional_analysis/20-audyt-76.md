# Rozdział 20 — audyt 76 (stabilizacja II, 2/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Domknięcie audytu 75
Bieg 45411102942 dla commitu a8c217b2432f17e7ead121c5e7e4e91d231d413b zakończony sukcesem. Artefakt 14927561844 pobrano i rozpakowano. PDF ma 171 stron; wyrenderowano i obejrzano strony 162–171, w tym wykres Heaviside'a na s.164 i poprawioną uwagę na s.171. Brak widocznych kolizji i obcięć. W logu brak dopasowań Overfull, undefined, Missing character, LaTeX Warning. Porównanie rastrów wszystkich 171 stron z artefaktem 14928006118 wykazało zmianę wyłącznie strony 171. Tym samym audyt 75 uzyskał pełne zaliczenie 1/3.

## Drugi czysty przegląd
Blob rozdziału ee15ae2188855df577f6008cd6acdf328e3178d5 pozostaje niezmieniony. Pięć podsekcji, jedenaście środowisk dowodu, 24/24 unikatowych etykiet, poprawnie zagnieżdżone środowiska. Przejrzano ponownie znaki pochodnych, regułę Leibniza, formalną transpozycję bez sprzężenia, ciągłość silną, argumenty o nośniku i konstrukcję pierwotnej. Zbadano szczególnie przemienność rzutów całkowych, tożsamość ich złożenia oraz argument lokalno-globalny i jednoznaczność reprezentacji na I x V. Nie znaleziono nowych istotnych usterek. Siedem istniejących metod regresyjnych zaliczono w CI dokładnie dla tego źródła; nie zmieniano testów ani rozdziału. Nie uruchamiano Lean.

## Dodatkowe obliczenia symboliczne (wykonane lokalnie)
36 dokładnych tożsamości zweryfikowano w SymPy: 6 dla transpozycji biliniowej zespolonego operatora różniczkowego do rzędu 2 oraz 30 dla trzech modeli rzutów całkowych i pierwotnych na prostokącie. Są to skończone modele wielomianowe, a nie formalizacja ogólnych twierdzeń. Poniższy kod utrwala reprodukowalną kontrolę FA20-SYM-76-01; nie jest ona dodatkowym krokiem CI.

```python
import sympy as s
x, y = s.symbols("x y", real=True)
phi = (1-x*x)**2*(1-y*y)**2*(1+x+2*y+s.I*x*y)
a = 1+x*y+s.I*y
f = 2+x*x+y**3+s.I*x*y
def integ(expr):
    return s.integrate(s.integrate(s.expand(expr),(x,-1,1)),(y,-1,1))
for i,j in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
    assert s.simplify(integ(a*s.diff(f,x,i,y,j)*phi)
        - (-1)**(i+j)*integ(f*s.diff(a*phi,x,i,y,j))) == 0
def eta(v):
    return s.Rational(3,4)*(1-v*v)
def P(z,v):
    return s.expand(eta(v)*s.integrate(z,(v,-1,1)))
for z in [phi,1+x+y+x*y,x*x*y**3+s.I*y]:
    assert s.expand(P(P(z,x),x)-P(z,x)) == 0
    assert s.expand(P(P(z,y),y)-P(z,y)) == 0
    assert s.expand(P(P(z,x),y)-P(P(z,y),x)) == 0
    assert s.expand(P(P(z,x),y)-eta(x)*eta(y)*integ(z)) == 0
    for v in (x,y):
        h = z-P(z,v)
        t = s.symbols("t")
        prim = s.integrate(h.subs(v,t),(t,-1,v))
        assert s.expand(prim.subs(v,1)) == 0
        assert s.expand(prim.subs(v,-1)) == 0
        assert s.expand(s.diff(prim,v)-h) == 0
```

## Decyzja
2/3 czystych przebiegów. Kolejny audyt 77: trzecia niezależna stabilizacja; jeśli bez usterek, zamknąć rozdział zgodnie z bramkami projektu. Bez rozszerzania materiału przed zamknięciem.
