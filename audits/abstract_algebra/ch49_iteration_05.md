# AA-49 — audyt V: kontrola stabilizacyjna rodzin parametrów

Stan wejściowy 30c798493d2c01e8384c574934c5d763f7c93d32. Ponowny odczyt gałęzi: źródło AA-49 blob 27cc7e691df663b74ab1b157982aba48298f70a5, regresja SymPy blob f0aefd798f77345e99291f689a3b0f7bb4dc72ea; identyczne z audytem IV. Nie zmieniono treści ani etykiet.

## Kontrola niezależna

W lokalnym Python/SymPy wykonano dodatkowe dokładne obliczenia dwóch rodzin, zamiast powtarzać wyłącznie pojedyncze przykłady z regresji AA-49-FINAL-01. Dla m=2,...,9 przyjęto q=m(m-1)/x², theta=(2-2m)/x, P=x^(4m-2)+a x^(2m-1)+b. W każdym przypadku L(P)=0 oraz H=(2m-1)² x^(4m-4)(a²-4b), H'+2theta H=0. Dla wszystkich dziewięciu punktów siatki (a,b) w {0,1,2}² sprawdzono niezerowe wartości i stałość ilorazu H/x^(4m-4). Każdy niezerowy H ma parzysty stopień i jest kwadratem nad C(x). Dla p=-5,-3,-1,1,3,5,7 przyjęto theta=-p/(2x), q=x^p+p(p+4)/(16x²), P=1. W każdym przypadku L(P)=0, H=4x^p oraz H'+2theta H=0. Nieparzysta waluacja w zerze wyklucza kwadratowość. Te rodziny są modelami algebraicznych tożsamości; nie twierdzi się, że wszystkie dane pochodzą z list lokalnych drugiej gałęzi.

Wynik faktycznego wykonania: 15 modeli, 79 punktów parametrów, 63 niezerowe wartości H (8 rodzin kwadratowych, 7 modeli niekwadratowych), PASS. Kod odtwarzający:

```python
import sympy as s
from itertools import product
x,a,b=s.symbols('x a b')
def zero(e): return s.cancel(e)==0
def L(P,t,q):
    return (s.diff(P,x,3)+3*t*s.diff(P,x,2)
        +(3*t*t+3*s.diff(t,x)-4*q)*s.diff(P,x)
        +(s.diff(t,x,2)+3*t*s.diff(t,x)+t**3-4*q*t-2*s.diff(q,x))*P)
def H(P,t,q):
    return s.expand((4*q-2*s.diff(t,x)-t*t)*P**2
        -2*t*P*s.diff(P,x)-2*P*s.diff(P,x,2)+s.diff(P,x)**2)
models=points=nonzero=0
for m in range(2,10):
    q=s.Integer(m*(m-1))/x**2
    t=s.Integer(2-2*m)/x
    P=x**(4*m-2)+a*x**(2*m-1)+b
    h=H(P,t,q)
    assert zero(L(P,t,q))
    assert zero(h-(2*m-1)**2*x**(4*m-4)*(a*a-4*b))
    assert zero(s.diff(h,x)+2*t*h)
    for i,j in product(range(3),repeat=2):
        v=h.subs({a:i,b:j});points+=1
        if v!=0:
            assert zero(s.diff(v/x**(4*m-4),x))
            assert s.degree(v,x)%2==0
            nonzero+=1
    models+=1
for p in [-5,-3,-1,1,3,5,7]:
    t=-s.Rational(p,2)/x
    q=x**p+s.Rational(p*(p+4),16)/x**2
    P=s.Integer(1)
    h=H(P,t,q)
    assert zero(L(P,t,q))
    assert zero(h-4*x**p)
    assert zero(s.diff(h,x)+2*t*h)
    assert p%2==1
    models+=1;points+=1;nonzero+=1
print(models,points,nonzero)
```

Nie wykryto nowych usterek w poprawionym argumencie. Zachowano dodatkowe obliczenia w raporcie, bez redundantnego nowego obowiązkowego kroku CI. Nie jest to pełne uruchomienie testów repozytorium ani formalizacja Lean.

## CI

Run 45568064133, head 826df96888ea50354ec898349501370bf13be17a, job 139047640809: przy ostatnim odczycie 62 kroki success, 1 aktywny (AA-37), 87 oczekujących. Globalna bramka integralności AA-01–72: success na tym przebiegu. Regresje AA-49, kompilacja i weryfikacja PDF nadal pending. Zapytanie o artefakty tego przebiegu zwróciło pustą listę. Nie przeprowadzono inspekcji nieistniejącego jeszcze artefaktu.

Audyt V czysty w wykonanym zakresie, drugi po korekcie przekrojowej. AA-49 pozostaje otwarty technicznie do potwierdzenia CI i PDF; po nich niezależny audyt kontrolny. Nie przechodzić do nowych zagadnień. Tom AA-01–72 pozostaje w końcowym audycie przekrojowym.
