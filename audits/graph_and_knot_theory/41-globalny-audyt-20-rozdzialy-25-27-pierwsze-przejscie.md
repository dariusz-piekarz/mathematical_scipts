# Teoria grafów i węzłów — globalny audyt 20: rozdziały 25–27, pierwsze przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Poprzednie rozdziały 01–24: **lokalnie stabilne**.
Zakres: rozdziały 25–27, **pierwszy audyt**, nie finalna stabilizacja.

## Zakres i główne ustalenie

- 25 — rachunek Kirby'ego na ramowanych splotach i grafach;
- 26 — klasyczna wymierna kontrakcja Fintushela–Sterna `C_p`;
- 27 — uogólnienie do `C_{p,q}` i ułamki łańcuchowe.

Zbadano konwencje skręceń i meridianów,
warunki pierwotności nachylenia,
całkowitą kongruencję macierzy,
grupy brzegu i formy splecenia,
hipotezy istnienia wymiernych kul homologii
oraz zmianę `e,σ,b_2^±`.
Wyniki głębokie Kirby'ego,
Cassona–Harera, Fintushela–Sterna,
Parka i Symington pozostają
jawnie oznaczone jako przyjęte z literatury.

## 25 — wykryta i naprawiona błędna hipoteza `slam-dunk`

**Istotny błąd matematyczny (naprawiony):**
Lemat `lem:tg-kirby-slam-dunk` dopuszczał
`r,s∈Q` i wnioskował, że chirurgia
na splocie Hopfa o tych współczynnikach
jest równoważna pojedynczej chirurgii
`r−1/s`. Twierdzenie w tej postaci
jest **fałszywe**.

Kontrprzykład:
dla `r=1/2`, `s=4` relacje
na pierwszej homologii wynikają z
pierwotnych par nachyleń:
`μ_U+2μ_V=0`,
`μ_U+4μ_V=0`.
Dają `H_1≅Z/2`. Natomiast
`r−1/s=1/4` oznacza chirurgię
na pojedynczym węźle trywialnym,
dla której `H_1=0`.
Nie może istnieć dyfeomorfizm
tych dwóch trójrozmaitości.

**Korekta:** teza zakłada teraz
`r∈Z`, `s=c/d∈Q\{0}`,
`c≠0`, `d>0`,
`gcd(c,d)=1`.
Po wyeliminowaniu geometrycznego
meridianu uzyskujemy
pierwotne nachylenie
`(rc−d)μ_U+cλ_U`.
Jest ono pierwotne, ponieważ
`gcd(rc−d,c)=gcd(d,c)=1`,
a jego współczynnik wynosi
`r−1/s=(rc−d)/c`.
Poprawiono uzasadnienie i dodano
powyższy kontrprzykład do tekstu.
Kolejne zastosowania w łańcuchach
plumbingowych zawsze usuwają
meridian składowej o **całkowitym**
współczynniku na składowej pozostającej,
więc poprawiony lemat ma właściwe hipotezy.

Dodano też
`ex:tg-kirby-positive-blowdown`:
dla macierzy ramowanego splotu
`Q=[[1,1,1],[1,-2,0],[1,0,-3]]`
kontrakcja składowej `+1`
daje `B'=[[-3,-1],[-1,-4]]`.
Zatem `det Q=det B'=11`,
`H_1≅Z/11`, a samosplecenie
generatora `K_1`
ma wartość `4/11 mod Z`.
Kontrakcja tworzy nową **ujemną**
krawędź pomiędzy wcześniej
niesplecionymi składowymi.
Ten przykład obejmuje inną
orientację ruchu niż wcześniejsze
przykłady o składowej `-1`.

Pełne twierdzenie Kirby'ego o
zupełności ruchów nie zostało
zastąpione rachunkiem samych
macierzy przecięcia.

## 26 — dokładny ciąg homologii wymiernej kuli

Dodano Stwierdzenie
`st:tg-rb-boundary-kernel`
z dowodem przez uniwersalne
twierdzenie o współczynnikach
i dualność Poincarégo–Lefschetza.

Dla standardowego modelu
Cassona–Harera `B_p`
(uchwyty `0,1,2`), mamy
`H_1(B_p;Z)=Z/p` oraz
`H_2(B_p;Z)=H_3(B_p;Z)=0`.
Stąd
`H^2(B_p;Z)=Ext(Z/p,Z)=Z/p`
i `H^3(B_p;Z)=0`.
Dokładny ciąg pary daje
`0→Z/p→H_1(Y_p;Z)→H_1(B_p;Z)→0`.

Ponieważ `H_1(Y_p;Z)=Z/p²`,
jądrem mapy na `H_1(B_p;Z)`
jest dokładnie jedyna
podgrupa rzędu `p`,
czyli `pH_1(Y_p)`.
Jej izotropowość
i równość z dopełnieniem
ortogonalnym wynikają
niezależnie z wcześniejszego
wzoru na formę splecenia
`λ(e_1,e_1)=(p−1)/p² mod Z`.
Dowiedziono w ten sposób
**zgodności algebraicznej z wypełnieniem**,
nie postulując wypełnienia
na podstawie samej obecności
metabolizera.

Weryfikacja hipotez źródłowych:
standardowy model `B_p`,
jego identyfikacja brzegu
`L(p²,1−p)` oraz
przypisanie `π_1(B_p)=Z/p`
pozostają przyjętym wynikiem
Cassona–Harera. Obliczenia
Mayera–Vietorisa zmiany
`e`, `σ`, `b_2^±`
są osobnymi konsekwencjami
tych założeń.

## 27 — dokładny przykład `C_{7,3}`

Dodano
`ex:tg-general-C73`, niezależny
przykład dla `p=7`, `q=3`:
`p²/(pq−1)=49/20=[3,2,6,2]^−`.
Macierz `Q_{7,3}` ma przekątną
`(-3,-2,-6,-2)` i
jedynki obok przekątnej.
Wyznaczniki ogonowe `-Q`
wynoszą kolejno
`D_5=1,D_4=2,D_3=11,D_2=20,D_1=49`.
Stąd `det Q_{7,3}=49`,
`H_1(∂C_{7,3};Z)=Z/49` i
`λ(e_1,e_1)=20/49 mod Z`.
Podgrupa `7⟨e_1⟩`
jest metabolizerem, ponieważ
jej samosplecenie wynosi `20=0 mod Z`.
W konwencji chirurgicznej rozdziału
brzeg to `L(49,−20)`.
Dla konfiguracji rzeczywiście
zanurzonej w czterorozmaitości
wymierna kontrakcja ma
`Δe=−4`, `Δσ=4`.

Porównano dokładnie przykład
z rodziną `C_{p,q}`;
sama równość `H_1=Z/p²`
nie identyfikuje ani orientacji
przestrzeni soczewkowej,
ani dyfeomorficznego typu
przyszłej czterorozmaitości.

## Nowe niezależne testy

Utworzono
`tools/tests/test_graph_and_knot_kirby_rational_blowdowns.py`
i dołączono do workflow
`.github/workflows/graph-and-knot-global-audit.yml`.
Nie są używane biblioteki zewnętrzne;
testy realizują dokładne wyznaczniki
i odwrotności macierzy nad `Q`.

Ostatecznie **4028** niezależnych
sprawdzeń w czterech grupach:
1. **2401** konfiguracji kontrakcji
   `±1`, całkowitej kongruencji,
   determinantów i form splecenia,
   łącznie z jawną macierzą
   o nowej ujemnej krawędzi;
2. **359** względnie pierwszych
   par `(p,q)` dla `2≤p≤34`:
   ujemne ułamki łańcuchowe,
   `det Q=(-1)^r p²`,
   minory ogonowe, dodatnia
   określoność `-Q`,
   pierwszy element odwrotności
   i izotropowa podgrupa `p⟨e_1⟩`;
3. **1119** par pierwotnych
   współczynników chirurgii
   dla poprawnego `r∈Z`,
   wraz z wykazaniem błędu przy
   `r=1/2,s=4`;
4. **149** sprawdzeń
   jądra mapy `Z/p²→Z/p`
   i jego dopełnienia
   ortogonalnego dla `2≤p≤150`.

Testy są skończoną kontrolą
konkretnych przykładów
i tożsamości arytmetycznych.
Nie są poświadczeniem
istnienia `B_{p,q}`
ani dowodem twierdzeń
Parka lub Symington.

## Końcowy przebieg CI i kontrola składu

Po wszystkich poprawkach matematycznych i dodaniu regresji
[GitHub Actions 45215345443](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45215345443)
dla commitu `dff813b5f8eddfc3ec20f435089534953417209b`
zakończył **oba zadania** statusem **success**:
`structural-audit` i `full-book-pdf`.

- Źródła: **44/44 rozdziały**, **0** duplikatów etykiet,
  **0** nierozwiązanych odsyłaczy, **0** błędów środowiska,
  **0** terminów zakazanych;
- dokładne regresje: **4028 nowych PASS**,
  w dodatku do uprzednio ustabilizowanych testów;
- trzy udane przebiegi `pdflatex` całego tomu;
- wygenerowany i pobrany z tego samego przebiegu
  PDF: **281 stron A4**;
- `audit_output/graph_and_knot_full_warnings.txt`
  ma **0 bajtów**.

Przegląd wizualny faktycznie wygenerowanego PDF
objął **wszystkie strony 210–226**,
czyli cały pierwszy audytowany blok:

- **210–214:** rozdział 25; w szczególności
  poprawione założenia `slam-dunk`,
  nowy kontrprzykład homologiczny,
  kontrakcje składowych `±1`,
  diagram z usunięciem wierzchołka `−1`
  i nowy przykład `+1`;
- **215–221:** rozdział 26; konfiguracje `C_p`,
  soczewkowe brzegi, rysunki dla `p=2,3,4`,
  pełny ciąg pary dla `B_p`,
  diagram wymiennego wypełnienia
  i zmiana niezmienników;
- **222–226:** rozdział 27; grafy `C_{5,1}`
  i `C_{5,2}`, algorytm ułamków,
  wyznaczniki `C_{p,q}`,
  nowy przykład `C_{7,3}` (s. 225)
  oraz schemat wymiernej kontrakcji.

Nie wykryto widocznych kolizji etykiet
ani rysunków z tekstem, obciętych
wyrażeń czy przekroczeń marginesów.
Rozkład stron jest prawidłowy.

## Werdykt audytu 20

**Pierwsze przejście rozdziałów 25–27 zakończone: PASS.**
Poprawiono istotną fałszywą tezę o
`slam-dunk`, uzupełniono rachunki,
przeprowadzono niezależne regresje,
skompilowano pełny tom i sprawdzono wizualnie PDF.

**Rozdziały 25–27 nadal W STABILIZACJI:**
wymagane drugie, niezależne przejście,
czyli **audyt 21**.
Rozdziały **01–24** pozostają lokalnie
stabilne; globalny audyt wszystkich
44 rozdziałów pozostaje otwarty.
