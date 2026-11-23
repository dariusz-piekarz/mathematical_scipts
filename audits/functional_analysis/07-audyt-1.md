# Analiza funkcjonalna — rozdział 07 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex`.  
**SHA źródła po audycie:** `914059e1b20f1a9a3a8766a899659cde32109fb7`.  
**Werdykt:** pierwszy szczegółowy audyt **z poprawkami**, zatem **NIE jest czysty; stabilizacja rozdziału 07: 0/2**.

## Zakres

Sprawdzono pełne twierdzenia i definicje, wszystkie **11 dowodów, 4 przykłady**, diagram polar kul jednostkowych, znaczenie separacji punktowo ścisłej i separacji z jednolitą luką, przypadki nie-Hausdorffa, rzeczywiste i zespolone pola skalarów, silną separację przy zwartości/domkniętości, hiperpłaszczyznę podpierającą, polary, twierdzenie bipolarne i domknięcie wypukłe w topologii słabej. Kontrola objęła też odsyłacze do rozdziałów 05–06, terminologię i zgodność LaTeX.

## Kontrola 11 dowodów — 11/11 PASS po doprecyzowaniu

1. **Rzeczywista część funkcjonału zespolonego:** \(\ell=\mathrm{Re}F\) i wzór `F(x)=\ell(x)-i\ell(ix)` uzasadniają liniowość nad \(\mathbb C\), jednoznaczność i ciągłość z ciągłości mnożenia przez `i`. PASS.
2. **Funkcjonał Minkowskiego bez symetrii:** dla otwartego wypukłego otoczenia `V` w rzeczywistej TVS absorbowanie i skończoność `p_V` są poprawne. W oryginalnym tekście brakowało jawnego dowodu podaddytywności poza przypadkiem absolutnie wypukłym. **Uzupełniono:** dla `r>p_V(x)`, `s>p_V(y)` zachodzą `x∈rV`, `y∈sV`; wypukłość daje `x+y∈(r+s)V`. Po infimowaniu `p_V(x+y)≤p_V(x)+p_V(y)`. Dodatnia jednorodność, `V={p_V<1}` i dwustronna kontrola różnic zapewniają ciągłość również dla `V≠−V`. PASS po korekcie.
3. **Separacja punktu od otwartego zbioru wypukłego:** `D=C−x_0`, `V=D−a`, `−a∉V`; przedłużenie `g(t(−a))=t` przez rzeczywisty Hahn–Banach z dominacją `p_V`. Dla ujemnych `t`, `p_V≥0` wystarcza. Funkcjonał jest niezerowy, ciągły i daje \(\ell(c)<\ell(x_0)\) dla każdego `c`. PASS.
4. **Separacja dwóch wypukłych, jeden otwarty:** `D=A−B` jest otwarty, wypukły i nie zawiera 0; separator na `D` implikuje nierówność dla każdej pary `(a,b)`. Z ustalonych `b_0`, `a_0` wynika skończoność `sup_A \ell` i `inf_B \ell`. PASS, bez mylenia separacji punktowej z jednolitą luką.
5. **Wspólne otoczenie zbioru zwartego:** wybór `V_k`, następnie `W_k+W_k⊂V_k`, skończone podpokrycie i wspólne `U⊂∩W_{k_j}`. Przy lokalnej wypukłości wybór otoczeń wypukłych i otwartych jest dopuszczalny. PASS.
6. **Silna separacja zbioru zwartego i domkniętego:** z lematu 5 istnieje otwarte wypukłe `U` z `(A+U)∩B=∅`; otwarta separacja daje \(\ell(a+u)<\ell(b)\). Ponieważ \(\ell\ne0\) i `U` jest otoczeniem, istnieje `u_0∈U` z \(\ell(u_0)>0\), dające stałą lukę. PASS.
7. **Separacja punktu i domkniętego wypukłego:** zastosowanie silnej separacji do jednoelementowego zwartego `A={x_0}` i `B=C`. PASS.
8. **Hiperpłaszczyzna podpierająca:** separacja punktu `x_0∈∂C` od otwartego wypukłego `G=int(C)`, następnie aproksymacja każdego `x∈C` punktami `(1−t)x+tg_0∈G` i przejście do granicy. PASS.
9. **Własności polary:** odwrócenie inkluzji, niezmienność po przejściu do otoczki absolutnie wypukłej, `A⊂A°°`, domkniętość/wypukłość/zrównoważenie względem topologii punktowej i wyjściowej wynikają z przecięć odpowiednich poziomic. PASS.
10. **Twierdzenie bipolarne:** `C=cl(aco(A))` jest niepustym zrównoważonym zbiorem wypukłym; silna separacja `x_0\notin C` dostarcza \(\ell(x_0)>\sup_C\ell\). Reprezentacja przez `Re F` i zrównoważenie `C` dają \(\sup_C|F|=\sup_C\mathrm{Re}F\); odrębnie `m>0` i `m=0` konstruują `G∈A°` wykluczający `x_0`. PASS, także przy `A=∅` z przyjętą `aco(∅)={0}`.
11. **Domknięcie wypukłe w topologii słabej:** topologia słaba jest słabsza od wyjściowej; dla punktu poza domknięciem domknięty zbiór wypukły można silnie oddzielić funkcjonałem `Re F`. Otrzymana półprzestrzeń jest słabo otwarta i nie przecina `C`. Pusty `C` osobno. PASS.

## Kontrola czterech przykładów — 4/4 PASS po uzupełnieniu

1. **Otwartość bez jednolitej luki:** `A=(−1,0)`, `B={0}` z \(\ell(x)=x\): ścisła nierówność dla każdej pary, ale brak dodatniej różnicy między supremum i infimum. PASS.
2. **Polara kuli \(\ell^1\) w \(\mathbb R^2\):** romb jest polarny do kwadratu \(\ell^\infty\) poprzez \(\sup_{\|x\|_1≤1}|\langle a,x\rangle|=\|a\|_\infty\). PASS. Zachowano diagram TikZ.
3. **Polara w produkcie \(\mathbb K^\mathbb N\):** ciągłe funkcjonały zależą tylko od skończenie wielu współrzędnych, a warunki `|a_n|≤1` opisują polarę zbioru wektorów bazowych. `A°°` jest kulą jednostkową \(\ell^1\), rozumianą jako podzbiór produktu. **Doprecyzowano samodzielnie obie inkluzje domknięcia:** sumy częściowe \(\sum_{n=1}^m|x_n|\) są ciągłe w topologii produktowej i \(\le1\) na `aco(A)`, a obcięcia dowolnego `x` z kulą \(\ell^1\) leżą w `aco(A)` i zbiegają współrzędnościowo. PASS po uzupełnieniu.
4. **Brak twierdzenia bipolarnego bez lokalnej wypukłości:** w `L^p`, `0<p<1`, zachodzi `X'={0}`; dla `A={0}` bipolar `X` jest różny od `{0}`. PASS.

## Poprawki matematyczne i redakcyjne

- **Uzupełnienie dowodu podaddytywności niesymetrycznego funkcjonału Minkowskiego:** wcześniejsze odesłanie do przypadku absolutnie wypukłego nie uzasadniało samodzielnie przejścia do ogólnego otwartego zbioru wypukłego.
- **Uzupełnienie dowodu dla domknięcia w przykładzie z produktem:** obie inkluzje wyprowadzone przez skończone sumy i obcięcia, bez opierania się jedynie na zastosowaniu twierdzenia bipolarnego.
- **Terminologia:** zastąpiono „przestrzeń dualna” / „przestrzenie dualne” odpowiednio sformułowaniami „przestrzeń sprzężona” / „przestrzenie sprzężone” w motywacji, definicji polary i zapowiedzi.
- Zachowano **11 środowisk proof, 4 środowiska przykładów, 17 unikatowych etykiet i diagram TikZ**.

## Testy, integracja i CI

- Utworzono `tools/tests/test_functional_analysis_ch07.py` z **16 niezależnymi regresjami**. Modele obejmują niesymetryczny funkcjonał Minkowskiego na \(\mathbb R^2\), rozróżnienie ścisłej separacji punktowej i silnej, wspólne otoczenie dla zwartego zbioru, hiperpłaszczyznę podpierającą, polary \(\ell^1/\ell^\infty\), zrównoważenie w przypadku zespolonym, bipolar produktu i słabą separację wypukłą. Testy stanowią tylko diagnostykę skończenie wymiarowych modeli, a nie formalną weryfikację ogólnych dowodów.
- Utworzono `.github/workflows/functional-analysis-ch07.yml`: dedykowany workflow sprawdzający testy, kontekst `01–07`, kompilację LaTeX oraz końcowy PDF, ostrzeżenia i odsyłacze.
- Struktura: **17/17 etykiet unikatowych, 12 wystąpień odsyłaczy, 0 brakujących celów** w istniejących rozdziałach `01–07`.
- [GitHub Actions 45182375122](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45182375122) obejmuje ostatnią zmianę źródła; etap **16 testów PASS**, przygotowanie kontekstu PASS. Status kompilacji i wynik wizualnego przeglądu PDF zostaną uzupełnione po zakończeniu przebiegu.

## Decyzja

**Audyt 07/01 wykonano z rzeczywistymi poprawkami, więc nie jest czysty (0/2).** Następny audyt powinien ponownie samodzielnie sprawdzić zmienione źródło rozdziału 07; dopiero dwa kolejne czyste audyty pozwolą przejść do rozdziału 08.
