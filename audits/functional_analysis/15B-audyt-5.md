# Analiza funkcjonalna — moduł 15B — audyt 05 (pierwszy czysty przegląd po korektach 15B/04)

**Data:** 24 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`, istniejąca.  
**Źródło:** `chapters/pl/functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex`.  
**Blob SHA źródła:** `3611164daa8a7ca1d73fc4b564825bddd044d100`.  
**Test:** `tools/tests/test_functional_analysis_ch15b.py`, blob SHA `c73a00941b5789093f5f9322f79f79df059be4e7`.  
**Wynik:** **PIERWSZY CZYSTY AUDYT (1/2)** na źródle po poprawkowym 15B/04. Żadnych zmian w twierdzeniach, przykładach lub testach. Potwierdzenie dedykowanego CI po zapisie niniejszego raportu pozostaje warunkiem technicznym; zielone CI nie zastępuje drugiego czystego przeglądu.

## Rewizja źródła i wcześniejszych zmian

Niezależnie ponownie pobrano aktualne źródło, wszystkie sześć regresji, raport 15B/04 i przebieg CI [#45305576829](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45305576829). Ten przebieg dla commitu `85933597fe88af4a500c675915814562bfb388fd` ma status **completed/success**; odczytano bezpośrednio wszystkie dziewięć kroków zadania `audit-ch15b`, z których każdy jest oznaczony `success`. Obejmują one wykonanie regresji, wygenerowanie kontekstu 01–17 (wraz z 15A i 15B), kompilację LaTeX, maszynową kontrolę PDF i odsyłaczy oraz publikację artefaktu.

Poprzedni audyt 15B/04 miał status **POPRAWKOWY (0/2)**: w dwóch twierdzeniach wypisano jawnie kwantyfikatory, przestrzenie, mierzalność i hipotezy skalarnych całek; doprecyzowano też, że całka Dunforda z przykładu znajduje się w `X''`, lecz poza obrazem `J_X(X)`. Szósty test regresyjny zabezpiecza te sformułowania. Dwa przejściowo nieudane przebiegi CI dotyczyły asercji szukającej osobnego napisu `$X''$` zamiast faktycznego wyrażenia przynależności `\in X''`; finalny test sprawdza poprawny tekst. Nowa wersja źródła i regresji ma niezmienione bloby podane w nagłówku.

## Kontrola matematyczna — wszystkie 11 dowodów

1. **Mierzalność Pettisa** (`thm:pettis-meas15b`): słaba mierzalność silnie mierzalnej funkcji wynika z granic skalarów; jej obraz leży prawie wszędzie w ośrodkowej domkniętej podprzestrzeni generowanej przez wartości przeliczalnych funkcji prostych. W kierunku odwrotnym rodzinę normującą przestrzeń ośrodkową otrzymuje się przez Hahna–Banacha z gęstej rodziny wektorów jednostkowych; dla przestrzeni zerowej wystarcza funkcjonał zerowy. Mierzalność odległości od gęstego ciągu pozwala skonstruować funkcje proste z ogonami miary mniejszej od `2^{-n}`; lemat Borela–Cantellego zamienia to na zbieżność prawie wszędzie.
2. **Kryterium Bochnera** (`thm:bochner-criterion15b`): całki funkcji prostych są Lipschitzowskie względem normy `L^1`, więc w Banachu mają granicę niezależną od aproksymacji. Dla silnie mierzalnej funkcji o całkowalnej normie obcięte przybliżenia `s_n` spełniają `||s_n-f||<=3||f||` i zbiegają prawie wszędzie; dominacja skalarna uzasadnia przejście do `L^1`. Przemienność z ograniczonym operatorem liniowym jest zachowana.
3. **Zbieżność zmajoryzowana Bochnera** (`thm:bochner-dct15b`): dobór prostego przybliżenia dla `f_n` z wyjątkowym zbiorem miary `<2^{-n}` i Borel–Cantelli gwarantują silną mierzalność granicy; `||f_n-f||<=2g` zapewnia zbieżność całek.
4. **Fubini Bochnera** (`thm:bochner-fubini15b`): wersja względem uzupełnionej miary produktowej została prawidłowo zredukowana do mierzalnego przedstawiciela na nieuzupełnionej `sigma`-algebrze. Przekroje zerowego zbioru wyjątkowego są zerowe dla prawie wszystkich parametrów. Aproksymacja prostokątna w `L^1` z błędami `<4^{-n}` i twierdzenie Tonellego umożliwiają kontrolę przekrojów. Silna mierzalność przekrojów jest uzasadniona przed całkowaniem Bochnera; funkcja `F(s)=int_T f(s,t)dnu(t)`, przedłużona zerem poza zbiorem pełnej miary, jest granicą prostych `F_n`; dopiero po ustaleniu tej mierzalności stosuje się Tonellego do różnic. To pozwala bez luki zidentyfikować oba porządki całkowania.
5. **Zgodność Riemann–Bochner** (`prop:riemann-bochner15b`): ciągła krzywa w Banachu ma jednostajnie bliskie przybliżenia prostymi funkcjami na odcinkach; kontrprzykład z funkcją charakterystyczną wymiernych pomnożoną przez niezerowy wektor wyjaśnia brak implikacji odwrotnej.
6. **Dunford** (`thm:dunford-closedgraph15b`): jawnie podano przestrzeń z miarą, ciało skalarów, Banacha X, słabą mierzalność i całkowalność każdego `x'∘f`. Wykres `Q_f:X'→L^1` jest domknięty, gdyż zbieżność normowa funkcjonałów daje zbieżność punktową, a `L^1` dopuszcza podciąg zbieżny prawie wszędzie. `D_A` jest ograniczonym funkcjonałem na `X'`, czyli elementem `X''`.
7. **Hierarchia** (`thm:hierarchy-integrals15b`): całka Bochnera przenosi się przez każdy `x'`; istnienie wszystkich elementów reprezentujących `D_A` w X jest równoważne całkowalności Pettisa. Tekst nie utożsamia `X` z `X''` bez zanurzenia kanonicznego.
8. **Zbieżność Pettisa** (`thm:pettis-convergence15b`): refleksywność zapewnia reprezentowalność skalarnej całki Dunforda w X. Założona mierzalność `||f_n-f||` jest potrzebna i rzeczywiście występuje; po normowaniu funkcjonałów dostaje się oszacowanie normowe różnicy całek, a zbieżność zmajoryzowana skalarna daje granicę zero.
9. **Gelfand** (`thm:gelfand-exists15b`): twierdzenie ma samodzielnie wypisane Y, skalary, miarę, słabą-* mierzalność i skalarną całkowalność. Z domkniętego wykresu `Q:Y→L^1` uzyskujemy funkcjonał `g_A∈Y'`. Skalarna przeliczalna addytywność po każdym `y∈Y` daje dokładnie słabą-* addytywność; bez dodatkowych warunków nie implikuje normowej.
10. **Całkowita wariacja** (`prop:variation-measure15b`): jedna nierówność dla rozłącznej sumy jest uzyskana przez połączenie skończenie wielu partycji, druga przez rozbicie każdej części partycji względem wszystkich `A_n`, addytywność normową miary wektorowej i nierówność trójkąta. Dowód działa również przy nieskończonej wariacji.
11. **Miara z całki Bochnera** (`thm:bochner-measure15b`): ogony są kontrolowane przez `int_{union_{n>N}A_n}||f||`; partycje poziomicowe dają równość wariacji dla funkcji prostych, a oszacowanie różnicy wariacji przez normę `L^1` zapewnia tezę dla ogólnych funkcji.

**11/11 dowodów bez nowej zidentyfikowanej luki lub niejawnego wymagania zmieniającego treść.** Tej weryfikacji nie należy utożsamiać z formalizacją twierdzeń w Lean.

## Niezależna weryfikacja czterech przykładów

1. **Dunford bez Pettisa:** dla `f(n)=2^n e_n` i mas `2^{-n}` skalaryzacje przez `a∈ell^1` mają całkowalną wartość bezwzględną `sum |a_n|`, a całka Dunforda `(1,1,...)∈ell^infty` nie należy do `J_{c_0}(c_0)`. Całka normy jest nieskończona.
2. **Pettis bez Bochnera:** dla `f(t)=e_t∈ell^2([0,1])` każdy funkcjonał ma co najwyżej przeliczalny nośnik współrzędnych, więc wszystkie całki skalarne znikają, mimo że obraz funkcji poza zbiorem miary zero nie może leżeć w ośrodkowej podprzestrzeni. Norma f jest stale równa 1.
3. **Gelfand bez normowej addytywności:** w `ell^infty=(ell^1)'` miary na ogonach mają normę 1, lecz skalaryzacje przez `ell^1` zbiegają do zera; przykład dowodzi dokładnie braku normowej zbieżności.
4. **Brak RNP dla `C([0,1])`:** miara `m(A)(t)=mu(A∩[0,t])` ma `||m(A)||=|m|(A)=mu(A)`. Gdyby istniała pochodna Bochnera f, zgodność z ewaluacjami w przeliczalnym zbiorze argumentów wymiernych wymuszałaby funkcję skokową względem t, sprzeczną z ciągłością `f(s)∈C([0,1])` dla prawie wszystkich s.

**4/4 przykłady poprawne i właściwie odróżniają pojęcia całki.**

## Kontrola techniczna, odsyłacze i terminologia

Bezpośredni odczyt źródła: **594 wiersze**, 23 etykiety i 23 różne nazwy; w połączonym zbiorze etykiet modułów 15A, 15B i rozdziału 16 brak duplikatów. Wszystkie cztery odwołania występujące w źródle (w tym część w komentarzach) mają istniejące cele. Liczba początków i końców środowisk jest równa odpowiednio: 9 `twierdzenie`, 2 `stwierdzenie`, 6 `definicja`, 4 `przyklad`, 3 `uwaga`, 11 `proof`. Sześć par `\\[` i `\\]` do wzorów wyświetlonych jest zgodnych. Źródło nie zawiera rysunków TikZ. W tekście poprawnie rozróżniono `X'` (przestrzeń sprzężona) i `X''` (podwójnie sprzężona), stosowano `\\chi_A` dla funkcji charakterystycznych. Nie znaleziono błędnego rzeczownika „dual” ani użycia niedozwolonego zastępnika funkcji charakterystycznej.

Regresja `test_functional_analysis_ch15b.py` zawiera **6** testów, w tym arytmetyczne obliczenie obu współrzędnych w skończonej przestrzeni produktowej, wariację dla wszystkich podzbiorów czterech atomów, zabezpieczenie sformułowań twierdzeń Dunforda i Gelfanda oraz kontrakty LaTeX. Są to regresje skończonego modelu, nie matematyczna weryfikacja ogólnego twierdzenia Fubiniego. Raport 15B/04 dokumentuje wizualną kontrolę faktycznego 110-stronicowego PDF aktualnego źródła na stronach 98–100, włącznie z wyświetleniem samodzielnych twierdzeń; znany pojedynczy `Underfull \\hbox` dotyczy rozdziału 16.

## Decyzja

**15B/05: PIERWSZY CZYSTY AUDYT (1/2)** na niezmienionych blobach źródła i testów po korektach z 15B/04. Nie przechodzić do rozdziału 16. Następna jednostka: niezależny audyt **15B/06** na dokładnie tych samych blobach, następnie potwierdzenie nowego dedykowanego CI i formalna decyzja o statusie STABILNY. W przypadku konieczności jakiejkolwiek korekty matemat./redakcyjnej resetować licznik zamiast uznawać etap za drugi czysty.
