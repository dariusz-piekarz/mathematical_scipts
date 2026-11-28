# Miara i całka — audyt XLVIII: rozdział 14, audyt II — niezależna stabilizacja

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/14-przestrzenie-lp-i-ich-podstawowe-wlasnosci.tex.  
**Niezmieniony blob R14 przed i po audycie:** b187bde8f8f0377a8a3e10f1aa5d19dea428147c.  
**Zmiany źródła R14, jego testu, workflow i książki w tej iteracji:** **0**. Zapisano wyłącznie niniejszy raport.

## 1. Rzeczywisty punkt wznowienia

Na początku ponownie porównano gałąź biblioteka-matematyczna-iteracja-6 z commitem raportu XLVII **27bade7d3be67eca745bdf5e3c8607f916c67301**: **0 nowszych commitów**, brak zmian plików i brak raportu XLVIII. Ponownie odczytano audits/measure_theory/47-rozdzial-14-audyt-I-2026-11-23.md (blob 1f5e75e7b129ad746aeb9a8e895d80d734119117), dokumentujący rzeczywistą korektę dowodu gęstości funkcji prostych, doprecyzowanie hipotez i niezależne pozytywne CI, lecz pozostawiający R14 **W STABILIZACJI** w iteracji ze zmianami źródła.

Sprawdzono AGENTS.md, docs/pl/standardy_terminologiczne.md, cały R14, jego test tools/test_measure_theory_ch14.py i workflow .github/workflows/measure-theory-ch14.yml. Rozdziały R01–R13 pobrano **jedynie jako kontekst odsyłaczy i wcześniejszych twierdzeń** — nie prowadzono ich nowych audytów ani edycji. R15–R31 nie otwierano do pracy redakcyjnej, nie zmieniano innych skryptów i nie tworzono gałęzi.

## 2. Niezależny szczegółowy przegląd — 16/16 dowodów

R14 ma **697 wierszy, 11 sekcji, 12 twierdzeń, 2 wnioski, 2 lematy, 2 definicje, 16 dowodów, 7 przykładów i 3 uwagi**. Ponownie oceniono każde rozumowanie i wszystkie konieczne hipotezy:

1. **Lemat o kresie górnym istotnym:** przy skończonym kresie istotnym M, wybór M_n<M+1/n z μ({|f|>M_n})=0 i usunięcie przeliczalnej sumy zbiorów zerowych daje |f|≤M niemal wszędzie; przypadek M=0 i równość prawie wszędzie zapewniają dodatnią określoność normy.
2. **Nierówność Younga:** minimalizacja a^p/p−ab+b^q/q, dokładny warunek równości a^p=b^q oraz osobny przypadek b=0.
3. **Hölder:** normalizacja przez niezerowe normy, zastosowanie Younga, przypadki p=1,q=∞ i p=∞,q=1, całkowalność fg również na przestrzeni o nieskończonej mierze.
4. **Uogólniony Hölder:** skończona liczba czynników m≥2, jawne p_j oraz konwencja 1/∞=0; najpierw wyniesienie ograniczonych istotnie czynników, następnie właściwy krok indukcji z s_j=p_j/r i końcowe zastosowanie Höldera. Osobno przeanalizowano przypadek jednego pozostałego czynnika.
5. **Minkowski:** dla 1<p<∞ najpierw zapewniono całkowalność |f+g|^p przez oszacowanie z wypukłości; dopiero później stosuje się Höldera do |f+g|^{p−1}. Zbadano p=1, p=∞ i przypadek ∥f+g∥p=0 bez niedozwolonego dzielenia przez zero.
6. **Wniosek o normowaniu:** nieujemność, rozdzielność na klasach funkcji, jednorodność, nierówność trójkąta i poprawność operacji na klasach równoważności, dla każdej przestrzeni z miarą.
7. **Kryterium zbieżności szeregów w Lp:** dla p<∞ sumy nieujemne v_N=Σ|u_n| oraz Beppo Levi dla v_N^p dają prawie wszędzie zbieżność bezwzględną; nierówności Minkowskiego i Fatou kontrolują ogony w normie. Dla p=∞ sumowalne normy i przeliczalny wspólny zbiór zerowy dają jednostajną zbieżność przedstawicieli poza nim.
8. **Riesz–Fischer i struktura Hilberta L²:** z dowolnego ciągu Cauchy'ego wybrano podciąg o sumowalnych normach kolejnych różnic; kryterium szeregowe daje granicę podciągu i całego ciągu, a Hölder zapewnia poprawność całki w iloczynie skalarnym. Sprawdzono zespoloną liniowość w pierwszym argumencie.
9. **Jensen:** dla f rzeczywistej całkowalnej i funkcji wypukłej φ:R→R istnienie prostej podpierającej w m=∫f zapewnia, że ujemna część φ(f) jest całkowalna; dlatego nierówność zachodzi również przy całce prawej równej +∞.
10. **Włożenie przy skończonej mierze:** przypadek μ(X)=0 potraktowano oddzielnie; dla dodatniej skończonej miary zastosowano Höldera z q/p i q/(q−p), a q=∞ wynika z kresu istotnego.
11. **Zbieżność w Lp a zbieżność według miary:** dla p<∞ zastosowano Czebyszewa, dla p=∞ jawnie założono f_n,f∈L∞ i wykorzystano oszacowanie normy istotnej; nie wprowadzono niejawnej skończoności miary.
12. **Interpolacja Lp:** przy q<∞ parametry a=p/(θr)>1 i b=q/((1−θ)r)>1 spełniają 1/a+1/b=1; dla q=∞ działa bezpośrednie oszacowanie |f|^r≤∥f∥∞^{r−p}|f|^p. Sprawdzono zerowe normy i dowolną μ(X).
13. **Gęstość funkcji prostych:** dla f≥0 obcięcie do E_n={f>1/n} oraz {f≤n} ma błąd zmajoryzowany przez |f|, a E_n ma miarę skończoną. Kwantyzacja funkcji obciętej o skoku 1/m daje błąd ≤μ(E_n)^{1/p}/m. Po korekcie XLVII **oddzielnie** zastosowano konstrukcję do dodatniej i ujemnej części funkcji rzeczywistej, następnie do części rzeczywistej i urojonej funkcji zespolonej; suma zbiorów skończonej miary pozostaje skończonej miary. Dla p=∞ proste aproksymacje przez kwantyzację ograniczonego obrazu są wystarczające, lecz nie wymaga się ich zerowania poza zbiorem skończonej miary.
14. **Gęstość C_c^∞:** poprawnie wykorzystano wcześniej udowodniony wynik R10 dla p<∞, bez cyklicznego odwołania do kolejnych rozdziałów. Stała funkcja 1 dowodzi braku gęstości przy p=∞.
15. **Ciągłość translacji w Lp(R^d):** dla g∈C_c^∞ wsparcie translacji |h|≤1 mieści się w jednym zwartym zbiorze, a jednostajna ciągłość i skończona miara tego zbioru dają zbieżność. Niezmienniczość λ_d i gęstość C_c^∞ pozwalają przejść do dowolnego f∈Lp, p<∞. Oddzielnie potwierdzono przykład braku ciągłości w Linf.
16. **Separowalność:** przy sigma-skończonej mierze i przeliczalnie generowanej sigma-algebrze algebra generowana przez te zbiory i wyczerpanie X_n jest przeliczalna. Na X_n skończonej miary aproksymacja zbiorów według miary symetrycznej różnicy tworzy sigma-algebrę; argument domknięcia względem przeliczalnych sum wykorzystuje najpierw obcięcie do skończonej sumy. Z Beppo Leviego otrzymuje się ∥fχ_{X\setminus X_n}∥p→0. Kwantyzacja współczynników zespolonych do liczb wymiernych daje przeliczalną rodzinę gęstą.

**Werdykt merytoryczny:** **16/16 PASS** na aktualnym źródle. Nie stwierdzono w tym niezależnym audycie nowego błędu, luki dowodowej ani niejawnego założenia wymagającego poprawki; uzupełnienia z audytu XLVII zachowano.

## 3. Przykłady i uwagi

**7/7 przykładów i 3/3 uwagi — PASS:** funkcje potęgowe przy 0 i ∞, koncentracja masy przy zbieżności według miary, interpolacja L¹∩L∞, brak ciągłości translacji w L∞, rodziny jednostkowo oddalone w nieprzeliczalnym podzbiorze L∞([0,1]) i Lp na nieprzeliczalnym zbiorze z miarą liczącą. Przegląd potwierdził właściwe progi całkowalności i wartości norm, a także różnicę między klasą równoważności a wybranym przedstawicielem. Nie wprowadzono rozszerzeń merytorycznych wymagających odrębnej decyzji.

## 4. Niezależne testy matematyczne — rzeczywiste wykonanie

Utworzono **/mnt/data/r14_audit48/independent_regression.py** i **uruchomiono lokalnie**, bez importowania repozytoryjnego tools/test_measure_theory_ch14.py. Testy obejmowały różne funkcje atomowe, wagi zerowe, skończone i przypadki brzegowe:

| Zakres | Liczba pozytywnych prób |
|---|---:|
| Hölder i Minkowski, również wagi zerowe | 5625 |
| Uogólniony Hölder, p=(2,4,4) | 140625 |
| Jensen, włożenia przy skończonej mierze, interpolacja | 8000 |
| Dokładne oszacowania Czebyszewa | 10125 |
| Kwantyzacja prostych aproksymacji funkcji dowolnego znaku | 204 |
| Dokładne ogony szeregów geometrycznych | 356 |
| Racjonalne funkcje proste na przestrzeniach skończonych | 972 |
| **Razem** | **165907/165907 PASS** |

To **nie są dowody ogólnych twierdzeń** dla arbitralnych przestrzeni z miarą, lecz osobne regresje ich modeli i przypadków brzegowych. Każdy dowód ogólny skontrolowano niezależnie w sekcji 2.

## 5. CI — potwierdzenie obowiązywania dla niezmienionego bloba

Ponownie odczytano [GitHub Actions run 45184297429](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45184297429), commit **38d2ea3477204b105311701e075fade887ffa14b**. **Oba joby mają status completed SUCCESS (2/2)**: testy źródłowe i numeryczne oraz izolowana i pełna kompilacja. Artefakt **14822678181** jest dostępny i nieprzeterminowany.

Porównanie aktualnej gałęzi z commitem runu wykazało **zero zmian** w czterech obserwowanych plikach: źródle R14, tools/test_measure_theory_ch14.py, .github/workflows/measure-theory-ch14.yml i books/pl/measure_theory.tex. Dlatego wynik CI dotyczy **dokładnie audytowanego bloba**, mimo że na gałęzi równolegle mogły pojawiać się niezwiązane zmiany innych projektów.

Workflow potwierdza **75 prób Younga, 2304 przypadki Höldera/Minkowskiego, 3250 przypadków Jensena/włożeń/interpolacji, 25 kwantyzacji i 405 ogonów** oraz poprawność odsyłaczy i składni źródła. Skończone testy workflow nie zastępują dowodów.

## 6. Niezależna kontrola prawdziwego PDF

Do oględzin użyto dokładnego PDF pochodzącego z artefaktu wyżej: **/mnt/data/r14_audit47_verified/measure_theory_ch14_ci.pdf**, a nie hipotetycznej kompilacji. **Ponownie wyrenderowano wszystkie 7 stron przy 155 dpi** do /mnt/data/r14_audit48/render i obejrzano planszę kontaktową zawierającą każdą stronę. Strony 6–7 (gęstość funkcji prostych, translacje i separowalność) dodatkowo skontrolowano osobno w powiększeniu. Brak uciętych wzorów, nakładania napisów, nieczytelnych etykiet lub rysunków; R14 nie ma TikZ.

Rzeczywisty PDF: **7 stron A4**; własna analiza PyMuPDF rozpoznała **3504 słowa i 0 przekroczeń granic stron**, natomiast Poppler w runie CI **4492 słowa**, również wszystkie wewnątrz granic. Ta różnica wynika z odmiennego dzielenia tekstu na słowa.

Z pobranych autentycznych logów ZIP: **izolowany R14 — 0 Overfull hbox, 0 Underfull hbox**; **pełna książka — 258 stron, 0 Overfull hbox, 0 nierozwiązanych odsyłaczy, 14 nieblokujących globalnych Underfull hbox**. Pojawiające się w izolowanym składzie znaki „??” dotyczą **odsyłaczy zewnętrznych do wcześniejszego R10**; po złożeniu pełnego skryptu cele są poprawnie rozwiązane. Nie traktujemy tych znaków jako błędu pełnej książki.

## 7. Integralność odsyłaczy, język i struktura LaTeX

Pobrano R01–R14 przez API GitHub wyłącznie w celu sprawdzenia 12 odsyłaczy R14 do istniejących celów, w tym do R10. Ponowny niezależny skan wykazał:
- **26 etykiet w R14, 12 odsyłaczy — wszystkie 12 poprawne**;
- **0 powtórzonych etykiet** w sprawdzonym kontekście R01–R14;
- **0 błędnie dopasowanych lub niedomkniętych środowisk**;
- brak zakazanych terminów „unia zbiorów”, „zbieżność zdominowana”, samodzielnego rzeczownika „sekwencja”, „indykator” oraz zastępczych symboli funkcji charakterystycznej; zachowano $\chi_A$;
- utrzymano poprawkę dotyczącą funkcji prostych znikających poza zbiorem skończonej miary oraz wszystkie historyczne \label.

## 8. Formalna decyzja i dalsza kolejność

**ROZDZIAŁ 14 — STABILNY / FORMALNIE ZATWIERDZONY.**

Audyt XLVII wykazał i poprawił rzeczywistą lukę w dowodzie gęstości oraz braki samodzielnych hipotez; zakończył się zielonym CI 2/2 i weryfikacją siedmiostronicowego PDF. Obecny **drugi, pełny, niezależny i czysty audyt XLVIII** na tym samym, niezmienionym blobie R14 ponownie objął wszystkie **16 dowodów, 7 przykładów, 3 uwagi, 26 etykiet, 12 odsyłaczy, 165907 niezależnych regresji** i prawdziwy PDF. **Nie znaleziono nowego błędu wymagającego edycji źródła**. Spełniono zasadę stabilizacji.

**R01–R13 — STABILNE**, nieaudytowane ani nieedytowane podczas tego audytu. **R15–R31 — nietknięte.**

**Następna osobna iteracja:** audyt globalny **XLIX / R15 I — „Dualność, wypukłość i słaba zbieżność w przestrzeniach Lp”**. Nie rozpoczęto audytu R15 w tej iteracji.
