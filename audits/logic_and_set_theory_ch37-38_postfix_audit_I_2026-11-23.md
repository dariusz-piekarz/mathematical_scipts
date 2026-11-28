# Logika matematyczna i teoria mnogości — niezależny audyt I po korektach rozdziałów 37–38

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział 37:** `chapters/pl/logic_and_set_theory/37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex`; blob `6c495beddc92e39b6885171e6415f0efe21d5b59`.  
**Rozdział 38:** `chapters/pl/logic_and_set_theory/38-kardynaly-mahla-i-slaba-zwartosc.tex`; blob `28d73acfcc3a6db9519822df210aa66391c51628`.

**Werdykt:** pierwsza niezależna kontrola obu nowych blobów po korektach jest **czysta (1/2)** w zakresie poniższych dowodów, języka, środowisk i odsyłaczy. Brak kolejnych koniecznych zmian w źródłach. Nie przyznaje się jeszcze statusu stabilnego 2/2+1.

## 1. Zakres niezależnego audytu matematycznego — rozdział 37

1. **Współkońcowość i nieosiągalność, linie 24–104.** Z warunku `κ=λ^+` i Cantora otrzymuje się `2^λ≥λ^+=κ`, sprzecznie z `2^λ<κ`. Dowód `|V_α|<κ` nie pomija dwóch różnych założeń: na etapach następnikowych używa silnej graniczności, na etapach granicznych — regularności oraz `|α|<κ`. Przypadek `α=0` jest odrębnie uwzględniony.
2. **`V_κ ⊨ ZFC`, linie 106–162.** Wyróżnianie i zastępowanie opierają się na prawdziwości w **zbiorowej strukturze** `V_κ`. Obrazy `a∈V_κ` mają moc `≤|a|<κ` i dlatego ich rangi są wspólnie ograniczone poniżej κ. Aksjomat wyboru jest zachowany, bo relację dobrze porządkującą `a` można umieścić w ustalonej skończonej iteracji potęgowania `a` poniżej κ. Nie ma niejawnego użycia prawdy dla całego uniwersum w sensie Tarskiego.
3. **Poprawność wniosku o niesprzeczności, linie 164–187.** ZFC dowodzi implikacji `(∃κ inaccessible)⇒Con(ZFC)`, a drugi Gödel wyklucza jej bezwarunkowy dowód przez niesprzeczną ZFC. Nie wyciąga się z tego względnej niesprzeczności aksjomatu istnienia dużej liczby kardynalnej.
4. **Jednorodność ultrafiltru, linie 226–297.** Dla każdego `A⊆κ` o mocy mniejszej od κ przecięcie dopełnień singletonów pozostaje w ultrafiltrze, także gdy `A=∅`. W dowodzie regularności dokładnie `cf(κ)<κ` małych przedziałów nie może wyczerpać κ, jeśli wszystkie są małe dla ultrafiltru. W dowodzie silnej graniczności z `κ↪P(λ)` wybrane `λ<κ` współrzędnych daje przecięcie w ultrafiltrze o rozmiarze co najwyżej 1 — sprzeczność. Po korekcie występuje prawidłowe „liczba kardynalna λ *taka*, że”.
5. **Twierdzenie Łosia i ultraprodukt, linie 319–451.** Dla każdej *ustalonej* formuły można w ZFC zdefiniować zbiór indeksów spełniających ją. W kroku egzystencjalnym wybór najmniejszej rangi świadka i AC dla rodziny indeksowanej zbiorem `D` dostarczają jednej funkcji świadków. Scottowskie reprezentanty kodują klasowy iloraz zbiorami. Przeliczalna zupełność wynikająca z `κ>ω` eliminuje nieskończone ciągi malejące w relacji ultraproduktu.
6. **Punkt krytyczny i normalizacja, linie 453–702.** Indukcja dla `j(α)=α` przy `α<κ` prawidłowo używa liczby włókien `<κ`, nie wymaga normalności początkowej miary. Porównanie `[c_α]<[i]<[c_κ]` daje `j(κ)>κ` bez nieuzasadnionego utożsamienia `[i]` z κ. Definicja `W={X⊆κ:κ∈j(X)}` jest normalna: dla funkcji regresywnej `j(f)(κ)=ξ<κ`, więc `κ∈j(f^{-1}({ξ}))`.
7. **Środowiska i redakcja.** Po poprawkach oba wystąpienia „nieprzeliczalną regularną liczbą kardynalną” w definicji i twierdzeniu o normalności są gramatycznie spójne. Rozdział nadal zawiera 7 definicji, 4 lematy, 7 twierdzeń, 1 wniosek, 5 uwag, 1 przykład, 12 dowodów.

## 2. Zakres niezależnego audytu matematycznego — rozdział 38

1. **Przecięcia klubów, linie 28–139.** Przy `μ<κ` rekurencja długości ω tworzy punkt domknięcia we *wszystkich* `C_ξ`. Dla diagonalnego przecięcia `D` każdy `ξ<δ` należy ostatecznie do zakresu indeksów `ξ≤γ_n`; domkniętość danego `C_ξ` uzasadnia `δ∈C_ξ`. Nie używa się nieprawdziwej zwartości przecięcia dowolnych κ klubów.
2. **Lemat Fodora, linie 141–182.** Przy przeciwnym założeniu każde włókno regresywnej funkcji ma rozłączny klub. Diagonalne przecięcie klubów oraz `f(α)<α` wymuszają sprzeczność. Usunięcie 0 ze stacjonarnej dziedziny jest legalne, ponieważ ogon ponad 0 jest klubowy.
3. **Liczba kardynalna Mahla, linie 214–260.** W definicji żąda się stacjonarności zbioru silnie nieosiągalnych liczb kardynalnych, nie samej nieograniczoności. Poprawione uzgodnienie „liczba kardynalna λ *taka*, że” jest prawidłowe; nie zmieniono kwantyfikatora `α<λ<κ`.
4. **Drzewo i zanurzenie, linie 264–395.** Jeśli `t∈j(T)_κ`, poprzednik `u_α` dla `α<κ` leży w `j(T_α)`; małość `T_α` pozwala utożsamić `j(T_α)` z `{j(s):s∈T_α}`. Odbite węzły `s_α` są liniowo uporządkowane, a zastępowanie tworzy zbiór κ węzłów. Nie utożsamiono dowodu dla jednej gałęzi pełnego drzewa binarnego z własnością wszystkich drzew κ-owych.
5. **Normalna miara i kluby, linie 399–498.** Jeśli klub `C` nie należy do normalnej miary, funkcja `α↦sup(C∩α)` na odpowiedniej dużej dziedzinie jest regresywna. Włókno stałej wartości przeczyłoby nieograniczoności `C` i jednorodności ultrafiltru. Dowód `κ∈j(I_κ)` weryfikuje regularność i silną graniczność κ wewnątrz tranzytywnego `M`, używając faktu `M⊆V` oraz `P^M(λ)⊆P^V(λ)`.
6. **Mierzalność i kolorowania, linie 502–582.** Dokładnie jeden kolor `i_α` ma duże włókno nad ogonem `α`. Na kroku `ξ<κ` przecina się *mniej niż κ* zbiorów miary jeden; wspólny zbiór jest nieograniczony, więc można wybrać następny element `α_ξ`. Argument nie wymaga jednoczesnego przecięcia κ wielu zbiorów.
7. **Środowiska i redakcja.** Poprawiono odmianę „w nieprzeliczalnej regularnej liczbie kardynalnej κ” bez zmiany treści lematu. Rozdział nadal zawiera 8 definicji, 4 lematy, 5 twierdzeń, 1 wniosek, 5 uwag, 2 przykłady, 10 dowodów.

## 3. Kontrola techniczna

Ponownie pobrano pliki z GitHuba, a nie tylko wcześniejsze raporty. Aktualne bloby i liczba wierszy:

| Rozdział | Blob | Wiersze | Etykiety | Odsyłacze |
|---|---|---:|---:|---:|
| 37 | `6c495beddc92e39b6885171e6415f0efe21d5b59` | 775 | 26 | 18 |
| 38 | `28d73acfcc3a6db9519822df210aa66391c51628` | 640 | 26 | 19 |

- Obie struktury `\\begin/\\end` poprawnie domknięte; brak niezamkniętych środowisk.
- W obu plikach brak samodzielnego rzeczownika „kardynał” w treści.
- Wszystkie 19 odsyłaczy rozdziału 38 prowadzą do etykiet rozdziałów 37–38. Pięć odsyłaczy z rozdziału 37 prowadzi do potwierdzonych wcześniej etykiet w rozdziałach 22, 25, 31, 35 i 36.
- Porównanie commitów [a09047a...a44363d](https://github.com/dariusz-piekarz/mathematical_scipts/compare/a09047abb488c32b7c0ea4a3e7bfc47cec9ac6bb...a44363dce5669206c76e5cc342748e6fc7a70efb) wykazało jedynie **3 zastąpione wiersze rozdziału 37** i **2 rozdziału 38**; żadnych innych plików źródłowych nie modyfikowano w tym zakresie.
- [Walidacja skryptu logiki i teorii mnogości 45081007565 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007565): w rzeczywistych krokach zadania `validate-chapters` przeszły także regresje 37 i 38, kompilacja PDF, analiza logu oraz archiwizacja artefaktu.
- [Test terminologii 45081007498 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007498).
- [Kontrole aplikacji 45081007531 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007531).

**Uwaga o granicach kontroli:** w bieżącej iteracji nie pobierano i nie oglądano ponownie graficznie stron PDF; zaliczenie kroku „Check compiled PDF and log” nie jest osobnym audytem wizualnym. Nie przeprowadzono formalizacji w Lean.

## 4. Werdykt i dalszy tok

**Rozdział 37: czysty audyt nowego bloba I (1/2). Rozdział 38: czysty audyt nowego bloba I (1/2).** Dalszy tok: drugi niezależny audyt matematyczny na tych samych blobach, później niezależna kontrola potwierdzająca (+1) i, przy niezmienionych źródłach oraz zielonym CI, przywrócenie statusu stabilnego. Nie dodano nowej treści do zatwierdzonych rozdziałów.

**Osobna propozycja, bez ingerencji w źródło:** w przyszłości można rozważyć udowodnienie, że słabo zwarta liczba kardynalna jest liczbą kardynalną Mahla. Jest to wzmocnienie hierarchii rozdziałów 38–39, ale nie jest konieczne do poprawności obecnych wyników i wymaga osobnej zgody.
