# Miara i całka — audyt XLIV: rozdział 12, audyt III — niezależna stabilizacja

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/12-miary-produktowe-twierdzenia-tonellego-i-fubiniego.tex.  
**Niezmieniony blob źródła przed i po audycie:** 999411d62c4b1d5e06c2fbd6e6122bf9b457b7d0.  
**Zmiany treści, testów oraz workflow rozdziału 12:** zero; utworzono tylko niniejszy raport.

## 1. Rzeczywisty punkt wznowienia

Przed rozpoczęciem sprawdzono bieżącą gałąź względem commitu a101780a0ab79314025de10bc6b3c68a1aa52bdf, ostatniego commitu raportu XLIII. Siedem późniejszych commitów dotyczyło **innych skryptów i aplikacji**, nie R12. Istniał zatwierdzony raport XLIII: audits/measure_theory/43-rozdzial-12-audyt-II-2026-11-23.md (blob ef36de59e4f748dc676b6032ce24abedb5860998), dokumentujący poprawki precyzji, zmienione hipotezy, usunięcie Overfull hbox i udane CI. Raport XLIV jeszcze nie istniał, źródło R12 nie zmieniło się. Na tej podstawie wykonano **trzeci pełny, niezależny i czysty audyt rozdziału 12 po ostatniej poprawce**.

Odczytano pełny tekst R12 i jego test/workflow oraz zasady AGENTS.md i docs/pl/standardy_terminologiczne.md. Teksty R01–R11 pobrano **jedynie jako kontekst definicji i referencji**; nie wykonywano nowych audytów tych rozdziałów ani żadnej ich edycji. R13–R31 pozostają nietknięte. Nie scala się innych książek, nie tworzy dodatkowych rozdziałów ani gałęzi.

## 2. Niezależny przegląd matematyczny — wszystkie 12/12 dowodów

Po ostatnich poprawkach R12 ma **865 wierszy, 12 sekcji, 6 twierdzeń, 4 wnioski, 2 lematy, 12 środowisk dowodu, 7 przykładów i 3 uwagi**. Wszystkie dowody ponownie przeczytano w kolejności zależności logicznych:

1. **Mierzalność przekrojów:** dla ustalonego x rodzina zbiorów o przekroju w G jest sigma-algebrą; zawiera prostokąty i zatem całą F⊗G. Analogicznie z przekrojami poziomymi. Dla funkcji sprawdza się mierzalność przeciwobrazów dowolnego zbioru borelowskiego w rozszerzonej prostej. Jawne przestrzenie mierzalne dopisane w audycie XLIII są wystarczające.
2. **Lemat na prostokącie skończonej miary:** rozłączne rozbicie dowolnej skończonej sumy prostokątów, funkcje przekrojowe dla prostokątów, przejście do rosnących ciągów przez Beppo Leviego oraz do malejących przez ciągłość z góry i integrabilne dominaty ν(D)χ_C oraz μ(C)χ_D. Zastosowanie twierdzenia o klasie monotonicznej nie jest cykliczne, gdyż w tym miejscu nie używa się jeszcze Tonellego ani Fubiniego.
3. **Przekroje przy sigma-skończoności:** wyczerpania X_n i Y_n rosnącymi zbiorami skończonej miary; zbiory E∩(X_n×Y_n) rosną do E; zbieżność miar przekrojów i dwukrotne Beppo Levi. Poprawne także przy granicy +∞.
4. **Konstrukcja produktu:** π(E)=∫_Xν(E_x)dμ jest nieujemną miarą; addytywność przeliczalna opiera się na addytywności przekrojów i Beppo Levim. Własność prostokątów jest prawidłowa także przy 0·∞=0. Dla jednoznaczności wystarcza sigma-skończone wyczerpanie przez prostokąty oraz twierdzenie π–λ na skończonych ograniczeniach.
5. **Tonelli:** dla χ_E jest to wzór przekrojowy; dla funkcji prostych nieujemnych wynika z addytywności; dla ogólnych nieujemnych f z ciągu prostych s_n↑f i Beppo Leviego użytego kolejno w przekrojach, po X oraz na produkcie. Przekrojowe funkcje całkowane są mierzalne, bez zakładania skończoności całek.
6. **Kryterium skończoności całki nieujemnej:** wszystkie trzy całki Tonellego mają wspólną wartość w [0,+∞], zatem równoważna jest skończoność każdej z nich.
7. **Fubini:** zastosowanie Tonellego do |f| pozwala wyodrębnić mierzalne zbiory zerowe parametrów ze zbyt dużą całką modułu po przekroju; zerowanie funkcji iterowanych na tych zbiorach daje całkowalne funkcje F i G. Części dodatnie i ujemne oraz — osobno dla f zespolonej — rzeczywiste i urojone całkuje się bez nieokreślonego odejmowania +∞−∞.
8. **Praktyczne kryterium Fubiniego:** skończona iterowana całka z |f| jest przez Tonellego równa skończonej globalnej całce modułu. Po korekcie z XLIII warunek jest samodzielnie zapisany w czytelnym osobnym wzorze.
9. **Zgodność z miarą Lebesgue'a:** borelowskie przedstawiciele zbiorów Lebesgue'a różnią się od oryginałów na podzbiorach zbiorów zerowych. Mierzalność prostokątów w wyższym wymiarze, zgodność z produktem na ograniczonych prostopadłościanach, sigma-skończona jednoznaczność miar oraz uzupełnienie sigma-algebry produktu do L_{m+n} mają wskazane uzasadnienia. Zweryfikowano także przypadki zerowych i nieskończonych miar czynników.
10. **Tonelli i Fubini dla uzupełnienia produktu:** dla funkcji mierzalnej względem uzupełnienia można wybrać mierzalnego przedstawiciela produktowego poza produktowym zbiorem zerowym N. Tonelli dla χ_N pokazuje, że prawie wszystkie jego przekroje mają zerową miarę. Zupełność czynników pozwala na mierzalność funkcji pierwotnej na dobrych przekrojach; równość całek przenosi się z przedstawiciela.
11. **Zerowe przekroje:** równoważność π(N)=0 i ν(N_x)=0 dla μ-prawie każdego x, a symetrycznie w drugą stronę, wynika z tożsamości przekrojowej i faktu, że nieujemna funkcja ma całkę zero wtedy i tylko wtedy, gdy znika prawie wszędzie. W pełni uzasadniono konieczność kwalifikatora „prawie”.
12. **Łączność produktów:** dwie konstrukcje miary na trójce czynników są sigma-skończone, zgadzają się na generujących prostokątach i z jednoznaczności są identyczne. Dowolność kolejności iterowanego całkowania wynika przez kolejne zastosowanie Tonellego dla f≥0 i Fubiniego dla |f| całkowalnej.

**Wynik matematyczny: 12/12 PASS.** Nie wykryto nowej nieprawdziwej tezy, niejawnego istotnego założenia ani błędu w dowodzie wymagającego zmiany źródła. Poprawki z audytów XLII–XLIII są nadal obecne i prawidłowe.

## 3. Przykłady, uwagi i przypadki brzegowe

**7/7 przykładów i 3/3 uwagi PASS.** Ponownie skontrolowano:
- pole trójkąta T⊂[0,1]^2: 1/2 niezależnie od kolejności całkowania;
- całkę 1/(x+y) na (0,1)^2: 2 log 2;
- funkcję e^{−x−y}(x−y): bezwzględna całkowalność przez (x+y)e^{−x−y} i całka zero z antysymetrii;
- macierz a_{m,n}=1_{n=m}−1_{n=m+1}, której sumy iterowane są odpowiednio 0 i 1, bez istnienia globalnej całki funkcji ze znakiem;
- przekątną miara licząca × miara Lebesgue'a bez sigma-skończoności: iterowane całki 0 i 1;
- niemierzalny w sigma-algebrze produktowej podzbiór przekątnej, mimo mierzalności każdego przekroju i mierzalności w pełnej mierze λ_2;
- niezależność elementów losowych na dowolnych przestrzeniach mierzalnych i faktoryzację całek produktów nieujemnych funkcji, z jawnie określoną konwencją 0·∞=0.

Oceniono także ograniczenie wniosku o przekrojach dla uzupełnienia miary: nie wszystkie przekroje muszą być mierzalne; dobrze określona wersja działa niemal wszędzie. Warunek sigma-skończoności w twierdzeniach Tonellego i Fubiniego pozostał jawny. Terminologia i oznaczenia zachowane.

## 4. Nowe niezależne, faktycznie wykonane regresje

Uruchomiono lokalny skrypt **/mnt/data/r12_audit44/independent_regression.py**, nieimportujący modułu tools/test_measure_theory_ch12.py. Wyniki:
- **20736/20736 PASS** — dokładne skończone modele dwuwymiarowego Tonellego, w tym 0 i +∞ w wartościach funkcji oraz masach atomowych;
- **20736/20736 PASS** — niezależna implementacja Fubiniego z funkcjami zmieniającymi znak, sumami w obu kolejnościach i kontrolą całki modułu;
- **65536/65536 PASS** — wszystkie sześć kolejności całkowania i łączność trzech dwupunktowych produktów, także przy atomach o masie zero lub nieskończonej;
- **10000/10000 PASS** — porównanie różnych prostokątnych obcięć kontrprzykładu z niesumowalnym bezwzględnie szeregiem;
- **256/256 PASS** — poprawne zachowanie wyjątkowego przekroju przy zerowej mierze całego produktu.

**Razem 117264/117264 PASS.** To jedynie dodatkowe sprawdzenie szczególnych modeli; twierdzenia ogólne wymagają dowodów i zostały zbadane niezależnie w punkcie 2.

## 5. Rzeczywiste CI i PDF na niezmienionym źródle

Ponownie odczytano [GitHub Actions run 45170775564](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45170775564), commit 1eb9016751c86c78a441af7cefa917ba9fbd228a, i jego artefakt **14817470355**. Oba joby mają status **completed SUCCESS (2/2)**. Porównano także aktualną gałąź z commitem runu: **0 zmian w R12, tools/test_measure_theory_ch12.py, .github/workflows/measure-theory-ch12.yml oraz books/pl/measure_theory.tex**. Poprzednie nieudane runy 45170503751 i 45170607845 wykryły rzeczywisty Overfull hbox, który usunięto w XLIII; nie służą jako podstawa obecnego zatwierdzenia.

Z rzeczywistego ostatniego CI: izolowany PDF R12 — dwie kompilacje, **9 stron A4, 4921 słów Popplera w granicach stron i 9/9 podglądów PNG**. Pełna książka — trzy kompilacje, **257 stron**, bez nierozwiązanych referencji i Overfull hbox.

Niezależnie od workflow otwarto dokładny PDF z tego artefaktu (/mnt/data/r12_audit43/measure_theory_ch12_ci.pdf), wyrenderowano w 190% wszystkie strony do /mnt/data/r12_audit44/page-01.png ... page-09.png i obejrzano ich wspólne zestawienie, a osobno strony 5 (przebudowany wniosek Fubiniego) i 7 (produkt miar Lebesgue'a, jego uzupełnienie oraz lemat o przekrojach). Nie dostrzeżono obciętych wzorów, nachodzenia etykiet lub wad kierunków rozumowania w układzie. Na ostatniej stronie znajduje się krótkie podsumowanie — estetycznie słabiej wykorzystana powierzchnia, ale bez usterki matematycznej lub składu.

Niezależna kontrola PyMuPDF: **9 stron, 4150 słów według jego własnej segmentacji, 0 poza granicami stron**. Różnica względem Popplera pochodzi z innej tokenizacji. Sprawdzono pełne logi: **izolowany R12 — 0 Overfull hbox, 0 Underfull hbox**; **pełna książka — 0 Overfull hbox, 0 nierozwiązanych odsyłaczy, 14 wcześniejszych nieblokujących globalnych Underfull hbox**. Odsyłacze do wcześniejszych rozdziałów pokazujące „??” przy izolowanym składzie są prawidłowo rozwiązane w pełnej książce.

## 6. Odsyłacze, środowiska i język

Ponownie pobrano R01–R12 przez GitHub API wyłącznie w celu oceny celów odsyłaczy z R12. Źródło ma **23 etykiety i 21 odsyłaczy**; wszystkie cele istnieją, **0 duplikatów** w R01–R12, **0 niedomkniętych i błędnie sparowanych środowisk**. Wyrażenie „sekwencji” jest tylko podciągiem poprawnego słowa „konsekwencji” (i jego odmian); kontrola granic wyrazów nie znajduje żadnego zabronionego samodzielnego słowa. Nie ma niedozwolonych „unia zbiorów”, „zbieżność zdominowana”, „indykator” ani alternatywnych oznaczeń funkcji charakterystycznych. Stosowane jest \chi_A.

## 7. Formalna decyzja i dalsza kolejność

**ROZDZIAŁ 12 — STABILNY / FORMALNIE ZATWIERDZONY.**

Pierwszy audyt XLII poprawił brakujące hipotezy wniosku, a drugi XLIII dodał konieczne precyzje w twierdzeniach i przykładach, usunął błąd składu oraz potwierdził kompletny CI. Niniejszy trzeci audyt XLIV stanowi **kolejną, niezależną i czystą kontrolę po ostatniej poprawce** wszystkich 12 dowodów, 7 przykładów, 3 uwag, 23 etykiet, 21 odsyłaczy, przypadków brzegowych z miarą zero i nieskończoną, pięciu serii niezależnych regresji i autentycznego dziewięciostronicowego PDF. Nie wykazano nowych usterek i nie zmieniono źródła; spełniono rygor stabilizacji.

**R01–R11 — STABILNE**, nieaudytowane i nieedytowane w tej iteracji. **R13–R31 — niezmienione**.

**Następna osobna iteracja:** audyt globalny XLV / R13 I, dokładnie jeden nowy rozdział. Nie rozpoczęto go w audycie XLIV.
