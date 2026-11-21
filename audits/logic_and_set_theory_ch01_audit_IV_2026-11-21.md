# Audyt IV — rozdział 01 „Zdania i spójniki logiczne”

Data: 21 listopada 2026. Punkt wyjścia: bieżąca wersja `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex` z gałęzi `biblioteka-matematyczna-iteracja-6`, porównana z poprawionym źródłem Biblioteki matematycznej. Audyt ograniczony do poprawności obecnego materiału: **bez dodawania twierdzeń i lematów**.

## Usterki i poprawki

1. W definicji warunku koniecznego i wystarczającego odróżniono prawdziwość jednej implikacji przy jednym wartościowaniu od jej prawdziwości we wszystkich dopuszczalnych wartościowaniach.
2. W zdaniu o implikacji przeciwstawnej usunięto nieprawdziwe słowo „jedynie”: w szczególnych sytuacjach również implikacja odwrotna może być równoważna wyjściowej.
3. Zdefiniowano jednoznaczny skrót zapisu koniunkcji wielu przesłanek poprzez rekurencyjne nawiasowanie od lewej. Zachowano istniejące kryteria wynikania i ich etykiety.
4. Uściślono fragment dowodu jednoznaczności wartościowania, opisując odzyskiwanie bezpośrednich podformuł z poprawnie nawiasowanej formuły.
5. W dowodzie praw de Morgana i dowodzie praw implikacji odróżniono cztery **możliwe pary wartości** od czterech wartościowań: dla formuł ze wspólnymi literami część par może być nieosiągalna.
6. W definicji wynikania logicznego jawnie zaznaczono, że wszystkie przesłanki i wniosek rozpatruje się przy jednym wspólnym wartościowaniu liter.
7. Poprawiono układ wierszy bez zmiany znaczenia tekstu.

## Audyt kontrolny po poprawkach

- W tekście pozostało **10 twierdzeń**, tyle samo co przed audytem, bez nowych lematów i bez zmiany nazw żadnych z **31 etykiet**.
- Tablice prawdy, de Morgan, negacja implikacji, przeciwstawienie, podwójna negacja, rozdzielność, modus ponens, modus tollens, sylogizm rozłączny, przechodniość, sprzeczne przesłanki i przypadek zerowej liczby przesłanek: testy enumeracyjne zakończone sukcesem.
- Spójność zapisu nawiasów i przypadków `n=0` i `n≥1` w istniejących kryteriach wynikania — bez stwierdzonych dalszych luk.
- Zależności plikowe rozdziału: brak zewnętrznych plików graficznych i kodu; schemat składni jest TikZ.
- W lokalnym pełnym skrypcie: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` zakończył się z kodem `0`, **376 stron**, **44 rozdziały**, **1075 unikatowych etykiet**, **866 odsyłaczy**, bez nieistniejących celów i duplikatów etykiet. W pozostałych partiach pełnego skryptu występują nieblokujące ostrzeżenia dotyczące zakładek PDF (`hyperref`) i nielicznych słabo wypełnionych wierszy; nie są błędami kompilacji.
- Lokalny osobny skład rozdziału również przeszedł z kodem `0`; ostrzega tylko o odsyłaczu `ch:syntax-fol` do rozdziału 09, niezarejestrowanego jeszcze w tym repozytorium. Osobny dziewięciostronicowy PDF przygotowano z kompletnego składu, w którym odsyłacz ten jest poprawnie rozwiązany.
- Kontrola obrazów stron 4–11 osobnego wydania: brak zauważonych konfliktów elementów i nakładania się napisów na rysunek.

## Status

**Audyt IV zakończony.** Po niezależnym ponownym sprawdzeniu naniesionych zmian nie znaleziono kolejnych usterek wymagających zmiany treści. Nie jest to formalna certyfikacja wszystkich twierdzeń logiki klasycznej ani pozostałych rozdziałów.
