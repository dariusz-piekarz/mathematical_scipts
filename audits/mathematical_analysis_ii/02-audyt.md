# AM II 02 — audyt otwarty

## Zakres i źródła
Rozdział 02 rozwija wyniki AM I 09 o szeregach liczbowych na przestrzenie unormowane i przestrzenie Banacha, korzystając z ustabilizowanego rozdziału AM II 01. Zachowano etykiety rozdziału 01; dla nowych, uogólnionych twierdzeń zastosowano odrębne etykiety ma2, nie kopiując etykiet twierdzeń skalarnych pod zmienione tezy. Skrypt źródłowy AM I pozostaje bez zmian.

Zakres: sumy częściowe, warunek konieczny i kryterium Cauchy'ego, liniowość i ogony, operatory ciągłe, współrzędne w skończonym wymiarze, szeregi geometryczne i teleskopowe, grupowanie kolejnych wyrazów, zbieżność bezwzględna, oszacowanie reszty, charakteryzacja zupełności, kontrprzykład c00, majoranty oraz kryteria ilorazowe i pierwiastkowe. Przestawienia i zbieżność bezwarunkowa pozostają w rozdziale 03.

## Pierwszy audyt szczegółowy
Wersja początkowa: 6fd70d8321275d63aa0799f231238322aebee197 (400 wierszy).
Wersja po poprawkach: ad562382a42cc01c46c35e1deedac21b383fc060 (429 wierszy).
Doprecyzowano tezę o zbieżności kombinacji liniowej, przypadek wymiaru zerowego, dowód oszacowania przez majorantę z kontrolą skończonego początku i ogona, użycie kryterium progowego limsup/liminf, indukcję w dowodzie kryterium rozbieżności, wybór i własności indeksów podciągu w charakteryzacji zupełności oraz kwantyfikację oszacowania reszty. Zweryfikowano, że zupełność jest wymagana dla implikacji zbieżności bezwzględnej, ale nie przy warunku koniecznym ani przy przenoszeniu istniejącej sumy przez operator. Rozdział 01 bez zmian.

Kontrola statyczna: 18 etykiet w rozdziale 02, 15 wystąpień odwołań, 11 dowodów, 4 przykłady; brak duplikatów w obrębie obu rozdziałów AM II, brak lokalnych odsyłaczy bez celu, zbilansowane środowiska. Rejestracja w entrypoincie i catalog/books.json wykonana.
 
Status: OTWARTY. Licznik czystych audytów 0/2. Ponowne czytanie po poprawkach, CI aktualnej wersji, kontrola wizualna PDF i audyt kontrolny pozostają do wykonania. Nie przechodzić do rozdziału 03 przed stabilizacją.

## Drugi audyt szczegółowy — wersja e4e551be4672ed4b5dfbe181d37c545743a1975b
Poprzednia wersja ad562382 uzyskała SUCCESS w CI #45664976776. W aktualnej iteracji wzmocniono twierdzenie o grupowaniu do równoważności, dowodząc także konieczności zanikania maksymalnych przyrostów wewnątrz bloków. Dodano wniosek dla ograniczonej długości bloków i kontrprzykład dla nieograniczonej długości z wyrazami dążącymi do zera, sumami bloków równymi zero i sumami częściowymi oscylującymi między 0 i v. Dołączono rysunek TikZ pierwszych trzech bloków. Dodano kontrprzykład w l2 na zbieżność współrzędnościową bez zbieżności w normie oraz przykłady nierozstrzygalności kryteriów ilorazowego i pierwiastkowego przy wartości granicznej 1. Doprecyzowano definicję szeregu od dowolnego indeksu, argument harmoniczny, oznaczenie sumy w twierdzeniu o majorancie oraz geometryczne oszacowanie w kryterium ilorazowym. Rozdział 01 bez zmian; zachowano wszystkie dotychczasowe etykiety rozdziału 02.

Kontrola strukturalna nowej wersji: 558 wierszy, 22 etykiety, 19 wystąpień odwołań, 12 dowodów i 7 przykładów; brak duplikatów w obu rozdziałach AM II i odwołań bez celu, zbilansowane środowiska. CI aktualnej wersji oraz wizualna kontrola PDF pozostają niepotwierdzone. Status OTWARTY, licznik czystych audytów 0/2. Kolejny krok: ponowna kontrola całej treści, w szczególności nowych wyników o grupowaniu, oraz kompilacja i kontrola ilustracji. Nie rozpoczynać rozdziału 03.
