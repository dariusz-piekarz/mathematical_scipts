# AA-X25 — audyt przekrojowy AA-30 ↔ AA-36: konstruowalność i grupy Galois wielomianów ogólnych

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD ponownie odczytany bezpośrednio przed zapisem:** `8b4d8bb3ab0e9b37222b49f3dc00f054c78a51a4` (zmienił się w trakcie odczytów z początkowego `b0b6f4ef44ae40980653cfc7667d92d2bc208dd2`; zapis nowego raportu nie nadpisuje źródeł).

## Stan i zakres
Pełne drzewo GitHub (2409 wpisów, `truncated=false`) potwierdza 50 plików źródłowych AA-01–AA-50, brak AA-51 i raporty przekrojowe do AA-X24. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/konwencje_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md`, `catalog/books.json`, `books/pl/abstract_algebra.tex`, ostatni raport AA-X24 i źródła AA-30/AA-36. Audyt X25 nie powtarza X24 (Eisenstein/cyklotomiczne) ani X11 (ciała skończone/konstrukcje): dotyczy granicy pomiędzy kryterium konstruowalności a twierdzeniem o grupie Galois wielomianu ogólnego.

Źródła: AA-30 blob `f9d6e4e96d41e3faba57f9c9f895c99611c12998` (536 wierszy); AA-36 blob `4c7f5c055172ff88331978592b89d4c44d5584dc` (301 wierszy). Brak zmian źródeł.

## Kontrola matematyczna
1. AA-30, wiersze 205–217: konstruowalność liczby rzeczywistej implikuje stopień będący potęgą 2, lecz implikacja odwrotna jest fałszywa. Wiersze 267–386 dają konkretny wielomian `f=X^4-X-1`: nierozkładalny stopnia 4, ale o grupie Galois `S_4`, zatem żaden jego rzeczywisty pierwiastek nie jest konstruowalny. Kluczowe jest użycie **domknięcia normalnego wieży kwadratowej**, a nie nieuprawnionego twierdzenia, że każda grupa Galois wielomianu stopnia `2^m` jest 2-grupą.
2. Niezależnie sprawdzono rozkład `f mod 7=(X-3)(X^3+3X^2+2X-2)`, nierozkładalność czynnika sześciennego nad `F_7`, nierozkładalność `f mod 2`, nierozkładalność rezolwenty `R=Y^3+4Y-1` nad `Q`, a także `disc(f)=disc(R)=-283`. Każdy z tych faktów zgadza się z AA-30, wiersze 273–370. Rozumowanie o rzędzie grupy (podzielność przez 3 i 4, następnie transpozycja wykluczająca `A_4`) jest poprawne.
3. AA-36, wiersze 54–117: dla algebraicznie niezależnych `t_i` i dowolnego ciała `k` grupa Galois ogólnego wielomianu monicznego stopnia `n≥2` jest `S_n`; niezależność pierwiastków `x_i` zapewnia rozdzielczość także w dodatniej charakterystyce. Nie wolno przenosić tego twierdzenia bezpośrednio na **dowolną specjalizację współczynników**. AA-30 podaje szczególny, osobno sprawdzony przykład `S_4`, a nie wniosek ze specjalizacji ogólnego `S_4`.
4. Dla `n≥5` nierozwiązalność `S_n` przez pierwiastniki z AA-36 nie jest tożsama z niemożliwością konstrukcji cyrklem i linijką. Dla `n=4` grupa `S_4` jest rozwiązalna, ale nie jest 2-grupą: przykład AA-30 poprawnie rozdziela te pojęcia.
5. AA-30, wiersze 402–483: kryterium `φ(n)` będącego potęgą 2 dla wielokątów foremnych wykorzystuje **abelowość** grupy cyklotomicznej i wieżę podgrup indeksu 2, a nie jedynie liczbową przeszkodę stopnia. Niezależny test dla `3≤n≤100` potwierdził 98 klasyfikacji na podstawie faktoryzacji `n`; nie zastępuje dowodu ogólnego.
6. Niezależne obliczenia w Python/SymPy, wykonane w tej iteracji: **6 testów podstawowych** (nierozkładalności, wyróżniki, rozkład modulo 7) oraz **11 kontroli stopni formalnych wielomianów ogólnych** i **98 klasyfikacji n-kątów**, wszystkie zakończone bez błędu. Testy formalnych stopni nie są dowodem twierdzenia Galois.

## Statusy
- **Matematyka (wybrany interfejs AA-30/AA-36):** nie znaleziono sprzeczności w kontrolowanych twierdzeniach, hipotezach i przykładzie `X^4-X-1`. Nie jest to pełny ponowny audyt wszystkich dowodów tych dwóch rozdziałów.
- **Terminologia:** w analizowanych fragmentach nie stwierdzono naruszeń odczytanych zasad. **Odsyłacze:** kontrola logiczna wybranych zależności; nie przeprowadzono pełnego testu wszystkich `\\label`/`\\ref` w książce.
- **Nowa kompilacja LaTeX:** NIE WYKONANO. **Wizualna inspekcja PDF:** NIE WYKONANO. **Nowe CI:** NIE URUCHOMIONO / NIEZWERYFIKOWANO. Żaden z tych statusów nie jest PASS.
- **Korekty:** 0. **Stabilność:** brak nowej deklaracji.

## Propozycje bez zmiany zatwierdzonych rozdziałów
Opcjonalnie dodać do AA-36 krótkie porównanie „rozwiązywalność przez pierwiastniki” versus „konstruowalność cyrklem i linijką” z odsyłaczem do kontrprzykładu `X^4-X-1` z AA-30. Wymaga osobnej zgody.

**Następny krok:** ponownie odczytać HEAD i obecność AA-51; przy dalszym braku źródła wybrać nowy, niepowtórzony audyt przekrojowy z naciskiem na kompletność hipotez dowodów. Osobno uruchomić pełną kompilację i inspekcję PDF w środowisku z dostępnym checkoutem i zależnościami.

## AA-X25 — niezależna stabilizacja: kryterium przez domknięcie normalne

Po pierwotnym audycie AA-30 × AA-36 wykonano **nowy, niezależny most matematyczny**, bez modyfikowania zatwierdzonych rozdziałów. Uzupełnia on omówioną już przeszkodę stopnia o warunek konieczny i dostateczny, który jednoznacznie odróżnia pierwiastniki od konstrukcji cyrklem i linijką.

### 1. Kryterium grupy Galois dla rzeczywistych liczb algebraicznych

**Twierdzenie.** Niech \(\alpha\in\mathbb R\) będzie liczbą algebraiczną nad \(\mathbb Q\), a \(L\subseteq\mathbb C\) ciałem rozkładu jej monicznego wielomianu minimalnego nad \(\mathbb Q\). Wtedy następujące warunki są równoważne:
(a) \(\alpha\) jest konstruowalna z \(\{0,1\}\) cyrklem i linijką;
(b) \(\operatorname{Gal}(L/\mathbb Q)\) jest skończoną \(2\)-grupą.

**Dowód (a ⇒ b).** Na podstawie kryterium wieży kwadratowej z AA-30 istnieją ciała \(\mathbb Q=K_0\subseteq\cdots\subseteq K_r\subseteq\mathbb R\), z \(\alpha\in K_r\) i \([K_i:K_{i-1}]\in\{1,2\}\). Lemat o domknięciu normalnym tej wieży z AA-30 gwarantuje istnienie skończonego rozszerzenia Galois \(N/\mathbb Q\) zawierającego \(K_r\), dla którego grupa \(\operatorname{Gal}(N/\mathbb Q)\) jest \(2\)-grupą. Skoro \(N/\mathbb Q\) jest normalne i zawiera \(\alpha\), zawiera wszystkie sprzężenia \(\alpha\), a więc całe ciało rozkładu \(L\). Ponieważ \(L/\mathbb Q\) też jest Galois, odwzorowanie ograniczenia \(\operatorname{Gal}(N/\mathbb Q)\twoheadrightarrow\operatorname{Gal}(L/\mathbb Q)\) jest surjekcją. Iloraz skończonej \(2\)-grupy jest \(2\)-grupą.

**Dowód (b ⇒ a).** Załóżmy, że \(G=\operatorname{Gal}(L/\mathbb Q)\) jest \(2\)-grupą. Niech \(H=\operatorname{Gal}(L/\mathbb Q(\alpha))\). Jest to podgrupa \(G\), a z odpowiedniości Galois \(L^H=\mathbb Q(\alpha)\). Każda podgrupa właściwa skończonej \(2\)-grupy jest zawarta w podgrupie maksymalnej; każda podgrupa maksymalna skończonej \(2\)-grupy ma indeks \(2\). Stosując ten fakt kolejno wewnątrz coraz mniejszych podgrup zawierających \(H\), otrzymujemy skończony łańcuch \(G=G_0\supsetneq G_1\supsetneq\cdots\supsetneq G_s=H\) z \([G_{j-1}:G_j]=2\) dla wszystkich \(j\). Dla ciał stałych mamy zatem wieżę
\(\mathbb Q=L^{G_0}\subsetneq L^{G_1}\subsetneq\cdots\subsetneq L^{G_s}=\mathbb Q(\alpha)\),
a z prawa odpowiedniości \([L^{G_j}:L^{G_{j-1}}]=2\). Wszystkie jej ciała pośrednie leżą w \(\mathbb Q(\alpha)\subseteq\mathbb R\), więc jest to **rzeczywista** wieża kwadratowa kończąca się ciałem zawierającym \(\alpha\). Z kryterium AA-30 liczba \(\alpha\) jest konstruowalna. **Koniec dowodu.**

Warunek rzeczywistości jest istotny dla użytej formy wieży. Dla współrzędnych punktu zespolonego konstruowalność bada się osobno dla części rzeczywistej i urojonej. Sam warunek \([\mathbb Q(\alpha):\mathbb Q]=2^m\) nie wystarcza: normalne domknięcie może mieć grupę niebędącą \(2\)-grupą.

**Uzasadnienie użytego faktu grupowego.** Dla każdej właściwej podgrupy \(H\) skończonej \(p\)-grupy \(P\) zachodzi \(H\subsetneq N_P(H)\) (warunek normalizatora). Dowodzimy tego indukcyjnie po \(|P|\). Jeśli \(Z(P)\not\subseteq H\), wybieramy \(z\in Z(P)\setminus H\), a wtedy \(z\in N_P(H)\setminus H\). Jeśli \(Z(P)\subseteq H\), to \(H/Z(P)\) jest właściwą podgrupą mniejszej \(p\)-grupy \(P/Z(P)\) (centrum nietrywialnej \(p\)-grupy jest nietrywialne). Indukcja daje element spoza \(H/Z(P)\), który ją normalizuje; jego przeciwobraz normalizuje \(H\), ponieważ \(Z(P)\subseteq H\). Zatem \(H\ne N_P(H)\). W szczególności, jeśli \(M\) jest podgrupą maksymalną \(P\), to \(N_P(M)=P\), więc \(M\lhd P\). Iloraz \(P/M\) jest niezerową \(p\)-grupą, która nie ma nietrywialnych podgrup właściwych; z twierdzenia Cauchy’ego wynika zatem \(|P/M|=p\). Dla \(p=2\) wszystkie kroki łańcucha mają indeks \(2\). Przy tym żaden z rozważanych podgrup nie musi być normalny w całym \(G\): wystarcza indeks \(2\) w bezpośrednio poprzedniej podgrupie, by z prawa odpowiedniości otrzymać wieżę ciał odpowiednich stopni.

### 2. Dwa rzeczywiste przykłady o tym samym stopniu cztery

- Dla \(g=X^4-2\) dodatnia rzeczywista liczba \(\sqrt[4]{2}\) jest konstruowalna, gdyż \(\mathbb Q\subset\mathbb Q(\sqrt2)\subset\mathbb Q(\sqrt[4]{2})\) jest wieżą dwóch rozszerzeń kwadratowych. Grupa Galois jej domknięcia normalnego jest \(D_4\) rzędu \(8\), zatem również spełnia kryterium.
- Dla \(f=X^4-X-1\) każda rzeczywista liczba \(\alpha\) będąca pierwiastkiem ma stopień \(4\) nad \(\mathbb Q\) (nierozkładalność z AA-30), lecz nie jest konstruowalna: grupa Galois domknięcia normalnego to \(S_4\) rzędu \(24\), a \(24\) nie jest potęgą \(2\). **Jednocześnie** \(S_4\) jest rozwiązalna, ponieważ jej szereg pochodny to \(S_4\triangleright A_4\triangleright V_4\triangleright\{1\}\). Z AA-24 wynika więc rozwiązywalność \(f\) przez pierwiastniki, która nie implikuje konstruowalności.

Niezależny dowód \(G_f=S_4\) można przeprowadzić bez rezolwenty: redukcja \(f\) modulo \(2\) jest nierozkładalna stopnia \(4\), więc z AA-35 grupa Galois zawiera **4-cykl**; redukcja modulo \(7\) ma typ \((1,3)\), ponieważ
\[
\bar f=(X-3)(X^3+3X^2+2X-2)
\quad\text{w }\mathbb F_7[X],
\]
a czynnik sześcienny nie ma pierwiastka w \(\mathbb F_7\), więc jest nierozkładalny. Wyróżnik \(\operatorname{disc}(f)=-283\) nie jest podzielny ani przez \(2\), ani przez \(7\), a więc oba zastosowania AA-35 są uprawnione. Grupa zawiera 4-cykl i 3-cykl; jej rząd jest podzielny przez \(12\), więc jako dzielnik \(24\) wynosi \(12\) lub \(24\). Przy rzędzie \(12\) byłaby podgrupą indeksu \(2\) w \(S_4\), czyli \(A_4\), która **nie zawiera 4-cykli**. Stąd musi mieć rząd \(24\) i być całą \(S_4\). Ten dowód nie zakłada, że dowolna specjalizacja wielomianu ogólnego odziedziczy \(S_4\): wyznacza grupę **konkretnego** wielomianu.

### 3. Trwałe regresje i CI

Nowy moduł tools/tests/test_abstract_algebra_cross_aa30_36.py obejmuje **8 testów**:
1. niezależna nierozkładalność redukcji modulo \(2\), faktoryzacja modulo \(7\), wyróżnik i dobra redukcja;
2. pełne **48/48** par 4-cykli i 3-cykli w \(S_4\), dla każdej dokładne generowanie grupy \(24\)-elementowej;
3. dokładny szereg pochodny \(S_4>A_4>V_4>1\), wykazujący różnicę między rozwiązalnością a byciem \(2\)-grupą;
4. podgrupy \(D_4\) o rzędach \(8,4,2,1\) i rzeczywistą wieżę \(\sqrt2,\sqrt[4]2\);
5. dwie rzeczywiste wartości pierwiastków \(X^4-X-1\), nierozkładalność stopnia \(4\), a mimo to niekonstruowalność;
6. **98** klasyfikacji wielokątów o \(3\le n\le100\), porównujących liczbę względnie pierwszych reszt z kryterium wyróżnionych liczb pierwszych Fermata, dodatkowo przypadki 257 i 65537;
7. bezpośrednie niezmienniki elementarnych funkcji symetrycznych dla **24** permutacji, z rozróżnieniem modelu numerycznego i dowodu ogólnego;
8. liczbę źródeł 50, **24 etykiety i 20 odsyłaczy** w AA-30 oraz AA-36 i pełną integralność etykiet całej książki.

Wprowadzono osobny krok Run AA-X25 constructibility versus generic Galois checks w .github/workflows/abstract-algebra-chapter.yml, wraz z wyzwalaczem zmiany testu. Uruchomienie: [GitHub Actions 45251750248](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45251750248) na commicie af403110c6e494d110e79b365480654f782ce872.

**Status przy zapisie: W STABILIZACJI CI.** Do zamknięcia wymagane są odczyt w rzeczywistym logu 8/8 testów \`ok\`, zakończony zielony workflow, kompilacja AA-01–AA-50 oraz automatyczna weryfikacja odsyłaczy i PDF. Kompilacja nie jest niezależnym wizualnym audytem wszystkich stron PDF. Testy skończonych modeli nie są formalną weryfikacją Lean. Nie wprowadzono dodatkowego twierdzenia do zatwierdzonych rozdziałów; to **opcjonalna propozycja** rozszerzenia AA-30 lub AA-36, której użytkownik jeszcze nie zatwierdził.
