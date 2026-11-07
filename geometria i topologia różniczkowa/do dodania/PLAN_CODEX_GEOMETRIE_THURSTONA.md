# Zadanie dla Codexa: rozbudowa skryptu „Geometria i topologia różniczkowa” o geometrie Thurstona

**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź docelowa:** `review`  
**Katalog docelowy (weryfikuj, nie zakładaj, że identyczny lokalnie):**  
`rozdzialy-matematyka/geometria i topologia różniczkowa/tex/rozdzialy/`

**Cel:** uzupełnij już istniejący wielorozdziałowy skrypt o teorię ośmiu geometrii modelowych Thurstona, ich metryki i niezmienniki oraz topologiczne konstrukcje zwartych ilorazów. **Nie pisz nowego podręcznika od zera i nie duplikuj** treści o geometrii euklidesowej, sferycznej i hiperbolicznej, już opisanej w skrypcie.

## WAŻNE: status rozpoznania

Wstępny audyt wykonano na zachowanej w bibliotece kopii `geometria_i_topologia_rozniczkowa.tex` zawierającej rozdziały 1–19 oraz na PDF `geometria_i_topologia_rozniczkowa(1).pdf` z 5.10.2026 zawierającym rozdziały 1–22. To **nie jest audyt aktualnego stanu gałęzi `review`** — bieżące pliki musisz przeczytać samodzielnie. W innym, nowszym logu kompilacji występowało `tex/rozdzialy/30-potok-ricciego.tex`; dlatego nie zakładaj, że obecna numeracja kończy się na 22.

Dostępne materiały: praca S. A. Pinillos Prado, *Geometric Structures on 3-Dimensional Manifolds* (2021, 76 stron w PDF; pomimo mylącej nazwy pobranego PDF praca dotyczy geometrii Thurstona) oraz osobny **szkic treści** `geometrie_thurstona_3rozmaitosci.tex`. Szkic jest materiałem do weryfikacji i adaptacji, **nie** gotową wersją przeznaczoną do bezrefleksyjnego włączenia; szczególnie dostosuj etykiety, zależności, konwencje i miejsca wstawienia.

## Etap 1 — audyt w repozytorium (obowiązkowy i pierwszy)

1. Zlokalizuj katalog repozytorium, sprawdź `git branch --show-current`, `git status --short` i nie nadpisuj niezacommitowanych zmian użytkownika. Nie resetuj, nie force-pushuj. Pracuj na gałęzi `review`; w razie rozbieżności najpierw zgłoś ją.
2. Znajdź źródła `main.tex`, pliki tomów, pliki `tex/rozdzialy/*.tex`, definicje środowisk, makr, pakietów, opcje kompilacji, wszystkie `\input` / `\include`. Ustal, jak numerowane są rozdziały i czy istnieje rozdział o geometrii 3-rozmaitości.
3. Przeszukaj **treść**, a nie tylko nazwy plików. Hasła: `Geometrie modelowe`, `Thurston`, `geometryzac`, `Seifert`, `Nil`, `Sol`, `Heisenberg`, `\widetilde`, `PSL`, `SL_2`, `Kleina`, `(G,X)`, `Ricci`, `torus odwzorowania`, `monodrom`, `nakrycie`, `orbifold`, `Gieseking`, `ósemkowego`, `JSJ`.
4. Utwórz tabelę `temat | plik:sekcja (istnieje/fragment/brak) | proponowana zmiana`. Zanim zaczniesz tworzyć nowe sekcje, sprawdź istniejące etykiety i unikaj kolizji.
5. Porównaj osobno **klasyfikację ośmiu geometrii modelowych** z **twierdzeniem o geometryzacji 3-rozmaitości** — to nie jest to samo twierdzenie.

Pomocnicze polecenia (adaptuj ścieżki i ignoruj `build/`):

```bash
pwd
git branch --show-current
git status --short
find . -name '*.tex' -not -path '*/build/*'
rg -n '\\(chapter|section|subsection|input|include)\{' --glob '*.tex' -g '!build/**'
rg -in 'Thurston|geometryzac|Seifert|Heisenberg|Nil|Sol|orbifold|Gieseking|JSJ|geometrie modelowe' --glob '*.tex' -g '!build/**'
rg -n '\\label\{' --glob '*.tex' -g '!build/**'
```

## Etap 2 — mapa istniejącego pokrycia (hipoteza do sprawdzenia na aktualnych plikach)

| Rozdział w kopiach źródłowych | Pokrycie | Zalecane rozszerzenie |
|---|---|---|
| 1. Rozmaitości różniczkowe | atlasy, wiązki, podrozmaitości | jedynie krótki odsyłacz do struktur `(G,X)`, bez powtórzenia atlasów |
| 2. Pola wektorowe i przepływy | nawias Liego, przepływy, prostowanie pola | późniejszy przykład pól lewostronnie niezmienniczych Nil; nie duplikuj definicji nawiasu |
| 6. Homotopia, nakrycia i CW | grupy podstawowe, nakrycia, van Kampen | krótki przykład rozmaitości `X/Γ`, działanie swobodne i właściwie nieciągłe; grupa decka |
| 10. Tensor metryczny | Euklides, sfera, H^n (półprzestrzeń, kula, hiperboloida) | zachowaj; opcjonalnie doprecyzuj nazwę „klasyczne modele stałej krzywizny” |
| 11. Koneksje | Levi-Civita, wzór Koszula i Christoffel | Koszul w ortonormalnej ramie nieholonomicznej na Nil i Sol, z rachunkiem |
| 12. Geodezyjne | geodezyjne w istniejących modelach | nowe pierwsze całki geodezyjnych Sol lub opis poziomych krzywych Nil |
| 13. Krzywizna | Riemann, Ricci, krzywizna sekcyjna, skalar | twierdzenie: w wymiarze 3 Ricci określa cały tensor Riemanna, a `Ric = 0` implikuje płaskość |
| 16. Dualność i klasy charakterystyczne | klasa Eulera | przykład `S^1 -> T^1Σ_g -> Σ_g` i `e(TΣ_g)=χ(Σ_g)` |
| 17–22. Morse, uchwyty, kobordyzmy, chirurgia | podstawy globalnej topologii i chirurgii | krótkie odsyłacze do rozkładów 3-rozmaitości; nie przesuwaj dowodów ani chirurgii wyższych wymiarów |
| późniejszy rozdział o potoku Ricciego (w logach występował plik `30-potok-ricciego.tex`) | status w bieżącej gałęzi NIEZNANY | dodać jedynie precyzyjny odsyłacz od geometryzacji, jeśli rozdział faktycznie istnieje |

**Zasada:** „istnieje w zachowanej kopii” nie oznacza „potwierdzone w aktualnym GitHub”. Opisz różnice po rzeczywistym audycie.

## Etap 3 — wstawienie nowego rozdziału

Preferowane miejsce: **po rozdziale o dualności Poincarégo i klasach charakterystycznych**, przed teorią Morse'a, tak aby można było odwołać się do klasy Eulera wiązki. Jeśli nowsza wersja skryptu ma już osobną sekwencję poświęconą 3-rozmaitościom / potokowi Ricciego, umieść tam nowy rozdział bez duplikowania istniejącej tematyki. Ostateczne miejsce wyznacza struktura bieżącego repozytorium, nie numer z tego planu.

Nazwę nowego pliku dopasuj do schematu katalogu (`NN-geometrie-thurstona.tex`, ostateczny numer po inspekcji). Użyj standardowych środowisk i makr projektu. Włącz plik **we wszystkich odpowiednich źródłach tomów / dokumentu głównego**, jeśli projekt ma kilka wariantów składania.

Sugerowany układ rozdziału (każda sekcja z definicją / twierdzeniem / dowodem bądź przykładem):

1. **Struktury `(G,X)`**: podejście Kleina, pseudogrupa obcięć elementów `G`, atlas, mapy przejścia na składowych spójnych, rozwinięcie i holonomia; odróżnij struktury lokalne od pełnych.
2. **Geometria modelowa Thurstona**: jednospójność `X`, tranzytywność `G`, zwarte stabilizatory, maksymalność, istnienie zwartych ilorazów. Uśrednianie metryki względem stabilizatora przy użyciu miary Haara (dowód).
3. **Dlaczego osiem**: twierdzenie klasyfikacyjne; rola wymiaru izotropii `3/1/0`. Pełny dowód jest głęboki; zaznacz dokładnie, co jest dowodem, a co szkicem, nie ogłaszaj samej enumeracji pełnym dowodem.
4. **Przypomnienie geometrii stałej krzywizny**: `S^3`, `R^3`, `H^3` — maks. 1–2 strony; odwołania do rozdziału 10, oblicz `Ric=2κg`, `Scal=6κ`; zwarty przykład każdego typu.
5. **Produkty**: `S^2×R` i `H^2×R`, metryka produktowa, krzywizna sekcyjna dodatnia/ujemna tylko w płaszczyźnie bazy, przykłady `S^2×S^1`, `Σ_g×S^1`.
6. **Nil**: grupa Heisenberga i jej mnożenie, forma `θ=dz-xdy`, rama `E_1=∂_x`, `E_2=∂_y+x∂_z`, `E_3=∂_z`, `[E_1,E_2]=E_3`, `g=dx²+dy²+(dz-xdy)²`; obliczenia Koszula i krzywizn `(-3/4,1/4,1/4)`, Ricci `(-1/2,-1/2,1/2)`; połączenie i holonomia, zwarty iloraz kratowy nad `T²`.
7. **`\widetilde{SL}_2(R)`**: `T^1 H²`, nakrycie uniwersalne, lokalna postać metryki `g=y^{-2}(dx²+dy²)+(dt+dx/y)²`; krzywizna połączenia, przykład `T^1Σ_g`, liczba Eulera `2-2g`.
8. **Sol**: półprosty produkt `R²⋊R`, `g=e^{-2t}dx²+e^{2t}dy²+dt²`, rama i nawiasy, krzywizny `(1,-1,-1)`, `Ric=diag(0,0,-2)`. Zwarty torus odwzorowania macierzy hiperbolicznej `A∈SL(2,Z)` o wartościach własnych `λ, λ^{-1}`. Rozpisz izometryczność identyfikacji i warunek współzwartości.
9. **Seifert i orbifold bazy**: ścisła definicja lub dokładnie zaznaczona wersja uproszczona, liczba Eulera i `χ^{orb}`; porównaj `H²×R` oraz `\widetilde{SL}_2(R)`, `R³` oraz Nil. Zastrzeżenia dotyczące wyjątkowych włókien, orientacji i szczególnych przypadków.
10. **Ilorazy hiperboliczne**: dyskretne grupy izometrii, wielościany fundamentalne i założenia twierdzenia Poincarégo; węzeł ósemkowy (dwa idealne czworościany, przestrzeń niezwarta o skończonej objętości), Gieseking (jeden idealny czworościan i nieorientowalność). Wyraźnie odróżnij ilorazy zwarte od skończenie objętościowych niezwartych.
11. **Geometryzacja**: tylko poprawne sformułowanie na poziomie skryptu, rozkład na składniki pierwsze oraz rozkład JSJ; „osiem geometrii” i „geometryzacja” jako odrębne twierdzenia. Przygotuj odesłanie do potoku Ricciego / chirurgii w istniejącym tekście; NIE obiecuj pełnego dowodu Perelmana w tym rozdziale.
12. **Zależność od Ricciego w 3D** — wstaw przede wszystkim do rozdziału 13; w nowym rozdziale może być tylko zwięzłe zestawienie odsyłające do właściwego dowodu.

**Ilustracje (2–4, bez nadmiaru):** schemat włóknienia Nil nad `T²` i holonomii prostokątnej; torus odwzorowania Sol z monodromią hiperboliczną; ewentualnie porównanie `Σ_g×S¹` z `T^1Σ_g`; torusy rozkładu JSJ. Użyj istniejących kolorów TikZ (`manifoldblue`, `manifoldred` itd.) i stylu skryptu. Jeśli `figure` bywa kłopotliwe w tym projekcie, stosuj `center` i zwykły podpis pod rysunkiem; nie dodawaj nowej zależności tylko po to, by uzyskać `\captionof`.

## Etap 4 — punktowe integracje z rozdziałami istniejącymi

- **Rozdział 6:** po omawianiu nakryć umieść lemat: swobodne, właściwie nieciągłe działanie `Γ` przez izometrie zupełnej `X` daje pokrycie `X→X/Γ` będące lokalną izometrią. Dodaj kontrast: orbifold przy punktach z nietrywialnym stabilizatorem.
- **Rozdział 10:** zachowaj wszystkie rachunki dla sfery oraz trzech modeli `H^n`; dodaj jedno wyjaśnienie, że są to przestrzenie stałej krzywizny, natomiast pełny katalog trójwymiarowy zawiera pięć dalszych geometrii.
- **Rozdział 11:** jeden pełen, nieprzesadnie długi przykład zastosowania wzoru Koszula w ramie nieholonomicznej (najlepiej Nil); unikaj dwóch identycznych dowodów w dwóch rozdziałach, odsyłaj do wyliczeń.
- **Rozdział 12:** z metryki Sol wyprowadź `p_x=e^{-2t}\dot x`, `p_y=e^{2t}\dot y` jako stałe pierwsze całki geodezyjnych i `\dot t²+p_x²e^{2t}+p_y²e^{-2t}=2E`. Objaśnij, czemu zredukowane równanie w `t` opisuje ruch w efektywnym potencjale.
- **Rozdział 13:** sformułuj i udowodnij wzory w ramie diagonalizującej `Ric`: `K_12=(r_1+r_2-r_3)/2` itd. Następnie `Ric=0 ⇔ Rm=0` tylko w wymiarze 3, i dla zupełnej jednospójnej rozmaitości `Ric=0 ⇒ (M,g)≅(R³,g_E)`; osobno zastrzeż, że `n≥4` nie daje tego wniosku.
- **Rozdział 16:** jeśli klasy Eulera już istnieją, dopisz przykład z naturalną wiązką `T^1Σ_g`, wartością `χ(Σ_g)` i jej rolą w odróżnieniu geometrii modelowych.
- **Potok Ricciego i chirurgia, o ile istnieją:** jedynie merytoryczne mosty do geometryzacji, bez podmieniania dowodów i bez mylenia operacji chirurgicznych o różnych wymiarach.

## Wymagania matematyczne i redakcyjne

- Pisz **po polsku**, konsekwentnie używaj „mapa” (dla chart) i „odwzorowanie”; dowody wyjaśniają cel, ideę i kluczowe kroki bez rozwlekania elementarnych rachunków.
- W tekstach LaTeX stosuj `\(...\)`/`$...$` dla krótkich wzorów i tylko niezbędne wzory wyeksponowane. Bez ozdobnych ramek `\boxed` w nowym materiale.
- Nie używaj samej nazwy „włóknienie” zamiennie z lokalnym „pole prostych” bez wykazania/globalnych warunków; odpowiednio oznacz skróty rozumowania.
- Bądź uważny na grupy `SL_2(R)`, `PSL_2(R)` i ich uniwersalne nakrycie; nie twierdź, że są tym samym obiektem.
- Stosuj jedną konwencję `R(X,Y)Z` i zgodne znaki krzywizn w całym projekcie.
- Zweryfikuj założenia zwartości, orientowalności, zupełności, bezskrętności oraz właściwej nieciągłości w każdym twierdzeniu.
- Dla geometrii Sol sprawdź zgodność monodromii `A` / `A^{-1}` z konwencją torusa odwzorowania.
- Dla Seiferta zaznacz, że prosta tabela `(χ^{orb},e)` ma hipotezy oraz wyjątki; nie przedstawiaj jej jako klasyfikacji wszystkich 3-rozmaitości bez warunków.
- **Zachowaj dotychczasowe `\label` i `\ref`.** Nowe etykiety z prefiksem np. `thur:` lub `sec:thurston-`; sprawdź kolizje, rozwiąż undefined references.
- Nie zmieniaj globalnej preambuły, nazw środowisk, plików PDF i numeracji ręcznie, chyba że wymaga tego kompilacja; nie wprowadzaj pustych środowisk `figure`.
- Nie kopiuj dłuższych fragmentów pracy Prado dosłownie; pisz nową polską ekspozycję, cytuj źródła bibliograficzne (Thurston, Scott, Milnor, Prado).

## Testy i warunki ukończenia

1. Zbuduj najpierw **raport audytu przed zmianami**: istniejące pokrycie, dokładne ścieżki, czego nie ma oraz planowane pliki.
2. Wprowadź zmiany w istniejącym drzewie `tex/rozdzialy` i połączenia w plikach głównych tomów. Wykonaj build zgodnie z poleceniem przyjętym w repozytorium (`latexmk` lub jego odpowiednik); jeśli projekt ma wiele tomów, przetestuj każdy dotknięty tom.
3. Sprawdź błędy TeX, duplikaty etykiet, brakujące odsyłacze, błędne przypisy/odsyłacze, brakujące pakiety, przepełnione tabele oraz rysunki. Przebuduj drugi raz, jeśli tego wymagają referencje.
4. Ręcznie zrewiduj rachunki krzywizn Nil, Sol, `\widetilde{SL}_2(R)` i twierdzenia 3D-Ricci. W raporcie podaj konwencję znaku tensora krzywizny.
5. Wyświetl podsumowanie `git diff --stat`, listę dokładnie zmienionych plików, informację co dodano i co celowo pozostawiono bez zmian, wynik kompilacji i pozostające ograniczenia.
6. **Nie wykonuj samoczynnie push/merge**. Zmiany pozostaw w katalogu roboczym do przeglądu.

## Definicja ukończenia

Zmiany są zakończone dopiero, gdy nowy rozdział jest włączony do odpowiednich plików nadrzędnych, nie duplikuje rozdziałów 10–13, ma poprawne rachunki Nil/Sol, zawiera co najmniej dwa niebanalne konstruktywne przykłady zwartych ilorazów (Nil i Sol), odróżnia osiem geometrii od geometryzacji, oraz kompiluje się bez błędów i niepoprawnych odwołań w dotkniętych tomach.
