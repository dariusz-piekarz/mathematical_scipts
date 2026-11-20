# Biblioteka matematyczna — plan iteracji i dziennik

Aktualizacja: 19 listopada 2026. Katalog roboczy Biblioteki ChatGPT: `/Biblioteka matematyczna`.
Dokument przeznaczony do odczytu na początku **każdej automatycznej lub ręcznej iteracji**.

## Niezmienne zasady

1. `rozdzialy/*.tex` jest wspólną, kanoniczną bazą treści. Nie wolno zastępować jej kopiami z archiwum aplikacji bez odrębnego porównania wersji.
2. `skrypty/` to docelowo dokumenty składane z rozdziałów przez `\input`; bez dublowania treści.
3. Etykiety `\label` zachowują unikalność i stabilność. Po scaleniu odnotować aliasy, przekierowania i zależności; brakujący rozdział obsłużyć przez `xr-hyper` z prawdziwym `.aux`.
4. Nie usuwać różnych wariantów dowodów, przykładów, zadań, rysunków i kodu pod pozorem deduplikacji. Każda zmiana musi mieć mapę pochodzenia i walidację.
5. Nie mylić testów statycznych ze sprawdzeniem kompilacji PDF ani z audytem poprawności matematycznej.
6. Zanim zacznie się kolejny etap, sprawdzić ostatnie archiwum i ten dokument; po zakończeniu etapu zaktualizować stan i zapisać konkretne pliki w Bibliotece.

## Kolejka etapów (po jednej mierzalnej iteracji naraz)

- [x] **0. Parser i baza** — 233 moduły, 8686 obiektów, 2363 etykiety, 1515 odsyłaczy, bez kolizji w migawce 2026-11-19.
- [x] **1. Explorer, dymki, graf jawnych odsyłaczy i API** — aplikacja 0.2, 36 testów.
- [x] **2. Generator modularnych projektów `.tex` 0.3** — wybór rozdziałów i obiektów, kopiowanie źródeł, `main.tex`, prefabrykowane preambuły, zewnętrzne `aux/*.tex`, skrypty kompilacji z `xr-hyper`, eksport ZIP. 46 testów Python, 2 pozytywne kompilacje PDF.
- [ ] **3. Generator 0.4 — kompletność matematyczna fragmentów** — wykrywanie wolnych makr i niejawnych założeń, pomoc w dołączaniu definicji, konfliktów preambuł między dziedzinami, stabilne atrybucje przy zagnieżdżeniach.
- [ ] **4. UX i renderowanie matematyki** — prawdziwy podgląd części TeX, lepsze dymki, granice rozdziałów, filtry grafu, testy przeglądarkowe na środowisku umożliwiającym test lokalnego HTTP.
- [ ] **5. Graf semantyczny** — proponowanie relacji „uogólnia”, „przykład”, „korzysta z”, „równoważne” z rozróżnieniem jawnego dowodu i hipotezy; bez automatycznego stwierdzania równoważności twierdzeń na podstawie embeddingów.
- [ ] **6. Mapowanie pokrywających się treści** — automatyczna lista kandydatów, pary fragmentów, karty porównań, mapa pochodzenia; z zachowaniem źródeł i metadanych.
- [ ] **7. Deduplikacja + scalanie partiami** — kontrola funkcjonalna, matematyczna i redakcyjna każdego scalań, translacja etykiet, test globalnych i skryptowych odsyłaczy. Nie zastępować bez przeglądu kanonicznych źródeł.
- [ ] **8. Audyt techniczny całej zaktualizowanej Biblioteki** — labele, relacje, kompilacja, ostrzeżenia, przenikanie makr, obrazy i kod.
- [ ] **9. Audyt szczegółowy KAŻDEGO rozdziału** — serie 3–5 modułów na iterację, zapis wyników w `AUDYT_ROZDZIALOW.csv`, naprawa i ponowny audyt przed oznaczeniem jako „zaakceptowany”. Kolejka odzwierciedla aktualną kanoniczną liczbę modułów po scaleniu.
- [ ] **10. Audyt międzyrozdziałowy i końcowy** — testy wielu kombinacji skryptów, wywodzenie z jednego źródła, pokrycie definicji i pojęć przed użyciem, raport integralności.

## Standard szczegółowego audytu jednego rozdziału

Niezależnie ocenić i opisać: (1) język polski/terminologia, (2) samodzielność i kompletność definicji, zakresy kwantyfikacji, (3) założenia i poprawność twierdzeń, (4) wszystkie kroki dowodów i kontrprzykłady, (5) przykłady i zadania oraz wskazówki, (6) notację i lokalne objaśnienia symboli, (7) rysunki TikZ/ilustracje i kod obliczeniowy, (8) `\label`, `\ref`, `xr-hyper`, (9) kompilację i log, (10) brak utraty treści w stosunku do źródeł. Każda uwaga z lokalizacją, powagą, poprawką i wynikiem retestu.

Statusy: `oczekuje` → `w_trakcie` → `do_poprawy` → `ponowny_audyt` → `zaakceptowany`. Stan zapisujemy w CSV, nie w domysłach.

## Dziennik wykonanych iteracji

- **v0.1** — źródła podzielone i zaindeksowane; rejestr etykiet i zależności.
- **v0.2** — API FastAPI, Explorer, wyszukiwarka FTS, podgląd `\ref`, graf dwudzielny, plan zestawów.
- **v0.3, 19.11.2026** — `backend/generator.py`, `POST /api/generate` i `/api/generate/manifest`, interfejs „Generuj ZIP”, 12 szablonów preambuł, 10 nowych testów (razem 46), pozytywna kompilacja pełnego `BT-00` z referencją do `BT-04` (4 strony), pozytywna kompilacja `ALG-09/proof/0004` z referencją do reszty `ALG-09` (3 strony). Brak nieokreślonych odsyłaczy w obu przykładowych dokumentach. Sprawdzenie przeglądarki przez Playwright zablokowane przez politykę środowiska `ERR_BLOCKED_BY_ADMINISTRATOR`; nie jest zaliczone. Brak audytu matematycznego 233 rozdziałów.

## Następny nieukończony etap

**3. Generator 0.4 — użyteczność fragmentów w zestawach między dziedzinami.** Najpierw przypadki z `ALG`, `TOP`, `AT`: porównaj preambuły, zaimplementuj bezkonfliktowe łączenie pakietów i makr albo czytelnie raportuj brak zgodności; dodaj testy rzeczywistej kompilacji z minimum dwoma różnymi dziedzinami. Nie deklaruj samowystarczalności matematycznej na podstawie samych etykiet.

## Harmonogram

Automatyzacja ChatGPT „Iteracje Biblioteki matematycznej” uruchamiana co godzinę (Europe/Warsaw), pierwsze uruchomienie 2026-11-19 17:00. Użytkownik może wywołać iterację również ręcznie, pisząc „Kontynuuj Bibliotekę”. Harmonogram zleca kolejną iterację, ale nie gwarantuje, że każde środowisko będzie miało identyczne uprawnienia do zapisu lub możliwość lokalnej kompilacji; wynik każdorazowo weryfikujemy.

Po ukończeniu punktu 10 nie wykonywać fikcyjnych zmian. Zgłosić finalny stan i wyłączyć lub poprosić użytkownika o wyłączenie automatyzacji.

### Iteracja v0.4a — 19.11.2026, 17:04

Dodano `preamble_compatibility` do `backend/generator.py`: konserwatywny raport syntaktyczny opcji pakietów, nazw makr i środowisk dla wyboru wielu dziedzin; plik `preamble_audit.json` jest dołączany do każdego eksportu, a manifest ma pole `preamble_compatibility`. Nie wykonujemy ryzykownego automatycznego scalania preambuł. Dwa testy regresyjne dodane; **48/48 testów Python zaliczone**. Wygenerowano projekt `ALG-09 + TOP-01` i wykonano pierwszą kompilację `pdflatex main.tex`: kod wyjścia 0, 16 stron. To NIE jest pełna kompilacja `xr-hyper`: zewnętrzne dokumenty `.aux` i kolejne przebiegi pozostają do wykonania. Test nie dowodzi kompatybilności wszystkich kombinacji dziedzin ani matematycznej samowystarczalności. Kanoniczne źródła niezmienione.

**Następny krok etapu 3:** rozszerzyć analizę makr o zależności użyć (nie tylko deklaracji), przetestować więcej par dziedzin, wykonać pełną kompilację `xr-hyper` i zweryfikować logi. Etap 3 pozostaje otwarty.

### Iteracja v0.4b — 19.11.2026

Rozszerzono `backend/generator.py` o `macro_usage_audit`: dla każdego wybranego modułu wyszukuje użycia makr zdefiniowanych w preambule innego wybranego modułu, lecz nieobecnych w preambule głównej. Raport `macro_usage_audit.json` jest dołączany do eksportu i manifestu. Wynik jest **konserwatywną listą kandydatów do kontroli**, a nie dowodem braku makra: parser nie rozwija definicji warunkowych ani makr z pakietów. Dodano 2 testy regresyjne. **50/50 testów Python przechodzi**.

Wykonano rzeczywistą kompilację `BT-00` z referencją do `BT-04` przez `bash build.sh`: kompilacja dokumentu `aux/BT-04.tex` i dwa przebiegi `main.tex`, kod wyjścia 0, plik `aux/BT-04.aux` oraz `main.pdf` utworzone, w `main.log` nie znaleziono ostrzeżeń o niezdefiniowanych odsyłaczach. Zapisano `data/raport_v04b.json` i `examples/xr_hyper_BT-00_v04b.pdf`. Nie sprawdzono pełnej zgodności wszystkich dziedzin; etap 3 nadal otwarty. Kanoniczne `rozdzialy/*.tex` nie zostały zmodyfikowane.

**Następny krok:** wykrywanie definicji makr w samych rozdziałach, filtrowanie komentarzy i `\\verb` w skanerze użyć, testy pełnego `xr-hyper` dla pary międzydziedzinowej z faktycznymi referencjami zewnętrznymi; dopiero potem rozszerzenia interfejsu.

### Iteracja v0.4c — 19.11.2026

Poprawiono `backend/generator.py`: skaner `scan_tex_code` maskuje komentarze LaTeX, typowe środowiska dosłowne (`verbatim`, `lstlisting`, `minted`, `Verbatim`, `comment`) oraz `\verb` i `\lstinline` przed analizą użyć makr. Audyt pomija makra zadeklarowane w treści wybranego rozdziału przez rozpoznawane `\newcommand`, `\renewcommand`, `\providecommand`, `\DeclareMathOperator` i `\def`; dodaje liczniki lokalnych deklaracji. Cztery nowe testy regresyjne; **54/54 testy Python przechodzą**. Testy na prawdziwej bazie `ALG-09 + TOP-01` i `BT-00` wykonane; raport `data/raport_v04c.json`. Nie zmieniono kanonicznych źródeł. W tej iteracji nie wykonywano nowej kompilacji PDF ani pełnego testu `xr-hyper` między dziedzinami. Ograniczenia: catcode, zakres grup, warunki, własne środowiska dosłowne i makra pakietów. **Następny krok:** test pełnego `xr-hyper` dla rzeczywistej pary międzydziedzinowej, z kontrolą logów i zgodności preambuł; etap 3 nadal otwarty.

### Iteracja v0.5.2 — 19.11.2026

Wykonano rzeczywisty test kompilacji zestawu międzytomowego `P1-03 + P4-17` (aktualna migawka 264 modułów z archiwum 0.5.1). Generator wskazał pięć odsyłaczy zewnętrznych, przygotowując pliki pomocnicze dla czterech modułów. `bash build.sh` zakończył się błędem; pierwszy błąd to brak `\arraybackslash`, następnie brak `\toprule`, a po konserwatywnym uzupełnieniu pakietów `array` i `booktabs` kompilacja zatrzymała się na niezdefiniowanym środowisku `zadanie`. **Nie uznajemy kompilacji międzytomowej za zakończoną.**

W `backend/generator.py` dodano zapewnienie pakietów `array` i `booktabs` (bez powtórnego importu, jeżeli już występują w zbiorczej deklaracji `\usepackage{booktabs,array,...}`). Dodano `tests/test_cross_preamble.py`. **62/62 testy Python przechodzą**, ale pełna kompilacja tego zestawu pozostaje negatywna. Szczegółowy raport: `data/raport_v05_2.json`. Kanoniczne źródła `rozdzialy/*.tex` pozostawiono bez zmian.

**Następny krok:** jawny rejestr środowisk twierdzeniowych dla wszystkich preambuł, bezpieczne mapowanie tylko semantycznie zgodnych nazw oraz wykrywanie konfliktów `\newtheorem`; następnie ponowny pełny test z kontrolą `.aux`, logów i PDF. Nie wprowadzać automatycznych definicji środowisk bez sprawdzenia ich numeracji i stylu.

### Iteracja v0.7 — 19.11.2026, 20:58

Punktem wyjścia była najnowsza migawka `ATLAS_MATHEMATICAL_LIBRARY_APP_06.zip` (352 moduły), nie historyczne 264. Rozszerzono `backend/generator.py` o rejestr `\newtheorem` z nazwą, licznikiem i stylem oraz konserwatywny import brakującego środowiska z preambuły drugiego tomu. Jeśli definicje są różne lub licznik nadrzędny nie istnieje, zgłaszany jest konflikt zamiast automatycznego scalania. Eksport zawiera `theorem_environment_audit.json`. Usunięto z nagłówków generowanych dokumentów odziedziczone `\externaldocument` odnoszące się do nieobecnych PDF-ów tomów; pozostają wyłącznie odsyłacze wygenerowane dla rzeczywistych modułów `ext-*`.

**Test:** zestaw `P1-03 + P4-17`, cztery zewnętrzne pliki `.aux`, `bash build.sh` zakończony kodem 0, 12-stronicowy `main.pdf`; brak ostrzeżeń `undefined references`, `multiply defined` i historycznych brakujących `tom_II/III/IV.aux` w `main.log`. **64/64 testy Python zaliczone** (2 nowe). `main.pdf` SHA-256: `0fc859cdac50170446371e4d2ea9f5a1c16745b60e1cc53269b83d9ccac9daf1`. Kanoniczne rozdziały niezmienione. Zastrzeżenia: skaner nie interpretuje dowolnych makr, `catcode` i warunkowych deklaracji; zgodność wszystkich preambuł nie jest dowiedziona. Następna iteracja: wykrywanie użyć środowisk deklarowanych w treści rozdziałów i konfliktów ich liczników, testy kolejnych par dziedzin oraz testy przeglądarkowe.

### Iteracja v0.8 — 19.11.2026, 22:03

W `backend/generator.py` rozszerzono `theorem_environment_audit` o leksykalny rejestr deklaracji `\newtheorem` w **treści wybranych rozdziałów**, nie tylko w preambułach. Wykrywane są konflikty sygnatur między deklaracjami w treści i preambułach oraz wielokrotne deklaracje zgodnych nazw. Import definicji z preambuły jest pomijany, gdy treść już deklaruje środowisko; nie dokonuje się automatycznej zmiany licznika ani nazwy. Raport zawiera `body_declarations`. Dodano 3 testy regresyjne. **67/67 testów Python przechodzi**. W rzeczywistym projekcie `P1-03 + P4-17` rejestr wykazał 1 import, 0 konfliktów i 0 deklaracji lokalnych. Nie wykonano nowej kompilacji PDF w tej iteracji. Źródła kanoniczne niezmienione. Nadal nie jest rozwiązane modelowanie zasięgu grup, warunków TeX i dowolnych fabryk środowisk; testy przeglądarkowe pozostają otwarte. Następny krok: wykrywanie zasięgu lokalnych deklaracji i rzeczywiste kompilacje par z lokalnymi deklaracjami, następnie testy przeglądarkowe.

### Iteracja v0.9 — 19.11.2026

Zachowano wszystkie wystąpienia deklaracji `\\newtheorem` w pojedynczym źródle zamiast nadpisywać wcześniejsze wpisy w słowniku. Audyt zgłasza teraz `repeated_declaration_within_source` z numerami wierszy i `declaration_inside_brace_group` dla deklaracji w grupie klamrowej (sygnał konserwatywny, nie pełna analiza zasięgu TeX). Trzy nowe testy regresyjne; **70/70 testów Python przechodzi**. W istniejących testach API pojawiają się ostrzeżenia ResourceWarning o niedomkniętych połączeniach SQLite; do osobnego naprawienia. Nie wykonywano kompilacji PDF ani testów przeglądarkowych. Kanoniczne rozdziały pozostają niezmienione. Następny krok: rzeczywisty test kompilacji dokumentu z lokalnymi deklaracjami, obsługa konfliktów między modułami i testy przeglądarkowe.

### Iteracja v0.10 — 19.11.2026

Przeprowadzono przegląd wszystkich 352 modułów w bazie aplikacji pod kątem lokalnych deklaracji `\newtheorem`: **0 modułów z takimi deklaracjami** według skanera leksykalnego. Nie ma więc uczciwej możliwości przeprowadzenia rzeczywistej kompilacji kanonicznego rozdziału z lokalną deklaracją w tej migawce. Dodano `tests/test_local_theorem_compilation.py` z dwiema regresjami: rzeczywista kompilacja syntetycznego dokumentu zawierającego lokalne środowisko (pdflatex, kod 0, PDF utworzony) oraz wykrywanie zdublowanych lokalnych deklaracji. **72/72 testy Python zaliczone**. Nadal występują `ResourceWarning` dla połączeń SQLite w istniejących testach. Testy przeglądarkowe nie były wykonywane. Źródła kanoniczne niezmienione. Raport: `data/raport_v10.json`.

**Następny krok:** poprawić zarządzanie cyklem życia połączeń SQLite w testach, następnie uruchomić testy przeglądarkowe oraz regresje kompilacji na kolejnych rzeczywistych zestawach międzydziedzinowych. Nie oznaczać analizy deklaracji warunkowych TeX-a jako pełnej.

### Iteracja v0.11 — 20.11.2026

Usunięto ostrzeżenia `ResourceWarning` dotyczące SQLite w zestawie testów. Przyczyną były dwa użycia `with connect(...)` bez faktycznego zamykania połączenia (kontekst `sqlite3.Connection` wykonuje commit/rollback, lecz nie wywołuje `close`). Zastąpiono je `contextlib.closing(connect(...))`. Dodatkowo zarządzanie `TestClient` w trzech modułach testowych odbywa się przez wejście/wyjście kontekstu, z poprawnym uruchamianiem i zamykaniem lifespan FastAPI. Test przed poprawką: **72/72**, cztery linie `ResourceWarning` (dwa ostrzeżenia). Test po poprawce: **72/72**, **zero** `ResourceWarning` przy `python -W default -m unittest discover -s tests -q`. Nie zmieniono rozdziałów kanonicznych ani semantyki generatora. Raport `data/raport_v11.json`. Testy przeglądarkowe i kompilacja międzydziedzinowa pozostają otwarte.

**Następny krok:** testy przeglądarkowe oraz kolejna rzeczywista kompilacja międzydziedzinowa, z analizą logów i odsyłaczy.

### Iteracja v0.12 — 20.11.2026

Odczytano roadmapę i bazę v0.11 (352 moduły). Podjęto próbę uruchomienia obu testów Playwright (`tests/browser_e2e.py` oraz `tests/browser_workspace_e2e.py`) z lokalnym serwerem FastAPI; oba zatrzymują się przy nawigacji Chromium na `http://127.0.0.1:18765/` z `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Nie oznaczamy testów przeglądarkowych jako zaliczonych. Zidentyfikowano i usunięto nieaktualne założenie testu `browser_e2e.py`, który oczekiwał tekstu `233 rozdziałów` mimo 352 modułów. Oczekiwanie opiera się teraz na dynamicznej liczbie. Dodano `tests/test_browser_smoke_contract.py` sprawdzający składnię i brak historycznego licznika. **73/73 testy Python zaliczone**.

Ponownie wygenerowano z aktualnej bazy rzeczywisty zestaw `P1-03 + P4-17` z czterema zewnętrznymi celami i uruchomiono `bash build.sh`: kod 0, `main.pdf` utworzony; w `main.log` brak `LaTeX Error`, `undefined references` i `multiply defined`. Test dotyczy tej pary, nie dowodzi zgodności dowolnych preambuł. Kanoniczne rozdziały niezmienione. Raport: `data/raport_v12.json`.

**Następny krok:** testy przeglądarkowe w środowisku bez blokady loopback (lub dopuszczony mechanizm przeglądarkowy), rozszerzenie testów generatora o kolejne pary i analiza bezpieczeństwa API. Etap 3 nadal otwarty.

### Iteracja v0.13 — 20.11.2026

Po odczytaniu roadmapy v0.12 wykonano audyt bezpieczeństwa serializacji ZIP generatora. Poprzednia walidacja `Path(name).parts` zależała od systemu operacyjnego i na Linuksie nie odrzucała ścieżek Windows z `\\`, np. `..\\bad.tex`, ani prefiksów dysków. Zmieniono `backend/generator.py`: walidacja niezależna od systemu odrzuca ścieżki absolutne, prefiksy dysków, backslash, puste segmenty, `.` i `..`, bajt NUL oraz zawartość niebędącą `bytes`. Dodano przypadki regresyjne w `tests/test_generator.py`. **73/73 testy Python zaliczone**, `python -W default -m unittest discover -s tests -q`, kod 0. Liczba testów nie wzrosła, bo rozbudowano istniejącą metodę testową. Kanoniczne rozdziały niezmienione. Nie wykonano w tej iteracji kompilacji PDF ani testów przeglądarkowych; blokada loopback z v0.12 pozostaje nierozwiązana. Raport: `data/raport_v13.json`.

**Następny krok:** przegląd limitów żądań generatora i API, regresje międzydziedzinowe oraz uruchomienie testów przeglądarkowych w środowisku z dozwolonym loopback. Etap 3 pozostaje otwarty.

### Iteracja v0.14 — 20.11.2026

Odczytano dziennik v0.13 i sprawdzono limity generatora. `GenerateRequest` ogranicza wybór do 75 modułów, 300 obiektów i głębokości domknięcia 3, lecz `zip_project` nie ograniczał liczby plików ani łącznego rozmiaru danych przed kompresją. Dodano limity 512 wpisów i 64 MiB danych nieskompresowanych, sprawdzane przed rozpoczęciem zapisu ZIP. Nowy test regresyjny sprawdza przekroczenie obu limitów i akceptację dokładnej granicy rozmiaru. **74/74 testy Python zaliczone** (`python -W default -m unittest discover -s tests -q`, kod 0). Nie wykonano kompilacji PDF ani testów przeglądarkowych. Kanoniczne rozdziały niezmienione. Raport `data/raport_v14.json`.

**Następny krok:** testy limitów na poziomie API, kontrola czasu generowania i kolejna rzeczywista kompilacja międzydziedzinowa; testy przeglądarkowe nadal blokowane przez politykę loopback.

### Iteracja v0.15 — 20.11.2026

Po odczytaniu dziennika v0.14 i sprawdzeniu archiwum aplikacji dodano `tests/test_api_generation_limits.py`, obejmujący trzy testy HTTP: (1) odrzucanie przekroczeń granic `GenerateRequest` (76 modułów, 301 obiektów, głębokość -1/4, tytuł pusty lub 161 znaków); (2) odpowiedź 422 dla nieznanego modułu w trzech punktach końcowych (`/api/generate`, `/api/generate/manifest`, `/api/drafts`); (3) rzeczywisty eksport ZIP przez HTTP, jego typ MIME, integralność i obecność `main.tex`. **77/77 testów Python zaliczonych** (`python -W default -m unittest discover -s tests -q`, kod 0). Bez modyfikacji rozdziałów kanonicznych i kodu produkcyjnego. Testy przeglądarkowe i nowa kompilacja międzydziedzinowa nie były wykonywane; limity czasu CPU i pamięci serwera nadal wymagają osobnego rozwiązania. Następny krok: benchmark generowania na zestawach o rosnącym rozmiarze i niezależne ograniczenie czasu żądań; następnie test kolejnej pary dziedzin z `xr-hyper`.

### Iteracja v0.16 — 20.11.2026

Po odczytaniu dziennika v0.15 i weryfikacji archiwum v0.15 dodano powtarzalny benchmark `scripts/benchmark_generation.py` (odczyt bazy SQLite w trybie `mode=ro`, `perf_counter`, `tracemalloc`, oddzielne czasy przygotowania projektu i kompresji ZIP). W `data/benchmark_v16.json` zapisano rzeczywiste pomiary dla 1, 3 i 5 modułów, po jednym przebiegu: odpowiednio 1.0834 s, 2.8671 s i 4.2226 s (łącznie generowanie + ZIP). Są to pomiary orientacyjne jednego środowiska, nie limity ani wiarygodne percentyle. Próba większego benchmarku z `tracemalloc` przekroczyła dostępny czas wykonania i została przerwana bez raportu; nie zaliczono jej jako wyniku. Dodano `tests/test_benchmark_generation.py` (dwa testy). **79/79 testów Python zaliczonych** (`python -W default -m unittest discover -s tests -q`, kod 0). Kanoniczne rozdziały bez zmian. Nie wykonano nowej kompilacji PDF ani testów przeglądarkowych. Raport `data/raport_v16.json`.

**Następny krok:** benchmark bez narzutu `tracemalloc` dla większych zestawów, analiza ryzyka jednoczesnych żądań i limitów CPU/pamięci; następnie kompilacja kolejnej pary międzydziedzinowej z kontrolą `xr-hyper`. Etap generatora nadal otwarty.

### Iteracja v0.17 — 20.11.2026

Po sprawdzeniu dziennika v0.16 dodano do `scripts/benchmark_generation.py` przełącznik `--no-memory-tracing` oraz parametr `--sizes`, aby wykonywać większe pomiary bez kosztownego `tracemalloc`. Zachowano wcześniejszy tryb śledzenia pamięci; przy wyłączeniu pomiaru pamięci raport zawiera jawne `null`, nie pozorne zero. Dodano regresję `test_without_memory_tracing`. Wykonano **dwa przebiegi** dla każdego z rozmiarów 1, 5, 15 i 30 modułów; mediany łącznego czasu generowania i ZIP: **0.0812 s, 0.26215 s, 0.73065 s, 0.86145 s**. Wyniki dotyczą wyłącznie procesu lokalnego, bez HTTP, równoległości i kompilacji TeX. **80/80 testów Python zaliczonych**. Rozdziały kanoniczne niezmienione. Dane: `data/benchmark_v17.json`, raport: `data/raport_v17.json`.

**Następny krok:** pomiar równoczesnych żądań API i ograniczenie kosztu CPU/pamięci, a także kompilacja kolejnej pary międzydziedzinowej z `xr-hyper`. Etap generatora nadal otwarty.

### Iteracja v0.18 — 20.11.2026

Po odczytaniu dziennika v0.17 przeprowadzono pierwszą diagnostykę współbieżnych żądań HTTP do `/api/generate` przez lokalny ASGI `TestClient` (bez rzeczywistego serwera sieciowego). Dodano `scripts/benchmark_http_concurrency.py` z poziomami współbieżności, liczbą żądań, pomiarem czasu i walidacją odpowiedzi, a także dwa testy regresyjne w `tests/test_http_concurrency_benchmark.py`. Dane rzeczywiste: `data/benchmark_http_v18.json`. **82/82 testy Python zaliczone** (`python -W default -m unittest discover -s tests -q`). Test obejmuje tylko generowanie ZIP dla `ALG-09`; nie stanowi testu obciążeniowego produkcyjnego HTTP ani pomiaru limitów pamięci/CPU. Nie modyfikowano źródeł kanonicznych. **Następny krok:** niezależny pomiar procesowy CPU/RSS i ograniczanie kosztu generowania, następnie kompilacja kolejnej pary dziedzin z `xr-hyper`. Etap generatora pozostaje otwarty.

### Iteracja v0.19 — 20.11.2026

Po odczytaniu dziennika v0.18 i globalnego `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` dodano `scripts/benchmark_process_resources.py`: oddzielny proces Pythona na każdy rozmiar zestawu, pomiar czasu ściennego, czasu CPU użytkownika/systemowego i maksymalnego RSS (`resource.getrusage`, Linux). Dodatkowo ustawiono limit czasu oczekiwania na proces potomny; **nie jest to limit pamięci ani CPU w serwerze produkcyjnym**. Dodano dwa testy regresyjne. Pierwsza próba ujawniła brak `sqlite3.Row` w procesie potomnym (test negatywny); po poprawce **84/84 testy Python zaliczone**. Pomiar pojedynczy dla 1/5/15 modułów: czas całego procesu 0.963/0.999/1.542 s, szczytowy RSS 117280/118052/120864 KiB; CPU i pozostałe dane w `data/benchmark_process_v19.json`. Wyniki obejmują narzut importu Pythona i są diagnostyczne, nie służą do ustalania progów bez replikacji. Rozdziały kanoniczne pozostawiono bez zmian. Wprowadzono globalny standard granularności do kryteriów przyszłych audytów. Testów przeglądarkowych i kompilacji PDF nie wykonano. **Następny krok:** powtórzone pomiary zasobów, ocena izolacji i limitów produkcyjnego serwera, kompilacja rzeczywistego zestawu międzydziedzinowego z `xr-hyper`; etap generatora pozostaje otwarty.


### Integracja aplikacji v0.19 z gałęzią GitHub — 20.11.2026

Przed integracją zweryfikowano, że `application/backend/generator.py` w gałęzi `biblioteka-matematyczna-iteracja-6` zawierał powielone definicje i nie miał aktualnych zabezpieczeń / rejestru środowisk. Zaktualizowano generator do wersji v0.19 oraz zsynchronizowano testy (także `test_browser_smoke_contract.py`). W repozytorium zapisano `.github/workflows/mathematical-library-app.yml` z budowaniem indeksu z kanonicznego `chapters/pl` i zestawem testów; **wynik CI nie jest jeszcze potwierdzony**. `main`, `chapters/pl` i równoległe skrypty pozostawiono bez zmian.

W izolowanym katalogu archiwum v0.19 wykonano **84/84** testy (`OK`), następnie przebudowano indeks z jego `rozdzialy/` (352 dokumenty; 15729 obiektów; 5762 etykiety; 4453 odsyłacze; 159 niejednoznacznych, 17 brakujących, 303 powielone nazwy etykiet) i ponowiono testy: **84/84, OK**. Indekser zakończył się kodem 2, sygnalizując niejednoznaczności / braki, które pozostają otwarte. Testy nie są dowodem poprawności wszystkich rozdziałów ani pełnego `xr-hyper` na obecnym GitHubie. Raport: `docs/RAPORT_INTEGRACJI_V019_2026-11-20.md` w Bibliotece i `application/docs/` na GitHubie.

**Następny krok:** odczytać status GitHub Actions, zbudować i przetestować indeks z aktualnego `chapters/pl`, a następnie wykonać testy przeglądarkowe oraz pełne `xr-hyper` między dziedzinami. Zachować standard `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` podczas późniejszych audytów.

### Iteracja CI przeglądarki — 20.11.2026 (następna po integracji v0.19)

Dodano `application/tests/browser_ci_e2e.py` i kroki prawdziwego testu Chromium/Playwright do `.github/workflows/mathematical-library-app.yml`. Po poprawieniu selektora liczby rozdziałów wynik uruchomienia GitHub Actions #44706291102 dla commita `ec22ab95cf1af80025e995b81c032efbfdd56270`: **success**. Przebudowa indeksu kanonicznych `chapters/pl`: 355 rozdziałów; unittest: 85 uruchomionych, 84 zaliczone, 1 pominięty; Chromium otworzył rozdział w czytniku i kartę grafu (16 dziedzin); 0 błędów JavaScript. Raport szczegółowy: `docs/RAPORT_CI_PRZEGLADARKA_2026-11-20.md`. Stare nieudane uruchomienia pozostają w historycznej liście GitHub Actions. Nie wykonywano pełnego audytu matematycznego ani wszystkich ścieżek UI (dymki, drafty, eksporty); źródła rozdziałów i `main` bez zmian.

**Następny krok:** rozszerzyć realne testy przeglądarkowe o podgląd cytowanego fragmentu oraz workflow draft/save/close, zachowując osobną ścieżkę audytu nierozwiązanych i niejednoznacznych odsyłaczy.


### Iteracja CI workflow projektów — 20.11.2026

Po odczycie roadmapy i standardu granularności poprawiono przenośność `tests/browser_workspace_e2e.py`: proces serwera uruchamiany przez bieżący interpreter (`sys.executable`), a Chromium przez instalację Playwright zamiast stałej ścieżki `/usr/bin/chromium`. Do GitHub Actions dodano obowiązkowy test `Test browser draft save and tab-close cleanup`, obejmujący utworzenie szkicu, jawne zapisanie projektu, zamknięcie karty, usunięcie szkicu i zachowanie zapisanego ZIP. Zmiany ograniczono do aplikacji i workflow, bez zmian kanonicznych rozdziałów.

Weryfikacja: **GitHub Actions #44707579176: success** (commit `61d12f0`; 84 zaliczone testy Python, 1 pominięty; Chromium Explorer/czytnik/graf i zapis projektu + nawigacja poza stronę). Pierwsze próby testu były czerwone: Playwright `page.close()` nie potwierdził wysłania `pagehide`/`beforeunload`; test końcowy świadomie sprawdza nawigację `about:blank`, **nie** zachowanie przy kliknięciu X. Poprawiono konflikt stałego portu przez port przydzielany przez system. Produkcyjny frontend ma dodatkowy awaryjny nasłuch `beforeunload`, ale X-close wymaga osobnej weryfikacji w realnej przeglądarce.. Kolejna iteracja powinna objąć podgląd cytowanych fragmentów (`\\ref`) i raport rozróżniający jednoznaczne, niejednoznaczne i brakujące odsyłacze; testy przeglądarkowe nie zastępują audytu matematycznego.

### Iteracja: test podglądu cytowanego fragmentu — 20.11.2026

W `application/tests/browser_ci_e2e.py` dodano test prawdziwego hover nad jednoznacznym odsyłaczem `\ref` z aktualnej kanonicznej bazy SQLite, sprawdzenie treści podglądu i otwarcie wskazanego fragmentu. GitHub Actions #44707891398, commit `a9259c8675da574aac102950bf9c9ac22e28bfbf`: **success**, 85 testów Python (`OK (skipped=1)`), Chrome/Playwright: 355 rozdziałów, 16 dziedzin, `ALG-00` → `tw:korzenie`, brak błędów JS. Powiódł się też osobny test draft/save/page-leave. Raport: `docs/RAPORT_PODGLAD_ODSYLACZY_2026-11-20.md`. Źródła matematyczne i `main` niezmienione.

Następny krok: testować niejednoznaczne i brakujące etykiety oraz wyścigi przy szybkich hoverach. Test `pagehide` nadal nie gwarantuje czyszczenia szkiców przy każdym X-close. Brakujące odsyłacze i audyt matematyczny pozostają otwarte.

### Iteracja: niejednoznaczne/brakujące etykiety oraz wyścigi dymków — 20.11.2026

Po odczytaniu poprzedniego dziennika rozszerzono `application/frontend/app.js` o diagnostykę brakującego celu w podglądzie i ochronę przed spóźnionymi odpowiedziami HTTP / opóźnionymi zdarzeniami `mouseleave` z nieaktualnej kotwicy. Nie dokonuje się automatycznej identyfikacji właściciela etykiety. W `application/tests/browser_ci_e2e.py` dodano rzeczywistą ścieżkę niejednoznaczną, brakujący cel oraz opóźnioną odpowiedź. Pierwsze przebiegi CI wykryły wyścig między nawigacją przyciskiem `Otwórz w czytniku` i kolejnym podglądem; poprawiono identyfikację aktywnej kotwicy i synchronizację testu z ukończoną nawigacją, zamiast pomijać walidację.

**Zewnętrzna weryfikacja:** GitHub Actions [#44711138252](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44711138252), commit `e6ac161577e69f16b48e53b72eece38d0d78a092`: **success**. Uruchomiono 85 testów Python (84 zaliczone, 1 pominięty), oba testy Chromium przeszły. W bazie 355 rozdziałów, 16 dziedzin. Przykłady: `tw:korzenie` z `ALG-00` (jednoznaczna); `ch:algebra-homologiczna` z kandydatami `DG-06` i `TOP-03` (niejednoznaczna); `I-ch:clt` (brakująca). Test sztucznie opóźnionej odpowiedzi potwierdził, że nie zastąpi nowszego komunikatu. Raport: `docs/RAPORT_ODSYLACZE_E2E_2026-11-20.md` w Bibliotece i GitHubie. Pliki matematyczne oraz `main` bez zmian.

**Następny krok:** audyt źródeł konfliktów i brakujących etykiet z mapą pochodzenia bez automatycznego usuwania etykiet i różnorodnych dowodów. Osobno nadal wymagane pełne kompilacje międzydziedzinowe `xr-hyper` i test faktycznego X-close; zielony `pagehide` nie daje gwarancji usuwania szkicu przy każdym zamknięciu karty.

### Iteracja: pełny audyt odsyłaczy i mapa pochodzenia — 20.11.2026

Po odczytaniu aktualnego dziennika utworzono read-only `scripts/audit_reference_provenance.py` oraz `tests/test_audit_reference_provenance.py` (2 nowe testy). Narzędzie odtwarza wszystkie nierozwiązane cytowania oraz wszystkie wielokrotne nazwy etykiet z ich właścicielami, numerami wierszy, ścieżkami, SHA-256 i kontekstem źródłowym; nie dokonuje żadnego automatycznego scalenia dowodów, przepisania odsyłaczy ani zmiany źródeł. W workflow GitHub Actions po indeksowaniu zapisuje się raporty `reference_provenance_audit.json` i `reference_provenance_audit.md` jako oddzielny artefakt.

**Wynik na kanonicznych 355 rozdziałach GitHuba:** 4228 rozwiązanych odsyłaczy, 166 niejednoznacznych i 91 brakujących **wystąpień** (łącznie 257 nierozwiązanych); 61 różnych niejednoznacznie cytowanych nazw, 49 różnych brakujących nazw, 305 nazw etykiet z wieloma właścicielami (nie wszystkie powodują niejednoznaczność lokalnego cytowania). Przykłady: `tw:ga10-weak` cytowany w `ALG-10` wiersz 240 (brak); `thm:poincare-hopf-16` cytowany w `DG-02` wiersz 238, kandydaci `DG-17` i `TOP-11`. Aktualne liczby nie są tożsame ze starszą migawką 352 modułów.

**Weryfikacja:** GitHub Actions [#44712479054](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44712479054), commit `62fcdd117aa2c10ce2f46dcaf2056561f1b9ef54` — **success**, 87 testów Python (86 zaliczonych, 1 pominięty), oba testy Chromium zaliczone. Kompletny artefakt: [reference-provenance-audit](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44712479054/artifacts/14618175691). Pliki wynikowe w Bibliotece: `aplikacja/data/reference_provenance_audit_355.json`, `aplikacja/docs/reference_provenance_audit_355.md`; podsumowanie `aplikacja/docs/RAPORT_AUDYT_ODSYLACZY_2026-11-20.md`. Zmian w `chapters/pl` i `main` nie było.

**Następny krok:** audyt matematyczny pierwszej priorytetowej partii cytowań, z otwarciem kontekstu źródłowego i wszystkich kandydatów; przygotować uzasadnione propozycje lub pozostawić status nierozstrzygnięty. Po uzgodnieniu rozstrzygnięć skontrolować `xr-hyper` i regresje; zachować bez wyjątku standard `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, pełne dowody i mapę pochodzenia.


### Audyt integralności odsyłaczy — partia 01 (13 wystąpień), 20.11.2026

Po zbudowaniu pełnej mapy pochodzenia przeprowadzono ręczną kontrolę kontekstów pierwszych **13** nierozwiązanych wystąpień na aktualnym `chapters/pl/` (źródła cytowań oraz deklaracje kandydatów). Wynik: **10 uzasadnionych propozycji** wskazania właściciela w obrębie tego samego skryptu (bez wykonywania zmiany źródła), **3 braki nierozstrzygnięte** (`tw:ga10-weak`, `thm:xvii-blowup`, `app:grupy-algebry-macierzowe`), z których żadnego nie wolno automatycznie rekonstruować przez zgadywanie. Analiza uwzględnia m.in. dokładne założenia twierdzeń Poincarégo–Hopfa, van Kampena, o izomorfizmie modułów, definicje torsji i homotopii łańcuchowej. Kompletny protokół: `docs/AUDYT_PARTIA_01_13_ODSYLACZY_2026-11-20.md` (Biblioteka i GitHub). Nie modyfikowano `chapters/pl`, nie scalano skryptów i nie usuwano wersji dowodów.

**Zatwierdzona kolejność długoterminowa:** ukończyć kolejne działy, poczynając od podstaw matematyki i rozwijając gałęzie; **dopiero po skompletowaniu** przeprowadzać scalenia, zachowując sumę treści i wszystkie warianty dowodów. Obecne czynności to odrębna kontrola spójności odsyłaczy w niezależnych skryptach.

**Następny krok:** ręczny przegląd wystąpień 14–26 oraz oddzielna, kontrolowana poprawka wyłącznie zweryfikowanych odsyłaczy wewnątrz skryptów; następnie sprawdzić `xr-hyper`, kompilację oraz regresje. Standard `MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md` nadal obowiązuje.


### Iteracja audytu odsyłaczy, partia 02 (14–26) — 20.11.2026

Po odczycie dziennika i partii 01 zbadano kontekst 13 kolejnych wystąpień (`DG-07`, `DG-08`) z raportu 355 rozdziałów. Wszystkie 13 były niejednoznaczne; dla 12 przygotowano propozycję celu w tym samym skrypcie, a dla `DG-08:26` (`thm:homologia-char-zero`) propozycję warunkową, ponieważ twierdzenie dotyczy współczynników `\Q`, `\R`, `\C`, a nie dowolnej zmiany współczynników. Łącznie przejrzano 26/257 wystąpień; 231 pozostaje. **Nie dokonano zmian w źródłach, etykietach ani dowodach; nie wykonywano testów kompilacji.** Raport: `application/docs/AUDYT_PARTIA_02_14_26_ODSYLACZY_2026-11-20.md` i odpowiadający mu plik w Bibliotece. Zachowano nadrzędną zasadę: najpierw kompletowanie niezależnych działów, a dopiero później scalanie od podstaw matematyki. Następny krok: wystąpienia 27–39, pogłębiona kontrola hipotez wskazanych twierdzeń i test `xr-hyper` przed ewentualnymi poprawkami.


### Globalna reguła kopiowania etykiet — 20.11.2026

Na wyraźne polecenie użytkownika dodano pkt 8 do kanonicznego `/Biblioteka matematyczna/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`: kopiowany materiał **zachowuje oryginalne deklaracje `\\label{...}` i dokładnie powiązane `\\ref`, `\\eqref`, `\\cref` itd.**, wraz z wielokrotnością, niezależnie od zmian redakcyjnych. Konfliktów nazw między skryptami nie wolno rozwiązywać milczącą zmianą etykiet; trzeba zachować pochodzenie, jawnie wybrać cel lub odłożyć to do późniejszej integracji, dopiero po skompletowaniu działów. Lustrzana kopia standardu na GitHubie: `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`.

Dodano `scripts/verify_copied_labels.py`: porównuje multizbiór etykiet oraz pary (komenda odsyłacza, nazwa celu) między wskazanym oryginałem i kopią, wykorzystując parser ignorujący komentarze i środowiska kodu. Odrzuca zmianę etykiety, celu i wielokrotności; nie modyfikuje plików. Regresja `tests/test_verify_copied_labels.py` obejmuje pięć przypadków, **5/5 przeszło lokalnie**. Wywołanie: `python scripts/verify_copied_labels.py ORIGINAL.tex KOPIA.tex --report raport.json`. To kontrola **dokładnej kopii źródła lub wybranego fragmentu**, nie automatyczne porównanie dwóch całych niezależnie rozwijanych skryptów. Integracja z CI przez standardowe `unittest discover`.

Audyt wystąpień 14–26 został już niezależnie zapisany przez równoległą iterację; nie przepisano ani nie scalono jego wniosków. Obie prace nie modyfikowały `chapters/pl/` ani `main`.


### Audyt integralności odsyłaczy — partia 03, wystąpienia 27–39 (20.11.2026)

Na kanonicznych źródłach `chapters/pl/` i indeksie 355 rozdziałów skontrolowano wszystkie 13 kolejnych niejednoznacznych cytowań z `DG-08`: otoczenie użycia oraz deklaracje w `DG-06`, `DG-07`, `TOP-03`, `TOP-04`. Dla 13 przypadków wskazano uzasadnionych kandydatów w tym samym skrypcie (`DG-06` lub `DG-07`), nie zmieniając żadnego `\\label` ani `\\ref`. Dwa odsyłacze do lematu pięciu (`DG-08:1256`, `DG-08:1462`) wymagają jeszcze kontroli pełnych diagramów, a formuła `eq:homologia-char-zero` dotyczy współczynników `\\Q`, `\\R`, `\\C`, nie automatycznie `\\Z/2`. Szczegółowa ocena matematyczna i lokalizacje w `application/docs/AUDYT_PARTIA_03_27_39_ODSYLACZY_2026-11-20.md` oraz w Bibliotece. Postęp: **39/257 sprawdzonych, 218 pozostałych**, nie jest to licznik naprawionych cytowań. Kolejne: 40–52. Obowiązuje nowa zasada zachowania wszystkich etykiet i odsyłaczy oryginału przy kopiowaniu z Biblioteki; scalanie dopiero po skompletowaniu działów.


### Audyt integralności odsyłaczy — partia 04, wystąpienia 40–52 (20.11.2026)

Ręcznie skontrolowano 13 kolejnych niejednoznacznych odsyłaczy w `DG-09` (wyższe grupy homotopii i związek z homologią). Porównano wszystkie cytujące fragmenty z oryginalnymi definicjami, twierdzeniami i przykładami `DG-07` oraz `DG-08` (równoległe wystąpienia w `TOP-04` i `TOP-05`). W 13/13 przypadkach można wskazać odpowiednik w obrębie tego samego skryptu, z zachowaniem nazw etykiet i źródłowych wariantów dowodów. Szczególną uwagę poświęcono kryterium podnoszenia dla `S^n`, `n>=2`, inwariancji homologii singularnej, konstrukcji odwzorowania Hurewicza oraz ograniczeniu przykładu o dwóch okręgach do `r=2`. Tekst audytu: `application/docs/AUDYT_PARTIA_04_40_52_ODSYLACZY_2026-11-20.md` w Bibliotece i na GitHubie.

**Licznik audytu:** 52/257 przejrzanych nierozwiązanych wystąpień, 205 pozostaje. To propozycje rozstrzygnięcia pochodzenia, nie zmiany `\\label`, `\\ref`, nie naprawiony indeks ani scalanie. Nie zmieniano `chapters/pl/`, `main` i dowodów. Obowiązuje globalna reguła zachowania wszystkich etykiet oraz odsyłaczy przy kopiowaniu z Biblioteki. Następny przegląd: wystąpienia 53–65; osobno pogłębić argument przechodzenia od skończonych do dowolnych CW w `DG-09:544` i przygotować kontrolowany, bezstratny rejestr rozstrzygnięć.


### Audyt integralności odsyłaczy — partia 05, wystąpienia 53–65 (20.11.2026)

Na podstawie pełnego indeksu 355 rozdziałów i kanonicznych plików `chapters/pl/` zweryfikowano konteksty 13 niejednoznacznych wystąpień w `DG-09` (9) oraz `DG-10` (4), wraz z odpowiadającymi im deklaracjami w `DG-06` i `DG-08`. Wszystkie 13 mają odpowiadający znaczeniowo cel w tym samym skrypcie, ale **nie zmieniono żadnych `\\label`, `\\ref`, `\\eqref` ani źródeł**. Potrzebny dalszy przegląd stosowania wyniku o warstwach komórkowych dla nieskończonych CW (`DG-09:1440`), orientacji we wzorze brzegu (`DG-09:1706,1973`) i znaku w długim ciągu kohomologii form (`DG-10:1426`). Szczegółowy protokół: `application/docs/AUDYT_PARTIA_05_53_65_ODSYLACZY_2026-11-20.md` oraz odpowiednik w Bibliotece. Stan po pięciu partiach: **65/257** wystąpień przejrzanych, **192** oczekujące; nie jest to licznik faktycznych napraw. W następnej partii przejrzeć wystąpienia 66–78, zgodnie z regułą zachowania oryginalnych etykiet przy kopiowaniu, bez scalania działów matematyki do czasu ich skompletowania.


### Audyt integralności odsyłaczy — partia 06, wystąpienia 66–78 (20.11.2026)

Zweryfikowano ręcznie 13 niejednoznacznych wystąpień, 12 w `DG-10` oraz jedno w `DG-11`, porównując oryginalne cytowania z odpowiadającymi definicjami, przykładami i twierdzeniami `DG-06`, `DG-07`, `DG-08`, `DG-09` i `DG-10`. Wszystkie mają uzasadniony odpowiednik w tym samym skrypcie, bez ingerencji w `\\label`, `\\ref`, `\\eqref`, źródła `chapters/pl/` lub gałąź `main`. Wymagają osobnej głębokiej kontroli: argument dla kompleksów gładkich łańcuchów (`DG-10:1734,1859`), rozszerzenie porównania homologii na lokalnie skończone triangulacje (`DG-10:2127`) oraz dokładne hipotezy twierdzenia Hurewicza i triangulacji gładkich rozmaitości (`DG-10:2283`). Pełny protokół w `application/docs/AUDYT_PARTIA_06_66_78_ODSYLACZY_2026-11-20.md` (GitHub i Biblioteka). Łączny postęp **78/257** przejrzanych wystąpień, **179 pozostałych**; to audyt, nie naprawiony indeks ani scalanie. Następna partia 79–91. Niezmienna globalna reguła: zachowywać wszystkie oryginalne etykiety i odsyłacze w kopiowanym materiale; merge działów dopiero po ich skompletowaniu.


### Audyt integralności odsyłaczy — partia 07, wystąpienia 79–91 (20.11.2026)

Skontrolowano 13 odsyłaczy z `DG-11` (7), `DG-12` (2) i `DG-14` (4) na kanonicznym indeksie 355 rozdziałów. **7 to wystąpienia niejednoznaczne** (wybór właściciela `DG-10` zamiast równoległego `TOP-09` jest uzasadniony tekstem), **6 to odsyłacze bez jakiegokolwiek indeksowanego właściciela**: `prz:thur-dop-nil-kontakt`, `sec:rownanie-diraca`, `subsec:dirac-koneksja`, `sec:algebra-liego`, `cor:bochner-vanishing`, `cor:hodge-de-rham`. Tych braków nie wolno naprawiać wymyśloną etykietą ani udawać, że wskazane twierdzenia już zostały opracowane. Osobnego pogłębienia wymagają twierdzenia Hodge’a i Bochnera, koneksja spinorowa i operator Diraca, a także założenia Stokesa/Gaussa dla nieorientowalnych lub niezwartych rozmaitości. Pełny protokół: `application/docs/AUDYT_PARTIA_07_79_91_ODSYLACZY_2026-11-20.md` (GitHub i Biblioteka). Stan audytu: **91/257 przejrzanych, 166 pozostałych**; nie oznacza to fizycznego usunięcia błędów z indeksu. Bez zmian `chapters/pl/`, `main`, oryginalnych `\\label`, `\\ref`, `\\eqref`, dowodów czy scalania skryptów. Kolejna partia: 92–104.


### Audyt integralności odsyłaczy — partia 08, wystąpienia 92–104 (20.11.2026)

Ręcznie skontrolowano 13 kolejnych pozycji z pełnego raportu 355 rozdziałów w kanonicznych źródłach `DG-14`, `DG-15`, `DG-16` i `DG-17`. Wynik: **7 niejednoznacznych cytowań**, z uzasadnionymi lokalnymi właścicielami `DG-06`, `DG-08`, `DG-10`, `DG-17`, oraz **6 brakujących odsyłaczy**: `ch:chern-weil`, `prop:euler-identification-26`, `lem:angular-form-26`, `thm:CGB-boundary-26` (dwa wystąpienia), `ch:grafy-wezly-cztery`. Pierwsze cztery różne braki stanowią istotny blok niezrealizowanych zależności dowodu twierdzenia Cherna–Gaussa–Bonneta i jego wersji z brzegiem, nie można ich rozwiązać atrapami etykiet. Co więcej, w `DG-16:1200` twierdzenie z brzegiem jest niewłaściwym cytatem dla `TS^2`: argument dotyczy zamkniętej sfery, a `DG-14:4603` zawiera odpowiadające mu twierdzenie `thm:chern-gauss-bonnet`. Szczegółowy raport: `application/docs/AUDYT_PARTIA_08_92_104_ODSYLACZY_2026-11-20.md` i jego kopia w Bibliotece. Stan: **104/257 przejrzanych, 153 pozostałe**, ale liczba naprawionych odsyłaczy nie uległa zmianie, ponieważ nie zmieniano `chapters/pl/`, oryginalnych `\\label`, `\\ref`, `\\eqref`, ani nie scalano materiału. Następna partia: 105–117.


### Audyt integralności odsyłaczy — partia 09, wystąpienia 105–117 (20.11.2026)

Przeprowadzono ręczny audyt semantyczny 13 wystąpień na kanonicznych `chapters/pl/`, w rozdziałach `DG-17` (8), `DG-18` (3), `DG-19` (1), `DG-20` (1): **9 niejednoznacznych** z uzasadnionym właścicielem w tym samym skrypcie oraz **4 brakujące** (`prz:hodge-dwie-sfery-18`, `ch:chern-weil`, `thm:CGB-boundary-26` dwukrotnie). Szczególne ustalenia: w `DG-17:1888,2182` etykieta brzegowego twierdzenia Cherna–Gaussa–Bonneta jest zarówno brakująca, jak i merytorycznie niewłaściwa dla bezbrzegowego `S^2`; w `DG-14:4603` istnieje odpowiadające twierdzenie `thm:chern-gauss-bonnet` (propozycja późniejszej jawnej korekty cytowania, bez zmiany deklaracji źródłowych). W `DG-20:1202` zastosowanie homologicznego kryterium Whiteheada jest uzasadnione wcześniejszym sprawdzeniem `\\pi_1(W)=0` w `DG-20:1167–1172`, przy `n>=6`. Protokół: `application/docs/AUDYT_PARTIA_09_105_117_ODSYLACZY_2026-11-20.md` i Biblioteka ChatGPT. Licznik: **117/257 przejrzanych, 140 pozostałych**, naprawiony indeks: bez zmian. Niezmiennie obowiązuje zakaz cichej zmiany `\\label`, `\\ref`, `\\eqref` i zasada zachowania etykiet przy kopiowaniu. Nie scalano rozdziałów, nie modyfikowano `chapters/pl/` ani `main`. Kolejna partia: 118–130.


### Audyt integralności odsyłaczy — partia 10, wystąpienia 118–130 (20.11.2026)

Wszystkie **13 wystąpień** z `P1-03`, `P1-07`–`P1-10`, `P1-12` i `P1-14` mają w indeksie 355 rozdziałów status `missing`, ale są to **odsyłacze międzytomowe**, nie brakująca treść. Otworzono źródła oraz 10 istniejących rozdziałów celowych tomów II i IV; cytowania `\\ref{IV-ch:...}` i `\\ref{II-ch:...}` odpowiadają oryginalnym deklaracjom `\\label{ch:...}` w docelowym tomie. Prefiksy `IV-` i `II-` są dodawane przez `\\externaldocument[IV-]`/`\\externaldocument[II-]` pakietu `xr-hyper` w `books/pl/probability_volume_i.tex` (analogicznie pozostałe tomy). Nie wolno przemianowywać `\\label` ani usuwać prefiksów z cytowań. Rozwiązanie wymaga klasyfikacji zewnętrznych odsyłaczy w aplikacji oraz pełnej kompilacji tomów z prawdziwymi plikami `.aux`, której w tej iteracji **nie wykonywano**. Raport: `application/docs/AUDYT_PARTIA_10_118_130_ODSYLACZY_2026-11-20.md` (GitHub i Biblioteka). Licznik audytu: **130/257** przejrzanych, **127** pozostałych; źródła i indeks bez zmian. Następnie wystąpienia 131–143 i osobny test `xr-hyper` z kompilacją. Nie wykonywano scalania skryptów ani zmian w `chapters/pl` lub `main`.


### Audyt integralności odsyłaczy — partia 11, wystąpienia 131–143 (20.11.2026)

Przeanalizowano 13 kolejnych przypadków w indeksie 355 rozdziałów: `P2-01`, `P2-04`, `P2-05`, `P2-07`, `P2-09`, `P2-13`, `P3-01`, `P3-05`. Wszystkie 13 mają surowy status `missing`, lecz wszystkie odpowiadają **istniejącym rozdziałom innych tomów**, w sumie 10 różnym celom. Sprawdzono źródłowe `\\ref{I-ch:...}`, `\\ref{II-ch:...}`, `\\ref{III-ch:...}`, `\\ref{IV-ch:...}`, oryginalne deklaracje `\\label{ch:...}` i konfigurację prefiksów `\\externaldocument` w `books/pl/probability_volume_ii.tex` oraz `books/pl/probability_volume_iii.tex`. To w większości błędna klasyfikacja zewnętrznych odsyłaczy w aplikacji, nie brak treści. Nie zmieniano oryginalnych `\\label` lub `\\ref`: prefiks dodaje `xr-hyper` przy imporcie danych z `.aux`. Test rzeczywistej kompilacji z `.aux` i poprawa statusu w aplikacji nadal pozostają do wykonania. Raport: `application/docs/AUDYT_PARTIA_11_131_143_ODSYLACZY_2026-11-20.md` (GitHub i Biblioteka). Stan audytu: **143/257 przejrzanych, 114 oczekujących**; nie jest to liczba naprawionych cytowań. Następny etap: 144–156; bez scalania skryptów, bez zmian `chapters/pl/` i `main`.


### Audyt integralności odsyłaczy — partia 12, wystąpienia 144–156 (20.11.2026)

Ręcznie skontrolowano kolejne **13 wystąpień** na indeksie 355 rozdziałów, obejmujące `P3-06`, `P3-10`, `P3-11`, `P3-15` i `P4-00`. Surowy indeks oznacza wszystkie jako `missing`, lecz dla wszystkich potwierdzono **rzeczywistych właścicieli w innych tomach**, obejmujących 12 różnych oryginalnych etykiet `ch:...` w tomach I, II i IV. Sprawdzono kontekst cytowań, tytuły i deklaracje rozdziałów docelowych oraz pliki główne `books/pl/probability_volume_iii.tex`, `books/pl/probability_volume_iv.tex`: prefiksy `I-`, `II-`, `IV-` wynikają z `xr-hyper` i `\\externaldocument[PREFIX]`, a nie z modyfikacji źródłowych `\\label`. Szczegółowy protokół: `application/docs/AUDYT_PARTIA_12_144_156_ODSYLACZY_2026-11-20.md`, skopiowany do Biblioteki. Osobny test rzeczywistej kompilacji PDF z plikami `.aux` i poprawka klasyfikacji `external_resolved` w aplikacji pozostają zadaniami, nie zostały wykonane w tej partii. **Postęp: 156/257 przejrzanych, 101 pozostałych.** Źródła `chapters/pl/`, deklaracje `\\label` i cytowania `\\ref`, gałąź `main` oraz treść skryptów bez zmian; nie przeprowadzano scalania. Następna partia 157–169.


### Audyt integralności odsyłaczy — partia 13, wystąpienia 157–169 (20.11.2026)

Skontrolowano wszystkie 13 cytowań z `P4-00`, wprowadzenia do tomu IV. Indeks 355 rozdziałów oznacza każde jako `missing`, ale odczytano źródło, **12 różnych istniejących rozdziałów celowych** tomów I, II i III, oraz konfigurację `books/pl/probability_volume_iv.tex`. Wszystkie 13 są poprawnymi semantycznie odsyłaczami międzytomowymi `\\ref{I-ch:...}`, `\\ref{II-ch:...}`, `\\ref{III-ch:...}`, importowanymi przez `xr-hyper`; `I-ch:clt` występuje dwukrotnie. Oryginalne deklaracje w rozdziałach docelowych mają postać `\\label{ch:...}` i **nie wymagają zmiany**. Pełny protokół wraz z mapą 13 cytowań: `application/docs/AUDYT_PARTIA_13_157_169_ODSYLACZY_2026-11-20.md` i odpowiadający plik w Bibliotece. Pozostają osobne zadania: naprawa klasyfikacji `missing` → `external_resolved` w aplikacji oraz **rzeczywista** kompilacja tomów i test plików `.aux` (w tej partii nie wykonywane). Stan audytu: **169/257 przejrzanych, 88 pozostałych**; to nie jest liczba naprawionych odsyłaczy. Bez ingerencji w `chapters/pl/`, `main`, oryginalne `\\label`/`\\ref` ani warianty dowodów; bez scalania. Następne: 170–182.

### Audyt odsyłaczy — partia 14 (170–182), 20.11.2026

Zweryfikowano 13 kolejnych wystąpień `missing` w tomie IV względem 12 oryginalnych deklaracji rozdziałów w tomach I–III. To poprawne znaczeniowo cytowania międzytomowe z prefiksami `xr-hyper`, a nie brakujące rozdziały. Protokół: `application/docs/AUDYT_PARTIA_14_170_182_ODSYLACZY_2026-11-20.md`, wynik JSON: `application/data/PROVENANCE_BATCH_170_182.json`, skrypt kontrolny: `application/tests/verify_batch14.py` (6 kontroli zaliczonych lokalnie). Stan **182/257 przejrzanych, 75 pozostałych**. Bez zmiany `chapters/pl/`, etykiet, odsyłaczy, dowodów i `main`. Kompilacja PDF/`.aux` i poprawka statusu `external_resolved` nadal niewykonane. Następna partia 183–195.


### Ważne sprostowanie zakresu geometrii różniczkowej — 20.11.2026

**Pełny oryginalny skrypt geometrii różniczkowej liczy 36 rozdziałów.** Do aktualnej gałęzi Biblioteki zaimportowano dotąd jedynie **20 rozdziałów**, gdyż pozostałe 16 przechodzi jeszcze audyty. Dlatego wcześniejsze raporty odsyłaczy dotyczące `DG-` opisują wyłącznie **stan obecnego indeksu**. Oznaczenie `missing` dla `ch:chern-weil`, `thm:CGB-boundary-26`, `cor:hodge-de-rham`, `cor:bochner-vanishing`, `sec:rownanie-diraca` czy podobnych **nie jest dowodem**, że odpowiednie deklaracje lub dowody nie występują w pełnej wersji 36-rozdziałowej. W audycie należy stosować status roboczy „niezindeksowany w dostępnych 20 rozdziałach — sprawdzić pozostałe 16”; nie generować z tych braków fikcyjnych etykiet, duplikatów ani nowych sekcji. Po dodaniu kolejnych 16 rozdziałów powtórzyć kontrolę zależności i dopiero wtedy podejmować decyzje o ewentualnych rzeczywistych lukach. Zachować wszystkie oryginalne etykiety i odsyłacze przy kopiowaniu, bez scalania do czasu ukończenia działów.


### Audyt integralności odsyłaczy — partia 15, wystąpienia 183–195 (20.11.2026)

Skontrolowano **13 wystąpień**: **7 międzytomowych** odsyłaczy `P4-17`, `P4-23`, `P4-24`, `P4-30`, których istniejące cele w tomach I–III są importowane przez `xr-hyper`, i **6 kolizji etykiet** w `TOP-04`/`TOP-05`. W obrębie skryptu topologii algebraicznej właściwymi właścicielami są `TOP-03` (`ch:algebra-homologiczna`, `def:homotopia-lancuchowa`) oraz `TOP-01` (`def:topologia-ilorazowa`); odpowiedniki w `DG-06` i `DG-01` pozostają niezależnymi źródłami, a oryginalne nazwy nie są przemianowywane. Sprawdzono zgodność definicji i zastosowań oraz kontekst źródłowy. Pełny protokół: `application/docs/AUDYT_PARTIA_15_183_195_ODSYLACZY_2026-11-20.md`, kopia w Bibliotece. Stan: **195/257 sprawdzonych, 62 pozostałe**. Nie modyfikowano `chapters/pl/`, `main` ani oryginalnych `\\label`, `\\ref` i `\\eqref`. Przypomnienie: skrypt geometrii różniczkowej obejmuje **36 rozdziałów**, choć w repozytorium jest na razie pierwszych 20. Następna partia 196–208; w przyszłości dodać interpretację `external_resolved` i kontekst własności skryptu bez utraty oryginalnych etykiet, oraz rzeczywisty test kompilacji `.aux`.


### Audyt integralności odsyłaczy — partia 16, wystąpienia 196–208 (20.11.2026)

W kanonicznym `TOP-05` sprawdzono 13 niejednoznacznych cytowań o po dwóch właścicieli. Wszystkie 13 można jednoznacznie powiązać z pierwotnym skryptem topologii algebraicznej: `TOP-03` (homologia charakterystyki zero, homotopia łańcuchowa, długi ciąg, lemat pięciu) oraz `TOP-04` (kompleks symplicjalny, Δ-kompleks, CW, dołączanie komórki, brzeg sympleksu). Równoległe, niezmienione etykiety w `DG-06` i `DG-07` nie są właściwym właścicielem cytowań `TOP-05`. Pełny raport `application/docs/AUDYT_PARTIA_16_196_208_ODSYLACZY_2026-11-20.md` także w Bibliotece. Osobną kontrolą matematyczną trzeba objąć argument ciągłości retrakcji wokół `TOP-05:962`. **208/257** wystąpień przejrzanych, **49 pozostałych**. To nie oznacza zmiany indeksu ani naprawienia etykiet. Zasada zachowywania wszystkich oryginalnych `\\label`, `\\ref`, `\\eqref`; bez zmian `chapters/pl/`, `main` i bez scalania. Cała geometria różniczkowa to 36 rozdziałów, a tylko 20 dotychczas zaimportowano. Kolejne wystąpienia: 209–221.


### Audyt integralności odsyłaczy — partia 17, wystąpienia 209–221 (20.11.2026)

Ręcznie sprawdzono 13 niejednoznacznych cytowań z `TOP-05` (6) i `TOP-06` (7) względem źródeł i dwóch właścicieli etykiet w `TOP` i `DG`. **Wszystkie 13 mają właściwego właściciela w skrypcie topologii algebraicznej**: `TOP-03`, `TOP-04` lub `TOP-05`. Weryfikacja obejmuje przykłady CW sfery, torusa i `RP²`, twierdzenia o homologii i Eulerze, grupie podstawowej oraz kryterium podnoszenia. Dodatkowa uwaga matematyczna: `TOP-05:1579` zapisuje rangi całkowite homologii, podczas gdy cytowane twierdzenie `TOP-03:1633` dotyczy przestrzeni nad ciałem — należy przy następnym audycie jawnie wskazać przejście do `Q`. `TOP-06:690` używa kryterium podnoszenia poprawnie przy `n≥2`. Pełny protokół: `application/docs/AUDYT_PARTIA_17_209_221_ODSYLACZY_2026-11-20.md` (GitHub i Biblioteka). **221/257 sprawdzonych wystąpień, 36 pozostałych**. Żadne etykiety ani źródła nie zostały zmienione; nie wykonywano scalania. Pełna geometria różniczkowa ma 36 rozdziałów, w repozytorium zaimportowano obecnie 20. Następna partia: 222–234.


### Audyt integralności odsyłaczy — partia 18, wystąpienia 222–234 (20.11.2026)

Ręcznie skontrolowano 13 niejednoznacznych cytowań z `TOP-06`, konfrontując fragmenty źródłowe z deklaracjami w `TOP-04`, `TOP-05` i ich odpowiednikami w geometrii różniczkowej. Każde wystąpienie ma dwóch właścicieli etykiety, ale semantycznie właściwy cel w obrębie tego samego skryptu: **12 wystąpień w `TOP-05` i 1 w `TOP-04`**. Zweryfikowano niezmienniczość homotopijną homologii, grupę podstawową i homologię bukietu okręgów, homologię sfer, stopień odwzorowania, wzór różniczki komórkowej oraz homologię `RP²`. W `TOP-06:1216` wersja dla skończonych CW jest cytowana wraz z dodatkowym rozszerzeniem na nieskończone CW; wymaga szczegółowego audytu przejście do skończonych podkompleksów. Pełny protokół: `application/docs/AUDYT_PARTIA_18_222_234_ODSYLACZY_2026-11-20.md` na GitHubie i w Bibliotece. Licznik: **234/257 przejrzanych, 23 pozostałe**; bez fizycznej zmiany statusów w indeksie. Wszystkie oryginalne `\\label`, `\\ref`, `\\eqref` i kanoniczne pliki `chapters/pl/` pozostają bez zmian; bez scalania i bez ingerencji w `main`. Pełny skrypt geometrii różniczkowej liczy 36 rozdziałów, a obecnie zaimportowano 20. Następna partia: 235–247.


### Audyt integralności odsyłaczy — partia 19, wystąpienia 235–247 (20.11.2026)

Ręcznie skontrolowano **13 kolizji** w `TOP-09` względem istniejących etykiet w topologii algebraicznej i geometrii różniczkowej. We wszystkich 13 przypadkach kontekst jednoznacznie wybiera właściciela w skrypcie `TOP`: **7 cytowań do `TOP-05`, 3 do `TOP-03` i 3 do `TOP-06`**. Dotyczy to długiego ciągu kohomologii, kohomologii de Rhama i jej porównania z kohomologią singularną, homologii torusa, lematu małych łańcuchów, zmiany współczynników i twierdzeń Hurewicza. W późniejszym audycie matematycznym wymagają szczególnej kontroli przejście od skończonych do lokalnie skończonych triangulacji (`TOP-09:1860`) oraz zastosowanie pryzmatu i małych łańcuchów do gładkich sympleksów (`TOP-09:1502,1610`). Pełny protokół: `application/docs/AUDYT_PARTIA_19_235_247_ODSYLACZY_2026-11-20.md` oraz kopia w Bibliotece. **247/257 wystąpień przejrzanych, 10 pozostałych**. Nie wprowadzono zmian do `chapters/pl/`, `main`, oryginalnych `\\label`, `\\ref`, `\\eqref`, nie scalano skryptów ani nie naprawiano jeszcze indeksu aplikacji. Pełna geometria różniczkowa liczy 36 rozdziałów, a dotąd 20 zostało zaimportowanych. Ostatnia partia statycznego audytu: **248–257**.


### Zakończenie audytu statycznych 257 wystąpień — partia 20, pozycje 248–257 (20.11.2026)

Ostatnie **10 wystąpień** (`TOP-09`: 3, `TOP-11`: 6, `TOP-21`: 1) mają w indeksie status `ambiguous`, a w źródłowym kontekście wskazują na pierwotne etykiety skryptu `TOP`, nie na odpowiadające im kolizje w `DG`. Właściciele: `TOP-03` (algebra homologiczna), `TOP-04` (grupa podstawowa torusa), `TOP-05` (homologia, lokalna homologia), `TOP-06` (homotopia `RP²`), `TOP-09` (formy de Rhama), `TOP-11` (twierdzenie Poincarégo–Hopfa). Kontrola warunków: `prop:lokalna-homologia` podaje wynik dla rozmaitości **bez brzegu**; `TOP-21` rozważa osobno rozszerzenie twierdzenia Poincarégo–Hopfa na brzeg i odsyła do `TOP-11`. Raport szczegółowy i całościowa rekapitulacja: `application/docs/AUDYT_PARTIA_20_248_257_I_PODSUMOWANIE_2026-11-20.md` i kopia w Bibliotece.

**Cały pierwotny audyt pochodzenia zakończony: 257/257 wystąpień sprawdzonych** w 20 partiach, 0 nieprzejrzanych w tej statycznej migawce 355 rozdziałów. Wejściowy indeks miał **166 ambiguous + 91 missing**, a poza listą audytowaną **4228 resolved**; stan indeksu NIE został jeszcze naprawiony. Wśród pozornych braków występują prefiksy międzytomowe importowane przez `xr-hyper`, a wśród kolizji właściciele rozdziałów należących do odrębnych skryptów. Pełny skrypt geometrii różniczkowej ma **36 rozdziałów**, lecz jedynie 20 jest obecnie zaimportowanych; brak w migawce nie przesądza o braku materiału w oryginale.

**Kolejny etap:** wdrożenie rozwiązywania etykiet w kontekście skryptu, `external_resolved` i ochrony wszystkich źródłowych deklaracji; odtworzenie audytu w testach regresyjnych; rzeczywista kompilacja czterech tomów z `.aux` oraz `xr-hyper`, a po imporcie dalszych rozdziałów ponowne zbudowanie indeksu. Nadal bez zmian `chapters/pl/`, oryginalnych `\\label`, `\\ref`, `\\eqref`, bez scalania i bez zmian w `main`.

### Implementacja rejestru etykiet i aliasów (20.11.2026)

Po zamknięciu 20 partii audytu 257/257 wystąpień **wdrożono pierwszy etap naprawy indeksowania i interfejsu**, bez ingerencji w kanoniczne źródła. Dodano `backend/label_registry.py` oraz w schemacie SQLite v3 tabelę `label_occurrences`: identyfikator `rozdział::oryginalna-etykieta` jednoznacznie zachowuje każde wystąpienie. Rejestr rozwiązuje cytowania najpierw lokalnie i w ramach skryptu, a dla tomów `P1`–`P4` interpretuje prefiksy `I-`, `II-`, `III-`, `IV-` zgodnie z `xr-hyper` (status `external_resolved`). Dopuszcza też świadomie zatwierdzone aliasy konfiguracji `label_aliases` (status `alias_resolved`); nazwy i dowody nie są automatycznie scalane, pole `concept_id` pozostaje nieprzypisane bez audytu równoważności.

Backend `/api/labels/{label}?source_document=...` i frontend czytnika przekazują kontekst źródłowy do podglądu i nawigacji; w razie nierozstrzygniętych konfliktów zachowany jest wybór celu. Zaktualizowano audyt pochodzenia, graf zależności i statystyki API, dodano testy parsera, aliasów i nawigacji. Instrukcja: `application/docs/REJESTR_ETYKIET_I_ALIASOW_2026-11-20.md`. Pełny skrypt geometrii różniczkowej ma 36 rozdziałów, obecnie w repozytorium jest 20; po imporcie reszty konieczna ponowna przebudowa indeksu i audyt. Pozostałe osobne zadania: pełny test kompilacji LaTeX z rzeczywistym `.aux`, reguły ścisłej deklaracji zależności między skryptami, manualne łączenie równoważnych twierdzeń na poziomie `concept_id` i przyszłe scalanie całej niepowtarzalnej treści.

**Zachowano:** `chapters/pl/`, źródłowe `\\label`, `\\ref`, `\\eqref`, `main`; bez deduplikacji tekstu, bez fizycznego przepisywania etykiet.

### Audyt 19 odsyłaczy po wdrożeniu rejestru + kompilacja prawdopodobieństwa (20.11.2026)

Zweryfikowano wszystkie **19/19** nierozstrzygniętych wystąpień ze świeżego artefaktu CI 44743646693 (355 rozdziałów; w indeksie: 72 `external_resolved`, 0 `ambiguous`, 19 `missing`). Szczegółowy raport: `application/docs/AUDYT_19_PO_REJESTRZE_2026-11-20.md`; kopia raportu i tabela JSON znajdują się w Bibliotece. **2 fałszywe braki w ALG-10**: oryginalne etykiety są w źródłach `shared/pl/slabe_twierdzenie_lefschetza.tex` i `shared/pl/rozdmuchanie_punktu_kohomologia.tex` dołączonych przez `\\input`, lecz statyczny parser nie indeksuje plików shared. **12** wpisów wymaga źródeł poza aktualnie zaimportowanymi rozdziałami, **1** możliwej lokalnej korekty odsyłacza, **1** weryfikacji zależności między skryptami, **3** matematycznej korekty celu (zamknięta S² cytuje `thm:CGB-boundary-26`, a właściwszy jest `DG-14:4604` `thm:chern-gauss-bonnet`). Nie przypisano nieznanych właścicieli na podstawie domysłów: pełna DG ma 36 rozdziałów, obecnie 20 zaimportowanych. Audyt nie oznacza naprawy 19 pozycji w indeksie.

Utworzono odrębny workflow `.github/workflows/probability-xr-hyper.yml` oraz walidator `application/scripts/verify_probability_aux.py`: rzeczywista kompilacja 4 tomów, pierwsze pliki `.aux`, druga kompilacja z `xr-hyper`, walidacja prefiksowanych cytowań, logi i artefakty. Pierwsza próba ujawniła brak pakietu `lmodern` w środowisku CI; zależność została dodana. Każdą kolejną próbę dokumentować osobno, bez fałszywego oznaczania testu jako zaliczonego przed rzeczywistą weryfikacją. Kanoniczne `chapters/pl/`, `\\label`, `\\ref`, `\\eqref`, `main` bez zmian; nie scalać.

### Potwierdzenie kompilacji czterech tomów i xr-hyper — SUCCESS (20.11.2026)

Po dopisaniu zależności `lmodern` pełny workflow kompilacji `probability-xr-hyper.yml` przeszedł pomyślnie: [GitHub Actions 44746470218](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44746470218). Faktycznie zbudowano wszystkie **cztery tomy**, ich pliki PDF i AUX, ponownie skompilowano tomy z importami `xr-hyper`, a walidator `application/scripts/verify_probability_aux.py` zweryfikował **72/72 odsyłacze międzytomowe**, zero błędów: tom I 13, II 10, III 10, IV 39. Liczba oryginalnych etykiet AUX: 32, 46, 257, 357. Artefakt CI `probability-xr-hyper-logs-aux` ID 14634000776 zawiera logi, AUX i JSON. Raport `application/docs/WERYFIKACJA_XR_HYPER_4_TOMY_2026-11-20.md` opublikowany także w Bibliotece ChatGPT. Nie oznacza to automatycznie rozwiązania 19 nierozstrzygniętych odsyłaczy spoza czterech tomów ani całościowego audytu matematycznego. Źródła kanoniczne i `main` bez zmian.

### Rozwiązanie odsyłaczy do plików `shared/pl` i gotowość na import DG 21–36 (20.11.2026)

Wdrożono statyczny skaner `backend/included_labels.py` do odczytywania źródłowych etykiet z literalnych `\\input`, z kontrolą lokalizacji, głębokości i cykli; schemat SQLite v4 rejestruje `included_label_origins` bez dopisywania fikcyjnych natywnych `\\label`. Rozwiązano **2** wcześniej brakujące odsyłacze `ALG-10`: `tw:ga10-weak` oraz `thm:xvii-blowup`, których deklaracje istnieją w `shared/pl`. API pokazuje rzeczywistą ścieżkę i linię pochodzenia. W migawce 355 rozdziałów jest **17** nadal nierozstrzygniętych referencji, **0** niejednoznacznych i **72** międzytomowe `external_resolved`. Skrypt audytu usuwa `included_resolved` z listy problemów.

Pełny skrypt geometrii różniczkowej ma **36 rozdziałów**, ale obecnie zaimportowano tylko **20**. Dodano `scripts/dg_import_coverage.py` i krok CI, który zapisuje liczbę importów oraz brakujące odsyłacze do artefaktu; po imporcie rozdziałów 21–36 wymagany ponowny audyt. Trzy cytowania do `thm:CGB-boundary-26` w kontekście sfery bez brzegu wymagają osobnej korekty matematycznej. Dokumentacja: `application/docs/WDROZENIE_INPUT_SHARED_I_COVERAGE_DG_2026-11-20.md`, skopiowana także do Biblioteki. Parser pozostaje statyczny, nie rozwija warunków TeX-a. Zasada nienaruszalności oryginalnych `\\label`, `\\ref`, `\\eqref` i treści `chapters/pl/`; bez zmian w `main`, bez scalania.

### Audyt szczegółowy AT — partia 1, rozdziały 01–02 (20.11.2026)

Zgodnie z nową zasadą wykonujemy **po dwa rozdziały na iterację**, o szczegółowości dowodów, przykładów i rysunków wzorowanej na pierwszym rozdziale geometrii różniczkowej. Etap oznacza faktyczne poprawki źródeł i retesty, nie tylko raport.

W topologii algebraicznej zweryfikowano i poprawiono kanoniczne `chapters/pl/algebraic_topology/01-*.tex` oraz `02-*.tex`. Uzupełniono m.in. dowody homeomorfizmów ilorazowych, kontrprzykład spójności bez łukowej spójności, zawieszenie sfery, `RP^1` i `CP^1`, założenia przy płaskości modułów, dokładność i rozszczepienie ciągów oraz konkretne rachunki `Tor` i `Ext`. Dodano trzy samodzielne rysunki TikZ i zrewidowano je również po kompilacji. Zachowano wszystkie wcześniejsze etykiety, oryginalne dowody i przykłady; bez zmian `main` i bez scalania innych skryptów.

**Retesty:** [aplikacja #44756027445](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44756027445) — SUCCESS (121 testów, 1 pominięty, Chromium zaliczone); [LaTeX #44756027439](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44756027439) — SUCCESS (2 przebiegi, 13 stron, brak niezdefiniowanych odsyłaczy i przepełnionych wierszy). Szczegółowy protokół: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_01_02_2026-11-20.md`. Rejestr: `application/data/AUDYT_ROZDZIALOW.csv` — AT-01 i AT-02 mają status `zaakceptowany`.

**Następna partia AT:** rozdziały **03–04** (algebra homologiczna; homotopia, nakrycia i modele komórkowe), najpierw audyt poprzednio dodanych elementów w razie stwierdzenia regresji, potem szczegółowy audyt obu rozdziałów. Cała topologia algebraiczna nie jest jeszcze oznaczona jako audytowana.


### Audyt szczegółowy AT — partia 2, rozdziały 03–04 (20.11.2026)

Wykonano szczegółowy audyt dwóch kolejnych rozdziałów topologii algebraicznej, według standardu DG-01; poprawiono bezpośrednio kanoniczne pliki `03-algebra-homologiczna-moduly-kompleksy-i-ko-homologie.tex` oraz `04-homotopia-nakrycia-i-komorkowe-modele-przestrzeni.tex`. Nie tworzono nowej gałęzi i nie zmieniano `main`.

**AT-03:** skorygowano niepoprawną nad pierścieniami nieprzemiennymi kolejność współczynników w dowodzie kasowania pary wolnych lewych modułów: `x'=x-a(x)u^{-1}e`; dodano kontrprzykład nad `M_2(Z/2Z)`, jawnie podano przemienność pierścienia w konstrukcji kompleksu dualnego `Hom_R(-,G)`, dowiedziono zamkniętości torsji na działania grupowe, uzupełniono obliczenia przejścia modulo 2 z odwzorowaniem łączącym i nowym diagramem. Ujednolicono terminologię iloczynu tensorowego.

**AT-04:** rozwinięto lokalny dowód, że `z→z^m` jest `m`-krotnym nakryciem, oraz nowy przykład niemożności globalnego przekroju dla `m≥2` z użyciem `(q_m)_*(k)=mk`. Dodano rysunek, poprawiono opis postaci słowa zredukowanego w iloczynie wolnym (dopuszczalne słowa jednoelementowe). Zachowano wszystkie istniejące `\\label`, `\\ref` i warianty argumentacji.

**Wynik:** [testy aplikacji/Chromium #44759080700](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44759080700) — SUCCESS, **130** testów Python (1 pominięty), indeks bez regresji; [kompilacja #44759080408](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44759080408) — SUCCESS, **44 strony**, dwukrotny `pdflatex` z AT-01/02 jako kontekstem odsyłaczy, bez niezdefiniowanych odsyłaczy i `Overfull \\hbox`. Sprawdzono wizualnie wszystkie 9 rysunków AT-03/04. Nowe testy: `application/tests/test_topology_chapters_03_04.py`; niezależna bramka PDF: `.github/workflows/algebraic-topology-audit-ch03-04.yml`. Szczegóły: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_03_04_2026-11-20.md`.

Rejestr `application/data/AUDYT_ROZDZIALOW.csv`: **AT-03 i AT-04 zaakceptowane**, łącznie AT-01–AT-04. W aplikacji nadal 14 nierozwiązanych cytowań z niekompletnego importu DG; nie naprawiano ich przez fikcyjne aliasy.

**Następna partia:** **AT-05 i AT-06**, odpowiednio homologia przestrzeni oraz wyższe grupy homotopii, ich związek z homologią. Powtórzyć cykl: szczegółowy audyt, poprawki matematyczne/redakcyjne, przegląd ilustracji, testy i commit.


### Audyt szczegółowy AT — partia 3, rozdziały 05–06 (20.11.2026)

Zakończono pełną iterację kontrolną dokładnie dwóch rozdziałów topologii algebraicznej, zgodną ze standardem szczegółowości DG-01. Poprawki zostały zapisane w kanonicznych źródłach `chapters/pl/algebraic_topology/05-homologia-przestrzeni.tex` i `06-wyzsze-grupy-homotopii-i-zwiazek-z-homologia.tex`. Nie zmieniono żadnej historycznej deklaracji `\label` ani gałęzi `main`.

**AT-05:** dodano pełne wyjaśnienie działania odwzorowania łączącego Mayera–Vietorisa na fundamentalnej klasie `S²`; obliczono homologię butelki Kleina z `∂₂(1)=2b`, `H₁≅Z⊕Z/2Z`, `H₂=0` oraz zmianę po redukcji modulo `2`. Dodano rysunek kwadratu fundamentalnego, poprawiono terminologię iloczynu tensorowego.

**AT-06:** dodano rachunek abelianizacji `π₁` butelki Kleina; skonstruowano CW z `S²` i dwiema `3`-komórkami o stopniach `2,3`, dla którego `∂₃(a,b)=2a+3b`, `π₂=0`, `π₃=Z`, a nawet `X≃S³` z kryterium Whiteheada. Dodano diagram i objaśnienie różnicy pomiędzy wyższą homotopią a homologią.

**Walidacja:** [CI aplikacji #44762101029](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44762101029) — SUCCESS, 139 testów Python (1 pominięty) i Chromium; [CI LaTeX #44762171825](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44762171825) — SUCCESS, 76 stron, dwukrotna kompilacja AT-01–06 z pełnymi odsyłaczami, bez `Overfull \hbox`. Zweryfikowano wizualnie wszystkie 9 rysunków AT-05–06. Raport: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_05_06_2026-11-20.md`; rejestr: `application/data/AUDYT_ROZDZIALOW.csv` — status `zaakceptowany`.

**Zatwierdzony zakres:** AT-01–06. **Następna partia:** AT-07 (fibracje i długi ciąg homotopii) oraz AT-08 (kohomologia singularna i iloczyn kubkowy). Zachować dokładnie ten sam cykl audytu z poprawkami źródeł i testem PDF.

### Audyt szczegółowy AT — partia 4, rozdziały 07–08 (20.11.2026)

Wykonano dokładnie dwurozdziałowy audyt topologii algebraicznej zgodnie z normą szczegółowości DG-01. Poprawiono bezpośrednio źródła `chapters/pl/algebraic_topology/07-fibracje-i-dlugi-ciag-homotopii.tex` i `08-kohomologia-singularna-i-iloczyn-kubkowy.tex`. Zachowano wszystkie oryginalne `\label`, `\ref`, bez scalania skryptów i zmian `main`.

**AT-07:** rozwinięto monodromię butelki Kleina (`m↦-m`, prezentacja grupy podstawowej), wyprowadzono lokalną funkcję przejścia Hopfa `conj(u)/|u|`, izomorfizm `π₂(S²)→π₁(S¹)` i dowód braku globalnego przekroju. Dodano dwa samodzielne rysunki TikZ oraz poprawiono terminologię.

**AT-08:** poprawiono błędny opis kasowania wyrazów w dowodzie reguły Leibniza dla iloczynu kubkowego; obliczono go jawnie na dwóch trójkątach torusa, wyznaczono torsję `H₂,H₃` dla `RP²×RP²` oraz generator de Rhama na okręgu. Dodano rysunek triangulacji i uzupełniono przykłady.

**Testy i kompilacja:** [aplikacja #44764782403](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44764782403) — SUCCESS, 148 testów Python (1 pominięty), testy Chromium zaliczone; [LaTeX #44764848131](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44764848131) — SUCCESS, PDF **90 stron**, dwa przebiegi bez niezdefiniowanych odsyłaczy i przepełnień. Sprawdzono nowe rysunki na stronach 79, 80 i 85. Testy regresyjne: `application/tests/test_topology_chapters_07_08.py`, workflow `.github/workflows/algebraic-topology-audit-ch07-08.yml`. Pełny protokół: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_07_08_2026-11-20.md`.

Rejestr `application/data/AUDYT_ROZDZIALOW.csv`: **AT-07 i AT-08 zaakceptowane**; łącznie AT-01–08. Dowód twierdzenia de Rhama, zapowiedziany w AT-08, pozostaje merytorycznym zadaniem rozdziału AT-09, nie jest oznaczony jako zweryfikowany w tej iteracji.

**Następna para:** AT-09 oraz AT-10, audyt matematyczno-redakcyjny i kompilacyjny w tym samym standardzie.


### Audyt szczegółowy AT — partia 5, rozdziały 09–10 (20.11.2026)

Wykonano kolejny cykl szczegółowego audytu dokładnie dwóch rozdziałów topologii algebraicznej, według standardu DG-01: bezpośrednie poprawki kanonicznych źródeł, rozbudowane dowody, przykłady, kontrprzykłady, rysunki, kontrola LaTeX oraz testy aplikacji. Pracowano wyłącznie na gałęzi `biblioteka-matematyczna-iteracja-6`; nie zmieniano `main` ani historycznych `\label`.

**AT-09:** rozbudowano kryterium `ω=df` przez znikanie wszystkich okresów zamkniętych pętli; dodano przykład zamkniętej, lecz niedokładnej formy kąta i pełny rachunek Stokesa dla pierścienia `1≤r≤2` z `4π-π=3π` i przeciwnymi orientacjami brzegu. Dodano diagram TikZ; w pierwszej wersji poprawiono nachodzące na siebie oznaczenia normalnej wewnętrznej i „dziura”, po czym skompilowano ponownie. Zachowano dotychczasowy obszerny dowód twierdzenia de Rhama.

**AT-10:** dodano samodzielny lemat ciągłości (ko)homologii Čecha dla granic odwrotnych zwartych wielościanów z surjektywnymi wiązaniami. Uzasadniono model kolczyka hawajskiego jako granicę bukietów i różnicę `check H₁=∏Z`, `check H¹=⊕Z`; obliczono kontrprzykład z domkniętego wykresu `sin(1/x)` dla stopnia zero, odróżniono solenoidy 2-adyczny i 3-adyczny, wyprowadzono niedokładność granicy odwrotnej na układzie `0→2ⁿZ→Z→Z/2ⁿZ→0`. Dodano dwa diagramy TikZ, a słowo „mapa” poza kontekstem map współrzędnych zastąpiono „odwzorowanie”.

**Sprawdzone źródła:** w AT-01–10 nie znaleziono duplikatów deklaracji etykiet; wszystkie 68 odsyłaczy z AT-09 i AT-10 mają zadeklarowane cele w tym zestawie. Brak zewnętrznych plików graficznych i kodowych w audytowanej parze.

**Weryfikacja:** [GitHub Actions aplikacja #44769864949](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44769864949) — SUCCESS (ostatnia wersja źródeł, regresje i Chromium; 158 testów Python, 1 pominięty we wcześniejszym kontrolnym przebiegu); [GitHub Actions PDF #44769864938](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44769864938) — SUCCESS, 120 stron, 2 przebiegi `pdflatex`, brak niezdefiniowanych odsyłaczy i przepełnionych wierszy. Sprawdzono wizualnie wszystkie osiem rysunków AT-09–10, w tym poprawiony pierścień na stronie 103. Raport: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_09_10_2026-11-20.md`. Rejestr `application/data/AUDYT_ROZDZIALOW.csv`: **AT-09 i AT-10 zaakceptowane; łącznie AT-01–10**.

**Następna para:** AT-11 i AT-12, ten sam zakres kontroli matematyczno-redakcyjnej, rysunkowej i technicznej.


### Audyt szczegółowy AT — partia 6, rozdziały 11–12 (20.11.2026)

Zakończono kolejny szczegółowy audyt dwóch kanonicznych rozdziałów topologii algebraicznej według standardu dowodów, przykładów i rysunków DG-01. Zmiany źródłowe są commitowane bezpośrednio na `biblioteka-matematyczna-iteracja-6`; `main` niezmieniony, oryginalne `\label/\ref` zachowane.

**AT-11 — dualność, przecięcia i charakterystyczne klasy:** rozbudowano obliczenie `Q_{CP²}=(1)` z przecięcia dwóch transwersalnych linii rzutowych. Wykazano następnie, że `CP²#(-CP²)` i `S²×S²` mają wszystkie grupy homologii izomorficzne (także `H₂=Z²`), lecz nie są homotopijnie równoważne: forma `diag(1,-1)` jest nieparzysta, a `((0,1),(1,0))` parzysta. Dodano nowy czytelny diagram; poprawiono terminologię iloczynu tensorowego i „iniektywność”.

**AT-12 — ciągi spektralne:** dodano rachunek pierwszej niezerowej różniczki `d³` filtrowanego kompleksu oraz dwa konkretne, dokładnie rozpisane kompleksy o identycznych wszystkich stronach `E^r`, ale z końcowymi grupami `H₁=Z/4` i `H₁=(Z/2)²`. Dodano diagram problemu rozszerzeń i usunięto nieprawdziwe stwierdzenie, że ogólna wersja ciągu Serre'a jest w całości nieudowodniona: przy hipotezach skończeniewymiarowej bazy CW i włókna typu CW jest już dowiedziona w `thm:serre-general-v6`. Poprawiono polską terminologię.

**Kontrola:** 52/52 standardowych odsyłaczy audytowanej pary mają cele w AT-01–12; brak zduplikowanych etykiet i nowych zależności graficznych. [Aplikacja #44772572467](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44772572467) — **SUCCESS**, **167** testów Pythona (1 pominięty) oraz Chromium; [LaTeX #44772572609](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44772572609) — **SUCCESS**, **154 strony**, dwa przebiegi `pdflatex`, brak niezdefiniowanych odsyłaczy i `Overfull \hbox`. Sprawdzono wizualnie wszystkie siedem rysunków AT-11/12, w tym nowe na stronach 142 i 146. Dodatkowe regresje: `application/tests/test_topology_chapters_11_12.py`, workflow `.github/workflows/algebraic-topology-audit-ch11-12.yml`. Protokół: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_11_12_2026-11-20.md`.

Rejestr `application/data/AUDYT_ROZDZIALOW.csv`: **AT-11 i AT-12 zaakceptowane; łącznie AT-01–12**. Pozostała otwarta część uogólnień ciągu spektralnego wymaga osobnego opracowania, nie została fikcyjnie uznana za udowodnioną.

**Następna para:** AT-13 i AT-14, ten sam cykl: szczegółowy audyt, poprawki źródeł, ilustracje, testy i commit.


### Audyt szczegółowy AT — partia 7, rozdziały 13–14 (20.11.2026)

Przeprowadzono kolejną iterację szczegółowego matematyczno-redakcyjnego audytu **dwóch** rozdziałów topologii algebraicznej, w standardzie dowodów i przykładów DG-01. Wprowadzono poprawki bezpośrednio do `chapters/pl/algebraic_topology/13-przestrzenie-klasyfikujace-i-teoria-przeszkod.tex` oraz `14-wieze-postnikowa-iloczyny-whiteheada-i-operacje-steenroda.tex`, zachowując dotychczasowe `\label`, `\ref` i gałąź `main` bez zmian.

**AT-13:** szczegółowy rachunek przestrzeni Moore’a `M(Z/m,n)`: `H^n(M;A)=A[m]`, `H^{n+1}(M;A)=A/mA`, relacja z `Hom` i `Ext` oraz warunek przedłużenia mapy do `K(A,n)`. Dodatkowo realne linie nad `S¹`, `BO(1)=RP∞`, klasyfikacja przez `H¹(-;Z/2)` i wiązka Möbiusa. Nowy diagram różniczki Moore’a. Korekta polskiej terminologii „odwzorowanie”, „ekwiwariantny”.

**AT-14:** nowy przykład przeszkody `h²≠0` w podnoszeniu `CP²→P₂S²` do `P₃S²`, równoległy argument przez iloczyn kubkowy, przedłużenie składania `S²∨S²→S²` niemożliwe z `[ι₂,ι₂]=±2η` i `(x+y)²=2xy≠0`. Dodano diagram Whiteheada. Obliczono `Sq¹(t³)=t⁴` i `Sq²(t³)=t⁵` przy zerowym `(t³)²` w `RP⁵`; przykład relacji `Sq¹Sq¹=0`.

**Potwierdzona walidacja:** wszystkie 9 standardowych odsyłaczy AT-13/14 rozwiązuje się w AT-01–14; brak zduplikowanych etykiet, brak zewnętrznych obrazów i plików kodu. [CI aplikacji #44777464928](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44777464928) — **SUCCESS**, 177 testów Python (1 pominięty) oraz Chromium; [CI LaTeX #44777464845](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44777464845) — **SUCCESS**, 172 strony, 2 przebiegi `pdflatex`, brak niezdefiniowanych odsyłaczy i przepełnień. Naprawiono rzeczywisty błąd TeX (`hook->` jako nieobsługiwany grot TikZ) i ponownie skompilowano całość. Sprawdzono wizualnie pięć rysunków na stronach 158, 160, 163, 165 i 168. Zestaw testów: `application/tests/test_topology_chapters_13_14.py`, workflow `.github/workflows/algebraic-topology-audit-ch13-14.yml`, pełny protokół `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_13_14_2026-11-20.md`.

**Status w rejestrze `application/data/AUDYT_ROZDZIALOW.csv`:** AT-13 `zaakceptowany`, AT-14 `zaakceptowany_z_zastrzezeniem`. Zastrzeżenie dotyczy `thm:steenrod-cartan-v7`: brak pełnych konstrukcyjnych dowodów wzoru Cartana i relacji Adema. Nie przedstawiamy ich jako udowodnionych. W kolejnej iteracji sprawdzić, czy **AT-15** (operacje kohomologiczne, naturalność, iloczyny i relacje) dostarcza wymagane pełne dowody; w przeciwnym wypadku uzupełnić je tam lub jawnie utrzymać zależność.

**Następna para:** **AT-15** — operacje kohomologiczne, naturalność, iloczyny i relacje; **AT-16** — zawieszenie, twierdzenie Freudenthala i homotopia stabilna. Zachować rygor matematyczny, komentarze dowodowe, rysunki i kompletne testy CI; bez nieuzgodnionych zmian `main`.


### Audyt szczegółowy AT — partia 8, rozdziały 15–16 (20.11.2026)

Zakończono audyt dwóch kolejnych kanonicznych rozdziałów topologii algebraicznej według standardu DG-01. Wszystkie zmiany zapisano bezpośrednio na gałęzi `biblioteka-matematyczna-iteracja-6`, bez naruszenia `main` i historycznych `\label` ani istniejących `\ref`.

**AT-15 — operacje kohomologiczne:** rozszerzono rachunek Bocksteina na komórkach `RP²`: `δ̃a(e²)=2 mod 4`, `β₂(t)=t²≠0`, a na `RP³` następny Bockstein znika. Nowy diagram różniczki/koróżniczki i redukcji modulo 2. Dokładnie wyliczono relację `Sq²Sq²=Sq³Sq¹` na `H*(RP∞;F₂)`; parzystość dwumianów uzasadniono elementarnymi tożsamościami `(1+z)²=1+z²` i `(1+z)⁴=1+z⁴` nad `F₂`, bez założenia nieobjaśnionego twierdzenia Lucasa. **Nie** wyciągnięto z tego fałszywego wniosku o dowodzie uniwersalnej relacji Adema. Poprawiono polskie terminy „odwzorowanie” i „homomorfizm”.

**AT-16 — Freudenthal, stabilizacja:** w przypadku butelki Kleina wyprowadzono `π₁(K)_ab=Z⊕Z/2` i `π₂(ΣK)=Z⊕Z/2`; homomorfizm zawieszenia `E` utożsamiono z abelianizacją, której jądro zawiera niezerowy komutator `b⁻²`. Porównano to z torusem. Rozpisano stabilizację pierwszego dodatniego pnia: `π₃(S²)=Z → π₄(S³)=Z/2 → π₅(S⁴)=Z/2`, pierwsza strzałka jest redukcją modulo 2, a kolejne są izomorfizmami dzięki dokładnemu sprawdzeniu zakresu Freudenthala. Dodano diagram i poprawiono terminologię.

**Weryfikacja:** 11/11 standardowych odsyłaczy AT-15/16 rozwiązuje się w AT-01–16, bez duplikatów etykiet i zewnętrznych plików graficznych. [CI aplikacji #44779319312](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44779319312) — **SUCCESS**, 187 testów Pythona (1 pominięty), Chromium zaliczone; [CI LaTeX #44779319260](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44779319260) — **SUCCESS**, 185 stron A4, 2 przebiegi `pdflatex`, brak niezdefiniowanych odsyłaczy i przepełnień. Sprawdzono wizualnie 3 diagramy AT-15/16, m.in. nowe na stronach PDF 175 i 183. Testy `application/tests/test_topology_chapters_15_16.py`; workflow `.github/workflows/algebraic-topology-audit-ch15-16.yml`. Protokół `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_15_16_2026-11-20.md`.

**Status rejestru:** AT-15 oraz AT-16 — `zaakceptowany_z_zastrzezeniem`. Otwarte zadania dowodowe: pełna konstrukcja zewnętrznych potęg/normalizacji/iterowanych diagonalnych zapewniająca `Cartan` i `Adem`; niezależny dowód ekscyzji homotopijnej Blakersa–Masseya; konstrukcyjna stabilność `Sq^i`. Nie uznano warunkowych dowodów za niezależne. Zaaudytowano pary AT-01–AT-16, ale różne statusy zastrzeżeń są zachowane, a nie nadpisane globalnym „wszystko udowodnione”.

**Następna para:** AT-17 — konstrukcja Pontriagina–Thoma i podstawy teorii kobordyzmów; AT-18 — homologia Morse’a. Standard DG-01, po dwa rozdziały, poprawki źródeł, retesty i commity.


### Audyt szczegółowy AT — partia 9, rozdziały 17–18 (20.11.2026)

Przeprowadzono kolejną iterację audytu **dokładnie dwóch** rozdziałów topologii algebraicznej, z poprawkami w kanonicznych źródłach:
`chapters/pl/algebraic_topology/17-konstrukcja-pontriagina-thoma-i-podstawy-teorii-kobordyzmow.tex` oraz
`chapters/pl/algebraic_topology/18-homologia-morse-a-od-punktow-krytycznych-do-homologii-singular.tex`.
Nie modyfikowano gałęzi `main`, historycznych deklaracji `\label`, ani wcześniejszych rozdziałów.

**Zgodność z geometrią różniczkową:** zgodnie z wyraźną decyzją użytkownika wykorzystano istniejący rozdział DG03 `03-algebra-tensorowa-i-zewnetrzna.tex` z etykietami `ch:algebra-tensorowa`, `sec:iloczyn-tensorowy`, `thm:tensor-hom`, `thm:tensor-istnienie`. W AT-17 przy `TRP^n` przywołano `Hom(ℓ,ℓ⊥)=ℓ*⊗ℓ⊥`, w AT-18 przy współczynnikach wymiernych wyjaśniono `CM_*(f,g)⊗_Z Q`, korzystając z płaskości lokalizacji `Q`. Dodano także odsyłacze do DG18 o teorii Morse’a (`ch:teoria-morsea`) oraz DG19 o rachunku uchwytów (`ch:rachunek-uchwytow`). Ponieważ tomy kompilują się oddzielnie, nowe odsyłacze międzytomowe są linkami `\href` do kanonicznych źródeł na GitHubie, a nie niezdefiniowanymi `\ref` w samodzielnym PDF. Oryginalne etykiety DG pozostają niezmienione; po scaleniu można je wykorzystać w systemie `xr-hyper`.

**AT-17:** udowodniono w szczegółowym przykładzie, że `X=RP²×RP²` ma niezerowe `w₂(X)²` i `w₄(X)` (obie liczby Stiefela–Whitneya równe `1`) i reprezentuje element rzędu dokładnie `2` w `Ω₄^O`. Porównano `X` z `Y=RP⁴` — obie mają `χ=1`, lecz ich pary liczb `(w₂²,w₄)` to `(1,1)` i `(0,1)`, więc nie są kobordantne. Ich klasy generują podgrupę `(Z/2)²` w `Ω₄^O` (bez nieuzasadnionego roszczenia do pełnej klasyfikacji grupy). Dodano diagram klas charakterystycznych.

**AT-18:** skonstruowano funkcję Morse’a na `RP²` przez iloraz formy kwadratowej z trzema różnymi wartościami własnymi; wyprowadzono jawny wzór przepływu gradientowego, krytyczne punkty indeksów `0,1,2` oraz niestabilne komórki `RP^k\\RP^{k-1}`. Zidentyfikowano mapę przyłączającą drugą komórkę jako dwukrotne nakrycie okręgu, stąd `∂₂=2` i `HM₁(RP²;Z)=Z/2`. Dodano diagram kompleksu i poprawiono polską terminologię, bez niepreferowanego określenia operacji tensorowej.

**Walidacja:** 17/17 standardowych odsyłaczy z AT-17/18 rozwiązuje się w AT-01–18; brak zduplikowanych etykiet w tym zakresie i brak nowych zależności od zewnętrznych zasobów. [GitHub Actions — aplikacja #44782170923](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44782170923) — **SUCCESS**, **198** testów Python (1 pominięty) oraz Chromium. [GitHub Actions — PDF #44782979521](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44782979521) — **SUCCESS**, **203 strony**, dwa przebiegi, brak niezdefiniowanych odsyłaczy i przepełnień. Obejrzano w wynikowym PDF wszystkie cztery diagramy AT-17/18 (strony 187, 192 oraz dwie ilustracje na 203); poprawiono położenie etykiety „Whitney” na diagramie, ponownie skompilowano i sprawdzono. Szczegółowy protokół: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_17_18_2026-11-20.md`; nowe testy: `application/tests/test_topology_chapters_17_18.py`; workflow: `.github/workflows/algebraic-topology-audit-ch17-18.yml`.

**Status:** AT-17 — `zaakceptowany`; AT-18 — `zaakceptowany_z_zastrzezeniem`: pełny analityczny dowód zwartości i sklejania trajektorii oraz związek orientacji/incydencji pozostają do szczegółowego audytu AT-20. Nie utożsamiać kompilacji z ich niezależnym dowodem.

**Następna para:** AT-19 — stopień, indeks punktu stałego i twierdzenie Lefschetza; AT-20 — zwartość i sklejanie trajektorii Morse’a, podstawy analityczne. Przy AT-20 ponownie zweryfikować otwarte zastrzeżenie AT-18.


### Audyt szczegółowy AT — partia 10, rozdziały 19–20 (20.11.2026)

Przeprowadzono szczegółowy audyt dwóch kolejnych rozdziałów topologii algebraicznej według standardu DG-01 na gałęzi `biblioteka-matematyczna-iteracja-6`. Bez przemianowywania wcześniejszych etykiet `\label` i bez ingerencji w `main`. Protokół: `application/docs/AUDYT_TOPOLOGIA_ALGEBRAICZNA_19_20_2026-11-20.md`.

**AT-19 — Lefschetz i indeks punktu stałego.** Skontrolowano lemat śladu Hopfa, dowód Lefschetza dla skończonych CW-kompleksów przy użyciu symplicjalnej aproksymacji i ANR, definicję indeksu lokalnego oraz formułę Lefschetza–Hopfa. Dodano całkowicie obliczony przykład `A=((2,1),(1,0))` na `T²`: dokładnie dwa punkty stałe `[(0,0)]`, `[(1/2,1/2)]`, oba indeksu `-1`, a `L(f_A)=det(I-A)=-2`. Kratowy argument parzystości daje dokładną liczbę punktów. Dodano rysunek dwóch punktów w kwadracie fundamentalnym. Przy potęgach zewnętrznych i wzorze na wyznacznik wprowadzono link do istniejącego rozdziału DG03 o algebrze tensorowej i zewnętrznej, z zachowanymi etykietami `thm:potega-zewn-operatora` i `thm:minory-lambda`; uniknięto podwójnego dowodu. Przypadek nieorientowalny twierdzenia Lefschetza–Hopfa nadal opiera się na przyjętym twierdzeniu o lokalnych współczynnikach i jest jawnie odnotowany.

**AT-20 — podstawy analityczne sklejania.** Skontrolowano zwartość z dokładnością do łamania, ograniczenia energii, limit trajektorii na przekrojach poziomów regularnych, wykładniczą zbieżność do punktu hiperbolicznego, jednostajnie ograniczony prawy odwrotny i zgodność orientacji. Dodano pełny dowód elementarnego operatora Greena dla `u'+λu=h` (`λ≠0`, `h` ograniczona) i oszacowanie `||Q_λh||∞≤||h||∞/|λ|` dla obu znaków `λ`. Dla `f(θ,φ)=cosθ+cosφ` na torusie dokładnie rozwiązano równania gradientu, opisano cztery składowe `M(p,r)≅R`, ich dwa rodzaje granic łamanych i `ρ_+=e^(−s)`, `ρ_−=e^s`. Gładkość kołnierza w tym **konkretnym** modelu wynika z jawnych formuł. Dodano diagram granic sklejania i link do DG18 — teorii Morse’a. Nie wyciągnięto nieuprawnionego wniosku o pełnej teorii gluing dla dowolnych par Morse'a–Smale'a.

**Retesty:** nowy `application/tests/test_topology_chapters_19_20.py` ma 10 kontroli, w tym arytmetyki punktów stałych, równania Greena, dokładnego rozwiązania ODE, kanonicznych odsyłaczy do DG, zachowania etykiet i zależności LaTeX. Pierwsza wersja testu nadmiernie wymagała `>3` odsyłaczy w AT-19 i spowodowała przejściowy FAILURE aplikacji; zmieniono go na poprawny warunek `>=3` w commicie `001eb10c`. [GitHub Actions aplikacji #44794340600](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44794340600) — **SUCCESS**, **208 testów Python** (1 pominięty), Chromium zaliczone, indeks 355 rozdziałów. [GitHub Actions LaTeX #44794340616](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44794340616) — **SUCCESS**, **217 stron**, dwa przebiegi `pdflatex`, bez niezdefiniowanych odsyłaczy i przepełnień. Obejrzano wszystkie cztery ilustracje AT-19/20 w PDF (strony 208, 210 i dwie na 216); brak obciętych obiektów i nachodzących etykiet. Workflow `.github/workflows/algebraic-topology-audit-ch19-20.yml`.

**Stan rejestru:** AT-19 — `zaakceptowany_z_zastrzezeniem` (przyjęta wersja orientacyjna formuły indeksowej z lokalnymi współczynnikami); AT-20 — `zaakceptowany_z_zastrzezeniem` (brak ogólnego lemat o jednostajnym prawym odwrotnym dla `D_T` i pełnej reguły orientacji brzegowej). **AT-18 pozostaje z zastrzeżeniem po AT-20**, mimo wykazania jawnego modelu na torusie. Testy i kompilacja nie są dowodem brakującego twierdzenia analitycznego.

**Następna para:** AT-21 — indeks pól wektorowych i twierdzenie Poincarégo–Hopfa z brzegiem; AT-22 — kohomologia z nośnikami zwartymi i homologia Borela–Moore’a. Zanim rozpoczniemy, należy zweryfikować dokładny stan kanonicznych plików; jak zawsze dwie jednostki na iterację.
