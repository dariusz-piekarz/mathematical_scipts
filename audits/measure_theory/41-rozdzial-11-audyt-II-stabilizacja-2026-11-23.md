# Teoria miary / Miara i całka — rozdział 11, audyt II (globalny XLI): niezależna stabilizacja

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/11-calki-zalezne-od-parametru.tex.  
**Blob R11 przed i po audycie:** d9e41430abca9c0094767891c17f0c01ae166444.  
**Zmiany w źródle R11, jego teście oraz workflow w tej iteracji:** 0 — jest to niezależna kontrola po ostatnich poprawkach.

## 1. Rzeczywisty punkt wznowienia i ograniczenie zakresu

Przed rozpoczęciem odczytano aktualną gałąź i porównano ją z commitem fe0e7f35d3df42811a785e7672faf7d64c6e74f3, zamykającym poprzedni raport. W chwili wznowienia pięć nowych commitów nie dotyczyło źródła ani infrastruktury R11. Ponownie odczytano audits/measure_theory/40-rozdzial-11-audyt-I-2026-11-23.md, blob 18b75538e0470a71a6b4471dd77e32242f2a43da. Tamten audyt poprawił hipotezy twierdzeń, zerowe reprezentanty na zbiorach wyjątkowych, samodzielność wniosku L¹ i składnię LaTeX; słusznie pozostawił R11 niestabilny do kolejnej niezależnej kontroli. Raport XLI nie istniał.

Pobrano źródło R11, jego testy i workflow z istniejącej gałęzi oraz ponownie zweryfikowano zasady AGENTS.md i docs/pl/standardy_terminologiczne.md. Rozdziały R01–R10 i R12 służyły jedynie jako kontekst wcześniejszych definicji i odsyłaczy, a nie jako przedmiot kolejnych audytów. Nie edytowano R01–R10 ani R12–R31, nie scalano skryptów i nie tworzono nowej gałęzi.

## 2. Niezależna kontrola wszystkich ośmiu dowodów

Po poprawkach źródło liczy 526 wierszy, 9 sekcji, 8 twierdzeń, 1 wniosek, 1 definicję, 8 dowodów, 5 przykładów i 5 uwag; bez rysunków TikZ.

**Dowody: 8/8 PASS.** Sprawdzono następujące kroki i przypadki brzegowe:

1. **Lokalne kryterium ciągłości:** wspólny zbiór wyjątkowy w definicji lokalnej dominacji jest wystarczający dla DCT; dla danego ciągu parametrów wystarcza nawet przeliczalna suma zbiorów zerowych zależnych od t. Zbieżność f(t_n,·)→f(t₀,·) p.w. i dominacja |f(t_n,·)−f(t₀,·)|≤2g dają zbieżność w L¹ oraz ciągowe kryterium ciągłości w T.
2. **Zbieżność jednostajna całek:** T jest niepusty, przekroje mierzalne, 0≤h_n≤g∈L¹ i h_n→0 p.w. Jednoznacznie określone całki wszystkich f(t,·) wynikają z całkowalności f(t*,·) i dominacji g₀. Nierówność supremum po parametrze przez ∫h_n i DCT są poprawne również bez mierzalności supremum po nieprzeliczalnym T.
3. **Pierwsza pochodna pod całką:** dla funkcji zespolonej skalarne twierdzenie o wartości średniej zastosowane do Re(\bar u f) dla |u|=1 pozwala uzyskać właściwe oszacowanie modułu różnicy. Ilorazy różnicowe mają mierzalne przekroje i są dominowane przez g; pochodna jest mierzalna jako punktowa granica ilorazów i przyjmuje wartość zero na mierzalnym zbiorze wyjątkowym. DCT daje pochodną F w t₀.
4. **Pochodne wyższego rzędu:** dla każdego t można wybrać zwarty odcinek J⊂I łączący t z t*, używając g_{J,1} do całkowalności f(t,·). Lokalna indukcja korzysta z twierdzenia o pierwszej pochodnej i oszacowań g_{J,k}. Warunek różniczkowalności dla prawie wszystkich x dotyczy całego I; w razie potrzeby z lokalnie zależnych zbiorów wyjątkowych dla majorant można uzyskać wspólny zbiór miary zero na wyczerpaniu I przez przeliczalnie wiele zwartych przedziałów, dla skończenie wielu k. Ciągłość F^{(k)} wynika z lokalnej dominacji i ciągłości funkcji podcałkowych.
5. **Parametryczny Vitali:** przy skończonej μ(X), jednostajnej całkowalności modułów oraz zbieżności według miary dla t→t₀ każda sekwencja parametrów t_n→t₀ podlega twierdzeniu Vitaliego. Re i Im są jednostajnie całkowalne, a sprzeczność z dolnym ograniczeniem norm L¹ daje ciągłość.
6. **Ruchome obszary całkowania:** χ_{A_t}u(t,·) jest mierzalna, a na dowolnym ciągu parametrów jej majoranta może być wykazana poza przeliczalną sumą zależnych od parametru zbiorów zerowych. DCT zapewnia ciągłość całek po A_t bez nieuprawnionego żądania jednego zbioru wyjątkowego dla całego T.
7. **Jednostajna kontrola ogonów:** gdy sup_{t∈U}∫_{X\X_n}|f(t)|→0, dla dostatecznie dużego n całkowalność na X_n i skończoność całki ogona dają całkowalność na całym X. Trójkątne oszacowanie przez jedną część lokalną oraz dwa ogony jest poprawne przy t,t₀∈U.
8. **Holomorficzność transformaty Laplace’a:** lokalne liczby a<σ<σ′<Re z ograniczają x^k e^{-Re zx}|h(x)| przez stałą razy e^{-σx}|h(x)|. Zespolone ilorazy różnicowe są pod tym samym integrabilnym ograniczeniem, a ich granica daje pochodną bez stosowania jeszcze nieudowodnionego twierdzenia Fubiniego. Iteracja z (-x)^k h(x) uzasadnia wszystkie pochodne.

W tym niezależnym audycie nie znaleziono nowej fałszywej tezy, istotnej luki dowodowej ani niejawnego założenia wymagającego kolejnej zmiany źródła.

## 3. Pięć przykładów i pięć uwag

**5/5 przykładów i 5/5 uwag — PASS:** koncentracja jednostkowej masy f(t,x)=tχ_(0,1/t)(x) przy t↓0, kontrprzykład braku globalnej dominacji dla e^{-tx}, momenty rozkładu wykładniczego, ruchome przedziały (0,t) i własności funkcji Gamma. Dla Gamma sprawdzono całkowalność przy x↓0 majoranty x^{a−1}|log x|^k przy a>0, tłumienie wielomianowe w nieskończoności i znikanie wyrazów brzegowych w dowodzie rekurencji Gamma(s+1)=s Gamma(s). Uwaga o supremum po nieprzeliczalnej przestrzeni parametrów prawidłowo wymaga osobnego wykazania mierzalności.

## 4. Nowe niezależne testy — rzeczywiste wykonanie

Utworzono i uruchomiono **lokalny niezależny skrypt /mnt/data/r11_audit41_independent.py** (nieimportujący tools/test_measure_theory_ch11.py). Testował dokładną arytmetykę wymierną i osobno wybrane całki wysokiej precyzji:

- **29160/29160 PASS** — całki atomowe i jednostajne oszacowanie błędów po parametrze, z zerowymi wagami;
- **10935/10935 PASS** — ścisłe wzory dla ilorazów różnicowych wielomianowych rodzin podcałkowych i ich pochodnych;
- **800/800 PASS** — lokalna stabilność skończonych ruchomych obszarów całkowania przy parametrach nieprzekraczających atomowych punktów brzegowych;
- **450/450 PASS** — dokładne geometryczne wzory na ogony i oszacowania jednostajne w parametrze;
- **19/19 PASS** — weryfikacja transformaty Laplace'a i funkcji Gamma przez niezależne całki wysokiej precyzji;
- **łącznie 41364/41364 PASS**.

Zastrzeżenie: regresje skończonych i szczególnych modeli **nie stanowią dowodów** twierdzeń na dowolnej przestrzeni z miarą. Dowody ogólne oceniono niezależnie w sekcji 2.

## 5. Kontrola CI, PDF, LaTeX i terminologii

Z GitHub API ponownie odczytano **run [45160370883](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160370883)**, commit 26503f566c6e39401fdf495e0683e13425f3c26b. Oba joby **completed SUCCESS (2/2)**: testy oraz skład PDF/odsyłacze. Aktualne porównanie gałęzi do tego commitu wykazało **zero zmian w źródle R11, tools/test_measure_theory_ch11.py, workflow i books/pl/measure_theory.tex**, więc udany CI dotyczy dokładnie aktualnie audytowanego bloba.

Potwierdzone w logach CI: 125 modeli dominacji, 324 ilorazy różnicowe, 318 ruchomych obszarów, 100 ogonów i 23 testy Laplace'a; plus poprawny test referencji i środowisk. Izolowany R11: **6 stron A4**, dwie kompilacje pdflatex, **3774 słowa Popplera w granicach stron**, 6/6 podglądów. Pełna książka: trzy kompilacje, **257 stron**, bez niezdefiniowanych odsyłaczy i bez przepełnionych wierszy.

Niezależnie ponownie wyrenderowano autentyczny PDF z artefaktu CI **14809818860** do sześciu plików PNG przy 160 dpi. Obejrzano układ wszystkich stron (w tym pełne powiększenie stron 1–6) i nie stwierdzono kolizji oznaczeń, uciętych wzorów, nieczytelnych podpisów lub błędnych środowisk. Niezależna kontrola PyMuPDF potwierdziła **6 stron, 3003 słowa według własnej segmentacji, 0 poza prostokątami stron**. Różnica liczby słów względem Popplera wynika z różnych sposobów ich rozdzielania.

Z rzeczywistych logów: **izolowany R11 — 0 Overfull hbox, 0 Underfull hbox**; **pełna książka — 0 Overfull hbox, 0 niezdefiniowanych odsyłaczy, 14 globalnych nieblokujących Underfull hbox**. W izolowanym PDF są widoczne symbole ?? dla odsyłaczy międzyrozdziałowych, co wynika z kompilacji tylko R11; pełna książka rozwiązuje je prawidłowo.

W R11 **18 etykiet i 12 odsyłaczy**, wszystkie z poprawnymi celami w R01–R12 (R12 odczytany tylko jako kontekst). Nie ma niezamkniętych środowisk, niedozwolonego samodzielnego słowa „sekwencja” ani niezgodnych oznaczeń funkcji charakterystycznych; stosowane jest \chi_A. Utrzymano wszystkie zmiany z audytu XL, w tym niezależnie sformułowany wniosek o ciągłości L¹.

## 6. Formalna decyzja

**ROZDZIAŁ 11 — STABILNY / FORMALNIE ZATWIERDZONY.**

R11 przeszedł pierwszy audyt XL, w którym poprawiono rzeczywiste nieścisłości i błąd LaTeX, a następnie zakończono pełny CI 2/2 SUCCESS. Niniejszy audyt XLI stanowi **drugi, niezależny i czysty przegląd po ostatniej poprawce**: wszystkie 8 dowodów, 5 przykładów, 5 uwag, pełny zakres hipotez, szczególne modele regresyjne, 18 etykiet, 12 odsyłaczy oraz faktyczny PDF zostały zweryfikowane bez nowych usterek. **Nie wprowadzono kolejnej zmiany źródła**, toteż nie powstała potrzeba nowej fazy stabilizacji.

**R01–R10 — STABILNE**, nieaudytowane i nieedytowane w tej iteracji. **R12–R31 — nietknięte**.

**Następny osobny etap:** audyt globalny XLII / R12 I — rozdział 12 o miarach produktowych oraz twierdzeniach Tonellego i Fubiniego. Nie rozpoczynano go w ramach niniejszego audytu.