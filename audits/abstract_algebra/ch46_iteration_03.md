# AA-46 — audyt III: końcowa stabilizacja matematyczna, techniczna i PDF

**Data:** 23 listopada 2026 r.
**Werdykt: AA-46 STABILNY.**
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Rozdział:** chapters/pl/abstract_algebra/46-rozszerzenia-picarda-vessiota-i-rozniczkowa-teoria-galois.tex.
**Zweryfikowany blob SHA rozdziału:** a0175b3d9b2f4c2f3b5f1d6ae1606bee70331186.
**Weryfikowane zestawy testów:** test_abstract_algebra_ch46.py (10 testów, SymPy), test_abstract_algebra_ch46_independent.py (8 testów, fractions.Fraction bez SymPy).

## 1. Trzy audyty i rzeczywiście usunięte problemy

Raporty ch46_iteration_01.md oraz ch46_iteration_02.md dokumentują konstrukcję rozdziału i niezależny przegląd definicji, dowodów, przypadków brzegowych oraz bibliograficznych podstaw głębszych twierdzeń.

**Poprawka matematyczna — nierozkładalność T^m−x dla złożonego m.**
W pierwszym opracowaniu przykład μ_m sugerował, że z faktu, iż x nie jest m-tą potęgą funkcji wymiernej, wynika nierozkładalność T^m−x. Nie jest to poprawne ogólne rozumowanie dla złożonego m. Zastąpiono je pełnym argumentem z kryterium Eisensteina w C[x][T] względem pierwszego elementu x: wszystkie współczynniki poza wiodącym są podzielne przez x, wiodący 1 nie jest, a wyraz wolny −x nie jest podzielny przez x². To dowodzi nierozkładalności dla każdego m≥2. **Commit:** 676f76a8dd3e44a5a07fc06e59b93c88f3264fe0.

**Poprawka składu — zakładki PDF.**
Pierwszy pełny build zgłaszał trzy ostrzeżenia hyperref o niedozwolonych znacznikach matematycznych z nagłówka sekcji „Równanie Airy'ego: grupa SL₂”. Nagłówek zamieniono na poprawny językowo, pozbawiony składni matematycznej: „Równanie Airy'ego i grupa specjalna liniowa”. **Commit:** 961898b12d2a71da76fae27cfe5a9d51170db4d0. Nowsze kompilacje nie mają ostrzeżeń.

**Poprawka dowodu prostoty R=K[t,t^{-1}].**
Doprecyzowano, że w elemencie o minimalnej liczbie niezerowych monomianów współczynnik stały normalizuje się przez pomnożenie przez *odwrotność* odwracalnego monomianu, nie przez sam monomian. **Commit:** 343b4afbb18a3538037b280de2f9089cd046f576.

**Poprawka testów niezależnych.**
Tautologiczną asercję o pochodnej wyrazu z biegunem zastąpiono rzeczywistymi obliczeniami dokładnych pochodnych potęg ujemnych z arytmetyką wymierną, bez SymPy. **Commit:** 500a2769e526d2c88ce0d4ef518bc56b2cbbccbc.

## 2. Weryfikacja matematyczna

Przeanalizowano wszystkie 5 bloków dowodowych i 6 przykładów rozdziału (własne rozumowania oddzielono od wyników klasycznych):
1. D(U^{-1}y)=0 przy DU=AU, stąd pełny opis przestrzeni rozwiązań przez stałe oraz prawostronna zmiana macierzy fundamentalnej U→UQ, Q∈GL_n(C). Równanie Abela D(det U)=tr(A)det U dowiedziono z formuły Jacobiego.
2. Wprowadzenie pierścieni różniczkowo prostych oraz definicja PV wymagają algebraicznej domkniętości ciała stałych. Istnienie i jednoznaczność PV, brak nowych stałych, algebraiczność grupy, wymiar grupy i odpowiedniość Galois **są jawnie cytowane jako klasyczne wyniki** van der Puta i Singera, nie jako samodzielnie dowiedzione.
3. Udowodniono samodzielnie, że σ(U)=UM_σ, M_σ∈GL_n(C), oraz że σ↦M_σ jest różnowartościowym homomorfizmem; sprawdzono prawo składania i sprzężenie przy zmianie bazy.
4. Grupa multiplikatywna G_m dla t=e^x: dowód prostoty różniczkowej Laurentów przez wybór elementu ideału o minimalnej liczbie wyrazów; wykluczenie pochodnej logarytmicznej funkcji wymiernej równej niezerowej stałej.
5. Grupa addytywna G_a dla t=log x: dokładna macierz fundamentalna układu drugiego rzędu, minimalny stopień wielomianu w prostocie różniczkowej i przeszkoda reszty 1/x.
6. Grupa skończona μ_m: poprawny dowód przez Eisensteina, stopień rozszerzenia m, przedłużona derywacja Dt=t/(mx), brak nowych stałych i grupa automorfizmów t↦ζt, ζ^m=1.
7. Równanie y''+y=0: t=e^{ix}, t^{-1}=e^{-ix}, wyznacznik U=-2i, działanie diagonalne diag(c,c^{-1}); nie można niezależnie skalować dwóch rozwiązań zależnych relacją tt^{-1}=1.
8. Rozszerzenia liouvillowskie dopuszczają dowolne funkcje pierwotne, w przeciwieństwie do rozszerzeń elementarnych; przykład nieelementarnej całki Gaussa w wieży liouvillowskiej jest poprawny i posiada równanie F''+2xF'=0.
9. Dla Riccatiego r'+r²=x wykluczono algebraiczne rozwiązania za pomocą lokalnych rozwinięć Puiseux, nierozgałęzionych skończonych przykryć C i analizy przy nieskończoności. Odwołanie do klasycznego twierdzenia o przykryciach jest jawnie wskazane.
10. Dla równania Airy'ego Wrońskian jest stały i G⊆SL₂(C); brak algebraicznego Riccatiego, w połączeniu z cytowanym kryterium liouvillowskim Picarda–Vessiota i twierdzeniem Liego–Kołczyna, wyklucza rozwiązalność G°. Każda właściwa spójna algebraiczna podgrupa SL₂(C) jest rozwiązalna, zatem G=SL₂(C). Nie utożsamiono elementarnego rachunku wymiernego z pełnym dowodem cytowanego kryterium.

## 3. Ostateczne rzeczywiste GitHub Actions

**Przebieg końcowy na poprawionym źródle:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157760575

**Head SHA:** 676f76a8dd3e44a5a07fc06e59b93c88f3264fe0.
**Status:** completed / success, **83/83 zakończonych sukcesem kroków**.

W rzeczywistych krokach:
- AA-46 matematyczne regresje SymPy: **10/10 PASS**;
- AA-46 niezależne modele macierzowe Fraction: **8/8 PASS**;
- AA-GLOBAL źródła: **PASS**, dokładnie **46 rozdziałów**, **939** etykiet unikatowych, **0** duplikatów, **451** wystąpień odsyłaczy, **285** różnych celów i **0** nierozwiązanych; łącznie **427** dowodów i **293** przykłady;
- historia 11 raportów przekrojowych AA-01–AA-42 nienaruszona; AA-43–AA-46 mają osobne cykle audytów;
- kompilacja całej książki latexmk: success;
- weryfikacja PDF i odsyłaczy: success;
- artefakt archiwalny: success.

## 4. Ostateczny PDF i log

**Artefakt GitHub Actions:** abstract-algebra-aa01-aa46, ID **14808678893**.
- abstract_algebra.pdf: **297 stron**, **2 173 427 B**; SHA-256 **37f2c8f0e032d455347a5d2a0816bbd0636c5c3d7799c2fce4e331c131f31495**.
- abstract_algebra.log: **45 907 B**; SHA-256 **054d50c4502d501114343efa6903d6ddb40db43a0fa03aa83ea4c7b4c784cd39**.
- Końcowy log: **0** LaTeX Error, **0** LaTeX Warning, **0** hyperref Warning, **0** overfull/underfull hbox/vbox, **0** undefined references i **0** żądań ponownego przeliczenia odsyłaczy.
- AA-46 zajmuje dokładnie **7 stron PDF, 291–297** (drukowane 281–287). Każdą stronę wyrenderowano i obejrzano, w tym poprawioną sekcję Airy'ego i rozwinięty argument Eisensteina. Nie stwierdzono nachodzących tekstów, obcięć ani błędów składu.
- W całej książce sprawdzono pozycje **153 141** słów; **0** elementów poza granicami stron.
- Z poprzedniej stabilnej wersji AA-01–AA-45 **287/289 stron zachowało identyczną warstwę tekstową**: strona tytułowa zmieniła status, a spis treści zwiększył się o jedną stronę. Treść 45 poprzednich rozdziałów pozostała bez zmian, poza przesunięciem indeksów PDF o jedną stronę.

## 5. Decyzja

**AA-46 STABILNY.** Zamknięto dokładne sformułowania i zakres wszystkich twierdzeń, własne dowody, cytowania głębokich wyników, dwa niezależne zestawy regresji, integrację katalogu, końcowe CI i wizualny audyt kompletnego rozdziału.

**AA-47 pozostaje WARUNKOWY — nie uruchamiać rozwoju bez odrębnej decyzji o zakresie algorytmów Rischa i Kovacica.** Opracowanie AA-43–AA-46 i ich audyty są zakończone.
