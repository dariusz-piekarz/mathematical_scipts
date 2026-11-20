# Topologia algebraiczna — szczegółowy audyt AT-29 i AT-30

**Data:** 20 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (bez modyfikacji main).  
**Zakres:** dokładnie dwa kanoniczne rozdziały:
- chapters/pl/algebraic_topology/29-dalsze-narzedzia-homotopii-granice-odwrotne-przeszkody-operacj.tex;
- chapters/pl/algebraic_topology/30-minimalne-przypomnienie-geometrii-rozniczkowej.tex.

**Standard:** sprawdzenie hipotez, argumentów, obliczeń, przykładów, kontrprzykładów, terminologii, rysunków, etykiet i niezależności źródeł. Wymagana szczegółowość jak DG-01. Zachowano wszystkie historyczne etykiety, dotychczasowe przykłady i dowody.

## AT-29 — granice odwrotne, przeszkody, Steenrod, Blakers–Massey i sklejanie Morse'a

Sprawdzono definicję granicy odwrotnej jako jądra 1−T i pierwszego funktora pochodnego jako kokernela; warunek Mittaga–Lefflera (przypadek surjektywny, redukcja do ustabilizowanych obrazów i układu pro-zerowego); izomorfizm lim¹(Z,×p)=Z_p/Z; ciąg Milnora dla stopniowo surjektywnych układów kompleksów; komórkowy kołańcuch przeszkody i lokalne współczynniki; relacje Adema (status jako wyniku zewnętrznego); ekscyzję Blakersa–Masseya i zakres Freudenthala; analityczne przesłanki sklejania trajektorii Morse'a.

### Poprawki matematyczne

1. **Nowy efektywny kontrprzykład** (etykieta prz:xviii-lim1-2adic-audit). W układzie równań a_j−2a_{j+1}=b_j, gdzie b_{2m}=1 i b_{2m+1}=0, rozwiązania wszystkich pierwszych N równań istnieją: z a_N=0 wyznaczamy wstecz a_j=b_j+2a_{j+1}. Rozwiązanie nieskończone wymagałoby jednak a_0=Σ4^m=−1/3 w Z_2, a a_0 ma należeć do Z. Równość 3a_0=−1 nie zachodzi dla żadnej liczby całkowitej. Otrzymujemy jawną niezerową klasę w lim¹(Z,×2), zamiast samego abstrakcyjnego istnienia ilorazu Z_2/Z.
2. **Rysunek** (fig:xviii-lim1-2adic-audit) przedstawia zgodne skończone redukcje sumy 2-adycznej: 1 mod 4, 5 mod 8, 5 mod 16, 21 mod 32, połączone odwzorowaniami redukcji.
3. **Korekta hipotezy w konstrukcji przeszkody komórkowej:** wcześniejszy opis przyjmował trywializację ściągniętej fibracji nad dyskiem „ustaloną na brzegu”, czego nie można narzucać bez zbadania możliwości zgodnego przedłużenia. Teraz wyraźnie wskazano wybór identyfikacji włókien i transportów bez niedozwolonego założenia dotyczącego całego brzegu. To właśnie przedłużalność przekroju jest badanym zagadnieniem.
4. **Korekta linearyzacji operatora Morse'a:** po arbitralnej trywializacji pochodna współrzędnych dξ/ds nie jest równa pochodnej kowariantnej. Zapisano wewnętrznie poprawną formę D_γξ=∇_sξ+∇_ξ(∇_g f)|_γ i wskazano, że zwykła pochodna jest dopuszczalna w trywializacji równoległej (na linii R), a w pozostałych wymagane są współczynniki koneksji.
5. **Redakcja matematyczna:** poprawiono wyrażenia „mapy przejścia”, „mapa ekscyzji” i podobne na „odwzorowania”; niedopuszczalne „sekwencji” zastąpiono „ciągu”. Poprawiono też sformułowanie iniektywności w dowodzie, bez zmiany sensu.

### Granice kompletności dowodów

Twierdzenie Adema, geometria ekscyzji Blakersa–Masseya, pełny komórkowy lemat kocyklu przeszkody, jednolite odwrotności Fredholmowskie i pełność przestrzeni parametrów sklejania Morse'a pozostają jawnie przyjętymi rezultatami albo wskazanymi zależnościami. Rachunki lim¹ i Milnora oraz nowy przykład nie zastępują ich dowodów. Status rozdziału: **zaakceptowany z jawnymi zastrzeżeniami co do głębokich twierdzeń**.

## AT-30 — minimalne przypomnienie geometrii różniczkowej

Porównano fragment z kanonicznym tomem Geometria i topologia różniczkowa: DG-01 (ch:rozmaitosci), DG-03 (ch:algebra-tensorowa), DG-15 (ch:sard-transwersalnosc), DG-16 (ch:wlozenia-otoczenia). AT-30 jest celowo krótkim przypomnieniem, więc nie należy kopiować z tamtego tomu pełnych dowodów Whitneya, Sarda, algebry tensorowej ani twierdzenia tubularnego.

### Poprawki

1. **Definicja derywacji:** dopisano liniowość nad R i pełną regułę Leibniza D(fg)=f(p)Dg+g(p)Df. Bez niej opis przestrzeni stycznej był nieprecyzyjny.
2. **Uramowanie:** rozróżniono gładkie uramowanie gładkiej wiązki i jej gładką trywialność od topologicznych odpowiedników z ciągłymi przekrojami; podano jawne odwzorowanie trywializujące.
3. **Nowy pełny przykład regularnego przeciwobrazu** (prz:at30-okrag-regularny): dla F(x,y,z)=(x²+y²−1,z) obliczono macierz różniczki, jej rangę 2 na poziomicy zerowej, T_pS=R(−y,x,0) i N_pS=span{(x,y,0),(0,0,1)}. Następnie skonstruowano i odwrócono jawny dyfeomorfizm otoczenia tubularnego Φ((x,y,0),a,b)=((1+a)x,(1+a)y,b). Sprawdzono gładkość odwrotności przez ρ=√(X²+Y²)>0.
4. **Nowy kontrastujący przykład transwersalności** (prz:at30-transwersalnosc-prostych): okrąg x²+y²=1 styka się z prostą y=1 w p=(0,1), gdzie obie przestrzenie styczne są poziome. Po perturbacji do y=1−ε dla 0<ε<1 pojawiają się dwa przecięcia o współrzędnych x=±√(2ε−ε²). Wyznacznik kierunków stycznych wynosi −x≠0, więc przecięcia są transwersalne.
5. **Nowy rysunek** (fig:at30-stycznosc-transwersalnosc) zestawia styczność i dwa punkty przecięcia transwersalnego. Zawiera jawny parametr ε=0,3.
6. **Świadoma nieduplikacja:** dodano mapę odpowiedników w DG-01/03/15/16 z historycznymi etykietami jako identyfikatorami tekstowymi, a nie fałszywymi lokalnymi odsyłaczami \ref. Dzięki temu tom AT kompiluje się bez zewnętrznych plików .aux, a przyszłe scalanie może odtworzyć historyczne referencje.

## Testy i kompilacja

- Dodano application/tests/test_topology_chapters_29_30.py — 9 regresji: indeks i kolejność AT-01–30; zachowanie pierwotnych etykiet i rozwiązywanie odsyłaczy, w tym trzech istniejących współdzielonych modułów; bilans otoczeń LaTeX i osadzone figury TikZ; znikanie niepoprawnej terminologii; skończone rozwiązania układu z lim¹ i 2-adyczne redukcje −1/3; poprawna pochodna kowariantna; pełne hipotezy derywacji i uramowań; rachunek przestrzeni stycznej i odwracalności tubularnego odwzorowania; transwersalne perturbacje prostej.
- Dodano .github/workflows/algebraic-topology-audit-ch29-30.yml, który sprawdza regresje, składa AT-01–30 w jednym dokumencie z trzema oryginalnymi wspólnymi modułami źródłowymi i dwa razy uruchamia pdflatex. Budowa odrzuca niezdefiniowane odsyłacze i przepełnione wiersze poziome, a PDF i logi trafiają do artefaktów GitHub Actions.
- Po zatwierdzeniu testów należy odczytać końcowy status workflow AT-29/30 i wynik pdfinfo; do tego czasu nie należy deklarować zatwierdzonej kompilacji ani oględzin rysunków.
- Rozdziały AT-29/30 nie korzystają z zewnętrznych obrazów, danych, kodu ani \input; cały tom zachowuje trzy wspólne źródłowe pliki TeX używane w AT-28.

## Co dalej

Po AT-30 zakończono pierwszy szczegółowy cykl przeglądu całych 30 rozdziałów źródłowych. Nadal wymagane są osobne kontrole **globalne**: przepływ założeń i terminologii między rozdziałami, mapa konfliktów etykiet z geometrią różniczkową i algebraiczną, identyfikacja duplikatów oraz powtórny audyt głębokich zewnętrznych wyników (np. Steenrod, Blakers–Massey, Verdier, Hodge, Schmid). W przyszłym scalaniu zachować sumę wszystkich niepowtarzalnych definicji, twierdzeń, istotnych dowodów, przykładów i rysunków.
