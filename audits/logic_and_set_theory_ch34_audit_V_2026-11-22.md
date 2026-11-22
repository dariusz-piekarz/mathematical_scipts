# Logika matematyczna i teoria mnogości — audyt V (potwierdzający) rozdziału 34

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Plik:** chapters/pl/logic_and_set_theory/34-hipoteza-continuum-i-zastosowania-wymuszania.tex.  
**Tryb:** dodatkowy pełny audyt stabilności po czystym audycie IV.  
**Źródło matematyczne:** niezmienione od poprawek audytu III.

## Niezależna kontrola wszystkich ogniw argumentu

### 1. Konwencje i istnienie modeli

Wszystkie kardynały i przeliczalność warunków należących do $M$
są rozumiane wewnątrz $M$, zaś przeliczalność samego
tranzytywnego modelu zbiorowego $M$ jest zewnętrzna.
Istnienie filtrów $M$-generycznych o zadanym warunku
wynika z przeliczalności zewnętrznej i twierdzenia
Rasiowej--Sikorskiego. Każde rozszerzenie
$M[G]$ jest tranzytywnym modelem ZFC;
sama niesprzeczność ZFC nie zapewnia
istnienia takiego $M$.

### 2. Ordinalność i karty mocy

Nazwy należące do $M$ mają rangę ograniczoną
przez liczbę porządkową z $M$. Interpretacja
nazwy nie może utworzyć liczby porządkowej
większej od ograniczenia jej rangi,
więc $\operatorname{Ord}^{M[G]}
=\operatorname{Ord}^M$.
Dla ccc niezależnie sprawdzono:
każda potencjalna surjekcja
$f:\beta\to\lambda$ z $\beta<\lambda$
i nieprzeliczalną kardynalną $\lambda$
miałaby przy każdej współrzędnej
co najwyżej przeliczalnie wiele
możliwych wartości w $M$, ponieważ
maksymalny antyłańcuch warunków
rozstrzygających daną współrzędną
jest przeliczalny wewnątrz $M$.
Suma możliwości ma moc
$\max(\aleph_0,|\beta|)<\lambda$
i nie może być całym $\lambda$.
Argument działa bez wymagania
regularności $\lambda$.

Równość $\omega_1^M=\omega_1^{M[G]}$
oraz analogiczna równość dla
$\omega_2$ wynika dodatkowo stąd,
że bijekcje w $M$ pozostają
bijekcjami w $M[G]$, a więc
stare liczby porządkowe
niebędące kardynałami nie stają
się nowymi kardynałami.

### 3. Dwa rozłączne mechanizmy wymuszania

**Cohen / $\neg\mathrm{CH}$.**
Każde $\operatorname{Add}(\omega,\kappa)^M$
spełnia ccc; lemat o systemie $\Delta$
wraz ze zgodnością na rdzeniu skończonej
dziedziny daje sprzeczność z istnieniem
nieprzeliczalnego antyłańcucha.
Dla każdej $\alpha<\kappa$
istnieje funkcja $c_\alpha:\omega\to2$,
niebędąca elementem $M$.
Funkcja jest obiektem różnym od
podzbioru $\omega$ kodowanego przez
zbiór jej współrzędnych o wartości 1.
Gęste zbiory $D_{\alpha,\beta}$
zapewniają, że ciągi są parami różne.
Dla $\kappa=\omega_2^M$ ccc
zapewnia zachowanie $\omega_2$ i
$2^{\aleph_0}\ge\aleph_2$.

**Kolaps / $\mathrm{CH}$.**
W pojęciu częściowych funkcji
$\omega_1^M\to\lambda$ z wewnętrznie
przeliczalnymi dziedzinami
malejący ciąg warunków z $M$
ma dolne ograniczenie będące
ich sumą. W modelu $M[G]$
nie powstają nowe funkcje
$\omega\to\operatorname{Ord}$,
a więc nie powstają nowe
podzbiory $\omega$ oraz
$\omega_1$ zostaje zachowana.
Jednocześnie generyczna suma
warunków daje surjekcję
$\omega_1^M\to\lambda$.
Dla $\lambda=(2^{\aleph_0})^M$
stara bijekcja
$\lambda\to\mathcal P(\omega)^M$
pozostaje bijekcją na
$\mathcal P(\omega)^{M[G]}$,
co implikuje CH.

Sprawdzono obie możliwości
stanu początkowego $M$:
$M\models\mathrm{CH}$ i
$M\models\neg\mathrm{CH}$.
Żaden z dwóch dowodów
nie wymaga założenia,
że $M$ spełnia z góry
jedną z tych alternatyw.

### 4. Dwa uzasadnienia decydowania liczb porządkowych

Sprawdzono poprawność oryginalnego
argumentu z audytu III, opartego na
gęstym zbiorze warunków rozstrzygających
nazwaną wartość porządkową bez
założenia jej zakresu.
Następnie niezależnie zweryfikowano
redukcję tego argumentu do zakresu
ograniczonego rangą jednej ustalonej
nazwy, opisaną w audycie IV.
Obie metody prowadzą do tego
samego stwierdzenia o gęstości
poniżej każdego $p$.

Przy przeliczalnej domkniętości
kluczowe jest, że rekurencję
rozstrzygającą cały ciąg
rozpoczyna się poniżej
**dowolnego** $t\le p$;
pozwala to zastosować lokalną
generyczność do definiowalnego
w $M$ zbioru warunków $q$
wymuszających
$\dot f=\check g$ dla $g\in M$.
Sam wybór jednego wspólnego
ograniczenia poniżej $p$
nie byłby wystarczający.

### 5. Terminologia, odsyłacze, LaTeX i testy

- Nie wykryto niejawnego utożsamienia
  funkcji i zbiorów, zapomnianych
  parametrów modelu, błędnych
  kwantyfikatorów ani nowych luk
  w przesłankach twierdzeń.
- Odsyłacze do rozdziałów
  31–33 są prawidłowe, bez
  niezdefiniowanych etykiet.
- Rozdział nie zawiera rysunków
  wymagających osobnego audytu
  rozmieszczenia podpisów.
- **16 testów** w
  tools/tests/test_logic_and_set_theory_ch34.py,
  wszystkie PASS w
  [GitHub Actions #45039214151](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45039214151).
  Przetestowano między innymi
  29 preorderów na zbiorze
  trójelementowym, 138 lokalnie
  gęstych konfiguracji i
  231 maksymalnych antyłańcuchów
  bez kontrprzykładu.
- W książce nadal **34 rozdziały,
  851 etykiet i 640 odsyłaczy**.
  Rozdział 34: 23 etykiety,
  24 odsyłacze, 5 definicji,
  7 lematów, 5 twierdzeń,
  2 przykłady, 3 uwagi i 12 dowodów.
- PDF zawiera **295 stron**, a
  rozdział 34 strony PDF
  **289–295**. Ponowna wizualna
  kontrola siedmiu stron bez
  kolizji tekstu i wzorów.
  Log: 0 błędów, 0 nierozwiązanych
  odsyłaczy, 0 ostrzeżeń
  o przepełnionych wierszach,
  1 ostrzeżenie o niedopełnionym
  wierszu w całej książce.

## Ostateczny werdykt

**STABILNY PO V AUDYTACH.**
Audyty I–III wykrywały błędy
i niedostateczne uzasadnienia,
które poprawiono w repozytorium.
**Audyt IV był czysty, a audyt V
jest dodatkowym czystym audytem
potwierdzającym**. Nie zmieniano
w nich źródła matematycznego.
W ten sposób spełniono kryterium
stabilności oraz dodatkowej
iteracji weryfikacyjnej.

Należy odróżnić ten status
od formalnej weryfikacji w Lean:
testy Python, GitHub Actions
i przegląd PDF nie są
dowodem formalnym. Ponadto
ostateczny wynik o niezależności
CH względem samej niesprzeczności
ZFC wymaga osobnego argumentu
metamatematycznego i nie został
nieuczciwie przypisany temu
rozdziałowi.

**Stan:** rozdział 34 stabilny
w zakresie jego sformułowanych
twierdzeń modelowych i wymuszania
CH/$\neg\mathrm{CH}$.
