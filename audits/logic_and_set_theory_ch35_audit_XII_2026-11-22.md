# Logika matematyczna i teoria mnogości — audyt XII (potwierdzający) rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex`.  
**Blob rozdziału:** `1d510628d52469ef8aa00ad021125192c54ec439` (bez zmian od audytów X i XI).  
**Werdykt merytoryczny:** niezależny audyt potwierdzający nie znalazł kolejnych koniecznych poprawek. **Zamknięcie techniczne** wymaga zielonego CI uruchomionego zapisem tego raportu.

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

## 2. Nowa próba adversarialna (niezależna od testów repozytorium)

Przygotowano nowy, odrębny generator **223** niekanonicznych nazw boolowskich z rangami do czwartego poziomu rekurencji, także z zerowymi współczynnikami, powtórnymi wartościami semantycznymi i niejednakowymi rangami argumentów.

Dla \(\mathbb B=\mathcal P(\{0,1,2\})\) porównano bezpośrednią rekurencję \(\llbracket\sigma=\tau\rrbracket\), \(\llbracket\sigma\in\tau\rrbracket\) z trzema interpretacjami zbiorowymi po atomach \(1,2,4\). **54 000/54 000** porównań atomowych wartości równości i przynależności było zgodnych; ponadto **27 000/27 000** sprawdzeń nierówności przechodniości równości zakończyło się sukcesem. Wynik nie stanowi formalnego dowodu dla dowolnych algebr ani weryfikacji kodu Lean, lecz stanowi niezależną regresję semantyczną.

## 3. Przegląd całego pliku, redakcja i odsyłacze

Ponownie pobrano bieżący plik z GitHub i stwierdzono: **2406 wierszy, 28 różnych etykiet, 34 wystąpienia odsyłaczy, 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład i 14 dowodów.** Wszystkie środowiska LaTeX pozostają poprawnie sparowane. Nie znaleziono naruszeń sprawdzanych obowiązkowych określeń terminologicznych. Nie zmieniono ustalonego zakresu rozdziału.

Przed audytem XII audyt XI uzyskał **[SUCCESS w GitHub Actions 45062047392](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45062047392)**, a jego rzeczywisty artefakt PDF **14770295070** ma **311 stron**. Wykonano nowy montaż i wzrokową kontrolę wszystkich stron rozdziału 35 (**PDF 296–311**), bez zaobserwowanych kolizji. Log: **0** błędów LaTeX, **0** przepełnionych wierszy, **0** nierozwiązanych odsyłaczy, **0** brakujących znaków, jedno nieszkodliwe ostrzeżenie `Underfull \hbox`.

## 4. Werdykt i przejście dalej

**Czyste audyty X i XI: 2/2. Audyt XII merytorycznie czysty — dodatkowy audyt potwierdzający.** Warunkiem końcowego oznaczenia stabilności jest potwierdzony, ukończony zielony przebieg CI dla zapisu raportu XII. Po tym można zakończyć etap rozdziału 35 bez dopisywania niezatwierdzonych rozszerzeń i przejść do uzgodnienia zakresu następnego rozdziału. Niezależne testy Python i kompilacja LaTeX nie oznaczają formalnej weryfikacji dowodów w Lean.
