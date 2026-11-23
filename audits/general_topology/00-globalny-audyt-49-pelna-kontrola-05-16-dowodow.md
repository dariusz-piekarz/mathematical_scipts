# Topologia ogólna — globalny audyt 49: pełna niezależna kontrola 16 dowodów rozdziału 05

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Źródło:** `chapters/pl/general_topology/05-aksjomaty-oddzielania.tex`, zweryfikowany blob `462acd8f3e1e350478d921429118ec19ac7f4ca8` (993 wiersze).

## Metoda i zakres

Ponownie odczytano aktualne tezy i **wszystkie 16 środowisk proof**, przeprowadzając niezależnie kontrolę założeń, kierunków implikacji oraz skrajnych przypadków w przestrzeniach nie-Hausdorffa i bez T1. Przeczytano też całą konstrukcję Mysiora i dowód nienormalności płaszczyzny Sorgenfreya. Dla Urysohna i Tietzego sprawdzono konstrukcje funkcji, a nie tylko końcowe oszacowania. Numery identyfikatorów odpowiadają macierzy 33; nie zalicza się konstrukcji Mysiora jako osobnego `proof`, ponieważ jest umieszczona w środowisku `przyklad`.

## Macierz 16/16 dowodów

| ID | Etykieta i wiersze | Niezależny test argumentu |
|---|---|---|
| 05-01 | `prop:topog-t2-t1-t0`, 87–92 | Rozłączne otwarte U∋x,V∋y dostarczają obu skierowanych rozróżnień T1; dla T1 jedno takie rozróżnienie wystarcza do T0. Gdy X ma co najwyżej jeden punkt, wszystkie warunki są spełnione pusto. |
| 05-02 | `thm:topog-t1-singletony`, 108–122 | T1 ⇒ dopełnienie {x} jest sumą otwartych zbiorów niezawierających x; odwrotnie otwartość obu dopełnień singletonów rozróżnia uporządkowaną parę x≠y. Dowód obejmuje X=∅ i singleton. |
| 05-03 | `cor:topog-skonczone-t1`, 129–134 | Dla skończonej X każdy podzbiór jest skończoną sumą domkniętych singletonów, stąd wszystkie podzbiory są jednocześnie domknięte i otwarte; dla pustej X działa to samo. Odwrotność wynika z dyskretności singletonów. |
| 05-04 | `prop:topog-przekatna-hausdorff`, 156–171 | Z T2 rozłączne U,V dają otwarte U×V nieprzecinające przekątnej. Z domkniętości Δ_X i bazy topologii produktu otwarty prostokąt zawarty w dopełnieniu Δ_X ma rozłączne rzuty-otoczenia. Nie zakłada się metryzowalności. |
| 05-05 | `thm:topog-rownosc-na-gestym`, 181–189 | Mapa (f,g):X→Y² jest ciągła na mocy własności uniwersalnej iloczynu. Przeciwobraz domkniętej przekątnej Δ_Y jest domknięty. Gęstość D⊂E implikuje cl D=X⊂E, więc f=g; Hausdorffowość wymagana jest tylko w Y. |
| 05-06 | `prop:topog-regularnosc-zwezanie`, 221–233 | Dla x∉F rozdzielenie x i F otwartymi U,V daje cl U⊂X\V⊂X\F. W drugą stronę z x∈U⊂cl U⊂X\F i V=X\cl U dostajemy rozłączne otwarte U,V; brak potrzeby T1 w konwencji regularności użytej w tekście. |
| 05-07 | `cor:topog-t3-t2`, 239–244 | T3 jawnie łączy regularność i T1; domknięty singleton {y} można oddzielić od punktu x≠y. Wniosek byłby fałszywy bez hipotezy T1, ale została ona zastosowana. |
| 05-08 | `prop:topog-calkowita-regularnosc-regularna`, 313–321 | Oddzielająca funkcja ciągła f:X→[0,1] ma otwarte przeciwobrazy [0,1/3) oraz (2/3,1] w topologii względnej [0,1]; oba są rozłączne i rozdzielają x i F. Nie przemyca się T1 do samej regularności. |
| 05-09 | `prop:topog-normalnosc-zwezanie`, 511–520 | Z normalności F i zamkniętego X\W oddzielamy otwartymi U,V i otrzymujemy cl U⊂X\V⊂W. W kierunku odwrotnym W=X\G oraz V=X\cl U rozdzielają dowolne rozłączne domknięte F,G, również gdy F lub G jest puste. |
| 05-10 | `thm:topog-urysohn`, 529–592 | Indukcja po wymiernych dwójkowych dobiera otwarte U_r z cl U_r⊂U_s dla r<s; poprawnie traktuje poziomy 0 i 1. Funkcja f(x)=inf({r:x∈U_r}∪{1}) rozdziela F,G. Obie tożsamości {f<a}=∪_{r<a}U_r i {f>a}=∪_{a<r<1}(X\cl U_r) są prawidłowe, także gdy f(x)=1. Z gęstości liczb dwójkowych wybiera się a<r<s<f(x) (jeśli a<f(x)); nie jest potrzebne T1. |
| 05-11 | `cor:topog-t4-tych`, 600–607 | Hipoteza T4 dostarcza jednocześnie normalności i T1. Singleton {x} jest więc domknięty, a lemat Urysohna oddziela go funkcją od zamkniętego F. Wniosek Tychonoffa nie byłby uzasadniony samą normalnością bez T1. |
| 05-12 | `thm:topog-tietze`, 641–723 | Domkniętość C_- i C_+ w X wynika z domkniętości A. Funkcja g=(M/3)(2u−1) ma normę ≤M/3 i błąd ≤2M/3 na A. W iteracji M_n=(2/3)^n, suma ∑ M_n/3=1 zapewnia jednostajną zbieżność i wartości w [-1,1]; błąd h_N→0 daje F|A=f. Przedział [a,b] obsługuje reskalowanie i przypadek a=b. Dla nieograniczonego f transformacja φ(t)=t/(1+|t|), zbiór C=H^{-1}({±1}), Urysohn v|C=0,v|A=1 dają |vH|<1 w każdym punkcie i legalne φ^{-1}(vH). Pusty A nie łamie konstrukcji; nie ma domyślnego T1. |
| 05-13 | `thm:topog-metryczne-t4`, 790–813 | Funkcja odległości d(x,A) jest 1-Lipschitz dla niepustego A, a dla zamkniętego A zeruje się dokładnie na A. Dla rozłącznych niepustych F,G mianownik d(x,F)+d(x,G) jest ściśle dodatni. Oddzielające poziomy funkcji budują otwarte U,V; puste F lub G rozdzielamy trywialnie. T1 pochodzi z metryki. |
| 05-14 | `prop:topog-oddzielanie-dziedziczenie`, 826–848 | T0–T2 dziedziczą się przez przecięcia otwartych zbiorów z A. Dla domkniętego F⊂A używa się F=A∩C dla domkniętego C⊂X: to kluczowe dla regularności i całkowitej regularności podprzestrzeni. Normalność ograniczona jest w tezie do A domkniętego, co umożliwia podniesienie domkniętych w A zbiorów do X. Nie przypisano normalności wszystkim podprzestrzeniom. |
| 05-15 | `thm:topog-sorgenfrey-plane`, 875–933 | Sorgenfrey ma bazę przedziałów [a,b) otwarto-domkniętych i jest Hausdorffa, co implikuje Tychonoffa; iloczyn zachowuje Tychonoffa. Zbiór D={(t,−t)} jest domknięty i dyskretny: [t,t+ε)×[−t,−t+ε) przecina D w jednym punkcie, a poza D niezerowy a+b zachowuje znak dla małego ε. Gęsty Q=ℚ² jest przeliczalny. Przy normalności dla każdego A⊂D rozłączne U_A,V_A pozwalają z A≠B znaleźć punkt z Q∩U_A∩V_B, zatem A↦Q∩U_A byłaby iniekcją P(D)→P(Q); Cantor wyklucza 2^{2^{ℵ0}}≤2^{ℵ0}. Jawnie wykorzystuje wybór rozdzieleń dla wszystkich A. |
| 05-16 | `prop:topog-oddzielanie-hierarchia`, 947–954 | Cały łańcuch T4⇒T_{3½}⇒T3⇒T2⇒T1⇒T0 jest składaniem wcześniej udowodnionych wyników; metryzowalność ⇒T4 pochodzi z poprawnego, oddzielnie sprawdzonego twierdzenia o odległościach do domkniętych zbiorów. |

## Osobny kontrprzykład Mysiora — kontrola konstrukcyjna

Przykład `ex:topog-mysior-t3-nie-tych` nie jest środowiskiem `proof`, lecz należy do krytycznych argumentów rozdziału. Sprawdzono: (i) lokalne bazy w punkcie osi i w nieskończoności są zgodne; (ii) przecięcia `B_x∩B_z` dla x≠z są skończone, dzięki czemu `B_x\E` są otwarto-domknięte; (iii) `cl W_{n+2}⊂W_n` — dla x≤n punkty `B_x` mają pierwszą współrzędną ściśle mniejszą od n+2; (iv) suma wyjątków `E_{x,m}` jest przeliczalna; (v) dla x_j∈(k−1,k] i z∈(k,k+1] mamy **0<z−x_j<2**, dzięki czemu punkty (z,z−x_j) należą do B_{x_j} i pionowego B_z; (vi) nieskończenie wiele takich punktów z f=1 zmusza f(z,0)=1 mimo dopuszczalnego usuwania **skończenie** wielu punktów w bazowych otoczeniach; (vii) propagacja na przedziały (k,k+1] wymusza f(∞)=1. Otrzymano T3, ale nie całkowitą regularność, bez użycia niejawnej metryki. **PASS.**

## Zgodność z historią audytów

- Poprzedni globalny audyt 37 sprawdził osobno Urysohna, Tietzego i Mysiora; bieżąca iteracja rozszerza indywidualną kontrolę **na wszystkie pozostałe 14 środowisk proof** w tym rozdziale i potwierdza poprzednie dwa.
- Lokalne 2+1 dla rozdziału 05 dokumentowały stabilizację, ale zwięzłe raporty nie zawierały 16 odrębnych indywidualnych uzasadnień. Niniejszy raport ten brak dokumentacyjny zamyka na **tym samym blobie**, bez zmiany istniejących dowodów.
- **Wynik matematyczny: 16/16 PASS, a dodatkowy przykład Mysiora: PASS.** Sprawdzono aktualne 16 etykiet z macierzą 33. Żadne nowe założenie ani poprawka do twierdzenia nie są potrzebne.
- Kwestia techniczna: workflow 45139515178 po raporcie 47 ma potwierdzone `completed/success`; workflow 45139764137 po raporcie 48 był w toku przy wcześniejszym odczycie. **Nowego CI po tym raporcie nie oznaczać sukcesem bez odczytu statusu.** Nie uruchamiano nowej wizualnej inspekcji PDF, ponieważ plik LaTeX nie został zmieniony.

## Dalszy plan

Po tym audycie liczba dowodów objętych indywidualną pełną dokumentacją rozdziałową rośnie z **177 do 193** spośród 325. Pozostaje **132**: rozdziały 07–09 (43), 10–13 (45) i 24–26 (44). Rozdziały 06, 14–23 są już indywidualnie udokumentowane; 01–04 zamknięto raportami 46–47. W kolejnym etapie reaudyt 07 (18 proof) i następnie 08–09, zgodnie ze stałą kolejnością. Nie należy mylić tego bilansu dokumentacji z liczbą poprawnych/niepoprawnych twierdzeń ani z formalizacją Lean.
