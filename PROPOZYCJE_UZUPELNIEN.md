# Propozycje po przeglądzie skryptu

## Aktualizacja po pobraniu zmian autora — 5 października 2026

Poniższa pierwotna lista opisuje wersję 18-rozdziałową. W `19fa283`
książka ma już 27 rozdziałów i dodatek. Porównano zmiany od `66b220f`;
nie należy ponownie dopisywać tematów, które autor już wprowadził.
Obecność tekstu i deklaracja wykonania w planie nie zastępują przeglądu
jego dowodów; kontrola nowych fragmentów jest prowadzona rozdziałami.

| Punkt | Co jest już w aktualnej książce | Dalsze działanie |
|---|---|---|
| 1 | Osobna sekcja o brzegu w rozdziale 1, definicja, niezależność od map, przykłady i odsyłacze | Sprawdzono; uzupełniono dowód pełnego wymiaru przestrzeni stycznej przy brzegu i niezależności od przedłużeń |
| 2 | Rozdział 5: grupy, grupy wolne, redukcja słów, iloczyn wolny i prezentacje | Sprawdzić konstrukcje i przejście do van Kampena |
| 3 | Mapa książki, oznaczenia, indeks i uzupełnione lektury | Źródła podzielono i zweryfikowano w `9148128`; pełne ujednolicenie redakcyjne pozostaje osobnym zagadnieniem |
| 4 | Nie dodano zestawów zadań | Pozostają poza aktualnym zakresem zgodnie z zasadami projektu |
| 5 | Dodatek o wynikach zewnętrznych i samowystarczalności | Sprawdzić zgodność deklarowanych zależności z dowodami |
| 6 | Rozdział 27 o Chernie–Weilu i wzorze Cherna–Gaussa–Bonneta | Sprawdzić nową argumentację, normalizacje i wersję brzegową |
| 7 | Rozdział 20 o h-kobordyzmie | Sprawdzić hipotezy ruchów uchwytów i zakres dowodów |
| 8 | Rozdział 21 o torsji Whiteheada i s-kobordyzmie | Sprawdzić konwencje algebraiczne i zależności geometryczne |
| 9 | Rozdziały 22–24: chirurgia geometryczna, przeszkoda i ciąg dokładny | Przejrzeć nowe twierdzenia, przykłady i rysunki |
| 10 | Rozdział 25: wymiar 2 i wysokie wymiary | Sprawdzić założenia i odróżnienie homeomorfizmu od dyfeomorfizmu; wymiar 4 pozostaje poza tym skryptem |
| 11 | Rozdział 26 o sferach Milnora | Zachować i sprawdzić już dodany materiał; nie przenosić go automatycznie do planowanego osobnego skryptu |
| 12 | Nie dodano egzotycznych R⁴ ani teorii Freedmana | Dalsze metody czterowymiarowe autor planuje w osobnym skrypcie |

Nowe pomysły o Hodge'u, holonomii i geometrii podrozmaitości z
`PLAN_DZIALANIA.md` pozostają propozycjami. Pierwszeństwo mają kontrola
już dopisanej treści i usunięcie rzeczywistych luk.

## Pierwotne propozycje (stan przed rozbudową)

Stan: po przeglądzie 18 rozdziałów i ponownej kontroli uzupełnień autora
w rozdziale 1; źródło `a36c920`, PDF 325 stron. Poniższe punkty są
**propozycjami do wyboru**, a nie rozpoczętymi pracami. Numery można podać
przy zlecaniu dalszych zmian. Uwzględniono [listę autora](do_zrobienia.md),
której treści nie zmieniano.

## Najpierw uporządkowanie podstaw

### 1. Rozmaitości z brzegiem: jedna definicja i wspólne konwencje

**Już jest:** konwencja półprzestrzeni i przedłużalności gładkich map
na początku rozdziału 2; orientacja brzegu w 9, transwersalność przy brzegu
w 14, kołnierz i podwojenie w 15, zastosowania w 17–18.

**Proponuję:** w rozdziale 1 osobną definicję z przykładami, niezależnością
brzegu od map i opisem przestrzeni stycznej. Następnie odsyłać do niej
w dalszych rozdziałach. Wyjaśnić różnicę między brzegiem rozmaitości
a brzegiem podzbioru w przestrzeni otaczającej oraz krótko omówić naroża
i ich wygładzanie przy uchwytach. To porządkuje rozproszony materiał.

### 2. Krótki wstęp do teorii grup

**Już jest:** konstrukcja grupy podstawowej i opis słów w iloczynie wolnym
bezpośrednio przy twierdzeniu van Kampena w 6.3; moduły w rozdziale 5.

**Proponuję:** przed częścią algebraiczno-topologiczną zebrać grupy,
homomorfizmy, podgrupy normalne, ilorazy, grupy wolne, iloczyn wolny,
domknięcie normalne i prezentacje. Dodać przykłady redukcji słów oraz
wyprowadzenie prezentacji grupy torusa. Twierdzenie van Kampena będzie
wtedy korzystać z wcześniej objaśnionego języka. Grupy Spin z rozdziału 4
także zyskają czytelny punkt odniesienia.

### 3. Redakcja i nawigacja

**Już jest:** spis treści, liczne odsyłacze i lektury; ich forma nie jest
jednolita, a rozdział 1 ma inny rytm wyjaśnień i wzorów niż dalsze części.

**Proponuję:** ujednolicić styl rozdziału 1, zakończenia rozdziałów
i bibliografię. Dodać spis oznaczeń, indeks pojęć oraz krótką mapę zależności
między rozdziałami. W bibliografii podawać autora, tytuł, konkretną sekcję
i link, zamiast samej nazwy tematu. Zachować rozbudowane przykłady autora.

### 4. Zadania z rozwiązaniami lub wskazówkami

**Proponuję:** po każdym rozdziale kilka zadań o różnej trudności:
rachunek, uzupełnienie argumentu, kontrprzykład po usunięciu założenia
i zadanie łączące wcześniejsze pojęcia. Wybrane rozwiązania umieścić
na końcu. Dobry początek to wspólny zestaw przykładów: sfera, torus,
przestrzenie rzutowe i wstęga Möbiusa, badane kolejno różnymi narzędziami.
To rozbudowa dydaktyczna; obecne przykłady nie stanowią systematycznego
zbioru ćwiczeń.

## Większa samowystarczalność obecnego materiału

### 5. Jawny zestaw wyników zewnętrznych i wybrane dowody w dodatkach

**Już jest:** tekst wskazuje m.in. niezmienniczość wymiaru Brouwera,
twierdzenie o funkcji odwrotnej i twierdzenie o triangulacji gładkich
rozmaitości jako wyniki spoza przeprowadzonych dowodów. Interpretacja
przeszkody spinowej w rozdziale 4 wyprzedza teorię kohomologii Čech.

**Proponuję:** zebrać te zależności w jednym miejscu i ustalić poziom
wiedzy wejściowej. Osobno można zamówić dodatek o triangulacji lub
porównaniu kohomologii Čech i singularnej. Pełny dowód triangulacji to
znaczne rozszerzenie topologii, więc nie traktowałbym go jako krótkiej
poprawki redakcyjnej. Pierwszym krokiem powinien być katalog założeń
i dokładnych odsyłaczy, a następnie wybór dowodów do włączenia.

### 6. Teoria Cherna–Weila i pełne twierdzenie Cherna–Gaussa–Bonneta

**Już jest:** dowód dwuwymiarowego Gaussa–Bonneta, opis Pfaffianu,
kontrole wzoru w wyższych wymiarach oraz topologiczna klasa Eulera.
Pełne twierdzenie Cherna–Gaussa–Bonneta w rozdziale 13 jest oznaczone
jako wynik zewnętrzny, a jego wersja z brzegiem jako schemat.

**Proponuję:** połączyć rozdziały 11, 13 i 16: wielomiany niezmiennicze,
formy charakterystyczne, niezależność klasy od koneksji, transgresja
i identyfikacja formy Eulera z klasą topologiczną. Wersja z brzegiem
wymaga dodatkowo zdefiniowania i wyprowadzenia formy brzegowej.
To konkretny sposób doprowadzenia obecnej zapowiedzi do pełnego dowodu.

## Dalsza topologia różniczkowa

### 7. Pełne twierdzenie Smale'a o h-kobordyzmie

**Już jest:** rozkład uchwytowy, przestawianie wartości krytycznych,
przesuwanie uchwytów, znoszenie pary z jednym przecięciem i opis roli
triku Whitneya. Rozdział 18 nie dowodzi jeszcze pełnego h-kobordyzmu.

**Proponuję:** wyprowadzić istnienie potrzebnych dysków Whitneya
z odpowiednich założeń wymiarowych i spójności, kontrolować ich
obramowania, usunąć skrajne indeksy i przeprowadzić redukcję kompleksu
przez rzeczywiste ruchy uchwytów. Celem jest dyfeomorfizm
W ≅ N₋×[0,1] dla zwartego, gładkiego, po prostu spójnego h-kobordyzmu
o wymiarze W co najmniej 6, z ustaloną identyfikacją dolnego końca.
Warunki drugiego twierdzenia o znoszeniu są dobrze widoczne w
[wykładzie Morgana](https://www.math.columbia.edu/~jmorgan/Lecture_IIIA_hcobordism_Contd.pdf).

### 8. Torsja Whiteheada i twierdzenie o s-kobordyzmie

**Już jest:** wskazanie, że zwykły acykliczny kompleks nad Z nie wystarcza,
gdy grupa podstawowa jest nietrywialna.

**Proponuję:** pierścień grupowy Z[π₁], bazowane kompleksy nakrycia
uniwersalnego, proste równoważności homotopijne, grupę Whiteheada,
definicję torsji i twierdzenie o s-kobordyzmie w odpowiednim zakresie
wymiarów. Najpierw punkt 7, potem rozszerzenie algebraiczne rozdziału 5.
Trzeba oddzielić **torsję Whiteheada** od **triku Whitneya** — są to
różne pojęcia i różne nazwiska.

### 9. Chirurgia: co zmienia operacja i jak dobierać jej dane

**Już jest:** definicja obramowania, operacja na brzegu jako ślad
dołączenia uchwytu, podstawowe przykłady i rachunek charakterystyki Eulera.

**Proponuję:** obliczać wpływ chirurgii na grupę podstawową, homologię
i formę przecięcia; wyjaśnić rolę obramowania na konkretnych przykładach.
Następnie przejść do zabijania klas poniżej wymiaru środkowego.
Pełna teoria przeszkód chirurgicznych byłaby kolejnym, osobnym etapem;
zakres tej rozbudowy można oprzeć na
[książce Ranickiego](https://webhomes.maths.ed.ac.uk/~v1ranick/books/surgery.pdf).

### 10. Twierdzenie Poincarégo: osobne ścieżki dla różnych wymiarów

**Proponuję:** dla n=2 najpierw klasyfikację zwartych powierzchni
i wynikający z niej dowód. Dla gładkich sfer homotopijnych n>5
przeprowadzić argument przez usunięcie dwóch dysków, h-kobordyzm
i ponowne sklejenie, wskazując dokładnie, dlaczego wniosek dotyczy
homeomorfizmu ze sferą. Nie wolno bez dodatkowego argumentu zamienić go
na dyfeomorfizm. Przypadek n=5 wymaga osobnego potraktowania.
[Omówienie Milnora dla Clay](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
wyjaśnia te różnice wymiarowe.

Dla n=4 zaproponowałbym oddzielne omówienie twierdzenia Freedmana,
roli uchwytów Cassona i różnicy kategorii topologicznej oraz gładkiej.
**Gładka hipoteza Poincarégo w wymiarze 4 pozostaje problemem otwartym**;
nie należy planować dopisania jej dowodu. Status potwierdza
[aktualny opis programu Clay](https://www.claymath.org/events/recent-advances-in-low-dimensional-topology/).
Pełne rozwinięcie teorii Freedmana znacznie przekracza obecne przygotowanie
skryptu i wymagałoby osobnego bloku rozdziałów.

### 11. Sfery Milnora i egzotyczne struktury na sferach

**Proponuję:** konkretną konstrukcję wiązek S³ nad S⁴, obliczenia
charakterystyczne i argument rozróżniający struktury gładkie na S⁷.
Następnie można rozważyć grupy sfer homotopijnych. Potrzebne są rozwinięte
klasy Pontriagina i twierdzenie o sygnaturze; sama konstrukcja sklejenia
nie dowodzi egzotyczności. Punktem wyjścia może być
[oryginalna praca Milnora](https://sites.math.rutgers.edu/~feehan/teaching/math866/milnor7sphere.pdf).

### 12. Egzotyczne R⁴

**Proponuję:** osobny blok po wprowadzeniu metod czterowymiarowych:
topologia końców, uchwyty Cassona oraz wyniki Freedmana i Donaldsona,
a następnie wybrany dowód istnienia egzotycznego R⁴ i dokładne wskazanie
wykorzystanych twierdzeń. Istnienie egzotycznych R⁴ i ich bogate rodziny
jest ustalonym wynikiem; zob.
[pracę Gompfa](https://arxiv.org/abs/1705.06644).
Nie wynika ono z samego niepowodzenia triku Whitneya ani z konstrukcji
sfer Milnora. To największy z proponowanych kierunków rozbudowy.

## Sugerowana kolejność

Najpierw **1–3**, aby utrwalić podstawy i ujednolicić książkę.
Potem **7 → 10 (n>5) → 8 → 9**, jeżeli głównym celem jest dalsza
topologia różniczkowa. Punkt **6** przygotuje geometryczną stronę
punktu **11**. Punkt **12** warto zostawić jako osobny projekt rozbudowy.
Zadania z punktu **4** można dodawać po jednym rozdziale równolegle
z wybraną ścieżką. Punkt **5** określa, jak daleko ma sięgać
samowystarczalność skryptu.
