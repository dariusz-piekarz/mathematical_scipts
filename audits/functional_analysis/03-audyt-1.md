# Analiza funkcjonalna — rozdział 03 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/03-sieci-struktura-jednostajna-i-zupelnosc.tex`.  
**Status:** audyt z poprawkami; **NIEUSTABILIZOWANY**. Nie liczy się jako czysty audyt.

## Metoda

Niezależna kontrola wszystkich 9 dowodów i 3 środowisk przykładów, w tym definicji, domknięć i granic sieci, relacji sieci–filtry, kanonicznej struktury jednostajnej, Cauchy'ego i zupełności, odmienności zupełności ciągowej i sieciowej, konstrukcji uzupełnienia przez klasy sieci Cauchy'ego oraz jego własności uniwersalnej. Osobno kontrola symboli, założeń Hausdorffa, przypadków z indeksami nieprzeliczalnymi, poprawności słownictwa i LaTeX.

## Rejestr dziewięciu dowodów

1. **Domknięcie i ciągłość przez sieci:** rodzina otwartych otoczeń punktu skierowana odwrotną inkluzją; wybory `a_U∈A∩U`; konstrukcja sieci świadczącej o nieciągłości w danym punkcie. **PASS**.
2. **Kanoniczna struktura jednostajna:** przekątna, przecięcia, symetryczne odwrotności i składanie `E_V∘E_V⊆E_U`; `E_U[x]=x-U` odtwarza topologię, także przy nieotwartych U. **PASS**.
3. **Ciągłość liniowa implikuje jednostajną:** `T(x)-T(y)=T(x-y)` i kryterium ciągłości w zerze. **PASS**.
4. **Równoważność opisu sieciowego i filtrowego:** ogony sieci, filtr generowany ogonami, sieć indeksowana parami `(A,a)` z `A∈F, a∈A`, relacja odwrotnej inkluzji; kompletność poprzez zbieżność takiej sieci. **PASS**.
5. **Granice i jednoznaczność:** sieć zbieżna jest Cauchy'ego; jednoznaczność w przestrzeni Hausdorffa; sieć Cauchy'ego z podsiecią zbieżną zbiega do tej samej granicy. **PASS**.
6. **Zupełność ciągowa w metryzowalnych TVS:** konstrukcja malejącej bazy otoczeń zera, monotonicznych indeksów `e_n`, ciągu Cauchy'ego i przejście z granicy wybranych wyrazów do oryginalnej sieci. **PASS**.
7. **Podprzestrzenie i produkty zupełne:** domknięta podprzestrzeń przestrzeni zupełnej jest zupełna; zupełna podprzestrzeń przestrzeni Hausdorffa jest domknięta; zupełność produktu równoważna zupełności jego współrzędnych. **PASS**.
8. **Istnienie i uniwersalna własność uzupełnienia:** konstrukcja ustalonego zbioru indeksów `D_*` eliminuje problem klas właściwych; relacja równoważności sieci Cauchy'ego i działania liniowe; zbiory `Û` z zapasem otoczenia do brzegu; gęstość `j(X)`, ciągłość działań, zupełność i przedłużanie operatorów. **PASS po korekcie kroku o zmianie przedstawiciela i usunięciu niejednolitego symbolu**.
9. **Kryterium uzupełnienia:** przedłużenie `T:X→Y` do `S:X̂→Y`; skonstruowanie odwrotności na gęstym podzbiorze `T(X)`; niezależność od wyboru sieci z jednostajnej ciągłości; ciągłość `R` w zerze. **PASS**.

## Trzy środowiska przykładów

1. **`Σ(I)` w `K^I` dla nieprzeliczalnego `I`:** gęstość przez sieci o skończonych nośnikach; właściwość podprzestrzeni i ciągowa domkniętość przez przeliczalną sumę nośników. **PASS**.
2. **Podprzestrzeń ciągowo zupełna, lecz niezupełna:** `Σ(I)` w zupełnym produkcie `K^I`; sieć skończonych sum wektorów bazowych jest Cauchy'ego w `Σ(I)`, a granicę w produkcie ma poza tą podprzestrzenią. **PASS**.
3. **Trzy klasyczne uzupełnienia:** `c_{00}→ℓ^p` przy `1≤p<∞`, `C([0,1])→L^1` z normą całkową i `c_{00}→K^N` z topologią produktową. **PASS**.

## Poprawki rzeczywiście wprowadzone w pliku źródłowym

1. Ujednolicono oznaczenie z pomocniczym otoczeniem `W_0` w kroku 2 dowodu uzupełnienia: wcześniej występowało niezdefiniowane `W_e` w warunku `y_e+W_e⊆V`, choć następne zdanie używało `W_0` jako otoczenia niezależnego od `e`.
2. W dowodzie niezależności definicji `Û` od reprezentanta dopisano, że otoczenie `W` z `W+W⊆V` wybieramy **symetryczne**. Jest to potrzebne, ponieważ definicja równoważności sieci bezpośrednio kontroluje różnice `x_d-y_e`, zaś w argumentacji używa się `y_e-x_d`. Po wyborze symetrycznego W krok jest poprawny.
3. Tytuł przykładu `Sekwencyjnie zupełna, ale niezupełna TVS` zastąpiono `Przestrzeń ciągowo zupełna, ale niezupełna`, zgodnie z zasadą globalną.
4. Zachowano dotychczasowe 15 etykiet, 9 środowisk dowodów i 3 środowiska przykładów; nie dodawano niezatwierdzonych nowych tematów.

## Kontrola brzegowa i regresje

- **Nieprzeliczalny produkt:** zbieżność sieci częściowych sum zależy od dowolnego skończonego zbioru współrzędnych; ciągi o przeliczalnych nośnikach nie mogą przybliżyć wektora o nieprzeliczalnym nośniku w sensie granicy ciągu.
- **Zbieżność ciągowa a zupełność:** dla `Σ(I)` nie wolno wnioskować o zupełności z ciągowej zupełności, ponieważ przestrzeń nie jest metryzowalna.
- **Przypadek `λ=0` oraz niezerowe `λ`:** sprawdzono działanie mnożenia skalarnego na klasach sieci Cauchy'ego; otoczenia są zrównoważone.
- **Brzeg `U`:** dwie równoważne sieci `1-1/n` i `1+1/n` przy `U=(-1,1)` pokazują, dlaczego „ostatecznie w U” nie definiuje dobrze otoczenia klasy; stałe `V` zapewnia zapas.
- Dodano `tools/tests/test_functional_analysis_ch03.py` z **10 testami**: integracja, środowiska i odsyłacze, terminologia i symbol `W_0`, skierowanie skończonych zbiorów, filtry ogonów, własności `E_U`, zbieżność współrzędna `e_n`, aproksymacje w `ℓ²` i reprezentanci na brzegu `U`.
- Dodano `.github/workflows/functional-analysis-ch03.yml`, który kompiluje rozdział 03 w pełnym kontekście rozdziałów 01–05, aby sprawdzić rzeczywiste odsyłacze. **Końcowy status CI do uzupełnienia po zakończeniu przebiegu**.

## Kontrola składu i ilustracji

- Rysunek 3.1 pokazuje gęste osadzenie `j:X→X̂` i liniowe przedłużenie `T̂`; kontrola wizualna PDF wymagana przed ostatecznym zamknięciem raportu.
- W nowym workflow sprawdzane są brak błędów LaTeX, brak nierozwiązanych odsyłaczy, brak przepełnionych wierszy i brak brakujących znaków w końcowym logu.

## Decyzja

**Audyt 03/01 wymagał poprawek, więc NIE JEST CZYSTY.** Rozdział 03 pozostaje w stabilizacji. Następna iteracja powinna wykonać niezależny audyt poprawionej wersji, aż do osiągnięcia dwóch kolejnych czystych kontroli.
