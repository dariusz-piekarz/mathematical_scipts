# Topologia ogólna — audyt globalny 43: 17 krytycznych dowodów rozdziałów 10, 11, 12, 16, 18 i 19

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Wspólny odczyt:** commit `b375511f954f6c6bffdbda2de569bcee50e5a1aa`.

**Aktualne niezmienione bloby rozdziałów:** 10 — `1bc0fb72953cb70bcec7c60d3c2fc222ba1851c6`; 11 — `8f13420add065dca19d2653c86b0e5781aef2fe7`; 12 — `13597073db07742089b82ae3fc9878733dea5e88`; 16 — `1c2fcb925d62120feaea468400e48842a508a062`; 18 — `f7340514548ed3dfb5d98793bf7068fd84276c30`; 19 — `dd05dd723a4e92756d1e339309079c68a4580485`.

**Cel:** przeprowadzić kolejną rzeczywistą, niezależną próbę wykrycia błędów w hipotezach i złożonych dowodach, których nie weryfikują testy CI. Bez ponownego naliczania raportów wcześniejszych jako nowych audytów. W tym przebiegu skontrolowano **17 konkretnych środowisk `proof`**, wraz z definicjami i otaczającymi wynikami; **nie** ogłaszamy, że ponownie przeczytano wszystkie 325 dowodów.

## I. Rozdział 10 — metryzowalność (3 proof)

**10-06, `lem:topog-t3-lindelof-normalna`, linie 197–237 — PASS.** Dla rozłącznych domkniętych F,G z regularności otrzymuje się lokalnie otwarte U_x z `cl U_x ∩ G=∅` oraz V_y z `cl V_y ∩ F=∅`. Lindelöfowość obu domkniętych podprzestrzeni zapewnia podpokrycia przeliczalne; zbiory `U=⋃_n(U_n\⋃_{k≤n}cl V_k)` i `V=⋃_m(V_m\⋃_{k≤m}cl U_k)` są otwarte i rozłączne. Przy n≤m druga część wyklucza domknięcie U_n, przy m≤n pierwsza wyklucza domknięcie V_m. Przypadki zbiorów pustych są obsłużone, nie użyto niewypowiedzianego T1 do samego rozdzielenia dwóch domkniętych.

**10-08, `thm:topog-urysohn-metryzowalnosc`, linie 261–399 — PASS.** Dla dowolnego `x∈O` konstrukcja bazowych B,C spełnia `x∈B⊂cl B⊂C⊂O`. Dzięki T1 wybór `O=X\{y}` umożliwia rozdzielenie dwóch punktów funkcją f_{B,C}. Suma `d(x,y)=∑2^{-n}|f_n(x)-f_n(y)|` jest metryką, a obie inkluzje topologii są osobno udowodnione: (a) małe wartości skończonej liczby funkcji i ogon szeregu dowodzą otwartości kul d, (b) pojedyncza funkcja f_n równa 0 w x i 1 na X\O daje `B_d(x,2^{-n})⊂O`. Przypadki pustej i jednoelementowej przestrzeni rozpatrzono odrębnie; nie zakłada się metryzowalności przed konstrukcją.

**10-12, `thm:topog-przeliczalny-iloczyn-metryzowalny`, linie 518–569 — PASS.** Zastosowanie metryk ograniczonych `min(1,d_n)` zapewnia zbieżność szeregu oraz nierówność trójkąta; kontrola współrzędnych w skończonym zbiorze F i ogona daje dokładnie topologię produktu. Gdy F jest pusty, dowód wybiera dowolny promień; gdy któryś X_n jest pusty, osobno obsługuje pusty produkt. Należy odróżnić `min(1,d_n)<δ_n<1` od nieprawdziwego wniosku `d_n<δ_n` bez ograniczenia δ_n<1; tekst zawiera to ograniczenie.

## II. Rozdział 11 — zupełność i Baire (3 proof)

**11-04, `thm:topog-baire-metryczne`, linie 186–218 — PASS.** Z niepustego otwartego U wybiera się domkniętą kulę K_1 zawartą w `U∩G_1`; w kolejnym kroku `K_{n+1}⊂B(x_n,r_n)∩G_{n+1}`. Malejące promienie `r_n<2^{-n}` dają Cauchy'ego środków, a domkniętość K_n zapewnia przynależność granicy do każdego K_n. Nie użyto zwartości domkniętych kul w dowolnej przestrzeni metrycznej, co byłoby błędem.

**11-06, `thm:topog-baire-wymierne-nie-gdelta`, linie 267–285 — PASS.** Gdyby Q było przecięciem otwartych U_n, wszystkie U_n byłyby gęste; dołączenie `V_n=R\{q_n}` daje przeliczalną rodzinę otwartych gęstych zbiorów o pustym przecięciu, sprzecznie z twierdzeniem Baire'a dla R. Rozróżniono gęstość i miarę.

**11-07, `prop:topog-baire-otwarte-podprzestrzenie`, linie 301–326 — PASS.** Dla otwartego U⊂X, gęstych otwartych H_n⊂U, zbiory `G_n=H_n∪(X\cl_X U)` są otwarte i gęste w X, ponieważ `cl_X H_n⊇cl_X U`, zaś `cl_X(X\cl_X U)` pokrywa pozostałą część. Na V⊂U mamy `G_n∩U=H_n`, zatem zastosowanie Baire'a w X naprawdę daje Baire'a w U; **nie** wymaga się zupełności dowolnej podprzestrzeni otwartej w danej metryce.

## III. Rozdział 12 — przestrzenie jednostajne (3 proof)

**12-03, `thm:topog-jednostajne-hausdorff`, linie 146–167 — PASS.** Równoważność rozdzielania i `∩_{E∈𝒰}E=Δ_X` jest poprawna, także gdy relacje bazowe nie są symetryczne. W kierunku od przekątnej wybiera się symetryczne F z `F∘F⊂E`; wówczas wspólny punkt `F[x]∩F[y]` implikowałby `(x,y)∈E`. Przekroje nie muszą być otwarte, ale zawierają otwarte otoczenia dzięki wcześniejszemu lematowi.

**12-07, `thm:topog-jednostajne-iloczyn`, linie 323–368 — PASS.** Dla produktu istotne są relacje narzucające warunki tylko na skończenie wielu współrzędnych; przecięcie relacji bazowych bierze sumę ich nośników. Skończoność F zapewnia wspólny warunek składania. Pusty indeks i pusty czynnik są osobno rozważone, bez nieuprawnionego założenia istnienia punktu bazowego w produkcie.

**12-12, `thm:topog-jednostajne-zbiezna-cauchy`, linie 549–563 — PASS.** Dla zbieżnej sieci do x i symetrycznej relacji F z `F∘F⊂E` w ogonie mamy `(x_α,x),(x,x_β)∈F`; stąd pary ogonowe należą do E. Symetria F jest konieczna do właściwej orientacji pierwszej relacji. Dowód działa także bez Hausdorffowości.

## IV. Rozdział 16 — wprowadzenie do uzwarceń (3 proof)

**16-03, `thm:topog-uzwarcenia-funkcyjny-opis`, linie 77–127 — PASS.** Całkowita regularność wraz z T1 daje funkcje rozdzielające punkty od zbiorów domkniętych; odwrotnie topologia początkowa wszystkich funkcji X→[0,1] pozwala wybrać skończenie wiele funkcji z bazowego otoczenia i skonstruować maksimum funkcji oddzielających x od dopełnień otwartych V_j. Przypadek `F=∅` rozpatrzony oddzielnie; warunku T1 nie użyto bez wyraźnego wskazania.

**16-04, `thm:topog-uzwarcenia-istnienie`, linie 173–200 — PASS.** Każde uzwarcenie Hausdorffa osadza X w zwartej przestrzeni Tychonoffa, więc X jest Tychonoffa. W przeciwną stronę zanurzenie w kostkę, zwartość jej na mocy Tychonoffa i domknięcie obrazu tworzą uzwarcenie. Rozróżniono istnienie od jednoznaczności uzwarcenia.

**16-07, `prop:topog-uzwarcenia-porzadek-klasy`, linie 282–329 — PASS.** Mapę p:K_1→K_2 zgodną z zanurzeniami wyznacza gęsta podprzestrzeń e_1(X), a jej obraz jest zwarty, domknięty w K_2 i zawiera gęsty e_2(X), więc p jest surjektywna. Mapy w obu kierunkach dają identyczności przez jednoznaczność przedłużenia, stąd równoważność uzwarceń i antysymetria porządku na klasach.

## V. Rozdział 18 — topologie na funkcjach (3 proof)

**18-04, `thm:topog-odwzorowania-zwarto-otwarta-jednostajna`, linie 180–258 — PASS.** Dla dowolnej topologicznej X, niekoniecznie Hausdorffa, i metrycznej Y, obrazy f(K) są zwarte; dodatnie minimum odległości od domkniętego `Y\U` zapewnia otwartość [K,U] w topologii zbieżności jednostajnej na zbiorach zwartych. Odwrotnie zwarte `K_j=K∩g^{-1}(cl B(y_j,δ/4))` pokrywają K; są zwarte jako domknięte w zwartym K **także bez Hausdorffowości K**. Otoczenie `⋂[K_j,B(y_j,δ/2)]` mieści się w `B_K(f,ε)` przez `m+3δ/4<ε`. Wniosek nie wymaga lokalnej zwartości X.

**18-07, `thm:topog-odwzorowania-wykladnicze`, linie 367–409 — PASS.** Kierunek F ciągłe ⇒ `hat F` ciągłe korzysta z *lematu o rurze* i zwartości K, nie z lokalnej zwartości X. Kierunek odwrotny wymaga ciągłości ewaluacji `C_k(X,Y)×X→Y`, a ta została osobno wykazana z założenia lokalnej zwartości Hausdorffowej X. Konieczne jest rozdzielenie tych dwóch kierunków i zostało zachowane.

**18-09, `thm:topog-odwzorowania-zupelnosc`, linie 549–593 — PASS.** Cauchy'ego w metryce D implikuje jednostajną własność Cauchy'ego na każdym zwartym K_n; zupełność Y daje punktową granicę f, a ilościowe oszacowanie jednostajne na K_n daje ciągłość f wokół każdego x, ponieważ `X=⋃ int K_n`. Następnie poprzednie twierdzenie o metryce wyczerpania daje `D(f_j,f)→0`. Nie utożsamia się samej punktowej zbieżności z ciągłością.

## VI. Rozdział 19 — przestrzenie polskie i rangi borelowskie (2 proof)

**19-04, `thm:topog-polskie-gdelta`, linie 272–448 — PASS.** Dla A=∩U_n konstrukcja `h_n(x)=1/d(x,X\U_n)` na A i metryki `ρ=d+∑2^{-n}min(1,|h_n(x)-h_n(y)|)` zapewnia zgodność topologii i zupełność. Każdy ρ-Cauchy musi mieć d-granicę w X; gdyby granica należała do X\U_n, wartości h_n dążyłyby do ∞, przecząc własności Cauchy'ego w R. W kierunku odwrotnym przy zupełnej metryce σ na A małe d-kule o σ-średnicy <2^{-n} i dobór a_n blisko dowolnego x∈∩V_n dają σ-Cauchy'ego, więc x należy do A. Nie korzystano z domkniętości A w X.

**19-09, `thm:topog-polskie-borel-wyczerpanie`, linie 819–875 — PASS.** Każdy poziom Σ^0_α zawiera się w σ-algebrze borelowskiej. Klasa `𝒞=⋃_{α<ω₁}Σ^0_α` jest zamknięta na dopełnienia przez przejście do α+1. Dla przeliczalnej rodziny A_n o rangach α_n wybór `γ=sup_n(α_n+2)` daje przeliczalną liczbę porządkową i wszystkie A_n należą do poziomów Π^0_{β_n} z β_n<γ. W ten sposób `⋃ A_n∈Σ^0_γ`. Argument nie wymaga ośrodkowości X; istotne jest, że do utworzenia każdego zbioru borelowskiego używa się przeliczalnie wielu operacji na wcześniejszych poziomach.

## VII. Zależności, CI, decyzja

Kontrolowane argumenty mają spójny, niekołowy łańcuch zależności:
- rozdział **05** (regularność, lemat Urysohna) → **10** (metryzowalność) → **11** (zupełność, Baire) → **12** (struktury jednostajne);
- rozdział **07** (Tychonoff i zanurzenie w kostkę) → **16** (ogólna teoria uzwarceń) → **17** (konkretne uzwarcenia);
- rozdział **14** (zwartość lokalna i wyczerpanie) + **11** (zupełność metryczna) → **18** (ewaluacja, prawo wykładnicze, zupełność C_k);
- rozdziały **09–11** (metryzowalność, separowalność, Baire) → **19** (przestrzenie polskie, hierarchia borelowska).

**CI po audycie 42:** sprawdzone faktyczne `completed/success`:
[45135952737](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45135952737) oraz [45136010320](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136010320). Nie są to dowody matematyczne; nowy CI po zapisaniu raportu 43 wymaga odrębnego sprawdzenia.

**Werdykt:** **PASS 17/17 selektywnie wybranych dowodów, 0 nowych usterek wymagających zmian źródeł**. Nie zmieniono plików LaTeX ani testów. Nie uznajemy automatycznie całego globalnego audytu 325 dowodów za zakończony. Kolejne ryzyka: kontrola pozostałych twierdzeń z rozdziałów 01–09 i 13–15, formalna ocena zależności od zewnętrznego twierdzenia Brouwera, ostatni CI HEAD i końcowy audyt redakcyjny.
