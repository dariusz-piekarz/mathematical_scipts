# Rozdział 22 — audyt 88 (stabilizacja I, 1/3)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Przegląd
Źródło bez zmian od audytu 87 (blob acfd4698d6a8148985cea876bcf56259275abcd6). Ponowna kontrola czterech podsekcji i dziewięciu dowodów: kryterium ciągłości i oszacowania wzrostu, kontrprzykład Gaussa, ciągłość ograniczenia oraz włożenia L2 przy biliniowym parowaniu, działanie mnożników, zwartość domknięcia zbioru ograniczonego, rozróżnienie topologii silnej i słabej-* mimo zgodności ciągów zbieżnych, transpozycja Fouriera i znaki, konstrukcja przedłużenia Plancherela, różniczkowanie przesunięć i oszacowania ogonów w seminormach Schwartza, zamiana działania dystrybucji z całkowaniem oraz niezależność rzędu wzrostu transformaty dystrybucji o zwartym nośniku od wielowskaźnika pochodnej. Nie stwierdzono nowych istotnych usterek wymagających zmian.

## Bramki
16/16 unikatowych etykiet, 26/26 odsyłaczy rozwiązanych w kontekście 17–22, 49/49 fragmentów regresyjnych, poprawne zagnieżdżenie środowisk. Bieg 45430736181 dla commitu 038620b9dcf184105f0d2b60f0f987f9f82d8b87 zakończył się sukcesem we wszystkich krokach, w tym sześciu metodach Python, kompilacji pełnego kontekstu i diagnostyce PDF. Porównano 24 pliki rozdziałów 01–22 z 15A/15B, plik główny, workflow i plik regresji z wersją zaliczoną w CI: wszystkie identyczne. Pobrano artefakt 14937134732, PDF 185 stron. Wyrenderowano strony 178–185 w PyMuPDF (skala 1.5), obejrzano dwie plansze po cztery strony. Nie stwierdzono widocznych kolizji ani obcięć. W logu brak dopasowań Overfull, undefined, Missing character, LaTeX Warning. Nie uruchamiano Lean.

## Kontrola pomocnicza FA22-SYM-88-01
Wykonano lokalnie Python z Fraction: 729 tożsamości dopełniania kwadratu dla splotu przesuniętych funkcji Gaussa oraz 36 kontroli kwadratu stałej normalizacyjnej (po usunięciu wspólnego czynnika (2pi)^d) i 36 kontroli wykładnika dla wymiarów 1–4; razem 801/801. Kod zachowany poniżej. Są to dokładne modele algebraiczne, nie dowód ogólny ani dodatkowa metoda CI.

```python
from fractions import Fraction as F
from itertools import product
from math import prod

n = q = 0
for a,b,u,v,x,y in product([F(1,2),F(1),F(3)],
        [F(1,3),F(2),F(4)],[-2,0,3],[-1,0,2],
        [-3,1,2],[-2,0,4]):
    A = a+b
    B = a*u+b*(x-v)
    c = a*b/A
    assert a*(y-u)**2+b*(x-y-v)**2 == A*(y-B/A)**2+c*(x-u-v)**2
    n += 1
for d in (1,2,3,4):
    for a,b in product([F(1,2),F(1),F(3)],[F(1,3),F(2),F(4)]):
        aa = [a+j for j in range(d)]
        bb = [b+2*j for j in range(d)]
        cc = [a*b/(a+b) for a,b in zip(aa,bb)]
        assert prod(1/(a+b) for a,b in zip(aa,bb))*prod(1/c for c in cc) == prod(1/a for a in aa)*prod(1/b for b in bb)
        assert all(1/c==1/a+1/b for a,b,c in zip(aa,bb,cc))
        q += 2
assert (n,q) == (729,72)
```

## Decyzja
Pierwszy czysty przebieg: 1/3. Nie zmieniano źródła ani pliku regresji. Następny audyt 89 — stabilizacja II, bez rozszerzania materiału.
