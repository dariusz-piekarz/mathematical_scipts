# Topologia ogólna — rozdział 05 — audyt 1

**Data:** 21 listopada 2026 r.  
**Rozdział:** Aksjomaty oddzielania.  
**Wersja:** 0.1 po pierwszym audycie.  
**SHA256 źródła:** `f41f5bda8d5af272b3d13c3b94cd2007eabbe77a92452d1dc7e5af5ce107a04b`.  
**Objętość:** 632 wiersze/wierszy LaTeX; 7 stron samodzielnego PDF; 43 strony książki 01–05.

## Zakres weryfikacji

- Definicje T0, T1, T2, regularności, całkowitej regularności, normalności oraz T3, T3½, T4; kwantyfikatory i puste przypadki.
- Dowody: T1 przez singletony, Hausdorff przez domkniętą przekątną, jednoznaczność odwzorowania z gęstego podzbioru, kryteria zwężania otoczeń, implikacje.
- Pełna konstrukcja funkcji Urysohna z użyciem dyadycznych parametrów i otwartość przeciwobrazów.
- Rozdzielanie metrycznych zbiorów domkniętych przez funkcje odległości, dziedziczenie aksjomatów, przykład ilorazu Hausdorffa, który nie jest T1.
- Kontrprzykłady: przestrzeń Sierpińskiego, topologia koskończona, K-topologia, płaszczyzna Sorgenfreya; dokładne wykorzystanie gęstości i dyskretności antyprzekątnej.

## Wykryte i poprawione problemy

1. Trzy odsyłacze międzyrozdziałowe w nowym pliku wywoływały ostrzeżenia przy niezależnej kompilacji rozdziału. Zastąpiono je jednoznacznymi wskazaniami wcześniejszej konstrukcji z rozdziału 04.
2. W pierwszej wersji rysunku regularności etykiety U, W i X nie były precyzyjnie umieszczone we właściwych obszarach. Poprawiono pozycje.
3. Zwiększono odstępy w diagramie hierarchii, aby strzałki nie nachodziły na węzły.
4. Ujednolicono etykiety LaTeX do bezpiecznego kodowania ASCII.

## Testy i kompilacja

- `bash tools/validate_general_topology_ch05.sh`: PASS.
- Regresja rozdziałów 01–04: PASS.
- Wszystkie 390 topologii na przestrzeniach od 0 do 4 punktów: PASS.
- 5931 testów dziedziczenia oddzielania na podprzestrzenie: PASS.
- 4133 testy rozdzielania zamkniętych par w normalnych przestrzeniach skończonych: PASS.
- Spójność definicji T0, T1, T2, T3, T3½, T4 oraz równoważności kryteriów: PASS.
- Unikalność 35 etykiet w rozdziale i rozwiązywalność 8 referencji: PASS.
- `latexmk` na samodzielnym rozdziale oraz książce, bez `Overfull`, `Underfull`, `LaTeX Warning` i innych ostrzeżeń: PASS.
- Rysunki i tekst wizualnie skontrolowane na renderach wszystkich 7 stron: PASS.

**Decyzja:** audyt 1 zakończony z poprawkami. Licznik czystych audytów 0/2. Rozdział 05 nie jest jeszcze stabilny i nie jest przeznaczony do pushu GitHub. Następny audyt: 2 na wersji 0.1, bez dodawania nowych twierdzeń.
