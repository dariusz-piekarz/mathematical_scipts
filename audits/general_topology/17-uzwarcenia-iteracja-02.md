# Topologia ogólna — rozdział 17, audyt iteracja 02

Data: 2026-11-22. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Źródło: `chapters/pl/general_topology/17-uzwarcenia-aleksandrowa-i-cecha-stonea.tex`.

## Niezależna ponowna kontrola matematyczna

Zbadano wszystkie konstrukcje, założenia twierdzeń, dowody i przykłady rozdziału 17, po audycie 01. Audyt objął zarówno poprawność, jak i szczegółowość kroków, precyzję oznaczeń i odsyłaczy.

1. **Topologia konstrukcji Aleksandrowa:** wszystkie zbiory otwarte zawierające dodany punkt mają postać `X*\setminus C`, gdzie `C⊂X` jest zwarty. Skończone przecięcia odpowiadają skończonym sumom zwartych zbiorów, a dowolne sumy — przecięciom zwartych zbiorów. W przestrzeni Hausdorffa zbiory zwarte są domknięte; przecięcie niepustej rodziny zwartych zbiorów jest domkniętym podzbiorem wybranego jednego z nich, więc jest zwarte. Zbiory mieszane są kontrolowane przez `C\setminus U`. Konstrukcja jest topologią.
2. **Zwartość i gęstość:** pokrycie otwarte `X*` zawiera otoczenie dodanego punktu; poza nim pozostaje zbiór zwarty, pokrywany skończoną podrodziną. Warunek niezwartości `X` zapewnia gęstość `X` w `X*`; gdyby dodany punkt był izolowany, `X` byłaby zwarta.
3. **Kryterium Hausdorffa:** przy lokalnej zwartości rozdziela się `x∈X` i `∞` przez otwarty zbiór `U` o zwartym domknięciu i jego dopełnienie w `X*`. W drugą stronę `X` jest otwartą podprzestrzenią zwartej przestrzeni Hausdorffa, więc lokalnie zwarta. Odpowiednie wyniki rozdziału 14 są już udowodnione.
4. **Odwzorowania właściwe:** dla niezwartych lokalnie zwartych przestrzeni Hausdorffa `X,Y` przedłużenie `f*:X*→Y*`, z `f*(∞_X)=∞_Y`, jest ciągłe dokładnie wtedy, gdy preobrazy zwartych zbiorów `C⊂Y` są zwarte w `X`. Warunki te są równoważne kontroli przeciwobrazów wszystkich otoczeń dodanego punktu.
5. **Minimalność:** dla uzwarcenia Hausdorffa `(K,e)` zbiór `e(X)` jest otwarty w `K`, bo każdy punkt ma otwarte otoczenie `O` zawarte w zwartym, a więc domkniętym obrazie zwartego otoczenia z `X`. Zatem reszta `F=K\setminus e(X)` jest niepusta i zwarta. Zwijając `F` do `∞` uzyskuje się ciągłe, zgodne z zanurzeniami, surjektywne odwzorowanie `K→X*`; jednoznaczność wynika z gęstości i Hausdorffowości celu. Przy reszcie jednopunktowej jest to homeomorfizm.
6. **Przykład prostej i okręgu:** zanurzenie `e(t)=exp(i(2 arctan t+π))` jest homeomorfizmem `R→S¹\setminus{1}`. W trakcie audytu szczegółowo rozpisano ciągłość jego przedłużenia w `∞`: obie granice `2 arctan t` przy `±∞` dają `±π`, dlatego `e(t)→1`; dla otoczenia `V` punktu `1` istnieje `M` z `X*\setminus[-M,M]⊂\widetilde e^{-1}(V)`. To wprost wykazuje ciągłość w nowym punkcie, poza nim wynika z ciągłości `e`.
7. **Lokalnie zwarta przestrzeń Hausdorffa jest Tychonoffa:** dowód używa zwartego domknięcia `C` otoczenia punktu, lematu Urysohna w `C` i sklejania funkcji na dwóch domkniętych podzbiorach `C` i `X\setminus W`. Poprawność dla domkniętego `F` i `x∉F` sprawdzona; całkowita regularność i T₁ są uzyskane jawnie.
8. **Konstrukcja Čecha–Stone’a:** `I=C(X,[0,1])` oraz `βX=cl(e_X(X))` w zwartej kostce. Dla `f:X→L`, z `L` zwartą Hausdorffa, oraz `J=C(L,[0,1])` definiuje się `Φ(z)_g=z_{g∘f}`. Jest ciągłe współrzędnie i trafia do domkniętego `e_L(L)` przez gęstość `e_X(X)`; `e_L^{-1}∘Φ` jest jednoznacznym ciągłym przedłużeniem.
9. **Przedłużanie funkcji ograniczonych:** zakres `f(X)` zawiera się w zwartym przedziale `[a,b]`, dla którego działa własność uniwersalna. Jednoznaczność przedłużenia o wartościach rzeczywistych wynika z gęstości i Hausdorffowości `R`.
10. **Maksymalność:** każdy `(K,e)` jest obrazem `βX` przez jedyny zgodny ciągły czynnik `p`. Kiedy każda funkcja `f:X→[0,1]` przedłuża się do `F_f:K→[0,1]`, dla **jawnie zdefiniowanego rzutowania** `π_f:[0,1]^I→[0,1]` zachodzi `F_f∘p=π_f|_{βX}` na mocy zgodności na gęstym `e_X(X)`. Rozdzielenie współrzędnych daje iniektywność `p`; zwartość i Hausdorffowość — homeomorfizm. W audycie 02 doprecyzowano oznaczenie `π_f`, wcześniej użyte bez definicji.
11. **Porównanie i przykład dyskretnej N:** `X*` jest najmniejszym, a `βX` największym uzwarceniem niezwartych lokalnie zwartych Hausdorffa `X`. W przykładzie dyskretnej `N` dopisano jawne odwołanie do wniosku o jednoznaczności uzwarcenia jednopunktowego. Naprzemienna funkcja ograniczona nie przedłuża się do `X*`, ale przedłuża się do `βN`, co rozróżnia te uzwarcenia.
12. **Język i terminologia:** zachowano nazwy „uzwarcenie Aleksandrowa” i „uzwarcenie Čecha–Stone’a”; nie użyto „zwartościowania” ani innych niedopuszczonych zamienników. Twierdzenia formułują jawnie przestrzenie, mapy i hipotezy.

## Poprawki w audycie 02

- `db5f9c59ca0cedbc902ea6f6bced6dce3ef3558e`: rozpisanie ciągłości w nieskończoności w przykładzie prostej, zdefiniowanie rzutowań `π_f` w maksymalności oraz jawne użycie wniosku o jednoznaczności uzwarcenia jednopunktowego.
- `072227ab784baa46f64a5b6fcfaa86ccf8473254`: rozszerzenie testu regresyjnego o istotne fragmenty tych rozumowań.

## Walidacja

Przed korektą źródło przeszło workflow [45013696240](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013696240): `completed/success`, samodzielny PDF 5 stron A4, bez ostrzeżeń i przepełnień. Po korektach uruchomiono [workflow 45014196221](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014196221) (commit `072227ab784baa46f64a5b6fcfaa86ccf8473254`), który zakończył się **completed/success**, bez nieudanych kroków. Pobrano artefakt `14751178008` zawierający aktualny samodzielny `general_topology_ch17.pdf` (**5 stron A4**) i logi. Skontrolowano `general_topology_ch17.log` oraz `general_topology.log`: brak `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence` i `Fatal error`. Wyrenderowano i obejrzano wszystkie pięć stron PDF; brak ucięć, kolizji wzorów oraz nieczytelnych fragmentów. Ostatnia strona jest krótsza, co nie stanowi usterki składu.

| Warstwa | Status |
| --- | --- |
| Dowody obu konstrukcji | PASS — audyt 02 |
| Własności uniwersalne i porządek uzwarceń | PASS po doprecyzowaniach |
| Przykłady, przypadki brzegowe | PASS po doprecyzowaniach |
| Język, etykiety i odsyłacze | PASS |
| CI i PDF dla poprawionego źródła | **PASS — run 45014196221, 5 stron A4** |
| Stabilizacja | **W AUDYCIE** — audyt 02 zakończony, po poprawkach wymagana niezależna czysta iteracja 03 |
