# Algebra abstrakcyjna — AA-22, audyt V (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Twierdzenie Artina i podstawowe twierdzenie teorii Galois”.  
**Werdykt:** stabilny matematycznie, brak zmian źródła względem audytu IV.

## Pełna kontrola matematyczna

Ponownie przejrzano 5 kompletnych dowodów, 4 przykłady, definicję, 2 lematy, 2 twierdzenia, wniosek i uwagi. Kontrola obejmuje hipotezy i kwantyfikatory, dziedziny homomorfizmów, wszystkie zastosowane twierdzenia wcześniejsze, uzasadnienie wzorów, każdy etap rozumowania i przypadki skrajne. W szczególności weryfikowano:

- ciało elementów stałych oraz odwrócenie inkluzji;
- liniową niezależność różnych homomorfizmów ciał;
- oszacowanie [L:L^G] ≤ |G| za pomocą układu jednorodnego i minimalnej liczby niezerowych współczynników, oraz oszacowanie przeciwne przez niezależność homomorfizmów;
- rozdzielczość i normalność z wielomianu orbity w twierdzeniu Artina;
- normalność i rozdzielczość L/E dla ciała pośredniego, odwrócenie odpowiedniości Galois, formułę stopni;
- kryterium normalności E/K przez normalność podgrupy i surjektywność homomorfizmu ograniczania;
- rzeczywiste uzasadnienie istnienia automorfizmów dla rozszerzeń dwukwadratowego i z grupą S3, oraz przykład nienormalnego rozszerzenia czysto rzeczywistego;
- ciała pośrednie F_(p^12)/F_p, grupę cykliczną i rolę pierwszości p.

Nie stwierdzono błędnych twierdzeń, nieuzasadnionych istotnych wzorów ani usterek językowych. Nie zmieniono ani jednego bajtu źródła, nie dodano wyników.

## Walidacja

- 47/47 PASS: testy audytu I;
- 24/24 PASS: testy audytu II;
- 22/22 PASS: testy audytu III;
- 20/20 PASS: testy audytu IV;
- 24/24 PASS: nowe niezależne testy audytu V.

**Łącznie 137/137 testów PASS**. Nowe testy wykonują rzeczywistą arytmetykę w F4, F8, F16, F27, sprawdzają orbity Frobeniusa i wielomiany orbitowe, wyznaczają ciała elementów stałych podgrup Frobeniusa, obliczają wyznaczniki macierzy obrazów bazy (niezależność zanurzeń), generatory grup multiplikatywnych, kratę podgrup S3 i trzy ciała pośrednie rozszerzenia dwukwadratowego. Testy skończonych przykładów nie zastępują dowodów twierdzeń ogólnych.

- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: PASS;
- PDF: 4 strony; wszystkie wyrenderowane i sprawdzone wizualnie;
- błędy/ostrzeżenia LaTeX: 0; Overfull/Underfull: 0;
- etykiety: 12 unikatowych; wystąpienia odsyłaczy: 21; odsyłacze zewnętrzne: 11 różnych, wszystkie mają cele w wcześniejszych opublikowanych rozdziałach;
- samodzielny PDF wykorzystuje `prior-labels.tex` do numeracji wcześniejszych wyników.

## Integralność

- SHA-256 źródła po audycie IV: `e17c97d625849eb526d338e523d42f85d06573064fc05ff43b5afe935f81520c`;
- SHA-256 źródła po audycie V: **`e17c97d625849eb526d338e523d42f85d06573064fc05ff43b5afe935f81520c`**;
- Różnice LaTeX między IV i V: **0**.

## Integracja i następne kroki

Rozdział kwalifikuje się do publikacji na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6` w repozytorium `dariusz-piekarz/mathematical_scipts`. Publikacja obejmuje kanoniczny plik rozdziału, pięć zestawów testowych, książkę `books/pl/abstract_algebra.tex`, `catalog/books.json`, README oraz workflow CI. Status zdalnego workflow należy potwierdzić odrębnie — uruchomienie testów lokalnych nie jest równoważne sukcesowi GitHub Actions.

**Stan po stabilizacji:** AA-01–AA-22 są stabilne matematycznie; 74 iteracje audytowe liczone w bieżącej serii. Następny: AA-23, audyt I. Automatyzacja cogodzinna od 12:00 czasu Europe/Warsaw kontynuuje kolejne rozdziały, zawsze pojedynczo i do stabilności.

## Potwierdzona publikacja na GitHubie

Publikację wykonano na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6` (bez tworzenia nowej gałęzi). Następnie ponownie odczytano z GitHuba wszystkie pliki:

- `chapters/pl/abstract_algebra/22-twierdzenie-artina-i-odpowiedniosc-galois.tex`: Git blob SHA `f85f71d7121b986b610558db164c2ee0816e200e`, zgodny z lokalnie sprawdzonym źródłem;
- pięć zestawów `tools/tests/test_abstract_algebra_ch22*.py`: wszystkie pięć Git blob SHA zgodne z pięcioma lokalnymi plikami przechodzącymi łącznie 137 testów;
- `books/pl/abstract_algebra.tex`: zawiera AA-22;
- `catalog/books.json`: 22 rozdziały;
- `README.md`: 01–22 stabilne;
- `.github/workflows/abstract-algebra-chapter.yml`: pięć poleceń testowych AA-22 i build książki do AA-22;
- `audits/abstract_algebra/ch22_iteration_05.md`: raport opublikowany.

Statycznie sprawdzono etykiety wszystkich 21 wcześniejszych rozdziałów: żadna z 12 etykiet AA-22 nie koliduje ze starszymi. Wszystkie 11 zewnętrznych celów odsyłaczy zostało odnalezionych.

**Uwaga o CI:** odczyt statusów commitów nie zwrócił wyników potwierdzających GitHub Actions. Dostępne narzędzie listujące workflow filtruje runy do uruchomień na pull requestach, nie pozwala więc stwierdzić wyniku uruchomienia wywołanego przez push. Zdalny CI **nie jest potwierdzony**; pełna kompilacja książki z 22 rozdziałami nie była osobno wykonywana lokalnie w tej iteracji.

Uruchomiono również osobną automatyzację audytów rozdziałów `Automation_953de4ee16b08191bd7bb0c8d9ea01ee`, od **22 listopada 2026 r. godz. 12:00 Europe/Warsaw**, co godzinę, po jednym rozdziale i jednej iteracji, z przejściem do następnego rozdziału dopiero po stabilizacji.
