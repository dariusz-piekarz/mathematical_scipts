# Analiza funkcjonalna — rozdział 02 — audyt 03 (potwierdzenie stabilności)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/02-podprzestrzenie-produkty-ilorazy-i-topologie-uniwersalne.tex`.  
**SHA pliku źródłowego:** `0b2772a13459c13d9720e3726966981b289e2bed` (identyczny jak w audycie 02/02).  
**Wynik:** **czysty audyt potwierdzający; rozdział 02 — STABILNY (2/2 kolejnych czystych audytów).**

## Zakres i niezależność

Ponowna weryfikacja wszystkich 14 dowodów, 7 przykładów, 15 etykiet, odsyłaczy do rozdziałów 01 i 05 oraz poprawności składni LaTeX i obrazu PDF. Nie założono poprawności na podstawie wcześniejszych ocen: sprawdzono kluczowe kwantyfikatory i zależności od założeń Hausdorffa, zakresy topologii początkowej/końcowej oraz przypadki osobliwe. Rozdział nie został zmieniony.

## Dowody: 14/14 PASS

1. **Topologia podprzestrzeni:** przeciwobrazy otwartych zbiorów i topologia produktu podprzestrzeni uzasadniają ciągłość działań; warunek Hausdorffa przechodzi na podprzestrzeń.
2. **Domknięcie podprzestrzeni:** obie inkluzje w formule `cl(M)=∩_{U∈N(0)}(M+U)`, poprawne użycie symetrycznych otoczeń i liniowość domknięcia, w tym `λ=0`.
3. **Uniwersalna własność podprzestrzeni:** ciągłość `f:Z→M` równoważna ciągłości `i∘f` z definicji topologii indukowanej.
4. **Produkt i rzuty:** rzuty są liniowe, ciągłe i otwarte; ciągłość działań sprawdza się współrzędnie, a Hausdorff wynika z oddzielania w jednej współrzędnej.
5. **Ograniczoność produktu:** rosnące skalowania zrównoważonych otoczeń pozwalają przejść od ograniczoności wszystkich projekcji do ograniczoności zbioru w produkcie; również dla pustego `I`.
6. **Ciągłe funkcjonały na `K^I`:** kontrola `L` na bazowym otoczeniu zera ogranicza zbiór współrzędnych do skończonego `F`; skalowanie wektorów z zerami na `F` wymusza znikanie `L` na odpowiedniej podprzestrzeni.
7. **Iloraz jako TVS:** otwartość `q`, `q×q` i `id×q`; ciągłość obu działań na ilorazie; kryterium Hausdorffa przez domkniętość `M`.
8. **Własność uniwersalna ilorazu:** jednoznaczność i poprawność wzoru `T̃(x+M)=T(x)` przy `M⊆ker T`, ciągłość przez topologię ilorazową.
9. **Pierwsze twierdzenie o izomorfizmie:** homeomorficzność `X/ker T→T(X)` równoważna otwartości `T` na swój obraz, nie zaś samej bijektywności.
10. **Norma ilorazowa i zupełność:** niezmienniczość reprezentanta, dodatnia określoność dla `M` domkniętej, równość obrazów kul, zgodność topologii i sumowalne podniesienia przyrostów podciągu Cauchy'ego.
11. **Początkowa topologia liniowa:** kontrola ciągłości dodawania i mnożenia przez skalar przez wszystkie `T_i`; kryterium Hausdorffa przy `Y_i` Hausdorffa.
12. **Końcowa topologia liniowo-topologiczna:** rodzina dopuszczalnych topologii niepusta (topologia trywialna); topologia generowana przez ich sumę zachowuje łączną ciągłość działań, a każde `T_i` pozostaje ciągłe; własność uniwersalna wynikająca z topologii początkowej indukowanej przez `S`.
13. **Skończone sumy proste:** ciągłość `S` na produkcie przez skończoną sumę ciągłych składników `S∘j_i`.
14. **Hausdorffyzacja:** `N=cl{0}` jest domkniętą podprzestrzenią zawartą w jądrze każdego ciągłego odwzorowania liniowego do TVS Hausdorffa; iloraz spełnia własność uniwersalną.

W każdym punkcie **PASS**, bez nowej luki merytorycznej.

## Przykłady: 7/7 PASS

1. Wielomiany gęste w `C([0,1])`, ale niezupełne z normą indukowaną.
2. Zbieżność punktowa bez jednostajnej, dzięki funkcjom z przesuwającymi się nośnikami.
3. Ciągła bijekcja liniowa między przestrzeniami z normami supremum i całkową, bez ciągłej odwrotności.
4. Izomorfizm `C([0,1])/ker(E_0)≅K` i ciągłe rozszczepienie przez funkcje stałe.
5. Produkty i podprzestrzenie jako topologie początkowe.
6. Kontrprzykład dwóch osi w `R²`: końcowa topologia zbiorowa nie jest TVS, bo przesunięcia nie są homeomorfizmami.
7. `φ=⊕_n K e_n`: produktowa topologia indukowana a silniejsza lokalnie wypukła topologia sumy prostej; funkcjonały seminormowe i ciągłość operatorów.

## Próby kontrprzykładów i przypadki brzegowe

- **`I=∅`:** produkt to przestrzeń zerowa; pusta rodzina współrzędnych jest zgodna z uniwersalnymi własnościami i z ograniczonością wszystkich zbiorów.
- **Niedomknięte `M`:** `X/M` nadal jest TVS, lecz może nie być Hausdorffa; dla `c_{00}⊂ℓ²` seminorma `dist(x,M)` zanika dla klas niezerowych. Twierdzenie o normie ilorazowej jawnie wymaga `M` domkniętej.
- **`R²/span(1,1)`:** odległość od `(a,b)` do prostej diagonalnej to `|a-b|/√2`; zgadza się z normą ilorazową.
- **Warunek wspólnej ciągłości:** zarówno w produkcie, jak i ilorazie kontroluje się ciągłość działań jako odwzorowań z produktów, nie tylko osobno.
- **Końcowa topologia zwykła a liniowo-topologiczna:** przedstawiony przykład rzeczywiście oddziela obie konstrukcje; dowód istnienia tej drugiej nie wymaga pokrycia `X` obrazami `T_i`.
- **`K` zespolone i `λ=0`:** oszacowania jednorodności normy ilorazowej i seminorm działają również w tych przypadkach.

## Terminologia, integralność i PDF

- Nie występuje samodzielny angielski rzeczownik „dual” w prozie ani „map” w znaczeniu odwzorowania. Etykieta historyczna `thm:product-dual` zachowana dla kompatybilności odsyłaczy.
- 14 par `proof`, 7 par `przyklad`, 15 unikatowych etykiet. W rozdziale 02 żadna istniejąca etykieta nie została przemianowana ani usunięta.
- Rysunek 2.1 ilorazu `R²/M` oraz całe strony 7–15 w kontekstowym PDF były oglądane wizualnie w poprzednim przebiegu; nie stwierdzono kolizji napisów ani wychodzenia poza marginesy. Rozdział nie zmienił się od tej kontroli.
- [Przebieg CI 45154140716](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45154140716): **SUCCESS** dla 12 testów, przygotowania kontekstu źródeł 01–05, kompilacji i kontroli odsyłaczy/logów oraz zapisania PDF. [Przebieg 45153722035](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45153722035) był także **SUCCESS** po rozszerzeniu testów do 12.
- Żadnych nowych poprawek w źródle ani testach w tej iteracji; sukcesy CI odnoszą się do dokładnie tej samej wersji rozdziału.

## Status i decyzja

**Rozdział 02 — STABILNY, dwa kolejne czyste audyty: 02/02 i 02/03.** Można przejść do audytu **rozdziału 03 „Sieci, struktura jednostajna i zupełność przestrzeni liniowo-topologicznych”**. Nowe, opcjonalne treści z audytu 02/01 pozostają poza zakresem, dopóki użytkownik nie zatwierdzi ich dodania.
