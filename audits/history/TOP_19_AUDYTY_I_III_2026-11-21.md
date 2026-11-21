# Topologia algebraiczna — TOP-19, audyty stabilizacyjne I–III

**Data:** 21 listopada 2026.  
**Repozytorium i gałąź:** `dariusz-piekarz/mathematical_scipts`, `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/algebraic_topology/19-stopien-indeks-punktu-stalego-i-twierdzenie-lefschetza.tex`.  
**Końcowy blob rozdziału:** `5cb2a5022dfe141f07732f5907994c2ec103dad9`.  
**Zasada:** bez dodawania twierdzeń, lematów lub nowych tematów. Weryfikacja istniejącego materiału, dowodów, oznaczeń, rysunków, odsyłaczy, LaTeX, regresji i CI. Punktem wyjścia był raport wcześniejszego audytu pary TOP-19/20 (`TOP_19_20_ITERACJA_20_2026-11-21.md`).

## Audyt I — krytyczna rewizja całego rozdziału

Przeczytano kolejno: definicję liczby Lefschetza, lemat śladu Hopfa, twierdzenie Lefschetza dla skończonych CW-kompleksów z redukcją do wielościanów i argumentem ANR, indeks izolowanego punktu stałego, formułę Lefschetza–Hopfa przez graf i diagonalną, przykłady sfer, torusa, rotacji oraz odbicia odcinka.

Wykonano następujące poprawki bez zmiany zakresu twierdzeń:

1. Wniosek o homotopijnej niezmienniczości liczby Lefschetza zyskał samodzielne założenie, że `X` jest skończonym CW-kompleksem, oraz jawny warunek ciągłości odwzorowań.
2. Definicja indeksu lokalnego wprowadza wprost kartę `φ` z `φ(p)=0` i kulę `B=B(0,ε)`, a także konieczny warunek `f(φ^{-1}(cl B))⊂U`, by złożenie `F=φ∘f∘φ^{-1}` istniało na domkniętej kuli. Umożliwia to bezpośrednie zastosowanie rozwinięcia w punkcie zerowym w dowodzie.
3. Stwierdzenie o właściwościach indeksu ma jawne hipotezy dla `M,f,p` i precyzuje niezmienniczość sumy indeksów przy homotopii bez punktów stałych na brzegu otoczenia.
4. Poprawiono użycie rzeczownika „mapa” w znaczeniu odwzorowania, pozostawiając słowo „mapa” wyłącznie dla kart współrzędnych.
5. Usunięto przestarzały komentarz roboczy dotyczący innego rozdziału.

**Commit:** `c7bda045277bdee06d7a531b7fe16badb622059e`.

Dodano test regresyjny wymuszający poprawną dziedzinę indeksu, samodzielność sformułowań i terminologię: **commit** `fcc351520e0d646343837c6c29419189b0e7130a`.

## Audyt II — niezależna matematyczna, strukturalna i wizualna kontrola

Ponownie sprawdzono:

- Tożsamość śladu Hopfa w ograniczonym kompleksie skończeniewymiarowym: dokładne ciągi dla cykli, brzegów i homologii oraz anulowanie śladów.
- Argument kontrapozycji twierdzenia Lefschetza: odległość `δ` od diagonali, dwa różne podziały symplicjalne, brak wyrazów diagonalnych w operatorze `g_#∘S` oraz redukcję z ANR do wielościanu z cyklicznością śladu. Wyraźnie utrzymano zewnętrzne zależności od aproksymacji symplicjalnej i własności ANR skończonych CW.
- Stopień Brouwera pola różnicowego `id-F`, jego niezależność od kart i poprawny wzór `sgn det(I-Df_p)`.
- W przypadku zorientowanym klasę diagonalną i rachunek z dualnymi bazami kohomologii. W przypadku nieorientowalnym zachowano jawne wskazanie zewnętrznej wersji z lokalnymi współczynnikami.
- Na torusie dla `A=((2,1),(1,0))`: `tr A=2`, `det A=-1`, `det(I-A)=-2`, dwa punkty stałe `[(0,0)]` i `[(1/2,1/2)]`, oba z indeksem `-1`. Dodatkowo niezależnie zweryfikowano tożsamość `1-tr(A)+det(A)=det(I-A)` na 2401 całkowitych macierzach 2×2 z wyrazami od −3 do 3.
- **7/7 unikalnych etykiet**, **3/3 domkniętych odsyłaczy**, **2 diagramy TikZ** i poprawną strukturę wszystkich środowisk.
- Obejrzano wygenerowany siedmiostronicowy PDF TOP-19 (strony 223–229 dokumentu testowego): schemat przecięcia grafu z diagonalną i diagram torusa są czytelne, nie wychodzą poza marginesy i nie mają nakładających się podpisów.

W testach strukturalnych TOP-19/20 wykryto możliwość wzmocnienia ochrony: wcześniejszy test porównywał tylko liczność otwarć i zamknięć środowisk. Dodano kontrolę **kolejności ich zagnieżdżenia**, równowagi wszystkich `\begin{...}` i `\end{...}`, a także jednowierszowego domknięcia wszystkich typów odsyłaczy. **Commit:** `758c1991398941b3d13e4b0bcd5bd26780e95358`.

## Audyt III — ponowna walidacja po testach ochronnych

Bez kolejnych zmian w źródłowym TOP-19 zweryfikowano, że obydwa końcowe workflow GitHub Actions dla ostatniego commita testów są zielone:

- [TOP-19/20: TeX, dwie kompilacje, poprawne odsyłacze i brak overfull](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935987020): **completed / success**, SHA `758c1991`.
- [Aplikacja i regresje, w tym nowe testy TOP-19](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935986930): **completed / success**, SHA `758c1991`.
- [AT–DG–AG: zależności i spójność etykiet](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935691473): **completed / success**, SHA `c7bda045` (ten sam ostatni commit **źródła TOP-19**, późniejsze commity obejmowały wyłącznie testy).

Dokument TeX w CI zawiera wcześniejsze rozdziały TOP-01–20 i ma **236 stron**; **nie jest to pełna kompilacja 31-rozdziałowego tomu**. Kontrolę wizualną przeprowadzono na wydzielonym PDF TOP-19, 7 stron, w tym oba diagramy.

**Decyzja końcowa:** TOP-19 **STABILNY PO AUDYCIE III** względem wcześniejszego audytu TOP-19/20. Nie dodano nowych twierdzeń, lematów ani przykładów; istniejące etykiety i rysunki zachowano. Poprawki zapisano na tej samej gałęzi, bez ingerencji w `main`. Następny etap: TOP-20 — oddzielna niezależna kontrola analitycznej kompaktyfikacji i sklejania trajektorii Morse'a. Automatyzacji nie uruchomiono.
