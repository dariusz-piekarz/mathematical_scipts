# Algebra liniowa — rozdział 03, audyt 5 (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex`  
**SHA bloba rozdziału:** `7ee828f8438e6030cb7f47685433aa3639220ab7`  
**Zatwierdzony poprzedni CI dla identycznej treści:** [44904330466](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44904330466) — **success**.

## Cel i decyzja audytu

Piąta iteracja była **audytowaniem poprawności istniejącej treści**, nie rozszerzaniem zakresu. Sprawdzono matematyczne sformułowania, kompletność założeń, wszystkie istotne kroki dowodowe, przypadki brzegowe, przykłady, rysunki, odsyłacze oraz integralność kompilacji. Przyjęto standard szczegółowości wzorowany na rozdziale 01 skryptu „Geometria różniczkowa”.

**Wynik: nie wykryto nowego błędu ani istotnej luki w materiale. Nie zmieniono pliku rozdziału 03.** Jest to pierwsza czysta iteracja po audytach 1–4 zakończonych korektami.

## Szczegółowa weryfikacja dowodów

### Podstawowe odwzorowania i wartości na bazie

- Poprawne są równoważne warunki liniowości, zachowywanie wektora zerowego i wektorów przeciwnych oraz wszystkich skończonych kombinacji.
- Przedłużenie wartości przypisanych do wskazanej bazy Hamela jest dobrze określone dzięki jednoznaczności współrzędnych; dowód obejmuje pustą bazę i nie wymaga aksjomatu wyboru, gdy baza jest dana.
- Zgodność na zbiorze rozpinającym daje zgodność na całej przestrzeni.
- Przykłady wielomianowe są poprawne nad ciałami dowolnej charakterystyki, a przykład współrzędnych jawnie definiuje \(2_K=1_K+1_K\).

### Jądro, obraz i przestrzeń rozpięta

- Jądro i obraz są podprzestrzeniami; poprawne są kryteria iniektywności/surjektywności oraz własności przeciwobrazu podprzestrzeni.
- Równość \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\) ma teraz kompletny, poprawnie typowany dowód z osobnymi współczynnikami \(\lambda_j\in K\) i wektorami \(a_j\in A\), obejmujący \(A=\varnothing\).
- Równania dla operatorów \(T(p)=Xp\), \(R(p)=(p-p(0))/X\) oraz ich jąder i obrazów są poprawne i nie zależą od charakterystyki.

### Wymiar jądra i obrazu

- Przy aksjomacie wyboru rozwijamy bazę \(C\) jądra do \(B=C\sqcup D\); rodzina obrazów \(T(D)\) rozpina \(\operatorname{im}T\) i jest liniowo niezależna. Zatem \(\dim_KV=\dim_K\ker T+\dim_K\operatorname{im}T\), z dodawaniem kardynalnym.
- W przypadku skończenie wymiarowym cała konstrukcja baz jest skończona i niezależna od aksjomatu wyboru.
- Skrajne przypadki \(\ker T=\{0_V\}\), \(T=0\), zerowego obrazu i wymiaru zero mieszczą się w sformułowaniu oraz dowodzie. Nie odejmuje się nieskończonych liczb kardynalnych.

### Iloraz i izomorfizm na obraz

- Przyporządkowanie \(v+\ker T\mapsto T(v)\) jest dobrze określone, liniowe, iniektywne i surjektywne, bez użycia wyboru baz.
- Diagram TikZ rozróżnia poprawnie przeciwdziedziny: \(\widehat T\colon V\to\operatorname{im}T\), \(\widetilde T\colon V/\ker T\to\operatorname{im}T\) i włożenie \(\iota\colon\operatorname{im}T\hookrightarrow W\).
- Warunek faktoryzacji \(T=S\circ\pi_U\iff U\subseteq\ker T\) jest wyprowadzony bez luki.

### Odwrotności, przestrzenie odwzorowań i projekcje

- Liniowość złożeń i odwrotności bijekcji liniowych jest uzasadniona. W przypadku skończonego wymiaru poprawnie wykazano równoważność iniektywności, surjektywności i bijektywności pomiędzy przestrzeniami tego samego wymiaru.
- Konstrukcja baz \(\operatorname{Hom}_K(V,W)\) przez odwzorowania \(E_{ji}\) ma \(mn\) elementów i poprawnie obejmuje \(m=0\), \(n=0\).
- \(\operatorname{End}_K(V)\) jest łączną algebrą z jedynką, z uwzględnieniem przestrzeni zerowej. Pokazano poprawny kontrprzykład dla przemienności.
- W przypadku projekcji warunek \(P^2=P\) jest prawidłowo równoważny sumie prostej \(\operatorname{im}P\oplus\ker P\) wraz z identycznością \(P\) na obrazie. Sprawdzono obydwa kierunki i konstrukcję projekcji z wybranego dopełnienia.
- Przykłady i kontrprzykłady są zgodne z ogólnymi twierdzeniami.

## Niezależne testy na przestrzeniach skończonych

Niezależnie wyliczono wszystkie \(81\) liniowych endomorfizmów \(\mathbb F_3^2\) i wszystkie \(512\) podzbiorów \(\mathbb F_3^2\), a także \(6\) podprzestrzeni tej przestrzeni.

- Dla wszystkich **81** odwzorowań sprawdzono kardynalny odpowiednik wzoru wymiarowego \(|V|=|\ker T|\cdot|\operatorname{im}T|\), zgodność klas \(V/\ker T\) z wartościami na obrazie oraz równoważność definicji projekcji z sumą prostą i identycznością na obrazie. Stwierdzono 14 projekcji.
- Dla **41472** par \((T,A)\) sprawdzono równość zbiorów \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\).
- Dla **486** par \((T,U)\), gdzie \(U\) jest podprzestrzenią, sprawdzono dobrze określoną faktoryzację \(S(v+U)=T(v)\) dokładnie wtedy, gdy \(U\subseteq\ker T\).

**Wynik: 0 rozbieżności.** Testy wspierają audyt, ale nie zastępują ogólnych dowodów.

## Integralność książki i zgodność redakcyjna

- Rozdziały 01–03 zawierają **150 unikalnych etykiet**, bez duplikatów.
- Wszystkie **62** wystąpienia `\\ref`/`\\eqref` posiadają cele.
- Wszystkie `\\begin`/`\\end` są zgodne; nie ma niedomkniętych środowisk.
- Zachowano „suma zbiorów” i „warunek niezależności liniowej”, bez niedozwolonej terminologii w prozie i bez zmiany historycznych identyfikatorów `\\label`.
- Nie ma zewnętrznych plików graficznych w rozdziałach 01–03; diagram faktoryzacji jest integralnym TikZ.
- Kolejność `\\input` i katalog książki są poprawne.
- Plik rozdziału 03 jest bajtowo identyczny z wersją, dla której CI [44904330466](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44904330466) zakończyło się sukcesem. Ten przebieg wygenerował poprawny **37-stronicowy PDF**; w audycie 4 sprawdzono wizualnie poprawiony dowód i brak problemów ze składem.

W `books/pl/linear_algebra.tex` zaktualizowano wyłącznie nieaktualny komentarz statusu rozdziałów 01–03, bez zmian w treści ani układzie książki. Nowy przebieg CI po tej aktualizacji: [44904794591](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44904794591) — **success**. Wszystkie kroki CI dla rozdziałów 01–03 zaliczone: weryfikacja katalogu i importów, spójność etykiet i terminologii, kompilacja PDF oraz kontrola odsyłaczy i zapis artefaktu. Pobraną końcową wersję PDF zweryfikowano: **37 stron A4**, brak ostrzeżeń `LaTeX Warning`, `Overfull`, `Underfull`, `Missing character`, `Undefined control sequence`, `Fatal error` i `There were undefined references` w końcowym pliku `linear_algebra.log`. Wizualnie sprawdzono **strony 30, 31, 33 i 37**, w tym poprawiony wcześniej dowód przestrzeni rozpiętej i diagram pierwszego twierdzenia o izomorfizmie; bez ucięć, nieczytelnych symboli ani kolizji. Ostatnia strona zawiera krótkie podsumowanie, bez potrzeby skracania dowodów.

W nieblokującym walidatorze globalnym istnieje **24 wcześniejszych zgłoszeń** innych skryptów; nie utożsamia się ich z problemami w algebrze liniowej.

## Status

**Rozdział 03 jest stabilny i zostaje zamknięty po audycie 5 bez zmian merytorycznych oraz po pomyślnym końcowym CI 44904794591.** Kolejny audyt rozdziału 03 nie jest wymagany w obecnym cyklu. Na prośbę użytkownika można rozpocząć rozdział 04, bez ponownego rozszerzania zatwierdzonych rozdziałów 01–03.
