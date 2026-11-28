# Analiza funkcjonalna — rozdział 07 — audyt 03 (kontrola niezależna po współbieżnym 07/02)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/07-oddzielanie-zbiorow-wypuklych-polary-i-twierdzenie-bipolarne.tex`.  
**SHA źródła po korektach:** `3802015b41891911fe852e6a2600547d894fab8c`.  
**Wynik:** niezależny audyt **Z POPRAWKAMI, NIE CZYSTY — 0/2** kolejnych czystych audytów wymaganych do stabilizacji. Nie rozpoczynamy rozdziału 08.

## Wersjonowanie i współbieżny audyt 07/02

Podczas realizacji tego audytu opublikowano równolegle `audits/functional_analysis/07-audyt-2.md` o statusie czystym **1/2**, ale odnosi się on jawnie do źródła o **starym SHA `914059e1b20f1a9a3a8766a899659cde32109fb7`** i nie obejmuje dwóch późniejszych korekt. Zachowano raport bez nadpisywania. Nowe poprawki do LaTeX resetują licznik stabilizacji aktualnej wersji do **0/2**, niezależnie od dodatniego wyniku wcześniejszego przeglądu.

## Niezależna kontrola wszystkich 11 dowodów

1. **Reprezentacja funkcjonału rzeczywiście liniowego:** w zespolonej TVS wzór `F(x)=ell(x)-i ell(ix)` określa jedyny ciągły zespolono-liniowy funkcjonał o części rzeczywistej `ell`. Sprawdzono liniowość i ciągłość. PASS.
2. **Funkcjonał Minkowskiego dla otwartego niekoniecznie zrównoważonego V:** pochłanianie wynika z ciągłości skalowania, podaddytywność z kombinacji wypukłej punktów `x/r`, `y/s` dla `r>p_V(x)`, `s>p_V(y)`; z `V={p_V<1}` i nierówności dwustronnych uzyskuje się ciągłość. Nie zakłada się symetrii `p_V(x)=p_V(-x)`. PASS.
3. **Oddzielanie punktu od otwartego zbioru wypukłego:** dla `D=C-x_0`, `a∈D`, `V=D-a` zachodzi `-a∉V`, `p_V(-a)≥1`. Funkcjonał zadany `g(t(-a))=t` jest dominowany przez p_V także dla t ujemnych, a przedłużenie Hahn–Banacha daje punktową ścisłą separację. PASS.
4. **Separacja dwóch wypukłych przy jednym otwartym:** zbiór różnic `A-B` jest niepusty, otwarty, wypukły i nie zawiera 0. Zastosowanie poprzedniego twierdzenia i wybór ustalonych `a_0,b_0` zapewniają skończoność supremum i infimum. Nie twierdzimy o dodatniej jednolitej luce. PASS.
5. **Wspólne otoczenie dla zbioru zwartego i domkniętego:** lokalna konstrukcja `W_k+W_k⊂V_k`, skończone podpokrycie i `U⊂∩W_{k_j}` gwarantują `(K+U)∩F=∅`; nie jest wymagana metryzowalność. PASS.
6. **Silna separacja zwartego wypukłego A i domkniętego wypukłego B:** dla otwartego wypukłego otoczenia `U` z `(A+U)∩B=∅` otrzymuje się niezerowy separator `ell`. Dla `u_0∈U` z `ell(u_0)>0` mamy `sup_A ell+ell(u_0)≤inf_B ell`. PASS.
7. **Oddzielanie punktu od domkniętego wypukłego C:** zastosowanie silnej separacji do zwartego singletonu i niepustego zamkniętego wypukłego C daje właściwą orientację nierówności. PASS.
8. **Hiperpłaszczyzna podpierająca:** `G=int(C)` jest niepusty, otwarty, wypukły. Punkty `(1-t)x+tg_0∈G` przy `t>0` zbliżają się do dowolnego x∈C, a ciągłość separatora przenosi nierówność na C. PASS.
9. **Podstawowe własności polary:** antymonotoniczność, równość `A°=(aco A)°`, inkluzja `A⊂A°°`, absolutna wypukłość i domkniętość polar w odpowiednich topologiach wynikają ze skończonych kombinacji liniowych oraz przecięć poziomic. PASS.
10. **Twierdzenie bipolarne:** dla `C=cl(aco A)` silna separacja punktu spoza C dostarcza `ell(x_0)>sup_C ell`; przez reprezentację `Re F` i zrównoważenie C uzyskuje się `sup_C|F|=sup_C Re F`. Normalizacja osobno przy `m>0` i `m=0` wyklucza x_0 z bipolaru. Przypadek A pustego wymaga jawnej konwencji `aco(∅)={0}`, która po poprawce jest spójna z opisem najmniejszości. PASS.
11. **Domknięcie wypukłego C w topologii słabej:** `sigma(X,X')` jest słabsza od wyjściowej; separator punktu `x_0` spoza domknięcia wyjściowego daje słabo otwartą półprzestrzeń rozłączną z C. **Poprawiono istotny brak jawnego założenia:** w zastosowaniu wyniku o oddzielaniu od domkniętego zbioru trzeba użyć `D=cl C` (domkniętego i wypukłego), a nie niekoniecznie domkniętego C. Po poprawce nierówność obejmuje `inf_D ell≤inf_C ell`, zatem wniosek wynika bez niejawnego zastosowania twierdzenia poza jego hipotezami. PASS po korekcie.

**Wszystkie 11 dowodów sprawdzono matematycznie; jeden wymagał doprecyzowania, dlatego audyt nie jest czysty.**

## Cztery przykłady — 4/4 PASS

1. **Separacja punktowa bez jednolitej luki:** na R, `A=(-1,0)`, `B={0}`, `ell(x)=x` ma ścisłą nierówność punktową, ale nie dodatni odstęp między supremum a infimum.
2. **Polara rombu `l¹` w R²:** polara kuli `l¹` jest kwadratem `l∞`. Tożsamość norm i diagram TikZ sprawdzono bez zmian.
3. **Polara wektorów bazowych w produkcie K^N:** polara ma skończony nośnik i współczynniki o module ≤1; bipolar to kula `l¹`, zaś domknięcie w topologii produktowej opisują obcięcia i ciągłość skończonych sum modułów.
4. **L^p dla 0<p<1:** na nieatomowej przestrzeni miary `X'={0}`; bipolar zbioru `{0}` jest całym X, choć domknięta otoczka absolutnie wypukła wynosi `{0}`. Kontrprzykład jest poprawny.

## Dodatkowa korekta definicji otoczki absolutnie wypukłej

W definicji `aco(A)` pojawia się explicite `aco(∅)={0}`, lecz wcześniejsze stwierdzenie „jest to najmniejszy zbiór wypukły i zrównoważony zawierający A” jest przy A=∅ nieprecyzyjne: warunki wypukłości i zrównoważenia są spełnione przez zbiór pusty w interpretacji uniwersalnej. Zmieniono tezę na **najmniejszy niepusty zbiór wypukły i zrównoważony zawierający A**. Uzasadniono, że każdy niepusty zbiór zrównoważony zawiera 0. Wartość `aco(∅)={0}` jest teraz spójna z własnością minimalności i przypadkiem brzegowym twierdzenia bipolarnego.

## Testy regresyjne, struktura i CI

- Rozszerzono `tools/tests/test_functional_analysis_ch07.py` z **16 do 20 testów**. Nowe kontrole obejmują: (i) jawne zastosowanie separacji do `D=cl C` i konkretny niedomknięty odcinek `C=(0,1)`; (ii) kompleksowy support na absolutnie wypukłej kuli ważonej `|z_1|+2|z_2|≤1` i obrót fazy; (iii) kompleksową wersję wzoru na bipolar zbioru bazowych wektorów produktu; (iv) konwencję `aco(∅)={0}` i bipolar pustego zbioru.
- Zachowano **11 par `proof`**, **4 pary `przyklad`**, **17 unikatowych etykiet** i diagram TikZ polary `l¹/l∞`. Dotychczasowe odsyłacze między rozdziałami pozostają niezmienione.
- Wprowadzone zmiany dotyczą wyłącznie istniejącego rozdziału 07 i jego testów. Żaden ze stabilnych rozdziałów 01–06 nie został zmodyfikowany.
- Dedykowany [GitHub Actions 45183998311](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45183998311) zakończył się **pełnym SUCCESS** dla aktualnego źródła i zestawu **20/20 testów PASS**. Kompilacja LaTeX dokumentu w kontekście 01–07, końcowa kontrola PDF i odsyłaczy oraz publikacja artefaktu przeszły wszystkie kroki.
- Pobrano **PDF A4, 43 strony, 556327 bajtów**, zgodny z tym SHA źródła. Wyrenderowano i wizualnie obejrzano strony **39–43** (cały rozdział 07), w tym poprawioną definicję otoczki absolutnie wypukłej i diagram polary rombu i kwadratu. **0 bloków tekstowych poza stroną**, brak nachodzących podpisów, ucięć i błędów typograficznych.
- Przejściowe ostrzeżenie o odsyłaczach wystąpiło jedynie po pierwszym przebiegu LaTeX; **końcowy log** nie zawiera `Undefined control sequence`, `There were undefined references`, `Overfull \\hbox` ani `Missing character`. Końcowy status workflow potwierdzony przez GitHub API.

## Decyzja

**NIE CZYSTY audyt 07/03: dwie poprawki źródła po 07/02, zatem 0/2.** Raport 07/02 na starszym SHA pozostaje w historii, ale jego czysty status nie przechodzi automatycznie na aktualną wersję. Następna iteracja: niezależny audyt **07/04**, dopiero po dwóch kolejnych czystych audytach można rozpocząć rozdział 08.
