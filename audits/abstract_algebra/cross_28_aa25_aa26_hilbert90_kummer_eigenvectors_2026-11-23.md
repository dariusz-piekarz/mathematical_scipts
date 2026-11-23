# AA-X28 — 90. twierdzenie Hilberta i odwrotne twierdzenie Kummera (AA-25 × AA-26)

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6. **HEAD przed audytem:** 44d3472c97c4b874e9fc820e7aa4877f5facceb2.
**Commit modułu regresyjnego:** 2d5e6cf22c7e88e994113cda376969d2cc66c18e.
**Commit integracji CI:** bc27417de3da58f3383e8abb82a12afed7dcd7f1.

## Podstawa i zakres kontroli

Zweryfikowano rzeczywisty HEAD i nieucięte drzewo GitHub: AA-01–AA-50 istnieją, AA-51 nie istnieje. Zapoznano się z AGENTS.md, źródłami obu rozdziałów oraz raportami AA-X02 i AA-X26–X27. AA-X27 jest zamknięty. Niniejszy audyt nie ponawia testów Artina–Schreiera ani klasyfikacji rozszerzeń przez klasy Kummera z poprzednich audytów. Nowym przedmiotem jest bezpośredni most dowodowy AA-25 → AA-26, a także wzory na normę i ślad generatora.

* AA-25: chapters/pl/abstract_algebra/25-twierdzenie-hilberta-90-i-rownania-normowe.tex, blob 2524f56e0a4802d28c441ff932ba5399a10eb61c, 337 wierszy; istotne etykiety: aa:lem:dedekind-independent, aa:tw:hilbert90-multiplicative.
* AA-26: chapters/pl/abstract_algebra/26-rozszerzenia-cykliczne-i-teoria-kummera.tex, blob 5bee95fdfedeaaf4fc697dce636e5d82afcd249b, 507 wierszy; istotne etykiety: aa:tw:kummer-radical-cyclic, aa:tw:kummer-converse.
* Oba rozdziały znajdują się w kompilowanym tomie books/pl/abstract_algebra.tex. Zatwierdzone źródła i ich odsyłacze nie zostały zmienione.

## Twierdzenie przekrojowe i dowód

**Twierdzenie.** Niech L/K będzie skończonym cyklicznym rozszerzeniem Galois stopnia n≥2, a σ generatorem grupy Gal(L/K). Załóżmy, że K zawiera pierwotny n-ty pierwiastek z jedynki ζ. Wówczas istnieje α∈L× takie, że
\[
\sigma(\alpha)=\zeta\alpha,\qquad \alpha^n\in K^\times,\qquad L=K(\alpha).
\]

**Dowód.** Ponieważ ζ należy do K, wszystkie automorfizmy grupy Gal(L/K) ją ustalają. Zatem dla c=ζ⁻¹ mamy N_{L/K}(c)=c^n=ζ⁻ⁿ=1. Multiplikatywna postać 90. twierdzenia Hilberta (AA-25) daje α∈L× spełniający c=α/σ(α), czyli σ(α)=ζα. Wtedy σ(αⁿ)=ζⁿαⁿ=αⁿ. Ponieważ σ generuje całą grupę Galois, αⁿ należy do ciała elementów stałych K.

Indukcyjnie σʲ(α)=ζʲα dla 0≤j<n. Są to parami różne elementy, ponieważ ζ ma dokładnie rząd n i α≠0. Wszystkie są pierwiastkami wielomianu minimalnego α nad K, więc [K(α):K]≥n. Zawieranie K(α)⊆L daje nierówność przeciwną. Zatem [K(α):K]=n i L=K(α). Koniec dowodu.

**Ocena źródła.** AA-26:165–217 uzyskuje ten sam wynik odmiennie, przez sumę P(x)=Σ_{j=0}^{n−1}ζ⁻ʲσʲ(x). Jej niezerowość jest poprawnie uzasadniona niezależnością automorfizmów z AA-25. Nie ma koniecznej poprawki. Powyższy dowód jest opcjonalną alternatywą.

## Norma i ślad w bazie Kummera

Niech a=αⁿ∈K×. Stosując wzory AA-25 na normę i ślad w rozszerzeniu Galois, dostajemy
\[
N_{L/K}(\alpha)=\prod_{j=0}^{n-1}\zeta^j\alpha
=\alpha^n\zeta^{n(n-1)/2}=(-1)^{n-1}a.
\]
Dla n nieparzystego ζ^{n(n−1)/2}=1, bo wykładnik jest wielokrotnością n. Dla n parzystego ζ^{n/2}=−1, a n−1 jest nieparzyste. Obecność pierwotnego n-tego pierwiastka z jedynki gwarantuje, że charakterystyka K nie dzieli n.

Dla 1≤j<n zachodzi ζʲ≠1, zatem
\[
\operatorname{Tr}_{L/K}(\alpha^j)
=\alpha^j\sum_{k=0}^{n-1}\zeta^{jk}=0.
\]
Również Tr_{L/K}(1)=n·1_K. Ponieważ stopień α wynosi n, ciąg 1,α,...,α^{n−1} jest bazą L nad K.

## Kontrola hipotezy pierwotności

Jeżeli λ∈K ma rząd d dzielący n (ale niekoniecznie równy n), to N_{L/K}(λ⁻¹)=1 i 90. twierdzenie Hilberta daje β∈L× takie, że σ(β)=λβ. Liczba różnych sprzężeń σʲ(β)=λʲβ wynosi dokładnie d; ze skończonej galoisowskości wynika [K(β):K]=d, a βᵈ∈K. Jeżeli d<n, otrzymane podrozszerzenie jest właściwe. Sama norma 1 nie gwarantuje generatora stopnia n bez pierwotności λ. W teście wykorzystano n=4 i λ=−1 o rzędzie d=2.

## Regresje, LaTeX i status

Nowy trwały moduł: tools/tests/test_abstract_algebra_cross_aa25_26.py. Zawiera sześć funkcji testowych: działanie Frobeniusa, obliczenie norm i obrazów b/σ(b), rozmiary podprzestrzeni własnych, wzory śladu i normy, test przypadku niepierwotnej wartości własnej oraz inwentaryzację rozdziałów i odsyłaczy.

Modele: F₅[t]/(t²−2), F₇[t]/(t³−2), F₅[t]/(t⁴−2). Nierozkładalność sprawdzana w SymPy, reszta arytmetyki dokładna na współczynnikach modulo liczba pierwsza. Pięć testów arytmetycznych rzeczywiście przeszło w odizolowanym środowisku; szósty, kontrolujący 50 plików i etykiety, został osobno wykonany w symulacji struktury repozytorium i również przeszedł. Jest to wynik lokalny, nie wynik GitHub Actions. Testy nie zastępują ogólnych dowodów matematycznych ani formalizacji Lean.

Nowy moduł został podłączony do .github/workflows/abstract-algebra-chapter.yml jako wydzielony krok AA-X28 oraz dodany do wyzwalaczy. Na tym etapie **nie deklaruje się zielonego CI**. Do zamknięcia wymagane są rzeczywisty ukończony zielony przebieg workflow, w logu 6/6 testów AA-X28, kompilacja AA-01–AA-50 i analiza logu odsyłaczy. Oddzielna wizualna inspekcja PDF nie została wykonana.

**Werdykt: matematyka sprawdzonego interfejsu bez koniecznej poprawki; AA-X28 W STABILIZACJI CI.** Wszystkie zatwierdzone rozdziały pozostają bez zmian. Żaden nowy rozdział nie został otwarty.

**Propozycja opcjonalna (bez automatycznego dopisywania):** po twierdzeniu aa:tw:kummer-converse w AA-26 dodać odsyłacz do multiplikatywnej postaci 90. twierdzenia Hilberta i powyższy alternatywny krótki dowód. Wymaga osobnej zgody według AGENTS.md.

**Dalszy krok:** potwierdzenie dokładnego przebiegu CI i stabilizacja AA-X28, dopiero następnie wybór nowego przekrojowego zakresu AA-X29.
