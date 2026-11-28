# Logika matematyczna i teoria mnogości — audyt XII (potwierdzający) rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex`.  
**Blob rozdziału:** `1d510628d52469ef8aa00ad021125192c54ec439` (bez zmian od audytów X i XI).  
**Werdykt końcowy: AUDYT XII CZYSTY, ROZDZIAŁ 35 STABILNY (2/2+1).** Niezależny audyt potwierdzający nie znalazł kolejnych koniecznych poprawek. Pełne CI dla pierwotnego zapisu audytu XII zakończyło się sukcesem; sprawdzono rzeczywisty artefakt, log i wizualny wynik wszystkich stron rozdziału.

## 1. Ponowny dowód przypadków krytycznych

### 1.1. Boolowskie klauzule atomowe

Zbadano, czy jednoczesna rekurencja po rangach nazw rzeczywiście kończy się przy każdym wywołaniu, a wartości \(\llbracket\sigma=\tau\rrbracket\) i \(\llbracket\sigma\in\tau\rrbracket\) mieszczą się w ustalonej zupełnej algebrze. Obie klauzule odwołują się do nazw z dziedziny argumentów, o niższej randze. Indukcja po naturalnej sumie rang zabezpiecza rekurencję również przy przeplataniu równości i przynależności. Przy kwantyfikatorze \(\exists\) kres w algebrze jest kresem zbioru różnych wartości danej ustalonej formuły, a nie wielkości indeksowanej klasą właściwą.

### 1.2. Aksjomaty ZFC

- **Ekstensjonalność i wyróżnianie:** sprawdzono, że wartości przynależności dla arbitralnej nazwy \(\eta\), nie tylko literalnych argumentów dziedziny, pozwalają zastosować równość i zastępowanie równych.
- **Para, suma, nieskończoność:** klauzule dla nazw pary i sumy są dostępne jako konkretne konstrukcje nazw, zatem wystąpienie następnika \(\eta\cup\{\eta\}\) w dowodzie dla \(\check\omega\) nie zakłada aksjomatu nieskończoności w modelu boolowskim. Rozdzielność \(\wedge\) względem kresów górnych uzasadnia przejście od wszystkich \(\check n\) do dowolnej nazwy elementu \(\check\omega\).
- **Zbiór potęgowy:** \(T_\sigma\) jest rzeczywistym zbiorem funkcji o wartościach w \(\mathbb B\), z góry ograniczonych współczynnikami \(\sigma\). Dla dowolnej \(\tau\), na fragmencie \(b=\llbracket\tau\subseteq\sigma\rrbracket\), nazwa \(f_\tau\) daje równość z \(\tau\); nie wymaga zbieżności dosłownych dziedzin.
- **Zastępowanie:** przed wyborem rodziny \(\rho_\pi\) wykorzystuje się minimalne rangi i zastępowanie na *zbiorze* \(\operatorname{dom}\sigma\). Wykorzystana jednoznaczność wartości \(\varphi(x,y)\) dotyczy wyłącznie fragmentu \(b\), dokładnie jak wymagają kwantyfikatory schematu.
- **Ufundowanie:** kryterium minimalnej rangi stosuje się do wszystkich nazw \(\pi\), dla których \(c\wedge\llbracket\pi\in\sigma\rrbracket>0\), a nie tylko nazw bezpośrednio wypisanych w dziedzinie \(\sigma\). Własność przeciwprzykładu z nazwy \(\eta\in\operatorname{dom}\pi\) daje ściśle mniejszą rangę i sprzeczność.
- **Wybór:** indeksowanie starej dziedziny \(\sigma\) przez liczbę porządkową oraz nazwa surjekcji \(F:K\to\sigma\) pozwalają odzyskać dobre uporządkowanie przez najmniejszy przeciwobraz, bez zakładania uprzednio wyboru w modelu boolowskim.

### 1.3. Model ilorazowy i względna niesprzeczność

Sprawdzono niezależnie dwa kierunki kroku egzystencjalnego w lemacie prawdy. Z istnienia świadka w ilorazie wynika wartość należąca do ultrafiltru przez monotoniczność. W odwrotnym kierunku sam fakt \(\bigvee S\in U\) *nie* implikuje istnienia składnika \(s\in S\cap U\); konieczny jest lemat o pełności i pojedyncza nazwa \(\rho\) o wartości dokładnie równej kresowi. Ta nazwa istnieje wewnątrz dowolnego \(M\models\mathrm{ZFC}\), a otrzymany iloraz jest modelem zbiorowym także bez tranzytywności \(M\).

Osobno skontrolowano obydwa argumenty wymuszające: \(\operatorname{Add}(\omega,\omega_2)\) spełnia ccc, zachowuje \(\omega_1,\omega_2\) i dodaje przynajmniej \(\aleph_2\) różnych podzbiorów \(\omega\); \(\operatorname{Coll}(\omega_1,2^{\aleph_0})\) jest przeliczalnie domknięte, zachowuje \(\omega_1\) i podzbiory \(\omega\), a daje surjekcję na stary zbiór podzbiorów \(\omega\). Wniosek \(\operatorname{Con}(\mathrm{ZFC})\Rightarrow\operatorname{Con}(\mathrm{ZFC}+\mathrm{CH}/\neg\mathrm{CH})\) dotyczy dwóch osobnych teorii i wynika z pełności rachunku pierwszego rzędu; nie wyprowadza bezwarunkowej niesprzeczności ZFC.

## 2. Nowa próba odpornościowa (niezależna od testów repozytorium)

Przygotowano nowy, odrębny generator **223** niekanonicznych nazw boolowskich z rangami do czwartego poziomu rekurencji, także z zerowymi współczynnikami, powtórnymi wartościami semantycznymi i niejednakowymi rangami argumentów.

Dla \(\mathbb B=\mathcal P(\{0,1,2\})\) porównano bezpośrednią rekurencję \(\llbracket\sigma=\tau\rrbracket\), \(\llbracket\sigma\in\tau\rrbracket\) z trzema interpretacjami zbiorowymi po atomach \(1,2,4\). **54 000/54 000** porównań atomowych wartości równości i przynależności było zgodnych; ponadto **27 000/27 000** sprawdzeń nierówności przechodniości równości zakończyło się sukcesem. Wynik nie stanowi formalnego dowodu dla dowolnych algebr ani weryfikacji kodu Lean, lecz stanowi niezależną regresję semantyczną.

## 3. Przegląd całego pliku, redakcja i odsyłacze

Ponownie pobrano bieżący plik z GitHub i stwierdzono: **2406 wierszy, 28 różnych etykiet, 34 wystąpienia odsyłaczy, 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład i 14 dowodów.** Wszystkie środowiska LaTeX pozostają poprawnie sparowane. Nie znaleziono naruszeń sprawdzanych obowiązkowych określeń terminologicznych. Nie zmieniono ustalonego zakresu rozdziału.

Przed audytem XII audyt XI uzyskał **[SUCCESS w GitHub Actions 45062047392](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45062047392)**, a jego rzeczywisty artefakt PDF **14770295070** ma **311 stron**. Wykonano nowy montaż i wzrokową kontrolę wszystkich stron rozdziału 35 (**PDF 296–311**), bez zaobserwowanych kolizji. Log: **0** błędów LaTeX, **0** przepełnionych wierszy, **0** nierozwiązanych odsyłaczy, **0** brakujących znaków, jedno nieszkodliwe ostrzeżenie `Underfull \hbox`.

## 4. Końcowe CI audytu XII i porównanie artefaktów

GitHub Actions **[45062514837](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45062514837): SUCCESS**, commit `5de8fee615d868117c334cc0427ef58208198516`. Zakończono testy rozdziałów 01–35, pełną kompilację LaTeX, kontrolę referencji i logów oraz archiwizację. Pobrano rzeczywisty artefakt **14770295576**, zawierający PDF i log.

Nowy PDF ma **311 stron**, A4. Podczas inspekcji wszystkich 16 stron rozdziału 35 (strony PDF 296–311) wyrenderowano je ponownie w rozdzielczości 90 dpi i **porównano piksel po pikselu** z niezależnym renderem artefaktu audytu XI. **16/16 stron jest identycznych wizualnie**; tekst stron ma ten sam SHA-256 `d88130c65f8aa5287f509c4b0b1dd177479b6e31e9df6cb17053a42701189804`. W logu: **0** błędów LaTeX, **0** przepełnionych wierszy, **0** nierozwiązanych odsyłaczy, **0** brakujących znaków; **1** ostrzeżenie underfull w całej książce, bez obserwowanego wpływu na skład.

## 5. Końcowy werdykt i przejście dalej

**Audyt X — czysty (1/2), audyt XI — czysty (2/2), audyt XII — czysty (+1 potwierdzający). ROZDZIAŁ 35: STABILNY.** We wszystkich trzech audytach źródło pozostało tym samym blobem `1d510628d52469ef8aa00ad021125192c54ec439`. Żadna modyfikacja raportu nie zmienia źródła ani wyników matematycznych. Zamknięto etap rozdziału 35 bez dopisywania niezatwierdzonych rozszerzeń. Dalszy etap to ustalenie zakresu rozdziału 36 i jego szczegółowe opracowanie. Niezależne testy Python i kompilacja LaTeX nie oznaczają formalnej weryfikacji dowodów w Lean.
