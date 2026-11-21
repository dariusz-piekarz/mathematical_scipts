# Biblioteka matematyczna — skrypty LaTeX i Atlas matematyczny

[![Aplikacja i indeks](https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/mathematical-library-app.yml/badge.svg?branch=biblioteka-matematyczna-iteracja-6)](https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/mathematical-library-app.yml)
[![Algebra liniowa](https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/linear-algebra-chapter.yml/badge.svg?branch=biblioteka-matematyczna-iteracja-6)](https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/linear-algebra-chapter.yml)
[![Topologia ogólna](https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/general-topology-chapter.yml/badge.svg?branch=biblioteka-matematyczna-iteracja-6)](https://github.com/dariusz-piekarz/mathematical_scipts/actions/workflows/general-topology-chapter.yml)

**Biblioteka matematyczna** jest rozwijanym zbiorem polskojęzycznych, modułowych książek matematycznych w LaTeX-u. Do repozytorium należy również **Atlas matematyczny** — lokalna aplikacja internetowa służąca do przeszukiwania rozdziałów, czytania źródeł, eksplorowania odsyłaczy i pojęć oraz budowania własnych skryptów z konkretnych fragmentów.

Każdy rozdział ma własne źródło `.tex`; punkty wejścia książek dołączają je przez `\input`. Pliki źródłowe są kanoniczne, a indeks SQLite jest odtwarzalną warstwą pomocniczą. Tekst matematyczny pozostaje po polsku, nazwy katalogów i interfejsy programistyczne — po angielsku.

Projekt jest **aktywnie rozwijany i audytowany**. Działające funkcje aplikacji nie oznaczają, że wszystkie dowody, rysunki i odsyłacze między tomami zostały już ostatecznie zweryfikowane.

## Spis treści

- [Status](#status)
- [Katalog książek](#katalog-książek)
- [Uruchamianie Atlasu](#uruchamianie-atlasu)
- [Jak korzystać](#jak-korzystać)
- [Tworzenie własnego skryptu](#tworzenie-własnego-skryptu)
- [Kompilacja książek](#kompilacja-książek)
- [Struktura i współtworzenie](#struktura-i-współtworzenie)
- [Testy, CI i audyty](#testy-ci-i-audyty)
- [Ograniczenia](#ograniczenia)
- [Plan rozwoju](#plan-rozwoju)

## Status

**Migawka na 21 listopada 2026 r., gałąź `biblioteka-matematyczna-iteracja-6`.** Aktualny stan odczytuje się z [`catalog/books.json`](catalog/books.json) i [GitHub Actions](https://github.com/dariusz-piekarz/mathematical_scipts/actions).

| Obszar | Stan |
| --- | --- |
| Książki w katalogu | **20** |
| Zarejestrowane rozdziały | **391** |
| Suplementy | **2** |
| Źródła `.tex` w `chapters/pl/` | **393** (rozdziały i suplementy) |
| Explorer, wyszukiwanie i czytnik | **Działają** |
| Graf odsyłaczy i graf pojęć | **Działają** (patrz ograniczenia interpretacji krawędzi) |
| Generator własnych projektów | **Działa**: rozdziały, obiekty, wycinki wierszy, ZIP i manifest |
| Szkice tymczasowe i zapisane projekty | **Działają** |
| Audyty matematyczno-redakcyjne | **Trwają rozdział po rozdziale** |
| Deduplikacja wspólnych tematów | **W toku**, zgodnie z rejestrem kandydatów |
| Pełna automatyczna poprawność wszystkich kombinacji LaTeX | **Nie jest gwarantowana** |

Zielony status workflow oznacza **przejście testów objętych danym workflow**, a nie zakończenie audytu wszystkich twierdzeń. Liczby rozdziałów mogą szybko rosnąć podczas równoległych prac; powyższa tabela jest migawką, nie licznikiem aktualizowanym na żywo.

## Katalog książek

Poniższa lista pochodzi z `catalog/books.json`. Liczba rozdziałów oznacza pozycje rzeczywiście zarejestrowane w książce, **nie** ocenę jej kompletności.

| Książka / punkt wejścia | Rozdziały |
| --- | ---: |
| [Algebra abstrakcyjna](books/pl/abstract_algebra.tex) | 13 (01–13 stabilne) |
| [Geometria algebraiczna](books/pl/algebraic_geometry.tex) | 11 |
| [Topologia algebraiczna](books/pl/algebraic_topology.tex) | 31 |
| [Twierdzenie Banacha–Tarskiego](books/pl/banach_tarski.tex) | 11 |
| [Teoria kategorii](books/pl/category_theory.tex) | 19 |
| [Geometria i topologia różniczkowa](books/pl/differential_geometry_and_topology.tex) | 20 |
| [Analiza funkcjonalna](books/pl/functional_analysis.tex) | 35 |
| [Teoria Galois](books/pl/galois_theory.tex) | 10 |
| [Topologia ogólna](books/pl/general_topology.tex) | 5 |
| [Teoria grafów i węzłów](books/pl/graph_and_knot_theory.tex) | 37 |
| [Teoria całki](books/pl/integration_theory.tex) | 17 |
| [Algebra liniowa](books/pl/linear_algebra.tex) | 22 (01–22 stabilne) |
| [Logika matematyczna i teoria mnogości](books/pl/logic_and_set_theory.tex) | 12 |
| [Teoria miary](books/pl/measure_theory.tex) | 31 |
| [Teoria modeli](books/pl/model_theory.tex) | 19 |
| [Równania różniczkowe cząstkowe](books/pl/partial_differential_equations.tex) | 33 |
| [Rachunek prawdopodobieństwa — tom I](books/pl/probability_volume_i.tex) | 16 |
| [Rachunek prawdopodobieństwa — tom II](books/pl/probability_volume_ii.tex) | 15 |
| [Rachunek prawdopodobieństwa — tom III](books/pl/probability_volume_iii.tex) | 17 |
| [Rachunek prawdopodobieństwa — tom IV](books/pl/probability_volume_iv.tex) | 33 |

Książki w `books/pl/` zawierają preambuły, kolejność i `\input`; rozdziały są w `chapters/pl/<subject>/`. Suplementy wymieniane są osobno w katalogu.

## Uruchamianie Atlasu

**Wymagania:** Git, Python 3.11+ oraz przeglądarka internetowa. Dla kompilacji PDF potrzebny będzie dodatkowo TeX Live albo MiKTeX. Sam Atlas nie wymaga Node.js.

### Windows — PowerShell

```powershell
git clone --branch biblioteka-matematyczna-iteracja-6 --single-branch https://github.com/dariusz-piekarz/mathematical_scipts.git
cd mathematical_scipts\application
py -m venv .venv
.\.venv\Scripts\Activate.ps1
.\start.ps1
```

Skrypt `start.ps1` instaluje zależności, w pełnym klonie GitHuba indeksuje kanoniczne `../chapters/pl` i uruchamia lokalny serwer. Otwórz **http://127.0.0.1:8765/**. Zatrzymanie: `Ctrl+C`.

### Linux / macOS

```bash
git clone --branch biblioteka-matematyczna-iteracja-6 --single-branch https://github.com/dariusz-piekarz/mathematical_scipts.git
cd mathematical_scipts/application
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdir -p data
python backend/latex_parser.py index --source ../chapters/pl --recursive \
  --db data/biblioteka.db --aliases config/ALIASY_PO_SCALENIACH.json \
  --report data/index_report.json
python -m uvicorn backend.api:app --host 127.0.0.1 --port 8765
```

**Uwaga:** `start.sh` uruchamia serwer, ale sam nie przebudowuje indeksu; z pełnego klonu wykonaj wcześniej polecenie `index`. Występujące w części źródeł **nierozwiązane lub niejednoznaczne odsyłacze** mogą skutkować kodem wyjścia **2** mimo zapisania bazy i raportu. Jest to stan wymagający dalszego audytu, nie pomyślne rozstrzygnięcie odsyłaczy. Inne niezerowe kody traktuj jako błąd. Jeżeli nie ma `data/biblioteka.db`, API nie zadziała.

Przy pracy z samodzielną paczką offline zamiast pełnego klonu źródłem może być `application/rozdzialy/`; zobacz [dokumentację aplikacji](application/README.md). Repozytorium na GitHubie i aktualny katalog pozostają źródłem prawdy o zawartości.

## Jak korzystać

1. **Explorer:** rozwiń dziedzinę, wybierz rozdział; zmieniaj granularność (moduł, sekcja, obiekt), aby przejść do konkretnej definicji, twierdzenia, dowodu czy przykładu.
2. **Wyszukiwarka:** szukaj nazw, fragmentów lub pojęć. Indeks SQLite FTS5 obsługuje wyszukiwanie pełnotekstowe i otwieranie znalezionych źródeł.
3. **Czytnik:** obejrzyj dokładny LaTeX albo uproszczony podgląd. Klikalne odsyłacze (`\ref`, `\eqref`, `\cref` itd.) pokazują pochodzenie cytowanych etykiet; konflikt właścicieli wymaga wyboru odpowiedniego źródła.
4. **Graf zależności:** porównuj dziedziny, rozdziały, sekcje lub obiekty. Krawędzie w tym grafie pochodzą z **jawnych odsyłaczy LaTeX**, nie z automatycznego wnioskowania o matematycznej implikacji.
5. **Graf pojęć:** wpisz np. „Zorn”, by zobaczyć rzeczywiste wystąpienia i odrębnie opisane relacje matematyczne. Samo współwystępowanie nie jest dowodem implikacji.
6. **Kreator zestawu:** zaznacz elementy, ustaw ich kolejność, sprawdź zależności, pobierz projekt ZIP lub zapisz szkic.

Dostępne API i dokumentacja OpenAPI: **http://127.0.0.1:8765/api/docs**. Przykładowe endpointy: `GET /api/stats`, `GET /api/search?q=Zorn`, `GET /api/concepts/graph?q=Zorn`, `POST /api/generate/manifest` oraz `POST /api/generate`.

## Tworzenie własnego skryptu

W Czytniku możesz dodać **cały rozdział**, **pojedynczy obiekt** (np. lemat albo dowód), zaznaczyć tekst i kliknąć **„+ Zaznaczenie”** lub wpisać numery linii **Od/Do** i kliknąć **„+ Wiersze”**. Następnie przejdź do **Kreatora zestawu**, przestaw elementy strzałkami, nadaj tytuł, wybierz ewentualną głębokość domykania zależności i użyj **„Sprawdź zależności”** oraz **„Pobierz ZIP”**.

Przykładowe żądanie JSON do `POST /api/generate` albo `POST /api/generate/manifest`:

```json
{
  "title": "Mój skrypt matematyczny",
  "closure_depth": 0,
  "items": [
    {"kind": "module", "id": "LA-09"},
    {"kind": "lines", "module": "LA-10", "start_line": 10, "end_line": 20}
  ]
}
```

**Co powstaje:** archiwum ZIP z `main.tex`, dołączanymi fragmentami `.tex`, `manifest.json` (kolejność, źródła, zakresy i pochodzenie), raportami makr i preambuł, ewentualnymi plikami referencyjnymi `aux/*.tex` oraz `build.ps1` / `build.sh` do **lokalnej** kompilacji. Serwer **nie kompiluje PDF** i **nie nadpisuje źródeł**.

Generator usuwa duplikaty i fragmenty zawarte w większych, odrzuca częściowo zachodzące zakresy, a cały rozdział ma pierwszeństwo przed jego wycinkami. Domykanie zależności dla fragmentów korzysta z odsyłaczy w **rzeczywiście wybranych zakresach**, a dalsze poziomy uwzględniają pełne dołączone rozdziały.

**Ważne:** wycięty tekst może nie zawierać definicji, założeń, makr albo obu końców środowiska. Nawet gdy jawne referencje zostały rozpoznane, matematyczna samowystarczalność i kompilowalność arbitralnego zestawu nie są gwarantowane. Mieszanie książek może dodatkowo powodować konflikty preambuł; raport generatora sygnalizuje część z nich.

**Szkice i pliki:** niezapisane szkice są tymczasowe i podlegają automatycznemu czyszczeniu; jawnie zapisane projekty przechowywane są domyślnie w `application/data/saved_projects/`. Zamknięcie karty próbuje usunąć szkic, ale zdarzenia przeglądarki nie są gwarantowane. Pobrane na komputer ZIP-y pozostają poza kontrolą aplikacji.

## Kompilacja książek

Każda książka ma własny punkt wejścia w `books/pl/`. Na przykład:

```bash
cd books/pl
latexmk -pdf -interaction=nonstopmode -halt-on-error linear_algebra.tex
```

Pliki `chapters/pl/.../*.tex` są fragmentami włączanymi przez `\input` i mogą polegać na preambule książki. Nie należy traktować ich jako samodzielnych dokumentów. W części workflow GitHub Actions dostępne są także artefakty z PDF i logami kompilacji.

## Struktura i współtworzenie

```text
books/pl/                         Książki: preambuły, kolejność, \input
chapters/pl/<subject>/            Kanoniczne źródła rozdziałów
shared/pl/                        Moduły wspólne po zweryfikowanym scaleniu
sources/pl/                       Kopie oryginalnych materiałów
catalog/books.json                Rejestr książek, rozdziałów i suplementów
catalog/topic_registry.json       Kandydaci do deduplikacji i ich status
application/backend/              Indeksowanie, API, generator, graf pojęć
application/frontend/             Explorer, czytnik, grafy, kreator
application/config/preambles/     Preambuły generatora
application/tests/                Testy API, generatora, przeglądarki
tools/                            Walidatory i testy matematyczne
audits/                           Raporty iteracyjnych audytów
.github/workflows/                Kontrole CI
```

**Dodawanie rozdziału:** użyj schematu `chapters/pl/<english_subject>/NN-polski-tytul.tex` (ASCII w ścieżce; przyrostki typu `15A` / `15B` są obsługiwane), zaktualizuj `books/pl/<book>.tex` i **dokładną kolejność** w `catalog/books.json`. Przy nowej dziedzinie potrzebne są także mapowanie indeksu i szablon preambuły generatora. Wersjonuj wszystkie pliki danych, grafik i kodu wymagane przez rozdział; niedozwolone są zależności do nieistniejących plików lokalnych.

**Zasada deduplikacji:** jeden temat powinien docelowo mieć jedno źródło kanoniczne, ale dopiero po porównaniu merytorycznym. Zachowujemy wszystkie istotnie różne definicje, twierdzenia, warianty dowodów, przykłady, rysunki i kod. Utrzymujemy poprawne odsyłacze i aliasy. Kandydaci do scalenia są opisani w [`catalog/topic_registry.json`](catalog/topic_registry.json); oznaczenie „pending” nie znaczy, że merge został wykonany.

## Testy, CI i audyty

Z katalogu głównego:

```bash
python tools/audit_chapter_dependencies.py
python tools/validate_repository.py
python -m unittest discover -s tools/tests -v
```

Z katalogu `application/`, po przebudowaniu indeksu:

```bash
python -m unittest discover -s tests -v
python backend/latex_parser.py audit --db data/biblioteka.db
```

[Workflow aplikacji](.github/workflows/mathematical-library-app.yml) sprawdza m.in. indeks, pochodzenie etykiet, regresje API i generatora oraz realną przeglądarkę Chromium. Odrębne workflow walidują wybrane rozdziały (m.in. algebrę liniową, algebrę abstrakcyjną, logikę i topologię algebraiczną).

**Standard audytu rozdziału:** poprawność matematyczna, wszystkie założenia i kwantyfikatory, szczegółowość dowodów, przykłady i kontrprzykłady, język, zgodność terminologii, wykresy i TikZ, odsyłacze, kompilacja oraz testy CLI. Powtarzamy kontrolę do stabilizacji rozdziału, potem wypychamy go na **istniejącą gałąź**, bez tworzenia równoległych wersji.

**Uzasadnianie wzorów i przejść w dowodach:** każdy nietrywialny wzór (równość, nierówność, tożsamość, implikacja) lub krok rozumowania musi mieć zrozumiałą podstawę. Wystarcza **choćby krótkie, trafne wyjaśnienie** albo **wskazanie właściwego twierdzenia, lematu, definicji, przykładu bądź wcześniejszej konstrukcji**; dotyczy to również poprawnie nazwanego wyniku zewnętrznego, jeżeli wiadomo, jaka jego własność jest stosowana (np. „z konstrukcji powyżej”, „stosując twierdzenie o ...”). Nie trzeba ponownie przeprowadzać znanego już dowodu ani zawsze umieszczać formalnego `\ref`, jeżeli z kontekstu jasno wynika, skąd bierze się wzór i dlaczego użyty fakt ma tu zastosowanie. Jeżeli krok jest bezpośrednim rachunkiem lub zastosowaniem definicji, dodatkowe objaśnienie nie jest konieczne. **Do poprawy kwalifikuje się dopiero nietrywialny krok pozostawiony bez żadnego rzeczywistego wyjaśnienia ani rozpoznawalnego, adekwatnego odwołania**; należy wtedy dopisać wyprowadzenie lub wskazać jego podstawę. Samo „oczywiście” lub „standardowo”, bez rozpoznawalnej podstawy w przypadku nietrywialnego twierdzenia, nie wystarcza. Przyjęty wzorzec ogólnej szczegółowości dowodów i przykładów pozostaje bez zmian: rozdział 01 „Geometrii różniczkowej”.

Rejestr `application/config/pending_reference_baseline.json` dokumentuje odsyłacze wyprzedzające lub wymagające przeglądu; **nie oznacza ich jako rozwiązanych**. Niepełne importy, kolizje etykiet i brakujące cele pozostają jawną kolejką audytową. Przykład: książka geometrii i topologii różniczkowej ma aktualnie 20 zarejestrowanych rozdziałów, a pełna weryfikacja planowanego zakresu 36 rozdziałów jest nadal otwarta.

## Ograniczenia

- Indeksator jest analizatorem **statycznym**; nie rozwija dowolnych makr ani nie wykonuje kompilacji TeX.
- Uproszczony podgląd w czytniku nie zastępuje PDF.
- Graf jawnych referencji nie dowodzi logicznej zależności; graf pojęć oddziela poświadczone wystąpienia od jawnie zarejestrowanych relacji.
- Pełna zgodność preambuł i matematyczna samowystarczalność zestawionych fragmentów nie są automatycznie zapewniane.
- W katalogu mogą pozostać konflikty etykiet, nierozwiązane odsyłacze do przyszłych rozdziałów i nieprzeniesione jeszcze źródła. Nie należy tworzyć pozornych etykiet, by tylko „zazielenić” CI.
- Serwer działa lokalnie na `127.0.0.1`. Nie wystawiaj go do internetu bez osobnej konfiguracji zabezpieczeń.

## Plan rozwoju

**Priorytet nowych skryptów (ustalona kolejność):**

1. **Topologia ogólna** — od aksjomatów i podstaw przez zwartość, metryzowalność, sieci, filtry i uniformizacje.
   - **Zaplanowane do części o zwartości (decyzja z 21 listopada 2026):** twierdzenie o zanurzaniu przestrzeni Tychonoffa w kostkę \([0,1]^I\), z konstrukcją zanurzenia i pełnym dowodem. Nie włączać do rozdziału 05 o aksjomatach oddzielania.
2. **Analiza matematyczna** — uporządkowany, samodzielny kurs od fundamentów do analizy wielu zmiennych.
3. **Analiza zespolona** — jedna i wiele zmiennych, pseudowypukłość, geometria zespolona i interpolacja.
4. **Teoria liczb i arytmetyka** — podejście elementarne, algebraiczne, analityczne i geometryczne.

**Równolegle:** kontynuacja audytów istniejących działów, przegląd brakujących odsyłaczy i importów, porównywanie nakładających się opracowań oraz bezstratne scalanie wspólnych modułów.

**Plan techniczny Atlasu:** pełniejsze rozpoznawanie środowisk LaTeX i kontekstu wycinków; bezpieczniejsze łączenie preambuł; dokładniejsze raportowanie `xr-hyper` i kompilacji; rozwój semantycznego grafu pojęć z dowodowym uzasadnieniem krawędzi; dalsze testy przeglądarkowe, regresyjne i walidatory CI.

**W dalszej kolejce:** teoria orbifoldów oraz geometria na rozmaitościach Banacha, Hilberta i Frécheta. Analiza harmoniczna jest już w dużej mierze omówiona w analizie funkcjonalnej, teorii miary i RRC; ewentualny skrypt przekrojowy powinien wykorzystywać istniejące fragmenty, nie je przepisywać.

---

**Źródła prawdy:** [katalog książek](catalog/books.json), pliki `chapters/pl/`, [rejestr tematów](catalog/topic_registry.json), [workflow GitHub Actions](https://github.com/dariusz-piekarz/mathematical_scipts/actions). Historyczne README, archiwa offline i wcześniejsze raporty mogą mieć nieaktualne liczby.
