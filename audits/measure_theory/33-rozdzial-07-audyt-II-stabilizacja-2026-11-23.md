# Teoria miary / Miara i całka — rozdział 07, audyt II (globalny XXXIII): niezależny audyt czysty i stabilizacja

**Data:** 2026-11-23. **Jedyna użyta gałąź:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/07-konstrukcja-calki-lebesguea.tex.  
**Blob źródła R07 na początku i na końcu:** 783976ccc4d0c1ff02056e171233e2e70022f4f1.  
**Zmiany w źródle R07 w tej iteracji:** 0 — audyt kontrolny po ostatniej poprawce z audytu XXXII.

## 1. Ustalenie rzeczywistego punktu wznowienia i zakresu

Przed rozpoczęciem pobrano stan istniejącej gałęzi względem commitu d11ae77bd59ddbe0f884f88aced3bf301a2829b8. Dwa późniejsze commity dotyczyły aplikacji Lean i skryptu grafów; **żaden nie zmienił źródła R07**. Ponownie odczytano raport auditu XXXII: audits/measure_theory/32-rozdzial-07-audyt-I-2026-11-23.md, blob 6d4da38dbfad762f90647a6f25d5f1f500fd9700, w którym udokumentowano poprawki dwóch przykładów, pustej przestrzeni oraz terminologii i zapisano status R07 **NIESTABILNY**. Raport XXXIII jeszcze nie istniał.

Ponownie pobrano aktualne AGENTS.md, docs/pl/standardy_terminologiczne.md, books/pl/measure_theory.tex, treść R07 i jego testy/workflow. Źródła R01–R06 i R08 pobrano **wyłącznie jako kontekst wcześniejszych definicji oraz celów odsyłaczy**; nie prowadzono audytu innych rozdziałów ani ich nie edytowano. Plik books/pl/integration_theory.tex oraz powiązany rozdział integration_theory/11-calka-lebesgue-a.tex odczytano wyłącznie do kontroli zgodności sąsiedniej książki — bez zmian i scalania.

## 2. Drugi pełny, niezależny audyt matematyczny po ostatnich poprawkach

R07 zawiera 509 wierszy, 5 sekcji, 5 definicji, 2 lematy, 5 twierdzeń, **7 środowisk dowodu**, 6 przykładów i 5 uwag; nie ma rysunków ani schematów.

**Sprawdzenie dowodów 7/7 — PASS:**

1. **Niezależność całki prostej od rozkładu:** jej postać kanoniczna wynika z włókien mierzalnej funkcji. Przejście do wspólnego rozdrobnienia zachowuje całkę przy dowolnie dużych, również nieskończonych miarach atomów; nie występuje odejmowanie nieskończoności. Dla pustego X obowiązuje jawnie zapisana pusta suma.
2. **Algebra całki prostej:** monotoniczność, dodatnia jednorodność i addytywność wynikają z parami rozłącznych A_i∩B_j i reguły 0·∞=0, także dla c=0 i mas nieskończonych.
3. **Pierwsze własności całki nieujemnej:** monotoniczność rodzin minorant, bijekcja minorant przy skalowaniu c>0 i odrębny przypadek c=0; zgodność z funkcjami prostymi. Mierzalne zawężenie do A i zerowa całka na mierzalnym zbiorze zerowym nie wymagają addytywności całki ogólnej.
4. **Całka względem ograniczenia miary:** przedłużenie prostej minoranty z A przez zero i jej ograniczenie do A dają obie nierówności, a potem równość supremów.
5. **Nierówność Markowa i jej konsekwencje:** minoranta aχ_{f≥a}; ograniczenie μ({f≥n}) przy całce skończonej, a dla całki zerowej przeliczalna suma zbiorów {f≥1/n}.
6. **Niezmienniczość przy modyfikacji na zbiorze zerowym:** zerowanie prostych minorant na mierzalnym N nie zmienia ich całek; zamiana f i g daje równość. Dla całek ze znakiem sprawdzono osobno obie części f^± oraz brak nieokreślonego ∞−∞.
7. **Kryterium całkowalności bez ukrytego użycia twierdzenia Beppo Leviego:** osobno dzielimy każdą prostą minorantę |f| na P={f≥0} i M={f<0}; proste funkcje na tych zbiorach prowadzą do pierwszej nierówności, a suma niezależnych minorant f^+ i f^- do odwrotnej. Daje to ∫|f|=∫f^++∫f^- także dla przypadków, w których wartość mogłaby być nieskończona, bez przedwczesnego użycia ogólnej addytywności całki nieujemnej.

**Wynik matematyczny: 0 nowych błędów i 0 nowych brakujących hipotez wymagających poprawki.**

**Sprawdzenie przykładów 6/6 i uwag 5/5 — PASS:** obie funkcje proste na nieskończonej przestrzeni; f=+∞ na zbiorze mierzalnym miary zero; miara dyskretna i szereg z wartościami +∞ oraz wagami 0 i +∞; rozbieżna całka 1/x wykazana dokładnymi minorantami (wartości n/2); funkcja Dirichleta; całkowalność 1/(1+x²) na prostej mimo nieskończonej miary całej przestrzeni. W ostatnim przykładzie ponownie zweryfikowano, że (-1,1), [n,n+1), (-n−1,−n], n≥1 są parami rozłączne i pokrywają całą prostą, włącznie z ±1. Sprawdzono także różnicę między całką skończoną, nieskończoną i nieokreśloną.

## 3. Nowa, rzeczywiście uruchomiona niezależna regresja matematyczna

W lokalnym środowisku uruchomiono **oddzielny skrypt kontrolny** (/mnt/data/audit33_independent_r07.py), niezależny od repozytoryjnego tools/test_measure_theory_ch07.py. Sprawdzał wartości funkcji na przestrzeni trzech atomów, wagi 0, 2 i +∞, operację 0·∞=0, dyskretne całki grupowane według włókien, obcięcia oraz funkcje ze znakiem. Wyniki:

- **1728/1728 PASS** — całka prosta liczona dwiema niezależnymi formułami (suma po atomach i po włóknach);
- **6912/6912 PASS** — dokładna nierówność Markowa dla czterech progów dodatnich;
- **8640/8640 PASS** — ograniczenia całek obciętych funkcji nieujemnych, także z wartościami +∞;
- **3375/3375 PASS** — równość ∫|f|=∫f^++∫f^- oraz kryterium skończoności obu części;
- **161/161 PASS** — kontrola rozłączności i pokrycia przedziałami, w tym ±1;
- **PASS** — osobne kontrole pustego X i konwencji 0·∞=0.

To są regresje skończonych modeli, **nie dowody** ogólnych twierdzeń dla dowolnych przestrzeni z miarą. Wszystkie ogólne argumenty sprawdzono również osobno, jak wskazano w sekcji 2.

## 4. Język, LaTeX, etykiety i rzeczywisty PDF

Po raz drugi pobrano przez GitHub API źródła R01–R08 **wyłącznie do rozwiązania odsyłaczy z R07**. W R07: **17 etykiet, 11 odsyłaczy, 0 nierozwiązanych referencji w R01–R08, 0 powielonych etykiet w tym kontekście, 0 niezamkniętych albo błędnie sparowanych środowisk**. Brak słów „sekwencji”, „unia zbiorów”, „zbieżność zdominowana”, a funkcje charakterystyczne mają wyłącznie oznaczenie \chi_A. Etykiety historyczne zachowane.

Ponownie użyto **autentycznego sześciostronicowego PDF** z poprawionego przebiegu CI [45150225228](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45150225228), powiązanego z niezmienionym blobem R07. Lokalnie wykonano nowe rasteryzacje wszystkich 6 stron przy 150 dpi, a następnie **obejrzano każdą z nich indywidualnie**. Brak kolizji, uciętych wzorów, rysunków lub niewidocznych symboli. Ostatnia strona jest bardzo krótka (wyłącznie zamykająca uwaga), co odnotowano jako **nieblokującą cechę przełamania rozdziału**, nie błąd matematyczny ani czytelności. W izolowanym PDF widoczne są „??” w miejscu odsyłaczy do pozostałych rozdziałów: jest to spodziewane, gdy kompiluje się **tylko jeden rozdział**.

Ponownie odczytano rzeczywiste logi i wynik CI; dwa joby **2/2 completed SUCCESS**; pobrany artefakt PDF ID 14805592865 pozostaje dostępny. Log izolowanego R07: **0 Overfull hbox, 0 Underfull hbox**; „undefined references” pojawia się wyłącznie w izolowanym składzie. W pełnej książce: **257 stron, 0 Overfull hbox, 0 unresolved references, 14 Underfull hbox**, zatem globalne nieblokujące ostrzeżenia o niedopełnionych wierszach pozostają poza zakresem audytu R07. CI wykonał dwie kompilacje izolowanego R07, trzy kompilacje całej książki, bbox 3172 słów mieszczących się w stronach oraz 6/6 podglądów PNG. Od tego przebiegu inne commity w gałęzi nie zmieniły R07 ani jego testów/workflow.

## 5. Zgodność ze skryptem integration_theory — odrębna uwaga przekrojowa

Pobrano wyłącznie jako kontekst books/pl/integration_theory.tex (blob 6ec24a3d62bae4baef945fca0ff1c433510de141) i chapters/pl/integration_theory/11-calka-lebesgue-a.tex (blob b082083e7f73099263c97f77c959d4e1a627be40). Definicja całki przez supremum nieujemnych prostych minorant i kryterium absolutnej całkowalności są **zgodne merytorycznie** z R07.

**Wykazano jednak niespójność oznaczeń w odrębnej książce:** integration_theory.tex deklaruje makro \ind jako \mathbf 1, używane w rozdziale 11 dla funkcji charakterystycznych. Obowiązująca reguła globalna przewiduje wyłącznie \chi_A. **Nie poprawiono tego tutaj**, ponieważ bezwzględna reguła jednego rozdziału zabrania audytu lub edycji innych rozdziałów w tej iteracji. Uwaga pozostaje otwarta jako osobne zadanie terminologiczne dla tamtego skryptu; nie zmienia poprawności ani stabilności R07.

## 6. Formalna decyzja

**ROZDZIAŁ 07 — STABILNY / FORMALNIE ZATWIERDZONY.**

R07 przeszedł audyt XXXII, w którym poprawiono rzeczywiste błędy w przykładach i przypadek brzegowy, następnie zakończył pełne CI **2/2 SUCCESS** oraz przegląd autentycznego PDF. Bieżący **kolejny, niezależny i czysty audyt XXXIII po ostatniej poprawce** objął wszystkie dowody, przykłady, uwagi, założenia, konwencje, nowe obliczenia regresyjne, terminologię, etykiety, skład PDF i logi CI. **Nowych usterek w R07 nie wykryto.** Nie dokonywano nowych zmian treści, więc nie powstała konieczność kolejnego audytu po poprawce.

**R01–R06 — STABILNE, bez nowych audytów i zmian.** R08–R31 nie były audytowane w tej iteracji; jedynie ich konieczny kontekst odsyłaczy mógł zostać odczytany.

**Następna osobna iteracja:** rozdział 08 „Twierdzenia graniczne dla całki Lebesgue'a”, audyt I. W niniejszej iteracji nie rozpoczynano jego audytu.