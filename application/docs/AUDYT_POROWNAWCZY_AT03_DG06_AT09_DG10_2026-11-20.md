# Audyt porównawczy AT-03 / DG-06 oraz AT-09 / DG-10 — etap II

**Data:** 20 listopada 2026 r.
**Repozytorium:** dariusz-piekarz/mathematical_scipts.
**Gałąź:** biblioteka-matematyczna-iteracja-6. Nie zmieniano main.
**Przedmiot:** analiza twierdzenie po twierdzeniu i dowód po dowodzie dwóch par rozdziałów o dużym nakładaniu się treści.
**Zasada bezstratności:** zachować wszystkie oryginalne etykiety, twierdzenia, hipotezy, wartościowe warianty dowodów, przykłady, kontrprzykłady i rysunki. Fizycznego scalania jeszcze nie wykonano.

## 1. Wyniki porównania źródeł

| Para | Wspólne nazwy etykiet | Unikalne AT | Unikalne DG | Współczynnik Jaccarda istotnych linii tekstu |
|---|---:|---:|---:|---:|
| AT-03 / DG-06 — algebra homologiczna | 62 | 7 | 10 | 0,607 |
| AT-09 / DG-10 — formy i de Rham | 60 | 4 | 1 | 0,714 |

Współczynnik jest tylko miarą identycznych linii po uproszczeniu odstępów. Równe etykiety ani zbliżone akapity nie dowodzą matematycznej równoważności twierdzeń.

## 2. AT-03 i DG-06 — szczegółowe rozbieżności

### Dokładność i rozszczepienie
Twierdzenie thm:ses-rozszczepienie w obu źródłach dowodzi równoważności istnienia przekroju, retrakcji i zgodnego z danym rozszerzeniem rozkładu na sumę prostą. DG dokładniej precyzuje zgodność izomorfizmu z obiema strzałkami; przy scalaniu zachować to sformułowanie i pełne uzasadnienie niezależności podniesień.

### Długie ciągi homologii i kohomologii
Twierdzenia thm:les-homologia i thm:les-kohomologia konstruują homomorfizm łączący poprzez podniesienie cyklu albo kocyklu i obliczenie różniczki. DG podaje dodatkowo przykład, w którym odwzorowanie łączące jest mnożeniem przez m; AT ma inny przykład, gdzie jest identycznością. Zachować oba, gdyż ilustrują różne zjawiska. W docelowym tekście jawnie zweryfikować niezależność podniesienia, niezależność reprezentanta, naturalność i wszystkie trzy rodzaje miejsc dokładności.

### Dualność Hom
Twierdzenie prop:kompleks-dualny w AT lokalnie zakłada przemienność pierścienia R, podczas gdy DG korzysta z globalnej konwencji rozdziału. W wersji scalonej sformułować tę hipotezę w samym twierdzeniu: dla nieprzemiennego R grupa Hom_R między lewymi modułami nie jest automatycznie lewym R-modułem.

### Rzeczywisty błąd: kasowanie generatorów nad R nieprzemiennym
W AT-03 twierdzenie thm:kasowanie-pary obejmuje wolne lewe moduły nad pierścieniem z jedynką, niekoniecznie przemiennym. Przy założeniach d(e)=u f+v oraz d(x)=a f+w, poprawna zmiana generatora jest x'=x−a u⁻¹ e; odwrotna to x=x'+a u⁻¹ e. AT miało w drugim z tych równań niewłaściwą kolejność czynników u⁻¹ a. Poprawiono rzeczywistą pomyłkę matematyczną i dodano wyjaśnienie.
Jawny test w R=M₂(F₂) z u=[[1,1],[0,1]] i a=[[0,0],[1,0]] potwierdza, że a u⁻¹ != u⁻¹ a oraz (a u⁻¹)u=a. Przemienny rachunek DG pozostaje poprawny przy tamtejszych założeniach. Zachować uogólnienie AT oraz szczegółowy przykład macierzy całkowitoliczbowej DG.

### Redukcja modulo m
Twierdzenie thm:mod-m-homologia w obu plikach wyprowadza dokładny ciąg
0 -> H_n(C)/mH_n(C) -> H_n(C/mC) -> H_(n-1)(C)[m] -> 0
przy stopniowej iniektywności mnożenia przez m. Wystarczającą hipotezą jest wolność grup łańcuchów. DG dokładniej rozpisuje niezależność odwzorowania łączącego od wyboru podniesienia, a także ostrzega przed błędnym zastosowaniem do kompleksów z grupami niosącymi torsję m. AT wnosi trzywyrazowy przykład, gdzie nowa klasa pojawia się w stopniu drugim. DG wnosi inny, z dwiema niezależnymi klasami modulo 2 w stopniu pierwszym. Oba są niezbędne.

### Dualność algebraiczna nad ciałem
Twierdzenie thm:field-hom-dual dotyczy algebraicznego dualnego kompleksu, nie dualnego topologicznego. Dobór dopełnień podprzestrzeni wystarcza; skończony wymiar jest tylko szczególną wystarczającą hipotezą.

### Lemat pięciu
Dowód wspólny dla etykiety lem:pieciu wykorzystuje jedynie: surjektywność f1, izomorfizmy f2 i f4, iniektywność f5. Poprzednio AT wymagało czterech izomorfizmów skrajnych; zastąpiono ten zbędnie mocny warunek wersją optymalną i pozostawiono dotychczasowe wymagania jako przypadek szczególny. DG zachowuje dodatkowy przykład niediagonalnego środkowego homomorfizmu i wniosek dla quasi-izomorfizmów krótkich ciągów kompleksów.

### Unikalne źródłowe etykiety, których nie wolno utracić
AT-03:
sec:moduly, def:torsja, thm:modul-izomorfizm, prz:delta-izomorfizm, uwaga:nieprzemienny-pivot-top, prz:redukcja-mod2-trzy-stopnie, fig:redukcja-mod2-top.

DG-06:
prz:ses-z2, prz:ses-dwa-rozszerzenia, prz:homologia-alg-trojkat, fig:homologia-alg-trojkat, prz:homologia-mapa-mod-m, prz:delta-razy-m, fig:filtracja-klasy, fig:mv-dwa-luki, prz:mod2-dwa-zrodla, wn:pieciu-ses-kompleksy.

## 3. AT-09 i DG-10 — szczegółowe rozbieżności

### Operator homotopii i lemat Poincarégo
Obie wersje wprowadzają rozkład H*ω=dt∧a+b. DG szczegółowiej wykazuje, że rodziny a(t), b(t) są globalnie określone, zgodne ze zmianami map i z całkowaniem po parametrze. Zachować ten pełniejszy argument. AT dodaje jednak osobne kryterium globalnej funkcji pierwotnej dla 1-form, sformułowane za pomocą wszystkich całek po zamkniętych drogach, wraz z przykładem niezerowego okresu. Nie zastępować go samym lokalnym lematem Poincarégo.

### Orientacja i Stokes
Obie wersje uwzględniają orientację brzegu „normalna na zewnątrz najpierw” i hipotezy nośnika zwartego. DG szerzej uzasadnia przejścia w mapach przybrzegowych, AT zachowuje odrębny przykład pierścienia o dwóch składowych brzegu z przeciwnymi orientacjami i własny rysunek. W DG-10 usunięto dwa ozdobne zastosowania \boxed dla wzorów Cartana i Stokesa bez zmiany samych równości i etykiet.

### Dokładność Mayera–Vietorisa
W twierdzeniu thm:mv-de-rham stosujemy s(α,β)=β|_(U∩V)−α|_(U∩V). AT-09 poprzednio pomijało rachunek niezależności od podniesień i reprezentantów. Rozwinięto go, sprawdzając:
1. dla zamkniętej γ podniesienie (α,β) i zamkniętą formę sklejoną η;
2. poprawną lokalną postać η=dρ_U∧γ=−dρ_V∧γ;
3. zmianę podniesienia o globalne ograniczenia formy λ oraz zmianę η o dλ;
4. zastąpienie γ przez γ+dθ i odpowiednią zmianę podniesienia;
5. dokładność w miejscu grupy kohomologii przecięcia, w obu kierunkach.
Dowód DG ma analogiczną kontrolę, choć rozkłada ją na inne akapity. Po przyszłym scaleniu wystarczy jeden pełny dowód z zachowaniem obu istotnych wyjaśnień.

### Twierdzenie de Rhama
Oba źródła mają długi argument oparty na gładkich łańcuchach singularnych, podziale małych łańcuchów, totalizacji tabel Čech, lokalnych homotopiach i podziałach jedności. Zgodność etykiety thm:de-rham nie zastępuje kontroli technicznych lematów, które należy jeszcze oddzielnie przeanalizować przed scaleniem. Nie deklarujemy pełnej niezależnej rederywacji wszystkich narzędzi sklejania.

### Unikalne źródłowe etykiety, których nie wolno utracić
AT-09:
thm:forma-okresy-pierwotna, prz:okres-1-formy-pierwotna, prz:stokes-pierscien-dwa-brzegi, fig:stokes-pierscien.

DG-10:
prz:formy-rachunek-r3.

Wspólne przykłady pod identycznymi etykietami również nie są bajtowo równe: DG daje więcej szczegółów przy obliczaniu okresów na okręgu i torusie oraz przy przejściach przez Mayera–Vietorisa na sferach.

## 4. Wykonane zmiany i ochrona regresyjna

- Poprawiono AT-03: kolejność współczynników w nieprzemiennym dowodzie eliminacji i minimalne założenia lematu pięciu.
- Poprawiono AT-09: pełny rachunek strzałki łączącej Mayera–Vietorisa.
- W DG-06 i DG-10 ujednolicono terminologię „kołańcuch” w miejsce „kochain”, bez renumeracji etykiet.
- W DG-10 usunięto dekoracyjne obramowanie dwóch formuł zgodnie z globalnym stylem.
- Dodano application/config/KANDYDACI_SCALEN_AT_DG_ETAP_02.json, zawierający wszystkie unikalne etykiety, różnice założeń i jawne approved_to_merge=false.
- Dodano application/tests/test_at_dg_pairwise_03_06_09_10.py z 11 testami, w tym obliczeniem nad M₂(F₂), modelowym Mayerem–Vietorisem S¹, kontrolą historycznych etykiet i ochroną list unikalnych przykładów.
- Dodano .github/workflows/paired-at-dg-cohomology-homology-audit.yml, budujący AT i częściowy DG osobno.

Żaden z tych kroków nie nadał nowego kanonicznego właściciela dowodom ani nie usunął źródłowych plików. Rejestr jest planem przygotowawczym, a nie pozornie dokonanym scaleniem.

## 5. Kontrola wykonalności

W przebiegu GitHub Actions 44827422851:
- regresje porównawcze (wówczas 10 testów) — SUCCESS;
- AT-01–30: 295 stron A4 po trzech przebiegach pdflatex, brak niezdefiniowanych referencji, nieustabilizowanych etykiet i poziomych przepełnień;
- DG-01–10: 269 stron A4 po trzech przebiegach pdflatex i bez poziomych przepełnień. Pozostały wyłącznie cztery jawnie dopuszczone odsyłacze wybiegające poza zakres częściowej kompilacji: sec:kolnierz-15, sec:uchwyt-morse-17, thm:poincare-hopf-16, thm:holonomia-lokalny-produkt.
Późniejsza regresja manifestu zwiększyła liczbę testów do 11. Wszystkie 11/11 zaliczono także w osobnym zadaniu audytu AT w przebiegu 44827860688; pełny workflow aplikacji zaliczył je w przebiegu 44827579549. Weryfikacje wizualne wykonano na rzeczywistych plikach PDF, m.in. stronach AT 29 i 111 oraz DG 171 i 260.

Ograniczenie: złożenie DG-01–10 jest osobnym kontrolnym wycinkiem 269 stron, nie kompletnym dokumentem wszystkich 36 docelowych rozdziałów DG. Nie ma automatycznej gwarancji pełnej poprawności pozostałych 13 niewyjaśnionych odsyłaczy w obecnym DG-01–20.

## 6. Dalsza praca

Audyt porównawczy dwóch par zakończono z rzeczywistymi poprawkami. **Nie należy jeszcze scalać plików**: zachować unikalne dowody i przykłady, opracować przestrzeń nazw dla 304 wielotomowych kolizji etykiet, uzupełnić DG-21–36 i wtedy sprawdzić 13 odsyłaczy zależnych od tego importu.

Następna naturalna para przeglądu to AT-04/DG-07 (homotopia, nakrycia, CW), a kolejna AT-05/DG-08 (homologia). Kontynuować szczegółową kontrolę twierdzeń, dowodów, rysunków i unikalnych przykładów przed jakimkolwiek przenoszeniem treści.
