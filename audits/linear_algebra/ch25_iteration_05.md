# Algebra liniowa — rozdział 25, audyt V (doprecyzowanie kwantyfikatora)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex`; blob po korekcie `6b57fc1b64ef560b98e17f89322c688160376ccf`.

## Wynik

Po poprawce tytułu twierdzenia w audycie IV powtórnie przejrzano dowody wykrywalności i obserwatora. W dowodzie Stwierdzenia `prop:lin25-observer` występował skrót `Re σ(A-LC)<0`, w którym nierówność miała odnosić się do wszystkich wartości własnych, ale kwantyfikator nie był wypisany. Dla pełnej jednoznaczności zastąpiono go zdaniem: **„jeśli każda wartość własna A-LC ma ujemną część rzeczywistą, to macierz exp(t(A-LC)) zanika wykładniczo”**.

Korekta nie zmienia definicji, twierdzenia ani jego dowodu algebraicznego; usuwa nieprecyzyjną notację w miejscu wykorzystywanym do analizy obserwatora. Sprawdzono, że poprawne są zarówno równania różnicowe `e_(k+1)=(A-LC)e_k` i `e'=(A-LC)e`, jak też wnioskowanie ze stabilności spektralnej do zaniku błędu. W pozostałych twierdzeniach właściwe kwantyfikatory i dziedziny zostały wypisane.

## Decyzja

**Audyt V wykrył i usunął nieprecyzyjne sformułowanie. Nie jest czystym audytem stabilizacyjnym.** Licznik kolejnych czystych audytów resetuje się do zera na blobie `6b57fc1b64ef560b98e17f89322c688160376ccf`. Po nowych przebiegach CI i kontroli PDF należy uzyskać dwie kolejne czyste iteracje.
