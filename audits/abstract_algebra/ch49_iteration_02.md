# AA-49 — audyt II: niezależne obliczenia i granice kompletności algorytmu

**Data:** 23 listopada 2026 r. **Werdykt: NIE STABILNY (CI i PDF wymagają odrębnego zakończenia).**
**Rozdział:** chapters/pl/abstract_algebra/49-kwadratowy-przypadek-algorytmu-kovacica.tex.

## 1. Niezależne wyprowadzenie tożsamości (bez korzystania z raportu I)

Niech r1, r2 będą różnymi rozwiązaniami r' + r² = q sprzężonymi nad K=C(x); różniczkowanie komutuje z automorfizmem sprzężenia. Połóżmy φ=r1+r2, p=r1r2, δ=r1−r2, Δ=δ². Z równania φ'=2q−(r1²+r2²)=2q−φ²+2p otrzymujemy p=(φ'+φ²−2q)/2, a więc Δ=φ²−4p=4q−2φ'−φ². Odejmując równania Riccatiego: δ'=−φδ, zatem Δ'=−2φΔ. To w szczególności daje nieliniowe równanie śladu φ''+3φφ'+φ³−4qφ−2q'=0.

Odwrotnie, dla wymiernego φ spełniającego to równanie i Δ≠0 mamy Δ'=−2φΔ. Niech δ²=Δ w rozszerzeniu algebraicznym. Ponieważ char K=0, δ'=Δ'/(2δ)=−φδ, skąd dla r±=(φ±δ)/2 zachodzi r±' + r±² = φ'/2 + φ²/4 + Δ/4=q. Warunek [K(r±):K]=2 jest równoważny temu, że Δ **nie jest** kwadratem w K. Jeśli Δ jest kwadratem, procedura musi odrzucić kandydata jako drugą gałąź, choć rozwiązanie wymierne może istnieć.

## 2. Symetryczny kwadrat i operator trzeciego rzędu

Dla z1''=qz1, z2''=qz2 iloczyn v=z1z2 spełnia v''=2qv+2z1'z2' oraz v'''=2q'v+4qv'. Jeżeli φ=v'/v, to v'''/v=φ''+3φφ'+φ³. Stąd równanie śladu. Gdy φ=θ+P'/P i Dv0=θv0, v=Pv0, rozwinięcie (D+θ)^3(P) daje:
P''' + 3θP'' + (3θ²+3θ'−4q)P' + (θ''+3θθ'+θ³−4qθ−2q')P=0.
To jest dokładnie liniowy operator użyty do testowania P monicznego określonego stopnia; mnożenie przez mianownik i porównanie współczynników kończy się skończonym układem liniowym.

W tej części nie potrzebujemy twierdzenia o klasyfikacji lokalnej. Klasyczne listy lokalne Kovacica E_a,E∞ są **osobnym, jawnie cytowanym twierdzeniem**. Te listy są elementem konieczności algorytmu, a nie wynikiem powyższych rachunków.

## 3. Niezależna kontrola lokalnych danych i przykładów

- **q=x+5/(16x²):** przy 0 b=5/16, sqrt(1+4b)=3/2, E0={-1,2,5}. ord∞ q=-1, E∞={-1}; wybór e0=e∞=-1 daje n=0 i θ=−1/(2x). P=1 spełnia operator trzeciego rzędu. Wyróżnik Δ=4x ma nieparzystą krotność zera przy 0, więc nie jest kwadratem. r±=−1/(4x)±√x.
- **q=(4x+5)/(16x²):** biegun 0 jak wyżej, ale ord∞ q=1, E∞={1}. Wybór e0=-1 daje n=1. Dla θ=−1/(2x) liniowy operator na P=x+c daje c=−1. Przy P=x−1 dostajemy φ=−1/(2x)+1/(x−1), Δ=x/(x−1)² i r±=−1/(4x)+1/(2(x−1))±√x/(2(x−1)). Delta nie jest kwadratem w C(x).
- **q=1/x−3/(16x²):** b0=−3/16, sqrt(1+4b0)=1/2, E0={1,2,3}, ord∞ q=1 i E∞={1}. e0=e∞=1 daje n=0, θ=1/(2x), P=1. Delta=4/x i r±=1/(4x)±1/√x; sprawdzenie r±' + r±²=q wymaga skrócenia członów x^{-3/2}.
- **q=2/x² jako obowiązkowy wynik negatywny:** E0=E∞={−4,2,8}, e0=e∞=2 daje n=0, θ=1/x i P=1 spełnia operator. Ale Δ=9/x²=(3/x)² jest kwadratem w K. Pierwiastki 2/x oraz −1/x są wymierne, więc **nie jest** to drugi przypadek Kovacica. Ten przykład dodano do rozdziału i regresji w commicie ae45e1ebcb22954103ad818a25c49804d8326ed3.
- **q=1/x:** jedyny skończony biegun jest prosty, E0={4}, ord∞ q=1, E∞={1}. Stopień n=(1−4)/2 jest ujemny i niecałkowity: druga gałąź odrzucona już w pierwszym etapie.
- **q=x (Airy):** brak biegunów skończonych, E∞={−1}, n=−1/2, brak kandydatów drugiej gałęzi. Silniejszy brak liouvillowskości jest uzasadniony osobno w AA-46, nie wnioskiem z samego testu drugiej gałęzi.

## 4. Kompletność warunkowa i implementacja

Dla dowolnego ściśle kwadratowego r, **cytowane twierdzenie Kovacica** gwarantuje jedną z kombinacji lokalnych e, stopień n≥0 i P spełniający operator. Każde takie P daje wymierny φ i wyróżnik Δ. Filtr Δ≠0, Δ nieskwadratowe, jest konieczny i dostateczny do odróżnienia rozwiązania ścisłego stopnia 2 od gałęzi wymiernej. Test kwadratowości wymiernego Δ można wykonać na parzystości wykładników nierozkładalnych czynników licznika i mianownika.

Zagadnienie, czy istnieje odpowiednie P w **całej afinicznej rodzinie** rozwiązań liniowego układu, jest algebraiczne. Dla ustalonego stopnia n można nałożyć ograniczenia na liczniki i mianowniki ewentualnego pierwiastka kwadratowego wymiernego; rozstrzygnięcie postaci „istnieje P, dla którego Δ nie jest kwadratem” jest możliwe dzięki eliminacji algebraicznej. Nie wolno uważać pierwszego arbitralnego P za reprezentanta wszystkich rozwiązań. Nie deklarujemy praktycznej implementacji ogólnego eliminatora.

## 5. Jawne poprawki i otwarte bramki

Dodano przykład i test odrzucania kwadratowego wyróżnika; dodano test bieguna prostego i braku dopuszczalnych stopni n. Rozdział ma obecnie 5 środowisk dowodu, 5 przykładów i 25 unikatowych etykiet. Zestawy testów liczą **13 SymPy + 10 Fraction**.

Trzeba jeszcze uzyskać pełny zielony CI na finalnym źródle, skompilować książkę AA-01–AA-49, skontrolować log i obejrzeć wszystkie strony AA-49. Bez tych wyników audyt III nie może oznaczyć rozdziału jako STABILNY. AA-50 pozostaje nieotwarty.


## Korekta po pierwszym przebiegu CI

W przebiegu GitHub Actions [#45176160492](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45176160492) testy ogólne zakończyły się 3 błędami, ponieważ testowy enumerator `case2_local_sets` sprawdzał `v.is_integer is True` także dla zwykłej wartości Python `2`. Ta wartość nie była traktowana jak obiekt symboliczny o własności `is_integer=True`, więc w testowym E_a brakowało zawsze dopuszczalnej kandydatki 2. Poprawka `s.sympify(v).is_integer is True` występuje w dwóch miejscach (skończone bieguny i nieskończoność) i zachowuje kandydatów 2,2±2sqrt(1+4b). Jest to poprawka implementacji **testów**, nie matematycznego twierdzenia. Celem ponownego CI jest potwierdzenie wszystkich list E_a,E_∞ oraz pełnego PDF.
