# Geometria algebraiczna — audyt globalny IV (niezależny audyt dla pewności, 2026-11-22)

## Niezmienione źródła i metoda

Po bezusterkowym globalnym III ponownie sprawdzono aktualne drzewo Git: wszystkie **11 kanonicznych blobów ALG-00–ALG-10** i historyczny monolit są niezmienione. W szczególności ALG-03 = `a8dfcc00dbc84fb2e893d44f3bc3ace86e27a886`, ALG-04 = `ab1344ed93a02bb757e5a78cb3833d6c4a18079c`, ALG-10 = `5b231c9b40ad7f547ccfb3050e3712b7be7a75b0`, monolit = `6c5ae2c7d971b0c4574e6bd5c6cf3b86b5f28880`. Ten raport jest osobnym przeglądem wybranych zagadnień matematycznych i rysunków, a nie powtórzeniem samych obliczeń z audytu III.

## Wyrywkowa niezależna kontrola dowodów i przykładów

1. **Rozdmuchanie punktu (ALG-05 i moduł współdzielony).** Dwie mapy `y=xv` i `x=uy` z relacją `uv=1` rzeczywiście opisują rozdmuchanie płaszczyzny i poprawnie sklejają dzielnik wyjątkowy `E ≅ P¹`. Dla ostrza `y²=x³` po podstawieniu `y=xv` otrzymuje się `x²(v²−x)`; transformata ścisła jest gładka, przy czym nie należy mylić tego z automatycznym uzyskaniem normalnego przecinania transformanty z `E`. Normalna dzielnika wyjątkowego to `O_{P¹}(-1)`, zatem `E²=−1`.
2. **27 prostych (ALG-06).** Niezależnie wygenerowano dokładnie `6+15+6=27` różnych klas: `E_i`, `H−E_i−E_j` dla `i<j` oraz `2H−∑_{j≠i}E_j`. Wszystkie spełniają `C²=−1` i `(−K)·C=1`. Odwołanie do klasyfikacji powierzchni kubicznych jako rozdmuchań sześciu punktów jest jawnie oznaczone jako wynik zewnętrzny, nie udawany dowód z rachunków.
3. **Przekształcenie Cremony (ALG-08).** Na `xyz≠0` wzór `[x:y:z]↦[yz:xz:xy]` jest inwolucją; niezależny rachunek na **1000** trójkach niezerowych współrzędnych całkowitych potwierdził wynik po uwzględnieniu wspólnego czynnika rzutowego. Graf sześciu krzywych, ich wzajemne przecięcia oraz układ `2H−E_1−E_2−E_3` mają zgodne znaki.
4. **Wiązki `O(n)` na `P¹` (ALG-04 i ALG-09).** Dla wszystkich **2001** stopni `n∈[-1000,1000]` porównano liczbę niewyeliminowanych potęg Laurenta `n<j<0`, wymiar `h¹=max(−n−1,0)`, `h⁰=max(n+1,0)` i równość `h⁰−h¹=n+1`. Zweryfikowano, że twierdzenie Cartana B i GAGA nie są przedstawione jako elementarne fakty już dowiedzione w książce.
5. **Kubika węzłowa i cykl zanikający (ALG-10).** Dla **440** par całkowitych `(S,T)≠(0,0)` zweryfikowano bez wspólnych zer współrzędnych i równanie kubiki dla `[T(S²−T²):S(S²−T²):T³]`. Dla `S=±T` otrzymuje się ten sam węzeł, zgodnie z opisem normalizacji. Dla `uv=t`, `2|t|<ε²` gwarantuje dwa dodatnie promienie lokalnego pierścienia; rysunek jest świadomie schematem topologicznym, nie obrazem czterowymiarowego włókna.
6. **Status hipotez.** Reread twierdzeń GAGA, Chowa, Hodge'a, Kodairy i słabego/twardego Lefschetza: w sprawdzonych zastosowaniach zachowano właściwość/rzutowość, gładkość, zwartość i odpowiednie zakresy stopni. Hipoteza Hodge'a w kowymiarze większym niż jeden pozostaje określona jako otwarta.

## Regresja redakcyjna i skład

Potwierdzono sprostowanie z globalnego III: **„dywizor” i „dzielnik” są dopuszczalnymi określeniami**, w żadnym rozdziale nie trzeba przeprowadzać wymuszonej migracji. ALG-03/04 zachowują własną poprawną terminologię; dawne zalecenie migracji z globalnego II zostaje anulowane. Źródła nie były edytowane.

Podtrzymany odbiór obu aktualnych 184-stronicowych PDF: **184/184** stron zgodne tekstowo i pikselowo przy porównaniu rastrowym, **0** wykrytych bloków poza stronami, końcowe logi bez `LaTeX Warning`, `Overfull`, `Underfull`, `LaTeX Error` i niezdefiniowanych referencji. W osobnym wizualnym przeglądzie stron PDF 92, 154, 157, 175, 179, 182 i 184 sprawdzono rozmieszczenie rozdziałów, podpisów i diagramów; nie znaleziono widocznych kolizji. Skrypt regresyjny w workflow ma **187 zaliczonych testów** na tym niezmienionym zestawie źródeł, zgodnie z [CI 45069448058](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45069448058).

## Decyzja

**GLOBALNY IV: PASS — dodatkowy niezależny audyt bez nowych usterek. GLOBALNY AUDYT ALG-00–ALG-10: STABILNY / ZAMKNIĘTY w zakresie przyjętego planu i sprawdzonych materiałów.** Globalne audyty III i IV dotyczyły tych samych niezmienionych źródeł po zamknięciu ALG-10/IX. Własne obliczenia skończone i testy regresyjne nie zastępują dowodów twierdzeń głębokich ani pełnej formalizacji. Kolejne prace mogą dotyczyć planowych uzupełnień merytorycznych lub niezależnych kontroli przekrojowych; nie ma otwartego zadania wymiany słowa „dywizor”.
