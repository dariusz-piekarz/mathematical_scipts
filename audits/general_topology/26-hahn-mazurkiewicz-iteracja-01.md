# Topologia ogólna — rozdział 26: audyt 01 (korekcyjny)

**Data:** 2026-11-22. **Blob po korektach:** `f80742efe86ff1e29b38b8be921224573ae94a42`.
**Status:** 0/2; źródło nadal w audycie matematycznym
i wizualnym. Utrzymujemy rozdziały 01–25 jako stabilne.

## Zakres i zależności

- Rozdział 25 zawiera definicję continuum Peana,
  granice odwrotne, Knastera, solenoid i konstrukcje
  krzywych Peana na sześcianach. Rozdział 26
  nie kopiuje ich dowodów, tylko przeprowadza
  **ogólne** twierdzenie Hahna–Mazurkiewicza
  w obu kierunkach.
- Rozdział 08 zawiera podstawy spójności,
  lokalnej spójności oraz charakteryzację przez
  otwarte składowe zbiorów otwartych.
- Rozdział 10 ma twierdzenie Urysohna
  o metryzowalności; użyto go jawnie,
  zamiast ponownie budować metrykę.

## Audyt argumentów

1. Z lokalnej spójności wybieramy otwarte spójne
   otoczenia o średnicach <ε.
   Dzięki zwartości można wybrać skończenie wiele
   kul B(x_i,r_i), których podwojone promienie
   nadal mieszczą się w otoczeniach. Jeden
   δ=min r_i działa dla wszystkich bliskich par.
2. W dowolnym spójnym zbiorze metrycznym
   każda para punktów jest połączona skończonym
   δ-łańcuchem: zbiór punktów osiągalnych
   takimi łańcuchami jest otwarto-domknięty.
3. Dowód istnienia małych dróg nie zakłada
   ich wcześniej. Każdy odcinek parametru
   zastępowany jest co najmniej dwoma
   mniejszymi odcinkami, a nowym
   punktom przypisujemy wartości w spójnym
   zbiorze średnicy <ε_n.
   Sumy ogonowe Σ_{k≥n}ε_k dają
   kontrolę oscylacji na każdym odcinku
   podziału. Jednostajnie ciągłe odwzorowanie
   ze zbioru gęstego przedłuża się dzięki
   zupełności X; obraz drogi ma małą średnicę.
4. Z małych dróg wynika otwartość
   składowych drogowych dowolnego zbioru
   otwartego, a z wcześniejszego twierdzenia
   rozdziału 08 — lokalna spójność drogowa.
   Spójność daje spójność drogową.
5. W lemacie o krótkich wycieczkach
   wybór disjoint małych przedziałów
   parametru jest możliwy, bo punktów
   t_y jest skończenie wiele.
   Pętle zaczynają się i kończą
   w starym punkcie trajektorii;
   wstawienie ich nie zmienia wartości
   na końcach całego odcinka.
   Błąd jednostajny jest <2ε.
6. Konstrukcja surjekcji wybiera
   w każdej iteracji skończoną
   δ_{n+1}/2-sieć; bliskość jej punktów
   do poprzedniej krzywej umożliwia
   dołączenie pętli małej średnicy.
   Ograniczenie Σ2ε_n<∞ daje
   granicę jednostajną, a zbieżność
   δ_n→0 zapewnia gęstość obrazu
   granicznego; zwartość odcinka
   daje domkniętość obrazu i surjekcję.
7. W kierunku koniecznym
   nie zakładamy wcześniej
   metryzowalności przestrzeni docelowej.
   Skończone sumy elementów przeliczalnej
   bazy odcinka dają otwarte W_V =
   X\ f([0,1]\V); odpowiednie W_V tworzą
   przeliczalną bazę X. Metryzowalność
   wynika dopiero z Urysohna.
8. W dowodzie lokalnej spójności obrazu
   dobieramy skończenie wiele domkniętych
   podprzedziałów, których obrazy są spójne
   i mają wspólny punkt x. Ich suma
   K zawarta w zadanym O jest spójna,
   a zbiór W = X\ f([0,1]\V)
   jest otwarty, zawiera x i leży w K.
   Stąd każda składowa spójna O jest otwarta.
9. Główne twierdzenie jest sformułowane
   dla **niepustych przestrzeni Hausdorffa**;
   brak T2 nie jest ukryty. Zwartość,
   spójność, lokalna spójność i metryzowalność
   są wszystkie jawnie wymagane.

## Wykryte i poprawione błędy

- W pierwszym szkicu błędnie stwierdzono,
  że zbiór Cantora jest lokalnie spójny.
  To fałsz: Cantor jest całkowicie niespójny
  i nie ma izolowanych punktów.
  Zamieniono przykład na dwupunktową
  przestrzeń dyskretną (lokalnie spójna,
  ale niespójna) oraz poprawnie wyjaśniono
  własności zbioru Cantora.
- Zamiast niepoprawnego lub nieinformacyjnego
  kontrprzykładu bez aksjomatu Hausdorffa
  podano jawny ciągły obraz odcinka
  w dwupunktową przestrzeń Sierpińskiego:
  f(0)=0, f(t)=1 dla t>0;
  preobrazem otwartego singletonu {1}
  jest (0,1], otwarty względnie w [0,1].
  Przestrzeń Sierpińskiego nie jest T2,
  a więc nie jest metryzowalna.

## LaTeX i integracja

23 unikatowe etykiety, 24 odsyłacze
(w tym do rozdziałów 08, 10 i 25),
9 środowisk dowodu, jeden rysunek
schematyczny krótkich wycieczek.
Sparowane środowiska LaTeX,
brak zakazanej terminologii.
Zarejestrowano rozdział i testy
w katalogu i workflow.
Wynik CI oraz inspekcja rzeczywistego
PDF są oddzielnym obowiązkiem przed
oznaczeniem stabilności.

**Po audycie korekcyjnym: 0/2.**
