# Teoria miary / Miara i całka — audyt II rozdziału 03 (iteracja globalna XVI)

**Data:** 2026-11-23. **Istniejąca gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zakres merytoryczny:** wyłącznie `chapters/pl/measure_theory/03-miary-zewnetrzne-i-konstrukcja-caratheodoryego.tex`.
Rozdziały 01–02 (stabilne) i 04–31 pozostawiono bez zmian. Sprawdzanie całej książki służy tylko kontroli integracji i odsyłaczy do R03. Nie zmieniono osobnego `books/pl/integration_theory.tex`.

## Odtworzony stan wejściowy

Przed rozpoczęciem odczytano aktualną gałąź (HEAD `ab118461ea7e3c51cee3793ac0f6be40a23d9bce`), ostatnie commity, listę audytów, raport poprzedniej iteracji `15-rozdzial-03-audyt-I-2026-11-23.md`, bieżący R03, workflow, skrypt testowy i globalne standardy `AGENTS.md` oraz `docs/pl/standardy_terminologiczne.md`. Ostatnia poprawka tekstu R03 w audycie I: commit `a3fdeb4ea86fa07e845c05df07a988cc175f2870`, dotyczący odróżnienia wystarczalności od konieczności warunku premiary przy zachowaniu kosztów pokrycia. R03 nie zmienił się od tej poprawki: blob **`3c95138c4dc60b892835e8c9bc8421c70666ee72`**, 529 linii.

## Niezależny, sceptyczny przegląd całego R03 po poprawce

Ponownie sprawdzono **7 sekcji, 1 podsekcję, 6 twierdzeń, 2 lematy, 4 definicje, 4 przykłady, 4 uwagi i 8 dowodów**, nie przyjmując wniosków audytu I za uzasadnienie. Sprawdzono jawne hipotezy, kwantyfikatory, szczegóły rachunków z wartością `∞`, argumenty przekrojów i pokryć oraz przypadki nieskończonej masy.

1. **`thm:outer-from-cover` (miara zewnętrzna z kosztu pokryć):** niepustość rodziny pokryć wynika z pokrycia X; wartość zera na zbiorze pustym z `c(∅)=0`; monotoniczność przez zawieranie rodzin pokryć; przeliczalna podaddytywność przez wybory z błędem `ε2^{-j}` i połączenie pokryć. Rzeczywiste brzegowe przypadki `μ^*(E_j)=∞` są oddzielone przed użyciem przybliżenia infimum.
2. **Poprawiona uwaga „Rola założeń”:** w nowej wersji równość `μ_c^*(C)=c(C)` przy algebrze i premiarze jest wyraźnie nazwana **wystarczającą, niekonieczną**. Przykład kontrolny na dwupunktowym zbiorze, `c(∅)=0` i `c(E)=1` dla pozostałych E: równość kosztu jest zachowana, ale skończona addytywność zawodzi. Uwaga jest obecnie poprawna, nie dopisano nowego przykładu do rozdziału.
3. **`thm:caratheodory`:** osobno przejrzano sześć kroków dowodu: dopełnienia, skończone i przeliczalne sumy, mierzalność rozłącznionych rodzin, przeliczalna addytywność i zupełność. W przejściach z `μ^*(T)=∞` używa się nierówności dla wartości rozszerzonych, nie niedozwolonego odejmowania `∞−∞`.
4. **`lem:premeasure-cover`:** rozłącznienie `B_n` pozostaje w algebrze, a jego suma jest elementem algebry, co umożliwia zastosowanie definicji premiary. Monotoniczność premiary wynika z addytywności skończonej.
5. **`thm:premeasure-continuity`:** przy `A_n↓∅` zbiory różnicowe dają szereg z sumą `μ_0(A_1)<∞`, więc jego ogony zanikają. W drugą stronę malejące reszty `R_N↓∅` pozwalają przejść od skończonej do przeliczalnej addytywności. Kontrprzykład z miarą liczącą i ogonami liczb naturalnych prawidłowo wskazuje rolę hipotezy skończoności.
6. **`thm:extension-caratheodory`:** rozcięcie każdego pokrycia względem ustalonego zbioru z algebry dowodzi kryterium mierzalności; lemat o pokryciach dowodzi równości na algebrze; ograniczenie do `σ(𝒜)` nie jest bez dodatkowych argumentów nazywane zupełnym.
7. **`thm:extension-uniqueness`:** wyczerpanie `A_n` można założyć rosnące; miary ograniczone są skończone i zgadzają się na wspólnej algebrze-układzie π, następnie ciągłość z dołu usuwa ograniczenie. Kontrprzykład z miarą liczącą i miarą zero/∞ na zbiorach borelowskich pokazuje, dlaczego nie wolno usunąć wymaganych hipotez bez zastępczych założeń.
8. **`lem:outer-approx-algebra`:** przy skończonym koszcie E można znaleźć pokrycie o sumie kosztów mniejszej niż `μ^*(E)+ε`; jego suma B należy do `σ(𝒜)`. Dopiero mierzalność E uzasadnia rozkład miary B i oszacowanie różnicy.
9. **`thm:caratheodory-completion`:** rozdzielenie na części `E∩A_n` o skończonej mierze, pokrycia o błędach `2^{-n}/k`, konstrukcja górnego D i dolnego C oraz zerowa miara `DC`. Dokładnie w tym miejscu potrzebna jest σ-skończoność; nie wyciągano wniosków dla przypadku nieskończenie ciężkiego atomu bez tej hipotezy.

Wszystkie cztery przykłady i uwagi skonfrontowano z definicjami: miara zewnętrzna nierozdzielająca singletonów, funkcja skończenie addytywna niebędąca premiarą, brak σ-skończoności przy niewystarczających generatorach oraz rozróżnienie przestrzeni borelowskiej od jej uzupełnienia. **Wynik pełnego audytu II: brak nowej matematycznej lub językowej usterki wymagającej zmiany R03.** Jest to pierwszy pełny czysty audyt tego samego pliku po ostatniej poprawce.

## Nowe niezależne regresje — rzeczywisty postęp

Dodano nowy skrypt `tools/test_measure_theory_ch03_skeptical.py` (commit **`9239e59d60fcab00e6807dc21e41931c1f1b4631`**) i dołączono jego faktyczne uruchamianie do istniejącego workflow `.github/workflows/measure-theory-ch03.yml` (commit **`c9aff9636d81996c00661b4504afac30a0e51099`**).

Regresja niezależnie, od początku, konstruuje z kosztów pokryć **wszystkie 16 384 funkcje** `c:P({1,2,3})→{0,1,2,∞}` z `c(∅)=0` i wynikową miarę zewnętrzną metodą dokładnego minimalnego kosztu pokryć. Dla każdej sprawdza monotoniczność, podaddytywność, σ-algebrę zbiorów Carathéodory'ego i addytywność na mierzalnych zbiorach. Wynik rzeczywistego wykonania:

- **16 384** modeli kosztów, **112 022** instancje zbiorów mierzalnych;
- w **81** przypadkach miara zewnętrzna zachowuje zadany koszt na całej algebrze, w tym **43 przypadki z kosztem nieaddytywnym**. To szczególnie mocna regresja poprawki z audytu I;
- w **16 303** przypadkach koszt któregoś zbioru maleje po optymalizacji pokryć.

Dodatkowo test sprawdza model **bez σ-skończoności** na czteropunktowej przestrzeni: algebra wyznaczona przez dwa bloki ma premiarę o masie `∞` pierwszego bloku i masie 1 drugiego; po konstrukcji Carathéodory'ego powstaje **8 zbiorów mierzalnych**, podczas gdy uzupełnienie pierwotnej σ-algebry ma **4 zbiory**. Stanowi to kontrolny kontrprzykład pokazujący, dlaczego utożsamienie obu rodzin w `thm:caratheodory-completion` musi wymagać dodatkowych przesłanek.

Oba testy uruchomiono lokalnie. W GitHub Actions [45135022116](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45135022116) na commicie `c9aff9636d81996c00661b4504afac30a0e51099` zadanie `chapter-03-finite-models` zakończyło się **`success`** dla nowego i wcześniejszego testu. Końcowy status drugiego joba (PDF) wymaga osobnego sprawdzenia; w chwili pierwotnej redakcji raportu kompilacja była w toku.

## Kontrola LaTeX, PDF, odsyłaczy i terminologii

W źródle R03 jest **18 unikatowych etykiet**, **25 odsyłaczy** i **38 poprawnie sparowanych środowisk**, bez błędów zagnieżdżenia i duplikatów. Wszystkie 6 różnych zewnętrznych celów odnaleziono w R02 lub R04, a oba są traktowane wyłącznie jako kontekst odsyłaczy. Nie ma zabronionych symboli `\mathbf{1}`, `\mathbb{1}`, `\mathds{1}` ani terminów „unia zbiorów”, „zbieżność zdominowana”. Brak rysunków, podpisów i elementów TikZ w R03.

W poprzedniej iteracji wykonano i obejrzano realny PDF R03 (wszystkie **6 stron**) oraz jego wersję w 256-stronicowej książce. W tej iteracji niezależnie ponowiono analizę geometrii plików PDF z tamtego samego, niezmienionego źródła: **119 bloków tekstowych** w izolowanym PDF, **0 poza granicami stron**; rozdział R03 zajmuje strony fizyczne 26–31 pełnej książki, **0 nierozwiązanych odsyłaczy**, **25 hiperłączy**, **0 bloków poza stronami**. Sprawdzono aktywne cele odsyłaczy w kontekście książki. Nie nazywa się tego merytorycznym audytem innych rozdziałów.

## Stabilizacja i proponowane następne działanie

**R03: drugi niezależny, pełny audyt matematyczny CZYSTY, kontrola PDF wizualnie CZYSTA.** R03 pozostaje **niezmieniony** od ostatniej poprawki. Formalny certyfikat stabilności należy oprzeć na tym raporcie, potwierdzonym wyniku CI i ponownym odczycie blobu R03.

**Propozycja opcjonalna, bez zmiany źródła:** rozważyć później dodanie jako osobnego przykładu wyżej opisanego przypadku bez σ-skończoności, gdzie rodzina Carathéodory'ego jest większa od uzupełnienia. Wzbogacenie materiału wymaga wyraźnej zgody użytkownika, nie jest błędem tekstu ani warunkiem stabilizacji.

**W tej iteracji nie przechodzono do R04.** Ewentualny audyt R04 musi być osobną, późniejszą iteracją i może rozpocząć się dopiero po potwierdzeniu stabilności R03.
