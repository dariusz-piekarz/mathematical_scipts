# Topologia ogólna — audyt globalny 13: rewalidacja 03–04, kontrola czysta 2/2

**Data:** 2026-11-22.
**Niezmienione bloby audytu 12:**
- 03: `021f4f843b26e90dca57b3e38b33e95cd0c03a5b`,
- 04: `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081`.

**Wynik:** druga czysta, niezależna
kontrola treści matematycznej i
zgodności redakcyjnej; nie zmieniono źródeł.

## Spójność matematyczna rozdziału 03

Wzory zachowywane przez
homeomorfizm nie korzystają
z aksjomatu T1 ani z
metryzowalności przestrzeni.
Sprawdzono kolejno:

- wnętrze: dwukrotne zastosowanie
  otwartości homeomorfizmów
  `f` i `f^{-1}`;
- domknięcie: po jednej inkluzji
  z ciągłości każdego kierunku;
- brzeg: obraz dopełnienia
  `X\setminus A` jest
  `Y\setminus f(A)`, a
  bijekcja zachowuje przecięcie;
- zbiór pochodny: w definicji
  przez otoczenia usunięcie
  punktu odbywa się przed
  przecięciem z `A`.
  Równość
  `f((U\setminus\{x\})∩A)
    =(f(U)\setminus\{f(x)\})∩f(A)`
  jest poprawna w dowolnej
  przestrzeni topologicznej;
- izolowanie punktu `x∈A`:
  jest równoważne warunkowi
  `x∉A'` bez żądania T1.

W przykładzie zanurzenia
naturalne włożenie
`A\hookrightarrow Y`
z topologią podprzestrzeni
jest homeomorfizmem na obraz.
Ciągła różnowartościowa
identyczność z topologii
dyskretnej do antydyskretnej
nie jest zanurzeniem,
gdyż odwrotność na obraz
nie jest ciągła.
Przykład pozostaje
udokumentowany w pełni
w poprzedniej sekcji
rozdziału 03.

## Spójność matematyczna rozdziału 04

- Przestrzeń ilorazowa jest
  zdefiniowana przez
  `V otwarty ⇔ q^{-1}(V) otwarty`;
  samo `q` musi być ciągłą
  surjekcją w definicji
  odwzorowania ilorazowego.
- W przykładzie identyfikującym
  na prostej punkty 0 i 1,
  nasycenie
  `(-1/2,1/2)`
  jest sumą
  `(-1/2,1/2)∪\{1\}`,
  nieotwartą w `R`.
  Odwzorowanie ilorazowe
  nie musi być otwarte.
- Przy sklejeniu wszystkich
  punktów przedziału
  `(0,1)`, domknięty singleton
  `\{1/2\}` ma nasycenie
  `(0,1)`, niebędące
  zbiorem domkniętym.
  Odwzorowanie ilorazowe
  nie musi być domknięte.
- Identyczność
  `(S,P(S))→(S,\{∅,S\})`
  jest ciągłą surjekcją,
  ale nie ilorazową,
  bo nie zachodzi równoważność
  otwartości zbioru i
  otwartości jego przeciwobrazu.
- W podsumowaniu
  topologię początkową
  prawidłowo wiąże się
  z rodziną odwzorowań
  `X→X_i`, a końcową
  z rodziną `X_i→Y`.
  Nie pomylono kierunku
  reguł uniwersalnych.

## Sprawdzenie struktury i status składu

Ponownie potwierdzono
niezmienność zbiorów etykiet,
pełną liczbę dowodów (15 i 17)
oraz obecność standardowych
komend sekcji i odsyłaczy.
W tekście 03 zastosowano
`\enlargethispage{4\baselineskip}`
jedynie dla ostatniej strony.
Rzeczywisty PDF nadal wymaga
potwierdzenia, czy zabieg
nie spowodował zbliżenia
treści do stopki albo
przeniesienia końca
podsumowania na nową stronę.

**Stan: czysty 2/2 pod kątem
matematyki i źródła;**
potrzebny dodatkowy,
niezależny audyt z
finalnym renderem PDF
na tych samych blobach.
