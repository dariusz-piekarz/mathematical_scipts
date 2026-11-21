# Algebra liniowa — rozdział 24, audyt V (pierwszy czysty po korekcie składu)

**Data:** 21 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/24-rownania-riccatiego-i-sterowanie-liniowo-kwadratowe.tex`  
**Blob po ostatniej korekcie:** `82b136e5bd2284442a47d1e740207b2ee3bda816`.  
**Poprzednie audyty:** I (matematyczne uzupełnienie DARE), II/III (czyste matematycznie), IV (tytuł wniosku i ostrzeżenie Underfull).

## Ponowny audyt

1. Sprawdzono wszystkie warunki w twierdzeniach: `n,m>=1`, `A∈M_n(C)`, `B∈M_{n×m}(C)`, `Q=Q*>0`, `R=R*>0`. Wzory na K mają rozmiar `m×n` i można je stosować także dla `B=0`.
2. W dowodzie DARE rekurencja Bellmana obejmuje `N=0`, zapewnia `P_N>=0` i minimalizację o jedynym pierwszym kroku. Granica przy stabilnym A istnieje dzięki monotonii i ograniczeniu przez zerowe sterowanie.
3. Tożsamość algebraiczna dla dwóch dowolnych stabilizujących rozwiązań DARE `D=A_1*DA_2` nie używa dodatniej określoności M_2, tylko jej odwracalności. Stabilność obu zamkniętych pętli gwarantuje D=0.
4. Zamknięte równania Lapunowa prowadzą do stabilności CARE i DARE bez niejawnych założeń sterowalności. Zarówno w dyskretnym, jak i ciągłym dowodzie każda dodatnio określona Q zapewnia brak niezerowego wektora w jądrze rozwiązania granicznego.
5. W czasie ciągłym równanie różniczkowe ma lokalną jednoznaczność, a ograniczenie z góry przez koszt sterowania zerowego wyklucza wybuch w skończonym czasie. Osiągnięcie kosztu `x*S(T)x` wynika z ciągłego sprzężenia optymalnego.
6. W ciągłym horyzoncie nieskończonym uzasadniono zanik stanu dla *każdego* sterowania o skończonym koszcie: `x,u,x'∈L²` i nierówność Cauchy'ego–Schwarza dają `x(t)→0`. W dyskretnym horyzoncie wystarcza `x∈ℓ²`.
7. Jednoznaczność optymalnego sterowania ciągłego sformułowano „prawie wszędzie”; uwaga o punktowych zmianach wartości sterowania pozostaje poprawna.
8. Przypadki skalarne CARE (`p=1,-3`) i DARE (`p=1,-7/8`) wprost ilustrują brak jednoznaczności wszystkich algebraicznych rozwiązań przy zachowaniu jednoznaczności *stabilizującego* rozwiązania. Dwuwymiarowe przykłady mają zerowe residua.
9. Ostatnia zmiana ogranicza się do tytułu wniosku `cor:lin24-discrete-opt`: obecnie **„Sterowanie optymalne”**, bez naruszania treści i etykiety. Dzięki temu unikamy dawnego dużego ciągu sylab w nagłówku.

## Kontrola wizualna i skład

PDF uzyskany przed ostatnią zmianą tytułu jest zbudowany i dostępny z artefaktu pomyślnej kompilacji TeX (choć kontrola logu odrzuciła ostrzeżenie); ma **10 stron, wszystkie niepuste**. Render wszystkich stron został obejrzany: widoczne wzory i akapity są poprawnie rozłożone, bez kolizji. Automatyczna inspekcja PyMuPDF wykazała **0 bloków tekstu poza stroną**. PDF z najnowszym krótszym tytułem oraz końcowy zielony CI są jeszcze wymagane i nie są w tym raporcie deklarowane jako wykonane.

## Decyzja

**Audyt V czysty** matematycznie i redakcyjnie, bez kolejnych poprawek w źródle. Jest to pierwszy czysty audyt po korekcie IV. Do stabilizacji potrzebny kolejny czysty przebieg i końcowy zielony CI/PDF.
