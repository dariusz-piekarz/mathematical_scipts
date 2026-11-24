# Moduł 15B — iteracja 13 (zatwierdzone rozszerzenie)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Po zamknięciu audytu 12 użytkownik jawnie zatwierdził dodanie przykładu funkcji silnie mierzalnej, całkowalnej w sensie Pettisa, lecz nie Bochnera, w ośrodkowej przestrzeni Hilberta. Pozostałych propozycji z audytu 12 nie realizowano.

## Zmiana
Po przykładzie ex:pettis-not-bochner15b dodano ex:pettis-strong-not-bochner15b: S=N, pełna sigma-algebra, masa atomu 2^(-n), X=l2 nad R lub C, f(n)=2^n e_n/n. Silna mierzalność z punktowej zbieżności skończonych obcięć. Całkowalność skalarna z reprezentacji Riesza (jawna konwencja liniowości w pierwszej zmiennej) i nierówności Cauchy'ego–Schwarza. Dla każdego A wektor v_A=(chi_A(n)/n) należy do l2 i reprezentuje wszystkie całki skalarne, więc jest całką Pettisa. Całka normy jest rozbieżnym szeregiem harmonicznym. Podano różnicę względem przykładu nieośrodkowego, gdzie przeszkodą jest brak silnej mierzalności mimo stałej normy.

## Technika
Źródło: commit 2db89773cb8d93fee512ae522382fec66c12a557, blob 641dd59fc065281f00dda099123dac99533213cc. Dodano 69 wierszy, 862 wiersze łącznie. Zachowano wszystkie 23 wcześniejsze etykiety, dodano jedną unikalną; 5 przykładów, 11 środowisk dowodów. Zagnieżdżenie środowisk poprawne w ponownym odczycie.
Testy: commit 0dd145ca0b6b1388fe4f8fe189a23fca209d44f8, blob 5b744df89381f90529f84effdddfdba6a28ac40c. Dodano dwunasty test: sześć kontraktów tekstowych, dokładne rachunki całki skalarnej i wektora reprezentującego na skończonych podzbiorach, oszacowania bloków diadycznych dwóch szeregów. Kontrakty tekstowe sprawdzono; pełny unittest i PDF nowego źródła nie są jeszcze zweryfikowane w tej iteracji. Statusy odczytane z API: [{"id":45348086656,"sha":"0dd145ca0b6b1388fe4f8fe189a23fca209d44f8","status":"in_progress","conclusion":null},{"id":45348063025,"sha":"2db89773cb8d93fee512ae522382fec66c12a557","status":"in_progress","conclusion":null}].

## Decyzja
Nowe zatwierdzone rozszerzenie zmienia ustabilizowany moduł: stan 0/2 dla nowego źródła. Następny niezależny audyt 14, kontrola nowego przykładu, regresji i PDF. Nie przechodzić do 16 przed ponowną stabilizacją.
