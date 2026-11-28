# Topologia ogólna — rozdział 26, audyt 09 (dodatkowy, czysty)

**Data:** 2026-11-22.
**Niezmieniony blob z audytów 07 i 08:**
`161d04d779ae86554f81c11bb24daa842c8dd363`.
**Wynik:** CZYSTY 3/2 (2 czyste audyty + 1 potwierdzający).

## Ponowna kontrola dowodów

1. Spójne otwarte otoczenia
   o małych średnicach istnieją
   z lokalnej spójności; jeden parametr
   δ dla całego zwartego X wynika
   ze skończonego podpokrycia.
2. Skończone δ-łańcuchy
   istnieją w spójnych zbiorach
   bez uprzedniego założenia
   spójności drogowej.
3. Konstrukcja drogi
   przez coraz drobniejsze łańcuchy
   daje funkcję jednostajnie
   ciągłą na zbiorze gęstym;
   zwartość zapewnia zupełność,
   a więc jej ciągłe przedłużenie.
4. Małe drogi dają
   lokalną spójność drogową
   poprzez otwartość składowych
   drogowych zbiorów otwartych.
5. Skończenie wiele pętli
   dołączanych do drogi
   nie zmienia jej końców.
   Błąd sup norm jest
   kontrolowany przez 2ε_n.
6. Surjekcja powstaje jako
   granica jednostajna
   poprawek o sumowalnych błędach.
   δ_n/2-sieci wymuszają
   gęstość obrazu granicy,
   a zwartość [0,1]
   domkniętość tego obrazu.
7. W kierunku koniecznym
   wykorzystano zwartość
   włókien f^{-1}(x),
   domkniętość kompaktowych
   obrazów w Hausdorffowym X,
   skończone sumy przeliczalnej
   bazy odcinka i
   wcześniejsze twierdzenie
   Urysohna o metryzowalności.
8. Wykazanie lokalnej spójności
   nie wymaga na wstępie
   metryzowalności X.
   Obrazy domkniętych przedziałów
   tworzą spójny zbiór K,
   a otwarte W⊂K
   daje otwartość składowej
   spójnej każdego O.
9. Kontrprzykłady rozróżniają
   niezależność spójności,
   lokalnej spójności
   i Hausdorffowości.
   Zbiór Cantora nie jest
   fałszywie uznawany
   za lokalnie spójny.

## Weryfikacja LaTeX i wydania

Źródło nie zmieniło się względem
audytów 07 i 08.
Ma 22 unikatowe etykiety,
19 odsyłaczy i 9 poprawnie
otwartych/zamkniętych dowodów.
Obecne etykiety wcześniejszych
wyników odnoszą się do
rozdziałów 08, 10 i 25.

[GitHub Actions 45062871304](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45062871304)
zakończyło się **completed/success**,
ze wszystkimi 63 krokami
i kompletnym artefaktem
`general-topology-ch01-ch26`,
ID 14769903315.
Pobrano archiwum i potwierdzono:
- samodzielny PDF rozdziału 26: **6 stron A4**,
- pełna książka przed aktualizacją tytułu: **190 stron**,
- logi samodzielnego i pełnego dokumentu:
  bez Overfull/Underfull, Missing character,
  LaTeX Warning, Undefined control sequence
  oraz Fatal error.

Wszystkie 6 stron wyrenderowano
i obejrzano w zestawieniu;
osobno skontrolowano stronę 6
z twierdzeniem końcowym, przykładami,
kontrprzykładami i podsumowaniem.
Nie ma osieroconej strony
ani nałożonych na siebie napisów.
Rysunek pętli na stronie 4
nie ma kolizji podpisów.

**Rozdział 26 jest stabilny matematycznie i wydawniczo.**
Po aktualizacji tytułu wersji książki,
README, planu i regresji należy
wykonać dodatkowy końcowy przebieg CI
integracyjnego tej aktualizacji.
