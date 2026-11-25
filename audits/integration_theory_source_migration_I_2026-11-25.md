# Teoria całki — migracja źródłowa I (01–02)

Decyzja: przed dalszymi audytami zastępujemy pokrywające się treści istniejącym materiałem z AM1, TM oraz AF. Audyty i rozszerzenia nastąpią po migracji.

Źródła na commicie 1b6a00345412c6734b61791b6c1a62e03081b3fa:
- chapters/pl/mathematical_analysis_i/29-calka-riemanna.tex (definicje, kryteria, równoważność, własności, przykłady i podstawowe twierdzenie rachunku całkowego);
- chapters/pl/mathematical_analysis_i/19-funkcje-patologiczne.tex (funkcja Thomae'a z rysunkiem i dowodem granicy przekłutej);
- chapters/pl/measure_theory/08-twierdzenia-graniczne-dla-calki-lebesguea.tex (kryterium Lebesgue'a).

Zachowano oryginalne etykiety importowanych wyników. Zastąpiono odsyłacze do nieimportowanych rozdziałów AM1 nazwami użytych klasycznych twierdzeń, dopisano lokalne uzasadnienie jednoznaczności funkcji pierwotnej. Zachowano swoiste treści: całkę Darboux funkcji Thomae'a, obliczenie z sum dolnych/górnych, ograniczoność funkcji Riemanna, zbieżność jednostajną i kratę wektorową, przykład braku zupełności. Włączono TikZ i makra potrzebne w importowanych fragmentach.

Kontrole wykonane przed zapisem: zgodność par środowisk, unikalność 25 etykiet i rozwiązywalność 15 lokalnych odsyłaczy w plikach 01–02. Nie wykonano kompilacji ani pełnego audytu matematycznego; nie ogłaszać stabilizacji. Kolejny etap migracji: rozdz. 04 i 07–08 wobec AM1-36, rozdz. 10–14 wobec TM i AF; zachować szczególne wyniki skryptu oraz rozdzielić zakresy.
