# Analiza funkcjonalna — rozdział 03 — audyt 03 (potwierdzenie stabilności)

**Data:** 23 listopada 2026 r.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/functional_analysis/03-sieci-struktura-jednostajna-i-zupelnosc.tex.
**SHA źródła:** 5ea236a2bdf75e97e9ef8082340457c9ee9bd0a6 (niezmienione względem audytu 03/02).
**Wynik:** CZYSTY; drugi z dwóch kolejnych czystych audytów **2/2 — rozdział 03 STABILNY**.

## Niezależna kontrola matematyczna — 9/9 dowodów

1. **Sieci a domknięcie i ciągłość.** Odwrotne zawieranie otwartych otoczeń jest relacją skierowaną, a sieć wybranych punktów A∩U jest ostatecznie w każdym zadanym otoczeniu. Dla nieciągłego f można wybrać punkty z obrazami poza ustalonym otoczeniem f(x). Sprawdzono nie-Hausdorffa; PASS.
2. **Kanoniczna struktura jednostajna.** E_U zawiera przekątną; E_{U∩V}=E_U∩E_V, E_V^{-1}⊂E_U przy symetrycznym V i E_V∘E_V⊂E_U przy V+V⊂U. E_U[x]=x−U odtwarza topologię; PASS.
3. **Liniowa ciągłość a jednostajna.** Różnica T(x)−T(y)=T(x−y); kontrola w zerze daje równomierną kontrolę we wszystkich punktach; PASS.
4. **Sieci Cauchy'ego i filtry.** Ogony stanowią bazę filtra, a relacja na parach (A,a) z A∈F, a∈A skierowuje zbiór indeksów: dla A,B używa się A∩B i dowolnego punktu przecięcia. Sprawdzono oba kierunki Cauchy'ego i zbieżności; PASS.
5. **Granice i podsieci.** Zbieżność implikuje Cauchy'ego przez symetryczne V z V+V⊂U; założenie Hausdorffa gwarantuje jednoznaczność; współkońcowość podsieci zapewnia wyraz z wystarczająco późnego ogona sieci Cauchy'ego; PASS.
6. **Zupełność metryzowalnych TVS.** Wybrano malejącą przeliczalną bazę otoczeń i indeksy e_n rosnące względem kierowania; e_n po n≥N dominuje d_N, zatem powstaje ciąg Cauchy'ego. Zbieżność wybranego ciągu przenosi się na całą sieć; PASS.
7. **Podprzestrzenie i produkty zupełne.** Poprawne warunki domkniętości i Hausdorffa; zupełność produktu równoważna zupełności czynników, odwrotność przez domknięte kopie czynników. Sprawdzono pustą rodzinę I; PASS.
8. **Uzupełnienie dowolnej TVS Hausdorffa.** Przeanalizowano osobno pięć etapów:
   - Przeindeksowanie sieci Cauchy'ego na zbiór skończonych rodzin otoczeń usuwa problem klasy właściwej; relacja równoważności jest zwrotna, symetryczna (po symetryzacji otoczeń) i przechodnia; działania na klasach niezależne od reprezentantów.
   - Definicja widehat U wymaga stałego „marginesu” V: x_d+V⊂U ostatecznie. Przy zmianie przedstawiciela **symetryczne** W z W+W⊂V pozwala poprawnie odwrócić różnicę. Sprawdzono zawieranie małych otoczeń, topologię addytywną i równość j^{-1}(widehat U)=U.
   - Gęstość j(X) uzyskuje się przez klasy późnych wyrazów pierwotnej sieci; ciągłość mnożenia skalarnego w zerze dla ustalonego z korzysta z przybliżenia przez j(X), następnie z rozkładu λz−λ₀z₀.
   - Zupełność: dla sieci Cauchy'ego (z_α) dobór x_{α,U} w X daje sieć Cauchy'ego z parametrem U malejącym; suma trzech różnic kontroluje zbieżność z_α do klasy nowej sieci.
   - Przedłużenie do zupełnej Y: T zachowuje sieci Cauchy'ego, definicja widehat T przez granicę nie zależy od przedstawiciela, a ciągłość wynika z domknięcia V zawartego w V+V i z gęstości. PASS.
9. **Kryterium uzupełnienia.** Ciągłe odwzorowanie R₀ na gęstej podprzestrzeni T(X) jest jednostajnie ciągłe; limity obrazów sieci Cauchy'ego są niezależne od wyboru sieci, R jest ciągłe w zerze, a S i R są odwrotne przez równość na zbiorach gęstych. PASS.

**Wynik dowodów: 9/9 PASS.** Nie znaleziono kolejnej matematycznej luki ani powodu do modyfikacji źródła.

## Ponowna kontrola przykładów — 3/3 PASS

1. Sigma(I)⊂K^I dla I nieprzeliczalnego: jest gęsta dzięki skończenie wspartym przybliżeniom indeksowanym skończonymi zbiorami, ale właściwa i ciągowo domknięta.
2. Sigma(I) jest ciągowo zupełna, lecz niezupełna: ciągi zachowują przeliczalne nośniki, a sieci Cauchy'ego w produkcie mogą mieć granicę o nieprzeliczalnym nośniku.
3. Uzupełnienia c_00→ℓ^p, C([0,1])→L¹ oraz c_00→K^N z topologią produktową: każde osadzenie jest liniowe, topologiczne i ma gęsty obraz w zupełnej przestrzeni.

## Kontrole brzegowe i redakcja

- Rozróżnienie zbieżności ciągów i sieci, domkniętości i ciągowej domkniętości oraz zupełności i ciągowej zupełności; bez błędnych uogólnień.
- Przypadki λ=0, z=0, sieci stałych, pustych produktów, otoczeń nieotwartych oraz wartości zespolonych są zgodne z założeniami.
- Przykład x_n=1−1/n i y_n=1+1/n obala nieprawidłową wersję definicji widehat U bez stałego marginesu; aktualne sformułowanie jest prawidłowe.
- Zachowano 15 unikatowych etykiet, 5 lokalnych odsyłaczy, 9 środowisk proof i 3 środowiska przyklad. Stosowana forma „ciągowo zupełna”, a nie „sekwencyjnie”; symbol W₀ jednolity.
- Schemat 3.1 i strony 15–22 zweryfikowane wizualnie na niezmienionym źródle: czytelne etykiety, brak kolizji tekstu z rysunkiem i brak ucięć.

## Walidacja techniczna

- Aktualne źródło i 14 testów regresyjnych są identyczne z przebiegiem [45156438672](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156438672): **SUCCESS** we wszystkich etapach — testy 14/14, kompilacja dokumentu z realnym kontekstem 01–05, kontrola odsyłaczy i logu oraz artefakt PDF.
- Poprzedni niezależny przebieg [45156131987](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45156131987) również zakończył się pełnym SUCCESS.
- W iteracji 03/03 nie zmieniano tekstu ani testów; weryfikacja dotyczy dokładnie wersji źródła z audytu 03/02.

## Decyzja

**CZYSTY AUDYT 03/03 — drugi z dwóch kolejnych czystych audytów. Rozdział 03 oznaczono STABILNYM.** Zgodnie z przyjętym procesem następnym rozdziałem do kontroli jest **04: Zbiory ograniczone, rodziny operatorów i metryzowalność TVS**. Nie przenosimy żadnych niezatwierdzonych rozszerzeń do ustabilizowanego rozdziału 03.
