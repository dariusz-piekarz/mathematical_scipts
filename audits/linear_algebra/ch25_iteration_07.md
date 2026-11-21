# Algebra liniowa — rozdział 25, audyt VII (drugi czysty; stabilizacja)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/25-sterowalnosc-obserwowalnosc-i-stabilizowalnosc.tex`.  
**Zatwierdzony blob:** `6b57fc1b64ef560b98e17f89322c688160376ccf`.  
**Historia:** audyt I – integracja; II – poprawka regresji; III – czysty matematycznie przed kontrolą składu; IV – korekta Underfull; V – doprecyzowanie kwantyfikatora; VI i VII – **dwie kolejne czyste kontrole końcowego bloba**.

## Samodzielna kontrola założeń i przejść dowodowych

1. **Wymiary i obiekty.** Przyjęto jawnie `n,m,p>=1`, `A∈M_n(C)`, `B∈M_(n×m)(C)`, `C∈M_(p×n)(C)`. Zależności obrazu i jądra są wykorzystane z poprawnymi wymiarami. Wersja rzeczywista sprawdza zespolone wartości własne w kryterium PBH.
2. **Kalman i Cayley–Hamilton.** W `lem:lin25-invariant` wszystkie potęgi A^kB redukują się do k<n, a minimalność przestrzeni osiągalnej jest jawnie dowiedziona. W `thm:lin25-kalman` wyprowadzenie trajektorii x_N uwzględnia kolejność sterowań i dowodzi przejścia od x do z w n krokach.
3. **Ciągły gramian.** Tożsamość `ker W_T=ker K*` jest dowiedziona obustronnie; nie pominięto przypadku wartości własnej 0 ani skończonego T. Jawna funkcja u(t) ma właściwy wymiar m i poprawny wykładnik e^(T-t)A*. Dodatniość W_T jest niezależna od T>0, nie jest postulowana.
4. **Obserwowalność i PBH.** O(C,A) opisuje dokładnie n pierwszych obserwacji; przestrzeń N=ker O jest największą A-niezmienniczą zawartą w ker C. Oba kierunki PBH sterowalności i obserwowalności są udowodnione bez ukrytego przypadku diagonalizowalności.
5. **Rozkład Kalmana.** U=R∩N, R=U⊕R0, N=U⊕N0, V=U⊕R0⊕N0⊕W. Wymienione bloki zerowe A, B, C wynikają z niezmienniczości R,N i własności obrazów/jąder. Pojęcia obserwowalności i osiągalności poszczególnych części interpretowane są przez podilorazy, nie przez fałszywą kanoniczność dopełnień.
6. **Stabilizowalność.** Lemat rezolwentowy konstruuje po kolei bazę wektorów dla różnych μ∈Ω i macierz F, nie odwołuje się do nieudowodnionego twierdzenia o dowolnym rozmieszczaniu biegunów. Każde nieosiągalne λ pozostaje wartością własną zamkniętej pętli. Stąd PBH z Re λ>=0 dla czasu ciągłego i |λ|>=1 dla czasu dyskretnego jest dokładnym kryterium.
7. **Wykrywalność i obserwator.** Sprzężenie pary (A*,C*) i wzór (A-LC)*=A*-C*L* dają kryteria PBH z prawidłowymi wartościami własnymi. Błąd obserwatora spełnia e'=(A-LC)e lub e_(k+1)=(A-LC)e_k. Kwantyfikator stabilności jest wypisany słownie dla każdej wartości własnej.
8. **Energia dyskretna.** `W_N^d=K_NK_N*`; przy W_N^d>0 formuła minimalnego sterowania jest udowodniona przez rzut ortogonalny na dopełnienie ker K_N. Otrzymano z definicji dokładny koszt d*(W_N^d)^-1d oraz jedyność minimalizatora.

## Testy oraz PDF

- 47 unikalnych etykiet, 30 odsyłaczy, 17 kompletnych dowodów. Terminologia zgodna z `AGENTS.md`; brak nieistniejących odsyłaczy, kolizji etykiet i zewnętrznych grafik.
- [GitHub Actions 44949428707](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44949428707): **SUCCESS** na dokładnym blobie końcowym, w tym wszystkie regresje LA-01–25, kontrola odsyłaczy, końcowy log LaTeX bez ostrzeżeń i eksport samodzielnego PDF.
- [GitHub Actions 44949449945](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44949449945): **SUCCESS** dla commita z raportem audytu V, bez zmian źródła.
- Regresja LA-25: wyczerpujące **64** pary (A,B) 2×2 nad F2 i **729** nad F3 (z NWD wielomianowych minorów PBH, także dla wartości własnych z rozszerzeń algebraicznych); ponadto **500** wymiernych sterowalnych przykładów 2×2 z jawnym sprzężeniem o wartościach własnych -1 i -2; przykłady graminów i dualności.
- Samodzielny PDF z artefaktu `linear-algebra-current-chapter` (run 44949428707) zawiera wyłącznie **rozdział 25, 15 stron**. PyMuPDF: wszystkie strony niepuste, **0 bloków tekstu poza obszarem strony**. Przeprowadzono wizualną inspekcję zestawienia renderów wszystkich 15 stron: bez uciętych wzorów, kolizji czy problemów z marginesami.

## Decyzja

**Audyt VII czysty**. To druga kolejna kontrola bez poprawek po ostatnim audycie V. Zewnętrzna walidacja i końcowy PDF są pomyślne. **Rozdział 25 stabilny po 7 audytach.** Tym samym rozdziały **01–25 algebry liniowej są stabilne**.

Następny rozdział w planie: **26 — uogólnione twierdzenia Riccatiego przy stabilizowalności i wykrywalności**, bez założenia stabilności otwartej pętli. Użytkownik zatwierdził też **grassmanniany (roboczo LA-29) i algebry Clifforda (roboczo LA-30)** do przeniesienia z DG-04 z zachowaniem dowodów, przykładów i ilustracji.
