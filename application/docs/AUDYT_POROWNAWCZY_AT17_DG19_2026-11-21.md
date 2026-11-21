# Etap VII. Audyt porównawczy AT-17 / DG-19

**Data:** 21 listopada 2026.  
**Repozytorium / gałąź:** `dariusz-piekarz/mathematical_scipts` / `biblioteka-matematyczna-iteracja-6`.  
**Zakres:** dokładnie dwa pełne rozdziały: AT-17 „Konstrukcja Pontriagina–Thoma i podstawy teorii kobordyzmów” (993 wiersze w źródle przed audytem) i DG-19 „Kobordyzmy i rachunek uchwytów” (1489 wierszy przed audytem).  
**Polityka:** zmiany w źródłowych plikach rozdziałów, bez tworzenia brancha pomocniczego, bez zmiany main, bez zacierania unikatowej treści, bez przemianowania historycznych \label i \ref.

## 1. Mapa pokrycia

**AT-17** rozwija: regularne włókno i normalne uramowanie; konstrukcję ściągającą Pontriagina–Thoma; bijekcję pomiędzy uramowanym kobordyzmem a homotopią sfer; stabilną homotopię i włókno Hopfa; związek z dualnością Poincarégo i klasą Eulera; nieorientowane i zorientowane grupy kobordyzmu; liczby Stiefela–Whitneya i Pontriagina; szczegółowe rachunki RP², RP²×RP², RP⁴ oraz Ω₂^O; normalne klasyfikacje, widma MO/MSO i uwagi o MU.

**DG-19** rozwija: Morse'owskie funkcje na kobordyzmach z ustalonymi brzegami, rozkład na uchwyty, rdzenie i współrdzenie, dualność uchwytów, ślady chirurgii i opis zmiany brzegu, względny kompleks łańcuchowy z podpisanymi przecięciami, parzystość Eulera, przesuwanie/przestawianie uchwytów, kryterium geometrycznego zniesienia pary, lokalny model narodzin oraz warunkowy trik Whitneya.

Rozdziały nie są redundantne: one odpowiadają na dwa różne pytania. Pierwszy pyta, jakie **klasy kobordyzmu** reprezentują rozmaitości; drugi pyta, jak **konkretnie zmienia się kobordyzm przy dołączaniu uchwytów**. Te twierdzenia wymagają innych założeń i technik. Wspólna tematyka nie upoważnia do usunięcia oryginalnych dowodów.

Po poprawkach: 18 etykiet AT-17, 38 etykiet DG-19, **0 wspólnych nazw etykiet**. Mapa pełnych nazw i świadectwa pochodzenia:
`application/config/KANDYDACI_SCALEN_AT_DG_ETAP_07.json`.

## 2. Audyt precyzji twierdzeń i granic dowodów

### 2.1. PT: podrozmaitość uramowana, klasa stabilna, widma

Twierdzenie AT-17 `thm:pt-framed-v9` odróżnia kowymiar stały k od stabilizacji. Dla przedstawiciela punktowanego f:S^{n+k}→S^k wybiera regularną wartość q, wyklucza punkt bazowy i uzyskuje uramowaną n-podrozmaitość. Wariant q poza obrazem poprawnie produkuje zbiór pusty i nullhomotopijną mapę (obraz mieści się w ściągalnym S^k\{q}). Wymagany krok gładkiej aproksymacji względnej i tubularna jednoznaczność są jawne, nie utożsamiają się z samym twierdzeniem Sarda.

Twierdzenie `thm:pt-MO-v9` operuje *widmem*: Ω_n^O=lim_k π_{n+k}(MO(k)) i analogicznie dla MSO. Nie przypisuje wszystkich klas jednej przestrzeni BO. Konstrukcja normalnego odwzorowania klasyfikującego wymaga tylko orientacji wiązki dla MSO, **nie uramowania**. AT-17 rozróżnia te rodzaje struktur i zachowuje warunki stabilizacji.

W DG-19 odpowiada im konstrukcja przeciwna do klasyfikacji: konkretny uchwyt jako ślad chirurgii (`thm:slad-chirurgii-18`), którego częścią przyczepienia jest całe S^{k−1}×D^{m−k}, **nie sama sfera** bez obramowania. Przy zmianie kierunku indeks k zamienia się na m−k (`thm:dualny-uchwyt-18`). Nie należy bez dowodu traktować izomorfizmu grup kobordyzmu z grupą homotopii widma jako przepisu na bezwzględny dyfeomorfizm dwóch brzegów.

### 2.2. Charakterystyczne liczby, torsja i granice wnioskowania

AT-17 `thm:sw-bdy-v9`: jeśli M=∂W, to TW|_M≅TM⊕ε¹, a i_*[M]=0 z długiego ciągu pary (W,M). Stąd znikają odpowiednie liczby Stiefela–Whitneya; dla orientowanego W analogicznie liczby Pontriagina. Nie wolno odwracać wniosku z tych warunków bez pełnego obliczenia grup Ω_* — zostało to wyraźnie oznaczone w oryginalnym rozdziale.

AT-17 `prz:bordism-rp2-product`: nad F₂ dla X=RP²×RP² mamy w(TX)=(1+a+a²)(1+b+b²), w₂=a²+ab+b² i w₂²=a²b², z oceną 1. W `prz:bordism-rp4-versus-rp2-square` porównanie RP⁴ wykazuje odrębne klasy kobordyzmu mimo równej parzystości Eulera. Utrzymano obie niezależne konstrukcje i diagram oryginalny.

DG-19 `thm:kompleks-uchwytow-18`: każda k-komórka uchwytu daje generator względnej grupy łańcuchowej C_k(W,N_-) nad Z. Współczynnik macierzy brzegu jest liczbą podpisanych przecięć sfer przyczepienia i pasa. Jest to informacja **całkowita**, której nie wolno zastępować tylko wymiarami po przejściu do Q. Lokalny geometryczny warunek pojedynczego przecięcia jest mocniejszy niż algebraiczne ±1 i wymaga rzeczywistego argumentu o dyskach Whitneya; `prop:whitney-do-zniesienia-18` zachowuje ten warunek i unika przypisania ogólnej skuteczności w niskich wymiarach.

## 3. Nowy przykład AT-17: ten sam kobordyzm, różna homologia brzegów

Nowy oryginalny `prz:bordism-torus-klein-24`.

Dla D²={z∈C:|z|≤1} i odbicia r(z)=bar z, zbudowano gładkie zwarte trójrozmaitości:
V_+=D²×S¹ i V_-=(D²×[0,1])/((z,1)~(bar z,0)).
Każda jest wiązką dysków nad S¹. Ich brzegi:
∂V_+=T² oraz ∂V_-=(S¹×[0,1])/((z,1)~(bar z,0))=K,
gdzie K jest butelką Kleina.

Wniosek kobordyzmu nieorientowanego to **[T²]=[K]=0 w Ω₂^O**. To nie oznacza homeomorfizmu, a nawet homologicznej równoważności.
Van Kampen i abelianizacja:
π₁(T²)=⟨a,b|bab⁻¹=a⟩, π₁(K)=⟨a,b|bab⁻¹=a⁻¹⟩,
H₁(T²;Z)=Z², H₁(K;Z)=Z⊕Z/2.
W obu przypadkach χ=0.
Wszystkie te stwierdzenia zostały uzasadnione bez odwoływania się do klasyfikacji wszystkich powierzchni.

## 4. Nowy przykład DG-19: dwóch sposobów przyklejenia 1-uchwytu nie wolno mylić

Nowy `prz:skrecony-uchwyt-klein-24` i `fig:skrecony-uchwyt-klein-24`.

Po usunięciu dwóch otwartych dysków z S² pozostaje pierścień A≅S¹×[0,1]. Część nowego brzegu 1-uchwytu B=D¹×S¹ jest drugim pierścieniem. Pierwsze sklejenie daje dłuższy cylinder, a drugie ustala dyfeomorfizm h:S¹→S¹ na końcach:
M_h=(S¹×[0,1])/((z,1)~(h(z),0)).

Jeżeli deg h=+1, izotopia rosnącego podniesienia h daje torus. Gdy deg h=−1, h jest izotopijne z odbiciem z→bar z, a wynik to K. Odpowiadające prezentacje π₁ i obliczenie H₁ wykazują obecność torsji Z/2 tylko w drugim przypadku. Po zamknięciu sferycznego wejścia dyskiem trójwymiarowym otrzymujemy bez skręcenia pełny torus D²×S¹, ze skręceniem V_- opisane w AT-17. Wniosek jest dokładnie zgodny z konwencją kierunku/orientacji brzegu.

Dla samodzielności DG-19 zdefiniowano lokalnie symbol Ω₂^O, zanim użyto go przy tych obliczeniach; grupa nie jest już domyślną, niezdefiniowaną notacją.

Rysunek przedstawia dwie pary identyfikowanych krawędzi prostokątów, osobno oznaczone strzałkami zgodnymi i przeciwnymi.

## 5. Dodatkowy nowy przykład DG-19: dwa brzegi S², wymiernie acykliczny środek z całkowitą torsją

Nowe `prz:uchwyty-torsja-sfera-sfera-24` i `fig:uchwyty-torsja-sfera-sfera-24`.

Do S²×I dołączamy 1-uchwyt, otrzymując na górze T²=R²/Z². Jego sferę pasa wybieramy jako B₁={[(1/4,t)]}. Następnie przyczepiamy 2-uchwyt wzdłuż gładkiej osadzonej krzywej γ(t)=[(2t,t)] dla t mod Z, o dobranym obramowaniu.

Intersekcje z B₁ powstają, gdy 2t=1/4 mod 1, czyli przy t=1/8 i 5/8. W każdym punkcie det((2,1),(0,1))=+2, co oznacza lokalny znak +1, a **sumę +2**.
Kompleks względny ma postać
0→Z --2→ Z→0,
więc H₁(W,S²;Z)=Z/2 i pozostałe grupy względne są 0.
Nad Q mnożenie przez 2 jest odwracalne i cały kompleks jest acykliczny.

Krzywa γ jest pierwotna, bo (2,1) jest wektorem prymitywnym: macierz [[2,1],[1,1]] ∈ SL₂(Z) wysyła standardowy poziomy okrąg na γ. Dlatego rozcięcie torusa wzdłuż γ daje pierścień, a chirurgia 2-uchwytu zakrywa jego dwa okręgi brzegowe dwoma dyskami: nowy brzeg jest ponownie S².

Długi ciąg homologii pary (W,S²) daje H₁(W;Z)=Z/2. W szczególności **W nie jest walcem S²×I**, choć oba brzegi są S², a H_*(W,S²;Q)=0.
To niezależny kontrprzykład do wniosku „równe brzegi + zanik wymiernej homologii względnej ⇒ iloczyn”.

Narysowano na fundamentalnym kwadracie torusa obie dodatnie intersekcje γ i B₁, z podaniem dokładnych parametrów, strzałek i wartości +1.

## 6. Testy, kompilacja i kontrola PDF

Dodano regresje `application/tests/test_at_dg_pairwise_17_19.py`:
- monodromia odbicia dysku i krzywej brzegowej;
- rozróżnienie H₁ torusa i butelki Kleina przez abelianizację;
- χ=0 dla obu brzegów;
- wymiary śladu chirurgii i dualność indeksów uchwytów;
- wzór na zmianę χ przy jednym 1-uchwycie;
- zamiana baz pod przesunięciem uchwytu, jawne macierze T i T⁻¹;
- liczenie w₂² na RP²×RP² oraz liczb na RP⁴;
- zachowanie warunków o PT i dyskach Whitneya;
- nowy wyznacznik nachylenia (2,1), dokładnie dwa dodatnie przecięcia i H₁(W,S²)=Z/2;
- kontrola zachowania unikalnych label, środowisk TeX i kanonicznych wejść \input w obu tomach.

Workflow: `.github/workflows/paired-at-dg-pontryagin-thom-cobordism-audit.yml`.
Uruchamia 12 testów i trzykrotną kompilację pełnych źródeł AT-01–30 oraz DG-01–20. Sprawdza nieustabilizowane odsyłacze i przepełnienia wierszy. W DG dopuszcza tylko wcześniej zidentyfikowaną listę 12 niezdefiniowanych referencji, których cele są w jeszcze niezaimportowanych DG-21–36.

**Wynik końcowy, liczby stron, job IDs i wzrokowa kontrola PDF — do dopisania po rzeczywistym sprawdzeniu wyników GitHub Actions.** Nie kopiować wyniku poprzedniej iteracji bez sprawdzenia bieżących artefaktów.

## 7. Ograniczenia i następny etap

Nie przypisano wszystkich nazw etykiet z AT do DG; różnica w numeracji rozdziałów nie jest powodem ich zmiany. Nie wykonano zbiorczego scalania ani wczesnego przeniesienia twierdzenia o s-kobordyzmie do źródła AT-17.
Pozostałe zagadnienia: import brakujących DG-21–36, porównanie dalszych konstrukcji chirurgii z AT i spójny system nazw i zależności po ustaleniu kanonicznego właściciela. Kolejny audyt porównawczy należy wybrać według merytorycznych pokryć w najnowszym stanie gałęzi, a nie tylko numerów rozdziałów.
