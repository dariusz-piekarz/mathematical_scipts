# Geometria algebraiczna — cykl kontrolny po zamknięciu ALG-00–10 (2026-11-22)

## Stan początkowy
Odczytano bieżący manifest `catalog/books.json`, README, standard `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, rejestr `STATUS.md` i końcowe raporty ALG-07/IX, ALG-08/V, ALG-09/V, ALG-10/V–VI. Według najnowszych raportów **ALG-00–ALG-10 są zamknięte**; stary nagłówek STATUS.md błędnie wskazywał ALG-07/III. Cykl kontrolny ograniczono do **jednego** rozdziału ALG-10, bez tworzenia ALG-11.

## Ustalenie i poprawka
W przykładzie normalizacji kubiki w ALG-10, linia około 835, wykryto błąd gramatyczny `w mapie afinicznym wielomian`. Poprawiono na `w mapie afinicznej wielomian` w kanonicznym rozdziale oraz w historycznym monolicie `sources/pl/geometria_algebraiczna(1).tex`, bez zmian wzorów, hipotez, etykiet i odsyłaczy. Poprzedni blob rozdziału: `348d3762fa6cb197e0f4578504170e0fc7f107c9`; nowy blob: `a1b568aeff8e4d5a70731c4799e479c19475b56e`. Commity: `613db9658bfdbb979db0bbee2276981fc8409532` i `36a62c15b39b02c2b1ec83ed2ba26e59c5e22afd`.

## Kontrole wykonane i ograniczenia
Odczytano całe 983 wiersze źródła ALG-10 i poddano ponownemu przeglądowi fragmenty dotyczące dualności Poincarégo, przecięć, powierzchni stopnia d, indeksu Hodge'a, liczb Hodge'a, Noethera, wygładzenia węzła i normalizacji kubiki. Po korekcie: 27 etykiet bez duplikatów, 16 wystąpień odsyłaczy (część do innych rozdziałów/modułów), 75 otwarć i 75 zamknięć środowisk, bez rozbieżności liczności. Jest to **kontrola strukturalna, nie dowód poprawności wszystkich odsyłaczy**. Nie ukończono dwóch nowych niezależnych pełnych audytów, lokalnych dwóch kompilacji ani oględzin aktualnego PDF: środowisko lokalne nie rozwiązuje hosta github.com, a złącze GitHub nie dostarcza binarnego PDF. Wyniki CI 45067808109, 18/18 regresji i PDF 184 stron pochodzą z **poprzedniego** bloba, więc nie są przypisywane poprawionej wersji. Trwające równoległe CI wymaga osobnego potwierdzenia.

## Status
ALG-00–09: stabilne według osobnych raportów końcowych. ALG-10: **ponownie otwarty do kontroli regresyjnej** po korekcie źródła; licznik pełnych czystych kontroli po korekcie **0**; dodatkowy końcowy audyt nowego bloba **niewykonany**. Nie deklaruje się nowego PASS. Następny przebieg powinien pozostać przy ALG-10, sprawdzić CI i PDF nowego bloba, wykonać pełną krytyczną kontrolę oraz oddzielny końcowy audyt.
