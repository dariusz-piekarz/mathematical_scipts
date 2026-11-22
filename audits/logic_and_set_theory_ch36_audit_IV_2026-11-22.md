# Logika matematyczna i teoria mnogości — audyt IV rozdziału 36 (potwierdzający)

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/36-modele-symetryczne-i-niezaleznosc-aksjomatu-wyboru.tex.  
**Blob źródłowy:** 6891b26609ccf77a0aaddc28653bb872f05a1701 — identyczny od audytu I.  
**Wynik matematyczno-redakcyjny:** czysty; brak nowego koniecznego uzupełnienia dowodu. Zakończenie dodatkowego audytu wymaga potwierdzenia końcowego CI i artefaktu PDF.

## 1. Odwrócony przegląd dowodu głównego

Przeprowadzono niezależny przegląd w kolejności od wniosku do założeń:

1. **Niesprzeczność ZF+¬AC z ZFC.** Wynika z istnienia *modelu zbiorowego* uzyskanego z ilorazu HS-nazw przez zewnętrzny filtr M-generyczny. Założenie Con(ZFC) wystarcza dzięki pełności i dolnemu Löwenheimowi--Skolemowi: nie ma ukrytego postulatu istnienia przeliczalnego modelu tranzytywnego. Definiowalność poszczególnych standardowych instancji relacji HS i lemat prawdy umożliwiają interpretację także w modelu źle ufundowanym zewnętrznie.
2. **Negacja wyboru.** Jeżeli N zawierałby iniekcję ω→A, jej nazwa miałaby skończony nośnik E. Każda wymuszona wartość nazwy funkcji na kanonicznym indeksie m musi być jednym z c_k. Zamiana k spoza E z całkowicie świeżym ell daje dwa zgodne warunki wymuszające różne wartości tej samej funkcji. Zatem jej zbiór wartości mieści się w {c_k:k∈E}; jest skończony i nie może być obrazem iniekcji z ω.
3. **Istnienie A w N.** Indywidualne nazwy c_n mają nośnik {n}, a nazwa zbioru wszystkich wierszy ma pusty nośnik, ponieważ permutacje tylko przestawiają jej argumenty. Generyczność rozdziela wszystkie pary c_n, c_m. A jest nieskończony, ale nie zawiera przeliczalnie nieskończonego podzbioru.
4. **Aksjomaty ZF w N.** Ekstensjonalność i ufundowanie przechodzą z transytywności. Pary, suma, zbiór pusty i nieskończoność mają jawne nazwy HS. Wyróżnianie, zbiór potęgowy i Collection wymagają sprawdzenia stabilizatorów skonstruowanych nazw, a nie tylko prawdziwości formuł w M[G]. Weryfikacja przebiega przez skończone nośniki parametrów oraz niezmienniczość relacji wymuszania. W przypadku Collection dobór ograniczenia rang jest wykonywany w modelu wyjściowym i daje zbiór kandydatów; nie stosuje się AC wewnątrz N.
5. **Lemat prawdy.** Dla atomów jest zwykłym lematem prawdy dla wymuszania P. W kroku negacji wykorzystuje gęstość rzeczywiście rozstrzygających warunków, dla egzystencji gęstość relatywnych świadków HS. Właściwość formuł jest rozumiana dla każdej *ustalonej standardowej formuły*, co nie wymaga jednego predykatu prawdy dla wszystkich wewnętrznych kodów w modelu źle ufundowanym.

Nie znaleziono miejsca, w którym potrzebna byłaby poprawka tekstu. W szczególności brak AC nie został utożsamiony z AD, a wynik dotyczy niezależności AC od ZF, nie jakiejś niezależności AD od AC.

## 2. Próby przypadków skrajnych

- **Pusty nośnik:** nazwa całej rodziny wierszy jest ustalona przez każdą permutację, chociaż poszczególne wiersze mają niepuste nośniki.
- **Nośnik zawierający badany indeks:** gdy k należy do E, argument transpozycyjny nie jest stosowany; możliwe wartości funkcji mogą odpowiadać tylko takim k. To warunek kluczowy dla poprawnej konkluzji skończoności obrazu.
- **Warunek częściowy na badanym wierszu:** wybór ell całkowicie poza skończoną dziedziną p gwarantuje zgodność p i obrazu przez transpozycję, niezależnie od przypisanych bitów k.
- **Nietranzytywny model wyjściowy:** wynik dotyczy zewnętrznej struktury ilorazowej; nie przypisujemy jej zewnętrznego dobrego ufundowania ani nie stosujemy kolapsu Mostowskiego.
- **Zbiór potęgowy:** nazwy ograniczone do dom(tau)×P wystarczają tylko dla podzbiorów τ należących do N; tekst nie utożsamia ich ze wszystkimi podzbiorami z M[G].

## 3. Inwentarz i testy

Źródło nadal obejmuje 938 wierszy, 21 odrębnych etykiet, 27 odsyłaczy, 5 definicji, 7 lematów, 4 twierdzenia, 3 uwagi, 1 przykład i 12 dowodów. Brak niezamkniętych środowisk i niezgodności z podstawowymi zasadami polskiej terminologii. Testy regresyjne: 8 metod, w tym 52488 prób zgodności atomowych wartości po permutacji oraz 2187 prób rozdzielania dwóch wierszy na świeżej współrzędnej.

Referencyjny pełny przebieg GitHub Actions **[45064877027](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064877027): SUCCESS**, artefakt 14770024176. PDF całej książki ma 320 stron A4, rozdział 36 obejmuje strony 313–320. Wszystkie te strony były wyrenderowane i obejrzane; nie stwierdzono obciętych równań ani nakładających się elementów.

## 4. Warunek ostatecznej stabilizacji

Audyty II i III nie wymagały zmian w źródle; audyt IV jest dodatkową, czystą kontrolą merytoryczną. Do formalnego uznania rozdziału 36 za **stabilny (2/2+1)** należy potwierdzić ukończenie pełnych przebiegów CI dla poprawionych testów i raportu IV, wraz z kontrolą PDF. Dopóki te warunki nie są potwierdzone, licznik pozostaje warunkowy. Samo zielone CI nie oznacza weryfikacji przez jądro Lean.
