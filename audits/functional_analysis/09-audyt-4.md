# Analiza funkcjonalna — rozdział 09 — audyt 04 (niezależne potwierdzenie stabilności)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/functional_analysis/09-banach-alaoglu-krein-milman-i-topologia-mackeya.tex`.  
**Blob SHA źródła:** `d0a20b01bdabfa4e85d9c00ebe11c8c41bea650a`, identyczny z SHA zweryfikowanym w 09/03 oraz zatwierdzonym po poprawkach 09/02.  
**Werdykt matematyczno-redakcyjny:** **CZYSTY, 2/2** kolejnych niezależnych kontroli tego samego źródła.  
**Zmiany pliku matematycznego:** **0**. Nie zmieniano również testów ani workflow.

## Kontrola statusów i niezależność

Przed audytem sprawdzono bieżącą gałąź, katalog raportów i przebiegi GitHub Actions. Raport 09/03 istnieje i oznacza pierwszy czysty przegląd (1/2); nie było jeszcze raportu 09/04. Ostatni przebieg związany z raportem 09/03, [#45213422713](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45213422713), zakończył się **SUCCESS** (testy, przygotowanie kontekstu, kompilacja, weryfikacja PDF i odsyłaczy, publikacja artefaktu). Nie traktujemy samego CI jako poświadczenia zgodności matematycznej: dowody, przypadki brzegowe i hipotezy oceniono osobno.

Ponownie pobrano cały plik 09, pliki źródłowe 01–08, bieżący plik 19 testów, poprzednie raporty 09/02 i 09/03 oraz definicję workflow. Sprawdzono nie tylko deklaracje poprzednich audytów, lecz także przyczyny wystąpienia i wyeliminowania wcześniejszych błędów.

## Niezależny przegląd wszystkich 14 dowodów

1. **Równociągłość i polary:** zawarcie w polarnym zbiorze pewnego otoczenia jest równoważne równociągłości przez skalowanie i prowadzi do punktowej ograniczoności; poprawnie także dla pustego zbioru funkcjonałów.
2. **Banach–Alaoglu–Bourbaki:** otoczenie zera jest pochłaniające, więc zbiór polarny jest współrzędnie ograniczony w `K^E`. Produkt zwartych dysków jest zwarty przez twierdzenie Tychonowa, a addytywność, jednorodność i nierówności polarne są domkniętymi warunkami. Dowód ciągłości powstałego liniowego funkcjonału nie wymaga Hausdorffa, lokalnej wypukłości ani zupełności `E`.
3. **Słabo-* zwartość normowej kuli:** dokładna identyfikacja polara kuli otwartej dla `R>0`; dla `R=0` zwarty singleton.
4. **Domknięte podzbiory słabo-* zwartej kuli:** bezpośrednia konsekwencja zwartości, w tym przy `A=∅`.
5. **Metryzowalność na rodzinie równociągłej:** metryka z odczytów na przeliczalnym gęstym zbiorze rozdziela elementy `H`. Równociągłość pozwala przenieść kontrolę wartościowania z punktów gęstych na dowolny `x\in E`, więc topologie są identyczne.
6. **Metryzowalność słabo-* kuli a ośrodkowość:** z bazy otoczeń zera w metryzowalnym `B'` uzyskuje się przeliczalny zbiór wektorów o normowo gęstej rozpiętości; w przeciwnym razie Hahn–Banach dałby niezerowy punkt `B'` w każdym z tych otoczeń. Kierunek przeciwny korzysta z równociągłości `B'` i ośrodkowości `E`.
7. **Ściana poziomicy maksymalnej:** zwartość gwarantuje osiąganie maksimum, a liniowość oraz nierówności dla punktów `K` sprawiają, że poziomica jest ścianą; przechodniość ścian jest prawidłowa.
8. **Istnienie punktu ekstremalnego:** łańcuchy niepustych domkniętych ścian mają niepuste przecięcia przez własność skończonych przecięć w zwartym `K`; Zorn daje minimalną ścianę, a rozdzielający funkcjonał czyni ją singletonem.
9. **Krein–Milman:** domknięta wypukła otoczka zbioru punktów ekstremalnych jest zwarta jako domknięty podzbiór `K`. Jeżeli `x_0` pozostaje na zewnątrz, ścisłe oddzielenie i ściana maksimum dostarczają sprzeczności. Przypadek zespolony poprawnie redukuje się do części rzeczywistej.
10. **Zasada maksimum Bauera:** górna półciągłość zapewnia niepustość i domkniętość zbioru maksimów; wypukłość funkcji daje własność ekstremalności tego zbioru, bez nieuprawnionego założenia jego wypukłości. Zorn oraz liniowy funkcjonał dają punkt ekstremalny maksimum.
11. **Lemat zwartej dominacji:** skończenie wymiarowe obrazy `T_S(K)` są zwarte i absolutnie wypukłe; ścisłe oddzielenie punktu spoza obrazu narusza `|g|\le p_K`. Własność skończonych przecięć w zwartym `K` zapewnia jeden reprezentujący element `f`.
12. **Mackey–Arens:** `\tau(E,F)` zapewnia ciągłość wszystkich elementów `F`; ciągły funkcjonał jest dominowany przez `p_{CK}` z odpowiednim zwartym absolutnie wypukłym `CK`, więc należy do `F`. Dla topologii zgodnej każda ciągła seminorma `p` odtwarza się jako `p_{K_p}` przy `K_p=\{f:|f(x)|\le p(x)\}`; Hahn–Banach i słabo-* zwartość polara uzasadniają drugą inkluzję.
13. **Ekstrema topologii zgodnych:** słaba topologia jest minimalna z definicji, a topologia Mackeya maksymalna na mocy poprzedniego dowodu.
14. **Kryterium interpolacji przy dowolnie wielu warunkach:** nierówności dla wszystkich skończonych kombinacji zapewniają poprawność `g_J`, także przy powtarzających się indeksach; Hahn–Banach daje każde skończone rozwiązanie, a zwartość i własność skończonych przecięć rozwiązanie globalne, także dla `I=∅` i `R=0`.

**Werdykt dowodowy: 14/14 PASS.** Nie znaleziono niejawnych założeń lub błędów matematycznych wymagających zmian.

## Kontrola 8 przykładów

1. **`E=c_0, E'=\ell^1`:** słabo-* zwarta i metryzowalna kula nie jest zwarta w normie; ciąg `e_n` jest słabo-* zbieżny do zera.
2. **Nieprzeliczalny produkt:** identyfikacja kuli `\ell^\infty(I)` z produktem zwartych dysków zachowuje topologię słabą-*; sieć `\chi_F\to\chi_I`, ale żaden ciąg skończonych nośników nie zbiega do `\chi_I`.
3. **Nierównociągła rodzina słabo-* zwarta na `c_{00}`:** dla `f_n(x)=n x_n` mamy punktową zbieżność do zera i nieograniczone normy operatorowe.
4. **Wielokąt wypukły i kula Hilberta:** w źródle jawnie wymagane są wypukłość wielokąta oraz **niezerowość** rzeczywistej przestrzeni Hilberta; argument jest poprawny po wcześniejszych korektach.
5. **Produkt przedziałów `[-1,1]^I`:** punkty ekstremalne mają wszystkie współrzędne równe `\pm1`.
6. **Kula rzeczywistej `\ell^1`:** ekstremalnymi punktami są dokładnie `\pm e_n`; pozostałe punkty rozkładają się na średnią różnych punktów kuli.
7. **Topologia słaba vs Mackey:** na nieskończenie wymiarowej przestrzeni Banacha inkluzja `\sigma(E,E')\subsetneq\tau(E,E')` wynika z nienormowalności słabej topologii i zgodności topologii normowej.
8. **Przedłużanie wartości na wektorach współrzędnych `\ell^1`:** ograniczone wartości `b_n` definiują funkcjonał z `\ell^\infty`; po zgrupowaniu powtórzonych indeksów nierówność jest poprawna.

**Werdykt przykładów: 8/8 PASS.**

## Kontrola strukturalna, redakcyjna i techniczna

Z niezależnego ponownego odczytu źródeł 01–09: **159 etykiet łącznie, bez duplikatów**; rozdział 09 ma **23 etykiety** i **14 poprawnie rozwiązanych odsyłaczy**. Wszystkie środowiska otwierają się i zamykają w parach: 14 `proof`, 6 `twierdzenie`, 1 `stwierdzenie`, 4 `wniosek`, 3 `lemat`, 3 `definicja`, 8 `przyklad`, 4 `uwaga`, 2 `enumerate`, 1 `tikzpicture` i 1 `center`. Nie ma pozostałości wcześniejszego `\\mathbf 1_I`, złej hipotezy o Hilbercie zerowym, ani nieprawdziwej tezy o dowolnym niewypukłym wielokącie. Terminologia `\chi_I`, „przestrzeń sprzężona” i „zwartość ciągowa” jest zgodna z regułami.

Przy źródle i testach o niezmienionych SHA potwierdzono pełny sukces [GitHub Actions #45213422713](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45213422713), obejmujący **19/19 testów, kompilację kontekstu 01–09, automatyczną kontrolę PDF i odsyłaczy oraz publikację artefaktu — PASS**. Przegląd 09/02 dokumentuje dodatkowo niezależną inspekcję wizualną aktualnego PDF na stronach 48–55, w tym figury na stronie 51. Nie wykonano nowej niezależnej wizualizacji PDF w audycie 09/04: korzystamy z kontroli tego samego SHA i automatycznego CI. Niniejszy raport nie traktuje testów ani kompilacji jako formalnego poświadczenia twierdzeń.

## Ostateczny werdykt merytoryczny

**Rozdział 09 ma dwa kolejne czyste, niezależne przeglądy tej samej wersji źródła: audyty 09/03 i 09/04, z wynikiem 2/2.** Żaden nie wymagał modyfikacji źródła, testów ani rysunku. W odniesieniu do niezmienionych plików testów i LaTeX istnieje już ukończony z sukcesem przebieg CI `#45213422713`.

**Stan techniczny po zapisaniu raportu:** nowy przebieg CI może zostać wyzwolony zmianą wyłącznie pliku raportu; jego wynik należy sprawdzić przed ostatecznym zamknięciem 09 i rozpoczęciem audytu rozdziału 10. Zamknięcie rozdziału 09 jest warunkowe do czasu potwierdzenia bieżącego CI, mimo że poprzedni CI dla identycznego źródła był zielony.
