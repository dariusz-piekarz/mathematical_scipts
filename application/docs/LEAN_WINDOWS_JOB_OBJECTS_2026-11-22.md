# Windows Job Objects — zabezpieczenia lokalnego runnera Lean

Data: 22 listopada 2026. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Architektura

Gdy zaufana aplikacja ma ustawione `MATLIB_LEAN_TOTAL_MEMORY_MB`, system Windows używa `application/backend/lean_windows_job.py`. Program przygotowuje anonimowy Job Object, ustawia `JOB_OBJECT_LIMIT_JOB_MEMORY` oraz `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`, odczytuje ustawienia z powrotem i blokuje uruchomienie, gdy konfiguracja jest odrzucona.

Serwer uruchamia tylko własny program `lean_windows_exec.py`, którego wejście standardowe jest kanałem synchronizacji. Program nie uruchamia `lake env lean` przed otrzymaniem dokładnego tokenu `START\n`. Serwer najpierw przypisuje PID tego programu do Job Object przez `AssignProcessToJobObject`, a dopiero potem wysyła token; kompilator i jego procesy potomne dziedziczą Job Object. Przy zakończeniu i błędach zamknięcie uchwytu Job Object kończy procesy pozostałe w grupie. Wynik nie jest przedstawiany jako `compiled`, jeśli w grupie pozostały procesy. Niezgodność źródła LaTeX i Lean nadal nie może być oceniana na podstawie kodu wyjścia: `certificate=false`.

Implementacja odmawia uruchomienia (`blocked`), gdy zażądano limitu, którego nie da się ustawić. Konfiguracja bez `MATLIB_LEAN_TOTAL_MEMORY_MB` zachowuje stary tryb i **nie** ustanawia systemowego limitu łącznej pamięci. Windows jest obsługiwany dla limitu **agregowanego**; osobna zmienna `MATLIB_LEAN_MEMORY_MB` nadal wymaga Linuksa, więc na Windows należy ją pozostawić nieustawioną.

### Konfiguracja PowerShell

```powershell
$env:MATLIB_LEAN_RUN = "1"
$env:MATLIB_LEAN_TOTAL_MEMORY_MB = "8192"
Remove-Item Env:MATLIB_LEAN_MEMORY_MB -ErrorAction SilentlyContinue
```

`8192` oznacza limit pamięci zatwierdzonej (committed) w MiB dla całego Job Object. Zakres konfiguracji wynosi 512–65536 MiB; wartość trzeba dobrać do obciążenia narzędzi Lean/Mathlib. Osobny limit czasu i ograniczonego logu pozostają włączone. `availability.ready` jest wstępnym sprawdzeniem platformy, a rzeczywisty test uprawnień odbywa się podczas tworzenia Job Object.

### Testy

```powershell
Set-Location application
python -m unittest discover -s tests -p "test_lean_windows_job.py" -v
python -m unittest discover -s tests -p "test_lean_formalization.py" -v
```

Testy z `test_lean_windows_job.py` obejmują odmowę startu bez poprawnego tokenu, uruchomienie dopiero po zdjęciu blokady, kontrolę kontraktu Win32 poprzez symulację, poprawność sprzątania i odmowę uruchomienia po błędzie Job Object. `test_native_windows_job_memory_restriction` wykonuje rzeczywistą próbę alokacji przekraczającej limit **wyłącznie na Windows**. `test_native_windows_timeout_terminates_descendants` sprawdza natywnie, że po timeout proces potomny nie może kontynuować działania. Uruchomienie linuksowego CI nie dowodzi natywnej zgodności Windows: przebieg na Windows wymaga osobnego potwierdzenia.

### Granice

Windows Job Object ogranicza łączną pamięć **committed**, a nie sumaryczne RSS. Jest to kontrola zasobów dla zatwierdzonych lokalnych źródeł, nie sandbox przeciw złośliwemu kodowi. Nie używamy flag umożliwiających swobodne opuszczenie Job Object. Jeśli aplikacja działa już wewnątrz Job Object, niekompatybilne zagnieżdżenie może spowodować odmowę przypisania; należy zachować `blocked`, a nie automatycznie wyłączyć limit. Windows wymaga nowoczesnego systemu obsługującego zagnieżdżone Job Objects.

Podstawa API Microsoft: https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects oraz https://learn.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-jobobject_extended_limit_information
