# Logika matematyczna i teoria mnogości — rozdział 30, audyt II

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`.

## ZF i rachunek rang w grach otwartych

W pierwszej wersji krótszego TeX dowód determinacji gier otwartych zawierał nieuzasadnione skróty dotyczące stabilizacji procesu, rang pozycji i doboru strategii. W audycie II rozpisano cały dowód etapami:

1. Dla drzewa skończonych pozycji `T=ω^{<ω}` podano dokładny wzór `W_{α+1}` z alternatywą egzystencjalną na pozycjach gracza I i uniwersalną na pozycjach gracza II, zachowując poprzednie etapy; na granicznych ordynałach bierze się sumy.
2. Jawnie zastosowano twierdzenie Hartogsa do `P(T)`; z dobrze uporządkowanego `H(P(T))` pobiera się jego **typ porządkowy**, a nie domyślnie istniejącą „klasę wszystkich ordynałów”. Dla ustalonego dobrego porządku konstrukcja typu porządkowego nie używa AC, co wyjaśnia dowód w rozdziale 28.
3. Gdyby wszystkie kolejne `W_α` były różne, powstałaby iniekcja `θ→P(T)`, sprzeczna z Hartogsem. Po pierwszej równości następuje stabilizacja.
4. Rangi pozycji w `W` wyznaczono jako **najmniejszy etap**, na którym pozycja pojawia się w konstrukcji. Pozycje o randze dodatniej mają rangę następnikową.
5. Strategia I w `W` wybiera najmniejszą liczbę naturalną obniżającą rangę. W ruchach II ranga maleje przy każdej odpowiedzi. Niemożliwość nieskończonego ściśle malejącego ciągu ordynałów wymusza osiągnięcie `W_0`.
6. Poza `W` strategia II wybiera najmniejszego następnika spoza `W`. Jego istnienie wynika z supremum rang wszystkich następców, jeżeli miałyby należeć do `W`.
7. Wniosek o grach zamkniętych udowodniono osobno przez zamianę warunków graczy w operatorze rangowym, bez nieprecyzyjnej sugestii, że wolno po prostu przesunąć pierwszy ruch gry.

**Wniosek:** oba wyniki zachodzą w **ZF**, a wszystkie wybory ruchów są definowalne przez minimum podzbioru `ω`.

## Inne korekty

Odesłanie do nieistniejącego rozdziału `ch:ad-incomparable-cardinals` zastąpiono odsyłaczem do odtworzonego dowodu twierdzenia o zbiorze doskonałym w bieżącym rozdziale. Odesłanie do planowanego `ch:quotient-choice-paradox` zastąpiono nieodsyłaczową informacją o dalszym materiale, nie deklarując jego dowodu.

Zachowano wszystkie pojęcia i przykłady. **Stan po audycie II:** 12 definicji, 7 przykładów, 15 twierdzeń, 9 lematów, 4 wnioski, 15 uwag, 26 dowodów, 1 rysunek oraz 57 etykiet.

**Werdykt:** rzeczywiste poprawki dowodów; potrzebny kolejny audyt.
