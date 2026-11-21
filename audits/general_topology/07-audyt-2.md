# Topologia ogólna — rozdział 07 — audyt 2 (uzgodnione rozszerzenie)

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.2, po dodaniu twierdzenia Weierstrassa o osiąganiu kresów.  
**Status:** audyt z zatwierdzonym rozszerzeniem, **0/2 kolejnych czystych audytów**.  
**SHA256 źródła:** `4cf05d8a0e69d633dd68818c24c975c06204b8e3c6fcf8d8250072127e962f70`.

## Wprowadzony materiał

1. Twierdzenie Weierstrassa: każda ciągła funkcja rzeczywista na **niepustej** zwartej przestrzeni topologicznej jest ograniczona i przyjmuje zarówno minimum, jak i maksimum, również bez założenia Hausdorffa dla dziedziny.
2. Dowód z wcześniejszych wyników rozdziału: zwartość obrazu ciągłego, domkniętość zbiorów zwartych w R, zupełność R i własności supremum i infimum. Każdy z tych kroków jest wyjaśniony.
3. Dwa kontrprzykłady ilustrujące konieczność hipotez: funkcja identycznościowa na (0,1) i funkcja nieciągła na [0,1] o obrazie [0,1).
4. Wiersz w tabeli podsumowującej, aktualizacja celu rozdziału.

## Kontrola

- `bash tools/validate_general_topology_ch07.sh`: PASS (regresja rozdziałów 01–07).
- Testy rozdziału 07: 390 skończonych topologii, 1542 sprawdzenia ultrafiltrów, 384 iloczyny, 29577 przypadków skończonych modeli funkcji rzeczywistych (2379 ciągłych). Testy modeli skończonych nie zastępują dowodu ogólnego.
- Etykiety i odsyłacze: PASS; kontrole terminologii i zgodności środowisk LaTeX: PASS.
- Samodzielny PDF rozdziału 07: 9 stron, bez ostrzeżeń LaTeX.
- Pełny PDF książki rozdziały 01–07: 64 strony, bez ostrzeżeń LaTeX.
- Render wszystkich 9 stron przejrzany; nowy dowód i przykłady mieści się na stronie 3, bez problemów ze składem.

## Wynik i plan

Dodanie nowego twierdzenia było zatwierdzone wprost przez użytkownika. Nie stwierdzono błędu w dodanym materiale po korekcie i walidacji, ale audyt **nie jest czysty**, gdyż zakres rozdziału uległ zmianie. **0/2**. Rozdział 07 nie został wypchnięty na GitHuba.

**Dalej:** audyt 3 wersji 0.2 (ponowna niezależna kontrola całości), bez nowych twierdzeń bez zgody.

**Propozycja odłożona do decyzji:** lemat Aleksandra o podbazie (z audytu 1); nie został dodany.
