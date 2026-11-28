# ME-21 — pierwszy czysty przebieg stabilizacji merytorycznej

27.11.2026. Blob rozdziału 0efbea510139ea2f88b05421139be747c136c740 (1116 wierszy), niezmieniony po ostatnich korektach.

Porównano pięć bloków z IT-13: def:metric-outer-21 (identyczny), lem:metric-outer-borel-21 (odsyłacz do kanonicznego twierdzenia Carathéodory'ego), thm:compact-riesz-21 (uzupełnione oszacowanie regularności), lem:exhaustion-21 (odsyłacz do GT-09), thm:riesz-c0-positive-21 (doprecyzowana dziedzina rzeczywista). Nie stwierdzono utraty treści. Sprawdzono konstrukcję miary zewnętrznej bez założenia sigma-skończoności, separację warstw w metrycznym dowodzie mierzalności, grupowanie powtarzających się indeksów podziału jedności, sumy progowe z progami ostrymi, wyczerpanie, normę funkcjonału dodatniego, addytywność obwiedni M i jednoznaczność reprezentacji zespolonej. Brak nowej usterki wymagającej edycji źródła.

Walidacja statyczna aktualnego źródła: 27 unikatowych etykiet, 63 ref/eqref bez brakujących celów, 18 atlasref zgodnych z docelowymi rozdziałami, 14 dowodów, wszystkie środowiska domknięte. 14/14 indeksowanych twierdzeń, definicji, lematów i wniosków ma poprawne wpisy indeksu.

Niezależne obliczenia wykonane w JavaScript z dokładną arytmetyką małych liczb całkowitych: 123930/123930 konfiguracji sum progowych (funkcje na czterech punktach o wartościach 0,...,3, masy 0,...,2, N=1,...,6, z pominięciem funkcji identycznie zerowej), w tym równość różnicy sum po przemnożeniu przez N/M z masą zbioru f>0; 82701/82701 konfiguracji grupowania czterech składników podziału jedności z trzema możliwymi indeksami, z kontrolą sumy i dominacji po pomnożeniu przez wspólny mianownik. Razem 206631 konfiguracji bez niezgodności. Nie są to dowody ogólnych twierdzeń ani uruchomienie suity Python.

CI na 96efc1d: ME-21 #45999839153 pending, globalny ME #45999839187 queued w chwili odczytu. PDF i odbiór techniczny pozostają niepotwierdzone. Następny krok: drugi czysty audyt, następnie audyt kontrolny.
