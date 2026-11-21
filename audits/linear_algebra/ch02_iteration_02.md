# Algebra liniowa — rozdział 02, audyt 2

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/02-wymiar-sumy-proste-i-przestrzenie-ilorazowe.tex`  
**Commit rozdziału po audycie:** `95c4c6317bb6185519b545082171c6fc4bd3899b`

## Cel i zakres

Nie poszerzano zakresu materiału: zgodnie z decyzją użytkownika drugi audyt dotyczył wyłącznie **poprawności istniejących twierdzeń, luk w dowodach, niejednoznaczności notacji, kompletności przykładów, języka matematycznego i składu LaTeX**.

Przeczytano całość rozdziału 02 w jego bieżącej wersji, szczególnie:
- nośnik współrzędnych względem bazy, oszacowanie mocy sumy skończonych zbiorów oraz równoliczność dowolnych baz;
- definicje sumy podprzestrzeni i wzór wymiarowy dla dwóch podprzestrzeni, także w przypadku nieskończenie wymiarowym;
- kryteria wewnętrznej sumy prostej, zewnętrzną sumę prostą, jednoznaczność składników i bazy takich sum;
- definicję i konstrukcję ilorazu, warunki równości warstw, niezależność działań od wyboru przedstawicieli, własność uniwersalną;
- konstrukcję dopełnienia algebraicznego i dowód wzoru wymiarowego dla przestrzeni ilorazowej;
- twierdzenie o ilorazie sumy, przykłady z wielomianami i podprzestrzeniami przestrzeni euklidesowych.

## Wykryte usterki i poprawki

### 1. Fałszywe uogólnienie konwencji sumy

Wstęp stwierdzał, że wszystkie sumy indeksowane dowolnymi zbiorami są skończonymi sumami wektorów. Było to sprzeczne z późniejszą notacją \(\sum_{i\in I}\dim_K U_i\), w której występuje suma *liczb kardynalnych*, potencjalnie nieskończona.

Nowe sformułowanie odróżnia:
- sumy wektorów z **wyłącznie skończonym nośnikiem**;
- sumę algebraiczną podprzestrzeni \(\sum_i U_i\), której elementami są skończone sumy wektorów;
- sumę kardynalną \(\sum_i\dim_KU_i\), definiowaną przez moc rozłącznej sumy zbiorów reprezentujących odpowiednie liczby kardynalne.

Zachowano rozróżnienie \(\bigcup_i U_i\) (suma *zbiorów*) i \(\sum_i U_i\) (suma algebraiczna).

### 2. Ukryty krok w dowodzie wzoru wymiarowego \(\dim(U+W)\)

W dowodzie konstruuje się bazę \(C\cup A\cup D\) przestrzeni \(U+W\), gdzie \(C\) jest bazą \(U\cap W\), \(C\cup A\) bazą \(U\), a \(C\cup D\) bazą \(W\).

Wcześniej po wykazaniu \(d\in\operatorname{span}(C)\cap\operatorname{span}(D)\) następowało zbyt szybkie przejście do \(d=0\). Wyjaśniono obecnie, że należy zapisać \(d\) w bazie \(D\) oraz w bazie \(C\), odjąć obie skończone kombinacje i zastosować warunek niezależności liniowej zbioru \(C\cup D\), który ma rozłączne części. Pozwala to wyzerować wszystkie współczynniki, a nie jedynie sam wektor \(d\).

### 3. Niedostatecznie rozpisany argument izomorfizmu a wymiaru

W dowodzie \(\dim_KV=\dim_KU+\dim_K(V/U)\) wcześniej tylko stwierdzano, że izomorfizm \(\Theta:W\to V/U\) przenosi bazę na bazę.

Uzupełniono rozpinanie (surjektywność \(\Theta\) oraz rozkład każdego wektora w bazie \(W\)) i niezależność liniową. Z równości \(\sum_{j\in F}a_j\Theta(w_j)=0\) przechodzimy przez liniowość do \(\Theta(\sum_{j\in F}a_jw_j)=0\), następnie przez iniektywność do \(\sum_{j\in F}a_jw_j=0\), wreszcie stosujemy niezależność wskazanej bazy. W ten sposób \(\dim_KW=\dim_K(V/U)\) jest jawnie uzasadniona.

### 4. Nieuprawniony wniosek o „niekanoniczności” dopełnienia

Przykład \(U=\mathbb R\times\{0\}\subseteq\mathbb R^2\) daje dwa różne dopełnienia \(W_1\neq W_2\). Poprzedni tekst wyprowadzał z tego mocniejszą tezę o braku wyróżnionego dopełnienia tylko z danych \(U\subseteq V\). Sam fakt istnienia wielu dopełnień nie wystarcza do wykazania, że nie istnieje konstrukcja naturalna.

Nowy tekst ogranicza wniosek do właściwego stwierdzenia: **dopełnienie algebraiczne nie jest jednoznacznie wyznaczone** przez dane \(U\subseteq V\). Wyraźnie odróżniono ten fakt od ewentualnego osobnego twierdzenia o konstrukcji naturalnej.

### 5. Precyzja przypadku skończonej bazy

W dowodzie równoliczności dowolnych baz sformułowanie „skończona niezależna podrodzina \(C\)” zastąpiono wyraźnym kwantyfikatorem: dla każdego **skończonego podzbioru** \(F\subseteq C\) niezależność bazy \(C\) i lemat Steinitza dają \(|F|\leq|B|\). Jeśli \(|C|>|B|\), wybieramy \(|B|+1\) różnych elementów \(C\), co jest sprzeczne z poprzednim oszacowaniem.

## Weryfikacja innych części

- **Równoliczność baz nieskończonych:** podstawa rozumowania jest poprawna; używany jest znany wynik arytmetyki kardynalnej \(|I\times\mathbb N_0|=|I|\) dla nieskończonego \(I\), **jawnie oznaczony w tekście jako importowane twierdzenie ZFC**. Jego dowód nie jest prezentowany w tym rozdziale i należy do teorii mnogości, nie do algebry liniowej.
- **Suma prosta:** kryterium przez jednoznaczność rozkładu oraz przecięcie \(U_j\) z sumą pozostałych podprzestrzeni jest poprawne, w tym dla pustego \(I\).
- **Iloraz:** sprawdzono trzy równoważne kryteria równości warstw i niezależność działań od przedstawiciela.
- **Istnienie dopełnienia:** poprawne przy aksjomacie wyboru; przypadek skończenie wymiarowy ma osobne uzasadnienie bez użycia aksjomatu wyboru.
- **Twierdzenie o ilorazie sumy:** jawnie wykazane liniowość, dobra określoność, iniektywność i surjektywność.

## Kontrole techniczne

Po zmianach:
- rozdział 01 ma **69**, a rozdział 02 **39** etykiet; łącznie **108**, bez powtórzeń;
- brak nieodnalezionych lokalnych i międzyrozdziałowych odsyłaczy `\\ref` i `\\eqref`;
- środowiska LaTeX są zrównoważone;
- brak niedozwolonych sformułowań „unia” i „relacja liniowa” poza stabilnymi historycznymi identyfikatorami etykiet;
- żadnych nowych zależności od zewnętrznych plików graficznych;
- wcześniejszy CI po pierwszym audycie: [44894556217](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44894556217) — **success**;
- CI aktualnego tekstu: [44895315252](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44895315252) — **success**. Wszystkie etapy kontroli źródeł, kompilacji LaTeX, sprawdzenia odsyłaczy i eksportu PDF zakończyły się powodzeniem. Końcowy PDF zawiera **27 stron**. W końcowym pliku `linear_algebra.log` nie znaleziono `LaTeX Warning`, `Overfull`, `Underfull`, `Missing character` ani `Undefined control sequence`. W logu zadania występują przejściowe ostrzeżenia z pierwszego przebiegu LaTeX, które zniknęły po kolejnych przebiegach. Wizualnie sprawdzono strony **19, 20, 24, 25 i 26**: nowo rozszerzone dowody oraz rysunek warstw nie wykazują kolizji ani ucięcia tekstu.

Nadal występują wcześniejsze problemy globalnej walidacji innych skryptów, raportowane oddzielnie. Nie uznajemy ich za naprawione.

## Decyzja

**Audyt 2 wykrył i naprawił nieścisłości oraz luki w dowodach.** Zakres rozdziału nie został rozszerzony. Rozdział 02 pozostaje otwarty; następny cykl to audyt 3 jego poprawności oraz składu.
