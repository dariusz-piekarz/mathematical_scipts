# Topologia ogólna — rozdział 10, audyt 1

- **Rozdział:** Metryzowalność przestrzeni topologicznych.
- **Wersja robocza:** 0.1.
- **Status:** audyt 1 zakończony z poprawkami; czyste audyty 0/2.
- **Plik:** `chapters/pl/general_topology/10-metryzowalnosc.tex`.
- **SHA-256 pliku po poprawkach:** `36763908cf9d93cd9f57155269524e5f33ae183414069d882c0470b4fa8b94b9`.
- **Integracja:** wstrzymana do dwóch kolejnych czystych audytów.

## Audyt matematyczny

Sprawdzono kolejno definicje pseudometryki, metryki i topologii kul,
warunki konieczne metryzowalności, zmianę zgodnej metryki, dziedziczenie
przez podprzestrzenie, lemat regularność + Lindelöf => normalność,
pełną konstrukcję metryki w twierdzeniu Urysohna, metrykę na kostce
Hilberta, zanurzenie w przeliczalną kostkę, przeliczalne iloczyny,
przypadek zwarty Hausdorffa, prostą Sorgenfreya, kostkę nieprzeliczalną,
iloraz z dwoma początkami i różnicę między metryzowalnością a
zupełną metryzowalnością.

## Wykryte i usunięte usterki

1. **Brak uzasadnienia otwartości całej kuli:** po wykazaniu istnienia
   otwartego otoczenia jej środka trzeba dla każdego punktu `y` kuli
   zastosować konstrukcję z promieniem `epsilon - d(x,y)` i nierówność
   trójkąta. Uzupełniono argument w twierdzeniu Urysohna oraz dla
   metryki na kostce i przeliczalnym iloczynie.
2. **Przykład metryk niezupełnych:** uzupełniono uzasadnienie,
   że `arctan` jest homeomorfizmem na `(-pi/2, pi/2)` i wyznacza
   metrykę zgodną z topologią euklidesową; odwołano się do
   wcześniej wykazanego przenoszenia metryki przez homeomorfizm.
3. **Skład stron:** przeniesiono cały przykład ilorazu z dwoma
   początkami na następną stronę oraz oddzielono Krok 5 konstrukcji
   metryki, żeby uniknąć złamania zdania między stronami.

## Niezależna kontrola i walidacja

- Wszystkie 390 topologii na zbiorach co najwyżej czteroelementowych:
  zweryfikowano `regularna => normalna` (skończone przestrzenie są
  Lindelöfa), `T_3 <=> dyskretna` oraz `T_2 <=> dyskretna`.
- Konstrukcje metryk rozdzielających na siedmiu modelach dyskretnych,
  1295 trójek weryfikujących nierówność trójkąta.
- Jawne metryki ograniczone na czterech iloczynach skończonych:
  551880 trójek weryfikujących nierówność trójkąta.
- Regresja rozdziałów 01–10: PASS.
- Etykiety i odsyłacze: PASS.
- Terminologia globalna: PASS, w tym sformułowania o pierwszym i drugim
  aksjomacie przeliczalności.
- Kompilacja samodzielna: 8 stron, bez ostrzeżeń.
- Kompilacja pełnej książki: 88 stron, bez ostrzeżeń.
- Render i kontrola wizualna wszystkich 8 stron: PASS.

## Licznik czystych audytów

Audyt 1 wymagał zmian: **0/2**. Następny etap: audyt 2 tej wersji,
bez rozszerzania treści, aż do dwóch kolejnych czystych iteracji.
