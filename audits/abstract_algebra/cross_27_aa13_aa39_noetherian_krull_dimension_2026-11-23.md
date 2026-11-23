# Algebra abstrakcyjna — audyt przekrojowy AA-X27: noetherowskość a wymiar Krulla (AA-13/AA-39)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD przed zapisem:** `719a01df197324b8f3a0ec13fbdd59544c8251b8`.

## Weryfikacja stanu i niepowtarzalności

Odczytano pełne drzewo GitHub (nieucięte), listę 50 źródeł `chapters/pl/abstract_algebra`, listę raportów `audits/abstract_algebra` (ostatni numer AA-X26), `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md` i `catalog/books.json`. W źródłach i katalogu istnieją AA-01–AA-50; AA-51 nie istnieje. Ten audyt bada *nowe powiązanie* między AA-13 (warunek łańcuchów wstępujących, twierdzenie Hilberta o bazie) a AA-39 (łańcuchy **ideałów pierwszych** i wymiar Krulla). Nie powtarza audytu AA-X06 (AA-09/12/13/14) ani AA-X07 (AA-37–40).

Źródła: AA-13 blob `548155ff626fd172691bd241c1240015edae197a` (493 wiersze); AA-39 blob `1b8990241d26cbf461a0e7b4a07546a3ef77fa9e` (565 wierszy). Brak zmian źródłowych.

## Kontrola matematyczna

1. **Nie mylić ACC z wymiarem skończonym.** AA-13:26–35 definiuje noetherowskość przez skończone generowanie wszystkich ideałów i równoważny ACC dla *wszystkich* ideałów. AA-39:15–27 definiuje wymiar jako supremum długości *skończonych ściśle rosnących łańcuchów ideałów pierwszych*. ACC nie zapewnia wspólnego skończonego ograniczenia długości wszystkich łańcuchów; rozdziały nie wyprowadzają błędnej implikacji. Wymiar nieskończony AA-39:515–535 jest wykazany dla pierścienia nieskończenie wielu zmiennych, a AA-13:199–213 wykazuje jego nienoetherowskość. Przykład nie rozstrzyga odwrotnej implikacji w ogólności.
2. **Ilorazy i lokalizacje.** AA-13:56–96 dowodzi zachowania noetherowskości przez iloraz i lokalizację, AA-39:78–153 i 154–238 podaje odpowiednio bijekcje ideałów pierwszych, które zachowują i odzwierciedlają ścisłe inkluzje. Wynikające stąd nierówności wymiarów wymagają niezerowości ilorazu/lokalizacji; AA-39:115–120, 205–210 wyraźnie ją zapewnia. W AA-39:132–153 redukcja przez nilradykał zachowuje spektrum i wymiar.
3. **Skończone generowanie nie ogranicza wymiaru do zera ani jednego.** AA-13:258–344 dowodzi noetherowskości K[U,V] na mocy twierdzenia Hilberta. AA-39:268–336 niezależnie wyprowadza wymiar 2, używając faktoryzacji w UFD, usunięcia mianowników i skończonego wymiaru K-algebry ilorazowej przez (f,g). Sprawdzono przypadek f lub g stałego względem jednej zmiennej: w K(U)[V] taki niezerowy element jest jednostką, więc tożsamość Bézouta nadal istnieje; po usunięciu mianowników otrzymuje się niezerowy wielomian w K[U]. Przypadek stałej niezerowej h lub k jest wyodrębniony w AA-39:300–302.
4. **Kontrprzykłady do błędnych utożsamień.** AA-13:98–131 pokazuje, że lokalny pierścień K[x,y]_(x,y) jest noetherowski, lecz jego ideał maksymalny nie jest główny. AA-39:491–513 wykazuje wymiar zero pierścienia K[T]/(T²), który nie jest ciałem. AA-39:439–466 wykazuje różne wysokości ideałów maksymalnych w iloczynie K[T] × K[U,V]. Wszystkie te przykłady są zgodne z rozróżnieniem między skończonym generowaniem, głównością ideałów i wymiarem.
5. **Przypadki brzegowe.** AA-13 dopuszcza pierścień zerowy i pusty układ generatorów, AA-39:10–36 jawnie wyklucza pierścień zerowy z definicji wymiaru; nie ma sprzeczności, ale konwencje nie są identyczne. AA-39:241–266 prawidłowo wyodrębnia ciało (wymiar 0) spośród dziedzin ideałów głównych.

**Wynik tej konkretnej kontroli:** nie znaleziono sprzeczności ani koniecznej korekty w sprawdzonych twierdzeniach, dowodach i przykładach. To nie jest ponowny pełny audyt wszystkich twierdzeń AA-13 i AA-39.

## Niezależny test skończonych modeli

Lokalnie wykonano krótki skrypt Python enumerujący ideały Z/nZ jako podzbiory, sprawdzający pierwszość przez definicję i wszystkie ścisłe zawierania ideałów pierwszych, dla n=6,12,30. Wyniki: odpowiednio 4/6/8 ideałów, 2/2/3 ideały pierwsze, **0** ścisłych zawierań między ideałami pierwszymi, wymiar 0 w każdym przypadku. Trzy modele zgodne z AA-39:468–487; nie stanowią dowodu ogólnego twierdzenia. Lokalny test zakończył się bez błędu (3/3 modeli).

## Kontrola techniczna i ograniczenia

Przeczytano źródła i sprawdzono kontekst istotnych etykiet oraz odsyłaczy (m.in. `aa:tw:hilbert-basis`, `aa:lem:krull-plane-dimension`, `aa:tw:krull-localization-primes`). Zachowano wszystkie istniejące `\\label` i `\\ref`. Nie przeprowadzono pełnej automatycznej kontroli odsyłaczy całej książki, kompilacji LaTeX, wizualnej inspekcji PDF ani nowego CI: lokalny `git ls-remote` nie zadziałał z powodu DNS, a pełne środowisko repozytorium nie było dostępne lokalnie. **Brak deklaracji PASS dla LaTeX, PDF i CI.** Nie modyfikowano zatwierdzonych rozdziałów, więc nie resetowano liczników czystych audytów.

**Propozycja (bez zmiany źródeł):** przy okazji przyszłego rozszerzenia materiału warto dodać osobny, uzasadniony przykład noetherowskiego pierścienia o nieskończonym wymiarze Krulla; unaoczniłby, dlaczego ACC nie ogranicza globalnie długości skończonych łańcuchów. Wymaga zgody przed dodaniem.

**Werdykt:** AA-X27 — ukończony audyt *wybranego powiązania*, bez wykrytej koniecznej poprawki; techniczna weryfikacja całej książki nieodbyta. **Następny krok:** odczytać nowy HEAD, sprawdzić istnienie AA-51; przy jego braku wybrać inne, nieobjęte AA-X01–X27 powiązanie i przeprowadzić dokładnie jeden nowy audyt.

## AA-X27 — niezależne testy i szczegółowy dowód powiązania ACC z wymiarem

Kontynuacja poprzedniej, ograniczonej kontroli AA-13 × AA-39. Zgodnie z AGENTS.md **nie dodano materiału do zatwierdzonych rozdziałów**. Nowy audyt zachowuje ich oryginalne etykiety, sformułowania i treści, a konfrontuje konsekwencje noetherowskości z operacjami na spektrum i rzeczywistymi skończonymi modelami.

### 1. Trzy niezależne własności pierścieni i przypadek pierścienia zerowego

Niech \(R\) będzie przemiennym pierścieniem z jedynką. Pierścień \(R\) jest noetherowski dokładnie wtedy, gdy wszystkie jego ideały są skończenie generowane, co równoważnie oznacza spełnianie warunku łańcuchów wstępujących (ACC) dla **wszystkich** ideałów. Gdy \(R\ne0\), jego wymiar Krulla to supremum liczb \(r\) takich, że istnieją **ideały pierwsze** \(P_0\subsetneq P_1\subsetneq\cdots\subsetneq P_r\). Wymiar 0 oznacza, że każdy ideał pierwszy jest maksymalny, a nie że \(R\) jest ciałem ani że każdy ideał jest główny.

ACC wyklucza jeden nieskończony ściśle rosnący łańcuch ideałów. Nie oznacza to jednak istnienia **jednego skończonego ograniczenia** na długości wszystkich skończonych łańcuchów ideałów pierwszych. Istnieją noetherowskie pierścienie nieskończonego wymiaru Krulla (klasyczne przykłady Nagaty); dowód ich konstrukcji wykracza poza badane rozdziały i nie jest tu zastępowany przykładami nienoetherowskimi. W szczególności skończone pierścienie \(\mathbb Z/2^e\mathbb Z\) mają wymiar 0, lecz przy zmiennym \(e\) długość ich **łańcuchów wszystkich ideałów** rośnie bez ograniczenia. To nie jest przykład pojedynczego pierścienia noetherowskiego o nieskończonym wymiarze.

Zachowano konwencję AA-39: dla pierścienia zerowego nie nadajemy automatycznie wymiaru 0; przy ilorazie lub lokalizacji otrzymującym pierścień zerowy nie stosujemy nierówności wymiarów bez jawnej konwencji.

### 2. Obraz ideałów pierwszych przy ilorazie i lokalizacji: pełne uzasadnienie

**Twierdzenie.** Niech \(R\) będzie noetherowski, \(I\lhd R\), a \(S\subseteq R\) zbiorem multiplikatywnym zawierającym \(1\). Wówczas \(R/I\) i \(S^{-1}R\) są noetherowskie. Jeśli odpowiednio \(R/I\ne0\) i \(0\notin S\), to
\[
\operatorname{Spec}(R/I)\cong\{P\in\operatorname{Spec}R:I\subseteq P\},\qquad
\operatorname{Spec}(S^{-1}R)\cong\{P\in\operatorname{Spec}R:P\cap S=\varnothing\},
\]
przy czym oba odwzorowania zachowują **i odzwierciedlają** ścisłe zawierania. Stąd \(\dim(R/I)\le\dim R\) oraz \(\dim(S^{-1}R)\le\dim R\) (również wtedy, gdy wymiar prawej strony jest nieskończony).

**Dowód noetherowskości ilorazu.** Dowolny ideał \(J\lhd R/I\) jest postaci \(J=J'/I\), gdzie \(J'\lhd R\) i \(I\subseteq J'\). Wybierzmy skończony układ generatorów \(a_1,\dots,a_t\) ideału \(J'\). Ich obrazy generują \(J'/I\) w \(R/I\). Ten argument obejmuje także ideał zerowy i pierścień zerowy.

**Dowód noetherowskości lokalizacji.** Dowolny ideał \(J\lhd S^{-1}R\) jest rozszerzeniem kontrakcji \(I=\{a\in R:a/1\in J\}\): dla \(a/s\in J\) mamy \(a/1=(s/1)(a/s)\in J\), a dla \(a/1\in J\) otrzymujemy \(a/s\in J\), gdyż \(s/1\) jest jednostką. Ponieważ \(I=(a_1,\dots,a_t)\), ideał \(J\) jest generowany przez \(a_1/1,\dots,a_t/1\).

**Odpowiedniość spektrów.** Dla ilorazu homomorfizm \(R\twoheadrightarrow R/I\) daje bijekcję między ideałami pierwszymi ilorazu i ideałami pierwszymi \(R\) zawierającymi \(I\), a inkluzje zachowują się przez branie obrazu i przeciwobrazu. Dla lokalizacji ideał pierwszy \(Q\lhd S^{-1}R\) ma kontrakcję \(P\lhd R\) rozłączną z \(S\), bo wszystkie \(s/1\) są jednostkami. Odwrotnie, dla \(P\cap S=\varnothing\) ideał \(S^{-1}P\) jest pierwszy: iloraz \(S^{-1}R/S^{-1}P\) jest lokalizacją dziedziny \(R/P\) po niezerowych obrazach \(S\), więc jest dziedziną. W obydwu kierunkach kontrakcja i rozszerzenie są wzajemnie odwrotne dla takich ideałów pierwszych. Ścisła inkluzja dwóch odpowiadających ideałów pozostaje ścisła, bo bijekcja jest zgodna z inkluzją w obu kierunkach. Każdy skończony łańcuch w obrazie spektralnym daje więc równie długi łańcuch w \(\operatorname{Spec}R\), co dowodzi nierówności wymiarów. **Koniec dowodu.**

### 3. Dokładne obliczenia wymiaru noetherowskich ilorazów

Niech \(k\) będzie dowolnym ciałem i \(R=k[X,Y]\), który jest noetherowski na mocy twierdzenia Hilberta i ma wymiar 2 na mocy AA-39.

**Pierścień przecinających się prostych.** W \(A=R/(XY)\) ideały \(\mathfrak p_X=(X)/(XY)\) i \(\mathfrak p_Y=(Y)/(XY)\) są różnymi ideałami pierwszymi, gdyż ich ilorazy są izomorficzne odpowiednio z \(k[Y]\) i \(k[X]\). Oba są ściśle zawarte w ideale maksymalnym \(\mathfrak m=(X,Y)/(XY)\), ponieważ \(A/\mathfrak m\cong k\). Zatem \(\dim A\ge1\). Jeśli \(P\) jest dowolnym ideałem pierwszym \(R\) zawierającym \(XY\), to z pierwszości \(X\in P\) lub \(Y\in P\). W pierwszym przypadku cały łańcuch ideałów pierwszych ponad \(P\) można przenieść do \(\operatorname{Spec}(R/(X))\cong\operatorname{Spec}k[Y]\), która ma wymiar 1; w drugim do \(\operatorname{Spec}k[X]\). W dowolnym łańcuchu ideałów pierwszych \(P_0\subsetneq\cdots\subsetneq P_r\) zawierających \(XY\) ideał początkowy \(P_0\) zawiera \(X\) albo \(Y\), a zatem tak samo czynią wszystkie wyższe ideały. Stąd \(r\le1\). Otrzymujemy **\(\dim k[X,Y]/(XY)=1\)**.

**Redukcja nilpotentów.** Niech \(B=R/(X^2)\). Klasa \(X\) jest w \(B\) niezerowa, lecz jej kwadrat jest zerem. Pierwiastek ideału \((X^2)\) w \(R\) jest \((X)\), ponieważ \(R/(X)\cong k[Y]\) jest dziedziną, więc \((X)\) jest pierwszy, a jeśli \(f^j\in(X^2)\), to \(f\in(X)\). Stąd \(\sqrt{(0)}\subset B\) jest dokładnie ideałem generowanym przez klasę \(X\) i \(B/\sqrt{(0)}\cong k[Y]\). Każdy ideał pierwszy zawiera wszystkie elementy nilpotentne, więc redukcja indukuje bijekcję spektrów zachowującą zawierania; **\(\dim B=1\)** mimo obecności niezerowego elementu nilpotentnego.

**Skończony lokalny pierścień niebędący pierścieniem ideałów głównych.** Niech \(C=\mathbb F_2[X,Y]/(X^2,Y^2)\). Jego elementy mają jednoznaczne postacie \(a+bX+cY+dXY\), gdzie \(a,b,c,d\in\mathbb F_2\), więc \(|C|=16\) i \(C\) jest noetherowski. Ideał \(\mathfrak m=(X,Y)/(X^2,Y^2)\) składa się dokładnie z 8 elementów o zerowym wyrazie stałym, a \(\mathfrak m^3=0\). Jeśli element ma wyraz stały równy \(1\), to jest postaci \(1+u\), \(u\in\mathfrak m\), i \((1+u)^{-1}=1+u+u^2\) (w rzeczywistości \(u^2=0\) w charakterystyce 2). Zatem zbiór niejednostek to dokładnie \(\mathfrak m\), a \(C/\mathfrak m\cong\mathbb F_2\); \(\mathfrak m\) jest jedynym ideałem pierwszym, bo dowolny ideał pierwszy zawiera nilradykał, który tutaj równa się \(\mathfrak m\). Otrzymujemy **\(\dim C=0\)**.

Mimo wymiaru zero i noetherowskości \(\mathfrak m\) nie jest ideałem głównym. Istotnie, \(\mathfrak m^2=(XY)\), więc \(\mathfrak m/\mathfrak m^2\) ma wymiar 2 nad \(C/\mathfrak m\cong\mathbb F_2\), z bazą daną przez klasy \(X,Y\). Gdyby \(\mathfrak m=(f)\), iloraz \(\mathfrak m/\mathfrak m^2\) byłby generowany przez klasę jednego elementu \(f\) nad \(C/\mathfrak m\), sprzecznie z wymiarem 2. **Koniec dowodu.**

### 4. Trwałe testy i odpowiedzialne granice weryfikacji

Utworzono moduł tools/tests/test_abstract_algebra_cross_aa13_39.py, zawierający **8 testów regresyjnych**:
1. dokładna enumeracja wszystkich ideałów i definicyjna kontrola pierwszości w \(\mathbb Z/n\mathbb Z\) dla \(n=2,4,6,12,18,30,36,48,72\), wraz z nilradykałem;
2. odpowiedniość spektrów ilorazów \((\mathbb Z/n)/(d)\cong\mathbb Z/d\), w tym pierścień zerowy;
3. lokalizacje \((\mathbb Z/n)[1/s]\cong\mathbb Z/m\), gdzie \(m=\prod_{p^e\parallel n,\ p\nmid s}p^e\), niezależna kontrola jądra przez zabijanie potęgą \(s\) i filtrowanie ideałów pierwszych;
4. **wyczerpująca kontrola wszystkich \(2^{16}=65536\) podzbiorów** pierścienia \(C=\mathbb F_2[X,Y]/(X^2,Y^2)\), identyfikująca dokładnie **7 ideałów i jedyny ideał pierwszy**;
5. ścisłe zawierania ideałów \((XY)\subsetneq(X),(Y)\subsetneq(X,Y)\), niegłówność ideału maksymalnego \(C\) i znikanie \(\mathfrak m^3\);
6. kontrola **1024** wielomianów z nośnikiem na jednomianach stopnia całkowitego co najwyżej 3 w \(\mathbb F_2[X,Y]\): przecięcie \((X)\cap(Y)=(XY)\), pierwiastek \(\sqrt{(X^2)}=(X)\) oraz przypadki brzegowe;
7. zbiory ideałów \(\mathbb Z/2^e\mathbb Z\) dla \(1\le e\le8\): różnica między rosnącymi długościami skończonych łańcuchów **wszystkich** ideałów i stałym wymiarem Krulla zero;
8. globalna unikatowość etykiet i poprawność odsyłaczy wszystkich 50 rozdziałów, w tym **41 etykiet i 18 odsyłaczy** w AA-13 i AA-39.

Testy skończonych modeli nie zastępują twierdzenia ogólnego ani formalizacji Lean. Niezależna wizualna inspekcja PDF nie jest wykonywana. Żaden nowy przykład ani twierdzenie nie został dodany do zatwierdzonych rozdziałów: zgodnie z AGENTS.md ewentualny dodatek o noetherowskim pierścieniu nieskończonego wymiaru Krulla pozostaje **opcjonalną propozycją** i wymaga wyraźnej zgody.

Do workflow .github/workflows/abstract-algebra-chapter.yml podłączono osobny wyzwalacz i krok **Run AA-X27 Noetherian ACC and Krull dimension checks**; commit bramki **bcc704aa6f72c5579ab26a8ac91bfb032b01846a**.

**Werdykt przy zapisaniu suplementu: W STABILIZACJI CI**, bez deklaracji końcowego PASS. Warunkiem zamknięcia jest 8/8 nowych testów, zielony pełny workflow, kompilacja AA-01–AA-50 i automatyczna kontrola referencji oraz PDF. Rzeczywisty wynik CI zostanie wpisany do raportu po weryfikacji dokładnego przebiegu i SHA.

## Zamknięcie AA-X27 — weryfikacja GitHub Actions i stabilizacja

**Niezmienny przebieg referencyjny:** [GitHub Actions 45271071179](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45271071179), commit testowo-workflowowy **bcc704aa6f72c5579ab26a8ac91bfb032b01846a**. Status: **completed / success**. Job validate-cli ID **138030698790**: **105/105 ukończonych kroków**, bez błędów.

Odczytano bezpośrednio rzeczywisty log tego jobu. Wszystkie **8/8 testów AA-X27 mają wynik ok**, każda funkcja zarówno przy globalnym odkrywaniu testów, jak i w osobnym kroku Run AA-X27 Noetherian ACC and Krull dimension checks. Globalny zbiór regresji oraz pozostałe kontrole rozdziałów przeszły.

**Kompilacja AA-01–AA-50:** krok Compile AA-01 to AA-50 book with latexmk — **success**. Krok Verify PDF and references (no undefined refs) — **success**. Artefakt abstract-algebra-aa01-aa50, ID **14865507715**, ZIP **2 289 387 bajtów**, nieprzedawniony przy kontroli. Automatyczny skład i weryfikacja odsyłaczy, cytowań oraz przepełnionych pól w logu **nie zastępują osobnej wizualnej inspekcji stron PDF**; w tym audycie jej nie wykonano.

**Werdykt: AA-X27 ZAMKNIĘTY / STABILNY** dla szczegółowo opisanego interfejsu AA-13 × AA-39, z udowodnionym zachowaniem noetherowskości i specyfiką wymiaru Krulla dla ilorazów, lokalizacji i przykładów niecałkowitych. Żadna istotna korekta zatwierdzonych rozdziałów nie okazała się konieczna; wszystkie AA-01–AA-50 pozostają niezmienione. Globalny audyt wszystkich dowodów tomu pozostaje osobnym zadaniem. Osiem regresji to nie formalizacja w Lean.

**Propozycja do osobnego zatwierdzenia:** rozbudować AA-39 o uzasadniony przykład noetherowskiego pierścienia nieskończonego wymiaru Krulla; nie wprowadzono takiego rozszerzenia automatycznie, zgodnie z AGENTS.md. Nie mylić tej propozycji z już udowodnionymi skończonymi przykładami.

**Kolejna odrębna iteracja:** AA-X28, wyłącznie nowy zakres, po zamknięciu obecnego audytu.
