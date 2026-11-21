# Algebra liniowa — rozdział 25, audyt IV (korekta składu PDF)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex`.  
**Blob po korekcie:** `3313715950a0a01aa74ad07353a8acbb4494f570`.

## Wynik CI po naprawieniu testu

Przebieg [44949122637](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44949122637) zaliczył wszystkie regresje, w tym nowy test `tools/test_linear_algebra_control.py`, i poprawnie skompilował książkę. Końcowa kontrola logu odrzuciła jednak:

```text
Underfull \hbox (badness 2189) in paragraph at lines 1362--1367
```

Z logu: akapit twierdzenia `thm:lin25-stabilizability`, w którym nagłówek „Spektralne kryteria stabilizowalności” i pierwsze wyrażenia matematyczne tworzyły zbyt szeroki ciąg o nieoptymalnym łamaniu wierszy.

## Poprawka

Tytuł skrócono do **„Kryterium stabilizowalności”**. Numer, etykieta, treść twierdzenia, wszystkie założenia i dowód pozostały bez zmian. Przebieg testów przed tym krokiem był pozytywny; problem dotyczył tylko łamania tekstu.

## Decyzja

**Audyt IV wykrył i usunął błąd składu.** Poprzedni audyt III był czysty matematycznie, lecz nie może być uznany za pełny audyt stabilizacyjny po wykryciu ostrzeżenia LaTeX. Od tego momentu wymagane są **dwa kolejne pełne czyste audyty** na niezmienionym blobie po korekcie oraz pomyślny CI i sprawdzony samodzielny PDF rozdziału 25.
