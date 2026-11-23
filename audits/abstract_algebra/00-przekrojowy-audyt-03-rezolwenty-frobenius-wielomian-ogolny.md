# Algebra abstrakcyjna — audyt przekrojowy 03: rezolwenty, Frobenius i wielomian ogólny

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. HEAD odczytany przed zapisem: `2211c02113b34cc452f19c963045492a187808cd`.

## Zakres i identyfikacja źródeł

Kontrola przekrojowa AA-34–AA-36, odmienna od audytu przekrojowego 01 (AA-41–AA-42) i 02 (AA-38–AA-40). Katalog `catalog/books.json` wymienia 42 rozdziały, bez AA-43. Nie tworzono rozdziału AA-43.

- AA-34 `34-rezolwenta-szescienna-i-grupy-galois-stopnia-czwartego.tex`, blob `a7202801c7e5ae9d4ad202a5deceabd631512a85`.
- AA-35 `35-redukcja-modulo-p-i-cykle-frobeniusa.tex`, blob `345bdebd74b8190bfb04f70ac7afe56b043dcb11`.
- AA-36 `36-wielomian-ogolny-i-grupy-symetryczne.tex`, blob `4c7f5c055172ff88331978592b89d4c44d5584dc`.

Odczytano również `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` oraz wcześniejszy raport przekrojowy 02. Standard Biblioteki: nie zmieniać zatwierdzonych etykiet, nie dopisywać twierdzeń bez zgody, kontrolować jawność założeń i szczegółowość dowodów.

## Rzeczywiście wykonana kontrola

Porównano konstrukcję i typy rozkładu rezolwenty sześciennej w AA-34 z informacją o typach cykli Frobeniusa w AA-35 oraz z tezą o grupie Galois wielomianu ogólnego w AA-36. W AA-34 skontrolowano warunki: moniczność, nierozkładalność i rozdzielczość wielomianu stopnia czwartego oraz charakterystykę różną od 2 w klasyfikacji przez rezolwentę. Rozkłady rezolwenty 1+1+1, 1+2 i 3 odpowiadają obrazom grupy w działaniu na trzech podziałach parowych; same nie rozstrzygają C4/D4 ani A4/S4. W AA-35 skontrolowano wymóg dobrej redukcji (pierwsza nie dzieli wyróżnika), interpretację długości czynników nierozkładalnych i ostrzeżenie, że rozkład całkowity przy jednej liczbie pierwszej nie oznacza trywialności grupy. W AA-36 skontrolowano rozróżnienie wielomianu ogólnego o algebraicznie niezależnych współczynnikach od specjalizacji.

Przejrzano listy etykiet i użyć `\\ref`/`\\eqref`/`\\autoref`/`\\cref` w trzech źródłach; nie wykonano jednak pełnego globalnego rozwiązania wszystkich odsyłaczy względem całej książki. To ograniczenie nie jest wynikiem PASS.

## Niezależne testy obliczeniowe

Uruchomiono lokalnie skrypt Python/SymPy z 16 asercjami: wyróżnik `X^3-X-1=-23`; stopnie czynników modulo 2, 3, 5, 7, 59; powtórny pierwiastek modulo 23; wyróżnik `(X^2-2)(X-3)=392`; rozdzielczość `X^4-X-1` modulo 2, 3, 5, 7, 11; wyróżnik `X^4-X-1=-283`; rozkład rezolwenty `(Y-2)(Y^2+Y-1)` dla `\\Phi_5`; dodatniość wyróżnika `X^4-10X^2+1`. Wynik: **16/16 PASS**. Testy te potwierdzają wybrane rachunki, nie wszystkie dowody.

## Wynik i ograniczenia

- Nie wykryto sprzeczności w zbadanych zależnościach i rachunkach.
- **Zmiany w rozdziałach: 0.** Nie dodawano twierdzeń ani nie zmieniano etykiet.
- **Kontrola matematyczna:** częściowa kontrola przekrojowa z 16/16 asercjami; nie jest pełnym ponownym audytem każdego z trzech rozdziałów.
- **Kompilacja LaTeX i wizualna inspekcja PDF:** nie wykonano w tym przebiegu; brak deklaracji PASS.
- **GitHub Actions/CI:** nie uruchomiono i nie zweryfikowano; brak deklaracji PASS.
- **Stabilność AA-01–AA-42:** raport nie zmienia statusu wcześniejszych audytów ani nie potwierdza całości.
- **Następny etap:** ponownie sprawdzić AA-43 i bieżący HEAD; przy jego braku wykonać nową, niepowtórzoną kontrolę przekrojową innego zakresu, np. AA-28–AA-33 (wzory na wyróżniki i wypadkowe oraz ich hipotezy).

## Testy do odtworzenia

```python
import sympy as S
x,y=S.symbols("x y")
f=x**3-x-1
assert S.discriminant(f,x)==-23
for p,degrees in [(2,[3]),(3,[3]),(5,[1,2]),(7,[1,2]),(59,[1,1,1])]:
    factors=S.factor_list(f,modulus=p)[1]
    assert sorted(S.degree(g,x) for g,k in factors for _ in range(k))==degrees
assert S.rem(f,(x-3)*(x-10)**2,x,domain=S.GF(23))==0
assert S.discriminant((x*x-2)*(x-3),x)==392
for p in [2,3,5,7,11]:
    q=S.Poly(x**4-x-1,x,modulus=p)
    assert S.gcd(q,q.diff()).degree()==0
assert S.discriminant(x**4-x-1,x)==-283
assert S.expand((y-2)*(y*y+y-1))==y**3-y*y-3*y+2
assert S.discriminant(x**4-10*x*x+1,x)>0
```
