# Logika matematyczna i teoria mnogości — audyt II rozdziału 34

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/logic_and_set_theory/34-hipoteza-continuum-i-zastosowania-wymuszania.tex`.  
**Cel:** powtórna, niezależna kontrola matematyczna i redakcyjna twierdzeń o ccc, przeliczalnej domkniętości oraz wymuszaniu CH i jej zaprzeczenia.

## Najważniejsze wykryte luki i ich poprawki

### 1. Gęstość warunków rozstrzygających cały ciąg

W pierwotnej wersji dowodu lematu `lem:forcing34-closed-no-sequences` konstruowano jedno wspólne wzmocnienie $q\leq p$ ustalające cały ciąg, a następnie stwierdzano, że **zbiór takich warunków jest gęsty poniżej $p$**. Istnienie jednego warunku poniżej $p$ nie uzasadnia gęstości.

**Rzeczywista poprawka:** konstrukcja odbywa się dla **każdego** $t\leq p$. Wewnątrz $M$ wybiera się malejący ciąg warunków $(p_n)$ z $p_0=t$ i wartości $\gamma_n$ decydujące $\dot f(\check n)$; przeliczalna domkniętość daje $q\leq p_n$ dla wszystkich $n$, a zastępowanie tworzy $g=(\gamma_n)\in M$. Ponieważ $p$ wymusza dziedzinę $\omega$, interpretacje $\dot f$ i $\check g$ są równe w **każdym** generycznym rozszerzeniu zawierającym $q$. Z semantycznej części twierdzenia o wymuszaniu wynika $q\Vdash\dot f=\check g$.

Następnie jawnie definiuje się w $M$
\[
D=\{q\leq p:\exists g\,
(g:\omega\to\operatorname{Ord}\land q\Vdash\dot f=\check g)\}.
\]
Operacja $g\mapsto\check g$ i relacja wymuszania ustalonej formuły są definiowalne, więc $D\in M$ przez wyróżnianie. Ponieważ konstrukcja działa poniżej **dowolnego** $t\leq p$, $D$ jest gęsty poniżej $p$. Dopiero po tym stosuje się lemat lokalnej generyczności do uzyskania $G\cap D\ne\varnothing$. Otrzymujemy $f\in M$ bez błędnego koła.

### 2. Istnienie i jednoczesny wybór maksymalnych antyłańcuchów

W dowodzie `thm:forcing34-ccc-preserves` uściślono, co oznacza maksymalność antyłańcucha $A_\xi\subseteq D_\xi$ oraz dlaczego jest on **przedgęsty poniżej $p$**.

**Rzeczywista poprawka:** w $M$ zastosowano lemat Kuratowskiego--Zorna do antyłańcuchów zawartych w gęstym zbiorze $D_\xi$. Maksymalny antyłańcuch w $D_\xi$ jest przedgęsty poniżej $p$: dla dowolnego $r\leq p$ istnieje $d\in D_\xi$ z $d\leq r$; maksymalność antyłańcucha zapewnia zgodność $d$ z pewnym $a\in A_\xi$, a zatem również zgodność $r$ z $a$. Ponieważ $\xi$ przebiega **zbiór** $\beta$, aksjomat wyboru w $M$ umożliwia jednoczesne utworzenie rodziny $(A_\xi)_{\xi<\beta}\in M$.

Pozostała część dowodu — zbiory potencjalnych wartości $S_\xi$, ich oszacowanie $|\bigcup_{\xi<\beta}S_\xi|\leq\max(\aleph_0,|\beta|)<\lambda$ oraz sprzeczność z surjektywnością $\beta\to\lambda$ — nie wymagała zmiany. Oszacowanie działa również dla **osobliwych** nieprzeliczalnych kardynałów $\lambda$.

### 3. Brak powstawania nowych kardynałów

Samo zachowanie starych kardynałów i liczb porządkowych nie wyjaśniało explicite, dlaczego w rozszerzeniu nie mogą „pojawić się” nowe kardynały wśród starych liczb porządkowych.

**Poprawka:** każda bijekcja istniejąca w $M$ pomiędzy liczbą porządkową $\alpha$ a mniejszą liczbą porządkową pozostaje bijekcją w $M[G]$. Zatem ordinal niebędący kardynałem w $M$ nie staje się kardynałem w $M[G]$. W połączeniu z zachowaniem wszystkich kardynałów $M$ i brakiem nowych liczb porządkowych daje to równość $\omega_1^{M[G]}=\omega_1^M$ i $\omega_2^{M[G]}=\omega_2^M$.

## Kontrola pozostałych konstrukcji

1. **System $\Delta$ i ccc Cohena:** dwa warunki z odpowiednimi skończonymi dziedzinami i zgodnymi wartościami na wspólnym rdzeniu mają wspólne wzmocnienie. Żaden wewnętrzny antyłańcuch $\operatorname{Add}(\omega,\kappa)^M$ nie jest nieprzeliczalny w $M$.
2. **Nowe ciągi Cohena:** zbiory $D_{\alpha,\beta}$ zapewniają parami różne ciągi, a zbiory $E_{\alpha,x}$ — nowość każdego ciągu względem wszystkich $x\in(2^\omega)^M$.
3. **Brak nowych ciągów porządkowych:** nowy dowód oddziela wybranie pojedynczego dolnego ograniczenia od wykazania gęstości odpowiedniej klasy warunków wewnątrz $M$.
4. **Kolaps i CH:** $\operatorname{Coll}(\omega_1,\lambda)^M$ jest przeliczalnie domknięte, zachowuje $\mathcal P(\omega)$ i $\omega_1$, a suma generyczna jest surjekcją $\omega_1^M\to\lambda$ dla $\lambda=(2^{\aleph_0})^M$. To pozwala uzyskać CH także z modelu wyjściowego zaprzeczającego CH.
5. **Metamatematyka:** twierdzenie o dwóch modelach CH/$\neg\mathrm{CH}$ pozostaje warunkowe względem istnienia przeliczalnego tranzytywnego modelu ZFC. Nie utożsamiono go z pełnym twierdzeniem o względnej niesprzeczności względem samej $\operatorname{Con}(\mathrm{ZFC})$.

## Testy i inwentarz

W pliku `tools/tests/test_logic_and_set_theory_ch34.py` dodano **dwa testy regresyjne** (łącznie **13**):

- Wyliczenie wszystkich 81 częściowych funkcji z trzech współrzędnych do $\{0,1\}$ i sprawdzenie dla trzech współrzędnych, że dwuelementowe antyłańcuchy rozstrzygające wartości są maksymalne, przedgęste i poprawnie spotykane przez osiem filtrów odpowiadających całkowitym funkcjom.
- Dla wszystkich 81 częściowych funkcji na czterech współrzędnych test sprawdza możliwość skonstruowania malejącego ciągu wzmocnień i końcowego warunku rozstrzygającego wszystkie współrzędne, **startując poniżej dowolnego warunku**.

Te testy są ograniczonymi przypadkami obliczeniowymi, nie zastępują dowodów matematycznych ani formalizacji w Lean.

**Inwentarz rozdziału po korekcie:** 5 definicji, 7 lematów, 5 twierdzeń, 2 przykłady, 3 uwagi, 12 dowodów, 23 etykiety, **23 odsyłacze**. W całej książce 34 rozdziały, 851 etykiet i **639 odsyłaczy**.

## CI, skład i werdykt

- [GitHub Actions #45023245896](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023245896): **SUCCESS** — 13 testów rozdziału 34, regresje pozostałych rozdziałów, kontrola katalogu i inwentarza, kompilacja oraz analiza logu.
- [GitHub Actions #45023370260](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023370260): **SUCCESS** również po zapisaniu niniejszego raportu; nie modyfikowano źródła matematycznego między tymi przebiegami.
- **PDF całej książki:** **295 stron**; rozdział 34 na stronach PDF **289–295** (drukowane **280–286**). Wszystkie **7 stron** wyrenderowano i sprawdzono wizualnie, zwracając uwagę na rozszerzony dowód przeliczalnej domkniętości, aksjomat ccc, rozkład wzorów i ostatnią stronę. Nie stwierdzono ucięć, kolizji ani uszkodzonych glifów.
- **Log LaTeX:** **0 błędów, 0 niezdefiniowanych odsyłaczy, 0 brakujących cytowań, 0 przepełnionych wierszy**; **1 ostrzeżenie o niedopełnionym wierszu** w całej książce. Inwentarz: 851 etykiet i 639 odsyłaczy.

**Werdykt matematyczny:** audyt II wykrył rzeczywistą lukę w dowodzie lokalnej gęstości oraz dwa miejsca wymagające jawnych uzasadnień w dowodzie zachowania liczb kardynalnych. Wszystkie trzy poprawiono w źródle. Rozdział **pozostaje w audycie i nie uzyskuje statusu stabilnego**, ponieważ druga iteracja wymagała korekt. Następny etap: audyt III, zwłaszcza ponowna kontrola nowego argumentu przeliczalnej domkniętości.
