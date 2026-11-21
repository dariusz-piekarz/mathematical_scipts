# Topologia ogólna — rozdział 09: audyt 3

**Data:** 2026-11-21  
**Wersja:** 0.3  
**Wynik:** zakończony z poprawkami; kolejne czyste audyty **0/2**.  
**Zakres:** poprawność matematyczna, spójność terminologii, dowody kryteriów przeliczalności, ośrodkowość, Lindelöf, przestrzenie metryczne, prosta i płaszczyzna Sorgenfreya, przypadki brzegowe, rysunki, odsyłacze i kompilacja.

## Kontrola matematyczna

1. Sprawdzono implikacje drugiego aksjomatu przeliczalności, dziedziczenie przez podprzestrzenie, przeliczalne iloczyny, ośrodkowość i własność Lindelöfa bez dodatkowych aksjomatów oddzielania.
2. Ponownie zweryfikowano dowód równoważności ośrodkowości, drugiego aksjomatu przeliczalności i własności Lindelöfa w przestrzeniach metrycznych, w tym przypadek pustej przestrzeni.
3. Skontrolowano konstrukcję własności Lindelöfa prostej Sorgenfreya: \(G=\bigcup(a,b)\), \(F=\mathbb R\setminus G\), wymierny \(q_x\) i iniekcję \(x\mapsto q_x\). Rozumowanie jest poprawne w ZFC; użycie wyboru zostało jawnie omówione w rozdziale.
4. Sprawdzono dyskretny, domknięty, nieprzeliczalny zbiór antydiagonalny płaszczyzny Sorgenfreya i jego użycie do kontrprzykładów dotyczących własności Lindelöfa oraz ośrodkowości.
5. Zweryfikowano przykłady nieprzeliczalnej przestrzeni dyskretnej, koskończonej i jednopunktowego uzwarcenia nieprzeliczalnej przestrzeni dyskretnej. Nie znaleziono nowego błędu matematycznego.

## Wprowadzone poprawki redakcyjno-typograficzne

1. **Samodzielny przykład na jednej stronie:** otoczono przykład `Pierwszy aksjomat przeliczalności nie zapewnia ośrodkowości` środowiskiem `samepage`. Wcześniej po jego podziale między strony 6–7 na początku strony 7 pozostawały dwie linijki bez początku przykładu. Teraz cały przykład rozpoczyna stronę 7.
2. **Diagram implikacji:** usunięto powtórzony, niezręczny opis „górny, środkowy dolny i prawy dolny są równoważne”. Pełna, matematycznie precyzyjna informacja o równoważności w przestrzeniach metrycznych pozostaje w podpisie rysunku i w twierdzeniu. Nie zmieniono grafu ani wniosków.
3. **Regresja:** dodano testy obecności środowiska chroniącego przykład i nieobecności usuniętego sformułowania. Wszystkie historyczne etykiety LaTeX pozostały niezmienione.

## Wyniki kontroli

- `bash tools/validate_general_topology_ch09.sh`: **PASS** (testy rozdziałów 01–09).
- Rozdział 09: **390** topologii skończonych; **2483** rekonstrukcje; **5931** testów gęstości; **5931** testów dziedziczenia; **864** testy lokalnych baz w iloczynach; **96** skończonych modeli konstrukcji prostej Sorgenfreya.
- Kontrola referencji: **364** etykiety, **93** odsyłacze, wszystkie rozwiązywalne w pełnej książce.
- `latexmk`: **PASS**, bez `Overfull`, `Underfull`, `LaTeX Warning` i nierozwiązanych odsyłaczy.
- Samodzielny PDF: **7 stron**; pełna książka 01–09: **80 stron**.
- Renderowanie i oględziny wszystkich siedmiu stron PDF: **PASS**; przykład pozostaje w całości na stronie 7, diagram i podpis nie kolidują.
- Rozdział 09 pozostaje **lokalny**; na GitHub trafi dopiero po dwóch kolejnych czystych audytach.

## Decyzja

Audyt wymagał korekty składu i podpisu rysunku, dlatego nie może być zaliczony jako czysty: **0/2**. Kolejny krok: audyt 4 wersji 0.3, bez rozszerzania zakresu. Nowych propozycji rozszerzeń nie zgłoszono.
