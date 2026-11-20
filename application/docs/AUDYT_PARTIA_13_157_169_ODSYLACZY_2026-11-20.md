# Audyt integralności odsyłaczy — partia XIII (157–169)

Data: 20 listopada 2026 r.  
Repozytorium: `dariusz-piekarz/mathematical_scipts`  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Indeks: `reference_provenance_audit_355.json`, 355 rozdziałów, kolejność w `unresolved_references` liczona od 1.

## Wynik matematyczny i techniczny

**13/13 cytowań** z jednego rozdziału źródłowego `P4-00` (wprowadzenie do tomu IV) ma w indeksie status `missing`. **12 różnych etykiet docelowych** jest jednak rzeczywiście zadeklarowanych w istniejących rozdziałach tomów I–III. `I-ch:clt` pojawia się dwukrotnie, na liniach 11 i 16. Otworzono oryginalny tekst źródłowy, wszystkie 12 plików docelowych oraz `books/pl/probability_volume_iv.tex`.

We wszystkich przypadkach status `missing` jest **fałszywym brakiem semantycznym wynikającym z importu międzytomowego**. Deklaracja lokalna `\label{ch:clt}` w tomie I jest dostępna w tomie IV pod nazwą `I-ch:clt`, jeśli LaTeX załaduje plik pomocniczy przez `\externaldocument[I-]{probability_volume_i}`. Ta zasada dotyczy analogicznie tomów II i III.

## 13 przeanalizowanych wystąpień

| Nr | Źródło i linia | Oryginalne cytowanie | Znaleziony cel | Temat |
|---:|---|---|---|---|
| 157 | `P4-00:11` | `\ref{I-ch:clt}` | P1-09 — `\label{ch:clt}` | Centralne twierdzenie graniczne |
| 158 | `P4-00:16` | `\ref{I-ch:conditioning}` | P1-03 — `\label{ch:conditioning}` | Warunkowanie i niezależność |
| 159 | `P4-00:16` | `\ref{I-ch:condexp}` | P1-10 — `\label{ch:condexp}` | Warunkowa wartość oczekiwana |
| 160 | `P4-00:16` | `\ref{I-ch:lln}` | P1-08 — `\label{ch:lln}` | Prawa wielkich liczb |
| 161 | `P4-00:16` | `\ref{I-ch:clt}` | P1-09 — `\label{ch:clt}` | Centralne twierdzenie graniczne |
| 162 | `P4-00:16` | `\ref{I-ch:markov}` | P1-12 — `\label{ch:markov}` | Łańcuchy Markowa w czasie dyskretnym |
| 163 | `P4-00:17` | `\ref{II-ch:procesy}` | P2-01 — `\label{ch:procesy}` | Procesy stochastyczne |
| 164 | `P4-00:17` | `\ref{II-ch:poisson-process}` | P2-04 — `\label{ch:poisson-process}` | Proces Poissona |
| 165 | `P4-00:17` | `\ref{II-ch:wiener}` | P2-07 — `\label{ch:wiener}` | Proces Wienera |
| 166 | `P4-00:17` | `\ref{II-ch:quadratic-cont}` | P2-13 — `\label{ch:quadratic-cont}` | Wariacja kwadratowa i kowariacja |
| 167 | `P4-00:18` | `\ref{III-ch:sde-existence}` | P3-05 — `\label{ch:sde-existence}` | Stochastyczne równania różniczkowe |
| 168 | `P4-00:18` | `\ref{III-ch:sde-properties}` | P3-06 — `\label{ch:sde-properties}` | Własności i aproksymacje SDE |
| 169 | `P4-00:18` | `\ref{III-ch:levy}` | P3-10 — `\label{ch:levy}` | Procesy Lévy’ego |

## Potwierdzenie konfiguracji

W `books/pl/probability_volume_iv.tex` są kolejno:

```latex
\usepackage{xr-hyper}
\IfFileExists{probability_volume_i.aux}{%
  \externaldocument[I-]{probability_volume_i}[probability_volume_i.pdf]%
}{}
\IfFileExists{probability_volume_ii.aux}{%
  \externaldocument[II-]{probability_volume_ii}[probability_volume_ii.pdf]%
}{}
\IfFileExists{probability_volume_iii.aux}{%
  \externaldocument[III-]{probability_volume_iii}[probability_volume_iii.pdf]%
}{}
```

Odpowiadające oryginalne deklaracje `\label{ch:...}` są w źródłach rozdziałów, a nie w postaci prefiksowanej. Nie stwierdzono tu potrzeby dopisywania ani przemianowywania etykiet.

## Ograniczenia i dalsze czynności

1. Ta iteracja bada semantyczne istnienie celów i deklarowaną konfigurację `xr-hyper`; **nie wykonała kompilacji PDF z rzeczywistymi plikami `.aux`**, więc nie stanowi potwierdzenia działających odsyłaczy w czytniku PDF.
2. W indeksie aplikacji należy rozróżnić `missing` (rzeczywiście brakujący cel) od `external_resolved` (cel identyfikowany przez parę: tom docelowy, etykieta lokalna), zachowując pole oryginalnego tekstu odsyłacza.
3. Zależności międzytomowe trzeba rozstrzygać według konfiguracji dokumentu źródłowego, nie przez globalne usuwanie pierwszego prefiksu. Inaczej łatwo wskazać niewłaściwy rozdział lub zgubić kolizje.
4. Do wykonania pozostaje test przebudowy czterech tomów w odpowiedniej kolejności, z powtórną kompilacją po utworzeniu `.aux`, oraz testy regresji parsera dla braku `.aux` i prawdziwie brakujących etykiet.

**Reguła bezstratności:** zachować oryginalne `\label`, `\ref`, `\eqref` oraz dane pochodzenia podczas kopiowania z Biblioteki. Żaden plik `chapters/pl/`, żaden wariant dowodu i gałąź `main` nie zostały zmienione; nie wykonano scalania.

**Postęp:** 169 z 257 problematycznych wystąpień przejrzanych, 88 pozostaje. Ta liczba nie oznacza naprawionego indeksu. Następna partia: 170–182.