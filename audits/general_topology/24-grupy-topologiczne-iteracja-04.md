# Topologia ogólna — rozdział 24, audyt 04 (nadmiarowy, czysty)

**Data:** 2026-11-22.
**Ten sam blob w audytach 02–04:**
`4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`.
**Wynik:** CZYSTY 3/2. Nie zmieniono źródła rozdziału.

## Niezależny przegląd kontrprzykładów i hipotez

1. Jeśli G jest grupą wieloelementową z topologią
   antydyskretną, mnożenie i odwracanie są ciągłe,
   ale brak Hausdorffowości; stąd jawna definicja
   grup topologicznych Hausdorffa jest istotna.
2. Grupa Q z topologią odziedziczoną z R jest
   podgrupą gęstą, ale niedomkniętą; R/Q
   nie jest Hausdorffa. Nie wolno używać
   kryterium zamkniętości H bez T2 w G.
3. W S3 z topologią dyskretną podgrupa
   H={e,(12)} jest domknięta, ale nie jest normalna,
   a cosety lewostronne tworzą przestrzeń
   dyskretną 3-elementową.
   Obliczenie \((13)^{-1}(12)(13)=(23)\notin H\)
   pokazuje, dlaczego mnożenie cosetów jest źle
   określone. Sam fakt, że G/H jest przestrzenią
   Hausdorffa, nie daje grupy ilorazowej.
4. R/Z jest homeomorficzne z S1 na mocy
   ciągłego **otwartego** homomorfizmu
   exp(2πit). Pojedynczy przedział o
   długości <1 odwzorowuje się na otwarty
   łuk, a dowolny zbiór otwarty jest sumą
   takich przedziałów; jądro jest Z.
5. Ciągły bijektywny homomorfizm
   (R,dyskretna)→(R,euklidesowa)
   nie jest homeomorfizmem; otwartość
   w topologicznym twierdzeniu o izomorfizmie
   nie jest pustą hipotezą.
6. Dla jednostkowego elementu e
   wybrana dyadyczna funkcja wag rho
   ma wartość zero; dla innych punktów
   ma wartość dodatnią.
   Dla m=1 i m>1 oraz dla obu przypadków
   S<2^{-(n+1)} i S≥2^{-(n+1)}
   oszacowanie iloczynu jest poprawne.
   Dowód zachowuje też puste prefiksy
   i sufiksy przy rozdzielaniu iloczynów.
7. Własność „spełnia pierwszy aksjomat
   przeliczalności” to własność lokalnej bazy,
   nie wymóg przeliczalnej liczby elementów G:
   nieprzeliczalne grupy dyskretne są
   metryzowalne i spełniają pierwszy,
   ale nie drugi aksjomat przeliczalności.
8. Produkt {0,1}^I z I nieprzeliczalnym
   jest zwarty Hausdorffa, a przeliczalna
   rodzina jego otoczeń cylindrycznych
   kontroluje co najwyżej przeliczalny
   zbiór współrzędnych. Stąd nie ma
   przeliczalnej bazy otoczeń w e.
   Argument używa tylko pierwszego
   aksjomatu przeliczalności i
   nie odwołuje się do drugiego.
9. Dla składowej spójnej G^0
   dowód ilorazu całkowicie niespójnego
   korzysta z ciągłości i otwartości q
   oraz spójności włókien;
   nie zastąpiono tutaj spójności
   zwykłą spójnością drogową.
10. W strukturach jednostajnych użyto
    właściwych warunków:
    lewa E^L opiera się na x^{-1}y,
    a prawa E^R na xy^{-1}.
    W ogólnej grupie nie utożsamiono
    ich bez przesłanki przemienności.

## Redakcja, testy, publikacja

Ponownie pobrano plik z GitHub i potwierdzono
identyczny blob; 41 różnych etykiet, 14 poprawnych
odsyłaczy i 21 bloków dowodowych.
Sprawdzono pisownię polską, terminologię,
tytuły i rozdzielenie zagadnień od dowodu
miary Haara w teorii miary.
W CI 45053429106 wszystkie kroki
przeszły, łącznie z pełną książką
i samodzielnym PDF. Z artefaktu
pobrano 10 stron PDF, obejrzano
całą serię renderów oraz szczegółowo
strony 6 i 10. Bez kolizji napisów
i błędów logu.

**Wniosek:** spełniono zasadę
2/2 czyste audyty + 1 kontrola dodatkowa
na niezmienionym blobie.
Rozdział 24 może zostać oznaczony
jako stabilny po aktualizacji statusu
katalogu, strony tytułowej i testów
oraz końcowym zielonym CI.
