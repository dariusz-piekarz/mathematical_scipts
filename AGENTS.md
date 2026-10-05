# Geometria i topologia różniczkowa — zasady projektu

## Źródło

- Plikiem głównym jest `geometria_i_topologia_rozniczkowa.tex`; ustala kolejność części przez `\input`. Treść edytuj w odpowiednim pliku `tex/rozdzialy/`, a ustawienia wspólne w `tex/preambula.tex`.
- `geometria_i_topologia_rozniczkowa.pdf` jest ostatnim sprawdzonym składem, a nie osobnym źródłem treści.
- Skrypt ma obecnie 27 numerowanych rozdziałów i dodatek. Pozostaje jednym dokumentem PDF, ale zgodnie z nowszą prośbą użytkownika z 5 października 2026 źródła rozdziałów są w osobnych plikach. Korzystaj z istniejących etykiet i odsyłaczy; nie zmieniaj ich przy przenoszeniu treści. Nie dodawaj zadań.
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
- Rozróżniaj zanurzenie i osadzenie zgodnie z ich definicjami w skrypcie.

## Rysunki i kontrola

- Rysunki sfer i torusów utrzymuj w jasnej, niebieskiej stylistyce sfery z rozdziału 1. Geometria i położenie oznaczonych punktów muszą zgadzać się z tekstem.
- Nie zasłaniaj etykiet siatką ani powierzchnią; sprawdzaj szczególnie rysunki TikZ i PGFPlots po złożeniu PDF.
- Po zmianach kompiluj `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/sklad geometria_i_topologia_rozniczkowa.tex`. Sprawdź błędy, brakujące odsyłacze, indeks oraz strony z nowymi rysunkami. Instrukcja w `README.md` obejmuje również Perla z PortableGit i kompilację bez `latexmk`.

## Stan prac

- Rozdział 5 zbiera grupy, pierścienie, moduły i iloczyn tensorowy modułów; rozdział 6 rozpoczyna algebrę homologiczną.
- Rozdziały 22–24 obejmują chirurgię geometryczną, przeszkodę Walla i ciąg dokładny chirurgii.
- Rozdziały 25–27 obejmują twierdzenie Poincarégo poza wymiarem 4, sfery Milnora oraz teorię Cherna–Weila i wzór Cherna–Gaussa–Bonneta.
- Aktualne zadania i stan weryfikacji są w `PLAN_DZIALANIA.md`.
