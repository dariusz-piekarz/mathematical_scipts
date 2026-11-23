# Miara i całka — rozdział 04, audyt VI (iteracja globalna XXII)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Jedyny rozdział audytowany merytorycznie:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`.

## Stan wejściowy i zakres

Sprawdzono najnowsze zmiany gałęzi od raportu XXI (commit `fced88ada97fe2d1cb48c5b02e5aeef6b3ce6196`): późniejsze commity dotyczyły innych części repozytorium; R04 był niezmieniony (blob `84b6300e8939fee9874ff4872862e7604dd4c1aa`). Raport XXII nie istniał. Odczytano też `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, dotychczasowy raport XXI, R04 i workflow `.github/workflows/measure-theory-ch04.yml`. Ponownie skontrolowano wybrane trudniejsze argumenty o mierzalności Carathéodory'ego, regularności, konstrukcjach Cantora i Vitaliego. W tej iteracji nie edytowano pozostałych rozdziałów.

## Wykazana luka brzegowa — przykład wykresu Lipschitzowskiego

W przykładzie `ex:lipschitz-graph-null` pierwotne sformułowanie określało funkcję `f:[a,b]\to\mathbb R` bez jawnych założeń na `a,b,L`, zaś dowód rozpoczynał oszacowanie od `Dla a<b` i nie rozstrzygał przypadku `a=b`, chociaż odcinek `[a,a]` jest sensowną dziedziną funkcji. Była to **niekompletność dowodu przy warunkach brzegowych**, nie fałszywa teza.

Poprawiono **minimalnie**, bez rozszerzania tematu:
- jawnie wprowadzono `a,b\in\mathbb R`, `a\le b`, `L\ge0`, oraz kwantyfikator `x,y\in[a,b]`;
- dla `a=b` stwierdzono, że wykres `\Gamma_f` jest singletonem, więc jest zerowy na mocy wcześniej wykazanego `lem:hyperplane-null` (dla `d=2`);
- dla `a<b` pozostawiono niezmieniony wcześniejszy dowód oszacowania przez prostopadłościany.

**Commit źródła:** `08e23fc2db201ac941890bcd645361d453ae59bc`; nowy blob R04 **`ce0105f63aa4da494cf5f2f5e9e2b26fc6389fd4`**. Zweryfikowano pełny odczyt po zapisie. Żadnych etykiet nie zmieniono.

## Rozszerzenie testów regresyjnych

- `tools/test_measure_theory_ch04_geometry.py`, commit `ace3ffc4c4dcb6f57f5a8c2f08f10a6ec18ee585`: sprawdzanie wymiernych oszacowań pokryć dla grafu stałej funkcji (`L=0`) i dla przedziału `a=b` (singleton), oprócz istniejących testów dla dodatniego `L`.
- `tools/test_measure_theory_ch04_source.py`, commit `f2e5f66ba7049724dc4c6521f0e10c5f90e957a6`: statyczne zabezpieczenie przed usunięciem wymaganych jawnych założeń i argumentu singletonowego.
- Ponowny odczyt GitHub potwierdził nowe bloby i zawartość obu plików. W lokalnym Pythonie niezależnie przeliczono oszacowania dla `L=0` i `a=b`: PASS. Końcowe pola w użytych skończonych testach: odpowiednio `0.0001239776611328125` i `0.00390625`, z wymaganym spadkiem dla kolejnych wartości `N`. Jest to kontrola numeryczno-wymierna przypadków testowych, nie dowód ogólnego faktu.

## Kontrola spójności po poprawce

Na aktualnym źródle R04 i aktualnych R01–R03 przeprowadzono dodatkowo niezależną kontrolę:
- 982 wiersze R04 i **31 odsyłaczy**; wszystkie cele występują w R01–R04;
- brak powtórzonych etykiet w R01–R04, niesparowanych środowisk i zabronionych wariantów zapisu funkcji charakterystycznej;
- wszystkie siedem etykiet wprost sprawdzanych przez workflow R04 istnieje;
- potwierdzono nowe założenia oraz dokładny tekst przypadku `a=b`.
Wszystkie te *statyczne* kontrole dały PASS.

## Lokalna kompilacja i ograniczenia CI

Utworzono lokalny, odizolowany dokument LaTeX z poprawionym sformułowaniem przykładu i odpowiednimi pakietami polskimi. **`pdflatex` zakończył się kodem 0**, wygenerował jednostronicowy PDF A4, bez diagnostyki o przekroczonym łamie. Wyrenderowano PDF i obejrzano stronę: brak kolizji i ucięcia tekstu w tym wycinku. Nie jest to kompilacja całego R04 na jego pełnej oryginalnej preambule i nie dowodzi poprawnej paginacji całej książki.

Próba ustalenia bieżących uruchomień GitHub Actions przez dostępne API nie pozwoliła potwierdzić uruchomienia push; publiczny adres GitHub Actions i GitHub API nie był dostępny przez bieżącą przeglądarkę, a endpoint GitHub łączący commity z uruchomieniami w użytej integracji obejmuje wyłącznie przebiegi PR. **Wyniku obu zadań CI nie potwierdzono** i nie przypisuje się im PASS. Wcześniejsze pozytywne lokalne renderowanie rysunku Cantora pozostaje udokumentowane przez audyt XX; pełny PDF R04 w kontekście książki pozostaje do obejrzenia.

## Decyzja i kolejna iteracja

**R04: nadal NIEZATWIERDZONY.** Wykryto i poprawiono jeden nowy rzeczywisty brak w dowodzie, dlatego kolejne czyste iteracje należy liczyć od nowej wersji pliku. Zakres R04 nie został rozszerzony o nowe tematy.

**Następnie:** audyt VII wyłącznie R04: niezależny szczegółowy przegląd dowodów po ostatniej poprawce, rzeczywisty wynik CI, pełny build i wszystkie strony PDF (zwłaszcza rysunek Cantora). Nie przechodzić do R05.
