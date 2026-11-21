# Algebra liniowa — rozdział 26, audyt III (drugi czysty, stabilizacyjny)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/26-uogolnione-twierdzenia-riccatiego.tex`  
**Zatwierdzony blob:** `8ae57f3905cf88bc24d94fe1fd8d89f107a353e9`.  
**Historia:** audyt I — pełny przegląd wstępny; II — pierwszy niezależny czysty; III — drugi kolejny czysty na niezmienionym blobie.

## Matematyka — powtórna kontrola całości

1. **Faktoryzacja kosztu.** Dla każdego hermitowskiego Q≥0 wykazano jawnie istnienie C=Q^{1/2} z C*C=Q. Równość x*Qx=||Cx||² oraz ker C=ker Q jest prawdziwa również w przypadkach Q=0 i Q osobliwej. Różne faktoryzacje nie zmieniają wykrywalności, ponieważ mają to samo jądro i kryterium PBH testuje właśnie wektory własne w tym jądrze.
2. **Koszt stabilnego K_0.** Dzięki LA-25 istnieje stabilizujące K_0, jeśli (A,B) jest stabilizowalna. Szereg i całka z H=Q+K_0*R K_0≥0 są zbieżne; otrzymuje się W_d, W_c≥0 i oszacowanie kosztu dla każdego horyzontu. Nigdzie nie wyciąga się błędnego wniosku o stabilności macierzy z samego półokreślonego równania Lapunowa.
3. **DARE — istnienie.** Poprawna rekurencja P_0=0, P_{N+1}=Q+A*P_NA−A*P_NB(R+B*P_NB)^{−1}B*P_NA wynika z uzupełniania kwadratu dla M_N>0. Monotoniczność P_N opiera się na nieujemnych kosztach etapowych, a ograniczenie przez W_d daje zbieżność i przejście do granicy także przy macierzy P osobliwej.
4. **DARE — stabilność.** Tożsamość P−D*PD=Q+K*RK, D=A−BK, jest sprawdzona algebraicznie. Gdyby Dv=λv z |λ|≥1, nierówności po pomnożeniu przez v* i v wymusiłyby Cv=Kv=0, a wtedy Av=λv przeczyłoby wykrywalności. Warunek obejmuje granicę |λ|=1.
5. **DARE — jednoznaczność.** Dla P_i Hermitowskich i stabilizujących, bez żądania M_2>0, różnica E=P_1−P_2 spełnia E=D_1* E D_2. Iteracja oraz zanik obu potęg daje E=0. Każde rozwiązanie P_2≥0 jest stabilizujące przez poprzedni argument, więc P jest także jedynym rozwiązaniem półokreślonym.
6. **CARE — skończony horyzont.** Dla S'=A*S+SA−SBR^{−1}B*S+Q, S(0)=0, lokalna jednoznaczność i sprzężenie hermitowskie dają S=S*. Różniczkowanie x*S(T−t)x ma właściwe znaki; po uzupełnianiu kwadratu uzyskuje się osiągane minimum. Globalne istnienie S(T) wynika z ograniczenia przez zerowe sterowanie na każdym skończonym przedziale, niezależnie od stabilności A.
7. **CARE — granica i stabilność.** Z monotoniczności kosztu i jednostajnego W_c wynika S(T)↑P≥0. Z S'=F(S) i S(T)→P wyprowadzono F(P)=0, uzasadniając, dlaczego zbieżna pochodna musi mieć granicę zero. Tożsamość D*P+PD=−(Q+K*RK) i wykrywalność wykluczają wartości własne D z Re λ≥0.
8. **CARE — jednoznaczność.** Zastosowanie tożsamości kosztowej do dwóch stabilizujących rozwiązań P_1,P_2 pod ich własnymi sprzężeniami daje kolejno P_1≥P_2 i P_2≥P_1. Dowód nie wymaga dodatniości P_2. Każde inne rozwiązanie P_2≥0 samo musi być stabilizujące i stąd równe P.
9. **Wykrywalność i zanik.** Dla dowolnego sterowania o skończonym koszcie Q=C*C oraz R>0 oznaczają u,Cx∈ℓ² lub L². Wzmocnienie obserwatora L zapewnia stabilne D=A−LC; wymuszenie w=Bu+LCx również jest kwadratowalnie sumowalne/całkowalne. Podział splotu na końcową sumę i mały ogon z oszacowaniami Cauchy'ego–Schwarza prowadzi do zaniku całego stanu. Uzasadnia to brak końcowego składnika x_N*Px_N i x(T)*Px(T) w nieskończonych tożsamościach kosztowych.
10. **Optymalność.** W DARE minimalizacja residualnego kwadratu z M=R+B*PB>0, w CARE z R>0, daje dokładny koszt x_0*Px_0. Zanik zamkniętych trajektorii zapewnia osiągalność minimum oraz jednoznaczność: w dyskretnym przypadku na wszystkich krokach, w ciągłym prawie wszędzie.
11. **Przykłady i kontrprzykłady.** Skalarny DARE A=2, Q=4/5, P=4 i drugi pierwiastek −1/5; CARE A=1, Q=3, P=3 i drugi pierwiastek −1. Dwuwymiarowe osobliwe rozwiązania P=diag(4,0) oraz P=diag(3,0) spełniają równania dokładnie i zamykają niestabilny kierunek, a stabilny nieobserwowalny pozostaje bez kosztu. Przy Q=0 nie można usunąć wykrywalności bez utraty stabilizującego charakteru granicy; przy B=0 z niestabilnym A brak stabilizowalności uniemożliwia nieujemne rozwiązanie.

## Walidacja i PDF

- Dokładny plik `tools/test_linear_algebra_general_riccati.py` przechodzi wszystkie przypadki z arytmetyką wymierną, m.in. 250 dyskretnych oraz 250 ciągłych dokładnych tożsamości dopełnienia kwadratu dla układów z Q osobliwą, skalarne rekurencje i niezbędne kontrprzykłady.
- [GitHub Actions 44950558183](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44950558183) — **SUCCESS** dla zintegrowanego rozdziału, pełnych testów LA-01–26, kompilacji książki, sprawdzenia poprawności odsyłaczy i braku ostrzeżeń w końcowym logu. Kontroler wymienił 918 etykiet w skrypcie; brak powtórzeń i nieznanych odsyłaczy.
- Źródło LA-26 ma **38 różnych etykiet, 45 odsyłaczy i 9 kompletnych dowodów**. Środowiska są domknięte, tekst nie zawiera zakazanych form terminologicznych ani zewnętrznych obrazów.
- Pobraną z artefaktu `linear-algebra-current-chapter` wersję PDF zapisano jako `algebra_liniowa_rozdzial_26.pdf`. Dokument ma **13 stron i zawiera wyłącznie rozdział 26**, wszystkie strony są niepuste. Inspekcja PyMuPDF: **0 bloków tekstu poza stroną**. Wykonano render wszystkich stron i wizualnie obejrzano zestawienie: bez widocznych kolizji, uciętych wzorów i problemów z marginesami.
- Audyt III nie wykrył nowych błędów matematycznych ani typograficznych; rozdziału nie rozszerzono o niezaplanowane twierdzenia.

## Decyzja

**Audyt III czysty**, drugi z rzędu po audycie II. Po pomyślnym CI i pełnej kontroli PDF **rozdział 26 uznajemy za STABILNY po 3 audytach**. Rozdziały **01–26** algebry liniowej mają status stabilny.

Plan dalszy: opcjonalne uzupełnienie o minimalne realizacje i funkcje przejścia (27–28) oraz zatwierdzone do adaptacji z DG-04 **grassmanniany i algebry Clifforda** (29–30). Przy przeniesieniu zachować niepowtarzalne dowody, przykłady i rysunki.
