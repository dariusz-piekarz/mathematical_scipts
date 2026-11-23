# Atlas L1.1 — pakiet odbiorowy i niezależne zatwierdzenie

**Fragment:** L1.1, ograniczenie odczytu i tożsamość deskryptora artefaktów `.olean`.  
**Kandydat:** `5e6e017a7d98ce2dfb384b4e973cce08159be3fc` (niezmienny commit Git).  
**Źródło prawdy o CI:** [Atlas #45136597724](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136597724).  
**Stan pakietu przy utworzeniu:** 1/3 pełnych rund potwierdzona; w drugiej rundzie aplikacja, Linux i Windows zaliczone, rzeczywisty Lean/Mathlib był nadal w toku. **Nie jest to zatwierdzenie.**

## Zakres zatwierdzanego kodu

- `application/backend/lean_environment.py`: maksymalnie 64 MiB rzeczywistego odczytu treści na fingerprint, brak odczytu rosnącego pliku ponad jego początkowy rozmiar, zamknięta obsługa skróconego pliku, odrzucenie symlinków i nieprawidłowego typu otwartego deskryptora, kontrola `os.fstat(fd)` — `st_dev` i `st_ino` zgodne ze wstępnym `stat(path)`; statystyki po odczycie nie mogą wskazywać zmiany.
- `application/tests/test_lean_environment.py`: testy współbieżnego dopisania prawdziwego bajtu, przedwczesnego EOF, limitu odczytu, podmiany deskryptora na inny zwykły plik o tym samym rozmiarze i podmiany na urządzenie nieregularne.
- `application/scripts/atlas_validation_gate.py` oraz `application/tests/test_atlas_validation_gate.py`: testy kompletności dowodów, wymaganego SHA i niemożności samodzielnego nadania `stable` przez niesygnowany JSON o rzekomo niezależnym recenzencie.

## Kryteria techniczne (sprawdzać na dokładnie tym samym SHA)

1. Trzy pełne, odrębne przebiegi w [Atlas #45136597724](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136597724): każdy z kompletem application+Chromium, Linux/Windows, przypiętym Lean 4/Mathlib, rzeczywistym audytem aksjomatów i introspekcją MetaM. Kroki nie mogą być `skipped` zamiast wykonane; wyjątki środowiskowe są jawnie wymienione i uzasadnione.
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
- [#45136169753](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136169753): pełny CI na bieżącym kandydacie, 687 testów aplikacji, 10 jawnych pominięć, `test_self_declared_independent_review_never_grants_stable` zaliczony, Chromium bez błędów; pojedynczy CI nie zastępuje 2+1.
