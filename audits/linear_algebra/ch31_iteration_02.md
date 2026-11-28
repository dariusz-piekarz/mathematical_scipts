# Algebra liniowa — rozdział 31, audyt II (pierwszy czysty)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/31-grupy-pin-spin-i-spinory.tex`, blob `6c1d09b9eaf4083c9ebaa361dbf46fc350eae147`; bez modyfikacji.

## Audyt algebry i reprezentacji
1. **Pin i Spin.** Z definicji `u²=−1` dla jednostkowego u dostajemy `u⁻¹=−u`, a polaryzacja prowadzi do wzoru odbicia `r_u(v)=−uvu⁻¹`. Rozróżniono skręcone sprzężenie Pin od parzystego sprzężenia Spin.
2. **Twierdzenie o dwukrotnym nakryciu.** Surjektywność oparto na rozkładzie izometrii na odbicia, a `ker ρ={±1}` na bazie Clifforda LA-30 oraz normie rewersyjnej `s\tilde s=1`. Lokalny wybór rotora daje dwa gładkie płaty; dla `O(n)` dopisano lokalne uzasadnienie twierdzeniem o funkcji uwikłanej.
3. **Dwa i trzy wymiary.** Sprawdzono połówkowe kąty `Spin(2)→SO(2)`, kwaterniony jednostkowe `Spin(3)≅SU(2)`, znaki iloczynu `IJ=K`, brak pomieszania działania `ρ` i działania na spinorach.
4. **Klasyfikacja zespolona.** Wymiar po kompleksyfikacji wynosi `2^n`. Obrazy generatorów `F_j=e_j⊗σ₃`, `F_{n+1}=iσ₁`, `F_{n+2}=iσ₂` spełniają relacje Clifforda; uzyskany homomorfizm jest surjektywny, a równe wymiary dają izomorfizm. Rozróżniono dwa moduły dla nieparzystego n i jeden dla parzystego.
5. **Półspinory.** Operator `Γ=i^m c(e₁⋯e₂ₘ)` kwadratuje się do I, antykomutuje z działaniem wektorów i komutuje z `Spin(2m)`. Dowód nieredukowalności wykorzystuje `W⊕c(e₁)W` i nie wprowadza ukrytego założenia.
6. **Sfera Blocha.** Wzory na `b(ψ)`, rzut `ψψ*`, identyfikację `CP¹≅S²` i ekwiwariantność względem `SU(2)` sprawdzono na macierzach.

## Dodatkowa niezależna kontrola obliczeniowa
- Lokalny skrypt `/mnt/data/la31_review/independent_spin_audit.py`: w kompleksowym modelu `Cl₄` wszystkie 16 uporządkowanych monomów macierzowych są niezależne (rząd 16), `Γ²=I`, dwa rzuty chiralne mają rzędy po 2, a `Γ` komutuje z wszystkimi produktami dwóch generatorów. **PASS**.
- W modelu `Cl₃^ℂ` obie możliwości działania generatorów `±iσ_j` mają identyczne działanie na części parzystej i przeciwne wartości znormalizowanego elementu objętości. **PASS**.
- Niezależny dokładny test iloczynu Clifforda sprawdził odbicia bazowe Pin dla n=2,3,4 (łącznie 29 par). **PASS**.
- CI: [workflow 44956522593](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44956522593), **SUCCESS** z testami reprezentacji, pełną kompilacją książki, bez nierozwiązanych odsyłaczy i ostrzeżeń układu w końcowym logu.

## PDF i rysunki
Pobrano bieżący artefakt `linear-algebra-current-chapter` o identyfikatorze `14727736243`. Samodzielny PDF ma **14 stron A4**. Wszystkie strony zawierają tekst; kontrola PyMuPDF wykazała **0 bloków tekstu poza stroną**. Wyrenderowano 14 stron i obejrzano ich montaż oraz powiększenia stron 4, 9, 11 i 14. Rysunki nakrycia Spin(2), sfery Blocha, torusa i zmian ramek są czytelne, bez kolizji podpisów z diagramami.

## Decyzja
**Audyt II czysty**, bez poprawki źródła. Do formalnej stabilizacji potrzebny jest jeszcze drugi niezależny czysty audyt III tej samej wersji źródła.
