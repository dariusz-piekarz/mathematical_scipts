# Teoria miary — audyt VI: wyłącznie rozdział 01

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.
Rozdział: `chapters/pl/measure_theory/01-rodziny-zbiorow-i-przestrzenie-mierzalne.tex`.
**Status: drugi kolejny czysty audyt matematyczno-statyczny po ostatniej poprawce; formalna stabilizacja nadal wstrzymana do kompilacji aktualnej książki i oceny PDF.**

## Proweniencja

Na początku odczytano HEAD gałęzi `c734a1ff5894ea224aaf71c0b5890da8149f0fee`, listę raportów (I–V) i najnowsze commity, a następnie źródło R01: blob `a7c8610bf1eb9e4612e96df9f038679af4d4d2fb`, 537 linii. Odczytano poprzedni raport V, plik główny `books/pl/measure_theory.tex`, `AGENTS.md` i `docs/pl/standardy_terminologiczne.md`. W kontekście sprawdzono strukturę odrębnego `books/pl/integration_theory.tex`; nie scalano skryptów i nie audytowano R02 ani R03–R31. Źródło R01 pozostało niezmienione.

## Pełny ponowny przegląd matematyczny R01

Przeprowadzono niezależną kontrolę wszystkich sześciu sekcji i wszystkich dziewięciu bloków twierdzenie/lemat, w tym:
1. Aksjomaty pierścienia, algebry i σ-algebry; sprawdzenie przypadków w rodzinie skończono-kofinitywnej i rozbicia przeliczalno-koprzeliczalnego; algebra wyznaczona przez podział.
2. Przekroje σ-algebr, minimalność σ-algebry generowanej, σ-algebra śladowa i rosnąca suma σ-algebr `\mathcal F_n` na `\mathbb N`; w ostatnim przykładzie zweryfikowano obie inkluzje między sumą rodzin i algebrą skończono-kofinitywną.
3. Lemat o układzie Dynkina zamkniętym na przekroje, dowód π–λ przez dwie pomocnicze rodziny Dynkina, weryfikacja wszystkich operacji użytych w ich definicjach.
4. Twierdzenie o klasie monotonicznej: domknięcie na dopełnienia, następnie sumy dwuargumentowe i przeliczalne; obie inkluzje w tezie.
5. Generatory borelowskie na R i R^d: wymierna baza, wzory na półproste i ciągłość rzutów współrzędnych.
6. Kryterium mierzalności przez generatory, składanie odwzorowań, działania na funkcjach rzeczywistych i nieciągłość funkcji `\chi_{\mathbb Q}`.

**Nie stwierdzono nowej fałszywej tezy ani luki dowodowej wymagającej korekty źródła.** W R01 są 7 definicji, 8 twierdzeń, 1 lemat, 8 przykładów i 5 uwag. Każde z 9 twierdzeń/lematów ma blok dowodu. Rozdział nie zawiera rysunków.

## Niezależny test modelu skończonego

Uruchomiono enumeracyjny test rodziny `\mathcal D=\{\varnothing,X,\{1,2\},\{3,4\},\{1,3\},\{2,4\}\}`, kodując podzbiory `X=\{1,2,3,4\}` jako maski bitowe `[0,15,3,12,5,10]`. Sprawdzono wszystkie 6 dopełnień, 36 uporządkowanych par dla różnic zbiorów zagnieżdżonych i sum rozłącznych oraz wszystkie 64 podrodziny, z których 16 jest parami rozłącznych. **Wynik: zero naruszeń aksjomatów układu Dynkina**. Równocześnie wykryto brak domknięcia na przekroje: `3 & 5 = 1`, czyli `\{1,2\}\cap\{1,3\}=\{1\}\notin\mathcal D`. Jest to odrębne wykonanie testu, a nie deklaracja testu z poprzedniego raportu.

## Statyczna kontrola źródła

Ponownie wykonano kontrolę aktualnego bloba: **19 etykiet bez duplikatów**, **12 odsyłaczy**, z których 10 prowadzi do etykiet R01, a dwa do `ch:miary-wlasnosci` w R02; **43 prawidłowo sparowane pary środowisk**, brak niedomkniętych środowisk. Brak zapisów `\mathbf{1}`, `\mathbb{1}`, `\mathds{1}`. Bez zmian stabilnych etykiet i odsyłaczy.

## Kompilacja, PDF i CI — uczciwe ograniczenia

W tej iteracji nie uruchomiono pełnej kompilacji książki ani nie wykonano kontroli wizualnej PDF. Lokalny kontener ma `pdflatex` i `latexmk`, lecz `git ls-remote https://github.com/dariusz-piekarz/mathematical_scipts.git` zwrócił błąd DNS `Could not resolve host: github.com`; nie dysponowano lokalnie pełnym checkoutem 31 rozdziałów i suplementów. Z tego powodu **nie wolno traktować statycznego sprawdzenia jako zastępnika kompilacji**. Zapytanie o przebiegi GitHub Actions dokładnie dla commita raportu V `0cb1d194deeeab4ab6284e7301dbb8fce1060607` zwróciło pustą listę; nie jest to ani pozytywny, ani negatywny wynik CI. Poprzedni raport V potwierdzał sukces obu workflow dla wcześniejszego commita źródła `c426ca4e24462ae009bfff2e76a0f7e72837858c`, ale nie zastępuje to pełnego buildu książki.

## Stabilizacja i kolejny krok

**R01: dwa kolejne czyste audyty merytoryczno-statyczne (V i VI), bez zmiany źródła po audycie IV; formalnie NIESTABILNY z powodu brakującej pełnej kompilacji i kontroli PDF.** W kolejnej iteracji pozostać przy R01, pozyskać kompletny checkout (lub zweryfikowany artefakt PDF z bieżących źródeł), wykonać pełny build i ocenę wizualną oraz sprawdzić ewentualne nowe ostrzeżenia odsyłaczy. Dopiero po tych czynnościach potwierdzić stabilność i w następnej iteracji rozpocząć R02. Nie dodawać nowych twierdzeń bez zgody.
