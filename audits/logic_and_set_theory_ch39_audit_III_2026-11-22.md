# Logika matematyczna i teoria mnogości — audyt III rozdziału 39 (potwierdzający)

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/39-slaba-zwartosc-charakterystyki-i-logika-infinitarna.tex.  
**Blob źródła:** 9d06016d71a4c42434b8f0a58c13f666160a4034, bez zmian od audytów I i II.  
**Werdykt końcowy: ROZDZIAŁ 39 STABILNY (2/2+1).** Audyty I, II oraz III są niezależnie czyste i nie wymagały zmian w źródle rozdziału. Pełne CI dla wszystkich trzech zakończyło się sukcesem, a końcowy PDF został pobrany i zweryfikowany.

## 1. Krytyczne próby obalenia implikacji

**Drzewo profili i liczba kolorów.** Sprawdzono przypadek dowolnego 0<μ<κ, a nie tylko kolorów 0 i 1. W kodowaniu węzła na poziomie δ istotna jest nierówność μ^{|δ|}<κ, nie samo μ<κ. Dla gałęzi b świadkowie a(δ) mogą zmieniać się niemonotonicznie; dowód wprowadza dodatkowe δ_ξ przekraczające wszystkich wcześniej wybranych a(δ_η). Wyrażenie α_η<δ_ξ≤α_ξ jest więc prawidłowe, również przy granicznych ξ dzięki regularności κ. Kolor i uzyskuje się z jednego nieograniczonego przeciwobrazu h, gdyż μ<κ; to niezależny krok od wyboru gałęzi.

**Liniowe uporządkowanie na drzewie.** Dla pary nieporównywalnych węzłów istnieje pierwszy poziom różnicy ich ścieżek poprzedników. Dalsze przedłużenia nie zmieniają porównania na tym poziomie, więc stożki pozostają rozdzielone. Zbiór A użyty w dowodzie jest parametryzowany *κ wieloma* enumerowanymi potomkami, nie tylko niezerową liczbą potomków. Dzięki temu U_s i U_t są nieograniczone w κ. Ich przeciwne ułożenie indeksów w dwóch przypadkach jednorodności daje rzeczywistą sprzeczność, nie wymaga nieuzasadnionego założenia, że zbiór A jest z góry liniowo uporządkowany.

**Małe poziomy i regularność.** Rozważono liczbę porządkową δ<κ będącą granicą. Suma zbiorów poziomów T_γ dla γ<δ ma moc mniejszą od κ, mimo że supremum kardynalności pojedynczych poziomów może zależeć od γ; dokładnie regularność κ ogranicza ten supremum. W dowodzie A∩T_δ≠∅ to właśnie pozwala usunąć niskie węzły i zastosować zasadę podziału κ elementów na mniej niż κ włókien.

**Lokalna teoria i wielkość nośników.** W definicji infinitarnej logiki zdaniowej nie dopuszczono formuły o nośniku mocy κ. Gdyby taki nośnik dopuścić, mógłby być nieograniczony i argument z poziomami T_α mógłby nie wymusić jej spełnienia w żadnym etapie α<κ. W tekście jawnie zapisano warunek |supp φ|<κ; z regularności wynika ograniczoność, co jest kluczowe. Spełnienie formuły zależy tylko od wartości zmiennych w jej nośniku, a nie od pozostałych współrzędnych.

**Kompaktność ⇒ gałąź.** Każda klauzula P_α jest dopuszczalną alternatywą <κ zmiennych, gdyż |T_α|<κ. Zakaz wyboru dwóch nieporównywalnych węzłów Q_{s,t} ma tylko dwie zmienne. Podteoria <κ klauzul wymaga tylko <κ konkretnych poziomów, a regularność pozwala wybrać nad nimi jeden węzeł. Kodowanie wszystkich jego poprzedników naraz spełnia nawet *wszystkie* klauzule Q, niezależnie od tego, ile z nich znajduje się w podteorii. Globalne wartościowanie daje wybrane węzły na wszystkich poziomach, parami porównywalne; to rzeczywista gałąź.

**Relacja podziałowa ⇒ regularność.** Dla singularnej κ sprawdzono, że barwienie par według tego, czy ich elementy leżą w jednym małym przedziale, nie dopuszcza jednorodnego H mocy κ: kolor pierwszy ogranicza H do jednego przedziału, drugi do co najwyżej cf(κ) punktów. Nie utożsamiono wyniku regularności z silną granicznością; główna równoważność pozostaje przy jawnym założeniu silnej nieosiągalności.

## 2. Terminologia, zakres i granice weryfikacji

Dokument stosuje wyłącznie pełne określenia „liczba kardynalna”, „liczby kardynalne” i właściwe przypadki gramatyczne. Globalny test nowych zasad sprawdza teraz wszystkie 39 źródeł LaTeX. Pełna zwartość logiki pierwszego rzędu L_{κ,κ} nie jest objęta twierdzeniem o infinitarnej logice zdaniowej; jej utożsamianie bez konstrukcji modelu i dowodu byłoby niepoprawne.

Inwentarz bez zmian: 949 wierszy, 22 etykiety, 25 odsyłaczy, 4 definicje, 4 lematy, 6 twierdzeń, 2 wnioski, 4 uwagi, 1 przykład, 12 dowodów. Zachowano wszystkie odsyłacze między rozdziałami 38 i 39 oraz nie wprowadzono nowego, niezatwierdzonego materiału.

## 3. Rzeczywisty PDF i CI

Punktem odniesienia jest **[CI 45070358451 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070358451)**. Pobrany artefakt zawiera PDF i log. Książka ma **337 stron A4**, a rozdział 39 zajmuje **strony PDF 332–337**. Wyrenderowano wszystkie sześć stron i obejrzano w montażu 3×2: brak widocznych kolizji, obciętych wzorów i błędów rozłożenia akapitów.

CI związane z rozszerzonym zestawem jedenastu testów: [45070999025](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070999025). Audyt II ma odrębny [przebieg 45071067496](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45071067496). Audyt III uruchomi własne CI; nie należy podawać jego wyniku jako sukcesu przed zakończeniem pracy.

## 4. Zamknięte przebiegi CI i analiza rzeczywistego PDF

- **[CI audytu I — 45070762870, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070762870)**.
- **[CI rozszerzonych regresji — 45070999025, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070999025)**: 11 metod testowych rozdziału 39, w tym globalny test właściwego nazewnictwa w 39 rozdziałach.
- **[CI audytu II — 45071067496, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45071067496)**, artefakt 14773037531.
- **[CI audytu III — 45071163738, SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45071163738)**, commit 9b6e7a37e4f06c939d1b2a9e4b760fff0f1d3f1e, artefakt 14773342497.

Pobrano rzeczywiste pliki PDF z pierwszego oraz końcowego CI. Pełna książka ma **337 stron formatu A4**, rozdział 39 obejmuje strony **332–337**. Wszystkie sześć stron wyrenderowano i obejrzano, a następnie porównano z wcześniejszą kompilacją: **6/6 stron identycznych tekstowo i pikselowo**. Log końcowy: **0** błędów LaTeX, **0** przepełnionych wierszy, **0** brakujących znaków, **0** niezdefiniowanych odsyłaczy oraz jedno nieszkodliwe ostrzeżenie underfull.

## 5. Werdykt i stabilność

**Audyt I — czysty (1/2). Audyt II — czysty (2/2). Audyt III — czysty (+1 potwierdzający). ROZDZIAŁ 39 STABILNY.** Wszystkie dotyczyły niezmienionego bloba źródła **9d06016d71a4c42434b8f0a58c13f666160a4034**. Treść i etykiety LaTeX zachowano. Zaktualizowano wcześniejsze rozdziały 34, 35, 37 i 38 zgodnie z globalną zasadą pełnego rzeczownika „liczba kardynalna”; ich zmiany nie modyfikują matematycznych dowodów rozdziału 39. Po zakończeniu pełnego CI tej aktualizacji raportu, jego efekt nie wymaga dalszego rozszerzania treści rozdziału 39. Kompilacja LaTeX i testów Python nie jest formalizacją w Lean.
