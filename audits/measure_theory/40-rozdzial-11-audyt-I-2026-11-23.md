# Teoria miary / Miara i całka — rozdział 11, audyt I (globalny XL)

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Zakres:** wyłącznie rozdział 11 „Całki zależne od parametru” oraz jego osobne testy i workflow.  
**Plik:** chapters/pl/measure_theory/11-calki-zalezne-od-parametru.tex.  
**Blob R11 przed audytem:** de1fd545d6346bc2a12a4f9b9607f28826b292e0.  
**Blob R11 po ostatniej korekcie:** d9e41430abca9c0094767891c17f0c01ae166444.

## 1. Rzeczywisty punkt wznowienia

Na początku porównano gałąź z commitem **133ad5ec696d856441acd512ca9bb54ea13038c7** i odczytano raport audits/measure_theory/39-rozdzial-10-audyt-II-stabilizacja-2026-11-23.md (blob 4d5abf14f998cff80f040a7b7073001e54686099). R10 pozostawał **STABILNY**; nie istniał raport XL. Odczytano AGENTS.md, docs/pl/standardy_terminologiczne.md, books/pl/measure_theory.tex oraz całe źródło R11.

R01–R10 i R12 pobrano tylko jako kontekst wcześniejszych faktów, definicji i etykiet. Nie edytowano ani nie audytowano pozostałych rozdziałów, nie scalano książek i nie zmieniano gałęzi. W czasie pracy inne automatyzacje wprowadziły równoległe commity do innych plików; pierwszy zapis raportu otrzymał konflikt wersji gałęzi 409. Ponownie pobrano aktualną gałąź, potwierdzono, że R11 pozostaje niezmieniony, i dopiero wtedy podjęto zapis raportu. Nie nadpisano obcych zmian.

## 2. Zakres kontroli matematycznej

R11 po poprawkach ma **526 wierszy, 9 sekcji, 8 twierdzeń, 1 wniosek, 1 definicję, 8 dowodów, 5 przykładów i 5 uwag; bez rysunków**.

**Sprawdzono wszystkie 8 dowodów, wraz z powiązanymi przypadkami brzegowymi:**

1. **Lokalne kryterium ciągłości:** rozróżnienie dominacji poza jednym wspólnym zbiorem zerowym i słabszej dominacji z wyjątkami zależnymi od t; wzdłuż dowolnego ciągu t_n→t₀ wystarcza przeliczalna suma zbiorów zerowych. DCT dla |f(t_n,·)−f(t₀,·)| i ciągowe kryterium ciągłości w przestrzeni metrycznej.
2. **Zbieżność jednostajna po całkowaniu:** niepustość T, mierzalność przekrojów, nieujemne całkowalne majoranty h_n≤g, zbieżność h_n→0 p.w., kontrola całkowalności f(t,·) przez jedną funkcję referencyjną i g₀. Oszacowanie sup_t różnic całek przez ∫h_n, bez bezpodstawnego zakładania mierzalności supremum po dowolnej rodzinie.
3. **Różniczkowanie lokalne:** dla zespolonej f zastosowanie twierdzenia o wartości średniej do Re(\bar u f(s,x)) i supremum po |u|=1; oszacowanie całych ilorazów różnicowych wspólną funkcją g∈L¹. Mierzalność pochodnej jako granicy mierzalnych ilorazów, DCT, liniowość całki i definicja F′. Pochodna na mierzalnym zbiorze wyjątkowym ma jawnie wybrany reprezentant zerowy.
4. **Wyższe pochodne:** z lokalnej kontroli pierwszej pochodnej wynika całkowalność f(t,·) dla każdego t. Indukcja z twierdzenia o pierwszej pochodnej daje F^{(k)} jako całkę ∂ᵏf; dodatkowa dominacja ∂ᵏf i ciągłość po t zapewniają ciągłość kolejnych pochodnych. Jawne nieujemne funkcje g_{J,k} i konwencja zbiorów wyjątkowych.
5. **Parametryczne kryterium Vitaliego:** μ(X)<∞, jednostajna całkowalność modułów i zbieżność według miary w parametrze. Negacja zbieżności w L¹ daje ciąg parametrów sprzeczny z twierdzeniem Vitaliego zastosowanym do części rzeczywistej i urojonej.
6. **Ruchome obszary całkowania:** zastąpienie ∫_{A_t}u przez ∫_Xχ_{A_t}u, poprawność przekrojów i dominacja wzdłuż dowolnego ciągu parametrów poza przeliczalną sumą wyjątków, bez wymagania wspólnego zbioru dla wszystkich t. DCT daje ciągłość.
7. **Jednostajna kontrola ogonów:** wyczerpanie przez mierzalne X_n o skończonych miarach, całkowalność na każdym X_n i jednostajne małe całki modułów na X\X_n. Trójkątne oszacowanie różnicy całek przez część lokalną i dwa ogony.
8. **Holomorficzność transformaty Laplace'a:** lokalny wybór σ<σ′<Re z zapewnia integrację xᵏ e^{-Re zx}|h(x)| przez wyjściowy wykładniczy warunek całkowalności. Dominacja zespolonych ilorazów różnicowych i iteracja po k dają wzory na pochodne bez korzystania z twierdzenia Fubiniego.

**Pięć przykładów i pięć uwag:** sprawdzono koncentrację masy przy t↓0, lokalną dominację e^{-tx}, obliczanie momentów całki Laplace'a, ruchome przedziały i funkcję Gamma wraz z całkowalnością x^{a−1}|log x|ᵏ w zerze oraz zanikaniem ogonów wykładniczych. Zweryfikowano znaczenie wspólnego zbioru wyjątkowego i odróżnienie lokalnej dominacji od jednostajnej całkowalności.

**Wynik:** brak nowego fałszywego twierdzenia lub podstawowej błędnej implikacji, ale wykryto usterki precyzji hipotez i samodzielności sformułowania wniosku; zostały poprawione. Wymagany będzie niezależny audyt po zmianach, zanim można formalnie zatwierdzić stabilność.

## 3. Udokumentowane poprawki źródłowe

- **964e3fe1a7958f1b71109a2b8957b1fe24c6ef0d:** jawnie dodano (X,F,μ) do definicji lokalnej dominacji i odpowiednich twierdzeń. W twierdzeniu o zbieżności jednostajnej całek majoranty g i g₀ są nieujemnymi mierzalnymi funkcjami całkowalnymi, a zakres kwantyfikacji został doprecyzowany. W twierdzeniach o pochodnych wprowadzono konwencję zerowego reprezentanta na mierzalnym zbiorze wyjątkowym i poprawiono majoranty. W twierdzeniu o ruchomych obszarach podano przestrzeń z miarą. Zmieniono błędnie motywowany tytuł przykładu „Parametr uciekający do nieskończoności” na „Koncentracja masy przy zerze”.
- **b181b07c9c892cff724a49741a3aa44c7b93361e:** przepisano wniosek o ciągłości w normie L¹ jako samodzielne stwierdzenie z wszystkimi hipotezami.
- **6ddb0041064eb63edf48df132a8f1fd62acf9b5d:** określono lokalną dziedzinę U odwzorowania o wartościach w L¹, nie twierdząc bez dowodu, że wszystkie f(t,·) dla t∈T są całkowalne.
- **26503f566c6e39401fdf495e0683e13425f3c26b:** poprawiono uszkodzone zakończenie środowiska wniosku, wykryte przez realny CI: \end{wniosek> zastąpiono \end{wniosek}.

Wszystkie poprawki zapisano tylko w R11, bez zmiany jakiejkolwiek etykiety. **Ostateczny blob rozdziału:** d9e41430abca9c0094767891c17f0c01ae166444.

## 4. Nowe testy, również negatywne przebiegi CI

Utworzono tools/test_measure_theory_ch11.py (commit **6a81ac4c276290ceac283c3abfd2fb3eebf3afac**) i .github/workflows/measure-theory-ch11.yml (commit **10f165738c4286f994a913e34c557f692b6fbb5b**).

Pierwszy rzeczywisty [run 45159644601](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159644601) zakończył się niepowodzeniem testu źródła, mimo przejścia testów matematycznych: błędny filtr słowa „sekwencji” dopasowywał jego podciąg w poprawnym słowie „konsekwencji”. Poprawiono test w commicie **2bef229131a775b645d1bdced74a59ff82feb59e**, używając granicy wyrazu zamiast wyszukiwania podciągu. Kolejny [run 45159773269](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45159773269) zakończył się już **2/2 SUCCESS**. Późniejsze runy [45160186017](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160186017) i [45160219987](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160219987) wykryły błąd LaTeX w nowym wniosku, który również poprawiono. Nie przedstawia się tych nieudanych przebiegów jako zielonych.

**Ostateczny, rzeczywiście zakończony CI:** [GitHub Actions 45160370883](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160370883), commit **26503f566c6e39401fdf495e0683e13425f3c26b**, **2/2 joby completed SUCCESS**. Z logów najnowszego testu:
- **125/125 PASS:** jednostajna dominacja i supremum po parametrach;
- **324/324 PASS:** dokładne ilorazy różnicowe skończonych sum;
- **318/318 PASS:** ciągłość ruchomych obszarów na skończonych modelach;
- **100/100 PASS:** geometryczne oszacowania ogonów;
- **23/23 PASS:** rzeczywiste i zespolone przykłady Laplace'a;
- **PASS:** 12 odsyłaczy R11 (po usunięciu jednego odsyłacza w przebudowanym wniosku), poprawnie sparowane środowiska, hipotezy i terminologia.

Testy numeryczne dotyczą szczególnych modeli, **nie dowodzą ogólnych twierdzeń**. Złożone argumenty udowodniono i przejrzano osobno w rozdziale.

## 5. Faktyczny PDF końcowego bloba i niezależna inspekcja

CI dla **końcowego SHA**, nie tylko wcześniejszego, wykonał **2 kompilacje pdflatex izolowanego R11** i **3 kompilacje pełnej książki**. Poppler potwierdził **6 stron A4, 3774 słowa w granicach stron, 6/6 wygenerowanych podglądów PNG**. Pełna książka ma **257 stron**, brak niezdefiniowanych odsyłaczy i brak Overfull hbox.

Pobrano autentyczny artefakt **14809818860**, rozpakowano do /mnt/data/measure_r11_audit40_final/, niezależnie odczytano PDF przez PyMuPDF (**6 stron, 3003 słowa według innej tokenizacji, 0 poza stronami**) oraz obejrzano zestawienie **wszystkich sześciu stron najnowszego PDF**. Układ tekstu, wzory, nagłówki i końcowy przykład Gamma są czytelne, bez uciętych wzorów i kolizji; w tym rozdziale nie ma rysunków TikZ wymagających osobnej inspekcji.

Izolowany log R11: **0 Overfull hbox i 0 Underfull hbox**, oczekiwane ostrzeżenie o odsyłaczach do innych rozdziałów (nieobecnych w izolowanym składzie). Pełna książka: **0 Overfull hbox, 0 niezdefiniowanych odsyłaczy, 14 globalnych nieblokujących Underfull hbox**.

## 6. Kontrola źródła po ostatniej korekcie

R11 po zmianach liczy **526 wierszy, 18 etykiet, 12 odsyłaczy**, 8 poprawnie sparowanych środowisk dowodu, 8 twierdzeń, 1 wniosek, 1 definicję, 5 przykładów i 5 uwag. Test źródłowy uwzględnia etykiety R01–R12 jako kontekst, w tym prawidłowy przyszły odsyłacz do rozdziału o produktach miar: **0 brakujących celów, 0 zduplikowanych etykiet, 0 niesparowanych środowisk, 0 zakazanych wyrazów w prawidłowym rozpoznawaniu granic słów**. Obowiązuje notacja \chi_A.

## 7. Status i następny krok

**R11 — W STABILIZACJI / NIEZATWIERDZONY.** Audyt I wykrył i poprawił nieścisłości hipotez oraz samodzielność wniosku, następnie zakończył się pełnym prawdziwym CI **2/2 SUCCESS** i poprawnym 6-stronicowym PDF. Jednak w tej samej iteracji wielokrotnie zmieniano źródło, a błąd składniowy został wykryty i naprawiony dopiero przez regresję. Zgodnie z nadrzędną zasadą konieczny jest **kolejny pełny, niezależny i czysty audyt tego samego bloba R11**, zanim wolno go uznać za STABILNY.

**R01–R10 — STABILNE**, bez zmian w tej iteracji. **R12–R31 — nietknięte.**

**Następny osobny krok:** globalny audyt XLI / R11 II, wyłącznie rozdział 11. Do R12 przejść dopiero po jawnym zatwierdzeniu R11.