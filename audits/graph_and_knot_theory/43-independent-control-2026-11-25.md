# TG-43 — kontrola niezależna, 2026-11-25

Zakres: rozdział 43 (ekspandery), stan źródła `903636354f694c0a54ba7d15a6379a88178097c7`, test regresyjny `fc431736fcdba8ff4118cdec250eec4c8ad40275`.

## Wyniki rzeczywiście wykonanych obliczeń niezależnych

- Enumeracja wszystkich 33 866 grafów prostych etykietowanych na 2–6 wierzchołkach; do kontroli spektralnej wybrano 193 grafy regularne o dodatnim stopniu oraz grafy nieregularne bez izolowanych wierzchołków na co najwyżej 5 wierzchołkach (w tym 752 spójne).
- 20 603 dopuszczalne przekroje (dokładne ilorazy Fraction); wartości własne przez numpy.linalg.eigvalsh. Nierówności Cheegera, zakres widma, zależność luki od spójności i porównanie ekspansji: bez naruszeń w granicy tolerancji numerycznej 1e-9.
- 15 184 par zbiorów wierzchołków: lemat o mieszaniu krawędzi (tolerancja 1e-8).
- 34 254 kontrole rozkładu spaceru leniwego dla czasów 0–8 oraz stacjonarności i równowagi szczegółowej: bez naruszeń (tolerancja 1e-8).
- TG43-DIA-01: niezależne BFS ze wszystkich wierzchołków dla h=2,...,6. Liczności 14, 30, 62, 126, 254; średnice dokładnie 5, 7, 9, 11, 13; przekrój połówkowy ma jedną krawędź. Dla n=14 pełna enumeracja przekrojów potwierdza przewodność 1/21. Dla większych n dokładna wartość wynika z dowodu w rozdziale.

## Integracja

Wszystkie cztery zewnętrzne etykiety TG-43 występują w źródłach: ch:tg-random-graphs, ch:tg-podstawy, rem:tg-laplacian-conventions, ch:tg-laplacian. Lista 44 plików w książce jest identyczna z catalog/books.json.

## Ograniczenia

Powyższy przebieg jest niezależnym testem numeryczno-kombinatorycznym, nie uruchomieniem pełnego repozytoryjnego zestawu Python/CI. Lokalny git ls-remote nie działa (DNS); zbiorcze pobieranie wszystkich 44 źródeł przekroczyło limit wywołań. Nie skompilowano ani nie obejrzano PDF. Pełna stabilizacja techniczna pozostaje otwarta. Nie zgłasza się wyniku PASS dla CI ani formalizacji Lean.
