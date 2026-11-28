# Audyt integralności odsyłaczy — partia XI (131–143)

Data: 20 listopada 2026 r.  
Repozytorium: `dariusz-piekarz/mathematical_scipts`  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Indeks źródłowy: `reference_provenance_audit_355.json` (355 rozdziałów); numeracja obejmuje wystąpienia z tablicy `unresolved_references`, licząc od 1.

## Wynik

**13/13 odsyłaczy** ma w surowym indeksie status `missing`, jednak wszystkie 13 są formalnymi odsyłaczami międzytomowymi do rzeczywiście istniejących rozdziałów. Sprawdzono osiem rozdziałów cytujących i dziesięć różnych rozdziałów docelowych (tomy I–IV), a także konfigurację `xr-hyper` w plikach `books/pl/probability_volume_ii.tex` i `books/pl/probability_volume_iii.tex`.

To nie jest brak tekstu ani potrzeba tworzenia nowych etykiet. Prefixy `I-`, `II-`, `III-`, `IV-` są nazwami przestrzeni odsyłaczy tworzonymi podczas importowania pomocniczych plików `.aux` przez `\externaldocument[PREFIX]{...}`. **Oryginalne deklaracje `\label{ch:...}` muszą pozostać bez zmian**, natomiast cytowania `\ref{IV-ch:...}` i analogiczne są prawidłowe w kontekście międzytomowym.

## Rozpoznanie każdego wystąpienia

| Nr | Źródło cytowania | Oryginalny odsyłacz | Zweryfikowany właściciel i etykieta | Zakres |
|---:|---|---|---|---|
| 131 | `P2-01:3` | `\ref{I-ch:probability}` | P1-02, `\label{ch:probability}` | Przestrzeń probabilistyczna i miara prawdopodobieństwa |
| 132 | `P2-01:3` | `\ref{IV-ch:time-series}` | P4-16, `\label{ch:time-series}` | Wnioskowanie z procesów zależnych i szeregi czasowe |
| 133 | `P2-04:3` | `\ref{IV-ch:conjugate-families}` | P4-18, `\label{ch:conjugate-families}` | Rodziny sprzężone |
| 134 | `P2-04:3` | `\ref{IV-ch:glm}` | P4-14, `\label{ch:glm}` | Uogólnione modele liniowe (w tym Poissona) |
| 135 | `P2-05:3` | `\ref{I-ch:markov}` | P1-12, `\label{ch:markov}` | Łańcuchy Markowa w czasie dyskretnym |
| 136 | `P2-05:3` | `\ref{IV-ch:mcmc}` | P4-24, `\label{ch:mcmc}` | Metody MCMC |
| 137 | `P2-07:3` | `\ref{III-ch:wiener-integral}` | P3-01, `\label{ch:wiener-integral}` | Całka Wienera dla funkcji deterministycznych |
| 138 | `P2-07:3` | `\ref{IV-ch:monte-carlo}` | P4-23, `\label{ch:monte-carlo}` | Metody Monte Carlo |
| 139 | `P2-09:3` | `\ref{IV-ch:glm}` | P4-14, `\label{ch:glm}` | Uogólnione modele liniowe (w tym Poissona) |
| 140 | `P2-13:3` | `\ref{III-ch:ito-construction}` | P3-02, `\label{ch:ito-construction}` | Konstrukcja całki Itô |
| 141 | `P3-01:3` | `\ref{II-ch:wiener}` | P2-07, `\label{ch:wiener}` | Proces Wienera |
| 142 | `P3-01:3` | `\ref{IV-ch:monte-carlo}` | P4-23, `\label{ch:monte-carlo}` | Metody Monte Carlo |
| 143 | `P3-05:3` | `\ref{IV-ch:monte-carlo}` | P4-23, `\label{ch:monte-carlo}` | Metody Monte Carlo |

## Podstawa semantyczna i techniczna

- `P2-01` kieruje do konstrukcji przestrzeni probabilistycznej w tomie I i statystyki danych zależnych w tomie IV.
- `P2-04` łączy proces Poissona z rodzinami sprzężonymi oraz regresją Poissona w GLM. `P2-09` również cytuje GLM w kontekście intensywności zliczeń i czasu ekspozycji.
- `P2-05` łączy łańcuchy Markowa w czasie ciągłym z czasem dyskretnym i z metodami MCMC.
- `P2-07` przechodzi od procesu Wienera do jego całkowania w tomie III oraz symulacji w tomie IV; `P2-13` odsyła do konstrukcji całki Itô.
- `P3-01` cytuje własności procesu Wienera z tomu II, a `P3-01` i `P3-05` odsyłają do metod Monte Carlo z tomu IV.
- Pliki główne tomów II i III zawierają `\usepackage{xr-hyper}`, warunkowe importowanie `.aux` i `\externaldocument[I-]`, `\externaldocument[II-]`, `\externaldocument[III-]` lub `\externaldocument[IV-]` odpowiednio do importowanego tomu.

## Zalecane działanie (bez ingerencji w treść)

1. W parserze aplikacji rozpoznawać odsyłacze `I-ch:...`, `II-ch:...`, `III-ch:...`, `IV-ch:...` **w kontekście źródłowego tomu**, a nie przez usuwanie prefiksu globalnie. Rozpoznanie powinno zwracać docelowy tom i oryginalną etykietę. Nie wolno wybierać przypadkowego właściciela niejednoznacznej nazwy `ch:...`.
2. Dodać do raportów status np. `external_resolved` dla potwierdzonych celów międzytomowych, odrębny od `missing`, wraz z informacją o regule `xr-hyper`. Oryginalne pole `target_label` należy zachować.
3. Kompilować tomy do wspólnego katalogu wynikowego, aby wygenerować właściwe `.aux`, a następnie ponownie kompilować każdy tom z importem pozostałych. W tej iteracji **nie wykonywano jeszcze rzeczywistego testu kompilacji PDF ani `.aux`**.
4. Uzupełnić automatyczne testy parsera o prefiksy tomów, brakujący plik `.aux`, rzeczywiście brakujący cel i rozstrzygnięcie lokalnej kolizji z prefiksem.

## Zasady ochrony

Nie modyfikowano kanonicznych rozdziałów, deklaracji `\label`, cytowań `\ref` ani gałęzi `main`. Nie scalano niezależnych opracowań. W razie kopiowania materiału zachowuje się jego oryginalne etykiety i odsyłacze. Ten audyt nie oznacza, że zgłoszone `missing` zostały już usunięte z indeksu.

**Licznik audytu: 143/257 przejrzanych wystąpień, 114 pozostałych.** Następna partia: 144–156.