# Topologia ogólna — globalny rejestr kontrolny 27: rozdziały 01–06

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. HEAD odczytany przed pomiarem: `0e13f26a9db06e10babcb07fa32052b2d8d11108`. CI tego HEAD: [45121151933](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45121151933), completed/success.

## Zakres rzeczywiście wykonany

Pobrano sześć pełnych źródeł `.tex` z bieżącej gałęzi, policzono środowiska, odsyłacze, etykiety, środowiska rysunkowe i sprawdzono automatycznie wybrane zakazane formy terminologiczne. Jest to **audyt rejestru i powierzchniowa kontrola strukturalna**, NIE niezależny audyt matematyczny wszystkich 87 dowodów, NIE oględziny PDF i NIE nowa lokalna kompilacja. Wartości są liczbami otwarć środowisk w źródłach; nie należy ich interpretować jako liczby dowodów poprawnych matematycznie.

| Rozdział | Blob źródła | proof | twierdzenie | stwierdzenie | wniosek | definicja | przykład | tikzpicture | label | ref/eqref/pageref |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 | `1e8ee853eb9915d96913e5a0a8cdb5e32f2ec5f6` | 9 | 3 | 6 | 0 | 8 | 17 | 2 | 50 | 7 |
| 02 | `53a8dc7e62590a9011bd5858eedb4141c5f38162` | 12 | 7 | 5 | 0 | 5 | 10 | 1 | 35 | 0 |
| 03 | `b571753b5ab9a8777424fc32f6c4a54a4048af77` | 15 | 8 | 7 | 0 | 6 | 10 | 0 | 39 | 1 |
| 04 | `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` | 17 | 7 | 10 | 0 | 7 | 6 | 2 | 40 | 3 |
| 05 | `462acd8f3e1e350478d921429118ec19ac7f4ca8` | 16 | 6 | 7 | 3 | 4 | 7 | 6 | 43 | 15 |
| 06 | `365204000d0d5b21f213132e58b71aa48db3910e` | 18 | 10 | 6 | 1 | 9 | 8 | 2 | 45 | 16 |
| **Suma 01–06** | — | **87** | **41** | **41** | **4** | **39** | **58** | **13** | **252** | **42** |

Dla każdego z sześciu źródeł: brak powtórzonych etykiet *wewnątrz tego samego pliku*; brak dopasowań do wyrażeń `zwartościowani\\w*`, `zbieżnoś(?:ć|ci|cią)\\s+zwart\\w*`, `pierwszo-?przeliczaln\\w*`, `drugoprzeliczaln\\w*`, `sekwencyjn\\w*`. Nie sprawdzono w tej iteracji kolizji etykiet między rozdziałami, rozwiązywania wszystkich 42 odsyłaczy ani czytelności 13 rysunków. Wartości 13 i historyczne 27/24 dotyczą innych zakresów lub metod liczenia i wymagają uzgodnienia na jednym commicie.

## Stan historycznych kontroli i CI

W katalogu `audits/general_topology` odczytano istnienie raportów globalnych 20–26; raport 26 dotyczy uzgodnienia rozdziału 13. Obecny blob rozdziału 03 jest taki sam jak wcześniej udokumentowany `b571753b5ab9a8777424fc32f6c4a54a4048af77`, ale **zgodność bloba nie jest nowym niezależnym sprawdzeniem matematycznym**. Aktualny HEAD ma CI success; w historii znajduje się także failed run 45113110234, a następne zakończone przebiegi success. Nie przeprowadzono nowej inspekcji artefaktów PDF.

## Otwarte punkty

1. Rozszerzyć ten rejestr na 07–12, 13–18 i 19–23, każdorazowo na oznaczonym SHA; połączyć z katalogiem i raportami w rejestr 01–23.
2. Porównać indywidualne 281 (lub inną faktyczną liczbę) dowodów z trzema niezależnymi audytami oraz kontrolami regresyjnymi; nie utożsamiać obecnego licznika z zaliczeniem.
3. Sprawdzić globalne kolizje etykiet, kompletność odsyłaczy i czytelność wszystkich rysunków na wygenerowanych PDF, a także zbudować osobne rozdziały i pełny skrypt.
4. Po zamknięciu wszystkich punktów wykonać dodatkowy niezależny audyt końcowy i CI na finalnym SHA; dopiero wtedy zakończyć automatyzację.

**Następna iteracja:** analogiczny mierzalny rejestr 07–12, bez powtarzania zamkniętych audytów matematycznych.
