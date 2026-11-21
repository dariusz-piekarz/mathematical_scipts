# Algebra liniowa — rozdział 32, audyt IV: druga korekta łamania akapitu

**Data:** 22 listopada 2026  
**Przed poprawką:** blob `afab161412aaf5e5d794f64942a65690878af546`; [workflow #44960416348](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44960416348) — **FAILURE**.

## Znaleziony problem
Ostrzeżenie finalnego logu: `Underfull \\hbox (badness 1389)` w wierszach 96–105 dowodu kwadryki Segrego. Poprzednia korekta rozdzieliła akapit lokalnej odwrotności, ale błąd składu dotyczył wcześniejszego akapitu.

## Zmiana
- Rozdzielono argument o dobrym określeniu odwzorowania rzutowego od argumentu o bijektywności na \(Q\).
- Wyraźniej uzasadniono, że obraz rzędu jeden wyznacza \([u]\), a jednowymiarowa przestrzeń wierszy wyznacza \([\alpha]\).
- Nie zmieniono założeń, twierdzeń, etykiet ani rachunków.

## Status
Audyt IV **nie jest czysty**, ponieważ zmieniono skład i redakcję dowodu. Wymagane ponowne CI oraz dwie kolejne czyste iteracje na identycznym źródle.
