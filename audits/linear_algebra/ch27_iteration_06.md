# Algebra liniowa — rozdział 27, audyt VI (korekta składu)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`  
**Blob po korekcie:** `a91dfa108d4a6ef4221b9ba24a98c87772c75d4a`.

## Rozpoznanie błędu

Pełny przebieg [GitHub Actions 44951891623](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44951891623) zaliczył wszystkie testy, w tym nowe regresje LA-27. Po poprawce niedostępnego polecenia `\mathscr` kompilacja TeX także przebiegła, lecz walidacja końcowego logu wykryła:

```text
Underfull \hbox (badness 4328) in paragraph at lines 895--903
```

Problem dotyczył rozpoczynającego się na tej linii nagłówka twierdzenia `thm:lin27-minimal-uniqueness`, którego dotychczasowy długi tytuł „Jednoznaczność minimalnej realizacji” źle łamał się wraz z tekstem matematycznym.

## Poprawka

Skrócono tytuł do **„Podobieństwo realizacji”**, zachowując dokładnie treść twierdzenia, pełny dowód, założenia, równości i stabilną etykietę. Nie jest to zmiana twierdzenia matematycznego; jego teza nadal obejmuje podobieństwo minimalnych realizacji oraz wynikającą stąd jednoznaczność z dokładnością do zmiany współrzędnych.

## Decyzja

**Audyt VI wymagał korekty składu i nie jest czysty.** Po tej korekcie należy uzyskać dwa kolejne pełne czyste audyty oraz potwierdzić zielony CI i ściśle samodzielny PDF rozdziału 27.
