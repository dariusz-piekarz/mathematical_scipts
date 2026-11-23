# Teoria miary / Miara i całka — rozdział 04, audyt I (iteracja globalna XVII)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Jedyny audytowany rozdział:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.
Rozdziały 01–03 mają wcześniej potwierdzoną stabilność; R05–R31 nie były audytowane ani edytowane w tej iteracji.

## Stan wejściowy

Odczytano aktualny stan gałęzi przez porównanie z poprzednim commitem audytu, raporty XIV–XVI, `books/pl/measure_theory.tex`, `AGENTS.md`, `docs/pl/standardy_terminologiczne.md` i cały tekst R04. Raport XVI potwierdza stabilność R03 po zakończeniu 2/2 zadań CI. Blob R04 przed zmianą: `86a804bff434ccbd96e8a4a448befc8df70cbb75`.

## Pierwszy przegląd matematyczny R04

Przejrzano konstrukcję objętości na pierścieniu ograniczonych sum prostopadłościanów, argument siatkowy, lemat o pokryciach, premiarę na ograniczonym prostopadłościanie, konstrukcję miary zewnętrznej Lebesgue'a, mierzalność w sensie Carathéodory'ego, jednoznaczność miary borelowskiej, niezmienniczość względem translacji i skali, regularność zewnętrzną i wewnętrzną, aproksymacje borelowskie, zbiory Cantora i Smitha–Volterry–Cantora, funkcję Cantora oraz konstrukcję Vitaliego.

**Wykryta luka brzegowa:** w dowodzie elementarnej nierówności dla skończonego pokrycia zwartego prostopadłościanu `K=∏[α_j,β_j]` autor bez jawnego założenia dodatnich długości boków wprowadza `P_η=∏[α_j+η,β_j−η)` i przechodzi z `η↓0`. Dla boków zdegenerowanych ten fragment nie jest poprawnym uzasadnieniem, choć sama nierówność pozostaje prawdziwa (objętość geometryczna wynosi zero). Poprawiono dowód, oddzielając przypadek `α_j=β_j` i wyraźnie przyjmując dodatnie długości w części siatkowej. Nie zmieniono etykiet, twierdzeń ani zakresu rozdziału.

**Poprawka źródła:** commit `a7098bebb00e3fe9a2c7aab53dcaec347119c5d2`; blob po zmianie `77e4ad8551f55a2ff579aa171761ccdd01aaa918`. Ponownie pobrano plik z GitHub i potwierdzono nowy fragment oraz SHA.

## Ponowny niezależny przegląd po poprawce

Ponownie przeanalizowano lemat o pokryciach, tym razem od definicji skończonej siatki: dla zdegenerowanego K nierówność jest trywialna; dla dodatnich boków istnieje η>0 pozwalające utworzyć P_η; każda komórka siatki z wnętrzem przypada na jedno otwarte O_i, jej domknięcie mieści się w domknięciu O_i; rozszerzenie do H_i^(γ) i granice γ↓0, η↓0 dają wymaganą nierówność. Następnie sprawdzono użycie tego lematu w dowodzie premiary i w globalnej konstrukcji Lebesgue'a; nie wymagają dodatkowej zmiany.

Sprawdzono też osobno przypadki miary nieskończonej w regularności, kierunki nierówności w konstrukcji Carathéodory'ego, użycie zupełności przy zbiorach zerowych, przeliczalną addytywność w argumencie Vitaliego i zgodność wzorów dla długości przedziałów w konstrukcji zbioru Smitha–Volterry–Cantora. Nie stwierdzono w tym ponownym przeglądzie kolejnej udowodnionej usterki. Jest to kontrola ręczna; **nie** jest jeszcze certyfikatem pełnej stabilności.

## Kontrole techniczne i ograniczenia

- R04 jest włączony przez `books/pl/measure_theory.tex`; istniejący rozdział R03 dostarcza konstrukcji Carathéodory'ego, R02 dostarcza własności miar.
- W źródle nie stwierdzono zastosowania alternatywnego symbolu funkcji charakterystycznej ani nazwy „zbieżność zdominowana”. Nie zmieniono żadnych etykiet.
- R04 zawiera rysunek TikZ pierwszych czterech etapów zbioru Cantora. Skontrolowano jego strukturę w źródle, ale **nie wykonano nowej wizualnej inspekcji wyrenderowanego PDF**.
- **Nie uruchomiono w tej iteracji kompilacji LaTeX, testów automatycznych ani CI**; nie przypisuje się im wyniku PASS. Pozostają otwartą częścią audytu technicznego.
- Nie wprowadzono dodatkowych twierdzeń ani przykładów bez zatwierdzenia.

## Status i następny krok

**R04: W TRAKCIE STABILIZACJI — NIESTABILNY / NIEZATWIERDZONY.**
Jedna rzeczywista poprawka uzasadnienia i ponowna kontrola jej poprawności zostały wykonane. Nadal wymagane są pełny niezależny audyt całego R04 po poprawce, kontrola odsyłaczy i wszystkich etykiet, kompilacja i inspekcja PDF z rysunkiem Cantora, oraz dodatkowy czysty audyt po ostatniej poprawce. Dopiero po ich zakończeniu można formalnie zatwierdzić stabilność.

**Następna iteracja:** wyłącznie R04, audyt II. Nie przechodzić do R05.
