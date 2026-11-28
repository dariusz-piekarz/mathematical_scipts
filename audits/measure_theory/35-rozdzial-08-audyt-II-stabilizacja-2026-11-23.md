# Teoria miary / Miara i całka — rozdział 08, audyt II (globalny XXXV): audyt czysty i formalna stabilizacja

**Data:** 2026-11-23. **Gałąź istniejąca:** biblioteka-matematyczna-iteracja-6.  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/08-twierdzenia-graniczne-dla-calki-lebesguea.tex.  
**Niezmieniony blob R08 przed i po audycie:** ee4660de677bebbe11323f08f18efc5111b91968.  
**Zmiany treści, etykiet i infrastruktury testowej R08 w tej iteracji:** zero; zapisano jedynie raport.

## 1. Rzeczywisty punkt wznowienia i izolacja zakresu

Przed rozpoczęciem porównano gałąź z commitem 14eeae5d1c7bdd81ac1d85b94443ecbae911dc97. Nowsze commity dotyczyły innych skryptów, a nie R08. Odczytano raport audytu XXXIV (audits/measure_theory/34-rozdzial-08-audyt-I-2026-11-23.md; blob d766797fa19fa46f5278d8c986d52cb3f4681c40), dokumentujący pięć korekt i status R08 „w stabilizacji”. Raport XXXV dotąd nie istniał.

Ponownie odczytano AGENTS.md, docs/pl/standardy_terminologiczne.md, rzeczywistą treść rozdziału 08, jego osobny test i workflow. Źródła R01–R07 służyły wyłącznie jako kontekst definicji i celów odsyłaczy; nie były w tej iteracji ponownie audytowane ani edytowane. R09–R31 nie były audytowane ani edytowane. Nie dokonano deduplikacji, scalania ani dodawania niezatwierdzonych twierdzeń.

Bieżąca iteracja stanowi **drugi niezależny i czysty audyt R08 po ostatniej korekcie**: w odróżnieniu od audytu XXXIV nie wymagała żadnej nowej zmiany źródła.

## 2. Ponowna weryfikacja wszystkich 27/27 środowisk dowodów

Aktualny R08: **1132 wiersze, 12 sekcji, 17 twierdzeń, 7 wniosków, 2 lematy, 2 definicje, 27 środowisk dowodów, 9 przykładów, 1 uwaga, 0 rysunków TikZ**.

Niezależnie przeanalizowano wszystkie następujące argumenty:

1. **Lemat o całkach funkcji prostej na rosnących zbiorach:** ciągłość miary z dołu dla każdej z finitarnych poziomic, także przy wartości +∞, oraz przypadek współczynnika zero.
2. **Beppo Levi:** mierzalność granicy, rosnące zbiory E_n={f_n≥θs}, ich suma równa X, oba kierunki nierówności, również gdy całka prostej minoranty jest nieskończona.
3. **Wniosek o prostych aproksymacjach:** poprawne odwołanie do twierdzenia MCT i kanonicznego ciągu funkcji prostych, z jawnie określoną przestrzenią z miarą.
4. **Beppo Levi prawie wszędzie:** jeden mierzalny zbiór zerowy dla wszystkich funkcji i monotoniczności; brak nieokreślonego 0·∞ dzięki przyjętej konwencji.
5. **Addytywność całki nieujemnej:** s_n+t_n rosnące do f+g; przeniesienie addytywności funkcji prostych na ogólne, także przy +∞.
6. **Przeliczalny rozkład całki:** skończona addytywność i rosnące nośniki częściowych sum na rozłącznych zbiorach.
7. **Liniowość rzeczywista:** rozkład na części dodatnie i ujemne, szczególna kontrola współczynników ujemnych i prawa odejmowania tylko całek skończonych.
8. **Wniosek o nierówności trójkąta:** oszacowanie przez |f|+|g| i zachowanie całkowalności.
9. **Liniowość zespolona i oszacowanie modułu:** rozdzielenie części rzeczywistych/urojonych i przemnożenie przez sprzężoną fazę całki.
10. **Lemat Fatou:** ciąg infimów ogonowych jest mierzalny, monotoniczny i zbiega do liminf, z prawidłowym oszacowaniem infimów całek.
11. **Odwrotny lemat Fatou:** wspólny mierzalny zbiór wyjątkowy, g skończona prawie wszędzie, odejmowanie wyłącznie skończonej całki g.
12. **Fatou z całkowalnym ograniczeniem od dołu:** ujemna część f_n jest zdominowana przez g; nigdy nie pojawia się niezdefiniowane ∞−∞.
13. **Twierdzenie Lebesgue'a o zbieżności zmajoryzowanej:** wspólny zbiór zerowy, nierówności Fatou zastosowane do g±f_n, ograniczone skończone całki i właściwe przejście od liminf/limsup do granicy.
14. **Zbieżność w L¹ pod wspólną dominacją:** zastosowanie rzeczywistej DCT do |f_n−f|≤2g, także dla funkcji zespolonych po przejściu do modułu.
15. **Twierdzenie o zbieżności ograniczonej:** μ(X)<∞ i wyraźnie nieujemna M∈[0,∞), więc g≡M jest nieujemną funkcją całkowalną.
16. **Szeregi nieujemne:** Beppo Levi dla sum częściowych, bez używania zamiany kolejności dwóch sum z wyrazami o nieokreślonym znaku.
17. **Szeregi absolutnie sumowalne:** G=Σ|f_n| jest całkowalna, więc skończona prawie wszędzie; zbiór zbieżności jest mierzalny i zespolona DCT stosuje się do S_N.
18. **Wzór warstwowy:** mierzalność nierosnącego ogona t↦μ({f>t}), rachunek dla prostych funkcji i dwukrotne użycie MCT bez zakładania twierdzenia Tonellego.
19. **Rozkład na poziomice dla |f|^p:** p>0, rozróżnienie punktu t=0 miary Lebesgue'a zero, poprawność formuły dla prostych aproksymacji i MCT.
20. **Przykład całki potęgi:** dla α≥1 porównanie z 1/x, dla α<1 obcięcie przedziału i wzór Riemanna na domkniętych przedziałach.
21. **Ciągłość pod całką:** dominacja w otoczeniu parametru, wspólny zbiór wyjątkowy i wykorzystanie ciągowego kryterium ciągłości przestrzeni metrycznej.
22. **Różniczkowanie pod całką:** twierdzenie o wartości średniej, mierzalność pochodnej jako granicy ilorazów, DCT dla dowolnego h_n→0 i jawna konwencja zerowej wartości pochodnej na mierzalnym zbiorze wyjątkowym.
23. **Lemat kontroli całek na małych zbiorach:** oszacowanie K μ(A) plus jednostajnie mały ogon; zapewniona niepustość rodziny i skończona μ(X).
24. **Równoważność kryteriów jednostajnej całkowalności:** kierunek konieczny oraz Markow z jednostajnym ograniczeniem norm dla drugiego kierunku, osobno M=0.
25. **Twierdzenie Vitaliego:** podciąg zbieżny prawie wszędzie, Fatou dla funkcji granicznej, małe zbiory i rozdzielenie na {|f_n−f|>η} oraz jego dopełnienie.
26. **Zgodność całki Riemanna i Lebesgue'a:** mierzalne funkcje Darboux na częściach podziału, pierwsza część lematu Borela–Cantellego, zupełność miary i zbieżność obu sum.
27. **Kryterium Lebesgue'a całkowalności Riemanna:** domknięte poziomice oscylacji, oszacowanie przez U−L w kierunku koniecznym; w kierunku wystarczającym wybór O z λ₁(O)<b−a gwarantuje niepusty K i uzasadnia skończone pokrycie oraz dodatnie minimum promieni.

**Wynik matematyczny: 27/27 PASS.** W tym niezależnym przeglądzie nie stwierdzono nowego błędu, brakującej istotnej hipotezy ani nieuzasadnionego przeskoku wymagającego modyfikacji R08. Przypadki brzegowe z audytu XXXIV zostały potwierdzone po poprawce. Sprawdzono także wszystkie 9 przykładów i 1 uwagę, bez nowych usterek.

## 3. Dodatkowa niezależna regresja arytmetyczna

Uruchomiono w lokalnym Pythonie nową, niezależną od repozytoryjnego test_measure_theory_ch08.py implementację sprawdzającą ściśle skończone modele:
- **512000/512000 PASS** — MCT dla monotonicznych trójek na trzech atomach, także z masami i wartościami +∞ oraz konwencją 0·∞=0;
- **65536/65536 PASS** — Fatou dla okresowych ciągów trójwyrazowych na dwóch atomach, w tym masy nieskończone;
- **1728/1728 PASS** — zespolona zbieżność zmajoryzowana dla skalowanych ciągów na dwóch atomach, bez mylenia modułu z wartością bezwzględną części rzeczywistej;
- **39/39 PASS** — dokładne oszacowanie Darboux dla funkcji będącej zerem poza jednym punktem nieciągłości.

Lokalny skrypt kontrolny: /tmp/r08_audit35_independent.py. **Skończone obliczenia nie zastępują ogólnych dowodów**, ale niezależnie weryfikują wskazane własności i przypadki brzegowe.

## 4. Język, źródło i etykiety

R01–R08 pobrano ponownie przez API GitHub wyłącznie w celu rozwiązania odsyłaczy z R08. Z aktualnego źródła (blob ee4660de677bebbe11323f08f18efc5111b91968) otrzymano:
- **40 etykiet R08, 45 odsyłaczy, zero nierozwiązanych celów** w kontekście R01–R08;
- **0 powtórzonych etykiet**, 0 niesparowanych środowisk i 0 niezamkniętych środowisk;
- **0 naruszeń** terminologii: brak „sekwencji”, „zbieżność zdominowana”, „unia zbiorów”, „pierwszoprzeliczal”, „drugoprzeliczal” i zabronionych alternatyw oznaczania funkcji charakterystycznych;
- zachowane wszystkie 5 poprawek z audytu XXXIV, w tym niepustość rodziny UI, M≥0, zbiór wyjątkowy dla pochodnej i niepustość K w kryterium Darboux.

Nie zmieniono stabilnych etykiet ani tekstu R08.

## 5. Pełny CI i niezależna kontrola autentycznego PDF

Ponownie sprawdzono **rzeczywisty udany przebieg** [GitHub Actions 45152299851](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45152299851) na commicie 3bb895bbfeaf05d6136bec52bec71cbe0c013175. Dwa joby zakończyły się **completed SUCCESS (2/2)**. Po tym commicie do chwili rozpoczęcia niniejszego audytu nie zmieniono R08, testu ani workflow; nowsze commity dotyczyły innych prac i raportu XXXIV.

Przebieg wykonał:
- 3600 modeli MCT, 36864 Fatou, 1800 DCT, 256 wzoru warstwowego oraz kontrolę wszystkich odsyłaczy;
- **2 kompilacje izolowanego R08**, z oryginalną preambułą książki, 12 stron A4;
- **12/12 wyrenderowanych podglądów**, kontrolę Popplera: 6777 słów w obrębie granic stron;
- **3 kompilacje pełnej książki** — 257 stron, bez nierozwiązanych odsyłaczy i przepełnionych wierszy.

Ponownie niezależnie zbadano pobrany w poprzednim audycie prawdziwy PDF /mnt/data/r08_audit34/measure_theory_ch08_ci.pdf i wszystkie 12 podglądów. Obejrzano kontaktowy zestaw stron oraz szczegółowo stronę 11 z kryterium Riemanna. Dodatkowo PyMuPDF zidentyfikował **5594 słowa według własnej tokenizacji**, zero poza granicami stron; wynik różni się od 6777 Popplera z powodu różnych metod segmentacji. Prawdziwy log izolowanego PDF: **0 Overfull hbox, 0 Underfull hbox**. Log całej książki: **0 Overfull hbox, 0 nierozwiązanych odsyłaczy, 14 Underfull hbox** (wcześniej istniejące, nieblokujące problemy globalnego łamania, poza izolowanym R08).

Krótka strona 12 zawiera końcowe podsumowanie; nie zasłania dowodu ani wzorów i nie stanowi powodu do niestabilności. W izolowanym składzie odsyłacze do wcześniejszych rozdziałów mogą być przedstawiane jako nierozwiązane, lecz w pełnej książce są prawidłowo rozwiązane.

## 6. Osobna uwaga o integration_theory

W poprzednich audytach odnotowano globalną niespójność notacji w odrębnej książce integration_theory: makro funkcji charakterystycznej rozwijane do \mathbf 1 zamiast wymaganego \chi_A. Jest to **otwarte odrębne zadanie przekrojowe**, które nie dotyczy treści ani poprawności R08 i którego nie rozwiązywano w tej iteracji. Nie audytowano ani nie modyfikowano tej książki.

## 7. Formalna decyzja

**ROZDZIAŁ 08 — STABILNY / FORMALNIE ZATWIERDZONY.**

Uzasadnienie: audyt XXXIV wykazał i poprawił pięć rzeczywistych nieścisłości, po czym kompletne CI zakończyło się pomyślnie. Niniejszy **następny pełny, niezależny, czysty audyt XXXV po ostatniej poprawce** skontrolował wszystkie 27 dowodów, 9 przykładów, definicje, hipotezy, 40 etykiet, 45 odsyłaczy, terminologię, skład oraz autentyczny 12-stronicowy PDF. Nowych usterek nie wykazano, a źródło nie wymagało kolejnej zmiany.

**R01–R07 — STABILNE;** nie wykonywano ich audytów ani zmian w tej iteracji. **R09–R31 — nieaudytowane w tej iteracji.**

**Następna odrębna iteracja:** pierwszy szczegółowy audyt rozdziału 09, jeden rozdział na iterację. Nie rozpoczynano go w audycie XXXV.