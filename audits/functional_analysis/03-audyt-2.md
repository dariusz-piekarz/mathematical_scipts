# Analiza funkcjonalna — rozdział 03 — audyt 02 (niezależny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/03-sieci-struktura-jednostajna-i-zupelnosc.tex.  
**SHA audytowanego źródła:** 5ea236a2bdf75e97e9ef8082340457c9ee9bd0a6.  
**Wynik:** **czysty audyt matematyczno-redakcyjny i techniczny (1/2), CI PASS**. Rozdział 03 jeszcze niestabilny.

## Metoda i zakres

Niezależnie sprawdzono 9 dowodów i 3 środowiska przykładów, definicje, kwantyfikatory, topologie, przejścia sieć–filtr, przypadki brzegowe i uzupełnienie dowolnej TVS Hausdorffa bez założenia metryzowalności lub lokalnej wypukłości. Nie opierano się tylko na wcześniejszych ocenach PASS. Źródło LaTeX pozostawiono bez zmian.

## Weryfikacja matematyczna: wszystkie 9 dowodów PASS

1. **Domknięcie i ciągłość przez sieci:** skierowanie otwartych otoczeń przez odwrotną inkluzję, wybory punktów w przecięciach z A i konstrukcja sieci świadczącej o nieciągłości. Nie wymaga Hausdorffa.
2. **Kanoniczna struktura jednostajna:** przekątna, przecięcia E_U, symetryczne otoczenia dla odwracania relacji, składanie dla V+V zawartego w U, przekroje E_U[x]=x-U odtwarzają topologię.
3. **Ciągłość liniowa i jednostajna:** T(x)-T(y)=T(x-y) oraz kryterium ciągłości liniowej w zerze.
4. **Sieci Cauchy'ego i filtry Cauchy'ego:** równoważność przez ogony; sieć indeksowana parami (A,a) przy odwrotnej inkluzji A jest skierowana i zachowuje warunki zbieżności oraz Cauchy'ego.
5. **Jednoznaczność granic i podsieci:** oszacowania przez symetryczne V, Hausdorff zapewnia jedyność; współkońcowość podsieci pozwala znaleźć jej wyraz o indeksie wystarczająco późnym.
6. **Zupełność ciągowa i zupełność w przypadku metryzowalnym:** malejąca przeliczalna baza U_n, wybór indeksów e_n, wybrany ciąg Cauchy'ego i przejście od jego granicy do granicy pierwotnej sieci.
7. **Podprzestrzenie i produkty zupełne:** zbieżność sieci w domkniętej podprzestrzeni, domkniętość zupełnej podprzestrzeni w TVS Hausdorffa, zupełność produktów sprawdzona współrzędnie, także dla pustego zbioru indeksów.
8. **Uzupełnienie TVS i jego własność uniwersalna:** oddzielnie sprawdzono pięć kroków:
   - Ustalenie zbioru indeksów D_* (skończone podzbiory zbioru otwartych zrównoważonych otoczeń), ponowne indeksowanie i klasy równoważności sieci Cauchy'ego.
   - Wprowadzenie otoczeń klas z zapasem V; niezależność od przedstawiciela dzięki symetrycznemu W oraz W+W zawartemu w V; własność j^{-1}(\widehat U)=U i warunek Hausdorffa.
   - Gęstość j(X), zbieżność późnych wartości sieci w uzupełnieniu oraz ciągłość łączna mnożenia przez skalar.
   - Zupełność przez pomocniczą sieć x_{alpha,U}, oszacowania trzech różnic za pomocą otoczeń i przejście do granicy.
   - Przedłużenie operatora, niezależność definicji od przedstawicieli, ciągłość dzięki oszacowaniu domknięcia V przez V+V oraz jednoznaczność z gęstości. Każdy krok **PASS**.
9. **Kryterium uzupełnienia:** budowa S oraz odwrotności na T(X), rozszerzenie odwrotności przez sieci Cauchy'ego i ciągłość z wykorzystaniem domknięcia małych otoczeń. **PASS**.

Nie stwierdzono nieprawdziwego twierdzenia ani dalszego przeskoku uzasadniającego zmianę źródła.

## Przykłady: 3/3 PASS

1. Sigma(I) w produkcie K^I, I nieprzeliczalne: gęstość przez sieci o skończonych nośnikach, ciągowa domkniętość dzięki przeliczalnej sumie nośników, a brak domkniętości topologicznej.
2. Sigma(I) ciągowo zupełna, ale nie zupełna: produkt K^I jest zupełny, a konkretna sieć sum wektorów bazowych nie ma granicy wewnątrz Sigma(I).
3. Uzupełnienia c_00 w l^p (1≤p<∞), C([0,1]) w L^1 oraz c_00 w K^N z topologią produktową.

## Niezależne próby kontrprzykładów

- **Zmiana znaku różnicy:** poprawione źródło wybiera symetryczne W w dowodzie niezależności otoczeń \widehat U od przedstawiciela; poprzednia luka jest zamknięta.
- **Brzeg otoczenia:** równoważne sieci 1−1/n i 1+1/n demonstrują, że bez stałego marginesu w definicji \widehat U otrzymalibyśmy definicję zależną od przedstawiciela.
- **Nośniki:** przeliczalna suma przeliczalnych nośników nie może dać nieprzeliczalnego nośnika, choć sieci indeksowane skończonymi podzbiorami taką granicę mogą przybliżać w produkcie.
- **Produkty indeksów:** przykład sumy dwóch ciągów Cauchy'ego uzasadnia stabilność operacji na klasach sieci po przejściu do produktu indeksów.
- **Przypadki brzegowe:** skalar zero, sieci stałe, puste rodziny czynników w produkcie oraz dowolne TVS Hausdorffa.
- Weryfikowano pełne kwantyfikatory, a nie jedynie testy liczbowe.

## Terminologia, etykiety i PDF

- **9 par proof, 3 par przyklad, 15 różnych etykiet, 5 lokalnych odsyłaczy** — wszystkie istnieją.
- Brak niepożądanego terminu „sekwencyjnie”; w rozdziale używa się „ciągowo zupełna”. Oznaczenia W_0 i symetrycznego W są po poprzednich poprawkach spójne.
- Obejrzano ponownie renderowane strony **15–22** dokumentu z rozdziałami 01–05, w szczególności rysunek 3.1 na stronie 21. Nie stwierdzono nachodzenia tekstu i strzałek ani obcięć. Źródło rozdziału nie zmieniło się od powstania tego PDF.
- [Wcześniejszy pełny CI 45155442949](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45155442949): PASS na tym samym źródle.

## Wzmocnienie regresji i CI

- Rozszerzono **tylko** narzędzia kontrolne: tools/tests/test_functional_analysis_ch03.py zawiera teraz **14 testów** zamiast 10. Nowe testy dotyczą jawnej symetrii W, niezmienniczości reprezentantów z marginesem do brzegu U, sum sieci Cauchy'ego o indeksach iloczynowych i przeliczalnych nośników.
- Kompilacja korzysta z pełnego kontekstu rozdziałów 01–05, aby odsyłacze były rzeczywiście rozwiązywane, nie pomijane.
- [Dedykowany przebieg CI 45156131987](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156131987): **pełny SUCCESS** — 14/14 testów Pythona PASS, przygotowanie dokumentu z rozdziałami 01–05 PASS, kompilacja LaTeX PASS, kontrola PDF i odsyłaczy PASS, artefakt przesłany. Pobrany plik PDF ma **33 strony A4, 480445 bajtów**. Końcowy log: 0 błędów `Undefined control sequence`, 0 nierozwiązanych odsyłaczy, 0 `Overfull \\hbox`, 0 `Missing character`. Ponownie wyrenderowano strony 19–21 i sprawdzono wizualnie treść konstrukcji uzupełnienia, diagram 3.1 oraz podpisy.

## Decyzja

**Audyt 03/02 CZYSTY (1/2), potwierdzony pełnym CI PASS**, bez zmian w rozdziale. Przed rozpoczęciem rozdziału 04 trzeba wykonać jeszcze niezależny czysty audyt potwierdzający 03/03.
