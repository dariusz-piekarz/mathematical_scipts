# Topologia ogólna — audyt globalny 26: rozliczenie zmiany wersji rozdziału 13

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Odczytany HEAD przed raportem:** `e122e1d3c126c568f722c67aeb7fe59f88a5c6fb`.
**Zakres:** niezależna kontrola historycznej rozbieżności źródła rozdziału 13 w audycie 09, potwierdzenie bieżących blobów rozdziałów 03 i 16, udokumentowanie statusu CI. Nie jest to powtórny pełny audyt wszystkich 281 dowodów ani nowy rendering PDF.

## 1. Identyfikacja rozbieżności 13

W raporcie `00-globalny-audyt-09-blok-12-18-kontrole-niezalezne.md` rozdział 13 ma **historyczny** blob `33200912c034f3f946909f00b9e4068deeca4ed0`. Bezpośrednio odczytany **aktualny** `chapters/pl/general_topology/13-zupelnosc-jednostajna-i-uzupelnienia.tex` ma blob **`c9078636452731e42a56196e84b5ed9831120e6b`** i 9 środowisk `proof`. Nie wolno przypisywać starego raportu do nowego bloba.

Zbadano osobno źródłowy ślad **po korekcie**: `13-zupelnosc-jednostajna-iteracja-07-czysty-audyt-1.md` i `08-czysty-audyt-2.md` dokumentują dwie odrębne czyste kontrole **dokładnie** bloba `c907...`; `09-audyt-potwierdzajacy.md` dokumentuje dodatkową kontrolę **tego samego** bloba. Aktualny test `tools/tests/test_general_topology_ch13.py` ma blob `c40ba836e7a53df0ea8b0974d384e365b2d22f12`, zgodny z raportem 09.

W aktualnym tekście niezależnie odczytano i zweryfikowano krytyczny fragment konstrukcji filtra `B(H,E)`: z gęstości otrzymuje się relację `(F,i(x))∈widehat D`; wybór **symetrycznego** `D⊆E` pozwala ją odwrócić do `(i(x),F)∈widehat D⊆widehat E`. Bez symetrii `D` takie odwrócenie nie byłoby uzasadnione. Następnie `B(H∩H',E∩E')⊆B(H,E)∩B(H',E')` daje własność bazową, a `D³⊆V` i warunek Cauchy'ego dla `H` dają średnicę entourage `V` dla wybranego zbioru bazowego na `X`. W tym miejscu aktualna wersja jest poprawna.

**Werdykt:** rozbieżność raportu 09 jest historycznym odniesieniem do wersji **sprzed korekty**, a nie nierozwiązanym konfliktem aktualnego źródła. Wersja aktualna ma udokumentowaną sekwencję 2+1 i test regresyjny. Nie należy jednak uznawać starszego audytu 09 za jeden z tych trzech audytów.

## 2. Kontrole pozostałych wcześniej wskazanych otwartych punktów

- **Rozdział 03:** aktualny blob `b571753b5ab9a8777424fc32f6c4a54a4048af77` jest identyczny z blobem szczegółowego potwierdzenia `00-globalny-audyt-17-potwierdzenie-03.md`. Raport 17 weryfikuje 15/15 dowodów, a raport 14 opisuje rzeczywisty siedmiostronicowy PDF i CI na tym samym źródle. **Brak nowej zmiany źródła** wymagającej ponownej stabilizacji.
- **Rozdział 16:** aktualny blob `1c2fcb925d62120feaea468400e48842a508a062` jest identyczny z badanym w globalnym audycie 10 i 09; liczba środowisk `proof`: 7. Weryfikacja wybranych twierdzeń w audycie 10 nie jest jednak automatycznie dowodem pełnego audytu każdego z siedmiu dowodów. Trzeba nadal powiązać ten rozdział z ewentualnym późniejszym raportem 7/7 albo wykonać brakującą kontrolę.
- **Weryfikacja CI aktualnego HEAD:** [workflow 45109592337](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45109592337) dla `e122e1d3c126c568f722c67aeb7fe59f88a5c6fb` ma **completed/success**. Ten wynik dotyczy **przedraportowego** commitu; nie zastępuje kontroli CI nowego commitu. Wcześniejszy [workflow 45070070493](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070070493) ma udokumentowane testy regresyjne rozdziału 13 oraz kompilację jego PDF; tamten test ma identyczny aktualny blob.
- W tej iteracji **nie uruchamiano lokalnie testów, nie pobierano artefaktów PDF i nie wykonywano oględzin stron**. Istniejące raporty PDF i CI są dokumentacją wcześniejszych rzeczywistych przebiegów, a nie nowymi pomiarami.

## 3. Stan i dalsza praca

**Zamknięty konkretny punkt:** uzgodnienie wersji 13 w starym raporcie 09 z aktualnym źródłem, po bezpośrednim sprawdzeniu obu raportów czystych, raportu potwierdzającego, testu regresyjnego i krytycznego argumentu o symetrii.

**Otwarte:** kompletny rejestr kontroli **każdego** dowodu 01–23 (bez podwójnego zaliczania raportów), w tym weryfikacja 7/7 rozdziału 16; ustalenie rzeczywistej liczby środowisk `proof` i rysunków na jednym zamrożonym HEAD zamiast mieszania historycznych liczb 261/281 i 27/24; wizualna kontrola wszystkich ilustracji, kompletności odsyłaczy i wydania; ostateczny niezależny globalny przegląd i PASS nowego CI.

**Następny krok:** zbudować rejestr 01–23 na jednym commicie, przypisać dowodom raporty wraz z identycznymi blobami, wykonać brakujące niezależne kontrole (priorytet: 16), a potem zamknąć pełny przegląd PDF i CI. **Automatyzacja pozostaje aktywna.**
