# Logika matematyczna i teoria mnogości — audyt I rozdziału 34

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/34-hipoteza-continuum-i-zastosowania-wymuszania.tex.  
**Tytuł:** „Hipoteza continuum i zastosowania wymuszania”.  
**Status:** po pierwszym audycie, jeszcze nie ostatecznie stabilny.

## Zakres audytu

Zweryfikowano wszystkie definicje, lematy, twierdzenia, przykłady i dowody, w szczególności: przeliczalność modeli i warunków w rozumieniu zewnętrznym/wewnętrznym; niepowstawanie nowych liczb porządkowych; lemat o systemie $\Delta$; ccc wymuszania $\operatorname{Add}(\omega,\kappa)$; zachowanie mocy przez ccc; nowość i wzajemną różność wielu ciągów Cohena; przeliczalną domkniętość; brak nowych ciągów liczb porządkowych długości $\omega$; kolaps mocy continuum i dowód CH; oddzielenie metamatematycznej niesprzeczności od istnienia przeliczalnego tranzytywnego modelu.

## Wykryte i usunięte usterki

### I. Niejawny zbiór wszystkich nazw

W pierwotnej wersji końcowego twierdzenia rozumowanie o zewnętrznej przeliczalności rozszerzeń sugerowało istnienie **wewnątrz $M$** zbioru wszystkich nazw wystarczających do budowy rozszerzenia. Byłoby to nieuprawnione: nazwy tworzą w $M$ klasę właściwą.

**Poprawka:** $M[G]$ jest przeliczalny zewnętrznie, ponieważ każdy jego element jest interpretacją pewnej nazwy $\tau\in M$, a zbiór nazw należących do $M$ jest **zewnętrznie** podzbiorem przeliczalnego zbioru $M$. Nie stwierdza się istnienia zbioru wszystkich nazw wewnątrz $M$.

### II. Niewykazana nowość każdego ciągu Cohena

W pierwszej wersji dowiedziono jedynie, że ciągi $c_\alpha$ są parami różne, choć sformułowanie mówiło też, że są nowe.

**Poprawka:** dla każdej $\alpha<\kappa$ i starego $x\in(2^\omega)^M$ wprowadzono gęsty zbiór
\[
 E_{\alpha,x}=\{p:\exists n<\omega\
 ((\alpha,n)\in\operatorname{dom}p\land p(\alpha,n)\ne x(n))\}.
\]
Dla dowolnego skończonego $p$ można dodać świeżą współrzędną z wartością $1-x(n)$, więc zbiór jest gęsty w $M$. Filtr generyczny go przecina; zatem $c_\alpha\ne x$ dla każdego $x\in(2^\omega)^M$ i **$c_\alpha\notin M$**.

### III. Niepełne jawne założenia

W kilku stwierdzeniach pozostawiono model $M$ lub typ wymuszania wyłącznie w kontekście rozdziału. Rozwinięto założenia na model tranzytywny, przeliczalność zewnętrzną tam, gdzie jest potrzebna, wewnętrzne liczby kardynalne, filtr generyczny oraz pojęcie wymuszania w ośmiu definicjach, lematach i twierdzeniach. Nie zmieniono zakresu merytorycznego wyników.

### IV. Błędny odsyłacz

Poprawiono odsyłacz do rozdziału o uniwersum konstruowalnym, stosując rzeczywistą etykietę ch:constructible. Aktualna książka nie ma nierozwiązanych odsyłaczy.

## Kontrola dowodów

**System $\Delta$ i ccc.** Lemat o systemie $\Delta$ jest wyprowadzony w ZFC przez indukcję po liczbie elementów zbiorów: występowanie wspólnego elementu w nieprzeliczalnie wielu zbiorach pozwala zmniejszyć liczbę elementów, a przeciwny przypadek i regularność $\omega_1$ pozwalają wybrać nieprzeliczalnie wiele zbiorów parami rozłącznych. W $\operatorname{Add}(\omega,\kappa)$ warunki o wspólnym rdzeniu dziedzin i tych samych wartościach na rdzeniu mają wspólne wzmocnienie, co wyklucza nieprzeliczalny antyłańcuch wewnątrz $M$.

**Zachowanie liczb kardynalnych.** Jeżeli istniałaby surjekcja $f:\beta\to\lambda$ z $\beta<\lambda$, maksymalne antyłańcuchy rozstrzygające $f(\xi)$ wyznaczają w $M$ przeliczalne zbiory $S_\xi$ możliwych wartości. Ich suma ma moc nie większą niż $\max(\aleph_0,|\beta|)<\lambda$, nawet gdy $\lambda$ jest osobliwa. Generyczność wymusza, że obraz $f$ należy do tej sumy, wbrew surjektywności.

**Zaprzeczenie CH.** Dodanie $\omega_2^M$ ciągów Cohena zachowuje kardynały modelu wyjściowego przez ccc, a ich różność daje w rozszerzeniu $2^{\aleph_0}\ge\aleph_2$. Każdy ciąg jest dodatkowo nowy względem $M$ dzięki gęstym zbiorom $E_{\alpha,x}$. Nie wymaga się CH w $M$.

**Przeliczalna domkniętość.** W modelu $M$ wybieramy malejący ciąg warunków decydujących kolejne wartości nazwanej funkcji na $\omega$. Domkniętość wewnątrz $M$ daje jeden warunek poniżej całego ciągu. Stąd żaden generyczny filtr nie wprowadza nowej funkcji $\omega\to\operatorname{Ord}$ i w szczególności żadnego nowego podzbioru $\omega$. Zachowana jest $\omega_1$.

**Wymuszenie CH.** Poset częściowych funkcji $\omega_1^M\to(2^{\aleph_0})^M$ o przeliczalnych w $M$ dziedzinach jest przeliczalnie domknięty. Funkcja generyczna jest surjekcją na dawną moc continuum; przy braku nowych ciągów binarnych daje to CH w rozszerzeniu. Jednocześnie nie wnioskuje się o zachowaniu wszystkich kardynałów.

**Rozróżnienie metamatematyczne.** Końcowe twierdzenie jest udowodnione przy założeniu istnienia przeliczalnego tranzytywnego modelu zbiorowego ZFC, co jest silniejsze niż sama $\operatorname{Con}(\mathrm{ZFC})$. Nie przedstawia się tego jako pełnego formalnego dowodu względnej niesprzeczności CH i $\neg\mathrm{CH}$ względem ZFC.

## Integracja i testy

- Rozdział 34 jest włączony do głównego pliku książki, katalogu i workflow CI.
- Inwentarz: **5 definicji, 7 lematów, 5 twierdzeń, 2 przykłady, 3 uwagi, 12 dowodów, 23 etykiety, 22 odsyłacze**.
- Książka: **34 rozdziały, 851 etykiet i 638 odsyłaczy**.
- Dodano **11 testów Python** kontrolujących inwentarz, odsyłacze, ograniczone przykłady zgodności i gęstości funkcji Cohena, ich nowości, domknięcia oraz kolapsu. Są to regresje obliczeniowe, nie formalizacja twierdzeń w Lean.
- [GitHub Actions #45022414876](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022414876): **SUCCESS** dla pierwszej wersji po integracji.
- [GitHub Actions #45022494057](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022494057): **SUCCESS** po korektach audytu I. Testy, inwentarz, skład LaTeX i kontrola logu: PASS.
- **PDF:** 294 strony; rozdział 34 zajmuje strony PDF **289–294** (drukowane **280–285**). Obejrzenie sześciu wyrenderowanych stron: poprawne łamanie, czytelne wzory, brak ucięć i nachodzenia tekstu.
- **Log:** 0 błędów, 0 nierozwiązanych odsyłaczy, 0 brakujących cytowań, 0 przepełnionych wierszy; jedno ostrzeżenie o niedopełnionym wierszu w całej książce.

## Werdykt

**AUDYT I — ZAKOŃCZONY, WALIDACJA TECHNICZNA PASS.** W audycie znaleziono nieuprawnione sformułowanie o zbiorze wszystkich nazw wewnątrz $M$, brak argumentu nowości każdego ciągu Cohena, niekompletne założenia i zły odsyłacz. Wszystko poprawiono. Ponieważ wprowadzone poprawki były merytoryczne, rozdział 34 **nie jest jeszcze stabilny po audycie I**.

**Następny krok:** niezależny audyt II, szczególnie weryfikacja zachowania kardynałów przez ccc, braku nowych ciągów przy przeliczalnej domkniętości oraz rozdzielenia modelowego wyniku CH/$\neg$CH od pełnej względnej niesprzeczności.
