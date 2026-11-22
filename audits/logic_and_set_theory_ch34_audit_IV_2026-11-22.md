# Logika matematyczna i teoria mnogości — audyt IV rozdziału 34

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/34-hipoteza-continuum-i-zastosowania-wymuszania.tex.  
**Charakter:** niezależna ponowna kontrola po korektach z audytu III, w tym alternatywne uzasadnienia kluczowych kroków.

## Wynik matematyczny

**AUDYT IV: bez nowej usterki; tekst matematyczny rozdziału 34 pozostaje niezmieniony.**

### A. Niezależna kontrola decyzji o wartościach porządkowych

W audycie III dowiedziono gęstości zbioru warunków rozstrzygających $\dot f(\check n)$ bez ustalonej wcześniej granicy na wartości. Sprawdziliśmy ten krok jeszcze raz metodą rang nazw:

Niech $\dot f\in M$. Istnieje $\gamma\in\operatorname{Ord}^M$ zależne wyłącznie od nazwy $\dot f$, takie że w każdym rozszerzeniu generycznym $M[H]$ zachodzi
$\operatorname{rank}(\dot f^H)\le\gamma$.
Jeśli $p\Vdash$ „$\dot f$ jest funkcją o dziedzinie $\omega$ i wartościach porządkowych”, to każda wartość $\eta=\dot f^H(n)$ jest liczbą porządkową występującą jako współrzędna pary uporządkowanej należącej do $\dot f^H$. Jej ranga jest więc ściśle mniejsza niż ranga odpowiednio zbudowanego grafu (z ewentualnym przesunięciem o skończoną liczbę kroków). Można wybrać jedną liczbę porządkową $\lambda\in M$ większą od wszystkich możliwych wartości, np. $\gamma+\omega$. Semantyczne twierdzenie o wymuszaniu zapewnia wówczas, że $p$ wymusza wartości $\dot f$ należące do $\check\lambda$. Stosujemy już udowodniony lemat o gęstym rozstrzyganiu **ograniczonych** wartości porządkowych.

Ten alternatywny argument nie wymaga poprawiania oryginalnego dowodu z audytu III; potwierdza jego konkluzję oraz właściwe ograniczanie kwantyfikatorów.

### B. Ccc a zachowanie liczb kardynalnych

Dla dowolnej nieprzeliczalnej liczby kardynalnej $\lambda$ modelu $M$, także osobliwej, i każdego $\beta<\lambda$ analizujemy domniemaną nazwę surjekcji $\dot f:\check\beta\to\check\lambda$. Z gęstości decyzji każdej współrzędnej i ccc uzyskujemy dla każdego $\xi<\beta$ przeliczalny w $M$ zbiór możliwych wartości $S_\xi$. Zastępowanie i AC w $M$ zapewniają rodzinę $(S_\xi)_{\xi<\beta}\in M$. Jej suma ma moc co najwyżej $\max(\aleph_0,|\beta|)<\lambda$. Maksymalne antyłańcuchy są przedgęste poniżej $p$, co zapewnia, że każda generyczna interpretacja $\dot f^H$ przyjmuje wartości ze wskazanej sumy, sprzecznie z surjektywnością.

Ponownie sprawdzono globalizację przedgęstości przez
$E_\xi=\{q:\exists a\in A_\xi\,q\le a\}\cup\{q:q\perp p\}$.
Argument nie wymaga antysymetrii porządku, nie zakłada regularności $\lambda$ ani globalnej przeliczalności $\mathbb P$ w $M$.

### C. Cohen i zaprzeczenie CH

Lemat o systemie $\Delta$ daje ccc dla funkcji częściowych $\kappa\times\omega\to2$ o skończonej dziedzinie. Dla każdego $\alpha<\kappa$ funkcja $c_\alpha(n)=F(\alpha,n)$ należy do $2^\omega\cap M[G]$; jej nośnik jest *odrębnym* podzbiorem $\omega$. Zbiory $D_{\alpha,\beta}$ wymuszają parami różne wartości, a $E_{\alpha,x}$ różnicę pomiędzy $c_\alpha$ a każdym starym ciągiem binarnym $x\in M$.

Dla $\kappa=\omega_2^M$ ccc zachowuje $\omega_2$ i żadna stara liczba porządkowa nie uzyskuje nowego statusu kardynalnego. W $M[G]$ zachodzi więc $2^{\aleph_0}\ge\aleph_2$, a zatem $\neg\mathrm{CH}$.

### D. Przeliczalna domkniętość i CH

Zaczynając **poniżej każdego** $t\le p$ możemy w $M$ rekurencyjnie wybrać warunki rozstrzygające poszczególne wartości nazwanej funkcji $\omega\to\operatorname{Ord}$, a przeliczalna domkniętość daje jedno wspólne wzmocnienie. Daje to zbiór gęsty poniżej $p$, definiowalny w $M$. Generyczność i lemat prawdy dowodzą, że nie pojawiają się nowe ciągi porządkowe długości $\omega$.

Dla pojęcia kolapsu z warunkami o dziedzinach przeliczalnych w $M$, suma malejącego ciągu z $M$ nadal ma w $M$ przeliczalną dziedzinę. Generyczna funkcja $F$ ma dziedzinę $\omega_1^M$ i jest surjekcją na $\lambda=(2^{\aleph_0})^M$. Brak nowych podzbiorów $\omega$ i zachowanie $\omega_1$ pozwalają przenieść starą bijekcję $\lambda\to\mathcal P(\omega)^M$ do rozszerzenia i wykazać w nim CH.

### E. Metamatematyka, język i skład

Niezależnie sprawdzono jawne kwantyfikatory, rozróżnienie modelu zewnętrznie przeliczalnego i wewnętrznej kardynalności, poprawność użycia słowa „suma” w argumentach zbiorowych, wprowadzenie oznaczeń oraz wszystkie odsyłacze. Twierdzenie o dwóch modelach nadal zakłada **istnienie przeliczalnego tranzytywnego modelu zbiorowego ZFC**, nie samą $\operatorname{Con}(\mathrm{ZFC})$. Nie ma podstaw do utożsamienia tego z formalnym dowodem niezależności od samej niesprzeczności.

## Regresje i walidacja

- **16 testów** rozdziału 34: PASS w [GitHub Actions #45039214151](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45039214151).
- Weryfikacje skończone obejmują 16 gęstych podzbiorów i 32 maksymalne antyłańcuchy w drzewie siedmiowarunkowym oraz **29 preorderów na trzech elementach** (wśród nich 16 z największym warunkiem, 138 przypadków gęstości, 231 przypadków maksymalnych antyłańcuchów), bez kontrprzykładu.
- Inwentarz niezmieniony: 5 definicji, 7 lematów, 5 twierdzeń, 2 przykłady, 3 uwagi, 12 dowodów, 23 etykiety, 24 odsyłacze. Książka: 34 rozdziały, 851 etykiet, 640 odsyłaczy.
- **Kompilacja PDF:** PASS; **295 stron**, nowy rozdział na stronach PDF **289–295**. Wizualna inspekcja wszystkich 7 stron: PASS.
- **Log TeX:** 0 błędów, 0 niezdefiniowanych odsyłaczy, 0 brakujących cytowań, 0 przepełnionych wierszy; 1 ostrzeżenie o niedopełnionym wierszu w całej książce.

## Werdykt

**AUDYT IV: PASS, bez zmiany matematycznego tekstu rozdziału 34.**
Weryfikację matematyczną wznowiono niezależną metodą ograniczania rang nazw i ponownie sprawdzono dowody ccc, kolapsu i CH/$\neg$CH.

Jest to **pierwszy czysty audyt po audycie III**, w którym konieczne były poprawki. Zgodnie z regułą stabilności wymagana jest jeszcze **dodatkowa iteracja kontrolna V**. Testy Python, log TeX i przegląd PDF nie są formalnym sprawdzeniem w Lean.
