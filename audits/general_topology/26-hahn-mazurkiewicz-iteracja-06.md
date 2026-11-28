# Topologia ogólna — rozdział 26, audyt 06 (korekcyjny, druga kontrola składu)

**Data:** 2026-11-22.
**Blob po korekcie:** `161d04d779ae86554f81c11bb24daa842c8dd363`.
**Wynik:** korekta wydawnicza — wymagany ponowny cykl 2/2 + 1.

## Ponowna kontrola PDF po audycie 03

CI 45062480979 zbudowało poprawny technicznie
PDF rozdziału 26, lecz w rzeczywistym
siedmiostronicowym wydaniu ponownie wykryto
osieroconą stronę końcową.
W tej wersji siódma strona zawierała
już **wyłącznie krótkie podsumowanie**;
cała merytoryczna część twierdzenia
mieściła się na stronach 1–6.
Pozostałe strony — zwłaszcza diagram
schematycznej wycieczki na stronie 4 —
były czytelne, bez kolizji.

## Korekta źródła bez strat matematycznych

Usunięto powtórzony przykład
okręgu, skończonych grafów i sześcianów,
które są już pełnoprawnie opracowane
w rozdziale 25 (zwłaszcza twierdzenia
o grafach i krzywych Peana na kostkach).
Nie usunięto żadnego twierdzenia ani
środowiska dowodu.
Pozostają przykłady niezależnych
hipotez: brak lokalnej spójności
(solenoid), brak spójności
(dyskretne dwa punkty), oraz
brak Hausdorffowości
(przestrzeń Sierpińskiego).
Ostatnia sekcja zachowuje
podsumowanie metody konstrukcyjnej.

Rozdział nie powiela wcześniejszych
opisów grafów i sześcianów,
a jego zakres pozostaje ścisłym
dowodem ogólnego twierdzenia
Hahna–Mazurkiewicza.

**Uwagi audytowe:**
- Po usunięciu powtórzonego
  przykładu liczba etykiet
  spadła z 23 do 22,
  lecz zachowano wszystkie
  etykiety istotnych twierdzeń
  i lematu konstrukcyjnego.
- Audyty 04 i 05 były czyste
  na starszym blobie;
  ich status nie przenosi się
  automatycznie na bieżące źródło.
- Konieczne: potwierdzenie
  sześcio- lub siedmiostronicowego
  wydania bez osieroconej strony,
  nowe audyty 2/2 + 1 na
  bieżącym blobie oraz końcowy CI.

**Status: korekcyjny — 0/2.**
