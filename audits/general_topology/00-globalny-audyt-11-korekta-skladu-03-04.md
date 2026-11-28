# Topologia ogólna — globalny audyt 11, korekta składu rozdziałów 03–04

**Data:** 2026-11-22.
**Rodzaj:** korekta wydawnicza po rzeczywistym
przeglądzie ostatnich stron PDF.
**Stan początkowy:** audyt korekcyjny, wymagane
2 czyste audyty + 1 potwierdzający po nowym CI i renderingu.

## Problem ustalony w artefakcie źródłowym

W udanym CI
[45064706272](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064706272)
pełna książka liczyła 190 stron, a
samodzielne wydania 03 i 04 po 8 stron.
W rozdziale 03 ostatnia strona
zawierała jedynie podsumowanie,
zaś w rozdziale 04 — krótką,
odizolowaną uwagę o kierunku
sprawdzania ciągłości.

Oba przypadki nie generowały
ostrzeżenia Overfull/Underfull,
dlatego same logi kompilacji
były niewystarczające do kontroli składu.

## Korekta rozdziału 03

**Blob przed:** `0c0395aebcf21a1ec253c21499049642dd710798`.
**Blob po:** `a5606bc0c213dbd1fb5224e7440f66a7cf66dbb0`.

W przykładzie o zanurzeniu
skrócono ponownie opisany
kontrprzykład ciągłej identyczności
\((S,\mathcal P(S))\to(S,\{\varnothing,S\})\),
dodając odsyłacz do wcześniejszego
pełnego przykładu
`ex:topog-bijekcja-niehomeomorfizm`.
Podsumowanie zredagowano zwięźlej,
z zachowaniem wszystkich wątków:
kryteria ciągłości,
baza i podbaza, warunek
ε–δ, sklejanie, homeomorfizm,
zanurzenie oraz powiązania
ze zwartością, spójnością
i zbieżnością.

Porównanie starych i nowych
źródeł z rzeczywistego drzewa Git:
**wszystkie etykiety zachowane,
15 środowisk dowodowych bez zmian,
liczba pozostałych środowisk
twierdzeń, definicji,
przykładów i rysunków bez zmian.**
Nowy odsyłacz wskazuje istniejącą
etykietę w tym samym rozdziale.

## Korekta rozdziału 04

**Blob przed:** `ba468b3413b37bf6cd7776761eb67195951ccd20`.
**Blob po:** `adbd56a91e5b5f3857ce16ec5c3b1241dd0d102e`.

Powtarzającą podsumowanie uwagę
o kierunku sprawdzania ciągłości
scalono z ostatnim akapitem
rozdziału. Pozostawiono
istotne rozróżnienie:
dla topologii początkowej
badamy złożenia z odwzorowaniami
wychodzącymi z danej przestrzeni,
dla topologii końcowej —
z odwzorowaniami do niej wchodzącymi.
Nigdzie nie zmieniono definicji
topologii początkowej ani końcowej.

Porównanie starego i nowego źródła:
**wszystkie etykiety zachowane,
17 środowisk dowodowych bez zmian,
liczba pozostałych środowisk
twierdzeń, definicji,
przykładów i rysunków bez zmian.**

## Zasada dalszej walidacji

Nowe źródła 03 i 04
muszą zostać osobno
skompilowane i wyrenderowane,
aby potwierdzić usunięcie
prawie pustych stron.
Nawet niezmieniona liczba
dowodów nie zastępuje ich
niezależnej kontroli.
Wynik należy uzupełnić
dwoma czystymi audytami i
jednym potwierdzającym
na dokładnie tych samych
blobach nowych źródeł.

**Na tym etapie nie ogłaszamy
nowej wersji jako stabilnej
wyłącznie na podstawie
zielonych testów źródłowych.**
