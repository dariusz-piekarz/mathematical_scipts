# Algebra liniowa — rozdział 07, audyt 3 (stabilizacyjny)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Treść:** `chapters/pl/linear_algebra/07-przestrzen-dualna-i-odwzorowania-dualne.tex`  
**SHA skontrolowanej treści:** `ddc127f9c94ec7bd71df6df74e4e1705eb48d7f7`

## Ponowna kontrola poprawności matematycznej

Po zmianach audytu 2 sprawdzono powtórnie wszystkie sekcje i dowody, nie rozszerzając ustalonego zakresu rozdziału:

1. **Dual i baza dualna:** definicje `V*=Hom_K(V,K)` i `v^i(v_j)=δ_ij` są poprawne, konstrukcja i jednoznaczność baz dualnych wynikają z twierdzenia o odwzorowaniu określonym na bazie. Nie utożsamiono bez podstawy przestrzeni `V` i `V*`.
2. **Zmiana bazy:** dla konwencji `[v]_B=P[v]_C` zweryfikowano oba wzory `[φ]_{C*}=P^T[φ]_{B*}` oraz `w^j=Σ_i(P^-1)_{ji}v^i`, wraz z indeksowaniem kolumn.
3. **Anihilatory:** definicje `U^∘⊂V*` i `S_∘⊂V` są typowane poprawnie; wzory wymiarowe, podwójnego anihilatora i anihilatora sumy/przecięcia są dowiedzione ze wszystkimi ograniczeniami do wymiaru skończonego. Poprawiony dowód dla `(S_∘)^∘=S` wykorzystuje jądro surjekcji `V→K^s`, nie odwołuje się do późniejszej bidualności, i uwzględnia `s=0`.
4. **Dual ilorazu i suma prosta:** funkcjonał na `V/U` jest dobrze określony dzięki zerowaniu na `U`, a rozszerzenie z podprzestrzeni korzysta z uzupełnienia bazy. Dowód sumy prostej jawnie korzysta z jednoznaczności rozkładu.
5. **Odwzorowanie dualne:** `T*:W*→V*` ma poprawny kierunek; wykazano `(S∘T)*=T*∘S*` i fakt, że jego macierzą w bazach dualnych jest `A^T`.
6. **Jądro/obraz:** wykazano zarówno `ker T*=(im T)^∘`, jak i `im T*=(ker T)^∘`; drugą inkluzję uzyskano przez konstrukcję funkcjonału na `im T` i jego rozszerzenie. Stąd pochodzą równości rzędów i kryteria iniektywności/surjektywności.
7. **Bidualność:** `J_V(v)(φ)=φ(v)` jest liniowym izomorfizmem w wymiarze skończonym, niezależnym od bazy, a naturalność `T**J_V=J_WT` ma poprawne dziedziny.
8. **Ślad:** liniowość i cykliczność `tr(AB)=tr(BA)` uzasadniono przez skończone sumy; `tr(P^-1AP)=tr A` pozwala zdefiniować ślad endomorfizmu. Wzór `tr R_{v,φ}=φ(v)` potwierdzono na macierzy endomorfizmu rzędu co najwyżej jeden.
9. **Brzegi zakresów:** uwzględniono `dim V=0`, `dim W=0`, `U={0}`, `U=V`, `S={0}`, charakterystykę `2` i rozróżnienie dualu algebraicznego od dualu ciągłego. Przykład z dzieleniem przez `2` ograniczono do `R`.

**Wynik audytu 3:** nie znaleziono kolejnego błędu matematycznego, istotnej luki dowodowej ani problemu terminologicznego. Nie zmieniono pliku `.tex` w tej iteracji.

## Niezależne obliczenia i CI

- Podwójny anihilator sprawdzony na wszystkich **16** podprzestrzeniach `F_2^3` i **6** podprzestrzeniach `F_3^2`: bez rozbieżności.
- Tożsamości `ker T*=(im T)^∘` i `im T*=(ker T)^∘` sprawdzono wyczerpująco dla **689** macierzy małych wymiarów nad `F_2` i **1621** nad `F_3`: bez rozbieżności.
- Ślad cykliczny porównano dla wszystkich **262144** par macierzy `3×3` nad `F_2` i **6561** par macierzy `2×2` nad `F_3`: bez rozbieżności.
- Kontrola siedmiu rozdziałów wykazała **303 różne etykiety, 128 istniejących celów odsyłaczy**, poprawne importy i katalog, brak naruszeń terminologicznych oraz brak niezbilansowanych środowisk.
- Po poprawkach z audytu II GitHub Actions [44911048502](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44911048502) — **success**: PDF **75 stron**, końcowy log LaTeX nie zawiera `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, błędów kompilacji ani brakujących odsyłaczy.
- [44911048459](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44911048459) — **success**: indeksowanie i testy aplikacji.
- [44910869077](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44910869077) — **success**: walidacja CLI pierwszego commitu rozdziału, a kolejny commit nie dotykał narzędzi.

## Decyzja

**Rozdział 07 stabilny i zamknięty po trzech audytach.** W tym commicie aktualizujemy tylko raport i komentarz statusowy w pliku głównym. Po tym commicie należy jeszcze sprawdzić nowy przebieg CI, który potwierdzi poprawność aktualnego stanu gałęzi.
