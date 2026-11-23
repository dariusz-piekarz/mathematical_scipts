# Analiza funkcjonalna — rozdział 06 — audyt 02 (niezależny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/06-twierdzenie-hahna-banacha-i-ciagly-dual.tex.  
**SHA źródła po korekcie:** c8caeb6a6c102e6bfa4ad4560c6a0f3d6c682000.  
**Werdykt:** audyt wymagał poprawki matematycznej — **NIE jest czysty**, rozdział 06 ma **0/2** kolejnych czystych audytów i pozostaje w stabilizacji.

## Niezależna weryfikacja

Przejrzano aktualny rozdział po audycie 06/01, nie ograniczając się do raportu. Sprawdzono pełne sformułowania i 17 dowodów, 5 grup przykładów, zakres użycia aksjomatu wyboru, istotność założeń lokalnej wypukłości i Hausdorffa, dowody normujące, separację i anihilatory. Dodatkowo skontrolowano wszystkie odsyłacze w rozdziałach 01–06, polską terminologię oraz przypadki brzegowe.

## Matryca dowodów — 17/17 po weryfikacji

1. **Kryterium ciągłości funkcjonału:** ograniczenie modułu na otoczeniu i skalowanie przez epsilon charakteryzuje ciągłość w zerze oraz wszędzie. PASS.
2. **Przedłużenie o jeden wymiar:** dla dominacji funkcją podliniową p przedział dopuszczalnych wartości [L,R] nie jest pusty; z f(y+z)≤p(y+z)≤p(y−x0)+p(z+x0) dostajemy L≤R, a podstawienie zera zapewnia skończoność krańców. PASS, także dla p niesymetrycznej i przyjmującej wartości ujemne.
3. **Rzeczywisty Hahn–Banach:** porządek przedłużeń, ich unie w łańcuchach i lemat Kuratowskiego–Zorna poprawnie dają globalne przedłużenie. PASS.
4. **Odtworzenie funkcjonału zespolonego:** G(x)=u(x)−i u(ix), liniowość rzeczywista i równość G(ix)=iG(x) zapewniają zespoloną liniowość i jednoznaczność. PASS.
5. **Dominacja przez seminormę nad R/C:** w przypadku zespolonym rzeczywista część przedłużenia i obrót fazy alpha z |alpha|=1 dają |F(x)|≤p(x), zachowując f na M. PASS.
6. **Ciągłość przez seminormę:** p=|f| dla funkcjonału ciągłego i dominacja przez p ciągłą w stronę przeciwną. PASS.
7. **Topologiczne przedłużenie:** dla f ciągłego na M wybór otwartego absolutnie wypukłego U⊂W i funkcjonału Minkowskiego p_U zapewnia |f(m)|≤p_U(m); HB dominuje przedłużenie i gwarantuje jego ciągłość, także bez domkniętości M i bez Hausdorffa X. PASS.
8. **Jednoznaczność na gęstej podprzestrzeni:** jądro różnicy F1−F2 jest domknięte, więc zawiera całe X, gdy M jest gęsta. PASS.
9. **Przedłużenie z zachowaniem normy:** użycie p(x)=||f||·||x|| daje ||F||≤||f||, a ograniczenie do M daje nierówność odwrotną; bez założenia zupełności X. PASS.
10. **Funkcjonał normujący:** na prostej Kx0 f0(lambda x0)=lambda||x0|| ma normę 1; jego przedłużenie osiąga ||x0||. Przypadek x0=0 nie wymaga budowy prostej. PASS.
11. **Seminorma jako supremum:** gdy p(x0)>0 przedłużamy f0(lambda x0)=lambda p(x0), a przy p(x0)=0 wybieramy 0; p ciągła zapewnia ciągłość wszystkich dopuszczalnych funkcjonałów. PASS.
12. **Rozdzielanie punktów przez ciągłe funkcjonały:** przy lokalnej wypukłości i Hausdorffie istnieje seminorma p z p(x−y)>0; funkcjonał normujący dla p rozdziela parę. PASS.
13. **Oddzielanie x0 od domkniętej podprzestrzeni M:** z (x0+W)∩M=∅ oraz −U=U i U⊂W wynika x0−m∉U dla każdego m; następnie p_U(x0−m)≥1 i g(m+lambda x0)=lambda jest dominowany przez p_U. PASS po poprawce audytu 06/01.
14. **Domknięta podprzestrzeń jako przecięcie jąder:** włączenie domknięcia w każde jądro funkcjonału zerującego się na M i oddzielenie dowolnego x0 poza domknięciem. PASS.
15. **Przestrzeń sprzężona produktu K^I:** ograniczenie modułu funkcjonału na podstawowym otoczeniu produktowym wymusza zerowanie na podprzestrzeni o skończenie wielu ustalonych zerowych współrzędnych; odwrotnie skończone sumy rzutów są ciągłe. PASS.
16. **Przestrzeń sprzężona ilorazu:** składanie z rzutowaniem q daje bijekcję (X/M)' z anihilatorem M; ciągłość funkcjonału na ilorazie wynika z finalnej definicji topologii. PASS.
17. **Wzór na odległość od domkniętej podprzestrzeni:** g(m+lambda x0)=lambda dist(x0,M) ma normę 1, norma jest zachowana przez przedłużenie i osiąga odległość; przypadek x0∈M traktowany osobno. PASS.

## Przykłady — 5/5 sprawdzonych

1. Nieciągły funkcjonał algebraiczny z wartościami f(e_n)=n na znormalizowanej rodzinie liniowo niezależnej; wymaga Hamelowskiego przedłużenia przez aksjomat wyboru.
2. Sumowanie na c00 w ℓ1 jako jednoznacznie przedłużalny funkcjonał ciągły, kontrast z brakiem ciągłości sumowania w normie supremum.
3. Ewaluacja pochodnych na C∞([0,1]) jako ciągłe funkcjonały względem seminorm pochodnych.
4. Nieunikatowe normujące przedłużenia F_a(x,y)=ax+(1−a)y na R² z normą supremum.
5. Brak przedłużenia niezerowego funkcjonału z M=Kχ_[0,1] w L^p([0,1]), 0<p<1, na całą przestrzeń o trywialnej przestrzeni sprzężonej.

## Nowy wykryty problem i poprawka

**Nieprawdziwa ogólna teza we wstępie:** wcześniejsze „W skończonym wymiarze każdy funkcjonał liniowy jest ciągły” jest fałszywe w dowolnej TVS bez założenia Hausdorffa. Kontrprzykład: rzeczywista przestrzeń liniowa X=R z topologią trywialną {∅,R}. Odwzorowanie identycznościowe X→R (R w zwykłej topologii) jest liniowe i nieciągłe, ponieważ przeciwobraz (-1,1) nie jest otwarty w X.

W źródle zastąpiono twierdzenie poprawnym: **na skończenie wymiarowej TVS Hausdorffa każdy funkcjonał liniowy jest ciągły**, dodając wskazany kontrprzykład i wyraźnie odróżniając przedłużenie algebraiczne przez bazę od ciągłego. Zmieniono znacznik wersji źródła na „audyt IV”; zachowano wszystkie etykiety, dowody i przykłady.

To istotne merytorycznie, ponieważ rozdział jawnie dopuszcza TVS nie-Hausdorffa i stosuje w nich topologiczny Hahn–Banach. **Zmiana nie jest kosmetyczna i wymusza reset licznika czystych audytów.**

## Regresje i kontrola redakcyjna

- Rozszerzono tools/tests/test_functional_analysis_ch06.py z **14 do 17 testów**. Dodane: formalna kontrola warunku Hausdorffa i kontrprzykładu w tekście; asymetryczna funkcja podliniowa p(x,y)=x+|y|, która przyjmuje także wartości ujemne; obrót fazy w kompleksowym Hahn–Banachu. Przebudowano również wcześniejszy zbyt trywialny test oddzielania punktu od podprzestrzeni na rzeczywiste oszacowanie funkcjonału przez funkcjonał Minkowskiego w R².
- **17 środowisk proof, 5 środowisk przyklad, 22 unikatowe etykiety, 19 wystąpień odsyłaczy, 0 celów brakujących w rzeczywistym kontekście rozdziałów 01–06**.
- Nie przywrócono słowa „dual” jako samodzielnego rzeczownika w treści, nie ma niezgodnego zapisu funkcji charakterystycznej. Stabilne identyfikatory LaTeX i nazwa pliku pozostały niezmienione.
- W dedykowanym [CI 45177060637](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45177060637) etapy testów i kompilacji zakończyły się PASS. Pełny status walidacji PDF, odsyłaczy i artefaktu uzupełnić po końcowym wyniku.
- Przedział stron i kontrolę wizualną PDF nowego stanu trzeba potwierdzić po pobraniu artefaktu.

## Decyzja

**Audyt 06/02 NIE JEST CZYSTY (poprawka istotnej matematycznie tezy we wstępie). Rozdział 06 pozostaje w stabilizacji 0/2.** Następna iteracja będzie audytem 06/03 nowej wersji, a nie przejściem do rozdziału 07.
