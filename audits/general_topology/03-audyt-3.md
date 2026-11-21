# Audyt 3 — Topologia ogólna, rozdział 03 „Odwzorowania ciągłe”

- Data: 2026-11-21.
- Wersja źródłowa: 0.1 (bez zmian po audytach 2 i 3).
- SHA256 rozdziału: `dd568d119fdf9ee051cb6701ec966cc6da1ef1a4dcd569fe88bfd8010fabe554`.
- Wynik: **drugi czysty audyt z rzędu — 2/2**.

## Weryfikacja merytoryczna

Zweryfikowano definicje, tezy i dowody kryteriów globalnych i lokalnych ciągłości, warunek ε–δ, kryteria przez bazę i podbazę, składanie, ograniczanie, sklejanie na otwartych i skończonych domkniętych pokryciach, odwzorowania otwarte i domknięte, homeomorfizmy i zanurzenia topologiczne. Kontrolą objęto przeciwobrazy pustych rodzin, pustą dziedzinę i przeciwdziedzinę, przypadki nie-T1, przykład Sorgenfreya i Sierpińskiego, funkcję skokową i nieskończone pokrycie domknięte. Żadna poprawka w tekście nie była konieczna.

## Testy i skład

- `bash tools/validate_general_topology_ch03.sh`: **PASS**.
- Rozdział 01: testy topologii, baz, podbaz, otoczeń i przestrzeni metrycznych: **PASS**.
- Rozdział 02: 390 topologii skończonych (n=0,1,2,3,4): **PASS**.
- Rozdział 03: 24 907 instancji odwzorowań przestrzeni o najwyżej 3 punktach (11 345 ciągłych, 184 homeomorfizmy): **PASS**.
- Etykiety: 124 unikatowe, wszystkie 7 `\ref` rozwiązane: **PASS**.
- `latexmk` rozdziału 03 i książki 01–03: **PASS**, bez ostrzeżeń składu.
- Rozdział 03: 8 stron A4; książka 01–03: 27 stron A4.
- Kontrola wizualna wszystkich ośmiu stron rozdziału: **PASS**.

## Decyzja

Rozdział 03 uznany za stabilny na poziomie matematycznym i edytorskim, gotowy do integracji na gałęzi `biblioteka-matematyczna-iteracja-6` i kontroli GitHub CI. Brak nowych twierdzeń lub rozszerzenia materiału w audycie.
