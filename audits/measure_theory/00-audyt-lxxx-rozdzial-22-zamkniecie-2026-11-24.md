# Audyt LXXX (80) — rozdział 22: zamknięcie stabilizacji

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Weryfikowana wersja
Commit fe6c764d7e49ddbc5897bfdd891c09e18fe49208; aktualny blob rozdziału 22: 408b901530bd30243665f4f7f577d195b0158877. Potwierdzono zgodność aktualnego bloba z wersją zweryfikowaną po audycie LXXIX.

## CI i rzeczywiste logi
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289602503 zakończony success, oba statusy regressions i pdf success. Poprzedni przebieg 45289414520 również success.
- Job 138095369079: 10 testów rozdziału oraz 4 testy integralności tomu, wszystkie zaliczone; sprawdzono rzeczywiste logi.
- Job 138095368625: pełny tom 260 stron, 1907941 bajtów; samodzielny rozdział 7 stron, 283400 bajtów; import sześciu zewnętrznych etykiet przy 23 lokalnych; odsyłacze rozwiązane.
- Kontrole terminologiczne 45289602515 i aplikacji 45289602654: success.

## Kontrola artefaktu i składu
Pobrano faktyczny ZIP artefaktu 14874510112 z weryfikowanego przebiegu. Rozmiar 3872480 bajtów, SHA256 60e6fecc5eabadc51b45299d50a70536363e9ce5d9de732a0af1fbce9190c074, zgodny z metadanymi GitHub. Rozpakowano oba PDF, oba logi i siedem obrazów podglądu. Niezależnie odczytano liczbę stron i wyrenderowano wszystkie siedem stron izolowanego rozdziału.
- Strony 1–2: tytuł, definicje, ucieczka masy, twierdzenie Portmanteau i dowód; wzory i lista poprawnie rozmieszczone. Teza przechodzi na kolejną stronę bez ucięcia.
- Strony 3–4: porównanie rodzajów zbieżności, definicja TV, ciasność, lematy o aproksymacji, zwartości i włożeniu; brak nachodzenia wzorów.
- Strony 5–6: dowody Prochorowa i oszacowania ciasności; brak obciętych wzorów, poprawne odsyłacze i numeracja.
- Strona 7: kontrprzykład momentów, brak ucieczki masy i przykłady końcowe; brak usterek składu.
- Odczyt tekstu: 0 wystąpień nierozwiązanych odsyłaczy oznaczonych ?? na wszystkich 7 stronach.
- Log samodzielnego rozdziału: 0 Overfull, 0 Underfull, brak końcowego ostrzeżenia o nierozwiązanych odsyłaczach. Log tomu: 0 Overfull, 14 Underfull; ostrzeżenia te nie stanowią błędu kompilacji, nie poświadczono oględzin wszystkich 260 stron. Początek rozdziału 22 na fizycznej stronie 163 pełnego tomu.

## Werdykt
Rozdział 22 ustabilizowany w zakresie dotychczasowego audytu matematycznego, regresji, integralności i składu samodzielnego PDF. Audyty LXXVII–LXXX zakończone. W poprzednich iteracjach poprawiono dowody Portmanteau, Prochorowa, zwartości miar na przestrzeni zwartej i ucieczki masy; wykonano dodatkowo 260775 dokładnych kontroli skończonych, które nie zastępują dowodów. Nie zmieniano źródła rozdziału w tej iteracji.

Stan: 22/31 rozdziałów ustabilizowanych. Następna iteracja LXXXI: pierwszy szczegółowy audyt rozdziału 23 — miara Haara na grupach lokalnie zwartych.
