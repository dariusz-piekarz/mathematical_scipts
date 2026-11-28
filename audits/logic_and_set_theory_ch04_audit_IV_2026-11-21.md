# Audyt IV — rozdział 04 „Pary uporządkowane i relacje”

**Data:** 21 listopada 2026 r.  
**Źródło:** najnowsza na początku audytu wersja `chapters/pl/logic_and_set_theory/04-pary-uporzadkowane-i-relacje.tex` na gałęzi `biblioteka-matematyczna-iteracja-6`, blob Git `c239d2ec5f1e5dbadf30ac1dd11fe1b5a62fccb7`, po audycie III.  
**Zakres:** niezależna ponowna kontrola **wyłącznie już istniejącego materiału**. Nie dodawano twierdzeń, lematów, definicji, przykładów ani sekcji. **Nie wprowadzono żadnej zmiany w pliku `.tex`.**

## Ponowny przegląd matematyczny

Sprawdzono wszystkie **12 twierdzeń, 3 lematy, 15 dowodów, 11 definicji, 17 przykładów i 6 uwag**. Weryfikacja objęła:

- konstrukcję par Kuratowskiego, w tym przypadek jednakowych współrzędnych, oraz osadzenie iloczynu kartezjańskiego w zbiorze potęgowym zbioru potęgowego;
- dziedziny, zbiory wartości, obrazy i przeciwobrazy relacji, rozróżnienie jednoznaczności lewo- i prawostronnej oraz równoważność ze wzorami na przecięcia;
- składanie relacji, relacje identycznościowe, odwracanie składania i łączność, również w przypadkach zbiorów pustych;
- zwrotność, przeciwzwrotność, symetrię, antysymetrię, asymetrię, przechodniość i ich charakteryzacje;
- ścieżki długości zero, potęgi relacji, minimalność domknięć zwrotnych, symetrycznych, przechodnich, zwrotno-przechodnich oraz relacji równoważności generowanej przez relację;
- iloczyn boolowski macierzy relacji, konwencję pustych wyliczeń oraz macierz relacji odwrotnej, łącznie z macierzami o zerowej liczbie wierszy lub kolumn.

W szczególności ponownie oceniono miejsca poprawione w audytach I–III: jawność wszystkich zbiorów w tezie, interpretację antysymetrii, dziedzinę mnożnika w podzielności liczb całkowitych i puste wyliczenia w części macierzowej. **Nie znaleziono nowego błędu w sformułowaniach, dowodach ani przykładach**. Wszystkie oryginalne 35 etykiet pozostają niezmienione.

## Niezależne kontrole obliczeniowe

Wykonano od nowa:

1. **187 714** kontroli semantycznych własności relacji, obrazów, przeciwobrazów, potęg i złożenia na skończonych zbiorach (rozmiary 0–3; potrójne złożenia na zbiorze dwuelementowym) — wszystkie zaliczone.
2. **499** kontroli macierzowego składania i odwracania relacji we wszystkich 27 konfiguracjach rozmiarów zbiorów od 0 do 2, z przypadkami pustymi — wszystkie zaliczone.
3. **16 197** *dodatkowych* kontroli minimalności domknięć, wyczerpujących wszystkie relacje na zbiorach rozmiarów 0–3 i wszystkie sprawdzane nadrelacje spełniające odpowiednią własność — wszystkie zaliczone.

**Łącznie 204 410 pozytywnych kontroli pomocniczych.** Wyliczenia skończone nie stanowią dowodu dla zbiorów dowolnych; każdy dowód skontrolowano również matematycznie.

## Kompilacja, etykiety, odsyłacze, układ

- **Ponowna pełna kompilacja wymuszona** (`latexmk -g -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`): kod 0, **44 rozdziały, 376 stron**. W pełnym tekście **1075 unikatowych etykiet**, **866 odsyłaczy**, **0 powielonych etykiet**, **0 nierozwiązanych odsyłaczy**, **0 przepełnionych wierszy**.
- Ponowna kompilacja częściowej książki repozytoryjnej 01–04 (`latexmk -g -pdf ...`): kod 0, **41 stron**, bez przepełnionych wierszy. Pozostałe odsyłacze do `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms` są nieaktywne **tylko w częściowym imporcie**. Wszystkie cztery cele istnieją w pełnym skrypcie; etykiet nie zmieniano.
- Rozdział 04 ma dokładnie **35/35 oryginalnych etykiet**, bez ich duplikacji czy zmiany kolejności. Żadne środowisko twierdzenia, lematu, definicji, dowodu lub przykładu nie zostało dodane ani usunięte.
- Wycięto z nowego PDF pełnego składu i wyrenderowano wszystkie **10 stron** rozdziału 04 (strony 42–51 pełnej książki). Skontrolowano tekst, wzory, oba diagramy TikZ i rozmieszczenie etykiet; nie zauważono nakładania się, obcięcia ani innych defektów wizualnych.
- Zawartość źródła wykorzystanego do testów jest bajtowo zgodna z kanonicznym blobem Git wskazanym powyżej.

## Status — zamknięcie

**Audyt IV wykonano bez wykrycia nowych usterek. Rozdział 04 uznaje się za stabilny i zamknięty po czterech iteracjach.** W bieżącej iteracji publikuje się wyłącznie raport kontroli, bez modyfikacji pliku źródłowego. Kolejny audyt powinien dotyczyć rozdziału 05, w takim samym cyklu wielokrotnych przeglądów. GitHub CI ostatniej zmiany źródłowej zostało wcześniej potwierdzone jako zakończone sukcesem; publikacja raportu wymaga osobnego sprawdzenia przebiegu CI, jeśli został uruchomiony.
