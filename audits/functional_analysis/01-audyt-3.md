# Analiza funkcjonalna — rozdział 01 — audyt 03 (audyt potwierdzający)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/functional_analysis/01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex`  
**SHA obiektu Git rozdziału (odczyt przed audytem):** `fd55de818b2e22954bfb0e0aeaecc43afe75948d`  
**Wynik:** CZYSTY. Drugi kolejny niezależny audyt matematyczno-redakcyjny bez zmian w źródle (2/2); **rozdział 01 STABILNY**.

## Procedura

Niezależna kontrola twierdzeń, 9 pełnych dowodów i 7 przykładów, ze szczególnym uwzględnieniem kwantyfikatorów, rozdzielenia założeń Hausdorffa, przypadków x=0 / λ=0 / zbiorów pustych, norm i metryk niepochodzących od normy, granic w przestrzeniach funkcji, a także poprawności stylistycznej, etykiet i składu sześciostronicowego PDF. Nie dodawano nowych tematów ani nie zmieniano zaakceptowanej zawartości.

## Dowody: niezależna macierz 9/9 PASS

| Lp. | Przedmiot kontroli | Sprawdzony krok krytyczny | Wynik |
| --- | --- | --- | --- |
| 1 | Przesunięcia i homotetie | Ciągłość z działań w TVS i ciągłe odwrotności; także bez Hausdorffa. | PASS |
| 2 | Rodziny otoczeń | Równoważność `U∈N_X(x) ⇔ U-x∈N_X(0)` dotyczy także otoczeń nieotwartych. | PASS |
| 3 | Własności otoczeń zera | Konstrukcja `V+V⊆U`, symetrii, zrównoważonego `int(DV)` przez skończone pokrycie zwartego `D`; pochłanianie przez ciągłość `λ↦λx`. | PASS |
| 4 | Hausdorff i domknięcie zera | Dwie inkluzje `cl({0})=∩N_X(0)`; dobór symetrycznego `V` z `V+V⊆U`; liniowość domknięcia zera. | PASS |
| 5 | Ciągłość w zerze | Przeniesienie warunku otoczeniowego z zera do dowolnego x. | PASS |
| 6 | Domkniętość jądra | Warunek Hausdorffa w przestrzeni docelowej zapewnia domkniętość `{0}`. | PASS |
| 7 | Test ograniczoności | Zrównoważenie otoczenia pozwala zamieniać `B⊆tU` na `λB⊆U` dla małych skalarów. | PASS |
| 8 | Zwarty zbiór jest ograniczony; obraz ograniczonego | `x∈tV`, następnie `x∈nV` dla całkowitego `n≥t`; skończone podpokrycie rosnące; ciągłość `T` i przeciwobrazy otoczeń. | PASS |
| 9 | `L^p([0,1])`, `0<p<1` | `d` jest metryką; wspólna ciągłość działań; podciąg Cauchy'ego z sumowalnymi przyrostami; Fatou; oszacowanie funkcjonału; podziały na równe miary i `n^{1-1/p}→0`; gęstość funkcji prostych także nad `C`. | PASS |

**Weryfikacja twierdzenia o zbiorach zrównoważonych i pochłaniających.** Skrypt definiuje „pochłaniający” jako `∀x ∃t>0: x∈tA`. Tę konwencję można spotkać w źródłach analizy funkcjonalnej; jest ona słabsza od konwencji `∀x ∃ε>0 ∀|λ|≤ε: λx∈A`, jeśli `A` nie jest zrównoważony. Dla zbiorów zrównoważonych oba warunki są równoważne. Rozdział 01 konsekwentnie stosuje własną definicję, a jego dowody pozostają poprawne. **Nie zmieniono definicji automatycznie**; w razie potrzeby można w przyszłości dodać uwagę porównującą konwencje. Przykład odróżniający: `A={-1,0,1}⊂R` spełnia słabszą definicję, ale nie silniejszą. Definicja na początku rozdziału 05 jest zbieżna z konwencją rozdziału 01.

## Przykłady: 7/7 PASS

1. Topologia trywialna na niezerowej przestrzeni: działa, lecz nie jest Hausdorffa.
2. Suma prostokątów zrównoważonych: `(1,1)`, `(2,1/2)` należą, środek `(3/2,3/4)` nie należy.
3. Funkcje `f_n(x)=max(1-nx,0)`: `‖f_n‖_∞=1`, `‖f_n‖_1=1/(2n)`; aproksymacja skoku w normie całkowej wykazuje brak zupełności przestrzeni ciągłych z tą normą.
4. Ograniczoność von Neumanna w przestrzeni unormowanej = ograniczoność normowa, wraz z przypadkiem `∅`.
5. `K^N`: każda bazowa okolica pozostawia wolną współrzędną, więc nie jest ograniczona; `e_n→0` punktowo.
6. Topologia zbieżności punktowej: topologia podprzestrzeni produktu, charakteryzacja także dla sieci.
7. `p↦p'(0)` w przestrzeni wielomianów z normą supremum: `p_n=(1-t)^n` daje nieograniczone wartości przy normie 1.

## Rewizja logiczna i skrajne przypadki

- W początkowych twierdzeniach nie przyjmuje się domyślnie warunku Hausdorffa; zostaje wprowadzony zgodnie z tekstem dopiero później.
- Zauważono różnicę między ciągłością osobno względem skalaru/wektora a ciągłością łączną mnożenia — w definicji pozostaje wymagana ta druga.
- Przypadki `λ=0`, `x=0`, `K=∅`, `B=∅`, `A` mierzalnego o mierze 0, `p` bliskiego 1 i wartości zespolonych nie łamią dowodów.
- Dla `p=1` wykładnik `1-1/p` wynosi 0, więc rozumowanie o zerowości ciągłych funkcjonałów nie działa; sformułowanie prawidłowo zakłada `0<p<1`.
- Nie ma rozbieżności między treścią rozdziału a konwencją funkcji charakterystycznej `\chi_A`, zakazem samodzielnego angielskiego rzeczownika „dual” lub stabilnymi etykietami historycznymi.

## Kontrola techniczna

- 9 środowisk `proof`, 7 środowisk `przyklad`; 15 unikatowych etykiet, 4 odsyłacze do etykiet istniejących w tym rozdziale; źródło niezmienione w audycie 02 ani 03.
- Po audycie 02: [CI GitHub Actions 45151391976](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45151391976) — **PASS** dla 11 testów Pythona, dwukrotnej kompilacji i kontroli PDF oraz logu. Odrębny [przebieg 45151297754](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45151297754) również PASS.
- Sześciostronicowy PDF A4 i końcowy log kompilacji sprawdzono ponownie; brak nierozwiązanych odsyłaczy, ostrzeżeń o przepełnionych wierszach i brakujących znakach. Całość stron porównano wizualnie na arkuszu kontrolnym; nie stwierdzono nachodzenia tekstu, ucięcia tekstu ani błędów glifów.
- Testy liczbowe i skończonych modeli są kontrolami pomocniczymi; pełne dowody matematyczne sprawdzono osobno.

## Propozycje rozszerzenia — bez wprowadzania zmian

- Kontrast `L^p` i `\ell^p` przy `0<p<1` (rola bezatomowości).
- Charakteryzacja ograniczoności w `K^N`.
- Krótka uwaga o dwóch spotykanych konwencjach „zbioru pochłaniającego” w związku z brakiem założenia zrównoważenia.

Wszystkie są **opcjonalne** i wymagają osobnej decyzji użytkownika.

## Decyzja

**AUDYT 03: CZYSTY. Rozdział 01 ma dwa kolejne czyste audyty (2/2) i zostaje oznaczony jako STABILNY.** Nie wprowadzono zmian w źródle. Zgodnie z przyjętym rytmem prac następnym rozdziałem do audytu jest **02 — Podprzestrzenie, produkty, ilorazy i topologie uniwersalne**.
