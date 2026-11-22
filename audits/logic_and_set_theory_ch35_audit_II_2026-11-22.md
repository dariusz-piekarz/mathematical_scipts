# Logika matematyczna i teoria mnogości — audyt II rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Cel:** niezależna ponowna kontrola modeli o wartościach boolowskich, ze szczególną uwagą na ufundowanie, zbiór potęgowy, zastępowanie, lemat pełności, iloraz przez ultrafiltr i względną niesprzeczność CH oraz jej zaprzeczenia.

## Najważniejsze usterki matematyczne

### 1. Niewystarczająca minimalizacja rang w dowodzie ufundowania

W pierwszej wersji argument o minimalnym elemencie nazwy $\sigma$ wybrał najmniejszą rangę wśród współrzędnych $\operatorname{dom}\sigma$. Nie było to wystarczające: nazwa elementu należącego do wybranego zbioru $\pi$, a równocześnie reprezentująca element $\sigma$, może **nie być dosłownie żadną nazwą ze zbioru $\operatorname{dom}\sigma$**. Może być jedynie równa boolowsko pewnej nazwie z tej dziedziny. Z samej minimalności rangi w $\operatorname{dom}\sigma$ nie wynika wówczas sprzeczność.

**Poprawka:** dla dowolnego $0<c\le b=\llbracket\sigma\ne\varnothing\rrbracket$ rozpatrujemy *wszystkie* nazwy $\pi$ spełniające
$c\wedge\llbracket\pi\in\sigma\rrbracket>0$. Zbiór nazw z $\operatorname{dom}\sigma$ zapewnia co najmniej jednego świadka. Minimalizujemy rangę w **definiowalnej klasie wszystkich dopuszczalnych nazw**, której minimum istnieje dzięki ograniczeniu przez rangę jednego świadka. Dla wybranego $\pi$ definiujemy $d=c\wedge\llbracket\pi\in\sigma\rrbracket>0$.

Jeżeli na niezerowym fragmencie $e\le d$ istniałby element wspólny $\rho$ zbiorów $\pi$ i $\sigma$, klauzula atomowej przynależności do $\pi$ dostarczyłaby $\eta\in\operatorname{dom}\pi$ z dodatnią wartością
\[
 e\wedge\pi(\eta)\wedge
 \llbracket\rho=\eta\rrbracket\wedge
 \llbracket\rho\in\sigma\rrbracket.
\]
Podstawianie dałoby $c\wedge\llbracket\eta\in\sigma\rrbracket>0$, sprzecznie z $\operatorname{rk}(\eta)<\operatorname{rk}(\pi)$. Stąd $d$ wymusza, że $\pi\in\sigma$ i $\pi\cap\sigma=\varnothing$. Fragmenty $d$ są gęste poniżej $b$. Maksymalny antyłańcuch oraz lemat mieszania sklejają lokalnych świadków w jedną nazwę minimalnego elementu na całym fragmencie $b$. Poprawka zamyka lukę i uzasadnia wartość boolowską $1$ aksjomatu ufundowania.

### 2. Zbyt skrótowa konstrukcja zbioru potęgowego

Pierwsza wersja twierdziła, że dla dowolnej nazwy $\tau$ i $b=\llbracket\tau\subseteq\sigma\rrbracket$ z ekstensjonalności wynika $b\le\llbracket\tau=f_\tau\rrbracket$, ale brakowało dowodu równości przynależności dla wszystkich nazw argumentów.

**Poprawka:** w modelu wyjściowym definiujemy **zbiór**
\[
T_\sigma=\{f:D\to\mathbb B:
 \forall\rho\in D\ f(\rho)\le\sigma(\rho)\},\qquad
D=\operatorname{dom}\sigma,
\]
i nazwę $\Pi_\sigma$ o dziedzinie $T_\sigma$, przyjmującą wartość $1$ na każdym jego elemencie. Dla $f\in T_\sigma$ sprawdzamy bezpośrednio $\llbracket f\subseteq\sigma\rrbracket=1$ przez klauzulę atomową. Dla dowolnej nazwy $\tau$ tworzymy $f_\tau(\rho)=\sigma(\rho)\wedge\llbracket\rho\in\tau\rrbracket$. Po rozpisaniu $\llbracket\eta\in f_\tau\rrbracket$ i użyciu podstawiania udowadniamy dla każdej nazwy $\eta$ dwa kierunki nierówności boolowskich na fragmencie $b$. Ekstensjonalność daje
$b\le\llbracket\tau=f_\tau\rrbracket$ i ostatecznie
\[
\llbracket\tau\in\Pi_\sigma\rrbracket
=\llbracket\tau\subseteq\sigma\rrbracket.
\]
Poprawka jawnie odróżnia zewnętrzne równości nazw-funkcji od równości wymuszanej boolowsko.

### 3. Niedostatecznie uzasadniony schemat zastępowania

Pierwsza wersja tworzyła nazwę obrazu ze świadków $\rho_\pi$ i współczynników $\sigma(\pi)$, nie rozwijając obu kierunków implikacji opisującej obraz na fragmencie, na którym $\varphi$ jest funkcjonalna.

**Poprawka:** dla
$b=\llbracket\forall x\in\sigma\ \exists!y\,\varphi(x,y,\vec\tau)\rrbracket$
z lematu pełności wybieramy dla każdego $\pi\in\operatorname{dom}\sigma$ świadka $\rho_\pi$. Zbiór świadków uzyskujemy przez ograniczenie minimalnych rang i zastosowanie wyboru **na zbiorze**, nie klasie właściwej. Definiujemy
\[
R_\sigma(\rho)=
\bigvee\{\sigma(\pi):
 \pi\in\operatorname{dom}\sigma,\ \rho_\pi=\rho\}
\]
dla nazw $\rho$ należących do zbioru wybranych świadków. W audytowanym dowodzie rozpisałem oba kierunki równości
\[
b\wedge\llbracket\eta\in R_\sigma\rrbracket
=b\wedge\llbracket\exists x\in\sigma\
 \varphi(x,\eta,\vec\tau)\rrbracket
\]
dla każdej nazwy $\eta$. Kierunek zwrotny używa jednoznaczności świadka pod fragmentem $b\wedge\sigma(\pi)$ oraz podstawiania w równości nazw. Jest to potrzebny dowód instancji zastępowania, a nie samo wskazanie konstrukcji.

### 4. Niejawna definicja rangi nazw boolowskich

Doprecyzowano oznaczenie
\[
\operatorname{rk}(\tau)=
\min\{\alpha:\tau\in V_{\alpha+1}^{\mathbb B}\}
\]
i podano jawnie, że dla $\eta\in\operatorname{dom}\tau$ zachodzi $\operatorname{rk}(\eta)<\operatorname{rk}(\tau)$. To ważna przesłanka poprawionego dowodu ufundowania i rekurencji atomowych wartości boolowskich.

## Kontrola pozostałych argumentów

- **Lemat mieszania i pełności:** konstrukcje zależą od *zbioru* indeksów antyłańcucha i ograniczenia rang świadków, nie wymagają wyboru z klasy właściwej. Egzystencjalna wartość logiczna jest kresem zbioru wartości zawartego w $\mathbb B$, choć przebiega się klasę wszystkich nazw.
- **Uzupełnienie boolowskie:** obraz stożków jest gęsty w algebrze zbiorów regularnie otwartych. Równoważne warunki preorderu nie muszą mieć różnych obrazów.
- **Iloraz przez ultrafiltr:** relacja równości nazw modulo $U$ jest relacją równoważności, a przynależność nie zależy od reprezentantów. Lemat prawdy używa dla egzystencji *lematu pełności*, dlatego działa dla dowolnego ultrafiltru — bez założenia generyczności.
- **Względna niesprzeczność:** model zbiorowy ZFC z twierdzenia o pełności logiki pierwszego rzędu może być nietranzytywny i zewnętrznie źle ufundowany; modele ilorazowe nadal spełniają wszystkie standardowe aksjomaty ZFC. Rozdział oddziela wewnętrzną zupełność algebry w $M$ od jej zupełności zewnętrznej i nie stosuje nieuzasadnionego kolapsu Mostowskiego.

## Testy i regresje

Dodano **3 nowe testy** do tools/tests/test_logic_and_set_theory_ch35.py (łącznie **14**):

1. **Zbiór potęgowy:** 64 małe nazwy i oba ultrafiltry główne czteroelementowej algebry Boole'a — **128 kontroli** zgodności przynależności do nazwy potęgi z rzeczywistym zawieraniem się interpretacji; dodatkowo sprawdzenie reprezentanta $f_\tau$.
2. **Ufundowanie i minimalna ranga:** wszystkie 256 czterowspółrzędnych nazw testowych, w dwóch interpretacjach boolowskich. Wśród nich znajduje się nazwa wyższej rangi równoważna pustej nazwie, której minimalny rangą reprezentant **nie występuje w oryginalnej dziedzinie** — przypadek istotny dla wykrytej luki.
3. **Zastępowanie:** 64 nazwy i dwa ultrafiltry, łącznie **128 kontroli** obrazu funkcji $x\mapsto\{x\}$.

Pierwszy przebieg nowego zestawu wykrył wyłącznie **błąd reprezentacji danych w teście Python**: próbowano umieścić zwykły mutowalny zbiór w zbiorze niemutowalnym. Zamieniono go na `frozenset({x})` i uruchomiono testy ponownie. Nie był to kontrprzykład matematyczny.

**Inwentarz źródeł:** 35 rozdziałów; rozdział 35 nadal zawiera 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 etykiet i 30 odsyłaczy. Cała książka nadal ma 879 etykiet i 670 odsyłaczy.

## Walidacja CI / PDF i status

- Wcześniejsza wersja po poprawie ufundowania: [GitHub Actions #45041914542](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041914542) — **SUCCESS**, bez nowych testów.
- Przebieg z rozszerzonymi testami: [GitHub Actions #45042054880](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45042054880) — **FAIL**, wyłącznie z powodu wskazanej wyżej niehashowalnej struktury testowej.
- Aktualny przebieg: [GitHub Actions #45042143249](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45042143249) — wynik końcowy kompilacji i PDF zostanie wpisany po ukończeniu.

**Werdykt matematyczny:** audyt II wykrył istotną lukę dowodową w aksjomacie ufundowania oraz poważne przeskoki w zbiorze potęgowym i zastępowaniu. W źródle wszystkie trzy dowody rozbudowano i poprawiono. Rozdział 35 **nie jest stabilny**: konieczny jest niezależny audyt III, a potem dalsze iteracje do uzyskania czystego audytu i dodatkowego audytu potwierdzającego. Testy Python i CI nie są formalną weryfikacją w Lean.
