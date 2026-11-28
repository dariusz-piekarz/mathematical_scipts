# Wycofanie skryptu Teoria całki — inwentaryzacja końcowa

Data: 2026-11-27. Gałąź: biblioteka-matematyczna-iteracja-6.

## Pokrycie etykiet

Porównanie etykiet w aktualnych plikach CAL-01–14 z docelowymi rozdziałami oraz wynikami kontroli CAL-12–14. Liczby oznaczają wystąpienia etykiet w plikach źródłowych, nie liczbę niezależnych twierdzeń.

| CAL | Etykiety zachowane | Rozdziały docelowe |
|---|---:|---|
| 01 | 10/10 | AM1-29, AM1-19 |
| 02 | 16/16 | AM1-29, ME-08 |
| 03 | 18/18 | AM1-40, AM1-36 |
| 04 | 43/43 | AM1-36, AM1-43 |
| 05 | 9/9 | AM1-39 |
| 06 | 41/41 | AM1-42 |
| 07 | 15/15 | AM1-37 |
| 08 | 32/32 | AM1-38, AM1-37 |
| 09 | 28/28 | AM1-41, AM1-43 |
| 10 | 40/40 | ME-02, 04, 16, 17, 18, 25, 26; AM1-29, 42 |
| 11 | 18/18 | ME-07, ME-08 |
| 12 | 23/23 | ME-32 |
| 13 | 44/44 | ME-20, ME-21, ME-32, FA-12 |
| 14 | 37/37 | ME-23 |
| Razem | 374/374 | |

Zachowanie etykiet nie jest automatycznym dowodem równoważności treści. Audyty szczegółowe CAL-12–14 zostały odnotowane w osobnych iteracjach; przed usunięciem należy także potwierdzić kompletność unikatowych fragmentów CAL-01–11, w tym tych bez etykiet, i przeniesienie regresji.

## Rozdziały bez etykiet

- CAL-00: konwencje, podziały, rozróżnienie funkcji konkretnych i klas L1; sprawdzić pokrycie w AM1 oraz ME.
- CAL-15: wyłącznie zapowiedź wielowymiarowej całki Mawhina (5 wierszy), bez definicji, twierdzeń i dowodów. Zgodnie z decyzją użytkownika opracować w przyszłości osobne rozdziały AM2 dotyczące całek Mawhina i Pfeffera, kontroli regularności podziałów i związku z twierdzeniem o dywergencji. Nie przenosić zapowiedzi jako pustego rozdziału i nie traktować jej jako gotowego materiału.
- CAL-16: literatura i historyczny status dowodów. Zachować bibliografię właściwą dla całek cechowanych, sprawdzić jej obecność w AM1, historię audytów zachować w dokumentacji.

## Warunki wycofania

1. Zweryfikować unikatowe treści bez etykiet i testy CAL-01–11; ustalić kanoniczne cele odsyłaczy.
2. Skontrolować katalog, manifesty, rejestry tematów, kwalifikowane odsyłacze CAL, workflow, skrypty i testy aplikacji; nie usuwać historycznych raportów.
3. Potwierdzić pełne CI ME i AM1 wraz z kontrolą PDF. Najnowszy sprawdzony przebieg ME 46035221707 oczekiwał; poprzednie przebiegi były anulowane. Ostatni potwierdzony wynik regresji to 247/247 przed najnowszymi zmianami, z błędem indeksu PDF, którego poprawka oczekuje na potwierdzenie.
4. Dopiero po spełnieniu powyższych warunków usunąć skrypt z katalogu i konfiguracji, następnie źródła i zastąpione testy, z końcowym CI i audytem odsyłaczy.
