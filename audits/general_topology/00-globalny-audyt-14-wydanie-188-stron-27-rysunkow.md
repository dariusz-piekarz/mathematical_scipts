# Topologia ogólna — globalny audyt 14: pełne wydanie, 27 ilustracji, rewalidacja 03–04

**Data:** 2026-11-22.
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Przedmiot:** rzeczywisty PDF (nie sam kod TikZ), porównanie jego wersji ze źródłami i powtórne oględziny ostatnich stron rozdziałów 03–04.

## Pochodzenie kontrolowanego artefaktu

- GitHub Actions: [przebieg 45068776546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068776546), **completed / success**.
- Commit wykonania: \`0fd629c07b0366c238720db3d4253f2ec7103122\`.
- Artefakt: [general-topology-ch01-ch26, ID 14771719456](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068776546/artifacts/14771719456).
- Zawartość ZIP: pełna książka \`general_topology.pdf\` i 25 samodzielnych PDF-ów rozdziałów 02–26 wraz z logami.
- **Bieżące źródła:** porównano wszystkie 26 ścieżek \`chapters/pl/general_topology/*.tex\` między drzewem Git wskazanego commitu a stanem tej samej gałęzi podczas audytu. **Brak różnic blobów**. To ważne: pozytywny wynik dotyczy także bieżącej treści rozdziałów, a nie innej ich wersji.

## Kontrola pełnego wydania

Pełne wydanie liczy **188 stron** (poprzedni, przedkorekcyjny PDF: 190 stron). Pliki rozdziałów 03 i 04 liczą obecnie po **7 stron** (poprzednio po 8). Render i oględziny ostatnich stron obu samodzielnych wydań potwierdzają, że:

1. Ostatnia strona rozdziału 03 zawiera końcowe stwierdzenie o zachowaniu operacji zbiorowych przez homeomorfizmy, definicję i kryterium zanurzenia, przykład oraz sekcję 3.7. Podsumowanie nie znalazło się samo na dodatkowej stronie; nie nachodzi na numer strony.
2. Ostatnia strona rozdziału 04 zawiera twierdzenia o odwzorowaniu ilorazowym, trzy przykłady i sekcję 4.6 z porównaniem własności uniwersalnych. Nie pozostała odizolowana ostatnia uwaga; tekst nie koliduje ze stopką.
3. Odczyt tekstu ze wszystkich **188 stron** nie ujawnia strony zawierającej wyłącznie paginację. Najkrótsza strona tytułowa jest zamierzona; strona 7 jest końcówką spisu treści, nie pustą stroną.
4. W pełnym logu i logach samodzielnych PDF-ów nie stwierdzono ostrzeżeń \`Overfull\`, \`Underfull\`, \`Missing character\`, \`LaTeX Warning\`, \`Undefined control sequence\` ani \`Fatal error\`.

## Oględziny wszystkich 27 ilustracji

Za pomocą rzeczywistego renderu stron skontrolowano wszystkie ilustracje (w tym dwie z rozdziału 01, dla którego w archiwum nie ma samodzielnego PDF). Każdą ilustrację odnaleziono w pełnym PDF po podpisie \`Rysunek n.m\`, sporządzono zbliżenie obszaru rysunku i podpisu oraz przejrzano plansze zbiorcze. Numery stron poniżej dotyczą **pełnego wydania 188-stronicowego**.

| Rozdział | Numery rysunków | Strony pełnego PDF |
|---:|---|---|
| 01 | 1.1, 1.2 | 9, 15 |
| 02 | 2.1 | 20 |
| 04 | 4.1, 4.2 | 33, 34 |
| 05 | 5.1–5.5 | 39, 41, 43, 46, 48 |
| 06 | 6.1, 6.2 | 50, 52 |
| 07 | 7.1, 7.2 | 59, 64 |
| 08 | 8.1, 8.2 | 69, 73 |
| 09 | 9.1, 9.2 | 79, 81 |
| 10 | 10.1 | 86 |
| 11 | 11.1 | 92 |
| 12 | 12.1 | 96 |
| 21 | 21.1 | 144 |
| 22 | 22.1 | 150 |
| 23 | 23.1 | 160 |
| 24 | 24.1 | 170 |
| 25 | 25.1 | 180 |
| 26 | 26.1 | 186 |

**Łącznie 27 ilustracji w 17 rozdziałach.** W pozostałych dziewięciu rozdziałach nie występują ilustracje tego typu.

W skontrolowanych renderach nie stwierdzono oczywistych kolizji napisów, przesłonięcia elementów graficznych, uciętych oznaczeń, podpisów przecinających rysunki ani wyjścia ilustracji poza szerokość tekstu. Szczególnie sprawdzono rysunek 12.1: pas bliskości dla \`|x−y|<0,8\` na kwadracie \`[0,5]²\` odpowiada współrzędnym i podpisowi; przerywane granice pasa prawidłowo nie należą do relacji.

**Ograniczenie metodologiczne:** wykonano wizualny przegląd wszystkich 27 rysunków oraz szczegółowy przegląd ostatnich stron 03–04 i logów. Nie oznacza to drobiazgowego, linia-po-linii audytu każdego z 188 łamów tekstu i wszystkich 26 rozdziałów.

## Ważna uwaga o identyfikatorze źródła rozdziału 03

Raport \`00-globalny-audyt-13-korekta-03-04-iteracja-02.md\` podawał dla rozdziału 03 blob \`021f4f843b26e90dca57b3e38b33e95cd0c03a5b\`.
W sprawdzonym PDF i obecnym drzewie źródło 03 ma już blob \`b571753b5ab9a8777424fc32f6c4a54a4048af77\`. Różnice dotyczą końcowego przykładu, skrócenia redakcyjnego podsumowania i zmiany \`\enlargethispage{4\baselineskip}\` na \`\enlargethispage{1\baselineskip}\` — bez zmiany dowodów i hipotez ich twierdzeń. Obejrzano już *nowy* PDF; korekta układu okazała się skuteczna.
Źródło rozdziału 04 w tym samym PDF ma blob \`a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081\`.

Nie należy bez sprawdzenia przenosić liczby czystych kontroli matematycznych z bloba 03 cytowanego przez raport 13 na jego nową wersję. **Wizualna rewalidacja jest zamknięta, ale rygor dodatkowego audytu potwierdzającego na bieżącym blobie 03 pozostaje osobną czynnością.**

## Wynik i kontynuacja

**PASS — 27/27 rysunków, pełny PDF 188 stron, brak wymienionych ostrzeżeń logów, naprawione końcowe strony 03–04.** Nie stwierdzono nowej usterki wizualnej wymagającej poprawki TikZ. Nie zmieniano w tej iteracji źródeł LaTeX.

Do wykonania pozostaje niezależna, dowód-po-dowodzie kontrola rozdziałów zaczynając od 13 oraz ewentualna finalna kontrola matematyczno-redakcyjna najnowszego bloba 03. Zielone CI i obecny audyt wydawniczy nie zastępują tych kontroli.
