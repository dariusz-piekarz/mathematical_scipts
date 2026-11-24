# AA-58 — audyt IV: radykał, rozszerzenia i kryteria Cartana

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob 0c16050097e6e9a1db456b98b1f4d29fd7372236, commit 7c719440a33d51216d2fafeb0c20fb9bba11fb47.

## Kontrola dowodów
Sprawdzono rozwiązalność rozszerzenia, maksymalność sumy ideałów rozwiązalnych, niezmienniczość radykału względem automorfizmów i półprostotę ilorazu. Weryfikowano dokładnie warunki ideału w całej algebrze oraz obraz przez homomorfizm surjektywny. W kryterium rozwiązalności ponownie sprawdzono redukcję do obrazu ad i rozszerzenie skalarów; w kryterium półprostoty oba kierunki, w szczególności abelowy ostatni niezerowy wyraz szeregu pochodnego radykału oraz zerowość śladu operatora mającego obraz w tym ideale i znikającego na nim. Rozróżniono radykał rozwiązalny i jądro formy Killinga (nie są ogólnie równe). W zakresie objętym audytem nie znaleziono nowych błędów wymagających zmiany źródła.

## Niezależna regresja
1. Modele g_m=sl2 ⋉ Sym^m(K^2), m=0,...,7. Stałe struktury na bazie h,e,f,v_0,...,v_m: [h,v_i]=(m-2i)v_i, [e,v_i]=i v_(i-1), [f,v_i]=(m-i)v_(i+1), nawiasy wewnątrz V zerowe. Dokładne obliczenia macierzy ad i K, rangi przez eliminację BigInt nad Q. Sprawdzono 4320/4320 tożsamości Jacobiego, 4320/4320 niezmienniczości K, 312/312 warunków abelowego ideału i 312/312 zerowych wpisów K dla pierwszego argumentu w V. Radykał to V, ponieważ V jest abelowym ideałem, a iloraz to prosta sl2. Ranga K=3 we wszystkich ośmiu modelach; K(h,h)=8+m(m+1)(m+2)/3, K(e,f)=K(h,h)/2. Dla m=0 wymiar algebry pochodnej 3, dla m>=1 równy całemu wymiarowi m+4. Pokazuje to także, że warunek [g,g]=g nie implikuje półprostoty.
2. Algebry b_n macierzy górnotrójkątnych, n=1,...,10. Obliczenie śladu iloczynu macierzy dołączonych z rzadkich współrzędnych nawiasu w bazie E_ij: 7942/7942 par. K(E_ii,E_jj)=n-1 dla i=j i -1 dla i!=j; wszystkie pary z co najmniej jedną jednostką ściśle górnotrójkątną mają wartość zero. Sprawdzono 6237/6237 par warunku kryterium rozwiązalności i 35/35 wyrazów szeregu pochodnego. Ranga K=n-1, co wynika z bloku nI-J (J macierz jedynek), a radykał jest całą b_n. Dla n>=2 jądro K jest właściwym podzbiorem radykału. Obliczenia w bezpiecznej arytmetyce całkowitej, nie dowody ogólnych twierdzeń. Bez rozszerzania treści rozdziału.

## CI
Run 45371914625, job 138368038152: in_progress/brak, kroki {"success":59,"in_progress":1,"pending":65}. Krok Run repository tool tests: success; naprawa kolizji etykiet nie jest traktowana jako zatwierdzenie całego CI. PDF nie oglądano.

## Werdykt
Pierwszy czysty audyt po korektach III: 1/2. AA-58 W AUDYCIE. Następnie ponowna kontrola rozkładu ortogonalnego, derywacji, rachunku tensorowego, pełnego CI i PDF. AA-59 nieotwarty.
