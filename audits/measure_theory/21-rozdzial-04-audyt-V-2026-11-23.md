# Miara i całka — rozdział 04, audyt V: niezależna kontrola struktury i rysunku (iteracja XXI)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Jedyny rozdział:** `chapters/pl/measure_theory/04-miara-lebesguea-na-przestrzeni-euklidesowej.tex`. Nie audytowano R05–R31 i nie edytowano innych rozdziałów.

## Stan wejściowy

Odczytano HEAD gałęzi względem commitu raportu XX `a42f1278404866891482768daf307e7ca7b1edef` (10 późniejszych commitów w innych częściach repozytorium, bez modyfikacji R04). Nie istniał raport XXI; R04 pozostał po poprawce podpisu z audytu XX na blobie `84b6300e8939fee9874ff4872862e7604dd4c1aa`. Ponownie odczytano aktualną wersję workflow R04 i jego skrypt geometryczny. Dotychczasowe audyty XVII–XX pozostają podstawą opisu zmian; w tej iteracji nie ponawiano ich jako fikcyjnie nowych kontroli.

## Niezależne, nowe kontrole po poprawce podpisu

1. **Zgodność odsyłaczy w R04 z R01–R04:** z czterech aktualnych plików źródłowych zebrano wszystkie etykiety, a z R04 wszystkie 30 odwołań. Nie wykryto duplikatów etykiet ani nierozwiązanych celów R04. W pozostałych 27 rozdziałach nie wykonywano audytu.
2. **Środowiska LaTeX:** sprawdzono kolejność i parowanie wszystkich wystąpień `\\begin`/`\\end` w R04, bez niewłaściwego zamknięcia lub otwartych środowisk.
3. **Terminologia i funkcje charakterystyczne:** nie stwierdzono w R04 `\\mathbf{1}`, `\\mathbb{1}`, `\\mathds{1}`, „zbieżności zdominowanej” ani „unii zbiorów”.
4. **Struktura rysunku:** odczyt po poprawce potwierdza `\\end{tikzpicture}` bezpośrednio przed `\\par\\smallskip` i właściwym podpisem; rysunek zawiera dokładnie jedną strukturę TikZ.
5. **Geometria rysunku Cantora:** niezależnie skontrolowano wszystkie narysowane przedziały `C_1,C_2,C_3`: odpowiednio 2, 4 i 8 odcinków o długościach zgodnych z `3^{-n}` z dokładnością `3·10^{-6}` wymaganą dla sześciomiejscowych przybliżeń dziesiętnych. Brak przecięć pomiędzy przedziałami danego etapu. Osobny lokalny program Python sprawdzający właśnie współrzędne oryginalnego wycinka TikZ zwrócił `PASS` dla trzech etapów, a równoległe sprawdzenie pełnego źródła z GitHub (w JavaScript) potwierdziło te same warunki.

Wynik bieżącej kontroli: **brak nowej wykazanej usterki struktury, podpisu i geometrii rysunku**. Tekstu matematycznego R04 w tej iteracji nie zmieniano.

## Rzeczywista poprawa ochrony przed regresją

Dodano `tools/test_measure_theory_ch04_source.py`, commit **`2eaa8254e96db1a9a1ae1103caaddbc91789f6be`**. Skrypt ma uruchamiać w repozytorium kontrole etykiet, celów odsyłaczy, parowania środowisk, zakazanej terminologii, obecności wymuszonego zakończenia akapitu pod rysunkiem oraz współrzędnych i liczby odcinków trzech etapów Cantora.

Podłączono go do istniejącego `.github/workflows/measure-theory-ch04.yml`, commit **`7479ed791a32a13f3ba02b9254d5faaae102b59d`**, zarówno w filtrze ścieżek powodujących uruchomienie workflow, jak i w osobnym kroku joba `chapter-04-exact-geometry`. Ponownie pobrano i potwierdzono zawartość obu zapisanych plików. Dotychczasowy test geometryczny, generowanie PDF i kontrola pełnej książki pozostawiono bez zmian.

## Wyniki i ograniczenia CI/PDF

Z wykonanej **bieżącej kontroli źródła przez skrypt JS** uzyskano: 30 poprawnych odsyłaczy, 0 duplikatów etykiet, 0 źle sparowanych środowisk, 0 zabronionych symboli lub wyrażeń, poprawny układ podpisu oraz 2/4/8 poprawnych przedziałów Cantora. Osobny program Python wykonał lokalną kontrolę współrzędnych diagramu ze zgodnym wynikiem.

**Nie potwierdzono nowego pełnego przebiegu GitHub Actions.** Endpoint łączący commity z workflow pokazuje w tym interfejsie tylko przebiegi związane z PR i zwrócił pustą listę; tradycyjne statusy commitu również były puste. Nie jest to dowód nieuruchomienia workflow ani podstawa do zgłoszenia PASS. Wcześniej zweryfikowany izolowany PDF samego rysunku jest poprawny; nie pobrano i nie przejrzano całego wielostronicowego PDF R04.

## Status

**R04: STABILIZACJA NIEZAKOŃCZONA.** Matematycznie nie znaleziono nowych błędów po ostatniej poprawce, a statyczne kontrole struktury i geometrii są pozytywne. Do formalnej certyfikacji pozostają: końcowy wynik obu zadań CI na aktualnym commicie, pobranie i wizualny przegląd wszystkich stron PDF R04 w kontekście rzeczywistej książki, oraz niezależny pełny czysty audyt po zmianach technicznych.

**Następna iteracja:** nadal tylko R04. Nie przechodzić do R05 przed formalnym zatwierdzeniem stabilności.
