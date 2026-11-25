# CAT-04 — audyt II (stabilizacyjny)

Stan badany: 943968e951a2574b93dc2cb026a02c3d121d4307.
Źródło CAT-04: cea506e802e9c9eeea411c9681cda97eb137f5f9.
Test CAT-04: 2f73732a0e167af1c44c88814ac3fd6b9e0c445e.

## Kontrola semantyczna
- Naturalność: oba złożenia w kwadracie mają dziedzinę F(A) i przeciwdziedzinę G(B). W kategoriach porządków monotoniczność i nierówność punktowa wystarczają przez jednoznaczność strzałek.
- Podwójna przestrzeń dualna: ewaluacja jest liniowa w v i w funkcjonale; naturalność wynika z definicji f**. Iniektywność wykorzystuje funkcjonał oddzielający niezerowy wektor, przy jawnie wskazanym ZFC. W skończonym wymiarze zgodność wymiarów daje surjektywność. W przykładzie k^(N) dual jest k^N, stały ciąg jedynek nie ma skończonego nośnika. Niezerowy funkcjonał na ilorazie, złożony z projekcją, zeruje wszystkie wektory współrzędnych. Żadna niezerowa ewaluacja przez element k^(N) nie ma tej własności.
- Singleton i działania grup: warunki naturalności zgodne z funktorem obrazu i lewym działaniem. Endomorfizmy identyczności Vect: odwzorowania k→V testują każdy wektor, a w Set odwzorowania z singletonu testują każdy element, także poprawnie potraktowano przypadek pusty. Kontrprzykład naturalnego wyboru bazy wykorzystuje odwracalną transwekcję.
- Pionowe składanie: naturalność obu składowych daje naturalność złożenia, jednostki i łączność punktowe. Przy małym źródle zbiór transformacji jest podzbiorem produktu zbiorów morfizmów; nie utożsamiono lokalnej małości z małością.
- Odwrotność naturalna: przekształcenie równania naturalności przez odwrotności komponentów jest poprawnie typowane. Nie jest potrzebny wybór spośród wielu odwrotności, bo są jednoznaczne.
- Poziome składanie: obie formuły mają typ HF(A)→KG(A), a ich równość daje naturalność beta dla alpha_A. Kolejne kroki dowodu naturalności wykorzystują naturalność beta, funktorialność H i naturalność alpha.
- Prawo wymiany: złożenie beta'_{F2(A)} G1(alpha'_A) beta_{F1(A)} G0(alpha_A) jest dobrze typowane. Naturalność beta zamienia środkową parę na beta_{F2(A)} G0(alpha'_A), po czym funktorialność G0 daje lewą stronę. Łączność pozioma i obie jednostki wynikają z jawnego wzoru na komponent.
- Tensor: izomorfizm R⊗N→N z AA-18, naturalność na generatorach, przemienność R wystarcza dla użytej kategorii R-modułów.
- Odwzorowanie łączące: stopniowa dokładność daje podniesienie b, następnie jednoznaczne a; a jest cyklem przez iniektywność i. Zgodność f_B z i,p i różniczkami daje naturalność delta. Niezależność reprezentantów przywołano z AT-03.
- De Rham: na kołańcuchach gładkich sympleksów równość wynika z funktorialności cofnięcia. Ograniczenie zwykłych kołańcuchów do gładkich jest naturalne i indukuje izomorfizm, którego odwrotność jest naturalna; końcowa równość ma właściwy kierunek kontrawariantny. Twierdzenie de Rhama przywołano z DG-10, nie powielano jego dowodu. Oznaczenie I_M na dwóch poziomach jest rozróżnione przez kontekst (forma / klasa kohomologii).
- GAGA: zachowano właściwość i skończony typ nad C, koherentność snopów; naturalność w zmiennej snopu na ustalonym X. Wynik zewnętrzny, nie przypisano temu rozdziałowi dowodu.
- Nie wykryto nowych istotnych usterek. Nie zmieniono źródła ani nie rozszerzano zakresu.

## CI
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45584545962, commit b0543ae54415156a9f99d3141998ac8558037f0d: job validate completed/success; wszystkie osiem kroków success, w tym discovery testów, kompilacja całej książki, kontrola PDF i odsyłaczy, upload. Zestawy obejmują 4+5+5+6+6 = 26 metod testowych. Porównanie 26 blobów (19 rozdziałów, książka, 5 zestawów testów, workflow): bez różnic. Pełnych logów nie odczytano, PDF nie obejrzano wizualnie. Nie wykonano formalizacji Lean.

## Decyzja
Audyt stabilizacyjny bez zmian zaliczony. Kolejny odrębny audyt III z kontrolą wizualną PDF i niezależnymi kontrolami matematycznymi przed CAT-05.
