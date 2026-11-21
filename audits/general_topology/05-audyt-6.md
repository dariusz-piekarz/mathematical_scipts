# Topologia ogólna — rozdział 05 — audyt 6

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.4, bez zmian merytorycznych ani redakcyjnych.  
**SHA-256 źródła:** `df9bcff25e15af3ae087a94b03af69d94152b70380a7a74533e43a98b57bb1af`.  
**Wynik:** pierwszy czysty audyt po wprowadzeniu przykładu Mysiora (**1/2**).

## Zakres

Przeczytano cały rozdział (992 wiersze) ze szczególną weryfikacją:

1. Dokładnych definicji i konwencji T0, T1, T2, regularności, T3, całkowitej regularności, Tychonoffa i T4; przypadków pustych.
2. Dowodu regularności przestrzeni Mysiora: zgodności baz otoczeń, skończoności przecięć B_x∩B_z, otwarto-domkniętości B_x\E oraz zawierania cl(W_{n+2})⊆W_n.
3. Dowodu braku całkowitej regularności Mysiora: przeliczalnych zbiorów wyjątkowych, indukcji na A_k i granicy w punkcie ∞. Konstrukcję porównano z klasycznym opisem konstrukcji Mysiora.
4. Dowodu lematu Urysohna: rekurencyjnego zwężania otwartych otoczeń, obu wzorów na przeciwobrazy otwartych półprzedziałów.
5. Trzech kroków twierdzenia Tietzego: oszacowania 2M/3, zbieżności jednostajnej i przedłużenia funkcji nieograniczonych przy pomocy homeomorfizmu R→(-1,1).
6. Pięciu kontrprzykładów dla ścisłych implikacji T0–T4, w tym argumentu kardynalnego dla płaszczyzny Sorgenfreya.
7. Rysunków T1/T2, regularności, Mysiora, Tietzego i hierarchii, spójności opisów, terminologii, etykiet i odsyłaczy.

## Testy i skład

- `bash tools/validate_general_topology_ch05.sh`: **PASS**.
- Łącznie 390 topologii na zbiorach 0–4 punktów, 5931 testów podprzestrzeni, 4133 kontroli par domkniętych zbiorów: **PASS**.
- 7688 testów przedłużania funkcji na skończonych przestrzeniach normalnych: **PASS**.
- Kompilacja osobnego rozdziału: **10 stron**, LaTeX bez ostrzeżeń.
- Kompilacja książki z rozdziałami 01–05: **46 stron**, LaTeX bez ostrzeżeń.
- Kontrola obrazów PDF: **PASS**.
- Etykiety i odsyłacze: **PASS** (43 etykiety, 15 odsyłaczy wewnątrz rozdziału).

## Wnioski

Nie znaleziono błędu, nieścisłości ani problemu składu wymagającego zmiany aktualnej wersji. **Pierwszy czysty audyt (1/2)**. Nie wykonano pushu rozdziału 05 — następny audyt 7 ma być drugim niezależnym czystym przebiegiem.

## Propozycja do osobnej decyzji — bez zmian w tekście

Warto rozważyć **twierdzenie o zanurzaniu każdej przestrzeni Tychonoffa w kostkę [0,1]^I**. Naturalnie łączy ten rozdział z własnościami uniwersalnymi iloczynu i z przyszłym twierdzeniem Tychonoffa o zwartości. Przypisać ewentualnie do rozdziału o osadzeniach/zwartości, by nie rozbudowywać obecnego rozdziału bez zgody.
