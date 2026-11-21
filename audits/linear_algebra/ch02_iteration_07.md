# Algebra liniowa — rozdział 02, audyt 7 (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
**SHA bloba rozdziału:** `71138e728ab572baffec15c986af02aace04249d`  
**SHA bloba rozdziału 01:** `072d79ddc70eed184eefc3840191be5cf380f69c`

## Kryterium audytu i decyzja

Zgodnie z ustalonym standardem przeprowadzono ponowny audyt **wyłącznie poprawności matematycznej i ewentualnych luk istniejącego materiału**, bez rozszerzania zakresu rozdziału i bez sztucznego dodawania twierdzeń.

**Wynik matematyczny: nie stwierdzono nowego błędu ani istotnej luki w obecnej treści. Nie wprowadzono żadnych zmian do pliku rozdziału 02.**

Po sześciu wcześniejszych audytach zakończonych poprawkami audyt 7 jest pierwszym audytem rozdziału 02 bez potrzeby korekty matematycznej. **Rozdział 02 uznaje się za matematycznie stabilny i przeznacza do zamknięcia po potwierdzeniu ostatniego CI.** Nie należy już dodawać materiału bez uzasadnionej konieczności.

## Kontrola wszystkich istniejących twierdzeń i dowodów

1. **Wymiar jako liczba kardynalna.** Ponownie sprawdzono lemat o nośniku współrzędnych, oszacowanie mocy sumy rodziny zbiorów skończonych, dowód równoliczności dowolnych baz i definicję wymiaru w ZFC. Założenia aksjomatu wyboru i wynik \(|I\times\mathbb N_0|=|I|\) dla nieskończonego \(I\) są właściwie oznaczone. Przypadki baz pustych i skończonych są zgodne z rozdziałem 01.
2. **Sumy algebraiczne podprzestrzeni.** Zweryfikowano definicję przez skończone sumy wektorów, przypadek pustego indeksu, własność najmniejszej podprzestrzeni i podstawowe działania. Sprawdzono wzór dla \(\dim_K(U+W)\) z argumentem poprzez bazy \(C\), \(C\cup A\), \(C\cup D\); jest poprawny także dla nieskończonych wymiarów przy AC, bez odejmowania liczb kardynalnych. Dowód przypadku skończonego nie korzysta z AC.
3. **Wewnętrzna i zewnętrzna suma prosta.** Zweryfikowano trzy równoważne kryteria prostości, w tym rodziny puste, zerowe i skończenie indeksowane. Sprawdzono sumowanie po skończonym nośniku, jądro kanonicznego odwzorowania \(\Sigma\), jego surjektywność i izomorfizm przy prostości. Rodziny baz składników dają bazę sumy prostej z odpowiednią sumą kardynalną.
4. **Przestrzenie ilorazowe.** Ponownie sprawdzono kryterium równości warstw i ich rozłączność, dobrą określoność działań, liniowość/surjektywność \(\pi_U\) oraz warunek na jądro. Własność uniwersalna jest wykazana przez konstrukcję indukowanego odwzorowania. Przypadki \(U=\{0_V\}\), \(U=V\) i przykład \(\mathbb R^2/U\cong\mathbb R\) są spójne.
5. **Dopełnienia algebraiczne.** Sprawdzono konstrukcję dopełnienia przez rozszerzenie bazy, dowód isomorfizmu \(W\cong V/U\), wzór kardynalny \(\dim_K V=\dim_K U+\dim_K(V/U)\) oraz jego niezależną, skończenie wymiarową wersję bez AC. Wykazano jedynie niejednoznaczność dopełnienia (bez niewykazanego silniejszego twierdzenia o naturalności).
6. **Twierdzenie o ilorazie sumy.** Konstrukcja \(U/(U\cap W)\to(U+W)/W\), jej niezależność od reprezentanta, liniowość, iniektywność i surjektywność zostały sprawdzone; nie wykryto luk.

Zweryfikowano też definicje, kwantyfikatory, ciała skalarów, powiązania z twierdzeniami rozdziału 01 i konsekwentną terminologię. Przykłady nie przypisują stopnia wielomianowi zerowemu; uwzględniają zerowy i nieskończony wymiar.

## Niezależna kontrola na skończonych przestrzeniach

Dodatkowo **wyczerpująco** wyliczono wszystkie 16 podprzestrzeni \(\mathbb F_2^3\) i przetestowano:

- **256 uporządkowanych par** podprzestrzeni: \(\dim(U+W)+\dim(U\cap W)=\dim U+\dim W\) oraz zgodność wymiarów ilorazu z \(|V/U|=|V|/|U|\).
- **4096 uporządkowanych trójek**: równoważność warunku jednoznaczności rozkładu, zanikania sumy jedynie dla zerowych składników oraz \(U_j\cap\sum_{i\ne j}U_i=\{0\}\).
- Przypadki podprzestrzeni zerowej oraz pustej rodziny indeksów.

**Wszystkie kontrole zaliczone.** Sprawdzenie obliczeniowe jest testem pomocniczym, nie zastępuje dowodów w tekście.

## Kontrola plików, odsyłaczy i terminologii

- Rozdział 01: **69** unikalnych etykiet; rozdział 02: **39**; razem **108**, bez duplikatów.
- Wszystkie **43** odsyłacze `\\ref`/`\\eqref` obu rozdziałów posiadają cele. Jeden historyczny odsyłacz w rozdziale 01 jest skierowany do definicji późniejszej w tym rozdziale — to poprawny, świadomy odsyłacz naprzód.
- Wszystkie środowiska `\\begin`/`\\end` poprawnie zagnieżdżone.
- Zachowano „suma zbiorów” i „warunek niezależności liniowej” w odpowiednich kontekstach, bez naruszania historycznych nazw etykiet.
- Nie ma zależności rozdziału 02 od zewnętrznych plików rysunków. Rysunek warstw w TikZ jest integralną częścią TeX.
- Porównanie SHA pokazuje, że plik rozdziału 02 jest **identyczny bajtowo** z wersją sprawdzoną przez poprawnie zakończony przebieg CI [44898808095](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44898808095).

## PDF i CI

Ponownie pobrano artefakt z CI 44898808095. Jest to **27-stronicowy** PDF dla dokładnie tej samej wersji treści rozdziału 02. Końcowy `linear_algebra.log` zawiera **0 wystąpień** `LaTeX Warning`, `Overfull`, `Underfull`, `Missing character`, `Undefined control sequence`, `Fatal error` i `There were undefined references`. Wyrenderowano i obejrzano strony 19, 23, 26, 27. Nie wykryto obcięć, kolizji ani nieczytelnych fragmentów.

W `books/pl/linear_algebra.tex` poprawiono wyłącznie **nieaktualny komentarz metadanych** „02 w pierwszym cyklu audytowym” na informację o stabilizacji rozdziałów 01–02; **treść matematyczna obu rozdziałów pozostała bez zmian**.

CI dla aktualnego pliku głównego po tej aktualizacji:
[44899784148](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44899784148) — **wynik do potwierdzenia**.

Wcześniejsze **24 problemy globalnego, nieblokującego walidatora innych skryptów** nie są częścią tego audytu i pozostają osobnym zadaniem.

## Stan końcowy

**Rozdział 02 matematycznie stabilny: po audycie 7 bez zmian w jego treści.** Formalne zamknięcie po ostatnim CI. Następny rozdział należy rozpocząć **dopiero w kolejnej iteracji na prośbę użytkownika**, zgodnie z regułą „rozdział po rozdziale”.
