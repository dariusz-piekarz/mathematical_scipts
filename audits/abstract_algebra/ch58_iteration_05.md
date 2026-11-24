# AA-58 — audyt V: rozkład ortogonalny, derywacje i ślady tensorowe

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob 0c16050097e6e9a1db456b98b1f4d29fd7372236, commit 7c719440a33d51216d2fafeb0c20fb9bba11fb47.

## Kontrola dowodów
Ponownie sprawdzono ortogonalne dopełnienie ideału względem symetrycznej niezmienniczej formy, komutowanie ideałów przy niezdegenerowaniu, zerowość ich przecięcia z półprostoty, wzór na wymiar dopełnienia i izomorfizm algebr Liego. Sprawdzono indukcję do składników prostych i kierunek odwrotny, również dla pustej sumy. W dowodzie wewnętrzności derywacji sprawdzono izomorfizm z przestrzenią dualną, wybór z, tożsamość [D,ad_x]=ad_(Dx), cykliczność śladu i końcowe zastosowanie niezdegenerowania. W rachunku tensorowym sprawdzono definicję T, przeplatanie działania, znak formy alternującej, obrazy przestrzeni własnych zamiany czynników, wymiary, rzuty oraz ślady. Ponownie sprawdzono modele gl, sl, so, sp i przypadki n=1, so_2. Nie stwierdzono usterek wymagających zmiany źródła. Zakres bez zmian.

## Niezależne regresje
Dla g=sl2^{⊕m}, m=1,...,5, zbudowano stałe struktury i pełny liniowy układ równań derywacji na wszystkich parach różnych wektorów bazowych. Dokładna eliminacja całkowita BigInt nad Q z redukcją przez NWD: 2790 równań łącznie; w każdym modelu dim Der(g)=dim g=3m. Macierze Killinga obliczono bezpośrednio z ad, ranga pełna. Dla wszystkich podzbiorów składników (62 podziały łącznie) zweryfikowano komutowanie obu podsum, ortogonalność i wymiary oraz niezdegenerowanie ograniczeń. Sprawdzono 495/495 wartości funkcjonału tr(ad_z ad_x) dla z i x z baz, zgodnych z obliczoną formą. Brak twierdzenia o sprawdzeniu dowolnej derywacji przez enumerację: równość wymiarów i zerowe centrum dają wewnętrzność w tych modelach.

Dla wymiarów V od 1 do 12 sprawdzono obie tożsamości śladowe na wszystkich uporządkowanych parach jednostek macierzowych (60710 par), przez indeksy obrazu wektora bazowego pod operatorem A⊗B oraz po zamianie czynników. Dodatkowo 240 par pełnych macierzy całkowitych: zgodność sum współczynników diagonalnych z tr(A)tr(B) oraz tr(AB). Wszystkie wyniki poprawne. Regresje nie zastępują dowodów.

## CI
Run 45371914625, job 138368038152: in_progress/brak, kroki {"success":119,"in_progress":1,"pending":5}, artefakty []. Nie oglądano PDF.

## Werdykt
Dwa czyste audyty matematyczne po korektach III: 2/2. AA-58 W AUDYCIE TECHNICZNYM do pełnego CI i oględzin aktualnego PDF. AA-59 nieotwarty.
