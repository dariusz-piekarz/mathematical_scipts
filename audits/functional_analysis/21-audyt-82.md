# Rozdział 21 — audyt 82 (stabilizacja I, 1/3)

24 listopada 2026. Wyłącznie gałąź biblioteka-matematyczna-iteracja-6.

## Przegląd
Źródło niezmienione od audytu 81 (blob b1f0eb53c44e2cc014aadd97b2ed4fcfd4b99654), 782 wiersze, pięć podsekcji, dziewięć dowodów. Ponownie sprawdzono przedłużenie działania i jednoznaczność identyfikacji liniowej, lokalność oraz przypadek pustego nośnika, różniczkowanie w seminormach, aproksymację iloczynową w jednym powiększonym etapie i przejście do granicy, ciągłość operatora testowego i nośnik splotu, wszystkie ustawienia dwóch zwartych nośników przy łączności, znaki translacji i różniczkowania, zwartość nośnika funkcji G, odbicie jądra, normalizację i oszacowanie silne oraz sprzeczność przy próbie rozszerzenia splotu. Skontrolowano konwencję funkcji i dystrybucji regularnej oraz odsyłacze. Nie stwierdzono nowych usterek wymagających zmian. Bez rozszerzania zakresu.

## Bramki
19/19 unikatowych etykiet, 24/24 odsyłaczy rozwiązanych w kontekście 17–21, 44/44 warunków tekstowych z trwałego pliku testów (blob a63b5f0ff9e6e3ec1a9b5fc70f468c5826bcb17d), poprawne zagnieżdżenie środowisk. Bieg 45425472472 dla commitu be4c17c7efd875d1e1a728c5e2abd9268db8c21e zakończył się sukcesem, w tym sześć metod regresyjnych, kompilacja pełnego kontekstu 01–21, diagnostyka PDF i upload. Pobrano artefakt 14936791805, rozpakowano PDF (178 stron), wyrenderowano strony 171–178 w PyMuPDF (skala 1.25) i obejrzano dwie plansze po cztery strony. Brak widocznych kolizji i obcięć. W logu brak dopasowań Overfull, undefined, Missing character, LaTeX Warning. Oględziny dotyczą aktualnego źródła. Nie uruchamiano Lean.

## Kontrola pomocnicza FA21-SYM-82-01
Uruchomiono lokalnie Python z Fraction: 80/80 dokładnych tożsamości dla pochodnych rzędu 1–4 dystrybucji całkowania po półosi, na modelach wielomianowych z zerowymi dżetami do rzędu 3 na prawym końcu przedziału. Są to modele całkowania przez części, nie funkcje testowe C-infinity ani formalizacja twierdzenia. Kod zachowany poniżej, nie jest dodatkową metodą CI.

```python
from fractions import Fraction as F
from math import comb
count = 0
for R in (F(1,2), F(1), F(2), F(3)):
    for p in ([1],[1,2],[0,1,3],[2,-3,4,1],[0,0,1]):
        c = [F(0)]*(len(p)+4)
        for i,a in enumerate(p):
            for j in range(5):
                c[i+j] += a*comb(4,j)*(-1/R)**j
        for n in range(1,5):
            deriv = c[:]
            for k in range(n):
                deriv = [(i+1)*v for i,v in enumerate(deriv[1:])]
            actual = (-1)**n*sum(v*R**(i+1)/F(i+1)
                                 for i,v in enumerate(deriv))
            jet = c[n-1]
            for k in range(1,n):
                jet *= k
            expected = (-1)**(n-1)*jet
            assert actual == expected
            count += 1
assert count == 80
```

## Decyzja
Pierwszy czysty przebieg 1/3. Nie zmieniano źródła ani istniejących testów. Następny audyt 83: stabilizacja II; nie rozszerzać materiału przed trzema czystymi przebiegami.
