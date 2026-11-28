# Topologia ogólna — audyt globalny 38: pełny przegląd 27 podpisanych rysunków, naprawy 06 i 21

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło PDF przed poprawkami:** workflow [45129914798](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45129914798), commit `e7ff9254923fd87f9cad05301b15704e7038befd`, artefakt `14797512262`.
**Źródło PDF po poprawkach obu figur:** workflow [45133887910](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133887910), commit `1e0b2003b6a8a24a69400cb896ee5c6a45d99539`, artefakt `14798298647`, rzeczywiste `completed/success`.

## 1. Sposób kontroli

Z bieżącego wydania 188 stron, zbudowanego z aktualnych matematycznie źródeł, automatycznie odnaleziono **27 unikatowych podpisów „Rysunek x.y”** i wyrenderowano wycinki wokół wszystkich 27 w wysokiej rozdzielczości (2,75×), a następnie przygotowano i przejrzano pięć plansz przeglądowych. Sprawdzano czytelność napisów, położenie względem osi, znaki końców przedziałów, kolizje etykiet oraz kompletność podpisów. Osobno otwarto pełnorozdzielcze wycinki problematycznych rysunków 6.1 i 21.1, zarówno **przed**, jak i **po** korekcie.

**27 figure / 28 tikzpicture**: pierwsza ilustracja rozdziału 05 zawiera **dwa** diagramy w jednym figure; nie ma dodatkowego TikZ poza figure. Potwierdzono też istnienie wszystkich 27 numerowanych podpisów w późniejszym PDF.

## 2. Dwie rzeczywiste usterki w starym PDF

### Rysunek 6.1 (strona 50 książki)

Przed poprawką etykieta `ε` i `wyrazy dalsze` miały **nakładające się prostokąty tekstowe**. Z rzeczywistego PDF wyodrębniono:
- `ε`: przybliżony bbox `(313.52,123.27,318.60,134.18)` pt;
- `wyrazy dalsze`: bbox `(266.40,126.10,332.58,137.01)` pt.
Wspólny prostokąt ma dodatnie wymiary ok. **5,08 × 8,08 pt**, zatem problem był rzeczywisty, choć log LaTeX nie generował ostrzeżenia.

**Zmiana źródła** `chapters/pl/general_topology/06-zbieznosc-topologiczna.tex`:
- blob przed `365204000d0d5b21f213132e58b71aa48db3910e`,
- blob po `71d7b30abb97286b7c64ddd5e369ec9f69ea1ff5`,
- commit `9352c1be6617a2d031f7d26ead166b8ccc55995a`.
Przeniesiono etykietę „wyrazy dalsze” do `(.25,-1.05)` i zastosowano `font=\scriptsize`, pozostawiając oznaczenia ±ε bez zmian.

**Potwierdzenie nowego PDF:** etykieta „wyrazy dalsze” ma bbox `(255.39,139.69,306.71,147.66)` pt, a ε pozostaje `(313.52,123.27,318.60,134.18)` pt. Etykiety nie nakładają się; nawet ich zakresy pionowe dzieli **5,51 pt**.

### Rysunek 21.1 (strona 144 książki)

Oznaczenia A i B były umieszczone zbyt blisko siebie po lewej stronie osi; zmierzono:
- stare A `y∈[161.72,171.69]` pt;
- stare B `y∈[168.53,178.49]` pt;
zatem wspólna część pionowa mierzyła ok. **3,16 pt**, a szerokości oznaczeń także się pokrywały.

**Zmiana** `chapters/pl/general_topology/21-topologie-na-rodzinach-podzbiorow.tex`:
- blob przed `a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b`,
- blob po `eae0bef9c2357189e1bdb7c9398b845fe7347c7b`,
- commit `1e0b2003b6a8a24a69400cb896ee5c6a45d99539`.
Przesunięto A z y=.52 na y=.67 oraz B z y=.28 na y=.13, pozostawiając punkty zbiorów i ich współrzędne bez zmian.

**Nowy PDF:** A ma `y∈[161.72,171.69]` pt, B `y∈[177.03,186.99]` pt — pionowa przerwa **5,34 pt**. Etykiety pozostają wizualnie związane ze swoimi kolorowymi punktami.

## 3. Matematyka, odsyłacze, testy i CI

Po poprawkach **porównano dosłownie** źródłowe treści wszystkich środowisk `proof` na pierwotnym commicie `73bfc3fb9f83c4e22afad138237a395fe50363ed` i późniejszej gałęzi:
- rozdział 06: **18/18 identycznych tekstów proof**;
- rozdział 21: **15/15 identycznych tekstów proof**;
- w obu rozdziałach wszystkie sekwencje `label` i `ref/eqref/pageref` są **identyczne**.
Zachowano więc całą treść matematyczną, przykłady (poza geometrią dwóch etykiet), definicje i odsyłacze. Nadal są 2 rysunki w 06 i 1 w 21, a pełna książka ma **188 stron i 27 podpisów**.

Z artefaktu workflow `45133887910` pobrano samodzielne `general_topology_ch06.pdf` i `general_topology_ch21.pdf` oraz pełną książkę; pliki `general_topology.log`, `general_topology_ch06.log`, `general_topology_ch21.log` nie mają żadnych wystąpień `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` ani `Fatal error`. Samodzielne strony PDF pozostały kompilowalne.

Aby zapobiec powrotowi kolizji, dodano **regresje statyczne geometrycznych odstępów etykiet** w:
- `tools/tests/test_general_topology_ch06.py` — warunek minimalnego odstępu pionowego `0.40` jednostki TikZ między ε a „wyrazy dalsze”;
- `tools/tests/test_general_topology_ch21.py` — odstęp pionowy `≥0.45` jednostki TikZ między podpisami A i B.

**Ważna historia CI:** pierwsze wersje obu asercji wygenerowano z usterką składni testów Pythona przy zastępowaniu kodu źródłowego; workflow `45133997697`, `45134028443` i `45134149660` zakończyły się niepowodzeniem testowym. Testy zostały poprawione osobnymi commitami `a83663b9880d45f06627b60417ee483f27209755` (06) i `a0dd1d5f10c0d3b47b8ddab59ebc7c04d23e11ef` (21). Na moment spisania pomiaru końcowy workflow `45134198801` wymaga jeszcze potwierdzenia wyniku; **nie przypisujemy mu zawczasu PASS**. Wcześniejszy workflow z poprawionymi diagramami, bez regresji, ma **rzeczywisty PASS**.

## 4. Werdykt i wymagania stabilizacji

**PASS wizualny po korektach — kolizje rysunków 6.1 i 21.1 usunięte w rzeczywistym PDF bez zmiany jakiegokolwiek z 33 dowodów.** W pozostałych 25 podpisanych rysunkach podczas nowego przeglądu nie zidentyfikowano ewidentnych ucięć ani kolizji; plansze zbiorcze nie zastępują jednak analizy wszystkich drobnych napisów w powiększeniu.

**Rozdziały 06 i 21 otrzymały nowe bloby źródłowe**, więc dla pełnej zgodności z zasadą stabilizacji 2+1 należy wykonać co najmniej dwa czyste niezależne audyty poprawionego wydania i jedną kontrolę potwierdzającą. Dawnych 2+1 nie wolno przepisać na nowe SHA bez odrębnego uzgodnienia. Dalsze warunki zamknięcia: rzeczywiście zielony CI z nowymi testami i aktualizacja macierzy 325/325 na dwóch nowych blobach.
