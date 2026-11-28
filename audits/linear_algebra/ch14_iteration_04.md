# Algebra liniowa — rozdział 14, audyt IV

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/14-wartosci-wlasne-diagonalizacja-i-twierdzenie-spektralne.tex`  
**Blob po poprawkach:** `1ab7ad1276406324e44e051c8a756cfd225e0808`  
**Poprzednie audyty:** `ch14_iteration_01.md`, `ch14_iteration_02.md`, `ch14_iteration_03.md`; uzupełnienie o jednoczesnej diagonalizacji w `ch14_addendum_simultaneous_diagonalization_2026-11-21.md`.

## Zakres pełnego powtórnego audytu

Sprawdzono kolejno: definicję wartości własnej i wielomianu charakterystycznego, niezależność bazy, krotności geometryczne i algebraiczne, niezależność przestrzeni własnych, kryteria diagonalizacji, dowód rozkładu Schura, normalność i jej konsekwencje, zespolone oraz rzeczywiste twierdzenie spektralne, rzuty spektralne i wielomiany operatora, iloraz Rayleigha, określoność, normę operatorową oraz trzy twierdzenia o wspólnych postaciach macierzy przemiennych. Zachowano przypadek `n=0`, ciała dowolnej charakterystyki i konwencję liniowości iloczynu skalarnego w drugim argumencie. Nie dodawano twierdzeń.

## Wykryte luki i korekty

1. **Dowód wspólnej diagonalizacji.** Po wykazaniu `p_j(T)W_lambda subset W_lambda` jawnie dodano `sum_j p_j(T)=I`, argument na przestrzeniach własnych i rozkład każdego `w in W_lambda` na `p_j(T)w`. Osobno uzasadniono bezpośredniość sumy poprzez niezależność przestrzeni własnych `T`. Usunięto skrót logiczny przy kluczowym kroku dowodu.
2. **Dowód wspólnej unitarnej triangularizacji.** Na `C^n/L` jawnie wprowadzono strukturę unitarną przez identyfikację z `L^perp`, co uzasadnia zastosowanie założenia indukcyjnego w wersji unitarnej. W konstrukcji bazy doprecyzowano `V_j=q^{-1}(F_{j-1})`, `V_0=0` i wybór `e_j in V_j intersect V_{j-1}^perp`, wraz z uzasadnieniem, że to przecięcie jest jednowymiarowe.
3. **Formy i określoność.** Forma `b(u,v)=h(u,Tv)` jest symetryczna dwuliniowa dla przestrzeni rzeczywistej, a hermitowska półtoraliniowa dla zespolonej. Wcześniejsza etykieta typologiczna obejmująca jednocześnie oba przypadki została skorygowana w treści i dowodzie. Doprecyzowano formę kwadratową `q(x)=x^T A x`.
4. **Przykład nienormalny.** Zastąpiono niedostateczny argument, który sprawdzał nienormalność wyłącznie `S`, pełnym uzasadnieniem dla `T=2S+I`: `TT^T-T^TT=4(SS^T-S^TS) != 0`.
5. **Język.** Poprawiono `skończenie wymiarowa` w stwierdzeniu (mianownik składniowy), `Z wzoru` na `Ze wzoru` i niezręczne sformułowanie o bazie ortonormalnej `V`.

## Niezależne testy i kontrola struktury

- Kontrola wyczerpująca macierzy `2x2` nad `F_2` i `F_3`: odpowiednio **40** i **441** par przemiennych operatorów, z których każdy jest diagonalizowalny nad swoim ciałem. Dla każdej pary zweryfikowano istnienie dwóch liniowo niezależnych wspólnych wektorów własnych. Dodano regresję do `tools/test_linear_algebra_spectral.py` (commit `1b06a9a7a913568d9c42ec44dfa18d29e9b09fa0`).
- Nie wykryto matematycznych kontrprzykładów dla żadnej z tez. Pozostawiono dotychczasowe etykiety `\\label` i odsyłacze.
- Po poprawkach rozdział ma **43 unikatowe etykiety**, **22 odsyłacze** oraz sparowane środowiska definicji, twierdzeń, dowodów i przykładów (lokalna kontrola strukturalna). Zmiana źródła: commit `20eda602dfb924a3011be567841ba879c7a68687`.
- Zbadano 14-stronicowy PDF sprzed poprawek: brak kolizji i przycięcia tekstu, wszystkie bloki tekstowe mieszczą się na stronach A4. Ostateczna kontrola po poprawkach opiera się na nowym PDF i GitHub Actions, a nie na tej wcześniejszej wersji.

## CI i decyzja

CI uruchomione dla korekty źródła: [44932867713](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932867713); dla nowej regresji: [44932971648](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932971648). Końcowy stan każdego przebiegu należy odczytać z jego strony; nie deklarowano wyniku przed zakończeniem. Workflow buduje pełną książkę dwukrotnie, sprawdza odsyłacze i ostrzeżenia składu, eksportuje PDF aktualnego rozdziału 15 oraz osobno rozdziału 14.

**Ocena merytoryczna:** po usunięciu wskazanych luk nie stwierdzono kolejnych niepoprawności; do zatwierdzenia typograficznego wymagany jest pomyślny wynik nowego CI i przegląd aktualnego PDF rozdziału 14. W następnej iteracji można kontynuować z rozdziałem 16 bez poszerzania rozdziału 14.
