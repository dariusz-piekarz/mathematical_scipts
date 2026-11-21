# Algebra liniowa — rozdział 02, audyt 6

Data: 21 listopada 2026  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Plik: `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
Commit treści: `e70f305aa0854bd59cc95dc313da73510535d252`

## Cel audytu

Audyt 6 dotyczył **wyłącznie poprawności obecnego materiału**: samodzielnych założeń twierdzeń, kwantyfikatorów, logiki dowodów, szczególnie użycia aksjomatu wyboru, poprawności przypadków skończonych i nieskończonych oraz integralności LaTeX. Nie dodano żadnych nowych tematów, definicji, twierdzeń, lematów ani przykładów.

## Najważniejsza poprawka matematyczno-logiczna

### Wzór wymiarowy dla sumy podprzestrzeni: zakres aksjomatu wyboru

W twierdzeniu `thm:lin2-wzor-wymiarowy` początkowe sformułowanie „Przyjmijmy aksjomat wyboru” obejmowało cały tekst, chociaż w drugiej części deklarowano, że wzór skończenie wymiarowy nie wymaga tego aksjomatu. W analogicznym twierdzeniu o wymiarze ilorazu dokonano już wcześniej odpowiedniego rozdzielenia. Pod względem samodzielności tezy jest to rzeczywista niespójność.

Poprawiono na dwa odrębne zdania w obrębie istniejącego twierdzenia. Dla przestrzeni \(V\) nad ciałem \(K\) i jej podprzestrzeni \(U,W\):

- Przy aksjomacie wyboru zachodzi równość kardynalna
  \[
  \dim_K(U+W)+\dim_K(U\cap W)=\dim_K U+\dim_K W.
  \]
- Jeśli \(U,W\) mają skończony wymiar, to niezależnie od aksjomatu wyboru zachodzi równość liczb naturalnych
  \[
  \dim_K(U+W)=\dim_K U+\dim_K W-\dim_K(U\cap W).
  \]

W dowodzie wskazano osobno, że w przypadku ogólnym stosujemy aksjomat wyboru do otrzymania baz, natomiast w przypadku skończonym rozpoczynamy konstrukcję od nowa: podprzestrzeń \(U\cap W\) ma skończoną bazę \(C\), którą skończonym algorytmem rozszerzamy do baz \(C\cup A\) w \(U\) i \(C\cup D\) w \(W\). Dalsza część dowodu jest wspólna. Nie zakładamy w przypadku skończonym baz wybranych uprzednio z użyciem aksjomatu wyboru.

## Jawne założenia definicji i twierdzeń

Przeprowadzono systematyczny przegląd samodzielności twierdzeń oraz definicji i uzupełniono ich wprowadzenia, nie zmieniając treści matematycznej:

- `lem:lin2-nosnik`: jawnie określona przestrzeń \(V\) nad \(K\) i jej baza Hamela.
- `thm:lin2-jednakowa-moc-baz`: jawna przestrzeń \(V\), ciało \(K\) oraz dwie bazy Hamela.
- `def:lin2-wymiar`: jawna przestrzeń wektorowa nad \(K\).
- `def:lin2-suma-podprzestrzeni`, `thm:lin2-suma-minimalna`, `prop:lin2-rachunek-sum`: jawna przestrzeń, rodziny jej podprzestrzeni i indeksy.
- `def:lin2-wewnetrzna-suma-prosta`, `thm:lin2-kryteria-sumy-prostej`: jawny zbiór indeksów i rodzina podprzestrzeni.
- `def:lin2-zewnetrzna-suma-prosta`, `thm:lin2-zewn-wewn`: jednoznacznie wskazano wspólne ciało i przestrzenie, z których zbudowano sumę.
- `def:lin2-iloraz`, `lem:lin2-warstwy`, `prop:lin2-iloraz-przypadki`: jawna przestrzeń nad \(K\), podprzestrzeń i zakres kwantyfikacji wektorów.
- `def:lin2-dopelnienie`, `thm:lin2-istnienie-dopelnienia`, `thm:lin2-iloraz-sumy`: pełne założenia o \(V\), \(U\), \(W\); w twierdzeniu o dopełnieniu wyraźnie wyodrębniono przypadek skończony bez aksjomatu wyboru.

Wszystkie stabilne etykiety `\\label` i odsyłacze `\\ref` pozostały niezmienione. Korekty ograniczono do już istniejących definicji, lematów i twierdzeń.

## Powtórna ocena poprawności pozostałych wyników

Sprawdzono dowód równoliczności dowolnych baz Hamela, w tym nośniki o skończonej mocy, lemat o sumie zbiorów skończonych oraz użycie twierdzenia Cantora–Bernsteina; obecny argument jest poprawny przy deklarowanym aksjomacie wyboru.

Zweryfikowano kryteria sumy prostej i jednoznaczności rozkładu, także przy pustym indeksie, izomorfizm sumy zewnętrznej z sumą wewnętrzną w przypadku prostości oraz dowód baz sum prostych. Nie stwierdzono nowej luki logicznej w tych miejscach.

Sprawdzono konstrukcję i równość warstw, dobrą określoność działań w \(V/U\), własność uniwersalną, dopełnienia i iloraz sumy. Odrębny dowód formuły wymiarowej ilorazu w przypadku skończonym pozostaje prawidłowy.

Nie zidentyfikowano nowego kontrprzykładu ani fałszywego twierdzenia; wykryta usterka dotyczyła **zakresu założeń i kompletności jego dowodowego uzasadnienia**, a inne poprawki — samodzielności sformułowań.

## Walidacja techniczna

- Rozdziały 01–02 zawierają łącznie **108 unikalnych etykiet**, bez duplikatów.
- Wszystkie lokalne i międzyrozdziałowe `\\ref` i `\\eqref` mają zdefiniowane cele.
- Środowiska `\\begin` i `\\end` są prawidłowo zagnieżdżone.
- Brak zakazanych wystąpień „unia” i „relacja liniowa” w treści; zachowano historyczne nazwy stabilnych etykiet.
- Nie dodano zewnętrznych grafik ani zależności do rozdziałów.
- CI dla wersji po korektach: [44898808095](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44898808095) — wynik końcowy do uzupełnienia.
- Istniejące błędy globalnej walidacji innych skryptów pozostają poza zakresem tego audytu.

## Status

**Audyt 6 zakończony z poprawkami.** Rozdział 02 pozostaje otwarty do kolejnej iteracji, zgodnie z kryterium stabilizacji (zamknięcie dopiero po audycie bez istotnych błędów i luk oraz po pomyślnych kontrolach technicznych).
