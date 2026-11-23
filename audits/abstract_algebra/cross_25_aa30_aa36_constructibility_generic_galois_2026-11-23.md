# AA-X25 — audyt przekrojowy AA-30 ↔ AA-36: konstruowalność i grupy Galois wielomianów ogólnych

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD ponownie odczytany bezpośrednio przed zapisem:** `8b4d8bb3ab0e9b37222b49f3dc00f054c78a51a4` (zmienił się w trakcie odczytów z początkowego `b0b6f4ef44ae40980653cfc7667d92d2bc208dd2`; zapis nowego raportu nie nadpisuje źródeł).

## Stan i zakres
Pełne drzewo GitHub (2409 wpisów, `truncated=false`) potwierdza 50 plików źródłowych AA-01–AA-50, brak AA-51 i raporty przekrojowe do AA-X24. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/konwencje_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `catalog/books.json`, `books/pl/abstract_algebra.tex`, ostatni raport AA-X24 i źródła AA-30/AA-36. Audyt X25 nie powtarza X24 (Eisenstein/cyklotomiczne) ani X11 (ciała skończone/konstrukcje): dotyczy granicy pomiędzy kryterium konstruowalności a twierdzeniem o grupie Galois wielomianu ogólnego.

Źródła: AA-30 blob `f9d6e4e96d41e3faba57f9c9f895c99611c12998` (536 wierszy); AA-36 blob `4c7f5c055172ff88331978592b89d4c44d5584dc` (301 wierszy). Brak zmian źródeł.

## Kontrola matematyczna
1. AA-30, wiersze 205–217: konstruowalność liczby rzeczywistej implikuje stopień będący potęgą 2, lecz implikacja odwrotna jest fałszywa. Wiersze 267–386 dają konkretny wielomian `f=X^4-X-1`: nierozkładalny stopnia 4, ale o grupie Galois `S_4`, zatem żaden jego rzeczywisty pierwiastek nie jest konstruowalny. Kluczowe jest użycie **domknięcia normalnego wieży kwadratowej**, a nie nieuprawnionego twierdzenia, że każda grupa Galois wielomianu stopnia `2^m` jest 2-grupą.
2. Niezależnie sprawdzono rozkład `f mod 7=(X-3)(X^3+3X^2+2X-2)`, nierozkładalność czynnika sześciennego nad `F_7`, nierozkładalność `f mod 2`, nierozkładalność rezolwenty `R=Y^3+4Y-1` nad `Q`, a także `disc(f)=disc(R)=-283`. Każdy z tych faktów zgadza się z AA-30, wiersze 273–370. Rozumowanie o rzędzie grupy (podzielność przez 3 i 4, następnie transpozycja wykluczająca `A_4`) jest poprawne.
3. AA-36, wiersze 54–117: dla algebraicznie niezależnych `t_i` i dowolnego ciała `k` grupa Galois ogólnego wielomianu monicznego stopnia `n≥2` jest `S_n`; niezależność pierwiastków `x_i` zapewnia rozdzielczość także w dodatniej charakterystyce. Nie wolno przenosić tego twierdzenia bezpośrednio na **dowolną specjalizację współczynników**. AA-30 podaje szczególny, osobno sprawdzony przykład `S_4`, a nie wniosek ze specjalizacji ogólnego `S_4`.
4. Dla `n≥5` nierozwiązalność `S_n` przez pierwiastniki z AA-36 nie jest tożsama z niemożliwością konstrukcji cyrklem i linijką. Dla `n=4` grupa `S_4` jest rozwiązalna, ale nie jest 2-grupą: przykład AA-30 poprawnie rozdziela te pojęcia.
5. AA-30, wiersze 402–483: kryterium `φ(n)` będącego potęgą 2 dla wielokątów foremnych wykorzystuje **abelowość** grupy cyklotomicznej i wieżę podgrup indeksu 2, a nie jedynie liczbową przeszkodę stopnia. Niezależny test dla `3≤n≤100` potwierdził 98 klasyfikacji na podstawie faktoryzacji `n`; nie zastępuje dowodu ogólnego.
6. Niezależne obliczenia w Python/SymPy, wykonane w tej iteracji: **6 testów podstawowych** (nierozkładalności, wyróżniki, rozkład modulo 7) oraz **11 kontroli stopni formalnych wielomianów ogólnych** i **98 klasyfikacji n-kątów**, wszystkie zakończone bez błędu. Testy formalnych stopni nie są dowodem twierdzenia Galois.

## Statusy
- **Matematyka (wybrany interfejs AA-30/AA-36):** nie znaleziono sprzeczności w kontrolowanych twierdzeniach, hipotezach i przykładzie `X^4-X-1`. Nie jest to pełny ponowny audyt wszystkich dowodów tych dwóch rozdziałów.
- **Terminologia:** w analizowanych fragmentach nie stwierdzono naruszeń odczytanych zasad. **Odsyłacze:** kontrola logiczna wybranych zależności; nie przeprowadzono pełnego testu wszystkich `\\label`/`\\ref` w książce.
- **Nowa kompilacja LaTeX:** NIE WYKONANO. **Wizualna inspekcja PDF:** NIE WYKONANO. **Nowe CI:** NIE URUCHOMIONO / NIEZWERYFIKOWANO. Żaden z tych statusów nie jest PASS.
- **Korekty:** 0. **Stabilność:** brak nowej deklaracji.

## Propozycje bez zmiany zatwierdzonych rozdziałów
Opcjonalnie dodać do AA-36 krótkie porównanie „rozwiązywalność przez pierwiastniki” versus „konstruowalność cyrklem i linijką” z odsyłaczem do kontrprzykładu `X^4-X-1` z AA-30. Wymaga osobnej zgody.

**Następny krok:** ponownie odczytać HEAD i obecność AA-51; przy dalszym braku źródła wybrać nowy, niepowtórzony audyt przekrojowy z naciskiem na kompletność hipotez dowodów. Osobno uruchomić pełną kompilację i inspekcję PDF w środowisku z dostępnym checkoutem i zależnościami.
