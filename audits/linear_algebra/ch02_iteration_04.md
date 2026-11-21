# Algebra liniowa — rozdział 02, audyt 4

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
**Commit treści po poprawkach:** `48e33cdde05912d31eeb220ded474a3751290add`

## Cel i zakres

Iteracja obejmuje **wyłącznie poprawność matematyczną i ewentualne luki już istniejącej treści**, bez rozbudowy zakresu rozdziału. Ponownie zbadano kolejność i samodzielność definicji i twierdzeń, kwantyfikatory, zależność od aksjomatu wyboru, przypadki zerowe, budowę przestrzeni ilorazowej, sumy proste i jej wzory wymiarowe oraz przykłady.

Nie dodano nowych twierdzeń, lematów, definicji ani przykładów. Dokonano wyłącznie korekt istniejących sformułowań i dowodów.

## Poprawki

### 1. Brak samodzielnego określenia obiektów w twierdzeniu o strukturze ilorazu

Twierdzenie `thm:lin2-struktura-ilorazu` zaczynało się od „Na (V/U) wzory…”, nie określając w obrębie tezy, czym są (V) i (U). Dopisano: **niech (V) będzie przestrzenią wektorową nad (K), a (Usubseteq V) jej podprzestrzenią**. Również w tezie nazwano (V/U) zbiorem warstw, dopiero później wyposażanym w działania wektorowe. Usunięto zależność formalnego brzmienia twierdzenia od poprzedzającej definicji.

### 2. Niepełne założenia w twierdzeniu o dopełnieniu i ilorazie

W twierdzeniu `thm:lin2-iloraz-dopelnienie` jawnie określono przestrzeń (V) nad (K) oraz podprzestrzenie (U,Wsubseteq V), zanim użyto warunku (V=Uoplus W).

### 3. Oddzielenie dowodu skończenie wymiarowego od zastosowania aksjomatu wyboru

Dotychczasowa wersja najpierw wybierała dopełnienie algebraiczne (W) na mocy twierdzenia ogólnego, wymagającego aksjomatu wyboru, a dopiero później stwierdzała, że wynik skończenie wymiarowy nie wymaga tego aksjomatu. To nie uzasadniało dostatecznie niezależności drugiej części od wcześniejszego wyboru.

Dopisano **osobną, skończoną konstrukcję**: wybieramy skończoną bazę (B_U) podprzestrzeni (U) i rozszerzamy ją do skończonej bazy (B) przestrzeni (V). Następnie (W_0=operatorname{span}(Bsetminus B_U)) jest dopełnieniem algebraicznym, a izomorfizm (W_0cong V/U) wynika z pierwszej części dowodu. Z równości (dim V=|B_U|+|Bsetminus B_U|) oraz (dim(V/U)=|Bsetminus B_U|) wyprowadzono wzór przez odejmowanie liczb naturalnych, nie korzystając z aksjomatu wyboru.

### 4. Jawne założenia o rodzinie podprzestrzeni w twierdzeniu o bazie sumy prostej

W `thm:lin2-wymiar-sumy-prostej` wskazano wprost, że ((U_i)_{iin I}) jest rodziną podprzestrzeni jednej przestrzeni (V) nad (K) i spełnia (V=igoplus_i U_i); dla każdego (i) ustalona jest baza (B_i). Zapobiega to odczytaniu stwierdzenia bez określenia obiektów.

### 5. Dokończenie weryfikacji przykładu warstw poziomych

W przykładzie `prz:lin2-warstwy-r2` jawnie wykazano, że warstwy ((a,b)+U) i ((c,d)+U) są równe dokładnie przy (b=d), a następnie sprawdzono dobrą określoność, liniowość, surjektywność i iniektywność przyporządkowania ((a,b)+Umapsto b). Przykład nie opiera się już na samym nieudowodnionym stwierdzeniu, że to izomorfizm.

## Weryfikacja pozostałych części

- **Wymiar w dowolnym wymiarze:** sprawdzono użycie nośników skończonych, oszacowanie mocy sumy mnogościowej rodziny zbiorów skończonych przy założeniu AC, postać twierdzenia Cantora–Bernsteina i przejście do liczby kardynalnej wymiaru.
- **Wzór dla dwóch podprzestrzeni:** poprawne są rozłączność fragmentów baz, konstrukcja bazy ich sumy i kardynalna tożsamość bez odejmowania nieskończonych liczb kardynalnych.
- **Sumy proste:** kryteria przez jednoznaczność rozkładu i przecięcie z sumą pozostałych podprzestrzeni pozostają poprawne również przy indeksie pustym.
- **Struktura ilorazu i własność uniwersalna:** sprawdzono zależność od przedstawicieli i konstrukcję indukowanego odwzorowania.
- **Twierdzenie o ilorazie sumy:** wzór (U/(Ucap W)cong(U+W)/W) i jego dowód spełniają wymagania.
- **Rysunek warstw:** nie wymaga merytorycznych zmian.

## Walidacja

- Oba rozdziały zawierają łącznie **108 unikalnych etykiet**; nie wykryto duplikatów ani brakujących odsyłaczy `\\ref` i `\\eqref`.
- Zachowano poprawne domknięcie środowisk LaTeX.
- Sprawdzono standard językowy: „suma zbiorów” i „warunek niezależności liniowej” (zachowano historyczne identyfikatory etykiet).
- CI dla tekstu po poprawkach: [44896948139](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44896948139) — **weryfikacja końcowego wyniku w toku**.
- Globalne problemy walidacji innych skryptów nie są częścią tego audytu.

## Status

**Audyt 4 wykrył i usunął luki formalne i dowodowe.** Rozdział 02 pozostaje otwarty; w następnym cyklu należy ponownie skontrolować poprawność tego samego materiału, bez dodawania nowych zagadnień.
