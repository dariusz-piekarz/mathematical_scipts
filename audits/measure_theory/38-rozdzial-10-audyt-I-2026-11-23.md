# Teoria miary / Miara i całka — audyt globalny XXXVIII: rozdział 10, audyt I

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Rozdział:** 10, „Regularność funkcji mierzalnych i aproksymacja funkcjami ciągłymi”.  
**Źródło:** chapters/pl/measure_theory/10-regularnosc-funkcji-mierzalnych-i-aproksymacja-funkcjami-ciaglymi.tex.  
**Książka:** books/pl/measure_theory.tex. **Porównanie kontekstowe:** books/pl/integration_theory.tex, wcześniejsze twierdzenia i etykiety; bez edycji sąsiednich rozdziałów.

## 1. Punkt wznowienia

Pobrano najnowszą gałąź i katalog audits/measure_theory. Ostatnim istniejącym raportem był **37-rozdzial-09-audyt-II-stabilizacja-2026-11-23.md**, formalnie zamykający R09. Raport XXXVIII nie istniał. W historii gałęzi znajdowały się już trzy commity bieżącej iteracji R10: **7857a3fbc0a729886faf1da3d3a2d89f85321c96** (źródło), **7abaa8602d949684f9ab331c9ff7f8b2e00478d6** (testy), **1c89b0996a2ba3e095f899e0743f243a5cfdb45a** (workflow). Przed raportem ponownie pobrano aktualne AGENTS.md, docs/pl/standardy_terminologiczne.md, książkę, skrypt całkowania i aktualny blob R10.

**SHA R10 przed zmianami:** b915e0bc47fc75784ba098199a2adf6a40c007ef.  
**SHA R10 po zmianach i po ponownym odczycie:** 2a5db02f83ae41a6ebabe30547d47080a75004cd.

## 2. Audyt matematyczny

Ponownie przeanalizowano 9 sekcji R10, w tym **5 twierdzeń, 5 lematów, 6 wniosków, 16 dowodów, 1 przykład, 6 uwag i 1 diagram TikZ** (liczby z pliku przed poprawkami). Zakres kontroli:

1. **Regularność miary Lebesgue'a:** oba kierunki aproksymacji zbioru skończonej miary, rozkład O\K, możliwość ograniczenia otwartego otoczenia kompaktu. Poprawne.
2. **Gładka funkcja odcinająca:** konstrukcja z η(t)=e^{-1/t} dla t>0; dodatniość mianownika, zachowanie wartości 1 na domkniętej półkuli, 0 poza kulą, nośnik wewnątrz O. Poprawne.
3. **Przybliżenie χ_A:** kontrola błędu całkowego przez λ_d(O\K), także dla p≥1. Poprawne.
4. **Łuzin dla funkcji prostych:** wykryto rzeczywistą lukę dla E=∅: liczba różnych wartości m=0, a dowód stosował ε/m. **Poprawiono** jawnie przypadek E=∅ przed podziałem przez m.
5. **Twierdzenie Łuzina:** aproksymacja prostymi, Jegorow na przestrzeni skończonej miary, usunięcie wyjątków o sumowalnych miarach, przecięcie kompaktów i jednostajna granica funkcji ciągłych. Sprawdzono budżet ε/4+ε/4+ε/4<ε; poprawny.
6. **Wnioski dla funkcji skończonych p.w. i rodziny przeliczalnej:** usunięcie zbioru wartości nieskończonych, sumowanie wyjątków i przecięcie kompaktów. W pierwszym wniosku **doprecyzowano samodzielne hipotezy i kwantyfikatory**, zamiast odsyłać niejawnie do całego twierdzenia.
7. **Aproksymacja Lipschitzowska na kompakcie:** infimum h(y)+L|x−y|, oszacowanie w pobliżu x i poza δ, obcięcie do [-M,M]. Poprawne.
8. **Przedłużenie funkcji ciągłej z kompaktu:** geometryczne zanikanie reszt, jednostajna zbieżność szeregu i obcięcie. W tezie wykryto **niezdefiniowane rzeczywiste supremum sup_K|h| przy K=∅**. **Poprawiono**: nierówność wyłącznie dla K≠∅, a dla K=∅ jawnie H=0.
9. **Aproksymacja w mierze przez C_c i C_c^\infty:** Łuzin, przedłużenie, funkcja odcinająca i wygładzanie splotem; prawidłowe oszacowanie zbioru wyjątkowego. Wniosek o wygładzaniu otrzymał **pełne jawne hipotezy** E, f, \widetilde f, ε, δ.
10. **Gęstość C_c^\infty w L^p dla 1≤p<∞:** obcięcie nośnika i wartości, kwantyzacja także dla wartości ujemnych, aproksymacja χ_A i złożenie błędów; warunek p<∞ konieczny, kontrprzykład z funkcją skokową dla p=∞ poprawny.
11. **Granice p.w. funkcji gładkich:** przybliżenia na kulach B_n, sumowalność miar wyjątków i pierwszy lemat Borela–Cantellego; wniosek o reprezentancie borelowskim przez zbiór punktów skończonej zbieżności poprawny.
12. **Uwagi:** rozróżnienie ciągłości ograniczenia f|K od ciągłości w otoczeniu, miary nieskończonej, przedstawicieli borelowskich i borelowskich otoczek zbiorów zerowych. Nie stwierdzono nowej sprzeczności.

Nie dodano nowych twierdzeń, przykładów ani rozdziałów.

## 3. Zmiany źródłowe

W jednym commicie **7857a3fbc0a729886faf1da3d3a2d89f85321c96** dokonano czterech lokalnych poprawek:
- obsłużono E=∅ w dowodzie lematu Łuzina dla funkcji prostych;
- obsłużono K=∅ w tezie twierdzenia o przedłużaniu funkcji;
- rozwinięto wszystkie hipotezy wniosku dla funkcji skończonych prawie wszędzie;
- rozwinięto wszystkie hipotezy wniosku o aproksymacji w mierze funkcjami gładkimi.

Zachowano wszystkie etykiety i przyjętą treść matematyczną. Nowy blob R10 potwierdzono przez ponowny odczyt API: **2a5db02f83ae41a6ebabe30547d47080a75004cd**.

## 4. Nowe testy i faktyczne wyniki CI

Dodano **tools/test_measure_theory_ch10.py** (commit **7abaa8602d949684f9ab331c9ff7f8b2e00478d6**) i workflow **.github/workflows/measure-theory-ch10.yml** (commit **1c89b0996a2ba3e095f899e0743f243a5cfdb45a**).

Faktycznie uruchomiono GitHub Actions **run 45157663182** na commicie **1c89b0996a2ba3e095f899e0743f243a5cfdb45a**, https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157663182. Ponownie pobrano joby i logi; **2/2 jobs completed SUCCESS**:
- **1809/1809** próbek gładkich funkcji odcinających;
- **13824/13824** modeli przybliżenia χ_A;
- **432/432** oszacowania Lipschitzowskie inf-splotu;
- **66/66** dokładnych przypadków kwantyzacji ze znakami;
- **14/14** budżetów miar zbiorów wyjątkowych;
- przypadki E=∅ i K=∅ — PASS;
- **21/21** odsyłaczy R10 znalezionych w odpowiednich rozdziałach kontekstowych; składnia środowisk i zakazane warianty terminologiczne — PASS.

**Rzeczywisty skład PDF:** izolowany R10, **7 stron**, **4267 słów** według kontroli workflow, wszystkie wewnątrz granic stron; **7/7** wygenerowanych podglądów stron; brak Overfull hbox według kontroli CI. Pełna książka **257 stron**, trzy przebiegi pdflatex, bez niezdefiniowanych i zduplikowanych odsyłaczy oraz bez Overfull hbox według walidacji workflow. Artefakt **measure-theory-ch10-audit-pdf**, ID **14808807520**, rozmiar **1907383 bajty**, nieprzeterminowany w chwili sprawdzania.

**Dodatkowa kontrola wizualna po pobraniu artefaktu:** lokalnie rozpakowano rzeczywisty ZIP runu 45157663182, odczytano `measure_theory_ch10_ci.pdf` (7 stron A4) i utworzono planszę zawierającą podglądy **wszystkich 7 stron**. Obejrzano ją wizualnie; stronę 2 z diagramem $K\subseteq A\subseteq O$ skontrolowano osobno w pełnym powiększeniu. Oznaczenia $K$, $A$, $O$ są czytelne i nie nachodzą na granice figur ani inne napisy; nie znaleziono uciętych wzorów lub kolizji w zestawieniu stron. Niezależna kontrola PyMuPDF objęła **3368 słów według jego własnej tokenizacji**, **0 poza stronami** (Poppler w CI rozpoznał 4267 słów). W izolowanym logu potwierdzono **0 Overfull hbox i 0 Underfull hbox**, a w pełnej książce 0 Overfull i 14 wcześniejszych, nieblokujących Underfull. Kontrola kontaktowego zestawienia oraz wybranej strony w pełnym rozmiarze nie jest tożsama z niezależną szczegółową inspekcją każdej strony w pełnym powiększeniu; taką kontrolę należy powtórzyć w kolejnym czystym audycie. Skończone modele numeryczne nie zastępują dowodów ogólnych.

## 5. Status i następny krok

**R10: W TRAKCIE AUDYTU — NIESTABILNY / JESZCZE NIEZATWIERDZONY.** W bieżącej iteracji poprawiono cztery miejsca, więc nie wolno uznać jej za dodatkowy niezależny czysty audyt *po ostatniej poprawce*. CI 2/2 jest zielone, ale rygor stabilizacji wymaga następnego, niezależnego przeglądu matematycznego, redakcyjnego, technicznego i wizualnego na niezmienionym blobie R10.

**Otwarte sprawy:** w następnej iteracji wykonać audyt II R10, przejrzeć wszystkie 7 stron artefaktu PDF (zwłaszcza rysunek), potwierdzić ponownie poprawność wszystkich dowodów, etykiet, terminologii, a następnie — tylko przy braku nowych usterek — formalnie zatwierdzić stabilność R10.

**R01–R09 pozostają formalnie stabilne; R11–R31 nietknięte.** Nie audytowano równolegle żadnego innego rozdziału, nie scalano ani nie usuwano treści z books/pl/integration_theory.tex.
