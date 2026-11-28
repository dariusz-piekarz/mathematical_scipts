# Algebra liniowa — audyt globalny, iteracja 15 (LA29–32 i rejestr 382 dowodów)

**Data:** 22 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Poprzednia iteracja:** [14](iteration_14.md), rozdziały LA21–28.
**Wynik:** **CZYSTY w badanym zakresie LA29–32**. Źródła bez zmian. Zbudowano osobny, per-dowodowy rejestr całej książki; **pełny audyt globalny nadal OTWARTY**.

## 1. Zakres i wersje źródłowe

| Rozdział | SHA źródła | Wiersze | Środowiska proof |
|---|---|---:|---:|
| LA29 — Grassmanniany i współrzędne Plückera | 55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd | 743 | 6 |
| LA30 — Algebry Clifforda | 6d90013dd6c66d347e5ae2ac78b4c1a194aa979e | 309 | 3 |
| LA31 — Pin, Spin, spinory i struktury spinowe | 6c1d09b9eaf4083c9ebaa361dbf46fc350eae147 | 1496 | 6 |
| LA32 — Twistory, incydencja i fibracja | 8aea8bd8db02ca8677fb0547f770c9166fdaef88 | 917 | 10 |
| **Łącznie** | | **3465** | **25** |

W tej iteracji odczytano wszystkie cztery rozdziały, a szczegółowo analizowano kluczowe twierdzenia wymienione poniżej. Nie jest to twierdzenie, że każdy ich krok został formalnie sprawdzony w Lean.

**Wersja i CI:** wszystkie cztery SHA są identyczne w bieżącej gałęzi i commicie 3078c9ca833f69d908bddbb616086646898e64e6; sprawdzono je osobnym odczytem z obu referencji. [GitHub Actions 45047971276](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45047971276) ma status **completed/success**. W tej iteracji nie uruchomiono nowej pełnej kompilacji ani wizualnej kontroli PDF: korzystamy z istniejącej kontroli wcześniejszych iteracji i z potwierdzonej zgodności blobów.

## 2. Kontrola matematyczna i powiązania z wcześniejszymi rozdziałami

### LA29 ↔ LA10–11

- Sprawdzono współrzędne map wykresowych na Gr_k(V), wzór na przejście między dopełnieniami, topologię modelowaną przez ortogonalne rzuty oraz identyfikację T_L Gr_k(V) ≅ Hom(L,V/L). Ważne: w przypadku zespolonym mowa o holomorficznej przestrzeni stycznej, której rzeczywiste podłoże jest zwykłą rzeczywistą przestrzenią styczną.
- Kontrolowano lokalną trywializację wiązki tautologicznej γ^k, ilorazowej Q oraz zgodność z (γ^k)^*⊗Q. Wyrazy tensorowe korzystają z wcześniej udowodnionego, skończenie wymiarowego izomorfizmu do Hom.
- Sprawdzono minory Plückera, odzyskiwanie parametrów wykresu ze znakami (−1)^(k−j), równanie kwadryki Gr_2(K^4): p12p34−p13p24+p14p23=0. W przykładzie w Gr_2(R^4) parametry a,b,c,d i podane minory są spójne.
- Osadzenie Plückera: zanikanie w∧ξ charakteryzuje rozpiętą podprzestrzeń, a zwartość grassmannianu i Hausdorffowość przestrzeni rzutowej gwarantują homeomorfizm na obraz. Rozdzielono przestrzeń ogólnych podprzestrzeni od ich orientacji.
- Odwzorowanie Gaussa i cofnięcia wiązek wymagają struktury różniczkowej; zostały wyjaśnione przez lokalne ramki i pochodne macierzy wykresu. Są tu elementy geometrii różniczkowej rozwijane odrębnie w bibliotece, nie jest to luka algebraiczna.

### LA30 ↔ LA11

- Relacja v²=−||v||² i vw+wv=−2⟨v,w⟩ jest zgodna z konwencją w całym LA30–31. Relacje ilorazowe zachowują parzystość, lecz nie stopień tensorowy.
- Dowód bazy 2^n nie poprzestaje na redukcji słów: buduje wierną na podprzestrzeni słów uporządkowanych reprezentację przez operator c(v)=ε(v)−ι_v na Λ(V), gdzie ι_v²=ε(v)²=0 i ε(v)ι_v+ι_vε(v)=||v||². Działanie na 1 rozdziela wszystkie uporządkowane słowa. Współczynnik 1/r! w antysymetryzacji jest dopuszczalny, ponieważ rozdział jawnie pracuje nad R, a nie nad ciałem dodatniej charakterystyki.
- Rozkłady w wymiarach 0,1,2 oraz przykład kwaternionowy są zgodne z bazą i wybraną konwencją znaków.

### LA31 ↔ LA29–30

- W grupach Pin i Spin właściwe skręcone sprzężenie opisuje odbicie hiperpłaszczyzny: dla pojedynczego u jest to −uvu^(−1). Dla parzystych iloczynów minusy znoszą się. Jądro na Spin jest dokładnie {±1} w n≥2; dowód nakrycia zawiera lokalne podniesienie i dwa płaty.
- Przykłady Spin(2)→SO(2), Spin(3)≅SU(2), macierze Pauliego, sfera Blocha oraz chiralność w wymiarze parzystym mają zgodną konwencję. W wymiarze 4 zbadano symbolicznie operatory Γ, kwadraty generatorów oraz przemienność Γ z parzystymi słowami.
- Klasyfikacja zespolonych algebr Clifforda używa zwiększenia wymiaru o 2 przez M_2(C). Nieredukowalność i rozmiary modułów wynikają z macierzowych jednostek E_ij, a w wymiarze nieparzystym dwa moduły Clifforda mają izomorficzne ograniczenia do Spin.
- Konstrukcje wiązki spinorowej i struktur spinowych stosują właściwą ekwiwariancję dla ramek; cztery podniesienia nad płaskim torusem mają dwa niezależne znaki. Lokalny dwukocykliczny test w_2 oraz jego identyfikacja z kohomologią Cech są **jawnie rozróżnione**: twierdzenie o identyfikacji Čech korzysta z wiedzy zewnętrznej, nie jest tutaj podawane jako samodzielnie udowodnione.

### LA32 ↔ LA29/31

- Det X jako forma kwadratowa na M_2(C), kwadryka Segrego i jej dwie rodziny prostych izotropowych mają poprawną klasyfikację, przy czym klasyfikacja używa niezmienniczej bazy nad C. Incydencja ℓ_X∩ℓ_Y ≠∅ ↔ det(X−Y)=0 wynika bezpośrednio z jądra różnicy.
- Współrzędne Plückera wykresu W_X w Gr_2(C^4) są (det X,−b,a,−d,c,1); spełniają relację Kleina. Wyraźnie odróżniono kwadrykę Segrego w CP^3 od kwadryki Kleina w CP^5.
- Lokalny skalar transformaty Penrose'a: jednorodność F stopnia −2 kompensuje formę π1 dπ2−π2 dπ1; mieszane pochodne znoszą się w operatorze ∂11∂22−∂12∂21. Symbolicznie potwierdzono residuum −1/det X oraz równanie falowe. **Pełnej kohomologicznej transformaty Penrose'a rozdział nie dowodzi i nie powinien tak być przedstawiany.**
- Dla J antiliniowego z J²=−id płaszczyzna span(z,Jz) jest dobrze określona rzutowo i daje kwaternionową prostą. Lokalny wykres H×CP¹ i stereograficzna identyfikacja HP¹≅S^4 rozróżniają tę gładką fibrację od zespolonej relacji incydencji.

## 3. Nowe niezależne testy rachunkowe

Uruchomiono skrypt **/mnt/data/la_global15_crosscheck.py**, 235 wierszy, seed 20261122, SHA256 **b079bc2ef5ec36025e07d79453170f27e1a75167fc49a64c298e82dcffa3955b**.

- **94 093/94 093 PASS**, 0 FAIL. Szczegóły asercji i liczby w pliku /mnt/data/la_global15_crosscheck.log.
- LA29: testy różnych wymiarów i map, projekcji oraz ich pochodnych; rekonstrukcja parametrów z minorów i relacja Plückera. Łącznie **12 670** asercji.
- LA30: dokładna łączność iloczynu bazowego algebry Clifforda (m.in. wszystkie 32³ trójki w n=5), relacje spolaryzowane i reprezentacja na Λ(V). **38 747** asercji.
- LA31: losowe odbicia Pin/Spin w R², R³, R⁴, sprawdzenie chiralności w C⁴ i reprezentacji Blocha. **9 637** asercji.
- LA32: relacje Segrego/Kleina, incydencja, symboliczny wzór Penrose'a, J²=−I, niezmienniczość rzutowa i stereografia HP¹. **33 039** asercji.
- Obliczenia oparte na liczbach zmiennoprzecinkowych mają tolerancję numeryczną; część algebraiczna Clifforda używa całkowitych współczynników i pełnej enumeracji wybranych wymiarów, a część Penrose'a symboliczną arytmetykę SymPy. Żadna skończona liczba testów nie jest formalnym dowodem wszystkich twierdzeń.

## 4. Nowy rejestr wszystkich dowodów

Utworzono cztery pliki CSV zawierające **382 rozłączne rekordy środowisk proof**: rozdział, ścieżkę źródła, SHA bloba, dokładny zakres numerów wierszy, powiązany typ i tytuł stwierdzenia, etykietę LaTeX, fakt odczytania źródła w tej iteracji oraz status **indywidualnej formalnej certyfikacji**. Rozdzielono zakresy dla czytelności i łatwego przydzielania pracy:

1. [LA01–08: 127 dowodów](iteration_15_proof_ledger_01_08.csv).
2. [LA09–16: 123 dowody](iteration_15_proof_ledger_09_16.csv).
3. [LA17–24: 61 dowodów](iteration_15_proof_ledger_17_24.csv).
4. [LA25–32: 71 dowodów](iteration_15_proof_ledger_25_32.csv).

**Znaczenie statusów:** historyczne audyty rozdziałowe 12–32 są zamknięte i to jest osobne, rzeczywiste osiągnięcie. W ostatnich iteracjach globalnych przeanalizowano wiele istotnych dowodów, w bieżącej odczytano też wszystkie dowody LA29–32. Natomiast kolumna individual_formal_certification=NIE **nie oznacza braku audytów ani matematycznej niepoprawności**: wskazuje wyłącznie brak osobnego, imiennego, wyczerpującego certyfikatu każdego kroku konkretnego dowodu w tej nowej ewidencji. Nie utożsamiamy tej kolumny ze statusem formalizacji Lean prowadzonej odrębnym procesem.

**Weryfikacja globalna na aktualnym drzewie:** 32 pliki rozdziałów; stan z iteracji 10 ma 1083 unikalne etykiety, bez duplikatów i nierozwiązanych odsyłaczy. Porównanie wszystkich SHA z aktualną gałęzią ujawniło **dokładnie jeden zmieniony plik: LA08** (celowa poprawka z iteracji 11). Ponowny odczyt LA08 potwierdził niezmieniony zbiór 43 etykiet i zwiększenie liczby prostych odsyłaczy z 13 do 14. W związku z tym aktualne 32 źródła zachowują **1083 unikalne etykiety i 660 odsyłaczy**, bez brakujących celów (nowy odsyłacz w LA08 jest odsyłaczem do istniejącej etykiety).

## 5. Priorytety dalszej kontroli

1. Weryfikacja krok po kroku wybranych dowodów fundamentalnych LA01–05, szczególnie: zastosowanie lematu Zorna, niezależność i rozpiętość dla baz nieskończonych, ilorazy i poprawność zależności od charakterystyki ciała.
2. Niezależny przegląd **LA12–13**, których wcześniejszą stabilizację rozdziałową odnotowano, ale nie były osobnym nowym blokiem globalnego audytu matematycznego w iteracjach 11–15; porównać ich założenia z LA09, LA14 i LA15.
3. Dla dowodów o zwiększonym ryzyku, zwłaszcza LA24–26 (Riccati) i LA31–32 (Spin/twistory), utworzyć indywidualne wpisy kontrolne opierające się na jawnym rozbiciu wnioskowań, przypadkach brzegowych i niezależnych kontrtestach, bez bezpodstawnego resetu zakończonej sekwencji LA12–32.
4. Po zamknięciu luk w indywidualnych dowodach przeprowadzić jeszcze **jeden dodatkowy sceptyczny audyt globalny**, zanim cała książka zostanie nazwana matematycznie stabilną.

**Reguła zatrzymania:** nie wolno deklarować „wszystkie 382 dowody formalnie zweryfikowane” na podstawie przejścia testów ani sukcesu CI. Istniejące audyty rozdziałowe i CI są realnymi, odrębnymi dowodami jakości; nowy rejestr ma zwiększać weryfikowalność dalszej pracy.
