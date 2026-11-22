# Logika matematyczna i teoria mnogości — audyt III rozdziału 39 (potwierdzający)

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Rozdział:** chapters/pl/logic_and_set_theory/39-slaba-zwartosc-charakterystyki-i-logika-infinitarna.tex.  
**Blob źródła:** 9d06016d71a4c42434b8f0a58c13f666160a4034, bez zmian od audytów I i II.  
**Werdykt matematyczny:** czysty — dodatkowa niezależna kontrola potwierdzająca. Do finalnego oznaczenia stabilności wymagany jest zielony pełny przebieg CI po rozszerzeniu testów oraz kontrola wynikowego PDF.

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

## 4. Werdykt i warunek finalizacji

**Audyt I — czysty. Audyt II — czysty merytorycznie. Audyt III — czysty merytorycznie (+1 potwierdzający).** Wszystkie trzy przeprowadzono na identycznym blobie. Status „ROZDZIAŁ 39 STABILNY (2/2+1)” jest warunkowy aż do potwierdzenia zielonych przebiegów CI dla audytów II i III oraz niezależnej kontroli ostatniego PDF. Kompilacja Python i LaTeX nie jest formalizacją w Lean.
