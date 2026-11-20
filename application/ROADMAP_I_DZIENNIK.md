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