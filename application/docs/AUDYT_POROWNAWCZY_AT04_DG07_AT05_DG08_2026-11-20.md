# Audyt porównawczy AT-04 / DG-07 oraz AT-05 / DG-08 — etap III

**Data:** 20 listopada 2026 r.  
**Repozytorium:** dariusz-piekarz/mathematical_scipts.  
**Gałąź:** biblioteka-matematyczna-iteracja-6, bez zmian w main.  
**Zakres:** dwie pary rozdziałów: (i) homotopia, nakrycia, van Kampen, grafy i CW; (ii) homologia singularna, symplicjalna, komórkowa i lokalna.  
**Standard:** szczegółowe hipotezy i uzasadnienie każdego istotnego kroku, przykłady i kontrprzykłady, kontrola rysunków, zachowanie historycznych \label oraz \ref, bezstratny plan scalania.

## 1. Rzeczywiste porównanie źródeł

| Para | Wspólne nazwy etykiet | Tylko AT | Tylko DG | Wspólne nietrywialne wiersze: Jaccard |
|---|---:|---:|---:|---:|
| AT-04 / DG-07 | 44 | 2 | 18 | 0,514 |
| AT-05 / DG-08 | 50 | 5 | 16 | 0,552 |

Wspólna nazwa etykiety NIE dowodzi tożsamości treści matematycznej. Różne przykłady pod wspólnymi tytułami bywają obliczone na różnym poziomie szczegółowości, a DG posiada całe dodatkowe sekcje nieobecne w AT. Nie wykonano automatycznego przenoszenia żadnych etykiet ani usuwania fragmentów.

Dokładny manifest wszystkich czterech list unikalnych etykiet i zmian wspólnych założeń:
application/config/KANDYDACI_SCALEN_AT_DG_ETAP_03.json.
Decyzja o scaleniu: NIEZATWIERDZONA.

## 2. AT-04 / DG-07: homotopia, nakrycia i CW

### Podstawowe definicje i grupa podstawowa
Oba źródła precyzyjnie rozróżniają homotopie zwykłe i homotopie względne, iloczyn i odwrócenie drogi, silny retrakt deformacyjny, zmianę punktu bazowego i funktorialność pi_1. DG ma dodatkowe przykłady homotopii w obszarze wypukłym oraz pętli na brzegu dysku. Ich pełne rachunki należy zachować przy scalaniu.

### Podnoszenie dróg i homotopii
Obie wersje twierdzenia thm:podnoszenie-nakrycie wykorzystują liczbę Lebesgue'a dla otwartego pokrycia I oraz I² i sklejanie po arkuszach. DG dokładniej uzasadnia, dlaczego spójny obraz już podniesionej krawędzi leży w jednym arkuszu, a AT ma bardziej wyodrębniony wzór podniesienia. Nie ma matematycznego uzasadnienia, by usuwać tę kontrolę ciągłości.

### Kryterium podnoszenia i nakrycie uniwersalne
Twierdzenia thm:kryterium-podnoszenia i thm:uniwersalne-nakrycie zawierają warunek na obraz pi_1 i klasyfikację z wykorzystaniem homotopii dróg względem końców. DG explicite identyfikuje włókno z warstwami prawostronnymi H\G, wyprowadza liczbę arkuszy jako indeks podgrupy i rozwija później osobno transformacje nakrycia. AT zawiera własny przykład q_m:S¹→S¹, z którego wynika brak globalnego przekroju dla m>=2. Nie wolno usuwać żadnej z tych części.

### Grupa transformacji nakrycia
**Unikalne DG-07**: def:transformacja-nakrycia i thm:deck-normalizator, wraz ze wzorem Deck(p)≈N_G(H)/H; także klasyfikacja nakryć normalnych.
W ramach audytu dodano przykład prz:nakrycie-nieregularne-bukiet-dg07 z rysunkiem fig:nakrycie-nieregularne-bukiet-dg07: nad bukietem S¹∨S¹ skonstruowano spójne nakrycie trzyarkuszowe o monodromiach (1 2) i (2 3). Graf całkowity ma V=3, E=6, zatem pi_1(E)≈F_4 (drzewo rozpinające ma dwie krawędzie). Każdy wierzchołek ma dokładnie jedną wychodzącą i jedną przychodzącą krawędź każdego z dwóch typów, więc sprawdzono warunek lokalnego nakrycia. Permutacja włókna transformacji nakrycia musi komutować z obiema transpozycjami. Ich wspólny centralizator w S_3 jest trywialny, więc Deck(p)=1. Nakrycie jest nienormalne mimo trzech arkuszy.
To kontrprzykład do błędnego, lecz możliwego przekonania, że każde nakrycie o skończonej liczbie arkuszy jest regularne.

### Twierdzenie van Kampena
**Rzeczywiste uzupełnienie dowodu AT-04:** przy oznaczaniu wypełnienia kwadratu prostokątami U/V nie było wystarczająco jasno uzasadnione, że fragment dolnego boku reprezentujący literę w G_U, a przylegający do prostokąta o obrazie w V, można przenieść do G_U po relacji z U∩V. Teraz sprawdzono, że taki fragment znajduje się w przecięciu, a przy podziale na końcach liter wybiera się stałe drogi pomocnicze. Dopisano jawnie obie inkluzje N⊆ker Phi i ker Phi⊆N, dzięki którym surjekcja Phi schodzi do izomorfizmu ilorazu.
DG dostarcza ponadto przykład wypełniania otworu w dysku oraz kontrprzykład pokazujący, dlaczego warunek łukowej spójności U∩V jest konieczny.

### Grafy, drzewa, CW
**Unikalne DG-07:** sekcja sec:grafy-drzewa z dowodem istnienia drzewa rozpinającego, wzorem |E|-|V|+1, bazą wolną grupy podstawowej grafu, rysunkiem kwadratu z przekątną i zastosowaniami do skończonych kompleksów CW. Podczas scalania nie kopiować bezrefleksyjnie do AT, bo DG ma także precyzyjniejsze rachunki prezentacji grup CW. AT zachowuje własne rysunki i obliczenia nakrycia q_m, których nie było w DG.

### Etykiety unikalne
Tylko AT-04: prz:nakrycie-m-arkuszy; fig:nakrycie-m-arkuszy.

Tylko DG-07: fig:retrakcja-promieniowa; prz:petla-w-dysku; fig:nakrycie-trzy-arkusze; prz:podnoszenie-poteg; def:transformacja-nakrycia; thm:deck-normalizator; prz:van-kampen-dysk; fig:van-kampen-dysk; uwaga:orientacja-przed-homologia; sec:grafy-drzewa; def:drzewo-grafowe; prop:drzewo-rozpinajace; fig:graf-drzewo-cykle; thm:pi1-graf; prz:nakrycie-nieregularne-bukiet-dg07; fig:nakrycie-nieregularne-bukiet-dg07; rem:iloraz-dysku-sfera; wn:pi1-cw-prezentacja.

## 3. AT-05 / DG-08: homologia

### Łańcuchy i homotopie
Oba rozdziały dowodzą d²=0, konstruują kompleks singularny, homotopię pryzmatyczną i homologię względną. DG dodaje rachunek dwóch trójkątów tworzących kwadrat i konkretny przykład operatora pryzmatycznego dla drogi. Te przykłady są niezbędne przy składaniu pełnej wersji.

### Lemat małych łańcuchów
Wspólny lemat lem:male-lancuchy jest w DG znacznie bardziej szczegółowy:
- wyprowadza wyznacznik orientacji barycentrycznego podziału standardowego sympleksu;
- sprawdza znaki każdej ściany;
- konstruuje stożek i wyprowadza jego brzeg;
- dowodzi teleskopowej tożsamości S^r−id=dT^(r)+T^(r)d;
- szacuje średnicę po kolejnych podziałach.
AT posiada ten sam rdzeń w skróconym zapisie. Przyszły wspólny dowód powinien zachować poziom DG oraz objaśnienia obrazu osobliwego sympleksu i rysunek DG.

### Wycinanie
Wspólne twierdzenie thm:wycinanie ma tę samą istotną hipotezę closure(Z)⊆interior_X(A). Dowody wykorzystują identyfikację kompleksów względnych małych łańcuchów; DG dodaje policzony kontrprzykład, jeśli hipotezy o domknięciu nie ma. Nie usuwać warunku topologicznego i koniecznie zachować kontrprzykład.

### Mayer–Vietoris
Obie wersje wprowadzają operator (i*,-j*) i strzałkę δ wysyłającą klasę cyklu a+b na [da]. AT ma **jedyny w tej parze** kompletny przykład prz:mv-sfera-dwie-polkul, gdzie δ fundamentalnej klasy S² jest generatorem H_1 równika. DG dodatkowo wylicza generator dla S¹ jako różnicę dwóch punktów i ilustruje go osobnym rysunkiem. To uzupełniające się przypadki w różnych stopniach.

### Komórki, torsja i zmiana współczynników
Wspólne rachunki torusa i RP² są matematycznie zgodne: dla torusa brzeg 2-komórki ma słowo komutatora i zerowe współczynniki, a dla RP² stopień dołączenia to 2 i H_1≈Z/2. **Unikalne AT-05**: rachunek butelki Kleina z przyjętym słowem a b a⁻¹ b, ∂_2(1)=2b i H_1≈Z⊕Z/2 wraz z rysunkiem fundamentalnego kwadratu. **Unikalne DG-08**: pełna homologia grafu jako jądro macierzy incydencji i wzór H_1≈Z^(m-n+c), przykład dwóch dysków wypełniających pętlę oraz dołączenie komórki stopnia m. W żadnym wypadku nie zastępować przypadku Kleina samym torusem.

### Homologia lokalna i punkty osobliwe
Wspólne twierdzenie prop:lokalna-homologia mówi, że dla m-rozmaitości bez brzegu lokalna homologia w punkcie p ma Z tylko w stopniu m. DG zawiera również odrębne stwierdzenie prop:lokalna-homologia-brzeg-8 o zerowaniu wszystkich grup względnych w punkcie brzegu oraz przykład trójnogu.

W AT-05 dodano **uogólnienie na r ramion**, prz:homologia-lokalna-r-ramion-at05 i fig:lokalna-r-ramion-at05. Dla Y_r=⋃[0,u_j] i p=0, gdzie promienie są różne, Y_r jest ściągalne, lecz Y_r\{p} ma r składowych. Długi ciąg pary redukuje grupę lokalną H_1 do jądra Z^r→Z, (a_j)↦sum a_j. Jego baza e_1−e_r,...,e_(r−1)−e_r daje H_1≈Z^(r−1); wszystkie inne grupy lokalne znikają.
Wyniki r=1,2,4 rozróżniają punkt brzegu, punkt wewnętrzny 1-rozmaitości i rozgałęzienie; r=3 odtwarza ujęcie trójnogu w DG. Zachować ogólny wzór AT oraz szczegółowe rysunki i obliczenia DG.

### Etykiety unikalne
Tylko AT-05: prz:mv-sfera-dwie-polkul; prz:homologia-butelka-kleina; fig:homologia-butelka-kleina; prz:homologia-lokalna-r-ramion-at05; fig:lokalna-r-ramion-at05.

Tylko DG-08: prop:brzeg-orientacja; prz:homologia-kwadrat; prz:pryzmat-drogi; fig:pryzmat-homologia; prz:para-odcinek-konce; prz:podzial-singularny-8; fig:podzial-barycentryczny-8; fig:mv-okrag-8; prz:dwa-dyski-homologia-8; sec:homologia-grafu-incydencja; thm:homologia-grafu-incydencja; fig:sklejenia-homologia-torus-rp2; prz:homologia-dolaczenie-stopien-m; prop:lokalna-homologia-brzeg-8; fig:lokalna-homologia-trzy-modele-8; prz:lokalna-homologia-trojnog-8.

## 4. Rejestr i regresje

Dodatki:
- application/config/KANDYDACI_SCALEN_AT_DG_ETAP_03.json — dokładne unikalne etykiety aktualnych 4 źródeł, osobne hipotezy i rozstrzygnięcia, decyzja approved_to_merge=false;
- application/tests/test_at_dg_pairwise_04_07_05_08.py — 8 testów, w tym jawne permutacje i centralizator w S3, połączenie grafu, całkowita baza jądra Z^r→Z, luki dowodu van Kampena, bilans otoczeń TeX i pełna zgodność manifestu z etykietami;
- .github/workflows/paired-at-dg-homotopy-homology-audit.yml — powtarzalne GitHub Actions dla pary AT i DG, osobna kompilacja pełnego AT i częściowego DG.

Istniejące audyty pojedynczych par rozdziałów AT03/04 oraz AT05/06 również przebiegły bez błędów po modyfikacji odpowiednich plików. Pełna kompilacja dwóch par i oględziny PDF są oddzielnymi czynnościami, których wyniki należy zamknąć dopiero po uzyskaniu odpowiednich logów GitHub Actions — nigdy na podstawie samego istnienia workflow.

## 5. Następny etap

Nie przeprowadzono destrukcyjnego scalania. Dalszy audyt porównawczy: AT-06 / DG-09 (wyższe grupy homotopii, Hurewicz), a potem analiza tych elementów DG, dla których brak równoległych rozdziałów AT. Po każdej parze: realny audyt hipotez, dowodów, konkretnych przykładów i rysunków; następnie testy i kontrola PDF; przy przyszłym łączeniu bez utraty żadnej niepowtarzalnej treści.
