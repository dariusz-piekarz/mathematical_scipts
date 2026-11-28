# Algebra liniowa — rozdział 24, audyt IV (korekta składu)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/24-rownania-riccatiego-i-sterowanie-liniowo-kwadratowe.tex`  
**Ostatni blob po korekcie:** `82b136e5bd2284442a47d1e740207b2ee3bda816`.

## Ustalenie problemu

Przebieg [CI 44947367459](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947367459) zakończył się **FAILURE** tylko na kroku **Verify compilation artifact and unresolved references**. Log końcowej kompilacji wykazał dokładnie:

```
Underfull \hbox (badness 1163) in paragraph at lines 523--531
```

Zidentyfikowano akapit zaczynający się tytułem Wniosku `cor:lin24-discrete-opt`. Szeroki tytuł „Optymalność sterowania nieskończonego” w połączeniu z blisko umieszczonym odsyłaczem do twierdzenia spowodował nieoptymalne łamanie pierwszego wiersza.

## Poprawka

Zastąpiono opisowy tytuł zwięzłym: **„Sterowanie optymalne”**. Treść twierdzenia, założenia, wszystkie wzory, dowód i jego etykieta pozostały bez zmian. Bez zmian są wszystkie wyniki matematyczne i zakres rozdziału.

Przed krokiem walidacji składu w tym samym przebiegu zostały zaliczone wszystkie istniejące regresje rozdziałów 01–23 oraz nowy `tools/test_linear_algebra_riccati.py`. W przeprowadzonym audycie nie znaleziono nowej luki merytorycznej.

## Decyzja

**Audyt IV wymagał korekty typograficznej.** To resetuje licznik czystych audytów: do stabilizacji wymagane są dwie kolejne czyste kontrole na blobie `82b136e5bd2284442a47d1e740207b2ee3bda816` oraz ukończony pomyślnie CI z wyeksportowanym samodzielnym PDF.
