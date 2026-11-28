# ME-32 — kontrola migracji CAL-12
Data: 2026-11-27. Gałąź: biblioteka-matematyczna-iteracja-6.

- CAL-12: blob 3ff2bf2b5d53837f40dfb4e54808cdfb9ccd15bd, 941 wierszy, 29 środowisk merytorycznych, 23 etykiety.
- ME-32: blob 30bd3b95532d910c2ce8b30f9e55c80df9c61a33, 1201 wierszy, 33 środowiska merytoryczne, 28 etykiet.
- Porównanie typów i tytułów środowisk: wszystkie 29 pozycji źródłowych ma odpowiedniki. Wszystkie 23 etykiety źródłowe zachowano. Kontrola strukturalna nie jest automatycznym dowodem równoważności treści.
- Poprzednie audyty uzupełniły dowody dla miary nieskończonej, gęstości w L1, warunków jednoznaczności, otoczki mierzalnej i porównania z miarą Radona.
- CI 46022158572: 241/241 testów, 11/11 ME-32. PDF skompilowany, ale kontrola indeksu zgłosiła rozbieżność strony lematu 23.7 (177/178). CI 46022691553 potwierdziło ten sam problem, regresje zaliczone.
- Próba korekty: pakiet needspace w preambule (2f862b2), lokalna rezerwacja miejsca przed lematem 23.7 (b717890). CI 46030318773 oczekuje; nie zmieniono kryteriów kontroli.
- Status: pokrycie strukturalne potwierdzone; usunięcie CAL-12 wstrzymane do potwierdzenia aktualnej kompilacji, indeksu i kontroli zależności pozostałych rozdziałów CAL.
