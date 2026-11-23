# AA-46 — audyt II: niezależna kontrola założeń, modeli i dowodu Airy'ego

**Data:** 23 listopada 2026 r. **Werdykt: NIE STABILNY — kontrola zdalnego CI i PDF pozostaje otwarta.**
**Źródło:** chapters/pl/abstract_algebra/46-rozszerzenia-picarda-vessiota-i-rozniczkowa-teoria-galois.tex.

## 1. Niezależny przegląd matematyczny

1. **Macierze fundamentalne.** Jeżeli DU=AU oraz U odwracalna, pochodna odwrotności wynosi D(U^{-1})=-U^{-1}A, więc D(U^{-1}y)=0 dla każdego rozwiązania Dy=Ay. Wszystkie rozwiązania są postaci Uc, c w C_L^n. Dwie macierze fundamentalne różnią się prawym czynnikiem z GL_n(C_L), nie lewym ani czynnikiem ze zmiennymi współczynnikami.
2. **Równanie Abela.** Jacobi: D(det U)=det U tr(U^{-1}DU)=tr(A)det U. Dla tr A=0 wyznacznik jest niezerową stałą. Równanie Airy'ego należy właśnie do tej klasy.
3. **Definicja PV.** Pierścień R=K[U_ij,(det U)^{-1}] jest różniczkowo prosty, a pole stałych C algebraicznie domknięte. Sformułowanie nie utożsamia prostoty różniczkowej z prostotą pierścienia w zwykłym sensie. Istnienie i jednoznaczność oraz dziedzinowość i brak nowych stałych stanowią jawnie cytowany wynik, nie ukryty w niepełnym dowodzie konstrukcji ilorazowej.
4. **Reprezentacja automorfizmów.** Z D(σU)=AσU wynika σU=UM_σ z M_σ w GL_n(C) (warunek C_E=C jest potrzebny). Przy zwykłej konwencji składania σ∘τ macierz wynosi M_σ M_τ. Jeśli M_σ=I, automorfizm ustala generatory E, jest więc identycznością. Zamiana U na UQ prowadzi do sprzężenia Q^{-1}M_σ Q.
5. **Co nie wynika elementarnie.** Z różnowartościowego odwzorowania G→GL_n(C) nie wynika zamkniętość obrazu Zariskiego, odpowiedniość Galois, wzór dim G=trdeg_K E, ani kryterium liouvillowskości. Wszystkie cztery wyniki zostały oddzielone, powołano literaturę van der Put–Singer.
6. **Grupa G_m.** Dla t=e^x nie istnieje a_j w C(x)^× z Da_j/a_j=-j (j≠0). W niezerowym ideale różniczkowym Laurentów wybieramy p o minimalnej liczbie niezerowych monomianów, mnożymy przez odwrotność jednego z nich, aby uzyskać wyraz stały 1. Dp ma mniej wyrazów i musi zniknąć. Pozostałe niezerowe potęgi niemożliwe, więc 1 należy do ideału. Sformułowanie zostało poprawione redakcyjnie, aby explicite mówić o odwrotności monomianu.
7. **Grupa G_a.** Dla t=log x mamy Dt=1/x. Macierz U=[[1,t],[0,1/x]] ma wyznacznik 1/x i spełnia DU=AU. R=K[t] jest różniczkowo proste: w ideale wybieramy wielomian unormowany najmniejszego stopnia; jego pochodna ma mniejszy stopień, zatem znika; dla stopnia m>=1 równość Da_{m-1}=-m/x jest niemożliwa dla funkcji wymiernej ze względu na residuum. Wszystkie przesunięcia t↦t+c realizują automorfizmy.
8. **Grupa skończona μ_m.** T^m−x jest nierozkładalny nad C(x); z różniczkowania t^m=x wynika Dt=t/(mx). W rozszerzeniu algebraicznym nie ma nowych stałych, bo C algebraicznie domknięte. Dowolny automorfizm t↦ζt z ζ^m=1 komutuje z D; grupa ma m elementów i wymiar zero. Nie wolno mylić tej grupy z pełną G_m.
9. **Równanie harmoniczne.** U=[[t,t^{-1}],[it,-it^{-1}]], Dt=it, det U=-2i. σ(t)=ct wymusza σ(t^{-1})=c^{-1}t^{-1}. Grupa w tej bazie to diagonalne macierze o wyznaczniku 1; niezależne skalowanie obu kolumn nie jest dopuszczalne.
10. **Liouvillowskość.** Rozszerzenie elementarne ma pochodną logarytmu w kroku pierwotnym; w rozszerzeniu liouvillowskim dopuszcza się dowolne Dt=a. Funkcja F'=e^{-x²} daje przykład nieelementarny, lecz liouvillowski i spełnia F''+2xF'=0. Jeżeli F' jest już całkowalne w bieżącym piętrze, nie dodajemy nowej zmiennej; w przeciwnym przypadku lemma AA-43 zachowuje stałe.
11. **Riccati/Airy.** Algebraiczna funkcja r spełniająca r'+r²=x nie ma rozgałęzień nad skończonymi punktami: dla gałęzi ograniczonej używamy lokalnego rozwiązania analitycznego r'=x-r², a dla biegunów u=1/r i u'=1-xu². Nierozgałęzione skończone przykrycie C ma jeden arkusz, więc r jest wymierna. Dla wymiernej r zachowanie w nieskończoności wyklucza zarówno biegun części wielomianowej stopnia d>=1 (r² ma rząd 2d), jak i regularność w nieskończoności (lewa strona regularna, x ma biegun). Zatem nie ma algebraicznych rozwiązań Riccatiego. Przejście do braku rozwiązań liouvillowskich wykorzystuje klasyczne, cytowane kryterium Galois, nie sam rachunek stopni.
12. **Grupa Airy'ego.** Wrońskian jest stały, więc G⊆SL₂(C). Brak niezerowego rozwiązania liouvillowskiego uniemożliwia rozwiązalność G°; każda właściwa spójna algebraiczna podgrupa SL₂(C) ma rozwiązalną algebrę Liego wymiaru ≤2, więc G°=SL₂(C), a zatem G=SL₂(C). To rozumowanie nie jest twierdzeniem o zwykłych automorfizmach ciała K bez derywacji.

## 2. Testy niezależne i poprawki

Przygotowano dwa niepokrywające się implementacyjnie zestawy: 10 testów macierzy i wzorów symbolicznych (SymPy) oraz 8 testów ścisłej arytmetyki wymiernej i równań macierzowych bez SymPy. Zbadano przypadki brzegowe m=2, ujemne współczynniki w macierzach, odwracalność i różne wartości parametrów x. Usunięto tautologiczną asercję testującą rzekomą przeszkodę residuów; zastąpiono ją obliczeniami dokładnych pochodnych potęg ujemnych.

## 3. Kryteria niezakończone

Weryfikacja w GitHub Actions na najnowszych blobach rozdziału i obu zestawów testów pozostaje w toku. Trzeba uzyskać zielony pełny CI, końcowy artefakt PDF, przejrzeć log kompilacji i każdą stronę nowego rozdziału. Bez spełnienia tych warunków nie nadajemy statusu STABILNY i nie rozpoczynamy warunkowego AA-47.
