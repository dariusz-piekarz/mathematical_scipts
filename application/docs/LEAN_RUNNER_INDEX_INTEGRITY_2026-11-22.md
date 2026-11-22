# Lean runner — weryfikacja integralności indeksu przed uruchomieniem

Data: 2026-11-22. Strumień A, etap 1, jedna iteracja bezpieczeństwa backendu.

## Zmiana

W `backend/lean_formalization.py::run` przed sprawdzeniem dostępności runnera i przed wywołaniem `subprocess.run` sprawdzany jest SHA256 **faktycznej zawartości** `documents.content` względem `documents.sha256`. Poprzednio sprawdzano wyłącznie SHA z indeksu względem opcjonalnego `source_document_sha256` rejestru; zmiana zawartości indeksu bez zmiany jego SHA nie była wykrywana. Teraz niespójny lub nie-tekstowy indeks zwraca `proof_status=blocked`, `certificate=false` i nie uruchamia procesu. Nie modyfikowano kanonicznych plików LaTeX ani rejestru Lean.

## Testy

Dodano dwa testy w `tests/test_lean_formalization.py`:
- `test_runner_blocks_inconsistent_index_before_subprocess` — niezgodny SHA blokuje uruchomienie i potwierdza `spawn.assert_not_called()`;
- `test_runner_rejects_nontext_index_content` — brak tekstu źródła blokuje proces i certyfikat.

**Wynik:** zmiany zatwierdzone na istniejącej gałęzi; pełne testy aplikacji uruchomione przez GitHub Actions [45011756997](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011756997), wynik jeszcze nieznany w chwili zapisu raportu. Poprzedni pełny przebieg [45011702386](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011702386) zakończył się błędem niezwiązanym z runnerem: `test_unregistered_auxiliary_lean_source_is_also_audited` oczekuje komunikatu `Missing or oversized`, a otrzymał `Missing #print axioms checks for: extra`. Jest to regresja narzędzia `application/scripts/lean_ci_audit.py`, poza zakresem zapisu tego strumienia. Nie zaliczać pełnej regresji, dopóki ten konflikt nie zostanie rozwiązany.

Testy korzystające z atrap subprocess nie są rzeczywistą kompilacją Lean. Brak narzędzia `lake` jest raportowany przez istniejący runner jako `toolchain_unavailable`, nigdy `verified`. Pomyślny subprocess pozostaje `compiled` z `certificate=false`.

## Ograniczenia i następny krok

Weryfikacja SHA zamyka konkretną lukę w integralności indeksu, lecz nie zapewnia izolacji systemowej wykonywanego pliku Lean, a istniejący runner nadal wymaga lokalnego zaufanego środowiska. Następna iteracja: odczytać wynik CI, skontrolować regresję całego backendu oraz wzmocnić ograniczenia wyjścia i zasobów procesu; bez rozszerzania uprawnień do wykonywania kodu dostarczonego przez klienta.

## Retest po wykryciu błędu składni testu

Pierwszy przebieg po dodaniu regresji, [45011756997](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011756997), zakończył się błędem `SyntaxError: unexpected character after line continuation character` w `tests/test_lean_formalization.py:116`: nowe testy zawierały podwójne ukośniki na końcu wierszy `with`. Poprawiono trzy kontynuacje na pojedynczy znak `\\` (commit `4314f43c7f572c9aad2adb5295a30acbb3f6f8bd`). Ponowny rzeczywisty test: [45011821712](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45011821712), wynik oczekujący. Nie zaliczać regresji przed jego zakończeniem.
