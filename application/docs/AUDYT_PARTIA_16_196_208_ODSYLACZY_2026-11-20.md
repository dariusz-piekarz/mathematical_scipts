# Audyt pochodzenia odsyłaczy — partia XVI (196–208)

Data: 20 listopada 2026 r.  
Repozytorium: `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`.  
Migawka indeksu: `reference_provenance_audit_355.json`, 355 rozdziałów, 257 nierozstrzygniętych wystąpień.

## Wynik

Zweryfikowano **13 odsyłaczy z `TOP-05`** (homologia przestrzeni). Wszystkie mają po **dwóch właścicieli** w indeksie: jeden w skrypcie topologii algebraicznej, drugi w skrypcie geometrii różniczkowej. Kontekst cytowań i źródłowe deklaracje potwierdzają lokalnych właścicieli **`TOP-03` (algebra homologiczna)** i **`TOP-04` (homotopia, sympleksy, CW)**. Nie ma podstaw do arbitralnego wskazania `DG-06` ani `DG-07` przy cytowaniach z `TOP-05`.

## Rejestr wszystkich wystąpień

| Nr | Cytowanie | Oryginalna etykieta | Właściwy cel lokalny | Alternatywny właściciel |
|---:|---|---|---|---|
| 196 | `TOP-05:7` | `ch:topologia-algebraiczna-podstawy` | `TOP-04:2` | `DG-07` |
| 197 | `TOP-05:24` | `thm:homologia-char-zero` | `TOP-03:1512` | `DG-06` |
| 198 | `TOP-05:33` | `def:kompleks-symplicjalny` | `TOP-04:995` | `DG-07` |
| 199 | `TOP-05:160` | `def:delta-kompleks` | `TOP-04:1049` | `DG-07` |
| 200 | `TOP-05:410` | `thm:homotopia-homologia` | `TOP-03:839` | `DG-06` |
| 201 | `TOP-05:478` | `prop:ses-iloraz` | `TOP-03:1063` | `DG-06` |
| 202 | `TOP-05:668` | `lem:pieciu` | `TOP-03:1705` | `DG-06` |
| 203 | `TOP-05:736` | `thm:les-homologia` | `TOP-03:393` | `DG-06` |
| 204 | `TOP-05:905` | `lem:pieciu` | `TOP-03:1705` | `DG-06` |
| 205 | `TOP-05:962` | `thm:pi1-dolaczenie-komorki` | `TOP-04:1435` | `DG-07` |
| 206 | `TOP-05:982` | `prop:brzeg-sympleksu` | `TOP-04:962` | `DG-07` |
| 207 | `TOP-05:1093` | `lem:pieciu` | `TOP-03:1705` | `DG-06` |
| 208 | `TOP-05:1114` | `sec:cw-kompleksy` | `TOP-04:1148` | `DG-07` |

## Weryfikacja znaczeniowa

- `TOP-05:7`: wprowadzenie do homologii korzysta z rozdziału `TOP-04` o sympleksach, a nie z równoległego `DG-07`.
- `TOP-05:24,410,478,668,736,905,1093`: twierdzenie o zmianie współczynników, niezmienniczość homologii przy homotopii łańcuchowej, długi ciąg ilorazu, lemat pięciu i długi ciąg dokładny zostały wprost zdefiniowane/udowodnione w `TOP-03`. Trzy cytowania lematu pięciu dotyczą różnych argumentów i nie mogą zostać sklejone w jedno wystąpienie audytu.
- `TOP-05:33,160,962,982,1114`: definicje kompleksu symplicjalnego i `\Delta`-kompleksu, twierdzenie o wpływie dołączania komórki na `\pi_1`, stwierdzenie o brzegu sympleksu oraz sekcja o CW znajdują się w `TOP-04`. Ich hipotezy i znaczenie odpowiadają użyciu w `TOP-05`.
- Zwraca uwagę sposób uzasadnienia ciągłości retrakcji przy `TOP-05:962`: sprawdzić osobno szczegóły topologiczne w dalszym pogłębionym audycie matematycznym. Występowanie prawidłowej etykiety nie jest dowodem pełnej poprawności argumentu.

## Zakres pozostałych źródeł

Skrypt geometrii różniczkowej ma **36 rozdziałów**, lecz tylko 20 jest obecnie zaimportowanych do repozytorium. Kolizje z części już zaimportowanej nie upoważniają do przemianowania źródłowych `\label` ani do przedwczesnego łączenia obu skryptów. Braki celów odsyłaczy do późniejszych rozdziałów należy rozpatrywać jako potencjalnie wynikające z niepełnego importu.

## Działania i postęp

**Audyt: 208/257 wystąpień; 49 pozostałych.** Indeks nie został naprawiony: to audyt pochodzenia, nie zmiana klas `ambiguous`. Zaleca się w aplikacji priorytet właściciela z tego samego skryptu, zachowując pełną listę oryginalnych właścicieli i oznaczeń. Nie zmieniano `chapters/pl/`, `main`, żadnego `\label`, `\ref`, `\eqref` i nie scalano skryptów.

Następna partia: **209–221**.