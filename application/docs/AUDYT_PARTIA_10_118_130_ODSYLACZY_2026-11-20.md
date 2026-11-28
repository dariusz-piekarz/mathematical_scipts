# Audyt odsyłaczy 118–130 — partia X (20.11.2026)

**Zakres:** kanoniczny indeks 355 rozdziałów, `reference_provenance_audit_355.json`, wystąpienia 118–130 w kolejności tego raportu. Odczytano źródła `P1-03`, `P1-07`–`P1-10`, `P1-12`, `P1-14` oraz dziesięć docelowych rozdziałów tomów II i IV. Wszystkie 13 wystąpień mają w indeksie `status=missing` i występują w trzecim wierszu swoich rozdziałów, w paragrafie „Odsyłacze międzytomowe”.

## Rozstrzygnięcia dla każdego wystąpienia

| Nr | Źródło | Oryginalne cytowanie | Wskazany istniejący rozdział i jego oryginalna etykieta | Ocena |
|---:|---|---|---|---|
| 118 | `P1-03:3` | `\ref{IV-ch:bayes-foundations}` | `P4-17`: `\label{ch:bayes-foundations}` | prefiks międzytomowy, zgodny z tematyką |
| 119 | `P1-03:3` | `\ref{IV-ch:conjugate-families}` | `P4-18`: `\label{ch:conjugate-families}` | prefiks międzytomowy, zgodny z tematyką |
| 120 | `P1-07:3` | `\ref{IV-ch:asymptotic-estimation}` | `P4-08`: `\label{ch:asymptotic-estimation}` | prefiks międzytomowy, zgodny z tematyką |
| 121 | `P1-08:3` | `\ref{IV-ch:estimators}` | `P4-05`: `\label{ch:estimators}` | prefiks międzytomowy, zgodny z tematyką |
| 122 | `P1-08:3` | `\ref{IV-ch:monte-carlo}` | `P4-23`: `\label{ch:monte-carlo}` | prefiks międzytomowy, zgodny z tematyką |
| 123 | `P1-09:3` | `\ref{IV-ch:testing}` | `P4-09`: `\label{ch:testing}` | prefiks międzytomowy, zgodny z tematyką |
| 124 | `P1-09:3` | `\ref{IV-ch:asymptotic-estimation}` | `P4-08`: `\label{ch:asymptotic-estimation}` | prefiks międzytomowy, zgodny z tematyką |
| 125 | `P1-10:3` | `\ref{IV-ch:sufficiency}` | `P4-06`: `\label{ch:sufficiency}` | prefiks międzytomowy, zgodny z tematyką |
| 126 | `P1-10:3` | `\ref{IV-ch:bayes-foundations}` | `P4-17`: `\label{ch:bayes-foundations}` | prefiks międzytomowy, zgodny z tematyką |
| 127 | `P1-12:3` | `\ref{II-ch:ctmc}` | `P2-05`: `\label{ch:ctmc}` | prefiks międzytomowy, zgodny z tematyką |
| 128 | `P1-12:3` | `\ref{IV-ch:mcmc}` | `P4-24`: `\label{ch:mcmc}` | prefiks międzytomowy, zgodny z tematyką |
| 129 | `P1-14:3` | `\ref{IV-ch:mcmc}` | `P4-24`: `\label{ch:mcmc}` | prefiks międzytomowy, zgodny z tematyką |
| 130 | `P1-14:3` | `\ref{II-ch:mart-cont}` | `P2-11`: `\label{ch:mart-cont}` | prefiks międzytomowy, zgodny z tematyką |

**Weryfikacja:** ręcznie otwarto 10 różnych docelowych plików z `chapters/pl/probability_volume_ii/` i `chapters/pl/probability_volume_iv/`; każdy zaczyna się od deklaracji `\label{ch:...}` odpowiadającej części po prefiksie `II-`/`IV-`. Oryginalne odwołania są celowo poprzedzone prefiksem, ale same etykiety w dokumentach docelowych nie są tak zapisane. Stąd parser niezależnych rozdziałów oznacza je jako brakujące. Dotychczasowa diagnoza `missing` **nie oznacza**, że brak odpowiednich rozdziałów ani że trzeba do nich dopisywać nowe twierdzenia.

## Mechanizm dokumentowy i ograniczenia weryfikacji

Pliki `books/pl/probability_volume_i.tex`, `_ii.tex` i `_iv.tex` już zawierają `\usepackage{xr-hyper}` i warunkowe wywołania `\externaldocument[IV-]{probability_volume_iv}[probability_volume_iv.pdf]` oraz analogicznie `II-`. Pakiet czyta etykietę `ch:bayes-foundations` z pliku `.aux` tomu IV i udostępnia ją w tomie I pod nazwą `IV-ch:bayes-foundations`. Jest to zamierzone rozróżnienie: **oryginalna deklaracja pozostaje bez prefiksu**; prefiks powstaje przy imporcie i jest częścią przestrzeni nazw cytującego tomu. Dlatego nie zmieniamy `\label` ani `\ref` w kanonicznych źródłach.

W tej partii sprawdzono **konfigurację i zgodność semantyczną odsyłaczy**, ale **nie wykonano pełnej kompilacji wielotomowej i nie zweryfikowano obecności wygenerowanych `.aux`**. Aktualne `xr-hyper` jest warunkowe (`\IfFileExists`), zatem pojedynczy tom może kompilować się bez innych tomów z ostrzeżeniami o niezdefiniowanych odsyłaczach. Status „możliwy do rozwiązania przez `xr-hyper`” nie oznacza jeszcze potwierdzenia przez kompilator.

## Dalsze działania bez scalania treści

1. W aplikacji odróżnić `brak deklaracji w bieżącym indeksie` od `zewnętrzny odsyłacz z prefiksem i ustalonym właścicielem`, na podstawie konfiguracji `\externaldocument` i rzeczywistych deklaracji. Nie zmieniać istniejących nazw źródłowych.
2. W oddzielnym etapie kompilacyjnym zbudować tomy II i IV, potem tom I, drugi przebieg dla cross-refs, i sprawdzić brak ostrzeżeń o wskazanych 13 etykietach; kontrolować również pliki `.aux` i ścieżki do PDF.
3. Do czasu pełnej kompilacji pozostawić w raporcie pierwotny status parsera `missing` wraz z nadaną niniejszym audytem klasyfikacją `external_xr_hyper_candidate`. Nie usuwać ich z liczby problemów w bieżącej migawce bazy.
4. Nie rozpoczynać łączenia działów: zostawić oba rozdziały jako autonomiczne moduły i zachować wszystkie oryginalne `\label` i `\ref`.

**Postęp audytu:** 130/257 wystąpień przejrzanych, 127 pozostaje. Spośród tych 13: 13 kandydatów zewnętrznych `xr-hyper`, 0 nierozpoznanych matematycznie celów, 0 zmienionych odsyłaczy. Nie modyfikowano `chapters/pl/`, `books/pl/` ani `main`.

**Następna partia:** wystąpienia 131–143; osobny test pełnego potoku `xr-hyper` z rzeczywistymi plikami `.aux`.