# Topologia algebraiczna — szczegółowy audyt AT-03 i AT-04

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Metoda:** audyt dwóch kolejnych rozdziałów, w standardzie szczegółowości DG-01; każde stwierdzenie kontrolowane pod kątem zakresu założeń, kroków dowodowych, przykładów, języka, rysunków i integralności odsyłaczy.

## AT-03 — Algebra homologiczna: moduły, kompleksy i (ko)homologie

Przeanalizowano definicje torsji, dokładności, kompleksów i homologii; konstrukcję odwzorowania łączącego w długim ciągu dokładnym, odpowiednik kohomologiczny, dualność nad ciałem, homotopię łańcuchową, algebraiczne skracanie par generatorów, ciągi względne, filtracje, ciąg Mayera–Vietorisa, zmianę współczynników i charakterystykę Eulera.

### Istotne znaleziska i korekty

1. **Błędny porządek iloczynu w dowodzie kasowania pary** (twierdzenie `thm:kasowanie-pary`). Dla wolnych lewych modułów nad dowolnym pierścieniem ze skalarnym elementem odwracalnym `u`, z równości `∂e=uf+v` i `∂x=a(x)f+w` wynika konieczna korekta `x'=x-a(x)u^{-1}e`, nie `x-u^{-1}a(x)e`. Nowa postać daje `∂x'=w-a(x)u^{-1}v` także bez przemienności pierścienia. Dodano jawny kontrprzykład macierzowy w `M_2(Z/2Z)`, w którym obie kolejności są różne.
2. **Zakres konstrukcji `Hom_R`** (`prop:kompleks-dualny`). `Hom_R(C_n,G)` dla lewych modułów nad pierścieniem nieprzemiennym jest zawsze grupą abelową, ale nie ma ogólnie naturalnej struktury lewego `R`-modułu. Doprecyzowano założenie przemienności `R` w twierdzeniu i podano działanie `(rφ)(c)=rφ(c)`. Nie zawężono przez to niezależnych twierdzeń o zwykłych kompleksach lewych modułów.
3. **Zbyt skrótowa własność torsji.** Dodano sprawdzenie, że elementy zabijane przez niezerową liczbę całkowitą tworzą podgrupę i że `A[m]` jest jądrem mnożenia przez `m`.
4. **Rozbudowa rachunkowego przykładu zmiany współczynników.** Dla kompleksu `C_2=Z`, `C_1=Z^2`, `C_0=Z` z `∂_2(t)=(0,2t)`, `∂_1(x,y)=x` obliczono homologiczne grupy nad `Z` i po redukcji modulo `2`. Nowa klasa `H_2(C/2C)` jest wykrywana przez `δ_2[1]=[(0,1)]` w `H_1(C)[2]`, podczas gdy `H_1(C/2C)` pochodzi z ilorazu `H_1(C)/2H_1(C)`. Dodano drugi rysunek TikZ z mapami w obu wierszach.
5. **Terminologia polska.** Usunięto formy zakazanego słowa „tensorowanie” i zastąpiono je konsekwentnym zapisem „iloczyn tensorowy” lub „zastosowanie funktora `-\otimes_R S`”.

Zachowano wcześniejsze etykiety, w szczególności `ch:algebra-homologiczna`, `thm:les-homologia`, `thm:mod-m-homologia` i `thm:kasowanie-pary`, oraz wszystkie wcześniejsze warianty dowodów i przykłady.

## AT-04 — Homotopia, nakrycia i komórkowe modele przestrzeni

Przejrzano definicje homotopii i grupy podstawowej, jej funktorialność i zależność od punktu bazowego; podnoszenie dróg i homotopii, kryterium podnoszenia, konstrukcję nakrycia uniwersalnego, opis nakryć przez podgrupy, twierdzenie van Kampena, sympleksy, struktury `\Delta` i CW oraz dołączanie komórek.

### Istotne znaleziska i korekty

1. **Za mało rachunkowego uzasadnienia nakrycia `q_m(z)=z^m`.** Dodano dowód na równomiernie nakrytych łukach: dla `m≥1` nad małym łukiem jest dokładnie `m` rozłącznych arkuszy o argumentach `(t+k)/m`.
2. **Brak przykładu odróżniającego lokalną trywialność od globalnego przekroju.** Wprowadzono przykład `prz:nakrycie-m-arkuszy` z dowodem, że `(q_m)_*:π_1(S^1)→π_1(S^1)` jest mnożeniem przez `m` i ma obraz `mZ`. Gdyby dla `m≥2` istniał globalny przekrój, funktorialność wymuszałaby surjektywność mnożenia przez `m`, sprzeczną z `1\notin mZ`. Dodano rysunek `fig:nakrycie-m-arkuszy`.
3. **Nieścisłość sformułowania postaci zredukowanej w iloczynie wolnym**, używanego w twierdzeniu van Kampena. Poprzedni opis sugerował, że niepuste słowo musi zawierać litery z obu czynników; doprecyzowano możliwość słowa jednoelementowego i warunek naprzemienności sąsiednich czynników.

Zachowano wcześniejsze etykiety, m.in. `ch:topologia-algebraiczna-podstawy`, `thm:pi1-okragu`, `thm:van-kampen`, `thm:uniwersalne-nakrycie` i `thm:pi1-dolaczenie-komorki`.

## Integralność, ilustracje i sposób weryfikacji

- W AT-03/04 łącznie było **66** wystąpień standardowych `\ref` i `\eqref` przed poprawkami; wszystkie cele znajdowały się już w zbiorze oryginalnych etykiet rozdziałów AT-01 do AT-04. Nowe odsyłacze lokalne nie powinny tego naruszyć.
- Etykiety w czterech rozdziałach są unikalne w tym zestawie; audyt nie wymaga żadnego automatycznego przepisania istniejących `\label`.
- Rysunki są osadzone w LaTeX przez TikZ. W obu rozdziałach nie wykryto instrukcji `\input` wymagających dodatkowych plików ani zewnętrznych plików graficznych bądź danych.
- `application/tests/test_topology_chapters_03_04.py` sprawdza m.in. zależności, pełność odsyłaczy w czterorozdziałowym zestawie, etykiety, zgodność środowisk, niedozwoloną terminologię, poprawność kolejności mnożenia macierzy `M_2(Z/2Z)` oraz przykład homologiczny i nakrycie.
- `.github/workflows/algebraic-topology-audit-ch03-04.yml` buduje PDF z AT-01–04, używając **dwóch wcześniejszych rozdziałów wyłącznie jako kontekstu dla odsyłaczy**, po czym sprawdza podwójną kompilację, brak niezdefiniowanych odsyłaczy i przepełnionych wierszy. Nie oznacza to ponownego merytorycznego audytu AT-01 i AT-02.

## Retest i zatwierdzenie

- [GitHub Actions — testy aplikacji #44759080700](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44759080700), commit `85252ad93f5d3666e0e0c4020276d1477bc9bc3f`: **SUCCESS**, **130 testów Python, 1 pominięty**, testy Chromium, indeksu i podglądu odsyłaczy zaliczone.
- [GitHub Actions — kompilacja TeX #44759080408](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44759080408), ten sam commit: **SUCCESS**, dwa przebiegi `pdflatex`, **44 strony A4**, bez niezdefiniowanych odsyłaczy i bez przepełnionych wierszy. Artefakt `algebraic-topology-audit-ch03-04-pdf` zawiera PDF i logi.
- Zbadano wizualnie po wyrenderowaniu wszystkie **9 rysunków** w AT-03–04 (AT-03: 2; AT-04: 7). Nie wykryto nachodzących podpisów ani obciętych elementów. Zestawienie rysunków pochodzi ze stron PDF 18, 28, 32, 34, 36, 39, 41, 42 i 43.
- W bieżącej migawce aplikacji jest **355** rozdziałów; nadal **14** nierozwiązanych wystąpień z DG, nie z audytowanych AT-03–04. Nowe etykiety nie spowodowały nierozstrzygniętych odsyłaczy.
- AT-03 i AT-04 mają status **`zaakceptowany`**, w rejestrze `application/data/AUDYT_ROZDZIALOW.csv`. Test PDF obejmuje także AT-01/02 ze względu na odsyłacze, ale nie jest ponownym audytem matematycznym tych rozdziałów.

**Następne do audytu (osobna iteracja): AT-05 i AT-06** — homologia przestrzeni oraz wyższe grupy homotopii i ich związek z homologią.

Nie wykonano scalania skryptów, zmian w `main` ani przenumerowania źródłowych etykiet.
