# Miara i całka — audyt XVIII: rozdział 04, kontrola II

**Data:** 2026-11-23  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`  
**Weryfikowany blob:** `77e4ad8551f55a2ff579aa171761ccdd01aaa918`

## Zakres i metoda

Niezależny przegląd po poprawce z audytu XVII, wyłącznie R04. Ponownie odczytano raport XVII i aktualny plik źródłowy bez użycia poprzedniego streszczenia jako substytutu tekstu. Sprawdzono poniższe łańcuchy wnioskowania.

1. **Skończona siatka i addytywność objętości.** Wspólne rozdrobnienie dla skończenie wielu ograniczonych prostopadłościanów półotwartych zapewnia niezależność sumy od przedstawienia; pusta rodzina nie powoduje problemu, bo pusty zbiór jest w pierścieniu.
2. **Nierówność dla pokryć.** Zwarty rdzeń K_delta leży we wnętrzu Q. Po zastąpieniu pokrycia otwartymi prostopadłościanami zwartość daje skończone podpokrycie. Po poprawce XVII przypadek zdegenerowanego K jest rozdzielony; dla niezerowych boków komórki P_eta można przypisać do otwartych prostopadłościanów, a domknięcia komórek mieszczą się w domknięciach przypisanych O_i. Przejścia gamma→0, eta→0, delta→0, epsilon→0 zachowują kierunki nierówności.
3. **Premiara lokalna.** Dla rozłącznego A=⊔A_n w pierścieniu skończonej sumy prostokątów dolne oszacowanie pochodzi ze skończonej addytywności, górne z lematu o pokryciach. H ma skończoną objętość; jednoznaczność przedłużenia jest stosowana w przypadku miary skończonej.
4. **Miara zewnętrzna i mierzalność.** Przecięcia R_n∩Q i rozkłady R_n\\Q zachowują sumę objętości. Przejście do infimum daje właściwą stronę nierówności Carathéodory'ego. Układ π prostokątów i wyczerpanie [-n,n)^d uzasadniają jednoznaczność borelowską.
5. **Niezmienniczość.** Translacje zachowują rodzinę pokryć; dla t<0 trzeba powiększyć obrazy przedziałów (lewootwartych, prawodomkniętych) do półotwartych, rozdzielając błąd na pokrycie przeliczalne. Odwrotne przekształcenie zapewnia równość. Przeniesienie kryterium Carathéodory'ego przez bijekcję uzasadnia mierzalność obrazu.
6. **Regularność.** Dla zbiorów o skończonej mierze aproksymacja otwartymi nadzbiorami ma dowolnie mały błąd; dla miary nieskończonej formuła infimum jest automatyczna. Przy aproksymacji od wewnątrz użyto wyczerpania zwartymi sześcianami i regularności zewnętrznej dopełnienia w sześcianie. Przy aproksymacjach borelowskich rozdzielenie E na części skończonej miary pozwala skonstruować G_delta i F_sigma o różnicy miary zero.
7. **Przykłady.** Wykres Lipschitzowski: suma pól osłon jest rzędu O(1/N). Zbiór Cantora: miara ≤(2/3)^n, a kodowanie cyframi 0/2 jest jednoznaczne; konstrukcja Smitha–Volterry–Cantora: długość przedziału na etapie n wynosi 2^(-n-1)+2^(-2n-1), suma usuniętych długości =1/2. Funkcja Cantora: przyrosty na 2^n przedziałach składowych sumują się do 1 przy ich łącznej długości (2/3)^n. Vitali: rozłączne przesunięcia przez Q∩[-1,1] i ograniczenie sumy do [-1,2] wykluczają każdą wartość miary V.

## Ustalenia

**Nie znaleziono nowej wykazanej usterki matematycznej w przeprowadzonym przeglądzie.** W szczególności poprawka z XVII nie wymaga cofnięcia ani kolejnej redakcji. W tej iteracji **nie zmieniano R04**; jego blob pozostaje `77e4ad8551f55a2ff579aa171761ccdd01aaa918`.

**Weryfikacja techniczna jest nadal niepełna:** nie uruchomiono kompilatora LaTeX ani pełnego CI, nie skontrolowano pliku PDF i położenia napisów na rysunku TikZ Cantora. Nie deklaruje się PASS dla tych kontroli. Próba odczytu standardowych nazw workflow `.github/workflows/latex.yml` i `.github/workflows/ci.yml` dała 404; nie oznacza to braku workflow pod innymi nazwami.

## Decyzja

**R04: audyt matematyczny II bez nowych poprawek; stabilność całości nadal NIEPOTWIERDZONA.** Kontynuować wyłącznie R04, ze szczególnym naciskiem na rzeczywisty build, odsyłacze i wizualny przegląd PDF. Nie przechodzić do R05.
