# Miara i całka — audyt XLVII: rozdział 14, audyt I (2026-11-23)

**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/14-przestrzenie-lp-i-ich-podstawowe-wlasnosci.tex.  
**Status: W STABILIZACJI — NIEZATWIERDZONY.** R15 pozostaje nietknięty.  
**Blob przed audytem:** 427b29c960565aeec81bef0c3578dda5a64ad766.  
**Blob po poprawkach:** b187bde8f8f0377a8a3e10f1aa5d19dea428147c.

## 1. Rzeczywisty punkt wznowienia i ograniczenie zakresu

Na początku porównano aktualną gałąź z commitem 47e61750ad470fa8d5db5d44fb0054bf3841a720, zamykającym audyt XLVI i **formalnie stabilizującym R13**. Nowsze wówczas commity dotyczyły innych skryptów; raport XLVII nie istniał. Odczytano books/pl/measure_theory.tex, AGENTS.md, docs/pl/standardy_terminologiczne.md, całą treść R14 i wzorcowy workflow poprzedniego rozdziału.

Źródła R01–R13 pobrano **jedynie do kontroli etykiet odsyłanych przez R14** i weryfikacji wcześniejszych twierdzeń, na które R14 się powołuje; nie przeprowadzano ich nowych audytów ani edycji. Nie modyfikowano R15–R31, nie scalano skryptów i nie tworzono gałęzi.

## 2. Szczegółowy przegląd matematyczny całego R14

Po poprawkach rozdział liczy **697 wierszy, 11 sekcji, 12 twierdzeń, 2 wnioski, 2 lematy, 2 definicje, 16 środowisk dowodu, 7 przykładów i 3 uwagi; bez rysunków TikZ**.

**Przejrzano wszystkie 16/16 dowodów**, z osobną kontrolą kluczowych argumentów:

1. **Konstrukcja przestrzeni Lp i Linf:** klasy równości prawie wszędzie, niezmienniczość całek i kresu istotnego względem przedstawiciela. W lemacie o kresie istotnym przeliczalne zbiory wyjątkowe oraz przybliżanie M=esssup z góry dają |f|≤M p.w. Oddzielnie oceniono μ(X)=0 oraz μ(X)=∞.
2. **Young, Hölder i uogólniony Hölder:** minimalizacja funkcji a↦a^p/p−ab+b^q/q, przypadek b=0, normalizacja funkcji o dodatnich normach, oddzielne przypadki p=1, q=∞ oraz p=∞, q=1. W uogólnionej wersji wyłączono czynniki istotnie ograniczone i użyto indukcji z wykładnikami p_j/r oraz ostatniego Höldera.
3. **Minkowski i struktura normowana:** zanim zastosowano Höldera do |f+g|^{p−1}, niezależna nierówność z wypukłości daje f+g∈Lp. Sprawdzono przypadki p=1, p=∞, 1<p<∞ i przypadek ∥f+g∥p=0 przed dzieleniem przez tę normę.
4. **Zbieżność szeregów w Lp i Riesz–Fischer:** dla p<∞ Beppo Levi zastosowany do (Σ|u_n|)^p gwarantuje prawie wszędzie bezwzględną zbieżność, a nierówności Minkowskiego i Fatou kontrolują ogony. Dla p=∞ wspólny przeliczalny zbiór zerowy pozwala zastosować kryterium Weierstrassa. Z ciągu Cauchy'ego wybrano podciąg z sumowalnymi normami przyrostów i następnie zbieżność pełnego ciągu. Dla p=2 sprawdzono seskwiliniowość (liniowość w pierwszym argumencie), dodatniość oraz zgodność normy.
5. **Jensen:** funkcja wypukła określona i skończona na R jest ciągła i posiada prostą podpierającą w m=∫f. Pozwala to zapewnić całkowalność części ujemnej φ(f) mimo braku założenia φ(f)∈L1, następnie scałkować nierówność i uzyskać wartość z przedziału (−∞,+∞].
6. **Włożenia i zbieżność według miary:** sprawdzono μ(X)=0, 0<μ(X)<∞, q<∞ i q=∞, a także nierówność Czebyszewa. Przypadek p=∞ w twierdzeniu o zbieżności według miary po poprawce jawnie dotyczy f_n,f∈L∞.
7. **Interpolacja Lp:** sprzężone wykładniki a=p/(θr) i b=q/((1−θ)r) przy skończonym q oraz przypadek q=∞. Nie używa się niejawnie skończoności miary X.
8. **Gęstość funkcji prostych:** część nieujemną obcina się na E_n={f>1/n} o skończonej mierze i poziomie n. Kwantyzacja daje błąd ≤μ(E_n)^{1/p}/m. W pierwotnym dowodzie **brakowało uzasadnienia przejścia do funkcji o ujemnych wartościach**: po poprawce jawnie przybliżane są części dodatnia i ujemna, a dla funkcji zespolonych również części rzeczywista i urojona, z Minkowskim dla błędu. Dla p=∞ działa jednostajna kwantyzacja ograniczonego zbioru wartości, ale nie można wymagać zerowania funkcji aproksymujących poza zbiorem skończonej miary przy μ(X)=∞.
9. **Gęstość funkcji gładkich i ciągłość translacji:** poprawne odesłanie do wcześniejszego rozdziału 10 dla gęstości C_c^∞ w Lp(R^d), p<∞, bez odwołania do późniejszych wyników. Z niezmienniczości normy względem translacji i jednostajnej ciągłości funkcji gładkich o zwartym nośniku wynika zbieżność po przybliżeniu ogólnego f. Kontrprzykład p=∞ z χ_(0,∞) jest prawidłowy.
10. **Separowalność:** przy sigma-skończonej mierze i sigma-algebrze generowanej przeliczalnie, algebra generowana przez rodzinę i zbiory wyczerpania jest przeliczalna. Na X_n skończonej miary klasa zbiorów przybliżanych w metryce symetrycznej różnicy jest sigma-algebrą; Beppo Levi daje ∥fχ_{X\X_n}∥p→0. Rzeczywiste i urojone współczynniki z liczb wymiernych oraz obcięte charakterystyki zbiorów z przeliczalnej algebry tworzą przeliczalny podzbiór gęsty. Przykłady nieprzeliczalnych rodzin punktów oddalonych o stałą dodatnią poprawnie wykazują nieseparowalność dla wybranych przestrzeni.

**Wynik matematyczny po poprawkach:** w przeglądzie nie znaleziono kolejnego fałszywego twierdzenia wymagającego przebudowy; wykryto i zamknięto lukę w uzasadnieniu gęstości oraz nieprecyzyjne sformułowania hipotez. Ze względu na zmiany w tej iteracji wymagany będzie kolejny niezależny czysty audyt.

## 3. Wszystkie przykłady i uwagi

**7/7 przykładów i 3/3 uwagi sprawdzone**, w tym wykładnicze osobliwości na (0,1), nieskończoną miarę na (1,∞), koncentrację masy f_n=n^{1/p}χ_(0,1/n), interpolację L1∩L∞, brak ciągłości translacji w Linf, nieseparowalność Linf([0,1]) i Lp na nieprzeliczalnym zbiorze z miarą liczącą. Potwierdzono właściwe wartości norm oraz przypadki brzegowe.

Nie wprowadzano niezatwierdzonych nowych tematów ani rozdziałów.

## 4. Rzeczywiste poprawki źródłowe

- **Commit 818d2bdb0424f7bb4406c1e0b3741f4c40ce7e58:** uzupełniono jawne przestrzenie z miarą w definicjach Lp i Linf, lemacie o kresie istotnym, wnioskach o uogólnionym Hölderze i normowaniu oraz twierdzeniach o włożeniach i zbieżności według miary. W dowodzie gęstości funkcji prostych dodano brakujący etap części dodatniej/ujemnej i poprawny rachunek obcinania ogonów na wyczerpaniu sigma-skończonym.
- **Commit 569eea2e0b31c5abc4e054a6ad0d4a3e2d8171f5:** w arbitralnej przestrzeni mierzalnej zastąpiono nieokreślony topologicznie „nośnik” jednoznacznym warunkiem, że funkcja znika poza mierzalnym zbiorem skończonej miary; jawnie określono d i miarę λ_d w twierdzeniu o translacjach.
- **Commit 38d2ea3477204b105311701e075fade887ffa14b:** jawnie skwantyfikowano naturalną liczbę czynników w uogólnionym Hölderze i odrębnie podano f_n,f∈L∞(μ) w części twierdzenia o zbieżności według miary dotyczącej p=∞.

**Ostateczny blob źródła:** b187bde8f8f0377a8a3e10f1aa5d19dea428147c. Nie zmieniono żadnej historycznej etykiety.

## 5. Nowe regresje matematyczne i rzeczywisty CI

Dodano **tools/test_measure_theory_ch14.py**, commit **488096e44226609be1e2b8acf6ebdcd6db609fdc** (testy nierówności dla atomów zerowej i dodatniej masy, kres istotny, Jensen, włożenia, interpolacja i kwantyzacja funkcji ze znakiem); osobny workflow **.github/workflows/measure-theory-ch14.yml**, commit **9e3ab255654f1efc2d7d26953712d13d9b956f4c**. W logu końcowym:
- **75/75 PASS:** Young;
- **2304/2304 PASS:** pary atomowych funkcji dla Höldera i Minkowskiego, także przy zerowych masach i p=∞;
- **3250/3250 PASS:** Jensen, włożenia przy skończonej mierze, interpolacja L1–L2–L∞;
- **25/25 PASS:** kwantyzacja dodatnich i ujemnych liczb wymiernych;
- **405/405 PASS:** normy częściowych sum oraz ogonów szeregów;
- **PASS:** źródło, hipotezy, środowiska i 12 odsyłaczy.

Suma wymienionych serii to **6059 modeli**, z których każdy przeszedł. Dodatkowy niezależny lokalny test, **nieimportujący testu repozytoryjnego**, sprawdził **140625/140625 PASS** przypadków uogólnionego Höldera z wykładnikami 2,4,4 na dwupunktowych przestrzeniach z masami 0,1,3.

Regresje skończone są **diagnostyką**, nie dowodem ogólnego twierdzenia.

**Końcowy, rzeczywiście wykonany CI po ostatniej korekcie:** [GitHub Actions 45184297429](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45184297429), commit **38d2ea3477204b105311701e075fade887ffa14b**, **2/2 joby completed SUCCESS**. Wcześniejsze zielone przebiegi [45182829110](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45182829110) i [45183120721](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45183120721) dotyczyły poprzednich wersji, więc nie zastępują końcowego.

## 6. Autentyczny PDF i jego kontrola

Z najnowszego CI pobrano artefakt **14822678181** jako /mnt/data/measure_theory_ch14_audit47_verified.zip i rozpakowano go do /mnt/data/r14_audit47_verified. Rzeczywisty plik PDF: **/mnt/data/r14_audit47_verified/measure_theory_ch14_ci.pdf**.

- **Izolowany rozdział:** 7 stron A4, 2 przebiegi pdflatex, **4492 słowa Popplera w granicach stron**, 7/7 wygenerowanych PNG; **0 Overfull hbox, 0 Underfull hbox**.
- **Pełna książka:** 3 przebiegi pdflatex, **258 stron**, 0 Overfull hbox, 0 nierozwiązanych odsyłaczy, 14 historycznych nieblokujących globalnych Underfull hbox.
- **Niezależna kontrola PyMuPDF:** 7 stron, 3504 słowa według innej tokenizacji, **0 słów przekraczających granice strony**. Różnica liczby słów wynika ze sposobu segmentacji.
- Obejrzano podglądy wszystkich 7 stron i osobno powiększono strony 5–7 z włożeniami, interpolacją, poprawionym dowodem gęstości i separowalnością. Nie znaleziono uciętych wzorów, kolizji etykiet ani błędnego łamania matematyki. R14 nie zawiera rysunków TikZ. W izolowanym PDF w odsyłaczach do R10 mogą występować znaki „??” — nie są one błędem pełnej książki, w której cele istnieją i są rozwiązane.

## 7. Kontrola integralności i formalna decyzja

Na końcowym źródle R14 przeprowadzono odrębną kontrolę API GitHub z etykietami R01–R14 jako kontekstem: **26 etykiet, 12 odsyłaczy**, wszystkie do istniejących celów, **0 powtórzeń etykiet**, 0 źle zamkniętych środowisk i 0 naruszeń globalnej terminologii (funkcje charakterystyczne zapisane przez $\chi_A$). Dokument ma 16 dowodów, 12 twierdzeń i 7 przykładów; nie został poszerzony o niezatwierdzone nowe tematy.

**R14 — W STABILIZACJI / NIEZATWIERDZONY.** Audyt I doprecyzował kilka wyników oraz uzupełnił rzeczywistą lukę w dowodzie gęstości. Potem zweryfikowano pełne, zielone CI **2/2**, autentyczny 7-stronicowy PDF i jego kompletność. Ponieważ jednak **źródło było wielokrotnie edytowane w tej iteracji**, zgodnie z ustaloną zasadą **nie można uznać R14 za STABILNY od razu**. Konieczny jest kolejny, pełny, niezależny, czysty audyt **XLVIII / R14 II** na niezmienionym blobie b187bde8f8f0377a8a3e10f1aa5d19dea428147c.

**R01–R13 — STABILNE**, bez nowych audytów i edycji w tej iteracji. **R15–R31 — nietknięte**.

**Następny krok:** audyt XLVIII, wyłącznie R14. Dopiero po formalnym zatwierdzeniu R14 można rozpocząć R15.
