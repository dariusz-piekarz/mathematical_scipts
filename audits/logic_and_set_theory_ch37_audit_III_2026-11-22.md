# Logika matematyczna i teoria mnogości — audyt III rozdziału 37

**Data:** 22 listopada 2026 r.  
**Źródło:** chapters/pl/logic_and_set_theory/37-duze-liczby-kardynalne-nieosiagalnosc-i-mierzalnosc.tex.  
**Blob:** 3e0ae67b1b6a9abb5a4ff93691a2947d207647c4 — bez zmiany od audytu I.  
**Wynik merytoryczny:** czysty, bez żadnej koniecznej zmiany dowodów lub redakcji. Jest to kandydat na **drugi czysty audyt (2/2)**, pod warunkiem potwierdzenia nowego CI.

## 1. Audyt w odwrotnej kolejności: od normalności do aksjomatów

**Miara normalna.** Sprawdzono, że zbiór W={X⊆κ:κ∈j(X)} jest zewnętrznie zbiorem dzięki definowalności j z parametru U. Pusty zbiór nie leży w W, podczas gdy κ należy do W. Ultrafiltrowość jest konsekwencją j(κ\X)=j(κ)\j(X) i tego, że κ<j(κ). Dla μ<κ mamy j(μ)=μ, co pozwala zachować przecięcia μ-wyrazowych rodzin. W normalności kluczowe jest zastosowanie j(f) do argumentu κ i odczytanie wartości ξ<κ jako j(ξ)=ξ; stąd konkretne włókno f^-1({ξ}) należy do W. Nie mylimy normalności z samą κ-zupełnością.

**Równoważność diagonalna.** W kierunku od normalności, na dopełnieniu przecięcia diagonalnego definiuje się regresywną funkcję przyjmującą najmniejszy indeks naruszenia, a jej stałe włókno przeczy członkostwu odpowiedniego A_ξ w U. W kierunku przeciwnym, gdyby żadne włókno regresywnej f nie było duże, dopełnienia wszystkich włókien tworzyłyby rodzinę U-dużą; jej przecięcie diagonalne byłoby duże, ale rozłączne z dziedziną f poza zerem. Punkt 0 nie powoduje problemu, ponieważ singleton nie należy do niegłównego ultrafiltru.

**Punkt krytyczny zanurzenia.** Nie zakładamy normalności miary wyjściowej. Nie utożsamiamy klasy funkcji identycznościowej z porządkowym κ dla miary nienormalnej. Wystarcza oszacowanie α<[id]<j(κ) dla wszystkich α<κ. Przy dowodzie j(α)=α każdą funkcję o wartościach mniejszych od α redukuje się do stałej modulo U, używając rozkładu na mniej niż κ włókien.

**Łoś i ufundowanie.** Klauzule atomowe wynikają z definicji relacji, negacja z decyzji ultrafiltru, koniunkcja z filtrowości. Egzystencja korzysta z wyboru po zbiorze D⊆κ w metateorii ZFC. Obecność AC nie oznacza w żadnym kroku wyboru dla rodziny indeksowanej klasą właściwą. Brak nieskończonego ciągu malejącego wynika z przecięcia wszystkich A_n dla n<ω (ponieważ ω<κ). Zbiorolokalność relacji zapewnia reprezentacja poprzedników [f] przez funkcje o wartościach ze zbioru suma wartości f oraz zbioru pustego. Dlatego klasa nadaje się do tranzytywnego kolapsu.

**Nieosiągalność.** W kroku granicznym hierarchii V_α korzysta się jednocześnie z małości liczby etapów α<λ<κ i regularności κ. W kroku następnika korzysta się z 2^μ<κ. Schemat zastępowania w V_κ wymaga ograniczenia rang wszystkich wartości na dziedzinie mocy <κ. Te założenia są obecne i nie są ukryte.

## 2. Dodatkowa niezależna regresja Łosia

Dodano kolejną metodę testową do tools/tests/test_logic_and_set_theory_ch37.py: oblicza cztery niezależne formuły z negacją, koniunkcją, kwantyfikatorem egzystencjalnym i ogólnym na trójelementowej strukturze relacyjnej, porównując bezpośrednią ewaluację po każdym z trzech głównych ultrafiltrów z ewaluacją przez zbiór indeksów. Liczba sprawdzeń wynosi **8748**. Zmiana dotyczy wyłącznie testów, bez edytowania rozdziału; commit 6a92037f5ea5415ee2c3cd69653e59885ebb9bc6. Skończona struktura nie stanowi modelu ZFC i test nie jest dowodem twierdzenia Łosia w pełnej ogólności.

## 3. Redakcja, skład i testy

Źródło nadal ma **775 wierszy, 26 etykiet, 18 odsyłaczy, 7 definicji, 4 lematy, 7 twierdzeń, 1 wniosek, 5 uwag, 1 przykład i 12 dowodów**; środowiska poprawnie sparowane. W audycie II pełny PDF miał 326 stron, a rozdział 37 strony PDF 321–326. Nie stwierdzono błędów składu w montażu sześciu stron. Punkt odniesienia: [CI 45066748548 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45066748548).

Zapis raportu i rozbudowany test uruchamiają odrębne CI. Wynik tych przebiegów należy potwierdzić przed formalnym zaliczeniem audytu III jako 2/2.

## 4. Werdykt

Brak koniecznej poprawki źródła, stąd audyt III jest **czysty matematycznie**. Do końcowego statusu stabilności pozostaje dodatkowy audyt IV, ale dopiero po potwierdzeniu obu przebiegów CI związanych z audytami II i III. Testy Python i skład LaTeX nie są weryfikacją dowodów w Lean.
