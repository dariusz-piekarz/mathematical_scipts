# Podział logiki i teorii mnogości oraz teorii modeli

Stan: 2026-11-28. Plan migracji; nie oznacza zakończenia migracji ani audytu.

## Źródła i granice
Katalog zawiera 39 rozdziałów logic_and_set_theory i 19 model_theory (00–18). Kanoniczną podstawą nowych skryptów są rozdziały logic_and_set_theory.
- LST 01–13, 16–22, 25–39 pozostają w logice i teorii mnogości.
- LST 14–15 oraz 23–24 przechodzą do właściwej teorii modeli; zachować ich etykiety oraz identyfikatory lub jawne aliasy migracyjne.
- LST 39 pozostaje przy dużych liczbach kardynalnych; odsyłacze do logiki infinitarnej z teorii modeli.
- Semantyka pierwszego rzędu i pełność pozostają kanonicznie w LST 09–13; teoria modeli odsyła do tych rozdziałów, bez kopiowania dowodów.
- Stara teoria modeli (00–18) zostanie wycofana po porównaniu treści, dowodów, przykładów i etykiet. Nie usuwać w ciemno.

## Wstępna mapa starego MT
| MT | Kanoniczny odpowiednik LST do audytu |
| --- | --- |
| 00–02 | 09–13 |
| 03–05 | 16–17 |
| 06–07 | 18 |
| 08 | 19 |
| 09 | 20 |
| 10 | 21 |
| 11–12 | 22 |
| 13–14 | 23–24, 14 i 22 |
| 15 | 19, 22 |
| 16 | 21–22 |
| 17 | 17–20 |
| 18 | 19–22 |

Wstępnie odczytano rozdziały MT 15–18 oraz LST 19, 20, 22: zakresy tematyczne nakładają się, ale etykiety są różne, m.in. sec:codzienna-matematyka, sec:granice-zaufania, sec:sens-tarski, sec:czego-nie-mowia oraz stare etykiety numeryczne. Mapa nie dowodzi pełnego pokrycia. Przed usunięciem trzeba rozstrzygnąć ich rzeczywiste cele, unikać kolizji i nie dodawać pozornych etykiet.

## Rozwój właściwej teorii modeli
Struktury, podstruktury i elementarność; zwartość; twierdzenia Löwenheima–Skolema; diagramy; test Tarskiego–Vaughta; łańcuchy elementarne; zbiory definiowalne; typy i przestrzenie typów; realizacja i pomijanie typów; nasycenie i jednorodność; eliminacja kwantyfikatorów; zupełne i modelowo zupełne teorie, uzupełnienia modelowe; ultrailoczyny i twierdzenie Łosia; kategoryczność, twierdzenie Ryll-Nardzewskiego; podstawy stabilności, rang, forkingu; przykłady DLO, ACF, RCF i arytmetyki. Rozszerzenia dopiero po stabilizacji migracji.

## Logika rozmyta — proponowany nowy rozdział w LST
Umieścić po klasycznej logice pierwszego rzędu (dotychczasowe 09–13), w bloku logik nieklasycznych. Numer ustalić po migracji, nie przenumerowywać etykiet automatycznie.
1. Wielowartościowość, wartości logiczne, różnica między stopniem prawdy a prawdopodobieństwem.
2. Zbiory rozmyte, funkcje przynależności, przekroje alfa, nośniki, jądra, zasada reprezentacji przez przekroje; relacje rozmyte.
3. Normy trójkątne i konormy, negacje, dualność de Morgana dla odpowiednio dobranych operacji; przykłady i kontrprzykłady.
4. Residuacja i implikacje; rozróżnienie koniunkcji kratowej i monoidalnej; logiki Gödla–Dummetta, Łukasiewicza i produktowa.
5. Algebraiczna semantyka: kraty rezyduowane, algebry MTL, BL, MV; aksjomatyzacje i poprawność, właściwie sformułowana pełność (oddzielić semantykę standardową od ogólnej i rachunek zdań od pierwszego rzędu).
6. Predykaty rozmyte, wartości kwantyfikatorów jako infimum i supremum, konsekwencja logiczna; ograniczenia twierdzeń klasycznych.
7. Liczby rozmyte, arytmetyka przekrojów alfa, zasada rozszerzania.
8. Przykład wnioskowania Mamdaniego i Sugeno, defuzyfikacja; zastosowania jako ilustracja, nie główny temat. Wykresy funkcji przynależności i porównania operacji, przykłady z rachunkami.
9. Relacja z logiką klasyczną, teorią prawdopodobieństwa i teorią możliwości. Odsyłacze do algebry abstrakcyjnej, teorii miary i teorii modeli; rozwinięcie modeli wielowartościowych ewentualnie w teorii modeli.

## Warunki zakończenia migracji
- Audyt różnic całych 19 starych rozdziałów, w tym wstępu i uwag końcowych; rejestr każdej etykiety i rzeczywistego odpowiednika.
- Uzgodnić preambuły, punkty wejścia, katalog, mapowania Atlasu i generatora, aliasy, dokumentację, workflow oraz testy; nie usuwać źródeł przed audytem.
- Porównać liczbę i treść obiektów, globalne odsyłacze, uruchomić walidację repozytorium i testy indeksu, generatora i aplikacji; skompilować oba PDF-y.
- Audyty do stabilizacji, następnie niezależny audyt kontrolny. Nie deklarować zielonego CI bez faktycznego wyniku.

## Kolejność realizacji
Najpierw LST: audyt metamatematyki i teorii mnogości, logiki nieklasyczne (rozmyta, intuicjonistyczna, modalna, wielowartościowa, parakonsystentna), kontrola pokrycia teorii krat i algebr Boole'a w AA, rachunki zdań i predykatów, konstrukcje liczb, indukcja i rekurencja pozaskończona, regularność i osobliwość kardynałów, kluby i zbiory stacjonarne, lemat Fodora, drzewa, wymuszanie i niezależność. Lista do audytu pokrycia, nie lista potwierdzonych braków.
Rozdział 40: podstawy logiki rozmytej. Do rozwinięcia aksjomaty MTL/BL/MV i poprawność/pełność, twierdzenie McNaughtona, kontrprzykłady zwartości, dodatkowe rysunki, relacje równoważności, szczegółowe przykłady wnioskowania. Docelowo przenieść po rozdziale 13 z dostosowaniem numeracji i testów.
Po stabilizacji LST: właściwa teoria modeli, kolejno diagramy, zwartość, LS, łańcuchy elementarne, ultrailoczyny, eliminacja kwantyfikatorów (DLO, ACF, RCF), typy, nasycenie, pomijanie typów, modelowa zupełność, kategoryczność, stabilność, o-minimalność i logika ciągła.
Migracja wymaga zmiany istniejącego workflow, który sprawdza pierwsze 39 rozdziałów w pierwotnej kolejności, oraz testów odczytujących fizyczne ścieżki LST 14, 15, 23, 24. Nie usuwać starych rozdziałów bez audytu etykiet. Każdy rozdział audytować do stabilizacji, następnie audyt kontrolny.

## Migracja strukturalna
Cztery rozdziały LST przenosimy z zachowaniem bajtów i etykiet do MOD-20–23. Wybór numerów zapobiega ponownemu użyciu identyfikatorów dawnych MOD-00–18. Stare źródła w całości archiwizujemy w `sources/pl/legacy_model_theory_2026_11_28/` (w tym punkt wejścia), a nie usuwamy bezpowrotnie. Audyt pokrycia i ewentualne odtworzenie odsyłaczy historycznych są oddzielnym etapem. Szczegóły SHA i ścieżek w `catalog/logic_model_migration.json`.

## Drugi etap podziału: fundamenty teorii modeli
Decyzja po dyskusji: dotychczasowe LST 09–13 stają się MOD-24–28 i poprzedzają MOD-20–23 w kolejności dydaktycznej. Obejmuje to składnię, semantykę, dedukcję naturalną (jako niezbędny aparat), poprawność i pełność Gödla. Nowe rozdziały ogólnej teorii dowodu (rachunek sekwentów, eliminacja cięcia, normalizacja) pozostaną w LST i odsyłają do dedukcji naturalnej w MOD. Twierdzenia o niezupełności, arytmetyka formalna, obliczalność, logiki nieklasyczne i teoria mnogości pozostają w LST. Nie dublować dowodów. LST-40 docelowo umieścić w części logik nieklasycznych. Priorytet opracowania pozostaje LST. Zachować identyfikatory MOD-20–23 i kolejność katalogową niezależną od numerów plików.
