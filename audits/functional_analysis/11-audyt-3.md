# Analiza funkcjonalna — rozdział 11 — audyt 03 (niezależny pierwszy czysty przegląd stabilizacyjny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`, istniejąca.  
**Źródło:** `chapters/pl/functional_analysis/11-przestrzenie-frecheta-twierdzenia-o-odwzorowaniu-otwartym-i-wykresie-domknietym.tex`.  
**SHA źródła:** `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2`, niezmieniony od zakończenia poprawek 11/02.  
**Zestaw testowy:** `tools/tests/test_functional_analysis_ch11.py`, blob SHA `04789592feeeeb181239d1e8659c1f8340f0a141`.  
**Werdykt matematyczno-redakcyjny:** **CZYSTY — 1/2** wymaganych kolejnych niezależnych przeglądów identycznej wersji źródła. **Brak zmian plików LaTeX, testów lub workflow.** Rozdział 12 pozostaje zablokowany.

## Odrębne potwierdzenie stanu przed audytem

Odczytano na nowo katalog raportów oraz bieżące workflow; w chwili rozpoczęcia nie istniał `11-audyt-3.md`, a istniejące `11-audyt-1.md` i `11-audyt-2.md` były audytami sprzed stabilizacji. Bieżący plik ma identyczną zawartość jak po ostatnich poprawkach 11/02. Dedykowany [GitHub Actions #45230679301](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45230679301) uruchomiony po 11/02 na commicie `e065ed1e58c05cb22ac6662245bfa0bb049eb442` zakończył się **COMPLETED/SUCCESS**. Jego kroki obejmowały 15 testów regresyjnych, pełny kontekst LaTeX 01–11, kompilację PDF, weryfikację PDF/odsyłaczy i publikację artefaktu, wszystkie PASS. Nie przyjmowano tej kontroli za matematyczny dowód; ponownie skontrolowano samą treść rozdziału 11.

## Niezależny przegląd 10 dowodów

1. **Metryka z przeliczalnych seminorm.** `d(x,y)=\sum_{n\ge1}2^{-n}\min(1,p_n(x-y))` jest skończona, translacyjnie niezmiennicza i spełnia nierówność trójkąta przez nierówność dla `\min(1,a+b)`. Rozdzielanie punktów przez `(p_n)` wynika z Hausdorffa i generowania topologii. Argument rozdzielenia skończonego początku i ogona szeregu działa dla sieci i dla warunku Cauchy'ego, więc metryka wyznacza tę samą strukturę jednostajną; stwierdzenie o zupełności nie pomija warunku metryzowalności.
2. **Podprzestrzenie, ilorazy i produkty Frécheta.** Domknięta `M\subset E` jest zupełna w metryce indukowanej. Metryka `\bar d(qx,qy)=\inf_{m\in M}d(x-y+m,0)` jest niezależna od reprezentantów, dodatnio określona właśnie dzięki domkniętości `M` i generuje topologię ilorazową przez równość obrazów kul. Dla Cauchy'ego `(u_n)` wybierane są indeksy z odległościami kolejnych wyrazów mniejszymi od `2^{-k-1}`; reprezentantów kolejnych klas można wybrać w odległości mniejszej od `2^{-k}`, uzyskując Cauchy'ego w `E`. Cały ciąg klas zbiega, bo ma zbieżny podciąg i jest Cauchy'ego. Dla przeliczalnego produktu wystarczają współrzędne metryki `\sum2^{-j}\min(1,d_j)`, zupełność współrzędnych i kontrola ogona.
3. **Krok Baire'a.** Z surjektywności `T:E\to F` i pochłaniania `U` wynika `F=\bigcup_{n\ge1}nT(U)`. Baire gwarantuje niepuste wnętrze pewnego `\overline{nT(U)}`. Skalowanie daje niepuste wnętrze `\overline{T(U)}`, a jego absolutna wypukłość pozwala otrzymać otoczenie zera. Argument nie wymaga zupełności `E` na tym etapie, jedynie otoczenia pochłaniającego i własności Baire'a w `F`.
4. **Odwzorowanie otwarte.** Konstrukcja `U_0` z `\overline{U_0}\subset U` używa regularności lokalnie wypukłej TVS, a `U_n+U_n\subset U_{n-1}` i `U_n\subset A_n` zapewniają malejącą bazę otoczeń zera. Dla każdego `U_n` krok Baire'a daje `V_n\subset\overline{T(U_n)}\cap B_n`. Dla `y\in V_1` rekurencja reszt `y-T\sum_{k=1}^n x_k\in V_{n+1}` daje reszty zbieżne do zera. Dla `N\ge m` suma ogona `\sum_{k=m}^N x_k\in U_{m-1}` na mocy indukcji wstecznej, bo `U_{n+1}\subset U_n` i `U_n+U_n\subset U_{n-1}`. To gwarantuje Cauchy'ego szeregowego i, dzięki zupełności `E`, `x\in\overline{U_0}\subset U` z `Tx=y`. Wniosek o obrazie każdego zbioru otwartego uzasadniają translacje. Hipotezy metryzowalności i surjektywności są jawne.
5. **Ciągłość odwrotności.** Liniowa bijekcja, będąc otwarta, ma ciągłą odwrotność: dla każdego otwartego `O\subset E` przeciwobraz `O` przez `T^{-1}` to `T(O)`. Logika i kierunki odwzorowań zgadzają się z tezą.
6. **Ograniczenie odwrotności w Banachach.** Ciągłość `T^{-1}` pomiędzy przestrzeniami unormowanymi jest równoważna ograniczoności; `C=\max(1,\|T^{-1}\|)` jest poprawne także w trywialnym przypadku.
7. **Izomorfizm ilorazu przez jądro.** Z `\ker T=T^{-1}(\{0\})` wynika domkniętość. Iloraz `E/\ker T` i `F` są Frécheta, a `\widetilde T` ma własność uniwersalną zapewniającą ciągłość i jest liniową bijekcją. Stosowanie twierdzenia o odwrotności nie wymaga dodatkowych ukrytych hipotez.
8. **Kryterium ciągowe domknięcia wykresu.** Produkt metryzowalnych TVS jest metryzowalny. Wykres operatora określonego na całej `E` jest domknięty dokładnie wtedy, gdy zachowuje granice wszystkich zbieżnych ciągów swoich punktów. Zmiana nazwy z „sekwencyjne” na „ciągowe” była wykonana w 11/02 i została potwierdzona.
9. **Wykres domknięty.** W jedną stronę `G(T)` jest przeciwobrazem singletonu przez ciągłe `(x,y)\mapsto y-Tx`. W drugą stronę `G(T)` jest domkniętą podprzestrzenią Frécheta `E\times F`; `P:G(T)\to E` jest ciągłą liniową bijekcją, a z ciągłości `P^{-1}` wynika ciągłość `T=\pi_F\circ P^{-1}`. Dziedzina musi być pełna — osobny przykład pokazuje ograniczenie.
10. **Równoważność zupełnych norm porównywalnych.** Gdy `(V,\|\cdot\|_a)` i `(V,\|\cdot\|_b)` są Banachami, ciągła bijekcja identycznościowa ma ciągłą odwrotność, co daje oszacowanie odwrotne. Pełność obu norm jest prawidłowo wymagana.

**Werdykt dowodów: 10/10 PASS** — nie znaleziono nieprawdziwej tezy ani nieuzasadnionego przejścia wymagającego zmian.

## Sześć przykładów

1. **`\K^{\N}` i `C^\infty([0,1])`.** Pierwszy przykład jest zupełny dzięki współrzędnym Cauchy'ego; drugi wykorzystuje jednolite granice funkcji `f_n^{(j)}\to g_j` i tożsamość całkową, która po przejściu do granicy daje `g_j'=g_{j+1}` i `p_m(f_n-g_0)\to0`. Wstawiony w 11/02 argument jest teraz kompletny.
2. **Niezupełna przeciwdziedzina.** Identyczność `(\ell^1,\|\cdot\|_1)\to(\ell^1,\|\cdot\|_2)` jest ciągła, lecz nie otwarta, ponieważ ciąg wektorów z pierwszymi `n` współrzędnymi `1/n` ma normę `\ell^1` równą `1` i normę `\ell^2` równą `n^{-1/2}`. Druga przestrzeń nie jest zupełna.
3. **Niezupełna dziedzina i wykres domknięty.** Odwrotna identyczność `(\ell^1,\|\cdot\|_2)\to(\ell^1,\|\cdot\|_1)` nie jest ciągła, lecz ma domknięty wykres przez jednoznaczność granic w `\ell^2`.
4. **Domknięty, nieograniczony operator różniczkowania.** Dla `E=F=C([0,1])`, `D(T)=C^1([0,1])` i `Tf=f'` funkcje `f_n(t)=n^{-1}\sin(nt)` dążą normowo do zera, lecz pochodne mają normę `1`. Granice jednostajne `f_n\to f` i `f_n'\to g` prowadzą przez całkowanie do `f'=g`; nie ma sprzeczności z twierdzeniem, bo dziedzina jest właściwa.
5. **Ciągła pochodna na `C^\infty`.** `p_n(Df)\le p_{n+1}(f)` dowodzi ciągłości, całkowanie daje surjektywność, a jądro to funkcje stałe. Prawa odwrotność jest ciągła, z `p_n(Rg)\le2p_n(g)`; izomorfizm ilorazu jest prawidłowy.
6. **Gęsty niepełny obraz `\ell^1\hookrightarrow\ell^2`.** Obraz zawiera `c_{00}` i jest gęsty, ale nie jest cały: `(n^{-3/4})\in\ell^2\setminus\ell^1`. Nieciągłość odwrotności na obrazie oraz brak zupełności tego obrazu nie naruszają twierdzenia o odwzorowaniu otwartym.

**Werdykt przykładów: 6/6 PASS.** W szczególności zbadano osobno zupełność przeciw- i dziedziny, właściwą dziedzinę operatora domkniętego oraz istnienie niezerowego przypadku `\ell^2\setminus\ell^1`.

## Kontrole redakcyjne, strukturalne i techniczne

Ponownie pobrano **11 plików źródłowych** z katalogu `chapters/pl/functional_analysis`. W rozdziałach 01–11 naliczono **202 etykiety, 0 duplikatów**; w rozdziale 11 **20 etykiet, 16 odsyłaczy i 0 nierozwiązanych**. Wszystkie środowiska w rozdziale 11 są poprawnie sparowane: 10 `proof`, 3 `twierdzenie`, 2 `stwierdzenie`, 1 `lemat`, 4 `wniosek`, 2 `definicja`, 6 `przyklad`, 4 `uwaga`, 1 `tikzpicture`, 1 `center`. Kontrola terminologii: brak zakazanych „sekwencyjne”, „zwartościowanie” oraz dawnego oznaczania funkcji charakterystycznej `\mathbf1_A` lub `\mathbb1_A`. Po zmianach 11/02 rozdział używa „kryterium ciągowe” i rozróżnia zupełność TVS od zbieżności jedynie ciągów Cauchy'ego bez metryzowalności.

Zrealizowane wcześniej, już zakończone **CI #45230679301: SUCCESS**, w tym 15/15 testów regresyjnych, kontekst LaTeX 01–11, kompilacja i kontrola PDF. Audyt 11/02 dokumentuje rzeczywistą inspekcję wizualną stron 61–66 i schematu wykresu domkniętego na stronie 65; w tym audycie źródło jest identyczne, więc nie powtarzano wizualizacji. Automatyczne kontrole traktowane są jako bramka techniczna, a nie formalna weryfikacja dowodów.

## Decyzja

**11/03: CZYSTY, 1/2.** Po korektach 11/02 rozdział 11 pomyślnie przeszedł pierwszy niezależny audyt stabilizacyjny na niezmienionym blob SHA `73505ec4ff0f51ae76f0cfdf67cccd5eccbbd2b2`. Nie było potrzeby ingerencji w źródło LaTeX, testy czy workflow. **Po zapisaniu raportu należy osobno sprawdzić wynik wyzwolonego CI**. Następna iteracja: audyt **11/04**, drugi niezależny przegląd tego samego SHA. Dopiero 2/2 i zielone CI pozwolą rozpocząć rozdział 12.
