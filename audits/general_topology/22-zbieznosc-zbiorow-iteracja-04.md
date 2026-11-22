# Topologia ogólna — rozdział 22, audyt 04 (dodatkowy, po stabilizacji)

**Data:** 2026-11-22.
**Źródło:** chapters/pl/general_topology/22-zbieznosc-kuratowskiego-wijsman-attouch-wets.tex.
**Blob nadal niezmieniony:** 33765c2bb1b3065f4ad32596795c3d1981b48dda.
**Wynik:** **CZYSTY 3/2** (dwa czyste audyty do stabilizacji + jeden potwierdzający).
Źródło matematyczne nie zostało zmodyfikowane.

## Kontrola granic i kontrprzykładów

- Nie wyprowadzono wniosku, że każda granica Kuratowskiego jest granicą topologiczną dla dowolnej przestrzeni metrycznej. Uogólnienie Wijsman/Kuratowski wymaga dodatkowej właściwości kul, a w Twierdzeniu o Fellu i Kuratowskim występuje lokalna zwartość.
- W dowodzie domkniętości Li/Ls dla arbitralnych F_n punkt y wybiera się z odpowiedniej granicy na podstawie domknięcia tej granicy, nie z F_n. Następnie dopiero stosuje się właściwość trafiania i nierówność trójkąta. Brak niejawnego założenia zwartego otoczenia.
- Dla funkcji odległości na X od niepustego domkniętego F prawdziwe są jednocześnie skończoność wartości i zachowanie 1-lipschitzowskie. Rozszerzona wartość d(x,∅)=∞ występuje wyłącznie w Kryterium Kuratowskiego, gdzie nie wykonuje się niedozwolonego odejmowania ∞−∞.
- Topologia Wijsmana jest indukowana przez całą rodzinę ewaluacji punktowych i odróżnia zbiory domknięte. W przestrzeni ośrodkowej jej metryzacja przez gęste współrzędne nie wymaga zupełności X.
- Ogólna implikacja Wijsman⇒Fell wykorzystuje zwartość testowego C, nie domkniętych kul ambientowych. Dodatnie minimum d(C,F)>0 i skończony wybór punktów x_i daje otwarte otoczenie spełniające ominięcie C. Nie ma przesłanki, że X jest lokalnie zwarta.
- W porównaniu AW/Wijsman właściwość X jest konieczna tylko dla zbieżności jednostajnej na kulach z punktowej zbieżności funkcji 1-lipschitzowskich; kontrprzykład na nieskończonej przestrzeni dyskretnej faktycznie pokazuje ścisłe zawieranie.
- Równoważność Kuratowski/Fell jest dokładnie twierdzeniem dla ciągów w lokalnie zwartej metrycznej X; dowód korzysta z sekwencyjnej zwartości C, nie z ogólnej twierdzy o ciągach w arbitralnych zwartych przestrzeniach topologicznych.
- W głównym twierdzeniu (cztery kryteria) limit F jest niepusty. Dowód Kuratowski⇒Wijsman dla r=d(x,F)>0 wykorzystuje zwartość pojedynczej domkniętej kuli wokół x. Dla r=0 działa samodzielnie przez oszacowanie limsup i nieujemność.
- Model X={p,q}∪{y_n} jest dyskretny z dodatnią minimalną odległością między różnymi punktami, zatem zupełny i lokalnie zwarty. Jego brak właściwości wynika z nieskończonej, ograniczonej, domkniętej i niezwartej podprzestrzeni.
- W R z F_n={0,n} oraz F={0} na każdej ustalonej kuli [-m,m] d(.,F_n)=d(.,F) od pewnego n>2m, mimo d_H(F_n,F)=n. Poprawnie rozróżniono topologię Vietorisa na K(R) od topologii AW ograniczonej do K(R).

## Kontrola techniczna i wizualna

Sprawdzono stabilność bloba 33765c2b... i zgodność 28 etykiet,
20 odsyłaczy, jawnych kwantyfikatorów, terminologii i otoczeń.
W repozytorium istnieją plik rozdziału, osobny entrypoint,
katalog 22 rozdziałów i test regressyjny.

Zielony [CI 45047289481](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047289481)
oraz późniejszy [CI 45047380847](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047380847)
dotyczą tego samego źródła; kompilacja całej książki i osobnego
PDF rozdziału 22 zakończyła się sukcesem, podobnie testy i kontrola logów.
Pobrano PDF z artefaktu ID 14764545206, 7 stron A4.
Wszystkie siedem stron sprawdzono po renderingu.
Nie stwierdzono nachodzenia tekstu na rysunki, uciętych wzorów
ani ostrzeżeń Overfull/Underfull/Missing character w logu.
Poprawiony rozkład stron daje pełne podsumowanie na ostatniej stronie.

## Stan

**STABILNY: 2/2 + 1 dodatkowy audyt, badany niezmieniony blob.**
Zaktualizowano książkę do opisu „Wersja 1.22 — rozdziały 01–22 stabilne”
oraz README. Po zmianie tytułowej wymagane jest jeszcze zielone CI
na commicie obejmującym nową wersję książki i nowy test asercji;
sukcesu tego przebiegu nie zakładamy z góry.
Kolejne rozszerzenia (np. zbieżność Mosco) można jedynie osobno
zaproponować użytkownikowi, bez dodawania ich do stabilnego rozdziału.
