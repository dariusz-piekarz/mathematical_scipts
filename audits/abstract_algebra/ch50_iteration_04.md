# AA-50 — audyt IV: dowód dla wielomianów nieunormowanych

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex.
Commit poprawki: 611ac48fbb27eec6529c6dc4ed0d00fd9878b16b.
Blob: fcd1dcc205a120df3c9d69b2ae1b04daf5b785b8.

## Usterki i poprawki

1. W lemacie o pierwiastkach F pominięto pochodną jednostki u z rozkładu F=u∏ f_j^{m_j}. Poprzednia tożsamość była fałszywa dla nieunormowanego F. Poprawna tożsamość: H=u'/u+Σ m_j Df_j/f_j. Jest to istotne, bo w konstrukcji F współczynnik wiodący to −S^n P, zwykle niestały.
2. K[T]_(f_j) to lokalizacja, nie pierścień ilorazowy. Uzupełniono dowód podzielności przez f_j: po wyizolowaniu składnika otrzymujemy Df_j/f_j=a/b, gdzie f_j nie dzieli b; stąd z pierwszości f_j wynika f_j | Df_j. Odwracalność m_j wynika z charakterystyki zero.
3. Jawnie uwzględniono q=0 w twierdzeniu algorytmicznym i jego dowodzie, doprecyzowano całkowitość n oraz zaktualizowano nieaktualne określenie liczby przykładów.

## Niezależny sprawdzian symboliczny

W bieżącej sesji uruchomiono SymPy dla q=0, f=T−1/x oraz F=u f^m, dla (u,m)=(x,1), (x²+1,2), (1/x,3). Wszystkie trzy przypadki potwierdziły poprawioną tożsamość, fałszywość wersji bez u'/u, podzielność Df przez f oraz Riccatiego dla w=1/x. Pierwsze uruchomienie przerwało się na porównaniu strukturalnym równoważnych wyrażeń SymPy; zastąpiono je sprawdzaniem uproszczonej różnicy i ponownie wykonano całość: 3/3 PASS. To kontrola konkretnej poprawki, nie pełne testy rozdziału.

## Status

Dowód został poprawiony, lecz poprzedni zielony CI i oględziny PDF odnoszą się do wcześniejszego źródła. Aktualny AA-50 wymaga ponownej bramki regresji, CI oraz kontroli stron PDF po zmianie. Werdykt: W AUDYCIE (ponowna stabilizacja). AA-51 pozostaje nieotwarty. Raporty historyczne pozostają nienaruszone.
