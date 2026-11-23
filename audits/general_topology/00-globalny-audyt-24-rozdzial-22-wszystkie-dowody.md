# Topologia ogólna — audyt globalny 24: rozdział 22, wszystkie 11 dowodów

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Zakres:** wyłącznie istniejący rozdział 22, bez nowych twierdzeń i bez zmiany tekstu źródłowego.

**Źródło:** `chapters/pl/general_topology/22-zbieznosc-kuratowskiego-wijsman-attouch-wets.tex`, aktualny blob `33765c2bb1b3065f4ad32596795c3d1981b48dda`; **11 środowisk `proof`**. **Test:** `tools/tests/test_general_topology_ch22.py`, blob `b8814d252077582e800abf2681400c04105df414`. **Stan gałęzi przy początkowym odczycie:** `cf51277d78a2fe19bb70aaefe71ddf758eb35c67`. Raport lokalny `22-zbieznosc-zbiorow-iteracja-04.md` dokumentuje uprzednie 2+1 i kontrolę siedmiostronicowego PDF; nie liczymy go jako nowej kontroli.

## I. Niezależna kontrola dowód po dowodzie

1. **`prop:topog22-kuratowski-dist` — PASS.** Równoważność przecięcia kuli z warunkiem `d(x,F_n)<ε` daje dokładnie kwantyfikatory granicy dolnej (ostatecznie) i górnej (nieskończenie często). Z definicji wynika `Li⊆Ls`. Domkniętość obu granic udowodniono z punktów ich domknięć, używając dwóch połówek promienia; nie zakłada się domkniętości `F_n`. Przy pustych `F_n` konwencja odległości (+\infty) jest zgodna z definicją.

2. **`lem:topog22-distance-lipschitz` — PASS.** Nierówność `d(x,F)≤d(x,y)+d(y,F)` uzyskana przez infimum po niepustym `F` i jej symetryczna wersja dają 1-lipschitzowskość. Dla domkniętego `F` zbiór zerowy jest dokładnie `F`. Nie użyto niejawnej zwartości.

3. **`thm:topog22-wijsman-metrizable` — PASS.** Szereg ważony obciętych różnic jest metryką: dodatnia określoność wynika z gęstości przeliczalnego `D`, ciągłości funkcji odległości i ich zerowych zbiorów. Równość topologii, a nie tylko zbieżności ciągów, wynika z oszacowania `|d(x,A)-d(x,B)|≤2d(x,q_j)+|d(q_j,A)-d(q_j,B)|` i argumentu skończonej liczby współrzędnych oraz małego ogona. Przypadek skończonej niepustej przestrzeni jest obsłużony powtarzaniem `q_j`.

4. **`thm:topog22-wijsman-kuratowski` — PASS.** Punkt `x∈F` ma odległości do `F_n` zbieżne do zera, zatem `x∈Li`; dla `x∉F` domkniętość `F` daje dodatnią odległość, więc `x∉Ls`. Włączenia składają się do równości.

5. **`prop:topog22-wijsman-fell` — PASS.** Warunki trafiania otwartych zbiorów są otwarte w topologii Wijsmana. Przy omijaniu zwartego `C` dodatnie minimum `r=min_C d(x,F)` istnieje, bo `C` jest zwarty, a `F` domknięty i rozłączny. Skończone pokrycie `C` kulami promienia `r/4` i warunki `|d(x_i,G)-d(x_i,F)|<r/4` dają `d(y,G)>r/2` dla wszystkich `y∈C`. Działa bez lokalnej zwartości `X`.

6. **`thm:topog22-aw-metric` — PASS.** Dla `x` w kuli promienia `m` obie funkcje odległości są ograniczone przez `m+d(x_0,A)` i `m+d(x_0,B)`, więc `Δ_m` jest skończona mimo braku zwartości kul. Dodatnia określoność korzysta z pokrycia `X` kulami oraz zamkniętości zbiorów. Obcięcie i szereg zachowują nierówność trójkąta. Zbieżność w `ρ_AW` jest równoważna jednostajnej zbieżności funkcji odległości na każdym zbiorze ograniczonym, bo kule wokół dowolnego punktu bazowego są współkońcowe.

7. **`prop:topog22-aw-wijsman` — PASS.** Ewaluacja w każdym `x` jest ciągła w `AW`, gdyż `|d(x,A)-d(x,B)|≤Δ_m(A,B)` dla `m` z `x` w kuli. Z własności początkowej wynika inkluzja topologii; samo kryterium ciągowe nie było jedynym argumentem.

8. **`lem:topog22-equilipschitz` — PASS.** Granica punktowa funkcji 1-lipschitzowskich też jest 1-lipschitzowska. Skończona `ε/3`-sieć zwartego `K` i wspólny próg dla skończenie wielu punktów dają oszacowanie trzema składnikami, każdy mniejszy niż `ε/3`. Dla `K=∅` warunek jest pusty.

9. **`thm:topog22-proper-wijsman-aw` — PASS.** Zwarta kula w przestrzeni właściwej pozwala zastosować poprzedni argument do dowolnej **sieci**: skierowanie indeksów daje wspólny próg dla skończonej sieci `ε`-punktów. Dowodzi to ciągłości identyczności Wijsman→AW na poziomie topologii, a nie tylko ciągów.

10. **`thm:topog22-fell-kuratowski` — PASS.** Dla lokalnie zwartej metrycznej `X` (Hausdorffa) każdy punkt poza domkniętym `F` ma otoczenie o zwartym domknięciu rozłącznym z `F`; warunek omijania zwartego zbioru wyklucza `Ls` poza `F`. Odwrotnie `Li` wymusza ostateczne trafianie otwartych; gdyby nieskończenie wiele `F_n` trafiało zwarty `C` rozłączny z `F`, punkty z tych przecięć miałyby zbieżny podciąg, którego granica należałaby do `Ls=F` — sprzeczność. Dowód poprawnie dopuszcza `F=∅` i puste wyrazy ciągu.

11. **`thm:topog22-proper-equivalences` — PASS.** Właściwość daje lokalną zwartość i równoważność Kuratowski↔Fell; Wijsman↔AW udowodniono już dla topologii. Brakujący kierunek Kuratowski→Wijsman: dla `r=d(x,F)` punkty `z∈F` o `d(x,z)<r+ε` i `z∈Li` dają `limsup d(x,F_n)≤r`. Jeśli `r>0` i `liminf<r`, wybór punktów `z_k∈F_{n_k}` w zwartej kuli `\overline B(x,r)` z `d(x,z_k)<r-η/2` prowadzi do punktu `z∈Ls=F` o odległości mniejszej od `r` — sprzeczność. Dla `r=0` wystarcza nieujemność. Istotne są niepustość `F` oraz zwartość **domkniętych** kul.

## II. Definicje, przykłady, kontrprzykłady, terminologia

- **Definicje:** `Li/Ls` obejmują zbiory puste; Wijsman i AW są zdefiniowane na niepustych domkniętych `\mathcal F_*(X)`. Rozdzielenie konwencji `d(x,∅)=+∞` od funkcji odległości o skończonych wartościach jest poprawne. Właściwa przestrzeń metryczna ma zwarte kule domknięte, nie tylko kule ograniczone.
- **Oscylacja:** `F_{2n}={0}, F_{2n-1}={1}` daje `Li=∅`, `Ls={0,1}`.
- **Ucieczka punktu:** `F_n={0,n}` w `\mathbb R` ma granicę Kuratowskiego `{0}` i `d_H(F_n,{0})=n`; na ustalonej kuli `[-m,m]` dla `n>2m` funkcje odległości są identyczne, co daje zbieżność AW.
- **Ścisłość AW/Wijsman:** w nieprzeliczalności nie ma potrzeby — na przeliczalnej, ograniczonej, dyskretnej przestrzeni `X=\mathbb N` z `F_n=X\setminus{n}` i `F=X` odległości zbieżne są punktowo, lecz supremum po ograniczonym `X` jest zawsze 1.
- **Lokalna zwartość nie wystarcza:** w dyskretnej przestrzeni `{p,q}∪{y_n}`, gdzie `d(p,q)=2`, pozostałe odległości różnych punktów są 1, `F_n={p,y_n}` zbiega Kuratowskiego/Fella do `{p}`, ale `d(q,F_n)=1\ne2=d(q,{p})`; przestrzeń jest zupełna, ośrodkowa, lokalnie zwarta i niewłaściwa.
- **Rysunek:** jeden TikZ `fig:topog22-escape`, poprzedni raport lokalny 22/04 dokumentuje rzeczywiste obejrzenie siedmiu stron samodzielnego PDF. **Nie wykonywano w tej iteracji nowego renderingu ani inspekcji obrazu**.
- **Terminologia:** w źródle występuje prawidłowe „zbieżność jednostajna ... na zbiorach ograniczonych”, „zbieżność w sensie Kuratowskiego”, „topologia Fella”, „przestrzeń metryczna właściwa”. W aktualnym teście są asercje zakazujące „zwartościowanie”, „zbieżność zwarta”, błędnych skrótów aksjomatów przeliczalności. Samo odczytanie testu nie jest jego lokalnym uruchomieniem.

## III. Dowody techniczne i ograniczenia

- Odczytano bieżącą gałąź, rejestr raportów globalnych 01–23 i lokalnych 22/01–04. Globalne 17 zamknęło kontrolę matematyczną rozdziału 03 na blobie `b571753b5ab9a8777424fc32f6c4a54a4048af77`; **ponowny odczyt aktualnego źródła 03 potwierdza dokładnie ten sam blob**. Nie dublowano audytu 03.
- Odczytano aktualny rozdział 13: blob `c9078636452731e42a56196e84b5ed9831120e6b`, **9 dowodów**. Raport globalny 07 dotyczy bloba `33200912c034f3f946909f00b9e4068deeca4ed0`; **różnica pozostaje otwarta** i wymaga porównania zmian przed przeniesieniem werdyktu.
- Odczytano aktualny test regresyjny 22, zawierający modele skończonych granic Kuratowskiego, odległości, kontrprzykłady Wijsman/AW, kontrolę metryki kontrprzykładu niewłaściwego oraz sprawdzenie katalogu, odsyłaczy i terminologii.
- **CI:** [45093113653](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45093113653), commit `296a15693c98a822d8d9bd9deea5d566a92b1699`, ma status **completed/success**. Tak samo [45087418332](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45087418332) i [45084687504](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45084687504). Lokalny raport 22/04 wskazuje [45047380847](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047380847) jako sukces na tym samym blobie 22, z kompilacją całej książki, osobnego rozdziału i oględzinami siedmiu stron. **Nie wykonano nowej lokalnej kompilacji ani nowych oględzin PDF w tej iteracji**; nowy CI dla commitu raportowego wymaga osobnego potwierdzenia.
- Stan licznika ilustracji: raport globalny 14 potwierdza **27/27 rysunków** w pełnym wydaniu 188 stron (zakres 01–26), a raport globalny 23 przywołuje **281 dowodów i 24 ilustracje** w innym zakresie 01–23. Te liczby mają różne zakresy i **nie należy ich utożsamiać** bez przeliczenia bieżących źródeł.

## IV. Werdykt i następny krok

**PASS matematyczny — 11/11 dowodów rozdziału 22** na aktualnym blobie, wraz z kontrolą definicji, przykładów, kontrprzykładów, hipotez, terminologii i odsyłaczy w źródle. Wcześniejsze lokalne audyty 22/02–04 dokumentują 2+1, a CI na tym samym źródle — testy i skład; raport 24 jest dodatkową niezależną kontrolą globalną, nie zastępuje nowych testów. Źródła nie zmieniano.

**Otwarte:** niezależny globalny audyt wszystkich dowodów rozdziału 23; rozstrzygnięcie rozbieżności źródła 13; aktualny rejestr 01–23 (dowody, twierdzenia, definicje, przykłady, ilustracje, odsyłacze); końcowy audyt całego wydania i dodatkowy audyt potwierdzający; końcowy CI. **Następna iteracja:** rozdział 23. Nie wyłączać automatyzacji, dopóki wszystkie kontrole nie będą rzeczywiście zamknięte.
