# Atlas L1.1 — pakiet odbiorowy i niezależne zatwierdzenie

**Fragment:** L1.1, ograniczenie odczytu i tożsamość deskryptora artefaktów `.olean`.  
**Kandydat:** `c3503db43bb2bb666baf0f34eb6bcbb3c2f7581b` (niezmienny commit Git).  
**Źródło prawdy o CI:** [Atlas #45139268248](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45139268248).  
**Stan kontroli przy aktualizacji:** 2/3 pełne rundy potwierdzone; w trzeciej aplikacja, Chromium, Linux i Windows zaliczone, Lean+Mathlib jeszcze nieukończony przy ostatnim odczycie. Ostateczny wynik ustala wyłącznie GitHub Actions i raport `atlas-validation-status`. **Nie jest to zatwierdzenie.**

## Zakres zatwierdzanego kodu

- `application/backend/lean_environment.py`: maksymalnie 64 MiB rzeczywistego odczytu treści na fingerprint, brak odczytu rosnącego pliku ponad jego początkowy rozmiar, zamknięta obsługa skróconego pliku, odrzucenie symlinków i nieprawidłowego typu otwartego deskryptora, kontrola `os.fstat(fd)` — `st_dev` i `st_ino` zgodne ze wstępnym `stat(path)`; statystyki po odczycie nie mogą wskazywać zmiany.
- `application/tests/test_lean_environment.py`: testy współbieżnego dopisania prawdziwego bajtu, przedwczesnego EOF, limitu odczytu, podmiany deskryptora na inny zwykły plik o tym samym rozmiarze i podmiany na urządzenie nieregularne.
- `application/scripts/atlas_validation_gate.py` oraz `application/tests/test_atlas_validation_gate.py`: testy kompletności dowodów, wymaganego SHA i niemożności samodzielnego nadania `stable` przez niesygnowany JSON o rzekomo niezależnym recenzencie. Nowe zabezpieczenie na tym SHA ponownie oblicza dozwoloną kategorię każdego pominięcia z identyfikatora testu i dokładnego powodu; wymaga `executed == outcome_count == len(outcomes)`. Testy atakujące: podrobiona kategoria znanego/nieznanego testu, brak imiennych wyników, nieprawidłowy typ licznika.

## Kryteria techniczne (sprawdzać na dokładnie tym samym SHA)

1. Trzy pełne, odrębne przebiegi w [Atlas #45139268248](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45139268248): każdy z kompletem application+Chromium, Linux/Windows, przypiętym Lean 4/Mathlib, rzeczywistym audytem aksjomatów i introspekcją MetaM. Kroki nie mogą być `skipped` zamiast wykonane; wyjątki środowiskowe są jawnie wymienione i uzasadnione.
2. Trzy artefakty `atlas-unittest-1`, `atlas-unittest-2`, `atlas-unittest-3`; w każdym `candidate_sha` równe powyższemu, `success=true`, zero błędów i nieznanych pominięć, obecna i wykonana regresja rzeczywistego wzrostu pliku. Zweryfikować liczbę i faktyczne nazwy testów oraz krytycznych przypadków bezpieczeństwa.
3. Artefakt `atlas-validation-status`: `passes` zawiera trzy poprawne rundy, wszystkie `workflow_results` są `success`, `problems=[]`, `certificate=false`. Wynik `stabilizing` jest prawidłowy **przed autentykowanym niezależnym zatwierdzeniem**.
4. Przypadki negatywne: różny SHA, pominięty test, pominięty cały przebieg, obce bajty pliku o równym rozmiarze, `os.devnull` oraz fałszywy `reviewer` nie mogą przechodzić niezauważone. Odrzucenie podstawienia deskryptora i fałszywego recenzenta ma wynikać z realnych testów, nie tylko deklaracji.

## Jawnie nieudowodnione własności

- Punktowy fingerprint nie daje ochrony przed wszystkimi możliwymi wyścigami TOCTOU, zwłaszcza przy niestandardowych systemach plików lub mutacjach po ostatnim `stat`. Metadane `metadata_only` nie oznaczają pełnego haszowania treści.
- Poprawna kompilacja Lean i pozytywny audyt aksjomatów **nie dowodzą** semantycznej zgodności twierdzenia źródłowego LaTeX i jego formalizacji. `certificate=false`.
- Pominięte ze względu na host cgroup i `pdflatex` nie zostały faktycznie wykonane. Nie wliczać ich do potwierdzonych funkcjonalności.

## Formalne poświadczenie odrębnego recenzenta — nadal wymagane

Przed awansem do `stable` wymagane są: (a) niezależna ocena kodu i wyników, (b) autentykowany podmiot zatwierdzający, inny niż autor zmian, (c) trwałe powiązanie oceny z pełnym SHA oraz zestawem linków do ukończonego CI, (d) zapis ryzyk i decyzji w kontrolowanym kanale. Przykładowo może to być zatwierdzenie Pull Request przez uprawnionego niezależnego recenzenta, którego uprawnienia i tożsamość są weryfikowane przez GitHub, przy właściwej polityce ochrony gałęzi. **Nie zakładać, że polityka jest skonfigurowana, bez potwierdzenia jej ustawień.**

Nie zastępować poświadczenia samodzielnie edytowanym plikiem JSON z `reviewer`, `independent=true` ani komentarzem autora. Integracja GitHub w obecnym środowisku zwróciła 403 przy próbie odczytu ochrony tej gałęzi, więc stan takich zabezpieczeń jest **niezweryfikowany**, nie „brak ochrony”.

**Decyzja w tym dokumencie:** `pending_authenticated_review`. Ten dokument jest pakietem dowodów i checklistą, **nie** podpisaną recenzją ani pozwoleniem na L1.2.

## Dowody historyczne (inne SHA)

- [#45133923118](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133923118): 3/3 pełne zestawy na `dda19fc9eb8fc274296d8cf15980f52354241301`, lecz przed poprawką walidacji niezależności recenzji.
- [#45136169753](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136169753): historyczny CI na starszym SHA `5e6e017a` (687 testów) z ochroną przed sfabrykowaną recenzją.
- [#45138963205](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45138963205): pełny CI na bieżącym SHA `c3503db4`, `completed/success`, **690 testów aplikacji** (10 sklasyfikowanych pominięć), 3 nowe regresje audytu kategorii pominięć i liczników zaliczone, Chromium bez błędów, 495 rozdziałów.

## Odczytane źródła prawdy i granica zatwierdzenia

- Repozytorium, gałąź i pełny SHA kandydata są określone wyżej. Jego zawartość nie zmienia się wraz z równoległymi zmianami innych audytów. Kontrole statusu opierać na **SHA kandydata**, a nie na ruchomym HEAD.
- Krytyczne pliki kodu, testów i workflow (9 ścieżek): `application/backend/lean_environment.py`, `application/tests/test_lean_environment.py`, `application/scripts/atlas_validation_gate.py`, `application/scripts/atlas_ci_report.py`, `application/tests/test_atlas_validation_gate.py`, `.github/workflows/atlas-stabilization.yml`, `.github/workflows/mathematical-library-app.yml`, `.github/workflows/lean-inspection-fast.yml`, `.github/workflows/lean-formalization.yml`. Porównanie Git blob SHA na aktualnej gałęzi i kandydacie wykazało 9 zgodnych plików przy audycie.
- Zamknięcie L1.1 wymaga odrębnej, autentykowanej decyzji osoby uprawnionej, która rzeczywiście zapozna się z kodem i wynikami. **Nie zapisano tu takiej decyzji.** Zweryfikowana kompilacja Lean+Mathlib nie dowodzi równoważności źródła i formalizacji.
