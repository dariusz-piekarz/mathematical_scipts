# Geometria i topologia różniczkowa — zasady projektu

## Źródło

- Plikiem głównym jest `geometria_i_topologia_rozniczkowa.tex`; ustala kolejność części przez `\input`. Treść edytuj w odpowiednim pliku `tex/rozdzialy/`, a ustawienia wspólne w `tex/preambula.tex`.
- `geometria_i_topologia_rozniczkowa.pdf` jest ostatnim sprawdzonym składem, a nie osobnym źródłem treści.
- Skrypt ma obecnie 33 numerowane rozdziały i dwa dodatki. Pozostaje jednym dokumentem PDF, ale zgodnie z nowszą prośbą użytkownika z 5 października 2026 źródła rozdziałów są w osobnych plikach. Korzystaj z istniejących etykiet i odsyłaczy; nie zmieniaj ich przy przenoszeniu treści. Nie dodawaj zadań.
- `tex/wstep.tex` zawiera spis treści i mapę książki, `tex/dodatki/` dodatki, a `tex/indeks.tex` polecenia składu indeksu. Nie kompiluj rozdziałów osobno; kompiluj plik główny z katalogu głównego repozytorium.

## Cel i sposób pisania

- Tekst jest po polsku i ma prowadzić od podstaw geometrii oraz topologii różniczkowej do teorii Morse'a, twierdzeń Smale'a i chirurgii rozmaitości.
- Każda nowa definicja powinna mieć intuicję, precyzyjne założenia i przykład. Dowody rozpisuj krok po kroku; wyjaśniaj przejścia algebraiczne i geometryczne.
- Jeżeli używasz głębokiego twierdzenia lub lematu, podaj jego dokładne założenia i wskaż źródło. Nie nazywaj szkicu pełnym dowodem.
- Unikaj powielania definicji już wprowadzonych; odsyłaj do wcześniejszych miejsc.

## Terminologia

- „Mapa” oznacza `chart`; `map` to „odwzorowanie”.
- Stosuj „inkluzja” dla odwzorowania włączającego, „funkcja pierwotna” zamiast samego „pierwotna”.
- W homologiach operator brzegu to `\partial`; `d` jest dla różniczki w kohomologiach i formach.
- „Kochainy” pozostają tłumaczeniem `cochains`; nie zamieniaj ich na „kołańcuchy”.
- Angielskie `germ` funkcji lub odwzorowania tłumacz jako „kiełek”.
- Dla $A\in\{\Z,\Q,\R,\H,\C\}$ zapis $A_*$ oznacza $A\setminus\{0\}$.
  Gdy chodzi o zbiór liczb niezerowych, pisz $A_*$ zamiast $A^\times$;
  $A^\times$ zachowaj dla grupy elementów odwracalnych, na przykład
  $\Z^\times=\{-1,1\}\neq\Z_*$.
- Rozróżniaj zanurzenie i osadzenie zgodnie z ich definicjami w skrypcie.

## Rysunki i kontrola

- Rysunki sfer i torusów utrzymuj w jasnej, niebieskiej stylistyce sfery z rozdziału 1. Geometria i położenie oznaczonych punktów muszą zgadzać się z tekstem.
- Nie zasłaniaj etykiet siatką ani powierzchnią; sprawdzaj szczególnie rysunki TikZ i PGFPlots po złożeniu PDF.
- Po zmianach kompiluj `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/sklad geometria_i_topologia_rozniczkowa.tex`. Sprawdź błędy, brakujące odsyłacze, indeks oraz strony z nowymi rysunkami. Instrukcja w `README.md` obejmuje również Perla z PortableGit i kompilację bez `latexmk`.

## Dokumentowanie pracy

- Zwykła iteracja matematyczna obejmuje jeden rozdział, chyba że autor
  wyznaczy szerszy etap. Zmiany i ich uzasadnienia
  dopisuj do `PRZEGLAD.md`; aktualny zakres, pokrycie i kolejkę aktualizuj wyłącznie
  w `PLAN_DZIALANIA.md`. Nie twórz równoległych list tych samych zadań.
- Po sprawdzeniu składu aktualizuj wspólny PDF, zatwierdzaj ukończony etap
  na gałęzi przeglądu i wypychaj go na GitHuba. Przed pracą pobierz zmiany
  współautora.
- Deklarację autora o ukończeniu rozbudowy odróżniaj od przeprowadzonego audytu.
  Szczegóły budowania i organizacji źródeł są w `README.md`.
