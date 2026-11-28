# Globalny audyt algebry liniowej — iteracja 01/09

**Data:** 22 listopada 2026, 01:00 CET  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Wejściowy HEAD:** `2cbcb11cf338ef34ce501443a4fa087715916e5d`  
**Zakres:** rozdziały 01–04.  
**Standardy:** `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`; porównanie z wymaganym poziomem szczegółowości rozdziału 01 geometrii różniczkowej jest standardem redakcyjnym, ale w tej iteracji nie zweryfikowano bezpośrednio źródła DG-01.

## Rzeczywiście przeprowadzone kontrole

Odczytano wszystkie cztery pełne pliki źródłowe: odpowiednio 1716, 1088, 1019 i 1203 wiersze. Rozdziały zawierają 24, 16, 17 i 15 środowisk dowodów, razem 72. Sprawdzono obecność dowodów przy każdym z 72 środowisk twierdzeń, lematów, stwierdzeń i wniosków: wszystkie mają dowody. To kontrola kompletności formalnej, nie automatyczne poświadczenie poprawności każdego kroku. Weryfikowano szczegółowo rachunki i argumenty w reprezentatywnych miejscach: aksjomaty przestrzeni wektorowej i kryterium podprzestrzeni (01), wymiar podprzestrzeni (01), kryterium warstw (02), pierwsze twierdzenie o izomorfizmie (03), wzór na macierz zmiany bazy, łączność i rozdzielność mnożenia macierzy, odwracalność i transpozycję (04). Kontrolowano także przykłady zerowego wymiaru, sum mnogościowych podprzestrzeni i zmiany baz. Nie stwierdzono błędu matematycznego w sprawdzonych fragmentach.

## Wprowadzone korekty
1. **01 — wymiar podprzestrzeni:** usunięto nieuzasadnione „równość wymiarów jest oczywista”; dodano argument z bazą i jednoznacznością jej liczby elementów.
2. **02 — warstwy:** zastąpiono skrót „analogicznie” pełnym uzasadnieniem zawierania odwrotnego, ze wzorem dla dowolnego elementu.
3. **04 — rozdzielność mnożenia macierzy:** dodano współrzędne trzech pominiętych tożsamości i wyjaśnienie wyciągania skalara ze skończonej sumy.
4. **04 — przykład odwrotności macierzy:** jawnie obliczono również \(BA=I_2\), zamiast pomijać drugi iloczyn.

W rozdziale 03 sprawdzona faktoryzacja przez jądro jest uzasadniona, nie wymagała korekty. Żadnych nowych twierdzeń ani rozdziałów nie dodano. Wszystkie istniejące etykiety pozostawiono bez zmian.

## Rysunki i skład
W czterech plikach występuje odpowiednio 2, 1, 1, 1 rysunków TikZ. Sprawdzono obecność podpisów i struktur środowisk w źródłach. **Nie przeprowadzono wizualnej inspekcji stron po kompilacji**; nie można jeszcze orzec o braku kolizji tekstu z rysunkami.

## CI, PDF i status
W tej iteracji nie uzyskano jeszcze zakończonego wyniku GitHub Actions dla niniejszego commitu. Nie wygenerowano ani nie zweryfikowano nowego PDF rozdziału 01–04. Do potwierdzenia: kompilacja książki i PDF, brak błędów odsyłaczy i nakładania tekstu, oraz ponowny audyt po zmianach. Dlatego iteracji nie oznaczono jako w pełni czystej.

| Rozdziały | Status globalny po iteracji 01 |
|---|---|
| 01 | poprawiono uzasadnienie; do weryfikacji PDF/CI |
| 02 | poprawiono dowód warstw; do weryfikacji PDF/CI |
| 03 | kontrola bez korekt; do weryfikacji PDF/CI |
| 04 | uzupełniono trzy wzory i przykład; do weryfikacji PDF/CI |
| 05–32 | oczekują na kolejne iteracje |

## Następny krok
Przed uznaniem 01–04 za stabilne sprawdzić wynik CI po tym commicie, PDF i ponownie miejsca zmienione. Iteracja 02 powinna rozpocząć kontrolę 05–08, a niezakończone testy 01–04 pozostać w raporcie otwartych zadań.
