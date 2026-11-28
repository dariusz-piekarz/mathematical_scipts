# Topologia ogólna — rozdział 15: audyt iteracja 04

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Zakres

Przeprowadzono niezależną kontrolę całego aktualnego pliku `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex`, ze szczególnym uwzględnieniem nowego dowodu twierdzenia Stone'a, po iteracji 03. SHA treści źródła: `e75e17ef040d7e523624458fee888f2d2b01049e`. Treści matematycznej nie trzeba było zmieniać.

## Pełna weryfikacja twierdzenia Stone'a

1. **Kwantyfikatory, indeksowanie, wybór.** Dla niepustego `X` dane jest dowolne pokrycie otwarte `(U_α)_{α<κ}`. Jego dobre uporządkowanie umożliwia zdefiniowanie pierwszego indeksu `α(x)`. Wybór taki dla wszystkich punktów jest dopuszczalny w zwykłym ujęciu ZFC (twierdzenie o dobrym uporządkowaniu). Przypadek `X=∅` jest jawnie wyłączony i rozwiązany.
2. **Rekurencja po poziomach.** `E_(α,n)` zależy wyłącznie od poziomów `j<n`, dlatego definicja nie jest kołowa. Z `B(z,3r_n)⊂U_α` i `r_n<3r_n` wynika `V_(α,n)=⋃_{z∈E_(α,n)}B(z,r_n)⊂U_α`; zbiór jest otwarty.
3. **Pokrycie.** Dla `x∈X` istnieje `n` z `B(x,3r_n)⊂U_{α(x)}`, ponieważ `r_n→0`. Gdy `x` nie leży na wcześniejszym poziomie, wszystkie warunki na środek są spełnione i `x∈V_(α(x),n)`. Nie wymaga to założenia o przeliczalności indeksów `α`.
4. **Separacja zbiorów jednego poziomu.** Dla `β<γ` środek `z∈E_(γ,i)` nie należy do `U_β` z definicji pierwszego indeksu. Drugi środek `y∈E_(β,i)` ma `B(y,3r_i)⊂U_β`. Zatem `d(y,z)≥3r_i`. Jeśli `p∈B(y,r_i)` i `q∈B(z,r_i)`, to `d(p,q)>r_i`. Każda kula o średnicy najwyżej `r_i` może zatem spotkać co najwyżej jeden element poziomu `i`; równość na granicy nie przeszkadza dzięki ostrym nierównościom dla otwartych kul.
5. **Odrzucenie dostatecznie późnych poziomów.** Wybieramy `x∈V_(α,n)` oraz `B(x,ρ)⊂V_(α,n)`. Przy `M>n` z `2r_M<ρ` dopuszczalne środki poziomów `i≥M` leżą poza `V_(α,n)`, więc ich odległość od `x` jest co najmniej `ρ`. Dla `p∈B(z,r_i)` mamy `d(x,p)>ρ-r_i≥ρ-r_M>r_M`. Dlatego `B(x,r_M)` nie spotyka żadnego `V_(β,i)` dla `i≥M`.
6. **Skończona liczba wcześniejszych poziomów.** Dla `1≤i<M` mamy `r_i≥2r_M`, natomiast średnica `B(x,r_M)` jest co najwyżej `2r_M`. Z wyniku w pkt 4 wynika, że otoczenie może spotkać co najwyżej jeden zbiór z każdego wcześniejszego poziomu, w sumie najwyżej `M-1` zbiorów indeksowanej rodziny. Otrzymano **lokalną skończoność**, nie jedynie `σ`-lokalną skończoność.
7. **Wniosek.** Otwarta rodzina `(V_(α,i))` pokrywa `X`, jest lokalnie skończona i uszczegóławia dowolne `U`. Zgodnie z definicją parazwartości bez domyślnego aksjomatu Hausdorffa — metryczność i tak zapewnia Hausdorffowość — dowód jest pełny.

## Pozostałe dowody i integracja

- Powtórnie sprawdzono własność domknięć lokalnie skończonej rodziny, uszczegółowienia indukowane przez podziały jedności oraz funkcje odcinające przy jawnych zagnieżdżeniach domknięć.
- Konstrukcja `φ_n=f_n∏_{j<n}(1-f_j)` ma lokalnie skończone nośniki dzięki otwartemu otoczeniu `W_N` z `f_N|_{W_N}=1`; tożsamość teleskopowa zapewnia sumę równą `1`.
- Przypadki `X=∅`, skończonego podpokrycia i nieprzeliczalnej przestrzeni dyskretnej nie prowadzą do braków w definicjach.
- Zależności od rozdziałów wcześniejszych są jawne, bez użycia późniejszej parazwartości w żadnym wcześniejszym dowodzie.
- Rozdział ma testy enumeracyjne konstrukcji Stone'a na skończonych przestrzeniach dyskretnych oraz test 3125 konfiguracji tożsamości teleskopowej. Testy są pomocnicze i nie zastępują sprawdzenia dowodu.

## Weryfikacja techniczna

Treść LaTeX jest identyczna z wersją zweryfikowaną w CI:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010390038 — `completed/success`.
Odpowiadający jej artefakt `14749232978` zawiera samodzielny czterostronicowy PDF rozdziału 15 i log bez ostrzeżeń oraz nieudanych kroków. W poprzedniej iteracji obejrzano strony 3–4 po korekcie łamania tezy Stone'a. W tej iteracji sprawdzono niezależnie założenia i oba oszacowania dowodu, bez zmiany źródła.

## Werdykt iteracji 04

| Kryterium | Ocena |
| --- | --- |
| Dowód Stone'a, w tym oba oszacowania | PASS |
| Własna konstrukcja podziałów jedności | PASS |
| Przykłady, kontrprzykłady i przypadki brzegowe | PASS |
| Przesłanki, język i poprawne odsyłacze | PASS |
| Testy/CI oraz samodzielny PDF dla niezmienionego źródła | PASS |
| Poprawki konieczne w iteracji 04 | **BRAK** |
| Decyzja | **ROZDZIAŁ 15 STABILNY — audyt zamknięty** |

Po iteracjach 01–04, w tym osobnym szczegółowym audycie pełnego dowodu Stone'a, rozdział 15 spełnia ustalone kryteria stabilizacji i może stanowić podstawę rozdziału 16.
