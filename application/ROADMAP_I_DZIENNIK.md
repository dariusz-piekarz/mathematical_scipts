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
