# ME-21 — drugi czysty przebieg stabilizacji merytorycznej

27.11.2026. Blob rozdziału 0efbea510139ea2f88b05421139be747c136c740, 1116 wierszy, bez zmian.

Sprawdzono ponownie gęstość C_c w L1 miary uzupełnionej, projekcję radialną do dysku jednostkowego, dodatnią i ujemną część funkcjonału rzeczywistego oraz ich identyfikację z częściami Jordana miary. W przypadku zespolonym sprawdzono konwencję liniowości, wybór sprzężonej fazy, dowód izometrii i alternatywną konstrukcję przez L1–L∞. Porównano z ME-32 zastosowanie Daniella–Stone'a do C_c i rozróżnienie sigma-algebry generowanej przez C_c od borelowskiej oraz warunki zgodności obu miar. Dowód ogólny ME-21 nie zależy od twierdzenia porównawczego ME-32, które korzysta z reprezentacji ME-21. Nie znaleziono nowej usterki wymagającej korekty rozdziału.

Dodano dwa testy regresyjne w tools/tests/test_measure_theory_ch21.py, commit 0640ff7ea155932cef6ee02beda1a5da5343f162, po ponownym pobraniu pliku wskutek konfliktu aktualizacji. Niezależnie wykonano w JavaScript dokładne obliczenia całkowite: 1944/1944 konfiguracji projekcji radialnej (współrzędne przeskalowane przez 10) i 8000/8000 konfiguracji części dodatniej funkcjonału na trzech punktach z wyczerpującym przeglądem całkowitych funkcji dopuszczalnych. Razem 9944 konfiguracje bez niezgodności. Nie uruchomiono pełnej suity Python. Poprzednia kontrola na identycznym blobie: 27 etykiet, 63 ref/eqref, 18 atlasref, 14 dowodów, 14 wpisów indeksu.

CI na 96efc1d: ME-21 #45999839153 pending, globalny ME #45999839187 queued w chwili odczytu. Nowe testy i PDF bez potwierdzenia CI. Kolejny krok: audyt kontrolny ME-21, następnie ME-23.
