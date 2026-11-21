# Algebra liniowa — rozdział 02, iteracja 01: utworzenie i pierwszy audyt

Data: 21 listopada 2026  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Rozdział: `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
Wersja treści po pierwszym audycie: commit `c962f1abcd20d6c64cf0c509dcd9f3520077d51a`

## Zakres nowego rozdziału

Rozdział 02 jest odrębnym plikiem TeX, włączonym do
`books/pl/linear_algebra.tex` i do `catalog/books.json`.
Obejmuje wymiar w dowolnym wymiarze (równość mocy baz,
współrzędne o skończonym nośniku i rachunek kardynalny),
sumy algebraiczne podprzestrzeni, wzór wymiarowy,
wewnętrzne i zewnętrzne sumy proste, kryteria jednoznaczności
rozkładu, warstwy i przestrzeń ilorazową, własność
uniwersalną ilorazu, dopełnienia algebraiczne, wymiar ilorazu
oraz izomorfizm
\(U/(U\cap W)\cong(U+W)/W\).

Wszystkie ważne wyniki mają samodzielne dowody. Rozdział
rozróżnia przypadki skończenie wymiarowe, w których nie
potrzeba aksjomatu wyboru, oraz ogólne przypadki
wymagające użycia baz i arytmetyki kardynalnej.
Dodano m.in. przykłady w \(\mathbb R^2\), \(\mathbb R^3\),
\(K[X]\) i rysunek warstw przestrzeni ilorazowej.

## Pierwszy audyt matematyczny

1. Zweryfikowano dowód równości mocy dowolnych baz:
   z rozpinania przez jedną bazę wynika pokrycie drugiej
   przez skończone nośniki; oszacowanie mocy sumy
   mnogościowej skończonych zbiorów stosuje aksjomat wyboru;
   po zamianie ról baz działa twierdzenie
   Cantora--Bernsteina.
2. Zweryfikowano wzór wymiarowy
   \(\dim(U+W)+\dim(U\cap W)=\dim U+\dim W\)
   dla liczb kardynalnych, bez wykonywania niedozwolonego
   odejmowania nieskończonych liczb kardynalnych.
3. Sprawdzono definicję i równoważne warunki sumy prostej,
   również przy pustej rodzinie indeksów oraz dla trzech
   podprzestrzeni, których przecięcia parami są zerowe,
   mimo że suma nie jest prosta.
4. Sprawdzono niezależność działań w ilorazie od wyboru
   przedstawiciela warstwy, surjektywność odwzorowania
   kanonicznego, opis wektorów zerowych i uniwersalną
   własność przestrzeni ilorazowej.
5. Sprawdzono konstrukcję dopełnienia przez rozszerzenie
   bazy i izomorfizm \(W\cong V/U\), wraz z przykładami
   niekanoniczności dopełnienia.
6. Potwierdzono poprawność i jednoznaczność odwzorowania
   \(U/(U\cap W)\to(U+W)/W\).

## Poprawki redakcyjne i dowodowe pierwszej iteracji

- W lemacie o nośniku współrzędnych przebudowano pierwsze
  zdanie dowodu, aby poprawić jego skład, ograniczyć
  dzielenie wyrazów i uniknąć lokalnego ostrzeżenia
  `Underfull \\hbox` z pierwszej kompilacji.
- W definicji przestrzeni ilorazowej sprecyzowano,
  że \(v+U\) jest \emph{przesunięciem zbioru \(U\)}
  o wektor \(v\).
- W przykładzie dopełnień w \(\mathbb R^2\)
  jawnie sprawdzono niezależność obu par generatorów
  i zapisano ich przedstawienia rozpinające.
- Dla ilorazu wielomianów przez wielomiany stałe
  doprecyzowano przypadek pustej sumy \(d=0\).

### 5. Uzasadnienie działania produktu i zachowania wymiaru przez izomorfizm

W dowodzie twierdzenia o sumie zewnętrznej dopisano uzasadnienie,
że produkt \(\prod_i U_i\) jest przestrzenią wektorową
z działaniami współrzędnymi, a suma zewnętrzna jest podprzestrzenią.

W dowodzie wzoru na wymiar przestrzeni ilorazowej
wykazano explicite, że liniowa bijekcja \(\Theta:W\to V/U\)
przenosi bazę Hamela \(W\) na bazę Hamela \(V/U\).
Dopiero stąd wyprowadzono równość wymiarów
\(\dim_K W=\dim_K(V/U)\).

## Globalna terminologia

W tej samej iteracji użytkownik wprowadził dwie wiążące
reguły dla całej Biblioteki:
- **„suma zbiorów” / „suma mnogościowa”** zamiast „unia”
  dla operacji \(\cup\);
- **„warunek niezależności liniowej wektorów”** zamiast
  „relacja liniowa” w odpowiednich dowodach.

Zasady zapisano w `AGENTS.md`
i `docs/pl/standardy_terminologiczne.md`.
W rozdziale 01 poprawiono wystąpienia starych wyrażeń
bez zmiany stabilnych nazw `\\label`; rozdział 02
napisano już według nowych zasad.
Wprowadzono automatyczną kontrolę terminologii
i odsyłaczy obu rozdziałów do
`.github/workflows/linear-algebra-chapter.yml`.
Pierwsza wersja nowego CI wykryła jeszcze słowo
„relację” w rozdziale 01: zostało usunięte,
a ponowny przebieg zakończył się sukcesem.

## Walidacja techniczna

- Rozdział 01: 69 etykiet, rozdział 02: 39 etykiet,
  **łącznie 108 bez duplikatów**.
- Wszystkie odsyłacze nowych rozdziałów mają cele,
  również odsyłacze między rozdziałami.
- Bez zewnętrznych plików graficznych w rozdziale 02;
  rysunek warstw wykonano bezpośrednio w TikZ.
- Dwurozdziałowy PDF po pierwszym kompletowaniu
  liczy **26 stron**.
- CI skanujące oba rozdziały po włączeniu nowego pliku:
  [44894198368](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44894198368)
  — **success**.
- CI po poprawkach audytu 1:
  [44894419432](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44894419432)
  — wcześniejsza wersja poprawek, oraz
  [44894493853](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44894493853)
  — ostateczny commit po dodatkowych wyjaśnieniach dowodowych, wynik do potwierdzenia.
- Starsze 24 błędy globalnej walidacji pozostałych
  materiałów w repozytorium są raportowane osobno
  i nie zostały objęte tą iteracją.

## Status

Rozdział 02 **utworzony i objęty pierwszym audytem**.
Nie deklarujemy jeszcze jego ostatecznego zamknięcia.
Kolejna iteracja powinna być szczegółowym audytem 2
*tego samego* rozdziału, koncentrującym się na poprawności
dowodów, brakujących uzasadnieniach, przykładach,
rysunku i LaTeX, bez automatycznego rozszerzania pokrycia
o kolejne działy.
