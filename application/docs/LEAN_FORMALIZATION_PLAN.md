# Lean Formalization — plan wdrożenia do Atlasu matematycznego

**Data przyjęcia:** 2026-11-22  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź robocza:** `biblioteka-matematyczna-iteracja-6`  
**Stan:** zatwierdzony plan; wdrożenie iteracyjne.  
**Zasada:** Lean to niezależna warstwa formalizacji, a nie zastępstwo audytu matematycznego i językowego. Kanoniczne źródła `.tex` są tylko do odczytu.

## Cel końcowy
W czytniku aplikacji użytkownik wybiera twierdzenie/lemat/dowód albo zaznacza dowolny zakres pełnych wierszy źródłowego LaTeX-a. Może otworzyć panel **Lean 4** z:
- dokładnym źródłem LaTeX, etykietą i lokalizacją,
- odpowiadającym mu kodem Lean 4, o ile formalizacja istnieje,
- statusem zgodności treści, statusem kompilacji/dowodu, logiem diagnostycznym,
- zależnościami Mathlib i lokalnymi lematami oraz odciskiem wersji źródła,
- przyciskiem **Uruchom Lean** dla zatwierdzonej formalizacji.
Brak istniejącego pliku Lean nie jest udawany przez generację szablonu jako dowód. Wybrany dowolny fragment nie jest traktowany jako wykonywalny kod.

## Rozdzielenie stanów (nie łączyć w jeden bool!)
1. **Wierność treści** (`statement_status`): `unreviewed`, `needs_review`, `approved`; kontrola zgodności formalnego stwierdzenia z polskim LaTeX, zakresami kwantyfikatorów, założeniami, definicjami i typami.
2. **Stan formalizacji** (`formalization_status`): `missing`, `draft`, `ready`, `stale`; powiązanie z `module_id`, `entity_id`, `label` i SHA256 źródła.
3. **Stan uruchomienia** (`proof_status`): `not_run`, `verified`, `failed`, `timeout`, `toolchain_unavailable`, `blocked`; wynika wyłącznie z rzeczywistego wykonania Lean.
Do wyświetlenia certyfikatu **Zweryfikowane matematycznie** wymagane są jednocześnie: zatwierdzona wierność stwierdzenia, aktualne SHA źródła, rzeczywisty pozytywny wynik Lean, kontrola niepożądanych aksjomatów, brak `sorry`/`admit` i brak pozornie dowolnych założeń. Kompilacja kodu nie certyfikuje poprawności przekładu oryginalnego twierdzenia.

## Architektura
- **Istniejące wejście:** `application/backend/latex_parser.py`, SQLite `documents`/`entities`/`labels` (read-only); wybór zakresu w `application/frontend/app.js`.
- **Nowy backend:** `application/backend/lean_formalization.py`: odczyt rejestru, sprawdzenie integralności SHA, uruchomienie Lean w procesie podrzędnym, diagnostyka.
- **Rejestr:** `application/lean/manifest.json`, elementy z `source_module`, `source_entity` lub dokładną etykietą, `source_sha256`, `lean_file`, `lean_theorem`, statusem recenzji treści. Pliki `.lean` w `application/lean/src/`; rygorystyczna kontrola ścieżek bez traversalu.
- **Backend API:** `GET /api/lean/status` (dostępność `lake`/Lean), `GET /api/lean/fragment?entity_id=...` lub `?module_id=...&start_line=...&end_line=...` (źródło + kod + status), `POST /api/lean/run` (identyfikator zatwierdzonej formalizacji, bez dowolnego kodu z przeglądarki).
- **Frontend:** panel/zakładka Lean otwierana z Czytnika; przejście z obiektu i z istniejącego zaznaczenia wierszy; tylko `textContent` dla nieufnego LaTeX/Lean/logów. Widoczne statusy osobno.
- **Uruchomienie:** wyłącznie lokalny `lake env lean` lub `lean`, ustalony katalog, izolowany katalog tymczasowy, limit czasu i wyjścia, biała lista zarejestrowanych plików; żadnej możliwości uruchamiania arbitralnych komend powłoki. W środowisku współdzielonym konieczny sandbox na poziomie systemu operacyjnego (sam timeout subprocess nie jest pełnym sandboxem).
- **Wersjonowanie:** stabilny Lean 4 + przypięty commit Mathlib/`lake-manifest.json`; rejestrować wersję przy każdym sprawdzeniu.
- **CI:** statyczne testy API/JS zawsze; kompilacja małej bazy próbnej tylko w środowisku z zainstalowanym Lean/Mathlib. Nie zaliczać „verified” bez takiego uruchomienia.

## Etapy

### Etap 1 — działający minimalny moduł (priorytet)
1. Zidentyfikować obiekt ze źródła `entities` (lemat, twierdzenie, dowód) albo dokładne wiersze.
2. Wyświetlić panel Lean wraz z dokładnym źródłem LaTeX, kodem formalizacji, statusami i komunikatami.
3. Dodać czytelny status `missing` dla fragmentów bez formalizacji (nie generować fałszywych odpowiedników).
4. Odczytać konkretne, ręcznie przygotowane przykłady z `manifest.json`, zabezpieczyć integralność źródła.
5. Dodać przycisk uruchomienia wyłącznie znanego pliku z rejestru, z limitem zasobów, logiem i poprawnym `toolchain_unavailable`, gdy Lean nie jest zainstalowany.
6. Dodać testy jednostkowe/API/UX: obiekt, wybór wierszy, brak kodu, uszkodzony manifest, przestarzały SHA, brak narzędzia, awaria/timeout, pomyślne wykonanie przez atrapę procesu.
**Kryterium akceptacji:** użycie UI i API dla 1 poprawnie powiązanego obiektu; testy regresji; realne uruchomienie Lean, jeśli środowisko je udostępnia. W przeciwnym razie jawnie status `toolchain_unavailable`, etap 1 nie ma dowodu rzeczywistego uruchomienia.

### Etap 2 — pilotaż 20–30 formalizacji
- Najpierw `LST-01`, `LST-02` oraz `LA-01`, zaczynając od prostych praw logicznych i podstaw algebry liniowej.
- Każda formalizacja powiązana z **konkretnym** `\label`/obiektem i wersją źródła; oddzielać nieformalną semantykę wartościowań od `Prop` w Lean. Zmiana siły stwierdzenia wymaga przeglądu.
- Przykłady pilotażowe: prawa de Morgana, rozwinięcie implikacji, negacja implikacji, prawa kwantyfikatorów, przemienność dwóch kwantyfikatorów tego samego typu, podstawowe własności przestrzeni wektorowych.
- Raport liczbowy: przygotowane, skompilowane, zatwierdzone semantycznie, bez `sorry`, błędy i ograniczenia.

### Etap 3 — biblioteka zależności i automatyczna transkrypcja (eksperyment)
- Zintegrować mapowanie `label ↔ theorem`, graf zależności i wyszukiwanie Mathlib.
- Opcjonalnie przetestować PaperFormalizer/LeanAide/Aristotle; wymagana walidacja licencji, wersji i kosztów. Kandydaci nie mogą bezpośrednio nadpisywać źródeł `.tex`.
- Generacja transkrypcji trafia zawsze do stanu `draft`/`needs_review`; niezależne sprawdzenie semantyki i Lean.

### Etap 4 — skala i CI
- Cache kluczowany `source_sha + lean_sha + toolchain_version`; powtórna kontrola tylko zmienionych zależności.
- Publiczne raporty JSON dla rozdziału; opcjonalne oznaczenie w PDF tylko po spełnieniu kryteriów certyfikatu.
- Stopniowe rozszerzanie na inne dziedziny, bez automatycznego przypisywania wysokiego statusu przy braku Mathlib.

## Podział prac automatycznych
**Strumień A — implementacja aplikacji:** pracuje tylko w `application/backend/`, `application/frontend/`, `application/tests/` i dokumentacji Lean; wykonuje jedną mierzalną iterację oraz testy, commit na istniejącej gałęzi, wpis do dziennika. Unika zmian `.tex` i innych audytów.
**Strumień B — formalizacje i ich audyt:** pracuje wyłącznie w `application/lean/` i własnych raportach, dodaje po jednym lub kilku niepowielanych przykładach oraz uruchamia Lean, jeśli dostępny; nie dotyka plików backend/frontend/kanonicznych `.tex`. Przy braku działającego interfejsu programu kontynuuje tworzenie i testowanie korpusu niezależnie.
**Zasada współbieżności:** przed zapisem zawsze odczytać aktualny HEAD gałęzi; nie robić force-push, nie nadpisywać zmian innych audytów; przy konflikcie zaniechać zapisu i zaraportować. Każda iteracja odczytuje ten plan i ostatni status; brak nowej pracy = raport, bez fikcyjnych commitów.

## Dziennik iteracji Lean
- 2026-11-22 — użytkownik zatwierdził uruchamianie Lean z aplikacji, podgląd kodu i statusu dla wybranego fragmentu. Przyjęto cztery etapy i dwa rozdzielone strumienie automatyczne. Etap 1 traktować jako pierwszy cel implementacji. Rzeczywiste wykonanie Lean nie jest jeszcze potwierdzone.
