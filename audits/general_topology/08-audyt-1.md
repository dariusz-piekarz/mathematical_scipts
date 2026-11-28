# Topologia ogólna — rozdział 08 — audyt 1

## Zakres

Utworzony rozdział 08 „Spójność i spójność drogowa”; nie wypchnięto do GitHuba.

Sprawdzono: równoważności definicji spójności (w tym dla przestrzeni pustej), spójność przedziałów, zachowanie przez obrazy ciągłe, sumy, domknięcia i dowolne iloczyny, składowe spójne, całkowitą niespójność i zbiór Cantora, drogi i składowe drogowe, krzywą sinusową topologa oraz lokalną spójność.

## Usterki ujawnione i poprawione w pierwszym audycie

1. Terminologię „przestrzeń niedyskretna, to znaczy...” zastąpiono poprawnym określeniem „przestrzeń z topologią antydyskretną”. Nie każda przestrzeń niedyskretna ma topologię antydyskretną.
2. Rozwinięto uzasadnienie zwartości zbioru Cantora: jawna rodzina skończonych sum przedziałów domkniętych, równość z ich przecięciem i odwołanie do twierdzeń o zwartości.
3. Uproszczono dowód braku spójności drogowej krzywej sinusowej topologa: bez konstruowania zbędnych ciągów indeksów, bezpośrednia sprzeczność z ciągłością drugiej współrzędnej.
4. Poprawiono podział strony przy wzorze określającym przybliżenia Cantora; wzór pozostaje z wprowadzającym zdaniem na tej samej stronie.
5. Naprawiono dwa wzorce wyrażeń regularnych w nowym teście kontroli etykiet; były błędami testu, nie tekstu matematycznego.

## Wynik testów

- Rozdziały 01–08: pełna regresja PASS.
- Chapter08: 5931 testów spójności podprzestrzeni, 35283 testów sum spójnych, 4475 testów domknięć, 1516 testów składowych, 6177 testów obrazów ciągłych, 36 testów skończonych iloczynów, 247 testów przybliżeń Cantora; PASS.
- LaTeX: unikatowe etykiety, rozwiązane odsyłacze, środowiska i terminologia — PASS.
- PDF samodzielnego rozdziału: 8 stron, bez ostrzeżeń LaTeX.
- PDF książki 01–08: 72 strony, bez ostrzeżeń LaTeX.
- Render stron PDF i ręczna kontrola ilustracji — PASS.

## Status

Wersja **0.1 po pierwszym audycie**, licznik kolejnych czystych audytów **0/2**. Nie integrować rozdziału 08 z GitHubem przed uzyskaniem dwóch czystych audytów.

## Propozycje, jeszcze nie dodane

- Quasi-składowe (przecięcia zbiorów otwarto-domkniętych zawierających dany punkt) i ich relacja do składowych spójnych, szczególnie w przestrzeniach zwartych Hausdorffa. Do decyzji użytkownika; nie należy dodawać automatycznie.
- Lemat Aleksandra o podbazie pozostaje wcześniejszą propozycją dotyczącą rozdziału 07 — nie dodawano go w rozdziale 08.
