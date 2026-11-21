# Topologia algebraiczna — TOP-27: audyty I–V oraz naprawa ogólnego CI

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian na `main`).  
**Rozdział:** `chapters/pl/algebraic_topology/27-szesc-operacji-snopowych-dualnosc-verdiera-i-cykle-specjalizac.tex`.  
**Końcowy blob TOP-27:** `812a54b896dbe12ac4316b7d407d5040890427f4`.  
**Zasada:** pięć audytów jednego istniejącego rozdziału, bez dokładania twierdzeń i lematów; szczegółowość według DG-01; samodzielne twierdzenia, uzasadnione wzory, ilustracje, odsyłacze i kontrola CI.

## Audyt I — kategorie i dokładność funktorów

- Usunięto błędne utożsamienie zachowywania krótkich ciągów dokładnych z dokładnością funktora pochodnego. Funktory `f_*` i `f_!` są lewostronnie dokładne, natomiast `Rf_*` i `Rf_!` zachowują trójkąty wyróżnione.
- Jawnie ustalono argumenty w adjunkcji iloczynu tensorowego i wewnętrznego Homu.
- „Rezolwenty iniektywne” poprawiono na „rezolucje iniektywne”.
- Poprawiono „mapa” → „odwzorowanie” w znaczeniu mapping; zachowano „mapa współrzędnych” w znaczeniu chart.
- Doprecyzowano, że dowód wymiany przez dualność zakłada morfizm algebraiczny po analityfikacji, a porównanie cykli pobliskich z włóknem Milnora wymaga lokalnie gładkiego otoczenia izolowanego punktu krytycznego.

Commit: `8cb04889f3cdcd7841234b1a688512f61b1b381e`.

## Audyt II — samodzielność sformułowań

- W lemacie o dokładnym ciągu lokalizacyjnym jawnie określono `X,Z,U,i,j,k,F`. W dwóch trójkątach lokalizacyjnych jawnie podano kategorię, podzbiór algebraiczny i włożenia.
- W definicji kompleksu dualizującego dopisano `X`, `a`, `k`, `A`.
- Twierdzenie o dualności Verdiera sformułowano dla analityfikacji zespolonej odmiany algebraicznej skończonego typu. Przypadek rozmaitości rzeczywistych podano osobno.
- Wniosek o dualności Poincarégo ma jawne założenia dotyczące `M,n,k`, orientacji, braku brzegu i współczynników orientacji dla przypadku nieorientowalnego.
- W twierdzeniu o zmianie podstawy określono `f,g,X',f',g',A` zamiast „standardowych założeń”; w twierdzeniu Leraya — `f,X,Y,k,F,p,q`.
- Uporządkowano język opisu zmian orientacji przy zmianie map współrzędnych.

Commity: `43cc9e87eef81ef8da7356b367719e3dd6c326f1`, `a9b12389cfb0e940fffbb51598848faaf8414cf7`, `965a50c7c01c3305ca6e86ab2e3399de69c50c11`.

## Audyt III — formalizm i polska terminologia

- Sformułowano samodzielnie pierwszą adjunkcję sześciu funktorów, wymieniając morfizm kompleksów konstruktybilnych w klasycznej topologii zespolonej.
- W twierdzeniu o gładkiej czystości podano rzeczywiste rozmaitości bez brzegu, stały wymiar włókien, ciało `k` i lokalny system orientacji.
- Rozwinięto definicję cykli pobliskich przez mapę do dysku, włożenie włókna centralnego i nakrycie uniwersalne.
- Zmieniono samodzielny rzeczownik „dual” na „obiekt dualny”, usunięto angielskie „pullback” i „Deck transformation” tam, gdzie właściwy jest polski „obraz odwrotny” i „automorfizm nakrycia”.
- Zachowano otwarcie wskazane zależności od twierdzenia Verdiera, czystości oraz twierdzenia Milnora.

Commit `d5ced6002049ba9d0921d7632155679e94ba4c75`.

## Audyt IV — regresje matematyczne

Dopisano testy: obecności poprawnych hipotez, rozróżnienia `f_!` od `Rf_!`, kieszeni lokalizacyjnych na warstwie otwartej i domkniętej, poprawności rang włókien `x²=y` dla `y<0,y=0,y>0`, niemożności użycia nieuprawnionej zmiany podstawy dla `j_*k_{(0,1)}` w `0`, dualności Poincarégo w dopełniających stopniach na `R`, a także przesunięcia `i^!k_C≃k[-2]` dla płaszczyzny zespolonej.

Commity testów: `1685fce33e5bd92a294ba497954df76a0961e01d`, `50b627e0c0c4e415faf15f0509dd863fb6e7c726`.

## Audyt V — ostatnia korekta i stabilizacja

- Uporządkowano zależność w treści stwierdzenia o włóknie Milnora: najpierw holomorficzne `f:X→Δ` i `X_0=f^{-1}(0)`, następnie `x∈X_0` i izolowany punkt krytyczny.
- Doprecyzowano twierdzenia o wzorze projekcji i kohomologii włókien tak, aby niezależnie wymieniały założenia algebraiczne, właściwość odwzorowania, współczynniki i obiekty.
- Usunięto ostatnie samodzielne angielskie lub niejednoznaczne określenia „dual”, „mapa” (jako mapping), „pullback”. Zachowano polskie „mapy współrzędne”.
- Po ponownej kontroli **nie stwierdzono kolejnych nieuzasadnionych wzorów ani luk matematycznych wymagających zmiany**. Przyjęte wyniki głębokie pozostają jawne.

Commity: `f1387d6e29fc288b76a3dea9e14e2ed8559f1742`, `b145a2a85e296c08247fcb44b2e86c2558a59a84`, `a53eb79031297a51076cdbb987733aa1dae72945`.

## Kontrola techniczna

- **14 etykiet** (wszystkie unikatowe), 5 wystąpień `\ref`, wyłącznie do istniejących celów w obrębie całej książki.
- **9 twierdzeń, 2 lematy, 2 stwierdzenia, 5 definicji, 7 przykładów, 1 wniosek, 7 uwag, 14 dowodów** — wszystkie środowiska są prawidłowo zamknięte.
- **3 osadzone diagramy TikZ**, w tym rysunek przekłutego dysku. Wszystkie dziewięć stron rozdziału obejrzano po renderowaniu; żadnych obcięć ani nakładających się podpisów.
- Kompilacja całej zależnej książki ze wszystkimi 28 rozdziałami w **dwóch przebiegach pdfLaTeX**, brak niezdefiniowanych odsyłaczy i brak `Overfull \\hbox`.
- **PDF TOP-27 ma 9 stron A4**, wydzielony bezpośrednio ze zweryfikowanego pliku `audit_at_27_28.pdf` (strony PDF 291–299). Źródło artefaktu: GitHub Actions #44946067383.

## Naprawa CI niezwiązana z TOP-27

W `LST-17` usunięto nieistniejący odsyłacz do przyszłego rozdziału `ch:representability-diagonal`; zastąpiono go zapowiedzią bez fałszywego celu. Dostosowano do zmiany workflow liczący odsyłacze (225 → 224; 4 → 3 oczekiwane odsyłacze naprzód) oraz test regresyjny LST-17. Nie stworzono etykiety zastępczej ani nie dodano do baseline'u fikcyjnego wyjątku.

Commity `d03edcdcb36cdacfaa79d1d55dfb3f0a89a54fb8`, `320514e38b23546ebeb50c614f12cb6c9f028073`, `49d3026544647c933675896ccdb272086c7b9f35`.

### Końcowe GitHub Actions

- [Walidacja logiki i teorii mnogości — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44945547352).
- [TOP-27/28 LaTeX i regresje — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44946067383), commit `a53eb790`.
- [Ogólne CI aplikacji — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44946067389), ten sam commit.
- [Kontrola międzytomowa AT–DG–AG — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44946067441), ten sam commit.

**Decyzja:** TOP-27 stabilny po audytach I–V. Kolejny w procedurze: TOP-28 — „Topologia gładkich zespolonych odmian projektowych: twierdzenia Lefschetza, przecięcia i rozdmuchania”.
