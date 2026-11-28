# L1.5.7 / RT-09d — lista kontroli niezależnego odbioru

28.11.2026. **Oczekuje na niezależny odbiór.** Dokument jest pakietem
dla recenzenta, nie recenzją ani zgodą na wykonanie kodu.

## Dowody

- Standardowy 2+1: d3e20ef2eac1f92c112e97fccb22da549ad0c966,
  [#46179766615](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46179766615):
  3/3 PASS, 1139 testów w każdym przebiegu, 11 sklasyfikowanych pominięć,
  zero unreviewed, Chromium, Linux/Windows i Lean/Mathlib.
  Końcowa bramka problems=[], status=stabilizing, skeptical_review=pending.
- Rootless: 56191f7cc08decf7e8497909737038272048a1e0,
  [#46177909934](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46177909934):
  próby 1 i 2 PASS, trzecia w toku. Raporty 1 i 2 identyczne pod względem
  manifestu, wejść, AST, kodu, diagnostyki i aksjomatów.
- 242 bloby backendu, skryptów, testów, Lean i workflow rootless identyczne
  na obu SHA. To ograniczone porównanie zakresu, nie wspólny SHA.

## Kontrole do wykonania przez niezależnego recenzenta

| ID | Kryterium |
|---|---|
| R1 | Powiązanie SHA, prób, jobów, artefaktów i rzeczywistych raportów. |
| R2 | Ocena równoważności drzew, także konfiguracji, zależności wykonania i wywoływanych workflow; brak istotnych różnic. |
| R3 | Rootless, brak sieci, limity RAM/procesów/czasu/wyjścia, metadane, zakończenie i potwierdzone sprzątanie; fail-closed. |
| R4 | Zachowanie źródła, AST, tezy i importów; trzy różne wejścia, maksymalnie trzy próby. |
| R5 | Rzeczywiste przypadki dodatni/ujemny i naprawa 1,1,0; pięć osobnych kontenerów, zgodność digestów wejścia i removed_verified. |
| R6 | Surowa diagnostyka, historia planera, manifest, aksjomaty, negatywne testy manipulacji; replay nie jest niezależną atestacją runtime. |
| R7 | Brak publicznego wykonywania dowolnych draftów, host fallback, certyfikatu semantycznego i automatycznego zapisu kanonicznego TeX/Lean. |
| R8 | Lokalny model pozostaje odrębnym etapem; brak automatycznej instalacji, pobrania wag i transferu danych. |

Recenzent wskazuje swoją tożsamość i niezależność, SHA i zakres, dowody
kontroli R1–R8, zastrzeżenia krytyczne i decyzję approve/reject. Nie
wpisywać aprobaty w imieniu recenzenta. Sam JSON w repozytorium nie jest
uwierzytelnionym podpisem. Bramka nie promuje automatycznie stable.

Po trzeciej rzeczywistej próbie rootless i niezależnym odbiorze można
rozliczyć techniczny zakres L1.5.7. Nadal execution_allowed=false,
offline_ready=false, certificate=false dla dowolnego niezaufanego wykonania.
