# CAT-32 — audyt kontrolny merytoryczny i testy modeli skończonych

Data: 27.11.2026  
Źródło: `chapters/pl/category_theory/32-2-kategorie-i-bikategorie.tex`  
Blob źródła: `a6a0d5afb1e80ea2d5fd7d376385f39e2fae21fa`  
Commit ostatniej zmiany źródła: `42b1f25ed854260bf520fb0320c87424d0cc1f89`  
Gałąź: `biblioteka-matematyczna-iteracja-6`

## Zakres audytu

Ponownie sprawdzono typowanie i zgodność konstrukcji: 2-kategorie ścisłe, prawo wymiany, składanie z 1-morfizmami, bikategorie, pięciokąt i trójkąt, pseudofunktory, transformacje pseudonaturalne, modyfikacje, bikategoria rozpiętości, sprzężenia, równoważności i birównoważności. Nie stwierdzono nowej usterki matematycznej wymagającej zmiany źródła.

## Testy konstrukcji Span(FinSet)

Model testowy obejmuje wszystkie zbiory o liczności 0, 1 i 2 oraz wszystkie rozpiętości z obiektami środkowymi o liczności co najwyżej 2. Łącznie enumerowano 43 rozpiętości. 2-morfizmy to wszystkie funkcje między obiektami środkowymi zachowujące obie nogi rozpiętości. Iloczyny włókniste i ich rzutowania są konstruowane jawnie jako skończone zbiory zgodnych par; nawiasowania są reprezentowane przez zagnieżdżone pary.

Wszystkie asercje zakończyły się powodzeniem:

- 43 identyczności w kategoriach morfizmów i 983 pary pionowo składanych 2-morfizmów;
- 971 przypadków zachowywania identyczności przez składanie poziome;
- 635 891 przypadków prawa wymiany (funktorialność składania poziomego);
- 277 elementowych przypadków naturalności lewego unitoru i 277 prawego unitoru;
- 3 771 rodzin 2-morfizmów sprawdzających naturalność łączności w mniejszym modelu (obiekty o liczności 0, 1, 2; obiekty środkowe rozpiętości o liczności najwyżej 1), w tym 81 przypadków elementowych; sprawdzono również wzajemną odwrotność izomorfizmów łączności;
- 533 691 rodzin czterech składanych rozpiętości sprawdzających pięciokąt, w tym 531 243 przypadki elementowe;
- 971 rodzin dwóch składanych rozpiętości sprawdzających trójkąt, w tym 1 227 przypadków elementowych;
- 11 funkcji między zbiorami o liczności najwyżej 2 sprawdzających dane jednostki i kojednostki dla sprzężenia rozpiętości wykresu. Obie tożsamości trójkątowe wynikają z tego, że odpowiednie nogi rozpiętości są identycznościami.

Testy są regresją na skończonych modelach. Nie zastępują dowodów ogólnych ani formalizacji Lean.

## Kontrola struktury i integracji

- 37 etykiet, wszystkie unikatowe;
- wszystkie odsyłacze lokalne i do wskazanych rozdziałów odnalezione;
- 10 środowisk dowodu;
- 7 diagramów TikZ;
- wszystkie środowiska `begin/end` poprawnie zagnieżdżone;
- rozdział obecny w głównym pliku książki i katalogu.

## CI i ograniczenia odbioru

Dla commitu źródłowego `42b1f25` trzy workflowy GitHub Actions — CAT-00 validation, Polish mathematical terminology i Mathematical library application checks — były w stanie `queued` podczas odczytu. Nie oznaczono ich jako PASS. Późniejszy commit gałęzi `027b40f` zmieniał wyłącznie `application/tests/browser_references.py`; blob CAT-32 pozostał niezmieniony.

Nie wykonano lokalnej kompilacji TeX/PDF ani oględzin renderowanych diagramów. Z tego powodu odbiór techniczny i wizualny pozostaje otwarty.

## Decyzja

Audyt kontrolny matematyczny i skończona regresja konstrukcji `Span(FinSet)`: PASS. Brak nowych poprawek źródłowych. Rozdziału nie oznaczać jeszcze jako w pełni zwalidowanego: wymagane są zakończone CI oraz kontrola kompilacji i PDF.
