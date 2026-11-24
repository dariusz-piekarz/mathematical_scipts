# AA-58 — audyt II: kryterium macierzowe Cartana

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Commit źródłowy 0412515967d98c267d9c8b9a464f96b2d7367c32, blob 60d74c01b4a281b823b454b924a3dd12e0e18c34.

## Audyt dowodu
Sprawdzono oba kierunki kryterium macierzowego, założenia twierdzeń Engela i Liego, rozkład na uogólnione przestrzenie własne, działanie na blokach Hom(V_j,V_i), interpolację chińskim twierdzeniem o resztach, ślad komutatora i argument nad Q. Uzupełniono 12 fragmentów: jawne założenia o przestrzeni wektorowej, definicja V_i i wykładnik nilpotentności, liniowość Y_f nad K, dwumianowy wzór na część nilpotentną operatora dołączonego, zgodność powtarzających się różnic, podstawienie operatora do kongruencji, korekta sformułowania o potęgach (potęgi operatora, nie wielomianu), obliczenie śladu z cykliczności, jawna suma kwadratów nad Q, końcowa potęga X^d=0, identyfikacja rozszerzeń podprzestrzeni oraz dokładna formuła rozszerzenia formy Killinga. Nie zakłada się Y_f w algebrze ani porządku na K. Sprawdzono przejście do dowolnego ciała charakterystyki zero i kryterium półprostoty. 890 wierszy, zakres niezmieniony.

## Niezależna regresja interpolacji
Dokładna arytmetyka modulo 1009, dwa bloki Jordana o rozmiarach od 1 do 4, wartości własne 0 i g dla g=1,2,4,7, wartości interpolacji 0,3,-3 na różnicach 0,g,-g. Zbudowano wielomian przez CRT, odwracając iloczyn pozostałych czynników w pierścieniu obciętych szeregów względem t-delta. Dla k=2 dim V sprawdzono stały współczynnik i zerowość pozostałych k-1 współczynników przesuniętego wielomianu dla każdej różnicy, następnie działanie p(ad_X) na każdej jednostce macierzowej wszystkich bloków niezależnie przez iterowanie N_i A-A N_j. 64 konfiguracje, 256 bloków, 1920/1920 współczynników kongruencji, 1760/1760 kontroli wektorów bazowych. Regresja modularna weryfikuje konstrukcję wielomianową, NIE dowodzi kryterium Cartana w dodatniej charakterystyce; argument sum kwadratów pozostaje nad Q w dowodzie.

## Integralność i CI
36 odsyłaczy do 21 różnych celów jednoznaczne w AA-56–58, środowiska zrównoważone. Pierwsze CI 45370168311: in_progress, kroki {"success":7,"in_progress":1,"pending":117}; po korekcie [{"id":45370329109,"status":"in_progress","conclusion":null}]. PDF nie oglądano.

## Werdykt
AA-58 W AUDYCIE. Czyste audyty po poprawkach II: 0/2. Kolejna iteracja: forma Killinga, rozkład na ideały proste, derywacje, wzory klasyczne i dokładne niezależne obliczenia macierzy form. AA-59 nieotwarty.
