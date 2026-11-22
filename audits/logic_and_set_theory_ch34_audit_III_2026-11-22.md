# Logika matematyczna i teoria mnogości — audyt III rozdziału 34

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Plik:** `chapters/pl/logic_and_set_theory/34-hipoteza-continuum-i-zastosowania-wymuszania.tex`.  
**Cel:** kolejny niezależny audyt matematyczny i redakcyjny po audycie II, z naciskiem na definicje nazw, gęstość, wybór antyłańcuchów i domkniętość. **Status: po korektach, przed niezależnym audytem IV.**

## Zmiany merytoryczne

### 1. Funkcja binarna a podzbiór $\omega$

Poprzedni dowód twierdzenia o wielu ciągach Cohena definiował
$c_\alpha:\omega\to\{0,1\}$, a następnie nazywał $c_\alpha$
„podzbiorem $\omega$”. To nie jest dosłowna równość obiektów w ZFC:
funkcja jest zbiorem par uporządkowanych, natomiast jej **nośnik**
$A_\alpha=\{n\in\omega:c_\alpha(n)=1\}$ jest podzbiorem $\omega$.

**Poprawka źródła:** wyjaśniono, że funkcja $c_\alpha$ jest elementem
$2^\omega\cap M[G]$: ograniczamy funkcję generyczną
$F:\kappa\times\omega\to2$ do współrzędnej $\alpha$,
korzystając z wyróżniania i zastępowania w $M[G]$. Następnie podano
jawny zbiór $A_\alpha$ i naturalne utożsamienie
$2^\omega\cong\mathcal P(\omega)$. Nie zmieniono
poprawnych dowodów $c_\alpha\ne c_\beta$ oraz $c_\alpha\notin M$.

### 2. Gęstość rozstrzygania wartości porządkowych bez górnego ograniczenia

W lemacie o tym, że przeliczalnie domknięte wymuszanie nie dodaje
nowych ciągów porządkowych, pierwsze uzasadnienie gęstości
warunków decydujących wartość $\dot f(\check n)$ odsyłało
do lematu o **ustalonym** przedziale wartości $\eta<\lambda$.
W przypadku funkcji $\omega\to\operatorname{Ord}$ górne
ograniczenie nie zostało założone. Choć argument można uzupełnić,
dla przyjętego standardu szczegółowości był to istotny przeskok.

**Poprawka źródła:** dla dowolnego $n\in\omega$ zdefiniowano
w modelu $M$ zbiór
\[
 D_n=\{r\le p:\exists\eta\,
 (\operatorname{Ord}(\eta)\land
 r\Vdash \dot f(\check n)=\check\eta)\}.
\]
Przynależność $D_n$ do $M$ wynika z wyróżniania
oraz definiowalności wymuszania dla ustalonej formuły
i definowalności konstrukcji $\check\eta$.
Gdyby $D_n$ nie był gęsty poniżej $p$,
istniałby $t\le p$, poniżej którego nikt nie rozstrzyga wartości.
Wybieramy filtr $M$-generyczny $H\ni t$.
Wtedy $\dot f^H(n)$ jest liczbą porządkową w $M[H]$;
lemat o zachowaniu liczb porządkowych dowodzi, że
$\dot f^H(n)=\eta$ dla pewnego $\eta\in M$.
Lemat prawdy daje $r\in H$ wymuszające równość z
$\check\eta$. Wspólne wzmocnienie $r$ i $t$ jest
elementem $D_n$, sprzecznie z wyborem $t$.
To dowodzi gęstości bez ukrytego założenia o stałej $\lambda$.

Pozostała część dowodu, poprawiona w audycie II,
konstruuje **dla dowolnego $t\le p$** warunek
$q\le t$ wymuszający $\dot f=\check g$ dla pewnego $g\in M$,
a następnie stosuje generyczność do zbioru takich warunków
gęstego poniżej $p$.

## Ponowna kontrola pozostałych twierdzeń

1. **Rangi nazw i liczby porządkowe.** Każda nazwa $\tau\in M$
   ma w $M$ ograniczenie rangi; jej interpretacja $\tau^G$
   nie może mieć rangi większej niż odpowiednie ograniczenie.
   Zatem nie ma nowych liczb porządkowych w $M[G]$.
2. **System $\Delta$ i ccc.** Lemat o systemie $\Delta$
   jest przeprowadzony przez indukcję po liczbie elementów
   skończonych zbiorów. W przypadku funkcji częściowych
   zgodność wartości na rdzeniu daje wspólne wzmocnienie,
   a więc $\operatorname{Add}(\omega,\kappa)^M$ spełnia ccc w $M$.
3. **Zachowanie kardynałów.** Dla domniemanej surjekcji
   $f:\beta\to\lambda$, gdzie $\beta<\lambda$ i $\lambda$
   jest dawnym kardynałem nieprzeliczalnym, wybrano
   w $M$ maksymalne antyłańcuchy $A_\xi$ w gęstych
   zbiorach warunków decydujących $f(\xi)$.
   Każdy $A_\xi$ jest przedgęsty poniżej $p$ i
   przeliczalny w $M$. Stąd zbiór $S$ wszystkich
   możliwych wartości ma moc
   $|S|\le\max(\aleph_0,|\beta|)<\lambda$,
   co przeczy surjektywności. Dowód nie zakłada
   regularności $\lambda$.
4. **Ciągi Cohena i $\neg\mathrm{CH}$.**
   Dla różnych $\alpha,\beta$ gęste zbiory
   $D_{\alpha,\beta}$ rozdzielają $c_\alpha,c_\beta$.
   Dla każdego $x\in(2^\omega)^M$ gęste
   zbiory $E_{\alpha,x}$ świadczą o nowości
   każdego $c_\alpha$. Zachowanie $\omega_2^M$
   przez ccc daje $2^{\aleph_0}\ge\aleph_2$.
5. **Kolaps i CH.** Pojęcie funkcji częściowych
   $\omega_1^M\to\lambda$ o wewnętrznie
   przeliczalnych dziedzinach jest przeliczalnie
   domknięte w $M$. Nie dodaje nowych funkcji
   $\omega\to\operatorname{Ord}$, a więc nie zmienia
   $\mathcal P(\omega)$ ani $\omega_1$.
   Generyczna suma warunków jest surjekcją
   $\omega_1^M\to\lambda=(2^{\aleph_0})^M$,
   co zapewnia CH.
6. **Status niezależności.** Konstrukcja dwóch
   rozszerzeń z CH oraz $\neg\mathrm{CH}$ jest
   warunkowa względem istnienia przeliczalnego
   tranzytywnego modelu ZFC; nie utożsamia
   się tego z samą $\operatorname{Con}(\mathrm{ZFC})$.

## Wzmocnienie regresji

Dodano dwa testy do
`tools/tests/test_logic_and_set_theory_ch34.py`:
- **Wyczerpujący przegląd maksymalnych antyłańcuchów.**
  Dla wszystkich 7 warunków skończonego drzewa, wszystkich
  podzbiorów gęstych poniżej danego warunku i wszystkich
  maksymalnych antyłańcuchów zawartych w takich podzbiorach
  sprawdzono przedgęstość oraz gęstość zbioru
  $E=\{q:\exists a\in A\,q\le a\}\cup I_p$.
  Test objął **16 zbiorów gęstych i 32 maksymalne antyłańcuchy**,
  a także przecięcia z filtrami odpowiadającymi wszystkim
  czterem gałęziom końcowym.
- **Typowanie ciągów Cohena.** Dla wszystkich 32
  funkcji binarnych na zbiorze pięcioelementowym
  sprawdzono rekonstrukcję funkcji z jej nośnika i
  zapisano warunek regresyjny zabraniający
  traktowania obu obiektów jako dosłownie równych.

**Zestaw regresji rozdziału 34:** 15 testów.
**Inwentarz rozdziału:** 5 definicji, 7 lematów,
5 twierdzeń, 2 przykłady, 3 uwagi, 12 dowodów,
23 etykiety i **24 odsyłacze**.
**Inwentarz całej książki:** 34 rozdziały,
851 etykiet i **640 odsyłaczy**.

## Walidacja techniczna i decyzja

GitHub Actions: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45038983380

Wynik końcowy CI i przeglądu PDF zostanie dopisany
po rzeczywistym zakończeniu kompilacji.

**Werdykt matematyczny:** wykryto i poprawiono
dwa miejsca wymagające zmian, dlatego audyt III
**nie jest czystą iteracją**. Rozdział nie otrzymuje
jeszcze statusu „stabilny”; następnym krokiem
pozostaje audyt IV, a po uzyskaniu stabilności
należy przeprowadzić dodatkowy audyt potwierdzający.
