# Topologia ogólna — rozdział 10, audyt 4

- **Rozdział:** Metryzowalność przestrzeni topologicznych.
- **Wersja źródła:** 0.2 (bez zmian po audycie 3).
- **Status:** **drugi czysty audyt z rzędu, 2/2 — rozdział stabilny**.
- **Źródło:** `chapters/pl/general_topology/10-metryzowalnosc.tex` (768 wierszy).
- **SHA-256:** `ad5de242b4dd63fdadea8eb5228e910e774147396f06dfe04611b1b150a4f088`.

## Ponowny audyt matematyczny

Przeczytano niezależnie wszystkie definicje, stwierdzenia, lematy, twierdzenia, wnioski, przykłady i dowody, w tym:

1. Własności pseudometryk i baz kul; metryzowalność a T3 i pierwszy aksjomat przeliczalności; nieprzeliczalne przestrzenie dyskretne i obowiązkowa obecność singletonów w każdej bazie.
2. Ograniczanie metryki przez `min(1,d)`, zgodność metryk i metryzowalność podprzestrzeni oraz przenoszenie metryki przez homeomorfizm.
3. Dowód regularność + Lindelöf → normalność (konstrukcja przeliczalnych rodzin i rozłącznych otwartych otoczeń), także dla pustych zbiorów domkniętych.
4. Pięć etapów twierdzenia Urysohna o metryzowalności: zwężanie par bazowych, funkcje Urysohna, rozdzielanie punktów, nierówność trójkąta, obie inkluzje topologii; zweryfikowano poprawkę z audytu 1 dotyczącą otwartości *całej* kuli, nie wyłącznie otoczenia jej środka.
5. Metrykę kostki Hilberta, zgodność z topologią iloczynu, zanurzenie przez funkcje Urysohna, przeliczalne iloczyny i cylindry bez ograniczeń współrzędnych.
6. Kryterium metryzowalności dla zwartych przestrzeni Hausdorffa, w tym wybór skończonych podpokryć i zbudowanie przeliczalnego zbioru gęstego.
7. Regularną, lecz niemetryzowalną prostą Sorgenfreya, brak pierwszego aksjomatu przeliczalności w nieprzeliczalnej kostce, niemetryzowalny iloraz dający prostą z dwoma początkami i przykład metryki zgodnej, ale niezupełnej.

Nie stwierdzono wymagających poprawek problemów matematycznych, luk uzasadnienia, niejawnych hipotez, wadliwych kontrprzykładów ani niepoprawnych odsyłaczy. W szczególności żadnych nowych twierdzeń nie dodawano.

## Niezależna kontrola techniczna

- `bash tools/validate_general_topology_ch10.sh`: **PASS**, log `/mnt/data/topologia_ogolna_ch10_audit04_validation.log`.
- Testy rozdziałów 01–10: **PASS**; 390 topologii skończonych, 7 modeli metryk rozdzielających, 1295 trójek metrycznych, 551 880 trójek dla metryk iloczynowych.
- LaTeX: 393 unikatowe etykiety i 104 rozwiązane odsyłacze, terminologia zgodna z regułą globalną.
- Pełna książka: **88 stron**, PDF samodzielnego rozdziału 10: **8 stron**.
- Dwa logi LaTeX bez `Overfull`, `Underfull`, `LaTeX Warning`, `Missing character`, `Undefined control sequence`, `Fatal error`.
- Render: wszystkie osiem stron obejrzane; diagram konstrukcji Urysohna, długie wzory, bloki dowodów i zakończenie rozdziału są czytelne. Nie stwierdzono nakładania ani obcięcia treści.
- Suma SHA-256 jest identyczna z audytem 3. **Nie wprowadzono zmian w kodzie źródłowym rozdziału.**

## Decyzja

**Audyt 4 jest czysty. Dwa kolejne czyste audyty (3 i 4) dają 2/2; rozdział 10 jest stabilny** i może zostać zintegrowany z bieżącą gałęzią GitHuba z aktualizacją książki, katalogu, testów, workflow i raportów 1–4 oraz weryfikacją CI.
