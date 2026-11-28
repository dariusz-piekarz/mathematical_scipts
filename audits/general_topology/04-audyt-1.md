# Topologia ogólna — rozdział 04 — audyt 1

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.1, tekst po pierwszym audycie.  
**SHA-256 źródła:** `1782069b7efa42a773542ed4b417676c8e54b6abe2ac34255fab2835e890fc2a`.  
**Zakres:** 666 wierszy LaTeX; 8 stron samodzielnego PDF.

## Zakres matematyczny

- Topologia podprzestrzeni; domknięcie, wnętrze i brzeg względny; przechodniość topologii względnej; ciągłość do podprzestrzeni.
- Topologia iloczynu dla dowolnej rodziny przestrzeni; baza, rzutowania, własność uniwersalna, domknięcie prostokąta, różnica z topologią pudełkową/skrzynkową.
- Suma rozłączna; otwarte i domknięte składniki, własność uniwersalna.
- Topologie początkowa i końcowa; definiujące je rodziny odwzorowań i własności uniwersalne; puste rodziny.
- Topologia ilorazowa; odwzorowania ilorazowe; zbiory nasycone, kryteria otwartości i domkniętości obrazów, własność uniwersalna, ciągłe surjekcje otwarte/domknięte i kontrprzykłady.

## Poprawki z audytu

1. **Rysunek:** odcinek ilustrujący $A=[0,2]$ miał puste znaczniki końców. Zastąpiono je punktami pełnymi, zachowując otwarty prawy koniec $[0,1)$ na wyróżnionym odcinku.
2. **Przykład sumy rozłącznej:** usunięto sformułowanie sugerujące, że $\mathbb R\coprod\mathbb R$ nie może być przedstawiona jako podprzestrzeń prostej. Wyjaśniono różnicę między sumą zbiorów a sumą rozłączną.
3. **Kompatybilność CLI:** zastąpiono w teście rozdziału 03 założenie „ostatni plik ma numer 03” jawnie wskazaną ścieżką rozdziału 03. To poprawka wyłącznie w testach przy dołączeniu kolejnego rozdziału.

## Kontrola

- Modelowanie skończonych przestrzeni: **823** przypadki podprzestrzeni i operacji względnych; **361** testów iloczynów; **1481** przypadków dla sum rozłącznych; **83** przypadki topologii początkowych i końcowych z jedną strzałką; **391** przypadków ilorazów i nasycenia; **406** przypadków topologii początkowej z pustą lub dwiema strzałkami; **398** przypadków topologii końcowej z pustą lub dwiema strzałkami — PASS.
- Testy regresyjne rozdziałów 01–03, w tym 24 907 odwzorowań w teście rozdziału 03 — PASS.
- Etykiety: 40 różnych etykiet rozdziału 04, 3 lokalne odsyłacze; wszystkie rozwiązane — PASS.
- `bash tools/validate_general_topology_ch04.sh` — PASS.
- `latexmk -pdf` osobnego rozdziału i książki 01–04 — PASS, zero ostrzeżeń (8 i 36 stron A4).
- Kontrola wizualna kompozycji PDF i dwóch rysunków po poprawce — PASS.

**Decyzja:** pierwszy audyt zawierał poprawki, dlatego licznik kolejnych czystych audytów wynosi **0/2**. Bez wypychania wersji roboczej na GitHub. Następna iteracja to audyt 2 tej samej wersji 0.1.
