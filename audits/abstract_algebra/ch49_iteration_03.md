# AA-49 — audyt III: końcowa stabilizacja kwadratowego przypadku Kovacica

**Data:** 23 listopada 2026 r.
**Werdykt: AA-49 STABILNY w określonym, jawnie ograniczonym zakresie.**
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Rozdział:** chapters/pl/abstract_algebra/49-kwadratowy-przypadek-algorytmu-kovacica.tex.
**Blob SHA ostatecznego rozdziału:** 1de4da38c21a5f02a409bd310ff16ecbcef50808.
**Blob SHA testów SymPy:** 2a4a63a050183171c3d56893f1c5d761b6e621e2.
**Blob SHA niezależnego zestawu Fraction:** 4122142ae0d4981aca41bfcd7d141f4e32901a1b.
**Podstawa zakresu:** docs/pl/zakres_aa49_kovacic_kwadratowy.md.

## 1. Trzy audyty i rzeczywiste poprawki

- **Audyt I:** audits/abstract_algebra/ch49_iteration_01.md — konstrukcja oraz kontrola wszystkich hipotez; rozdzielenie dowodów własnych od cytowanego klasycznego twierdzenia o listach lokalnych drugiego przypadku Kovacica.
- **Audyt II:** audits/abstract_algebra/ch49_iteration_02.md — niezależne wyprowadzenia operatora symetrycznego kwadratu i równania śladu, przeliczenie przykładów o stopniu wielomianu pomocniczego 0 i 1 oraz kontrola konieczności niekwadratowego wyróżnika.
- **Poprawka matematyczno-redakcyjna:** dodano przykład q=2/x², gdzie listy E0=E∞={−4,2,8} i wielomian P=1 spełniają równanie trzeciego rzędu, ale Δ=9/x² jest kwadratem w C(x), więc oba pierwiastki Riccatiego są wymierne. Sam dodatni wynik testu P nie wystarcza do stwierdzenia ścisłego stopnia algebraicznego 2. Dodano też test prostego bieguna q=1/x. Commit ae45e1ebcb22954103ad818a25c49804d8326ed3.
- **Pierwsze nieudane CI:** #45176160492 (3 błędy testowego enumeratora E_a) oraz #45176431341 (5 błędów, w tym nowych testów) wykryły pominięcie całkowitego kandydata 2: kod testowy stosował v.is_integer is True do zwykłej liczby Python. Naprawiono oba miejsca przez s.sympify(v).is_integer is True. Nie było błędu w matematycznej formule E_a. Commit 8005eb7ac51e4ea0f3951e3d746c3322a53cc466.
- **Korekta językowa:** „afininiczny” → „afiniczny” w dowodzie eliminacji algebraicznej, commit bc21510f2f17ea26ea5b059ae187b782f9fd0074.
- **Korekta metadanych książki:** po pierwszym zielonym CI i oględzinach PDF uaktualniono komentarz i stronę tytułową z „AA-49 w audycie” na status ukończony, commit 30fe591cf985ee3061fb2a4d529b3a911d7732c9.

## 2. Zamknięte zobowiązania matematyczne

1. **Ślad i wyróżnik.** Dla dwóch różnych sprzężonych rozwiązań Riccatiego r1,r2: φ=r1+r2 należy do C(x), p=r1r2=(φ'+φ²−2q)/2, a Δ=(r1−r2)²=4q−2φ'−φ². Z różnicy równań wynika Δ'=−2φΔ.
2. **Równanie śladu i odzyskiwanie pierwiastków.** Warunek φ''+3φφ'+φ³−4qφ−2q'=0 jest równoważny Δ'=−2φΔ. Gdy Δ≠0, elementy r±=(φ±√Δ)/2 spełniają Riccatiego. Są ściśle kwadratowe dokładnie wtedy, gdy Δ nie jest kwadratem w C(x).
3. **Symetryczny kwadrat.** Dla z1''=qz1 i z2''=qz2 iloczyn v=z1z2 spełnia v'''−4qv'−2q'v=0. Wstawienie v=P exp∫θ i trzykrotne zróżniczkowanie prowadzi bezpośrednio do liniowego operatora P'''+3θP''+(3θ²+3θ'−4q)P'+(θ''+3θθ'+θ³−4qθ−2q')P.
4. **Klasyczne listy lokalne.** Dla biegunów rzędu 1,2,>2 oraz trzech przypadków w nieskończoności zastosowano standardowe listy E_a,E∞; stopień n=(e∞−Σe_a)/2 musi być nieujemną liczbą całkowitą. **Wyczerpujący charakter tych list jest jawnie cytowany z J. Kovacica, Journal of Symbolic Computation 2 (1986), 3–43, i nie jest przedstawiony jako samodzielnie dowiedziony.** Jest to zasadnicza granica zakresu własnych dowodów AA-49.
5. **Skończona procedura warunkowa.** Kombinacji danych lokalnych jest skończenie wiele; dla każdej dopuszczalnej θ,n wyznacza się moniczny P z liniowego układu. Należy rozstrzygnąć istnienie w **całej afinicznej rodzinie** P niekwadratowego, niezerowego Δ, a nie przyjąć dowolne P; w modelu efektywnym zapewnia to eliminacja algebraiczna. Wynik dodatni jest bezpośrednio weryfikowalny, a kompletność korzysta z cytowanego lokalnego twierdzenia.
6. **Przypadki szczególne:** q=0 prowadzi jedynie do rozwiązań wymiernych r=0 albo r=1/(x+c), c∈C. Dla q=x lista stopni n jest pusta w gałęzi drugiej; pełny brak liouvillowskości jest odrębnym wynikiem AA-46. Nie mylić testu drugiej gałęzi z całościowym algorytmem Kovacica.
7. **Pięć sprawdzonych przykładów:** q=x+5/(16x²), n=0, Δ=4x; q=(4x+5)/(16x²), n=1, P=x−1 i Δ=x/(x−1)²; q=1/x−3/(16x²), n=0, Δ=4/x; q=2/x² z kwadratowym Δ; q=x jako negatywny przykład. Dla trzech pierwszych rachunek r±'+r±²=q jest wykonany i regresyjnie sprawdzony.
8. **Związek z Galois:** para sprzężonych linii rozwiązań jest zachowywana jako nieuporządkowany zbiór, co ilustruje normalizator torusa w SL₂(C); właściwa odpowiedniość Galois pozostaje cytowanym twierdzeniem z AA-46.

**Rozdział AA-49:** 5 bloków dowodu, 5 przykładów, 25 unikatowych etykiet. Żaden test skończonych modeli nie zastępuje dowodu klasycznych list lokalnych.

## 3. Ostateczny rzeczywisty GitHub Actions

**Przebieg:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45177895911
**Head SHA zweryfikowanych źródeł i metadanych:** 30fe591cf985ee3061fb2a4d529b3a911d7732c9.
**Status:** completed / success, **90/90 kroków zakończonych sukcesem**.

- Zestaw AA-49 SymPy: **13/13 PASS**.
- Zestaw AA-49 niezależny fractions.Fraction: **10/10 PASS**.
- Pełne regresje narzędzi repozytorium: PASS.
- Bramka AA GLOBAL 01–49: PASS; **49** rozdziałów, **1017** unikatowych etykiet, **0** duplikatów, **537** wystąpień odsyłaczy, **326** różnych celów, **0** nierozwiązanych; w książce **446** środowisk dowodu, **311** przykładów i **239** twierdzeń.
- Zachowano 11 raportów przekrojowych AA-01–AA-42 bez fałszowania ich pokrycia; AA-43–AA-49 mają osobne audyty.
- Pełna kompilacja latexmk, weryfikacja PDF i archiwizacja artefaktu: PASS.

## 4. Artefakt, log i kontrola wizualna

**Artefakt końcowego CI:** abstract-algebra-aa01-aa49, ID **14819314423**.
- Końcowy plik abstract_algebra.pdf: **316 stron**, **2 277 396 B**, SHA-256 **61a7b0edf2d946eb7f5b37a862f2a4497a1164f0bde0a8f41ff7d0bcd3abc3c4**.
- Końcowy abstract_algebra.log: **46 591 B**, SHA-256 **a942af6e80c7ab1353ec317d8dabc918fb0bae7594d28f5a5992b094530d3ad8**.
- Log końcowy: **0** błędów LaTeX, **0** ostrzeżeń LaTeX, **0** ostrzeżeń hyperref, **0** Overfull i Underfull, **0** brakujących odsyłaczy.
- AA-49 zajmuje **6 stron PDF: 311–316**, drukowane 301–306. Każdą stronę wyrenderowano w rozdzielczości dwukrotnie większej i niezależnie obejrzano; brak obcięć, nachodzenia tekstu, usterek wzorów i błędnych łamań.
- W całym PDF przeanalizowano współrzędne **161 888 wyrazów**, **0** poza granicami stron.
- Porównanie ze stabilnym AA-01–AA-48 (310 stron): **308/310 stron bez jakiejkolwiek zmiany warstwy tekstowej**; zmodyfikowano jedynie stronę tytułową i spis treści.
- Porównanie z pierwszym zielonym AA-49 sprzed korekty języka i tytułu: **314/316 stron identycznych tekstowo**; różnice to strona tytułowa i jedna strona ze skorygowanym wyrazem w dowodzie.

## 5. Werdykt

**AA-49 STABILNY w przyjętym, precyzyjnym zakresie.** Zamknięto audyty I–III, rzeczywiste korekty matematyczno-redakcyjne i testowe, obie niezależne serie regresji, pełny zielony CI oraz wizualną kontrolę każdej strony nowego rozdziału. Wyczerpujące listy lokalne Kovacica pozostają *jawnie cytowanym twierdzeniem klasycznym*, a nie samodzielnym dowodem.

**AA-50 NIEOTWARTY:** jego ewentualny zakres to trzeci przypadek Kovacica (grupy skończone, stopnie algebraiczne 4, 6 i 12), wymagający osobnego planu i audytów.
