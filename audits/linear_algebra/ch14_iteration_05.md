# Algebra liniowa — rozdział 14, audyt V (niezależna kontrola stabilności)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/linear_algebra/14-wartosci-wlasne-diagonalizacja-i-twierdzenie-spektralne.tex`  
**Zweryfikowany blob:** `1ab7ad1276406324e44e051c8a756cfd225e0808`  
**Poprzednia iteracja:** `audits/linear_algebra/ch14_iteration_04.md`.

## Niezależna kontrola całego rozdziału

1. **Charakterystyczny i krotności (sekcja 14.1).** Dla dowolnego ciała poprawnie wywiedziono niezależność od bazy, kryterium `ker(T-lambda I) != {0}` i ograniczenie `1 <= g_T(lambda) <= a_T(lambda)`; szczególny przypadek `n=0` jest spójny z pustym wyznacznikiem.
2. **Diagonalizacja (14.2).** Rozkład na sumę prostą przestrzeni własnych, kryterium krotności przy rozszczepieniu wielomianu, niezależność odpowiednich wektorów i przykład Jordana nie wymagają dodatkowych założeń. Weryfikacja wyklucza błędne zastosowanie kryterium krotności nad ciałem, nad którym charakterystyczny się nie rozszczepia.
3. **Schur (14.3).** Indukcja jest prowadzona na kompresji `P_W T|_W`; nie wymaga niezmienniczości `W` względem `T`. Poprawna orientacja `U^* A U=R` i ujęcie `n=0`.
4. **Normalność i twierdzenie spektralne (14.4).** Poprawnie pokazano normalność `T-lambda I`, równoważność `Tv=lambda v => T^*v=conj(lambda)v`, dwustronną niezmienniczość dopełnienia ortogonalnego i brak rozumowania kołowego. W przykładzie hermitowskim sprawdzono znaki wektorów własnych `(-i,1)`, `(i,1)`.
5. **Spektralne rzeczywiste (14.5).** Rozróżnienie macierzy symetrycznych i ogólnych normalnych nad `R` jest poprawne; zespolenie daje rzeczywiste wartości własne, a przez części rzeczywistą/urojoną niezerowy rzeczywisty wektor własny.
6. **Rzuty i rachunek wielomianowy (14.6).** Interpolacyjne projektory mają niezerowe mianowniki; własności `P_iP_j=0`, `sum P_j=I`, `T=sum lambda_j P_j` i ujęcie `V={0}` są spójne. Ślad, wyznacznik i odwrotność są zgodne z mnożnościami.
7. **Rayleigh, określoność i norma (14.7).** Średnia ważona `lambda_j` z wagami `|c_j|^2`, ostre przypadki równości, podział form na rzeczywiste symetryczne i zespolone hermitowskie oraz normy operatora normalnego są uzasadnione. Wyłączono `V=0` z maksimum pustego spektrum.
8. **Postacie macierzy przemiennych (14.8).** (i) dla samosprzężonych, każda przestrzeń własna pierwszego jest niezmiennicza względem drugiego, a jego ograniczenie nadal samosprzężone. (ii) dla diagonalizowalnych nad dowolnym `K`, projektory Lagrange'a spełniają `sum_j p_j(T)=I` i dają rozkład na wspólne przestrzenie własne bez powołania się na twierdzenie zespolone. (iii) dla przemiennych nad `C`, istnieje wspólny wektor własny, następnie flaga ilorazowa; iloczyn skalarny ilorazu pochodzi z `L^perp`; baza dostosowana do flagi jest ortonormalna. Dla `n=0` wszystkie trzy stwierdzenia pozostają zgodne z konwencją macierzy pustych.
9. **Przykłady i kontrprzykłady.** Skontrolowano diagonalizację nieortogonalną `S=[[1,1],[0,2]]`, `T=2S+I` oraz nienormalność obu; przykład przemiennych bloków Jordana dowodzi niemożności diagonalizacji bez dodatkowego założenia.
10. **Redakcja i PDF.** W rozdziale pozostaje 43 różnych etykiet, 22 odsyłacze i zamknięte pary środowisk `proof`, `twierdzenie`, `przyklad`, `wniosek` itd. W 14-stronicowym PDF brak przyciętych obszarów tekstowych i kolizji składu (kontrola 14 stron oraz skrajnych współrzędnych tekstu). Nie znaleziono ostrzeżeń `Overfull`, `Underfull`, brakujących znaków, błędnych odsyłaczy ani błędów kompilacji.

## Regresje i decyzja

Pomyślny workflow po poprawkach oraz wprowadzeniu testów ciał skończonych:
[GitHub Actions 44932971648](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932971648).
Pomyślny workflow po zapisaniu audytu IV:
[GitHub Actions 44933041365](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44933041365).

**Audyt V — czysty: bez zmian matematycznych ani redakcyjnych w rozdziale.** Obecna wersja pozostaje stabilna. Uzasadnione jest przejście do rozdziału 16, bez ponownego poszerzania rozdziału 14. Przedmiot nowej iteracji: podprzestrzenie niezmiennicze i wielomian minimalny; rozdział 16 musi zostać objęty odrębnym audytem, zanim otrzyma status stabilny.
