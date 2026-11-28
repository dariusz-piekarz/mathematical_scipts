# Topologia ogólna — rozdział 09: audyt 5

**Data:** 2026-11-21  
**Wersja:** 0.3; bez zmian w źródle  
**Wynik:** drugi kolejny czysty audyt, **2/2**, rozdział stabilny.

## Kontrola matematyczna

1. Sprawdzono sformułowania pierwszego i drugiego aksjomatu przeliczalności; drugi implikuje pierwszy, w tym dla nieotwartych otoczeń i pustej przestrzeni.
2. Sprawdzono dziedziczenie obu aksjomatów przez podprzestrzenie i zachowanie drugiego aksjomatu przez iloczyny przeliczalne, w tym przypadki pustych czynników i pustej rodziny indeksów. Skontrolowano nieprzeliczalny iloczyn rzeczywistych prostych jako kontrprzykład.
3. Skontrolowano dowody konsekwencji drugiego aksjomatu dla ośrodkowości i własności Lindelöfa oraz ich zachowanie przez ciągłe surjekcje, otwarte/domknięte podprzestrzenie i przeliczalne sumy podprzestrzeni. Odniesienia do aksjomatu wyboru są poprawne.
4. W przestrzeniach metrycznych sprawdzono kierunki ośrodkowość => drugi aksjomat i Lindelöf => ośrodkowość, dobór liczb wymiernych, nierówności i przypadek pusty.
5. Skontrolowano dowód własności Lindelöfa prostej Sorgenfreya: budowę otwartej części G, przeliczalne podpokrycie G, rodzinę F, wybór q_x i iniekcję F do Q. Sprawdzono także rozdzielanie punktów i brak globalnej bazy przeliczalnej.
6. Zweryfikowano nieprzeliczalną zamkniętą dyskretną antydiagonalę w płaszczyźnie Sorgenfreya, przykłady ośrodkowości i własności Lindelöfa, iloczyny, zwartą przestrzeń z otwartą nie-Lindelöf podprzestrzenią oraz nieprzeliczalną topologię koskończoną.
7. Końcowa lista implikacji i kontrprzykładów jest logicznie kompletna. Zachowano globalną terminologię: „spełnia pierwszy/drugi aksjomat przeliczalności”; nie rozszerzano materiału.

Nie wykryto błędów merytorycznych, nieuzasadnionych kroków wymagających uzupełnienia ani usterek redakcyjnych.

## Regresja i wygląd

- `bash tools/validate_general_topology_ch09.sh`: PASS rozdziałów 01–09.
- Rozdział 09: 390 topologii, 2483 rekonstrukcje zbiorów otwartych, 5931 prób gęstości, 5931 prób dziedziczenia, 864 kontroli iloczynów, 96 przypadków modelowych prostej Sorgenfreya.
- Wszystkie etykiety i odsyłacze rozwiązane: 364 unikatowe etykiety, 93 odsyłacze.
- Samodzielny PDF: 7 stron; kompletna książka: 80 stron. Brak ostrzeżeń i błędów LaTeX.
- Render wszystkich 7 stron i kontrola rysunków, odsyłaczy oraz przykładu 9.5.3 na stronie 7: PASS.
- Źródło `.tex` niezmienione względem audytu 4; suma SHA256: `0f8f44631c4632c9cffef10b69fac0d5a1bb35a997db3b14227763bfadce1609`.

## Decyzja

Audyt 5 czysty: **2/2**. Rozdział stabilny i gotowy do scalenia na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6` oraz sprawdzenia CI. Wszelkie rozszerzenia opcjonalne pozostają poza tą iteracją.
