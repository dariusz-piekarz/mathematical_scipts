# Topologia ogólna — globalny audyt 15: rozdział 14, siedem dowodów i kontrprzykłady

**Data:** 2026-11-22.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/general_topology/14-zwartosc-lokalna.tex`.
**Badany niezmieniony blob:** `24ca61f0e19fe6674719fc76e53073aa82cc755c`.
**Zakres:** niezależna kontrola wszystkich siedmiu środowisk `proof`, warunków koniecznych w hipotezach, sześciu przykładów i uwag, układu całego samodzielnego PDF i zależności logicznych. Żadna zmiana źródłowa nie była potrzebna.

## Wszystkie siedem dowodów

| Nr | Twierdzenie | Kontrola logiczna |
|---:|---|---|
| 1 | `lem:topog-baire-zwarte-domkniecie` | Z lokalnej zwartości istnieje zwarty K z x∈int_X K. Hausdorffowość X daje zwartość Hausdorffa K, więc normalność i regularność. Dla O=V∩int_X K wybór H otwartego w K z x∈H⊆cl_K H⊆O jest możliwy; ponieważ H⊆int_X K, zachodzi H=T∩int_X K dla pewnego otwartego T⊂X, więc H jest otwarty w X. Ponieważ K jest domknięty w X, cl_X H=cl_K H jest zwarty i zawarty w V. |
| 2 | `thm:topog-baire-lokalnie-zwarte` | Niepusty otwarty U przecina wszystkie gęste otwarte G_n. Rekurencyjnie wybieramy niepuste W_n oraz K_n=cl_X W_n zwarte, z K_{n+1}⊆W_n∩G_{n+1}. K_n są domknięte w X, zstępujące i niepuste, zawarte w K_1. Własność skończonych przecięć w zwartym K_1 daje punkt w U∩⋂G_n. Nie założono metryki, zupełności metrycznej ani przeliczalności baz. |
| 3 | `prop:topog-lokalna-podprzestrzenie` | Dla otwartego U wykorzystuje się zwężenie W o zwartym cl_X W⊆U, a więc ten sam kompakt jest zwartym otoczeniem punktu także w U. Dla domkniętego F kompakt K∩F jest domkniętym podzbiorem K, a x∈F∩int_X K⊆int_F(K∩F). Hausdorffowość dziedziczą obie podprzestrzenie. |
| 4 | `prop:topog-lokalna-iloczyny` | Dla m≥1 wybiera się zwarte otoczenia K_i w każdym czynniku. Zwartość produktu K z Tychonoffa/skończonego twierdzenia o produktach oraz otwartość ∏int(K_i) pokazują lokalną zwartość; własność Hausdorffa produktu jest udowodniona w rozdziale 04. |
| 5 | `thm:topog-lokalna-dowolny-iloczyn` | Konieczność: kompaktowe otoczenie K punktu x zawiera cylinder B ograniczony skończenie wieloma współrzędnymi F. Dla i∉F mamy p_i(B)=X_i, a więc X_i=p_i(K) jest zwarta. Dla wszystkich i, p_i(K) jest zwartym otoczeniem x_i, gdyż zawiera otwarte p_i(B). Niepustość każdej X_i umożliwia dopełnienie dowolnego punktu y_i do punktu produktu (w standardowym ZFC). Wystarczalność: produkt zwartych X_i dla i∉F jest zwarty według Tychonoffa; skończony iloczyn pozostałych jest lokalnie zwarty; produkt tych dwóch przestrzeni jest lokalnie zwarty. Pusty indeks F i pusty zbiór I nie są kontrprzykładami. |
| 6 | `thm:topog-lokalna-wyczerpanie` | Dla każdego kompaktu C istnieje kompakt K z C⊂int_X K, uzyskany ze skończonej sumy zwartych otoczeń punktów C. Rekurencja daje K_n∪C_{n+1}⊂int K_{n+1}; po indukcji X=∪int K_n. W kierunku (iii)⇒(ii) zwarty C ma skończone podpokrycie przez rosnące int K_n, więc C⊂K_N. W kierunku (ii)⇒(i) każdy singleton {x} jest zwarty, a zatem X=∪K_n. Przypadek C=∅ jest obsłużony. |
| 7 | `prop:topog-lokalna-drugi-aksjomat` | Drugi aksjomat przeliczalności pociąga własność Lindelöfa, więc otwarte pokrycie (U_x) otoczeniami o zwartych domknięciach ma przeliczalne podpokrycie. Zbiór X jest sumą odpowiednich zwartych domknięć, stąd jest σ-zwarty. Wyczerpanie wynika z poprzedniego twierdzenia, nie z nadużycia pierwszego aksjomatu przeliczalności. |

## Kontrprzykłady i granice hipotez

**Przestrzeń wymierna Q.** `Q` jest σ-zwarta jako przeliczalna suma zwartych singletonów, lecz nie jest przeliczalna w nieskończoności. Każdy kompakt K⊂Q ma puste wnętrze w Q: gdyby zawierał względnie otwarty niepusty przedział Q∩(a,b), byłby zwarty, więc domknięty w R, i zawierałby domknięcie [a,b] z punktami niewymiernymi. Dla przypuszczalnej współkońcowej rodziny kompaktów K_n można przejść do rosnących L_n=∪_{j≤n}K_j. Wybierając q∈Q i q_n∈Q∩(q−1/n,q+1/n)\L_n, otrzymujemy zwarty zbiór C={q}∪{q_n}⊂Q, który nie mieści się w żadnym L_n (dla każdego n świadkiem jest q_n). Argument nie wymaga, aby q_n były parami różne.

**Nieprzeliczalna przestrzeń dyskretna D.** Jest lokalnie zwarta, ponieważ singletony są zwarte i otwarte. Każdy jej kompakt jest skończony, więc D nie jest σ-zwarta; poprawnie obala domniemanie, że lokalna zwartość implikuje σ-zwartość bez warunku przeliczalności.

**Prosta rzeczywista.** K_n=[−n,n] spełnia K_n⊂int K_{n+1} i ∪int K_n=R; każdy kompakt jest ograniczony, więc mieści się w pewnym K_n.

**Dodatkowe przypadki brzegowe:** pusty X jest lokalnie zwarty, σ-zwarty i przeliczalny w nieskończoności w podanych definicjach; produkty pustej rodziny to singletony. Żadna implikacja nie wymaga wykluczenia tych przypadków. Dla dowolnych rodzin niepustych czynników niepustość produktu korzysta z zasady wyboru, która jest używana także przez twierdzenie Tychonoffa.

## Zależności i skład PDF

Sprawdzono, że normalność zwartej przestrzeni Hausdorffa, dziedziczenie zwartości i twierdzenie Tychonoffa pochodzą z rozdziału 07, własność Lindelöfa z rozdziału 09, a własności topologii produktu z rozdziału 04. W dowodach nie ma zależności od późniejszych rozdziałów o uzwarceniach.

W rzeczywiście wykonanym CI [45070070493](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070070493), completed/success, blob rozdziału 14 pozostaje niezmieniony. Z artefaktu **14773205627** pobrano i wyrenderowano wszystkie **4 strony A4** pliku `general_topology_ch14.pdf`. Obejrzano je jako planszę zbiorczą: brak oczywistych kolizji, ucięć i izolowanych akapitów. Brak środowisk `figure` w rozdziale. Logi `general_topology_ch14.log` i `general_topology.log` nie zawierają `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` ani `Fatal error`.

## Decyzja

**PASS: 7/7 dowodów, wszystkie trudne kontrprzykłady, przypadki brzegowe, odsyłacze i samodzielny PDF.** Nie znaleziono nowego błędu matematycznego ani wydawniczego. Źródło rozdziału 14 zachowuje blob `24ca61f0e19fe6674719fc76e53073aa82cc755c` i wcześniejszy status stabilnego rozdziału. Globalna kontrola całej książki pozostaje otwarta; następny blok: indywidualna kontrola dowodów rozdziału 15.
