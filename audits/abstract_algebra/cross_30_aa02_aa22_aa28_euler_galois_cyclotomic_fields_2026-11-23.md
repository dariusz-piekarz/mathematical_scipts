# Algebra abstrakcyjna — AA-X30: jednostki modulo n, odpowiedniość Galois i ciała cyklotomiczne (AA-02 × AA-22 × AA-28)

**Data:** 23 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Status na etapie przygotowania raportu:** matematyka zbadana, CI w stabilizacji.

## Rzeczywiste źródła i niepowtarzalność

Zidentyfikowano 50 zatwierdzonych rozdziałów AA-01–AA-50, bez AA-51, odczytano AGENTS.md i aktualne źródła:
- AA-02: chapters/pl/abstract_algebra/02-warstwy-lagrange-euler-i-grupy-ilorazowe.tex, blob 36efd06e0da961cc60dadc061ebc43122e4f14f2, 877 wierszy; definicja aa:def:jednostki, twierdzenia aa:tw:euler, aa:tw:phi-wzor.
- AA-22: chapters/pl/abstract_algebra/22-twierdzenie-artina-i-odpowiedniosc-galois.tex; definicja aa:def:fixed-field i podstawowe twierdzenie teorii Galois.
- AA-28: chapters/pl/abstract_algebra/28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex, blob 2e24a69608aeab7856acf40f882480a97eb455bc, 328 wierszy; twierdzenie aa:tw:cyclotomic-galois, przykłady aa:prz:cyclotomic-five i aa:prz:cyclotomic-eight.

AA-X30 jest nowym audytem zależności między trzema rozdziałami, a nie powtórzeniem AA-X04 (wypadkowe i wyróżniki cyklotomiczne) ani AA-X24 (kryterium Eisensteina dla potęg liczb pierwszych). Zatwierdzone rozdziały i etykiety nie zostały zmienione.

## 1. Twierdzenie o złożeniu i przecięciu dwóch ciał cyklotomicznych

**Twierdzenie.** Niech m,n≥1 będą liczbami całkowitymi, d=gcd(m,n), N=lcm(m,n). Przy ustalonym algebraicznym domknięciu Q połóżmy E_m=Q(ζ_m), E_n=Q(ζ_n), gdzie ζ_k oznacza dowolny pierwotny k-ty pierwiastek z jedynki, a ζ_1=1. Wtedy
\[
E_m E_n=E_N,\qquad E_m\cap E_n=E_d.
\]
Iloczyn ciał oznacza tu najmniejsze wspólne nadciało (złożenie rozszerzeń), nie iloczyn prosty czy iloczyn tensorowy. Zachodzą również:
\[
[E_m E_n:\mathbb Q]=\varphi(N),\qquad
[E_m\cap E_n:\mathbb Q]=\varphi(d),\qquad
\varphi(m)\varphi(n)=\varphi(d)\varphi(N),
\]
gdzie przyjmujemy φ(1)=1, zgodnie z konwencją używaną w AA-28. AA-02 definiuje grupę jednostek modulo n jawnie dla n≥2; przypadek n=1 jest grupą trywialną.

**Dowód równości złożenia.** Wybierzmy pierwotny N-ty pierwiastek ω i spójne generatory ζ_m=ω^{N/m}, ζ_n=ω^{N/n}. Taka zmiana pierwotnego generatora nie zmienia ciała cyklotomicznego, bo dowolne dwa generatory są potęgami o wykładnikach względnie pierwszych z odpowiednim modułem. Oba pierwiastki należą do Q(ω), zatem E_m E_n⊆E_N.

Skoro N=mn/d, liczby a=N/m=n/d i b=N/n=m/d są względnie pierwsze. Z tożsamości Bézouta istnieją s,t∈Z takie, że sa+tb=1. Otrzymujemy ω=(ω^a)^s(ω^b)^t=ζ_m^s ζ_n^t∈E_m E_n. Zatem E_N⊆E_m E_n, co daje równość. Wykładniki ujemne są dozwolone, gdyż pierwiastki jedności są jednostkami. Argument obejmuje przypadki m=1 i n=1.

**Pomocnicza tożsamość Eulera.** Dla dowolnej liczby pierwszej p i wykładników a,b≥0 mamy φ(p^a)φ(p^b)=φ(p^{min(a,b)})φ(p^{max(a,b)}); wynika to z faktu, że obie strony mają te same dwa czynniki w innej kolejności, także dla wykładnika 0 (φ(1)=1). Wykorzystując rozkład liczb na potęgi pierwsze i multiplikatywność φ, otrzymujemy φ(m)φ(n)=φ(d)φ(N). Multiplikatywność φ można uzasadnić chińskim twierdzeniem o resztach lub wzorem AA-02: φ(k)=k∏_{p|k}(1−1/p).

**Dowód przecięcia przez podgrupy.** Niech M=E_N i G=Gal(M/Q). AA-28 zapewnia izomorfizm G≅U(N)=(Z/NZ)^×, gdzie σ_k(ω)=ω^k, a AA-22 odpowiadające podgrupy i ich ciała elementów stałych. Oznaczmy H_m=Gal(M/E_m) i H_n=Gal(M/E_n). Ponieważ ζ_m=ω^{N/m}, element σ_k należy do H_m wtedy i tylko wtedy, gdy k≡1 (mod m); analogicznie dla n. Rozważmy też H_d. Bezpośrednio H_m H_n⊆H_d.

Dla każdej dodatniej liczby c dzielącej N redukcja U(N)→U(c) jest surjektywna. Istotnie, przy rozkładzie N=∏p^e oraz c=∏p^f (0≤f≤e) można każdą jednostkę modulo p^f podnieść do jednostki modulo p^e, a przy f=0 wziąć 1; chińskie twierdzenie o resztach łączy te podniesienia. Stąd |H_c|=φ(N)/φ(c), również dla c=1.

Ponieważ H_m∩H_n to klasy k≡1 zarówno modulo m, jak i modulo n, mamy H_m∩H_n={1} w U(N). Grupa G jest abelowa, więc H_m H_n jest podgrupą, a
\[
|H_mH_n|=|H_m||H_n|
=\frac{\varphi(N)^2}{\varphi(m)\varphi(n)}
=\frac{\varphi(N)}{\varphi(d)}
=|H_d|.
\]
Z zawierania H_mH_n⊆H_d wynika H_mH_n=H_d.

Korzystając z odwracania inkluzji w odpowiedniości Galois:
\[
E_m\cap E_n=M^{H_m}\cap M^{H_n}
=M^{\langle H_m,H_n\rangle}=M^{H_d}=E_d.
\]
Wraz z wynikami o stopniach E_k/Q=φ(k) z AA-28 dowodzi to wszystkich tez. **Koniec dowodu.**

## 2. Konsekwencje i granice twierdzenia

- Jeśli gcd(m,n)=1, to E_m∩E_n=Q, [E_mE_n:Q]=φ(m)φ(n); jest to liniowa rozłączność tych dwóch skończonych galoisowskich rozszerzeń nad Q. Użyte pojęcie dotyczy stopni, nie rozłączności zbiorowej ciał (które zawsze zawierają Q).
- Dla m=8,n=12 mamy d=4,N=24, zatem Q(ζ_8)∩Q(ζ_12)=Q(i), a ich złożeniem jest Q(ζ_24). Stopnie: 4,4,2,8, zgodne z 4·4=2·8. W szczególności przecięcie nie musi być równe Q dla niewzględnie pierwszych modułów.
- Dla m=9,n=15 mamy d=3,N=45, stopnie 6,8,2,24; przecięcie to Q(ζ_3).
- Przykład AA-28 n=8 wyraźnie wskazuje U(8)≅C2×C2 i brak generatora rzędu 4, podczas gdy n=5 daje U(5)≅C4. Nie należy wyciągać z abelowości grupy Galois ciała cyklotomicznego wniosku o jej cykliczności.
- Twierdzenie dotyczy podciał domknięcia algebraicznego Q. Nie należy wnioskować, że dowolne dwa rozszerzenia Galois o stopniach φ(m), φ(n) mają tak samo opisane przecięcie — konstrukcja jest specyficzna dla pierwiastków z jedynki.

## 3. Rzeczywiste regresje i technika

Dodano trwały moduł tools/tests/test_abstract_algebra_cross_aa02_22_28.py z 7 funkcjami:
1. φ(n), stopień, moniczność i nierozkładalność wielomianów cyklotomicznych dla n=1,…,48 (SymPy + niezależna enumeracja U(n));
2. surjektywność redukcji U(N)→U(d) dla wszystkich N≤96 i d|N, włącznie z d=1;
3. H_m H_n=H_gcd(m,n), H_m∩H_n={1}, poprawne liczności dla 1≤m,n≤21;
4. tożsamość φ(m)φ(n)=φ(gcd)φ(lcm) dla 1≤m,n≤75;
5. tożsamość Bézouta dla wykładników N/m,N/n i zgodność rzędów pierwiastków dla 1≤m,n≤75;
6. przykłady par (4,6), (8,12), (9,15), (8,9), (5,5), (1,14), grupy U(8), U(5);
7. liczba 50 rozdziałów, obecność i spójność kluczowych etykiet AA-02, AA-22, AA-28.

Sprawdzono niezależnie rachunek H_mH_n=H_gcd(m,n), H_m∩H_n i tożsamość Eulera dla **441 par** 1≤m,n≤21: PASS. To kontrola skończonych przypadków, nie zamiennik dowodu powyżej. Na moment publikacji raportu brak wyniku rzeczywistego CI nowego modułu.

**Commit testów:** b4484bf49676ce48aa5bf43e02a1beb3e6f53373.
**Commit integracji nowego kroku i wyzwalacza:** b2d7c2b82784d7606e56b25ea4e6691f3ba7c427.
Nazwa kroku: Run AA-X30 Euler cyclotomic Galois compositum checks.

**Werdykt na tym etapie: AA-X30 W STABILIZACJI CI.** Do zamknięcia potrzebne są wszystkie 7/7 nowych testów potwierdzone w rzeczywistym logu, pełny zielony workflow, kompilacja AA-01–AA-50 oraz automatyczna kontrola PDF i odsyłaczy. Bez nowej osobnej wizualnej inspekcji PDF nie należy deklarować pełnej kontroli wizualnej. Testy nie są formalizacją Lean.

**Wartościowe rozszerzenie opcjonalne (do decyzji użytkownika):** po twierdzeniu aa:tw:cyclotomic-galois w AA-28 umieścić wniosek o złożeniu i przecięciu ciał cyklotomicznych z wyraźnym odsyłaczem do AA-02 i AA-22. To nie jest obowiązkowa poprawka istniejącego dowodu; nie dodano jej do zatwierdzonych źródeł zgodnie z AGENTS.md.

**Następny etap:** stabilizacja AA-X30, a następnie dopiero nowy zakres AA-X31.


## Niezależna kontrola II — dodatkowe 3600 par modułów

Po zapisaniu testów wykonano **odrębny rachunek wyczerpujący w JavaScript** (bez SymPy, bez ponownego używania modułu Python z CI). Dla wszystkich 3600 uporządkowanych par `1≤m,n≤60` obliczono elementarnie grupy jednostek U(N), ich podgrupy H_m, H_n, H_d, gdzie N=lcm(m,n), d=gcd(m,n), a następnie bezpośrednio produkty podgrup H_mH_n. Porównano te produkty z H_d oraz zweryfikowano liczbowo równość φ(m)φ(n)=φ(N)φ(d). **Wynik: 3600/3600 par PASS, zero rozbieżności**.

Ta kontrola jest niezależna kodowo od testów GitHub Actions i obejmuje również przypadki m=1, n=1 oraz niecoprime m,n. Wykonanie rachunku zostało potwierdzone w bieżącej sesji audytowej; nie zastępuje ono żadnego z ogólnych dowodów ani nie stanowi jeszcze końcowej stabilizacji nowego workflow.
