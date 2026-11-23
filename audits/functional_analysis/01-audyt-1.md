# Analiza funkcjonalna — rozdział 01 — audyt 1

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło:** `chapters/pl/functional_analysis/01-przestrzenie-liniowo-topologiczne-definicje-i-przyklady.tex`  
**Punkt wyjścia:** źródłowa wersja po audycie II; niniejsza iteracja wprowadza oznaczenie audytu III.

## Metoda i zakres

Kontrola rozdziału punkt po punkcie: poprawność i kompletność założeń, 9 dowodów, 7 przykładów, przypadki brzegowe, precyzja argumentów, zgodność terminologiczna z `AGENTS.md`, kompletność oznaczeń, odsyłacze, integracja z książką i przygotowanie osobnego przebiegu CI LaTeX. Nie rozszerzano zatwierdzonej tematyki rozdziału.

## Rejestr matematyczny: 9/9 dowodów przeanalizowanych

1. **Przesunięcia i niezerowe homotetie:** ciągłość wynika z działań w TVS; odwrotności mają postać odpowiednio przesunięcia przeciwnego i mnożenia przez odwrotny skalar. **PASS**.
2. **Przesuwanie otoczeń do zera:** homeomorfizm zachowuje otoczenia; argument nie wymaga warunku Hausdorffa. **PASS**.
3. **Podstawowe własności otoczeń zera (i)–(iv):** sprawdzono konstrukcję otoczenia sumacyjnego, symetrycznego, zrównoważonego (zwartość dysku jednostkowego i wnętrze `DV`), a także pochłanianie przez ciągłość funkcji `t↦tx` w zerze. **PASS**.
4. **Warunek Hausdorffa i domknięcie zera:** zweryfikowano obie inkluzje wzoru `cl({0})=∩_{U∈N(0)}U`, oddzielanie punktów przez przesunięte symetryczne otoczenia i liniowość domknięcia zera. **PASS**.
5. **Kryterium ciągłości liniowej w zerze:** stosowanie przesunięć oraz liniowości przy przeniesieniu ciągłości z zera do dowolnego punktu. **PASS**.
6. **Domkniętość jądra:** preobraz domkniętego singletonu w przestrzeni Hausdorffa. **PASS**.
7. **Test ograniczoności przez małe skalary:** obie implikacje z wykorzystaniem zrównoważonej bazy otoczeń. **PASS**.
8. **Ograniczoność zbiorów zwartych i obrazów liniowych:** zwartość daje skończone podpokrycie przez rosnącą rodzinę `nV`; poprawiono jawne uzasadnienie przejścia od pochłaniania do pokrycia. Obraz ograniczonego zbioru kontroluje przeciwobraz otoczenia zera. **PASS po doprecyzowaniu**.
9. **Zupełność `L^p([0,1])` dla `0<p<1` i zerowa przestrzeń ciągłych funkcjonałów liniowych:** sprawdzono podaddytywność potęgi `p`, wspólną ciągłość mnożenia, wybór podciągu z sumowalnymi `p`-potęgami przyrostów, zbieżność prawie wszędzie, domknięcie argumentu Cauchy'ego, oszacowanie ciągłego funkcjonału, podział zbioru na części równej miary w przestrzeni bezatomowej oraz gęstość funkcji prostych. **PASS**.

Nie wykryto fałszywej tezy matematycznej. W jednym dowodzie wymagane było dopisanie jawnego przejścia, żeby spełnić przyjęty standard szczegółowości.

## Rejestr przykładów: 7/7

1. Topologia trywialna na niezerowej przestrzeni liniowej: ciągłość działań i brak własności Hausdorffa. **PASS**.
2. Zbiór zrównoważony, ale niewypukły: punkty `(1,1)`, `(2,1/2)` oraz środek `(3/2,3/4)`; sprawdzony kontrprzykład. **PASS**.
3. Ciągła bijekcja liniowa bez ciągłej odwrotności: funkcje trójkątne o normach `1` i `1/(2n)`; sprawdzono również uzasadnienie niezupełności normy całkowej. **PASS**.
4. Równoważność ograniczoności w TVS unormowanej i zwykłej ograniczoności normowej, łącznie z przypadkiem zbioru pustego. **PASS**.
5. Produkt `K^N`: ciągłość współrzędna działań, brak ograniczonych otoczeń i zbieżność wektorów bazowych `e_n→0`. **PASS**.
6. Topologia zbieżności punktowej na podprzestrzeni przestrzeni wszystkich funkcji: własność uniwersalna produktu; argument obejmuje również sieci. **PASS**.
7. Nieciągły funkcjonał `p↦p'(0)` na wielomianach z normą supremum: świadek `(1-t)^n`. **PASS**.

## Rzeczywiste poprawki w źródle

- Pięć wystąpień `\mathbf1_A` (także z innymi indeksami) zastąpiono przez obowiązujące `\chi_A`; dotyczy przykładów z `L^1` i dowodu dla `L^p`.
- Uzupełniono dowód ograniczoności zbiorów zwartych: jeśli `x∈tV` i `n≥t`, zrównoważenie daje `x∈nV`.
- Usunięto dwa przypadki niedozwolonego rzeczownika „dual” z prozy (bez zmiany historycznej etykiety `thm:lp-trivial-dual`).
- Zmieniono nagłówek „Przykłady przestrzeni nienormowalnych” na „Topologie produktowe i zbieżność punktowa”: drugi przykład obejmuje także przypadki normowalne, więc wcześniejszy nagłówek był mylący.
- Skorygowano zapowiedź rozdziałów: produkty/podprzestrzenie/ilorazy są w 02, sieci w 03, ograniczoność i metryzowalność w 04, seminormy i lokalna wypukłość w 05.
- Zachowano bez zmian wszystkie istniejące etykiety i nazwy twierdzeń.

## Kontrola techniczna i CI

- **9** par środowisk `proof`, **7** przykładów; **15** unikatowych etykiet i **4** odsyłacze, wszystkie do etykiet zdefiniowanych w rozdziale; identyfikatory etykiet zachowane: **PASS**.
- Modelowe kontrole liczbowe: świadek niewypukłości, norma `L^1` funkcji trójkątnych, wykładnik `1-1/p<0`, losowe próby podaddytywności potęgi `p`: **PASS** (kontrole pomocnicze, nie dowody).
- Dodano `tools/tests/test_functional_analysis_ch01.py`, zawierający **8 testów** struktury, oznaczeń, odsyłaczy, integracji z książką, rachunków pomocniczych i zakazu angielskiego rzeczownika „dual” w prozie.
- Dodano `.github/workflows/functional-analysis-ch01.yml`, który uruchamia testy i buduje wyizolowany PDF rozdziału z preambułą książki. **CI: PASS** na commicie `1e36e936578ad6632bf429e1af4327df9ff3232e`, [przebieg 45149989014](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45149989014): 8/8 testów Pythona, dwukrotna kompilacja LaTeX, kontrola logu po drugiej kompilacji i zawartości PDF, zapis artefaktu. PDF ma 6 stron A4 i 264612 bajtów. Ostrzeżenia o niezdefiniowanych odsyłaczach występowały tylko w pierwszym przebiegu kompilacji i zniknęły po drugim.
- Oględziny wszystkich 6 stron finalnego PDF: **PASS** — renderowane strony z repozytoryjnego artefaktu sprawdzono wizualnie w układzie 3×2; brak widocznych kolizji, obcięć i przekroczeń marginesów. Rozdział nie zawiera rysunków wymagających osobnej kontroli. Log końcowy bez błędnych odsyłaczy, overfull i brakujących znaków.

## Propozycje merytoryczne — nie dodano, wymagana decyzja użytkownika

1. Przy przykładzie `L^p` dla `0<p<1` rozważyć zwięzłe porównanie z `\ell^p` dla `0<p<1`: funkcjonały współrzędnych są w tej drugiej przestrzeni niezerowe i ciągłe. Pozwala to pokazać rolę bezatomowości w dowodzie zerowości przestrzeni funkcjonałów.
2. Przy produkcie `K^N` można dodać charakterystykę ograniczoności jako ograniczoności każdej współrzędnej (albo przenieść to do rozdziału 04).

## Decyzja i kolejny etap

**Po pierwszym audycie: poprawki wprowadzone, status rozdziału — NIEUSTABILIZOWANY.** Nie jest to audyt czysty, ponieważ wymagał zmian. Kolejna iteracja: niezależny ponowny przegląd wszystkich 9 dowodów i 7 przykładów na aktualnej wersji oraz ponowne potwierdzenie jakości składu i odsyłaczy. Pierwsza iteracja nie może być liczona jako czysta; dopiero kolejne czyste audyty mogą uzasadniać stabilizację rozdziału 01. Nie przechodzić do rozdziału 02 przed stabilizacją 01.
