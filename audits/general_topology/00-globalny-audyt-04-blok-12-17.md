# Topologia ogólna — globalny audyt 04, blok 12–17

**Data:** 2026-11-22.
**Zakres:** tematyczne, niezależne sprawdzenie reprezentatywnych
dowodów z rozdziałów 12–17. Nie obejmuje wszystkich
dowodów źródłowych. Nie zmieniono plików 12–17.

## Struktury jednostajne i zupełność (12–13)

- W twierdzeniu o strukturze jednostajnej pochodzącej od
  pseudometryki (12) relacje E_epsilon zawierają przekątną,
  mają odpowiednią symetrię, relacje złożenia
  E_{epsilon/2}∘E_{epsilon/2}⊂E_epsilon,
  a topologia jest określona przez kule
  E_epsilon[x]. Rozdzielanie następuje wtedy i tylko
  wtedy, gdy pseudometryka rozdziela różne punkty.
  Przykład d(x,y)=|x-y| i
  e(x,y)=|arctan x-arctan y| jest rzeczywistym
  kontrprzykładem identyczności struktur jednostajnych
  dla metryk wyznaczających tę samą topologię.
- W konstrukcji uzupełnienia jednostajnego (13)
  za punkty przyjęto minimalne filtry Cauchy'ego.
  Przejrzano definicję \hat E przez świadków
  A×B⊂E, argument przekątnej i złożenia relacji
  oraz zanurzenie x↦N_x i jego gęstość.
  W lemacie o rozszerzaniu z gęstej podprzestrzeni
  filtr otoczeń z∈Z daje filtr Cauchy'ego na A,
  a jednostajnie ciągły f przenosi go do filtru
  Cauchy'ego w zupełnej, rozdzielającej Y.
  Jednoznaczność korzysta z Hausdorffowości Y.
  Jest to audyt kluczowych kroków, nie potwierdzenie
  każdego technicznego argumentu minimalizacji filtrów.

## Zwartość lokalna i metryzowalność (14–15)

- W rozdziale 14 lemat o otoczeniu z zwartym
  domknięciem wymaga **zarówno** lokalnej zwartości,
  jak i własności Hausdorffa. Lokalnie zwarta
  Hausdorffa X ma otoczenia W o zwartym
  domknięciu zawartym w dowolnym otwartym V.
  Dowód Baire'a z zstępujących zwartych
  domknięć nie opiera się na zupełności metrycznej.
  Ten sam lemat jest jawnie stosowany później
  w rozdziałach 21–22.
- W rozdziale 15 twierdzenie Nagaty–Smirnowa
  ma poprawne wymaganie regularności T1 oraz
  bazy będącej **przeliczalną sumą rodzin lokalnie
  skończonych**, a nie po prostu bazy przeliczalnej.
  Przejrzano konieczność dla metryk (pokrycia kulami
  o promieniach 2^{-n}, rozdrobnienie lokalnie skończone
  ze Stone'a) oraz zasadniczą konstrukcję
  wystarczalności: z lokalnej skończoności
  i zwężania otoczeń zbudowano normalność
  oraz funkcje g_G dodatnie dokładnie na G.
  Następnie odwzorowanie F do \ell^\infty(J)
  jest ciągłe dzięki skończonej liczbie
  aktywnych B∈B_n lokalnie przy punkcie
  i jednostajnie małym ogonom n≥N.
  Pełną kontrolę wszystkich szczegółów
  izometrycznego/metryzowalnego osadzenia
  zachowano jako kolejny etap.

## Uzwarcenia (16–17)

- Rozdział 16 definiuje relację porządku na
  uzwarceniach przez istnienie zgodnej ciągłej
  surjekcji, wykazuje jednoznaczność takiej
  surjekcji z gęstości X, a antysymetrię
  uzyskuje *dopiero na klasach równoważności*.
  Przykład dwóch uzwarceń (0,1) przez
  [0,1] oraz S¹ jest poprawny: oba końce
  w pierwszej przestrzeni musiałyby przejść
  na jeden punkt okręgu przy zgodnym
  odwzorowaniu, co wyklucza homeomorfizm.
- W rozdziale 17 uzwarcenie Čecha–Stone'a
  jest określone jako domknięcie obrazu X
  w kostce wszystkich C(X,[0,1]).
  Dla ciągłego f:X→L o zwartej Hausdorffa
  przeciwdziedzinie L przedłużenie
  skonstruowano przez współrzędne
  \(\Phi(z)_g=z_{g\circ f}\);
  ich ciągłość i gęstość obrazu X
  gwarantują, że \(\Phi(\beta X)\)
  leży w zamkniętym obrazie L.
  Maksymalność wynika z tej własności
  uniwersalnej i surjektywności obrazu
  zwartego zawierającego gęsty obraz X.
  Nie dubluje to podstawowych definicji
  z rozdziału 16.

## Odsyłacze i logiczna kolejność

Rozdziały 12–13 dostarczają języka
struktur jednostajnych i uzupełnień,
14 dostarcza lokalnej zwartości,
15 niezależnego kryterium metryzowalności,
a 16–17 badają ogólne i szczególne uzwarcenia.
Nie znaleziono przesłanki wykorzystanej
bez odpowiedniego wcześniejszego pojęcia.

**Wynik próbki:** brak ujawnionych błędów.
Pozostaje do zrobienia pełna kontrola
wszystkich dowodów, przykładów i rysunków;
następny blok tematyczny: 18–22.
