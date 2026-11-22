# Topologia ogólna — rozdział 15: audyt iteracja 02

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Samodzielny audyt matematyczny — bez nowych twierdzeń

Skontrolowano całą aktualną treść `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex` (blob SHA `07698d6f300129b9e1ec8d7c4ab65888b272560d`), niezależnie od raportu 01. W tej iteracji nie wykryto luki wymagającej korekty matematycznego źródła.

### 1. Lokalna skończoność

Dla ustalonego `x` otwarty `O_x` przecina tylko skończenie wiele `A_i`. Jeśli `O_x∩A_i=∅`, to także `O_x∩cl(A_i)=∅` (bo otwarty zbiór rozłączny z `A_i` jest rozłączny z jego domknięciem). Dlatego rodzina domknięć pozostaje lokalnie skończona. W drugiej części dla `x∉⋃cl(A_i)` zbiór `O_x\setminus⋃_{i∈F}cl(A_i)` jest otwartym otoczeniem `x`, rozłącznym z całą sumą. Dowód nie zakłada żadnych aksjomatów oddzielania.

### 2. Funkcje odcinające

Przy założeniach `F⊂W⊂cl(W)⊂V`, `F` domknięty, `W,V` otwarte, funkcja z lematu Urysohna dla rozłącznych domkniętych zbiorów `F` i `X\setminus W` jest równa `1` na `F`, `0` poza `W` i ma nośnik zawarty w `cl(W)⊂V`. W głównej konstrukcji role odpowiadają: `F=cl(W_n)`, `W=V_n`, `V=U_n`, dzięki `cl(W_n)⊂V_n⊂cl(V_n)⊂U_n`. Zatem pojedyncze funkcje `f_n` spełniają dokładnie warunki używane dalej. Normalność `X` wynika z udowodnionego w rozdziale 10 twierdzenia o regularnych przestrzeniach Lindelöfa (Hausdorff).

### 3. Właściwa lokalna skończoność podziału

`φ_n=f_n∏_{j<n}(1-f_j)`. Gdy `x∈W_N`, na całym otwartym `W_N` mamy `f_N=1`. Dla `n>N` zachodzi `φ_n|_{W_N}=0`, a otwartość `W_N` implikuje `supp φ_n∩W_N=∅`. Co najwyżej `N` nośników przecina `W_N` — to dowodzi lokalnej skończoności, a nie tylko punktowej skończoności wartości. Tożsamość `Σ_{n≤m}φ_n=1-∏_{n≤m}(1-f_n)` daje dokładnie `Σφ_n(x)=1` przy wyborze `N` z `x∈W_N`. Nie jest potrzebna żadna granica nieskończonego iloczynu.

### 4. Przypadki brzegowe

Jeśli `X=∅`, pusta rodzina funkcji i puste pokrycie załatwiają twierdzenie wprost. Jeśli `X` jest niepusty, to pokrycie `U` jest niepuste, więc po wybraniu skończonego podpokrycia można uzupełnić listę o `W_n=V_n=∅` i wybrane `U_n∈U` bez naruszenia konstrukcji; wtedy `f_n=0` dla pustych zbiorów. To zapewnia poprawność indeksowania przez `n≥1`.

### 5. Pozostałe wyniki i przykłady

- Zbiory `{φ_i>0}` są otwarte, zawarte w odpowiednich nośnikach i tworzą lokalnie skończone uszczegółowienie dowolnego pokrycia: przejście od podziałów jedności do parazwartości jest poprawne.
- Przestrzeń metryzowalna spełniająca drugi aksjomat przeliczalności jest regularna, Hausdorffa i Lindelöfa; lokalnie zwarta `σ`-zwarta przestrzeń Hausdorffa jest regularna i Lindelöfa. Wniosek ma komplet hipotez.
- Trójkątne funkcje `h_n(x)=max(0,1-|x-n|)` mają nośniki `[n-1,n+1]`, są lokalnie skończone i sumują się do `1` na każdym `[n,n+1]`. Nieprzeliczalna przestrzeń dyskretna dostarcza poprawnego kontrprzykładu dla implikacji parazwartość ⇒ Lindelöf.

## Testy i PDF

Wersja źródła po audycie 01 i przed niniejszym raportem jest niezmieniona. Zielone przebiegi CI dla tej wersji: `45009615654` i `45009691163` (`completed/success`), po wcześniejszym usunięciu brakującej etykiety w samodzielnym PDF. Zależne testy i kompilacja pełnej książki przeszły. Artefakt `14749367232` obejmuje samodzielny PDF rozdziału 15 (3 strony A4). Oględziny wszystkich 3 stron i analiza logów podczas audytu 01 nie wykazały problemów składu ani ostrzeżeń. W niniejszym audycie dodatkowo sprawdzono tekst wyrenderowanego PDF z zachowaniem układu i obecność wszystkich końcowych wzorów i przykładów.

## Werdykt i dalsza praca

| Kryterium | Wynik |
| --- | --- |
| Poprawność matematyczna istniejącego materiału | PASS |
| Szczegółowość dowodów i uzasadnienie wzorów | PASS |
| Przypadki brzegowe, nośniki, lokalna skończoność | PASS |
| Terminologia, etykiety i zależności 01–14 | PASS |
| Testy, pełna książka i samodzielny PDF | PASS — na niezmienionym źródle |
| Błędy wymagające korekty w audycie 02 | **BRAK** |
| Zakres rozdziału 15 | **NIEPEŁNY**: ogólne twierdzenie Stone'a o parazwartości wszystkich przestrzeni metrycznych jest tylko wspomniane, bez dowodu |
| Stabilizacja rozdziału 15 | **W AUDYCIE** — dalsza iteracja powinna rozwinąć i udowodnić twierdzenie Stone'a, następnie przeprowadzić nowe audyty |

Nie należy traktować braku błędów w aktualnych dowodach jako formalnego uzasadnienia nieudowodnionego jeszcze twierdzenia Stone'a.
