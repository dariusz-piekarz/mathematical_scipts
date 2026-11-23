# Analiza funkcjonalna — moduł 15A — audyt 02 (niezależny przegląd matematyczny)

**Data:** 24 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (istniejąca; bez nowej gałęzi).  
**Źródło:** `chapters/pl/functional_analysis/15A-calkowanie-funkcji-w-przestrzeniach-lokalnie-wypuklych.tex`.  
**SHA źródła:** `f42bf05883d30c43cc6037ed3e78476a5bf6318f`, bez zmian od 15A/01.  
**SHA regresji:** `d9dc2437a13b441fbcaf16e3a252809529551ca0`, bez zmian od 15A/01.  
**Werdykt matematyczno-redakcyjny:** pierwszy niezależny **CZYSTY audyt (1/2)** po audycie 15A/01, który poprawiał źródło i miał status 0/2. Zamknięcie modułu wymaga jeszcze drugiego czystego audytu na niezmienionym źródle, zielonego CI i kontroli faktycznego PDF.

## Przebieg i weryfikacja punktu wyjścia

Odczytano z GitHub API bieżące źródło 15A, raport 15A/01, regresję `test_functional_analysis_ch15a.py`, książkę zbiorczą i przykładowy workflow rozdziału 15. Rozdział 15 jest stabilny (15/03: dwa czyste audyty i ukończone zielone CI). Raport 15A/01 wykrył i naprawił brakujące założenie całkowalności na podprzedziałach oraz skonstruował przykład kompensacji dwóch nieistniejących całek w niezupełnej przestrzeni; nie wolno ignorować tej poprawki ani przypisywać jej ponownie do 15A/02.

Na istniejącej gałęzi nie było workflow `functional-analysis-ch15a.yml`. Utworzono go w commicie [9b4f8ca5e433](https://github.com/dariusz-piekarz/mathematical_scipts/commit/9b4f8ca5e433221a6329b5f6e694016f39d745c8). Uruchamia istniejącą regresję i przygotowuje wrapper faktycznych rozdziałów 01–17 wraz z modułami 15A i 15B, dzięki czemu obejmuje również przywołane etykiety z rozdziałów 14, 16, 17 i modułu 15B. Nie jest to formalizacja w Lean ani dowód wszystkich twierdzeń.

## Drugi przegląd wszystkich dziesięciu dowodów

1. **Istnienie całki Riemanna (zupełność ciągowa).** Dla każdej seminormy `p`, jednostajna ciągłość `p(f(t)-f(s))` na zwartym odcinku daje moduł `omega_p(r)->0`. Wspólne rozdrobnienie podziałów P i Q prowadzi do `p(S_P-S_Q)<=2(b-a)omega_p(r)`. Istotny krok logiczny jest poprawny: tylko *jeden* wybrany ciąg sum dyadycznych potrzebuje zupełności ciągowej; następnie to samo oszacowanie kontroluje już wszystkie drobne sumy w topologii E. Nie przemyca się zupełności dla dowolnych sieci.
2. **Liniowość i oszacowania seminormowe.** Suma Riemanna jest liniowa, a przejście do granicy daje liniowość całki. Z nierówności trójkąta otrzymujemy `p(int f)<=int p(f)`. Addytywność względem przedziału jest stwierdzona **tylko wtedy, gdy obie całki na podprzedziałach istnieją**; to ograniczenie jest konieczne, co potwierdza przykład z `c_{00}` poniżej.
3. **Przemienność z ciągłymi odwzorowaniami liniowymi.** Dokładna równość `S(Tf,P)=T(S(f,P))` i ciągłość T zapewniają całkę obrazu nawet bez zupełności F. Oddzielanie punktów przez E' (Hahn–Banach i Hausdorff) wyjaśnia jednoznaczność wektora całki na podstawie jej wartości skalarnych.
4. **Środek ciężkości ciągłej krzywej.** Każda znormalizowana suma dla a<b należy do otoczki wypukłej obrazu f; przejście do granicy wymaga domknięcia i wystarcza do tezy bez twierdzeń o zwartości otoczki.
5. **Całka w uzupełnieniu.** Kanoniczne `j:E->Ehat` jest zanurzeniem topologicznym. Po całkowaniu `j circ f` w przestrzeni zupełnej warunek `int j(f) in j(E)` jest jednocześnie konieczny i wystarczający; w dowodzie kierunku wystarczającego istotnie użyta jest topologia indukowana na j(E).
6. **Całka niewłaściwa.** Ogon `int_R^{R'}p(f)` daje warunek Cauchy'ego dla całek wektorowych po kolejnych całkowitych promieniach. Istnienie ich granicy wynika z zupełności ciągowej, a kontrola dowolnego rzeczywistego R zapewnia pełną granicę, nie tylko zbieżność wybranego ciągu.
7. **Newton–Leibniz w E.** Różnica ilorazowa funkcji pierwotnej jest oszacowana przez supremum `p(f(t)-f(x))` na krótkim odcinku, także przy ujemnym h po uwzględnieniu orientacji. Dla dowolnej krzywej C¹ zastosowanie skalarnego twierdzenia do wszystkich `ell circ G` i rozdzielanie punktów przez E' daje formułę wektorową.
8. **Różniczkowanie całki parametrycznej.** Założona ciągłość pochodnej `partial_s f` na zwartym prostokącie wokół ustalonego s jest *jednostajna względem t*. Dla ustalonej seminormy `p` nierówność dla ilorazu różnicowego wynika ze skalarnego Newtona–Leibniza po wszystkich funkcjonałach liniowych zdominowanych przez p (Hahn–Banach); norma `p` różnicy jest supremum odpowiednich modułów. Po scałkowaniu i oszacowaniu w seminormie otrzymujemy różniczkowalność oraz ciągłość F'. Nie potrzeba nieudowodnionego wektorowego twierdzenia o wartości średniej.
9. **Fubini dla funkcji ciągłych.** Obie całki wewnętrzne istnieją przez zupełność ciągową i zależą ciągle od drugiej zmiennej. Ich sumy Riemanna są porównywane z *tą samą* podwójną sumą, z błędem ograniczonym przez `(b-a)(d-c)omega_p`; obie kolejności mają tę samą granicę. Nie użyto bezpodstawnie mierzalności Bochnerowskiej.
10. **Silna całka rodziny operatorów.** Punktowa ciągłość t↦T(t)x na zwartym przedziale daje punktowe ograniczenie rodziny operatorów; Banach–Steinhaus zapewnia `sup_t||T(t)||<infty`. Całka `int T(t)x dt` istnieje dla każdego x w Banachu Y, jest liniowa i ma normę nie większą niż `(b-a)sup_t||T(t)||`. Twierdzenie celowo *nie* stwierdza ciągłości normowej rodziny.

**10/10 dowodów: bez nowej luki matematycznej wymagającej poprawki źródła.** Uwzględniono poprawione założenie z 15A/01.

## Niezależna kontrola czterech przykładów

1. **`c_{00}` w normie `ell²`.** Podpory składowych są rozłączne, amplituda `2^{-n}` zapewnia ciągłość w t=0; w uzupełnieniu współrzędna całki wynosi `2^{-2n-1}int_0^1 eta>0`, więc granica nie leży w `c_{00}`. Odbicie z przeciwnym znakiem na [1,2] znosi całkę w `ell²`, a zerowa całka całej krzywej należy do `c_{00}`; ograniczenie do [0,1] nadal nie jest całkowalne. To uzasadnia korektę addytywności w 15A/01.
2. **`C^infty(Omega)`.** Dla topologii wyznaczonej przez seminormy na zwartych podzbiorach funkcja t↦u_t jest całkowalna dzięki zupełności; operator każdej pochodnej i ewaluacja są ciągłe, więc wzór na pochodną całki wynika z przemienności z ciągłym operatorem.
3. **Przestrzeń Schwartza.** Seminorma `q_{m,k}(partial^alpha u)` jest ograniczona przez `q_{m,k+|alpha|}(u)`. Oszacowania całki i zgodność z różniczkowaniem są poprawne dla każdego m,k,alpha.
4. **Silna ciągłość bez normowej.** `U_t f(x)=e^{itx}f(x)` na zespolonym `L²(R)` jest silnie ciągłą grupą unitariów przez zbieżność zmajoryzowaną. Dla każdego t≠0 mnożnik `e^{itx}-1` osiąga moduł 2 i przez ciągłość jest dowolnie bliski 2 na zbiorze dodatniej miary; stąd norma operatorowa `||U_t-I||=2`. To odróżnia całkę silną od całki w normie operatorowej.

**4/4 przykłady: poprawne.** Test dokładnych współrzędnych dla funkcji odcinkami liniowej z pierwszego przykładu jest rzeczywistą regresją skończenie wymiarową; nie dowodzi sam w sobie tezy o przestrzeni `c_{00}`.

## LaTeX, skład i odsyłacze

Źródło 15A zawiera **443 wiersze**, **16 etykiet**, osiem wystąpień odsyłaczy typu `ref/hyperref`. Sparowanie: 7 `twierdzenie`, 2 `stwierdzenie`, 1 `wniosek`, 1 `definicja`, 4 `przyklad`, 2 `uwaga`, 10 `proof`. Brak ilustracji TikZ i niedozwolonych terminów objętych kontrolą. Odsyłacze do `sec:integral-vector15b`, `sec:wariacyjny16`, `sec:gladkie-schwartz17` i `sec:gateaux-frechet14` mają cele w istniejących modułach/rozdziałach. Kompletną kontrolę odsyłaczy w faktycznym PDF przeprowadza nowa bramka CI.

## Decyzja stabilizacyjna

**15A/02: CZYSTY przegląd matematyczno-redakcyjny na niezmienionym blobie źródła: 1/2.** Nie poprawiano na siłę źródła, nie tworzono nowej gałęzi, nie rozwijano 15B ani rozdziału 16. W momencie tworzenia tego raportu dedykowany workflow [#45288905189](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45288905189) wykonał test regresyjny i przygotowanie dokumentu, a kompilacja/walidacja PDF pozostają do ostatecznego potwierdzenia. Jeżeli CI zakończy się niepowodzeniem, naprawić rzeczywiste przyczyny i nie liczyć nieudanych bramek jako sukcesów.

**Następny etap: druga niezależna czysta kontrola 15A/03, wizualna inspekcja wygenerowanego PDF i zielone CI; dopiero potem decyzja STABILNY i audyt 15B.**

## Weryfikacja ukończonego CI, rzeczywistego PDF i tożsamości źródła

Przebiegi dedykowanego workflow `functional-analysis-ch15a.yml`: [#45288905189](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45288905189), [#45289255859](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289255859) oraz [#45289298380](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289298380) zakończyły się **completed / success**. Dla ostatniego przebiegu niezależnie sprawdzono wszystkie dziewięć kroków: regresja PASS, przygotowanie rzeczywistego kontekstu **01–17 z 15A i 15B PASS**, kompilacja LaTeX PASS, weryfikacja PDF, nagłówków i odsyłaczy PASS, przesłanie artefaktów PASS. W osobnym commicie `ad4cb6e719dda801149b5048803b8e3ba4481870` doprecyzowano wyłącznie techniczne nazwy joba i kontekstu; nie zmieniono merytorycznej kontroli.

Pobrano faktyczny artefakt `functional-analysis-ch15a-pdf` (ID **14873835678**) z pierwszego zielonego przebiegu. `pdfinfo` potwierdził dokument **109 stron, A4, pdfTeX**. Zbadano wizualnie **strony 90–95**, zawierające cały moduł 15A (z początkiem 15B na s. 95). Nie stwierdzono uciętych wzorów, nachodzących fragmentów tekstu ani widocznych błędów łamania rozdziału. Podwójna numeracja 15A/15B jest zamierzona i odsyłacze w ich obrębie mają cele w kompilowanym kontekście. Sprawdzono log: nie występują błędy `Undefined control sequence`, niezdefiniowane odsyłacze, `Overfull \\hbox` ani `Missing character`. Jest **jedno `Underfull \\hbox` w rozdziale 16**, za 15A i 15B (wiersze 336–342 tego pliku); nie jest błędem składu samego modułu 15A i nie blokuje jego aktualnego audytu, pozostaje do przeglądu przy rozdziale 16.

Ponownie pobrano źródło 15A (SHA `f42bf05883d30c43cc6037ed3e78476a5bf6318f`) oraz test (SHA `d9dc2437a13b441fbcaf16e3a252809529551ca0`), oba niezmienione od 15A/01. **Końcowy werdykt 15A/02: czysty przegląd 1/2, bramka techniczna PASS.** Moduł **nie jest jeszcze stabilny**: wymaga niezależnego drugiego czystego audytu 15A/03 na tej samej wersji źródła i potwierdzonej końcowej bramki. Moduł 15B pozostaje zablokowany do tej decyzji.
