# Teoria miary / Miara i całka — rozdział 06, audyt I (iteracja XXX)

**Data:** 2026-11-23. **Gałąź istniejąca:** biblioteka-matematyczna-iteracja-6.  
**Wyłączny zakres audytu:** chapters/pl/measure_theory/06-funkcje-mierzalne-i-ich-aproksymacja.tex.  
**Blob wejściowy R06:** a910c57c6e466f1ec195b579ce2a40e287bc5cf8.  
**Blob po poprawkach R06:** 856a7f7434e110b61ad598d9199ace960d6047fb.

## 1. Wznowienie na aktualnym stanie

Przed rozpoczęciem odczytano aktualny stan gałęzi względem commitu a6e6b950d7ef311ec83e11294a233d663d04b36b. Nowsze commity nie dotyczyły R05 i R06. Potwierdzono raport 29-rozdzial-05-audyt-II-stabilizacja-2026-11-23.md (blob 67c494e4929382431340b5fd9b00edb38b730b94), wyraźnie nadający R05 status **STABILNY**. Nie istniał dotąd raport R06, więc niniejsza iteracja jest pierwszym audytem tego rozdziału.

Ponownie odczytano AGENTS.md, docs/pl/standardy_terminologiczne.md, books/pl/measure_theory.tex i pełny tekst R06. R01–R05 pobrano **wyłącznie jako kontekst dla odsyłaczy i wcześniejszych definicji**, nie audytowano ich ponownie. books/pl/integration_theory.tex pozostaje osobnym skryptem, bez scalania lub edycji. Nie dotykano R07–R31.

## 2. Zakres kontroli matematycznej, struktury i języka

R06 po poprawkach zawiera **725 wierszy, 9 sekcji, 5 definicji, 11 twierdzeń, 4 wnioski, 15 środowisk dowodów, 6 przykładów, 7 uwag i 1 rysunek TikZ**.

**Zweryfikowane łańcuchy dowodowe:**

1. Funkcje o wartościach w rozszerzonej prostej: mierzalność przeciwobrazów półprostych z końcami wymiernymi, mierzalność zbiorów przyjmowania wartości ±∞ i ciągłość operacji jednoargumentowych.
2. Algebra funkcji rzeczywistych i rozszerzonych: mierzalność pary (f,g), składanie z działaniami ciągłymi, ograniczenie ilorazu do {g≠0}, sumy nieujemnych funkcji rozszerzonych przez przeliczalne sumy przekrojów półprostych; oddzielne rozpatrzenie przeciwnych nieskończoności i ich wykluczenie z dziedziny sumy.
3. Kresy i granice punktowe: tożsamości dla infimum i supremum, przejście do liminf i limsup, mierzalność zbioru zbieżności poprzez ciągłe odwzorowanie rozszerzonej prostej na [-1,1].
4. Funkcje proste: mierzalne włókna i rozłączna reprezentacja; konstrukcja przez obcięcie do n i kwantyzację z krokiem 2^{-n}, jej monotoniczność i dokładny błąd; aproksymacja funkcji rzeczywistych przez różnicę części dodatniej i ujemnej oraz kwantyzację podpisaną także dla wartości ujemnych.
5. Funkcje zespolone: test mierzalności przez części rzeczywistą i urojoną oraz ciągłość sprzężenia i modułu.
6. Równość prawie wszędzie i uzupełnianie: konieczność *mierzalnego* zbioru wyjątkowego przy niezupełnej mierze; konstrukcja nieborelowskiego podzbioru zbioru Cantora jako kontrprzykładu; mierzalna wersja granicy punktowej.
7. Zbieżność według miary: implikacja z prawie wszędzie na przestrzeni miary skończonej przez ciągłość z góry; kontrprzykład przesuwających się funkcji charakterystycznych na prostej; podciąg zbieżny prawie wszędzie przez pierwszą część lematu Borela–Cantellego; jednoznaczność granicy i przykład „maszyny do pisania”.
8. Rysunek aproksymacji funkcji f(x)=x przez schodkową s_2: właściwe długości czterech przedziałów poziomych, wartości i domknięte końce przedziałów.

**W audycie nie stwierdzono nowego fałszywego twierdzenia ani błędnego wzoru**, ale wykryto niedostatecznie określone hipotezy oraz problem przypadku brzegowego, które poprawiono poniżej.

## 3. Zapisane poprawki (wyłącznie R06)

**Commit źródła e1f7701c9277fabcff50e1c68d826f9dbceabaf5:**
- usunięto błędny i zduplikowany odsyłacz „na mocy wniosku [thm:composition-measurable] i twierdzenia [thm:composition-measurable]”; pozostawiono jedno poprawne powołanie się na **twierdzenie**;
- w twierdzeniu o działaniach na funkcjach rozszerzonych jawnie określono przestrzeń (X,F);
- we wniosku dotyczącym monotonicznych ciągów funkcji podano przestrzeń (X,F), indeksację, wymaganie mierzalności oraz pełną treść dla malejących ciągów;
- we wniosku o jednoznaczności granicy według miary jawnie określono przestrzeń (X,F,μ), ciąg mierzalnych funkcji f_n oraz mierzalne funkcje graniczne f,g.

**Commit źródła 916d7fac8862e3a9dddcdc1fce5a410cfb4dbdf0:**
- doprecyzowano **X=∅** w równoważnej definicji funkcji prostej: funkcja pusta ma reprezentację jako pusta suma; dowód równoważności osobno ujmuje ten przypadek. Bez tej konwencji reprezentacja przez dodatnią liczbę niepustych części podziału byłaby niejednoznaczna przy pustej przestrzeni.

Wszystkie wcześniejsze etykiety i odsyłacze zachowano, nie dodano niezatwierdzonych twierdzeń.

## 4. Testy regresyjne i workflow

Utworzono tools/test_measure_theory_ch06.py:
- 84 etapy dokładnej kwantyzacji nieujemnych wartości wymiernych i +∞;
- 84 etapy kwantyzacji rzeczywistych wartości dodatnich i ujemnych;
- 1125 porównań rozróżniania wartości rozszerzonych półprostymi o wymiernych końcach;
- 2048 testów przedziałów „maszyny do pisania” na punktach dwójkowo wymiernych;
- kontrprzykład niezupełnej miary na trzech punktach, pokazujący brak mierzalności zmiany na podzbiorze mierzalnego zbioru zerowego;
- automatyczną kontrolę etykiet, odsyłaczy, środowisk LaTeX, terminologii i jawnych hipotez; dodano też regresję konwencji X=∅.

**Commity testu:** a4e37328dbd689779de19c2e3e0575c368efbbe2, abba494d2cca5504c9a6c2275090f608f8e91512 (uzupełnienie wymiernego progu 1/4, oddzielającego 0 od 1/2) i b05bbfdc18b512eb7074a4327bc84dfae3546a20 (kontrola przypadku pustego). **Końcowy blob testu:** 7e875938bdb8d6bac00162c53407e6a204ccd887. Wszystkie zapisy potwierdzono ponownym odczytem przez API GitHub.

Utworzono .github/workflows/measure-theory-ch06.yml (commit c37ada0f347beb9d815b6acdba20bb815e2c749b), poprawiono nazwę kroku testowego (commit 26daa50caf9d14c8ac350bca78dd07497dc9d772). **Blob workflow:** 679bba0b9e0a9c6781c94c00a962144e234b6b2f. Dwa joby: testy i statyczna kontrola źródła, a także rzeczywista kompilacja izolowanego rozdziału i pełnej książki, PDF, podglądy wszystkich stron oraz sprawdzanie odsyłaczy.

Pierwsze dwa przebiegi CI na commitach c37ada0... oraz 26daa50... zakończyły się **2/2 SUCCESS**; drugi udany przebieg [45147947683](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147947683) potwierdza 8 stron izolowanego R06, 4270 słów w granicach stron, 8/8 podglądów, dwie kompilacje izolowanego rozdziału i trzy kompilacje kompletnej książki (256 stron). Rzeczywisty artefakt pobrano z GitHub, a wszystkie osiem stron wizualnie obejrzano w zestawieniu; stronę 4 z rysunkiem funkcji schodkowej powiększono osobno. Podpis i oznaczenia osi nie nachodzą na siebie; nie stwierdzono uciętych napisów ani przepełnienia. Ostrzeżenia o niezdefiniowanych odsyłaczach *izolowanego* rozdziału są spodziewane i rozwiązywane w pełnej książce. Brak Overfull hbox w izolowanym R06.

**Po ostatniej poprawce źródła i testu** uruchomiono nowe przebiegi CI: [run 45148423927](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148423927), commit 916d7fac8862e3a9dddcdc1fce5a410cfb4dbdf0, oraz [run 45148448457](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148448457), commit b05bbfdc18b512eb7074a4327bc84dfae3546a20. **W obu najnowszych przebiegach job testów dokładnych i kontroli źródła zakończył się SUCCESS.** Na moment zamknięcia raportu job PDF i kompilacji całej książki **nadal trwał na etapie instalacji pakietów LaTeX**; nie ogłaszamy mu PASS. Samo powodzenie dwóch wcześniejszych pełnych przebiegów (poprzedni blob rozdziału) nie zastępuje potwierdzenia PDF po ostatniej poprawce.

## 5. Kontrola statyczna po ostatniej poprawce

Ponownie pobrano z GitHub źródła R01–R06 wyłącznie w celu rozwiązania odsyłaczy R06. **R06: 26 etykiet, 18 odsyłaczy, 0 nierozwiązanych celów, 0 duplikatów etykiet, 0 błędnie sparowanych środowisk**. Brak zakazanych oznaczeń funkcji charakterystycznych i niezgodnej terminologii. Funkcje charakterystyczne oznaczane są tylko przez \chi_A. Część matematyczna, rysunek i argumenty innych rozdziałów pozostały niezmienione.

## 6. Stan stabilizacji i następny krok

**R06: NIESTABILNY / DO DALSZEGO AUDYTU.** W tym audycie poprawiono rzeczywiste nieścisłości i przypadek brzegowy. Nawet przy pełnym zielonym CI rozdział wymaga **co najmniej jednego kolejnego, pełnego i niezależnego czystego audytu po ostatniej zmianie**: wszystkich twierdzeń i dowodów, terminologii, środowisk, odsyłaczy, przykładów, rysunku i PDF.

**R01–R05: STABILNE** (status odziedziczony z ich zatwierdzonych raportów, bez ponownego audytu). **R07–R31: nieauditowane w tej iteracji**.

**Następna iteracja:** wyłącznie rozdział 06, audyt II (globalny XXXI). Nie przechodzić do R07 do czasu formalnego zatwierdzenia R06.
