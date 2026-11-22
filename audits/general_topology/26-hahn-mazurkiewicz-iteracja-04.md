# Topologia ogólna — rozdział 26, audyt 04 (pierwszy czysty po korekcie składu)

**Data:** 2026-11-22.
**Źródło:** `chapters/pl/general_topology/26-twierdzenie-hahna-mazurkiewicza.tex`.
**Blob:** `9f1ea17248b4df5805c025ba7bb47219c1dd4562`. **Wynik:** CZYSTY 1/2.
Źródła w tej iteracji nie zmieniono.

## Audyt głównego dowodu (wystarczalność)

1. Lokalna spójność i zwartość metryczna
   umożliwiają wybranie **jednego**
   δ>0 zapewniającego wspólne małe
   spójne otoczenie dla każdej bliskiej pary.
   Wyprowadzenie δ przez skończone podpokrycie
   i min r_i zawiera wszystkie kwantyfikatory.
2. W spójnym zbiorze C, skończone δ-łańcuchy
   istnieją między każdymi dwoma punktami,
   bo ich klasy osiągalności są otwarto-domknięte.
   Nie zakłada się nieudowodnionej spójności drogowej.
3. Każda krawędź podziału poziomu n ma
   końce odległe o mniej niż δ_n,
   a nowe wierzchołki mieszczą się
   w spójnym zbiorze o średnicy <ε_n.
   Przypadek jednoodcinkowego łańcucha
   prowadzi do dodania powtórzonego punktu,
   co zapewnia rozdrobnienie parametru
   nawet jeśli sam łańcuch był krótki.
4. Wartości przypisane na dalszych poziomach
   odchylają się od końca odcinka poziomu n
   o najwyżej ogon Σ_{k≥n} ε_k.
   Odcinki czasowe stopniowo maleją co
   najmniej dwukrotnie; dla dwóch bliskich
   parametrów potrzebne są najwyżej
   dwa sąsiednie odcinki poziomu n.
   Stąd nie opiera się ciągłości
   granicznej na intuicji z obrazka:
   ma ona ścisłe oszacowanie oscylacji 4S_n.
5. Zwartość X zapewnia zupełność,
   dlatego jednostajnie ciągła funkcja
   na gęstym zbiorze parametrów
   rozszerza się jednoznacznie do [0,1].
   Końce drogi zachowują wartości a,b,
   a jej średnica jest ograniczona
   przez 2Σ ε_n<η.
6. Lokalne małe drogi w otwartym O
   pozwalają udowodnić, że każda
   składowa drogowa O jest otwarta.
   Wykorzystany wynik rozdziału 08
   daje lokalną spójność drogową,
   a spójność X daje spójność drogową.
7. Lemma krótkiej wycieczki grupuje
   powtórzone czasy t_i, wybiera
   skończenie wiele rozłącznych
   przedziałów czasu i wstawia
   domknięte pętle o małej średnicy.
   Poza wybranymi przedziałami
   droga nie ulega zmianie;
   na nich błąd jest <2ε.
8. W rekurencji z δ_{n+1}/2-siecią
   nowa droga przechodzi przez
   wszystkie jej punkty,
   a sup d(f_{n+1},f_n)≤2ε_n.
   Summowalność kosztów
   daje jednostajną granicę.
   Każde x∈X jest w domknięciu
   obrazu granicy z oszacowania
   δ_n/2+Σ_{k≥n}2ε_k→0;
   obraz jest zwarty i domknięty,
   więc jest całą przestrzenią.

## Zależności i przypadki skrajne

- Gdy continuum jest jednoelementowe,
  pierwsza droga i kolejne są stałe.
  Zatem konstruowana surjekcja istnieje.
- Gdy a=b w lemacie małych dróg,
  stała droga jest dopuszczalna;
  konstrukcja podziałów nadal działa.
- Nie założono istnienia surjekcji
  Cantora na X ani gotowej
  parametryzacji Peana: dowód jest
  logicznie samodzielny względem
  takich twierdzeń.
- Wymóg Hausdorffa jest jawny.
- Podstawowe definicje z rozdziału 25
  zostały wykorzystane przez odsyłacze,
  a nie przepisane.

## Stan techniczny

23 różne etykiety, 24 odsyłacze
do własnych i wcześniejszych wyników,
9 poprawnie sparowanych dowodów.
Przegląd terminologii nie ujawnił
naruszenia standardów. W stosunku do
przyjętego bloba źródła nie wykonano
żadnej poprawki.

**Status: czysty 1/2.**
