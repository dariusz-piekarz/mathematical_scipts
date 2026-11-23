# Analiza funkcjonalna — rozdział 09 — audyt 03 (niezależna kontrola stabilizacyjna)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/09-banach-alaoglu-krein-milman-i-topologia-mackeya.tex`.  
**Blob SHA źródła:** `d0a20b01bdabfa4e85d9c00ebe11c8c41bea650a` — **dokładnie ten sam, który pozostawiono po poprawkach audytu 09/02**.  
**Zakres:** niezależna kontrola wszystkich 14 dowodów, 8 przykładów, definicji, warunków granicznych, terminologii, oznaczeń, rysunku i odsyłaczy w kontekście rozdziałów 01–09.  
**Werdykt audytu matematyczno-redakcyjnego:** **CZYSTY — 1/2** kolejnych czystych kontroli tej samej wersji. **Nie zmieniano pliku źródłowego.**

## Weryfikacja kontekstu i powtórna kontrola dowodów

Przed napisaniem niniejszego raportu pobrano na nowo cały rozdział 09, wszystkie poprzednie rozdziały 01–08, bieżący plik 19 testów oraz raport 09/02. Sprawdzono SHA źródła i osobno każdą z poniższych jednostek; wcześniejszy zielony CI nie jest traktowany jako dowód matematyczny.

1. **Równociągłość i zbiory polarne.** Użycie otoczenia dla `ε=1` i odwrotne skalowanie `(ε/2)U` są poprawne także w nielokalnie wypukłych TVS. Punktowa ograniczoność wynika z pochłaniania przez `U`; dla pustej rodziny funkcjonałów interpretacja jest trywialna.
2. **Banach–Alaoglu–Bourbaki.** Otoczenie zera jest pochłaniające, więc można ograniczyć każdą współrzędną algebraicznie liniowego `f`. Warunki addytywności, jednorodności i oszacowania na `U` są domknięte w produkcie zwartych dysków. Oszacowanie na skalowanym `U` zapewnia ciągłość każdego powstałego `f`. Nie wprowadzono niejawnych założeń Hausdorffa, zupełności ani lokalnej wypukłości.
3. **Słabo-* zwartość normowej kuli.** `U°=B'_R` przy `R>0`, a przypadek `R=0` jest rozpatrzony jawnie.
4. **Domknięte podzbiory kuli.** Słabo-* domkniętość w zwartej kuli daje zwartość także dla `A=∅`.
5. **Metryzowalność rodziny równociągłej.** Metryka z przeliczalnej rodziny wartościowań rozdziela funkcjonały, a równociągłość kontroluje dwa składniki błędu `f(x-x_n)` i `f_0(x_n-x)`, dając dokładnie topologię punktowej zbieżności na całym `E`.
6. **Kryterium ośrodkowości z metryzowalności kuli.** Ciąg bazowych słabo-* otoczeń zera prowadzi do przeliczalnej rozpiętości `M`; gdyby nie była normowo gęsta, Hahn–Banach dałby niezerowy funkcjonał w każdym z tych otoczeń, sprzecznie z własnością Hausdorffa. Kierunek odwrotny korzysta z równociągłości kuli.
7. **Ściana poziomicy maksymalnej.** Ciągły rzeczywisty funkcjonał osiąga maksimum na zwartym wypukłym `K`; własności wypukłości i ściany wynikają z liniowości i ograniczenia przez maksimum. Przechodniość ścian działa również nad `C` przy wypukłości rzeczywistej.
8. **Istnienie punktu ekstremalnego.** Odwrotne uporządkowanie domkniętych niepustych ścian ma ograniczenia łańcuchów na mocy zwartości. Zorn i ciągły funkcjonał rozdzielający dwa punkty wymuszają singleton będący ścianą.
9. **Krein–Milman.** Domknięta otoczka wypukła punktów ekstremalnych pozostaje w zwartym `K`; ścisłe oddzielenie punktu spoza niej daje maksymalizującą ścianę i punkt ekstremalny łamiący nierówność. Sprawdzono realną postać oddzielania dla przestrzeni zespolonych.
10. **Zasada maksimum Bauera.** Przy wypukłej i półciągłej z góry funkcji zbiór maksimów jest domknięty, niepusty i ekstremalny, choć nie musi być wypukły. Zorn stosuje się do rodziny zamkniętych ekstremalnych podzbiorów; singleton kończy dowód.
11. **Lemat zwartej dominacji.** W skończenie wymiarowych obrazach `T_S(K)` możliwe jest ścisłe oddzielenie punktu; absolutna wypukłość `K` daje `sup Re = sup |·|` na jednowymiarowym obrazie. Własność skończonych przecięć i zwartość `K` zapewniają wspólne rozwiązanie wszystkich równań.
12. **Mackey–Arens.** Funkcjonały ciągłe dla `τ(E,F)` dominują skończone maksima seminorm; zwarta suma Minkowskiego `K_1+...+K_m` pozwala zastosować lemat. W odwrotnym kroku `K_p={f:|f(x)|≤p(x)}=U°` przy `U={p≤1}`, a Hahn–Banach pozwala odtworzyć `p=p_{K_p}`. Oba kierunki zgodności są uzasadnione.
13. **Najsilniejsza/najsłabsza topologia zgodna.** `σ(E,F)⊂ρ⊂τ(E,F)` jest bezpośrednim wnioskiem z definicji początkowej i poprzedniego twierdzenia.
14. **Kryterium interpolacji.** Dla każdego skończonego `J` warunek na wszystkie kombinacje gwarantuje poprawną definicję oraz ograniczoność `g_J`; Hahn–Banach daje `f_J`. Słabo-* zamkniętość warunków i zwartość normowej kuli zapewniają właściwy wniosek nawet dla nieskończonego `I`, także przy powtarzanych indeksach i `R=0`.

**Wynik:** 14/14 argumentów poprawnych przy podanych hipotezach. Nie wykryto nowej luki wymagającej dopisania warunków do twierdzeń.

## Powtórna kontrola 8 przykładów

1. `E=c_0, E'=ℓ¹`: słabo-* zwarta metryzowalna kula; wektory bazowe nie mają podciągu Cauchy'ego w normie.
2. `E=ℓ¹(I)` z nieprzeliczalnym `I`: produkt dysków z topologią współrzędną jest słabo-* zwarty i niemetryzowalny. Kierowana sieć `χ_F` zbiega do `χ_I`, żadna sekwencja skończonych nośników tej granicy nie osiąga — tekst używa poprawnie **ciągów**, nie dawnej notacji `\\mathbf 1`.
3. Niezupełne `c_{00}`: `f_n(x)=n x_n` daje słabo-* zbieżny ciąg do zera, a `||f_n||=n`, stąd zwartość bez równociągłości.
4. Ekstremalne punkty wypukłego wielokąta oraz kuli **niezerowej** rzeczywistej przestrzeni Hilberta: wcześniejsze kontrprzykłady dla niewypukłego wielokąta i `H={0}` są wyeliminowane; tożsamość równoległoboku działa.
5. Produkt przedziałów `[-1,1]^I`: ekstremalność wymusza każdą współrzędną równą `±1`.
6. Rzeczywista kula `ℓ¹`: ekstremalne punkty `±e_n` oraz rozkład pozostałych punktów przez przeniesienie małej części masy lub perturbację wektora o normie poniżej 1.
7. Nieskończenie wymiarowy Banach: topologia słaba nie jest normowalna, więc jest ściśle słabsza niż zgodna topologia normowa, a ta nie jest silniejsza od Mackeya.
8. `ℓ¹` i zadawanie wartości na `e_n`: ograniczona rodzina `b_n` określa element `ℓ∞`; przy powtórzonych indeksach sumowanie po tej samej współrzędnej jest właściwe.

**Wynik:** 8/8 bez nowych błędów matematycznych. Jedyny rysunek TikZ i podpis reprezentują punkt ekstremalny oraz ścianę poziomicy; poprzedni audyt 09/02 dokumentuje bezkolizyjny skład PDF w stronach 48–55 aktualnej wersji.

## Niezależna kontrola struktury, terminologii i zależności

Na nowo pobranych plikach 01–09 zweryfikowano: **159 etykiet łącznie, żadnego powtórzenia**, **23 etykiety rozdziału 09**, **14 odsyłaczy rozdziału 09, żadnego brakującego celu**. Wszystkie środowiska są zbilansowane: 14 `proof`, 6 `twierdzenie`, 1 `stwierdzenie`, 4 `wniosek`, 3 `lemat`, 3 `definicja`, 8 `przyklad`, 4 `uwaga`, 2 `enumerate`, 1 `tikzpicture` i 1 `center`.

W rozdziale 09 brak poprzednio wykrytych błędnych oznaczeń funkcji charakterystycznych `\\mathbf 1` i `\\mathbb 1`. Sprawdzono lokalną zgodność terminologii „przestrzeń sprzężona”, „przestrzeń algebraicznie sprzężona”, „ciąg” i „zwartość ciągowa”. Polski przymiotnik „dualna” w tytule jednego przykładu jest dopuszczalnym odpowiednikiem, nie stanowi samodzielnego angielskiego rzeczownika „dual”; nie wymusza zmian w stabilizowanym źródle.

**Aktualny plik testów:** `tools/tests/test_functional_analysis_ch09.py`, SHA `b563c54e380f9d98bfab3cebf1bf51bd1cca8a96`; zawiera 19 testów. Potwierdzono dedykowany [GitHub Actions **#45211318985**](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45211318985): status **SUCCESS**, w tym testy, przygotowanie dziewięciu rozdziałów, kompilacja LaTeX, automatyczne sprawdzenie PDF i odsyłaczy oraz publikacja artefaktu. Jest to CI na commicie raportu 09/02, ale przy tym samym blob SHA źródła i testów co obecnie. Automatyczne testy nie poświadczają same z siebie matematycznej poprawności twierdzeń; ta została skontrolowana oddzielnie powyżej.

Nie ma w tej iteracji zmian źródłowych ani testowych; **nie deklarowano nowej, niezależnej inspekcji wyrenderowanego PDF**, opierając kontrolę wizualną na pełnej inspekcji z raportu 09/02 i kontroli CI.

## Decyzja i następny krok

**Audyt 09/03 — CZYSTY (1/2).** Plik źródłowy pozostaje niezmieniony względem zakończenia 09/02. Przed przejściem do rozdziału 10 konieczny jest **jeszcze jeden niezależny, czysty audyt 09/04 dokładnie tego samego SHA źródła**, a po zatwierdzeniu zielonego CI można uznać rozdział 09 za stabilny.
