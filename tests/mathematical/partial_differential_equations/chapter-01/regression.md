# PDE-01 — trwałe kryteria regresyjne

Źródło: [rozdział 01](../../../../chapters/pl/partial_differential_equations/01-wprowadzenie-do-pde.tex).
Kryteria semantyczne wymagają ponownej oceny po zmianie źródła; nie są automatycznymi testami ani formalizacją Lean.

| ID | Etykieta / sekcja | Kryterium | Metoda |
|---|---|---|---|
| PDE-01-001 | sec:pde-unknown | Równanie Burgersa w podanej postaci ma jedną zmienną przestrzenną. | semantyczna |
| PDE-01-002 | sec:pde-unknown | Odróżnienie równania, zagadnienia i rozwiązania. | semantyczna |
| PDE-01-003 | sec:pde-unknown | C^{1,2} obejmuje ciągłość funkcji i wszystkich wymaganych pochodnych przestrzennych do rzędu 2 i czasowej do rzędu 1, bez wymogu pochodnych mieszanych. | semantyczna |
| PDE-01-004 | sec:pde-types | Superpozycja; obie inkluzje opisu zbioru rozwiązań jako przesunięcia jądra. | semantyczna |
| PDE-01-005 | eq:principal-symbol | Dla D=-i∂ symbol tego samego operatora to i^m p_m; znak dla -Δ zmienia się z -abs(ξ)^2 na +abs(ξ)^2. | semantyczna |
| PDE-01-006 | sec:pde-symbol | Test wysokich częstości jawnie dopuszcza funkcje zespolone i określa operator oraz konwencję. | semantyczna |
| PDE-01-007 | sec:pde-symbol | Funkcja definiująca hiperpowierzchnię jest lokalna i ma niezerową różniczkę. | semantyczna |
| PDE-01-008 | sec:pde-symbol | Wspólne jądro różniczek jest przestrzenią styczną; proporcjonalność z niezerowym czynnikiem i jednorodność symbolu. | semantyczna |
| PDE-01-009 | sec:pde-symbol | Charakterystyczność dotyczy kowektorów; symbol paraboliczny iτ+κabs(ξ)^2 odróżniony od zwykłego symbolu rzędu 2. | semantyczna |
| PDE-01-010 | sec:pde-classification | Macierz zerowa jest poza klasyfikacją; rząd 1, określoność i znaki wartości własnych rozróżnione. | semantyczna |
| PDE-01-011 | sec:pde-classification | Współczynniki A,B,C jawnie określone w stwierdzeniu. | semantyczna |
| PDE-01-012 | sec:pde-classification | J_{ki}=∂_i Φ_k, część główna J A J^T, pochodne drugie Φ tylko w części niższego rzędu; prawo bezwładności. | semantyczna |
| PDE-01-013 | thm:laplace-max | Jawne jednostajne ograniczenie eps*max abs(x)^2 i przejście do granicy. | semantyczna |
| PDE-01-014 | cor:dirichlet-stability | Funkcje rzeczywiste w dowodzie przez zasadę maksimum. | semantyczna |
| PDE-01-015 | cor:dirichlet-stability | Oba oszacowania w i -w oraz jednoznaczność przy zerowych danych różnicowych. | semantyczna |
| PDE-01-016 | eq:neumann-compatibility | Znak warunku zgodności dla -Δu=f i normalnej zewnętrznej. | semantyczna |
| PDE-01-017 | eq:neumann-compatibility | Tożsamość Greena z pola conjugate(w)∇w (w przypadku rzeczywistym w∇w) oraz warunków brzegowych. | semantyczna |
| PDE-01-018 | eq:neumann-compatibility | Zerowa całka gradientu, lokalna stałość i spójność obszaru. | semantyczna |
| PDE-01-019 | ex:burgers-blowup | Równanie charakterystyki z reguły łańcuchowej. | semantyczna |
| PDE-01-020 | ex:burgers-blowup | Ścisła monotoniczność, surjektywność, gładka odwrotność zależna od t,x i weryfikacja PDE oraz danych. | semantyczna |
| PDE-01-021 | prop:heat-kernel | Obliczenie pochodnych jądra i całkowalna majoranta dla różniczkowania. | semantyczna |
| PDE-01-022 | prop:heat-kernel | Ogon gaussowski po skalowaniu i jednostajna zbieżność na całej przestrzeni. | semantyczna |
| PDE-01-023 | thm:dalembert | Obraz t≥0 to ξ≥η, rozkład F+G uzasadniony na półpłaszczyźnie. | semantyczna |
| PDE-01-024 | thm:dalembert | Konstrukcja C², weryfikacja PDE i obu danych początkowych. | semantyczna |
| PDE-01-025 | prop:pde-v31-wave-cone | Zerowe dane implikują zerowy gradient początkowy i energię. | semantyczna |
| PDE-01-026 | prop:pde-v31-wave-cone | Odcinek pionowy zawarty w zwężającym się przedziale; ciągłość na brzegu. | semantyczna |
| PDE-01-027 | prop:heat-uniqueness | Jawne założenie d≥1 i rzeczywistości funkcji w energii kwadratowej. | semantyczna |
| PDE-01-028 | prop:heat-uniqueness | Ograniczona majoranta, zastosowanie Gaussa, zanik wyrazu brzegowego, zerowa energia i wniosek punktowy także na brzegu. | semantyczna |
| PDE-01-029 | prop:pde-v31-wave-cone | Rzeczywistość u i a,b oraz niepusty przedział na całym zakresie czasu. | semantyczna |
| PDE-01-030 | prop:pde-v31-wave-cone | Lokalna tożsamość energii wynika z równania i równości pochodnych mieszanych. | semantyczna |
| PDE-01-031 | eq:pde-v31-wave-cone | Znaki strumienia na obu końcach i poprawne dopełnienie kwadratów. | semantyczna + test skończony |
| PDE-01-032 | ex:laplace-illposed | Harmoniczność i obie dane Cauchy'ego sprawdzone przez różniczkowanie. | semantyczna |
| PDE-01-033 | ex:laplace-illposed | Zbieżność wszystkich ustalonych półnorm C^r. | semantyczna |
| PDE-01-034 | ex:laplace-illposed | Jawna klasa danych i rozwiązań, ciągłość przekroju, jednoznaczność jako założenie argumentu nie wniosek; poprawna asymptotyka normy i normalny kowektor. | semantyczna + test skończony |
| PDE-01-035 | ex:backward-heat | Periodyczność, równanie, półnormy, miara o masie 2π oraz warunki argumentu Hadamarda. | semantyczna + test skończony |
| PDE-01-036 | sec:pde-scaling | Jawne dodatnie parametry i wspólna otwarta dziedzina Q. | semantyczna |
| PDE-01-037 | sec:pde-scaling | Przeciwobrazy otwarte, zachowanie regularności, jawne czynniki λ² w obu równaniach. | semantyczna |
| PDE-01-038 | sec:pde-scaling | Skale czasu wynikają z bezwymiarowych współczynników κτ/ℓ² i c²τ²/ℓ². | semantyczna |
| PDE-01-039 | sec:pde-unknown | Dodanie stałej zachowuje równanie Poissona, jeśli istnieje rozwiązanie. | semantyczna |
| PDE-01-040 | sec:pde-types | Jawna przestrzeń współrzędnych dżetu, dziedzina F i warunek przynależności dżetu. | semantyczna |
| PDE-01-041 | sec:pde-types | Jawne ciało skalarów oraz przynależność danych i rozwiązań do przestrzeni. | semantyczna |
| PDE-01-042 | sec:pde-types | Zgodność oznaczeń zmiennych z poszczególnymi przykładami. | semantyczna |
| PDE-01-043 | sec:pde-symbol | W definicji eliptyczności wskazany symbol główny i jego konwencja. | semantyczna |
| PDE-01-044 | sec:pde-symbol | Jawny znak części głównej w konwencji jednostajnej eliptyczności. | semantyczna |
| PDE-01-045 | eq:neumann-compatibility | Dla funkcji zespolonych pole Greena ma postać conjugate(w)∇w; zastosowanie Gaussa do obu części. | semantyczna |
| PDE-01-046 | eq:neumann-compatibility | Sprzężenie w obu całkach po prawej stronie tożsamości Greena. | semantyczna |
| PDE-01-047 | prop:heat-kernel | Natychmiastowa ścisła dodatniość dotyczy nieujemnych, niezerowych danych, a nie dowolnych danych zmieniających znak. | semantyczna |
| PDE-01-048 | prop:transport | Etykieta punktu na rysunku ma kolejność zgodną z osiami x,t. | kontrola źródła TikZ; renderowanie otwarte |
| PDE-01-049 | sec:pde-types | Rząd określony przez różne wartości F przy tych samych współrzędnych niższego rzędu; dżet w dziedzinie F. | semantyczna |
| PDE-01-050 | sec:pde-data | Jawne dane g, beta, normalna i odpowiednia regularność przy warunkach brzegowych. | semantyczna |
| PDE-01-051 | sec:pde-data | Jawne dziedziny danych początkowych i brzegowych w warunku zgodności. | semantyczna |
| PDE-01-052 | eq:principal-symbol | Wielomian względem kowektora przy ustalonym x, dopuszczony zanik części głównej. | semantyczna |
| PDE-01-053 | eq:neumann-compatibility | Jawny zakres zespolonych danych, wymiar i normalna zewnętrzna. | semantyczna |
| PDE-01-054 | eq:neumann-compatibility | Obie funkcje należą do tej samej klasy zespolonej. | semantyczna |
| PDE-01-055 | ex:burgers-blowup | Charakterystyka na całym przedziale istnienia dowolnego rozwiązania C¹ uzyskana przez czynnik całkujący bez niejawnego założenia globalnego istnienia ODE. | semantyczna |
| PDE-01-056 | ex:burgers-blowup | Jednoznaczność przed t=1 i wykluczenie rozwiązania C¹ na przedziale obejmującym t=1. | semantyczna |
| PDE-01-057 | thm:dalembert | Odwrotność zmiany współrzędnych, jawna reguła łańcuchowa i czynnik -4c². | semantyczna |
| PDE-01-058 | eq:dalembert | Zapis całki z miarą Lebesgue'a zgodny z konwencją skryptu. | semantyczna |
| PDE-01-059 | sec:pde-types | Jawne oznaczenie N₀ i wymiar n. | semantyczna |
| PDE-01-060 | sec:pde-classification | Macierz przekształconej części głównej jest symetryczna; łączny współczynnik mieszany wynosi 2b₁₂, nie b₁₂. | semantyczna |
| PDE-01-061 | eq:tricomi | Napisy obszarów i nierówności odsunięte od osi poziomej. | kontrola wizualna po renderowaniu |
| PDE-01-062 | prop:transport | Oba końce tej samej charakterystyki oznaczone punktami; etykieta nad właściwym końcem. | kontrola wizualna po renderowaniu |
| PDE-01-063 | ex:burgers-blowup | Rozwiązanie rzeczywiste w argumentacji charakterystyk na rzeczywistej osi. | semantyczna |
| PDE-01-064 | thm:dalembert | Wypełnienie obszaru zależności nie zasłania osi czasowej; kolejność warstw TikZ. | kontrola wizualna po renderowaniu |
| PDE-01-065 | thm:dalembert | Tekst w obszarze zależności pozostaje czytelny na tle osi. | kontrola wizualna po renderowaniu |
| PDE-01-066 | cor:dirichlet-stability | Oszacowanie stabilności dotyczy zmiany wartości brzegowych przy ustalonej prawej stronie f. | semantyczna |
| PDE-01-067 | eq:neumann-compatibility | Jeśli rozwiązanie istnieje, zbiór wszystkich rozwiązań to u+C; sprawdzony również kierunek dodawania stałej. | semantyczna |
| PDE-01-068 | prop:heat-kernel | Normalizacja Gaussa z jakobianem i iloczynem całek jednowymiarowych, z uzasadnieniem Tonellego. | semantyczna |
| PDE-01-069 | thm:dalembert | Jawne całkowanie F' na przedziale [η,ξ] i wykorzystanie F(η)+G(η)=u₀(η). | semantyczna |
| PDE-01-070 | ex:backward-heat | D zawiera 0 i wszystkie g_k, ciągłość przekroju końcowego do L² jest jawna, a sprzeczność wynika z założenia jednoznaczności i ciągłości S. | semantyczna |

## Pierwsze wykonanie — 2026-11-24
Przejrzano kryteria 001–012 w poprawionym tekście (commit 6c55830d79679c70a164546a1f0ff953198e29f6). Kontrola strukturalna wykonana na treści przed zapisem: zachowano 35 etykiet, wszystkie 14 odsyłaczy wewnętrznych rozwiązywalne, środowiska begin/end poprawnie zagnieżdżone. Nie wykonano kompilacji LaTeX, renderowania rysunków ani Lean. Rozdział pozostaje otwarty; dalsze sekcje od sec:pde-models wymagają osobnego audytu.

## Druga iteracja — 2026-11-24
Przegląd semantyczny kryteriów 013–026 w ramach poprawek (commit 9eb95ea38bff8f46eab3e0ceaccc3e2a2606ff55). Kontrola strukturalna wykonana: 35 etykiet zachowanych, 15 odsyłaczy wewnętrznych rozwiązywalnych, środowiska poprawnie zagnieżdżone. Nie wykonano kompilacji ani renderowania; Lean nie uruchomiono. Otwarte: kontrola energetyczna równania ciepła, przykłady Hadamarda, skalowanie, niezależna kontrola całości oraz rysunki i kompilacja.

## Trzecia iteracja — 2026-11-24
Poprawki 027–038: commit 47eb7d7fd982665bb242cf58fd4a4319e342882d. Przegląd semantyczny zmienionych fragmentów wykonany; kontrola strukturalna: 35 niezmienionych unikalnych etykiet, 15 rozwiązywalnych odsyłaczy, zgodne zagnieżdżenie środowisk. Wykonano skończoną kontrolę rachunkową: 45 kombinacji całkowitych (c,p,q) dla obu tożsamości strumienia, 5 trybów k dla stosunku normy do asymptotyki i dyskretnej kontroli całki sin² na torusie. Wyniki pozytywne; nie zastępują dowodów. Pierwszy przebieg treści ukończony, niezależny audyt całości, kompilacja i renderowanie pozostają otwarte. Lean nie uruchomiono.

Testy wykonywalne: [test_energy_hadamard.py](test_energy_hadamard.py), commit 3dc7d65094e81c280c3b3aa3d81c7963dbde3377. Uruchomiono lokalnie kopię o identycznym SHA blob 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2: 3/3 testy unittest zaliczone. Polecenie: `python tests/mathematical/partial_differential_equations/chapter-01/test_energy_hadamard.py -v`.

## Czwarta iteracja — 2026-11-24
Niezależny audyt stabilizacyjny, poprawki 039–048: commit 49589c74363fbb591d9d0045493ec46d461be5bb. Kontrola strukturalna wykonana na zmienionym źródle: 35 etykiet zachowanych, 16 odsyłaczy rozwiązywalnych, środowiska zgodne. Ponownie wykonano plik test_energy_hadamard.py zgodny z SHA blob 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2: 3/3 testy unittest zaliczone. Kontrola renderowania i kompilacji jeszcze otwarta. Zmiany wymagają ponownego audytu; rozdział nie jest ustabilizowany.

## Piąta iteracja — 2026-11-24
Poprawki 049–058: commit d646625027396ec01feee4d3a77a2efea064ce55. Ponowna kontrola strukturalna zmienionego źródła: 35 niezmienionych etykiet, 16 rozwiązywalnych wystąpień odsyłaczy, zgodne środowiska. Workflow [45404958762](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45404958762) na wcześniejszym commicie d6b27b9 potwierdził sukces kroku testów wykonywalnych i kontroli strukturalnej; kompilacja była w toku w chwili sprawdzenia. Nie przenosić wyniku starszego workflow na nowy commit. Kryteria 049–058 sprawdzono semantycznie przy poprawkach; niezależny ponowny przegląd i kompilacja aktualnej wersji oraz wizualna kontrola rysunków pozostają otwarte. Lean nie uruchomiono.

## Szósta iteracja — 2026-11-24
Poprawki 059–065: commit 193afa2c7da2d781a6bd486c464ba2caaf6650c3. Kontrola strukturalna zmienionego tekstu: 35 zachowanych unikalnych etykiet, 16 rozwiązywalnych odsyłaczy, poprawnie zagnieżdżone środowiska. Starszy [workflow 45404958762](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45404958762) zakończył się sukcesem, w tym testy, kompilacja, diagnostyka i renderowanie. Pobrano artefakt 14925920421 (14 stron PNG) i przeprowadzono oględziny układu stron oraz trzech rysunków (s. 6, 8, 11). Wnioski: zwiększyć odstęp napisów od osi, wyróżnić właściwą charakterystykę punktami, nie zasłaniać osi czasowej w stożku. Poprawiono źródło trzech rysunków; nowe renderowanie wymaga ponownej kontroli. Dla wersji po piątej iteracji potwierdzono sukces kroków testów i kontroli strukturalnej w przebiegu 45405221487; nie jest to wynik dla commitu szóstej iteracji. Lean nie uruchomiono. Rozdział nadal otwarty.

## Siódma iteracja — 2026-11-24
Poprawki 066–069: commit f2811c1705ad6c0f307da03fe02c9a0d4b9c5fb5. Ponowny przegląd definicji, symbolu, klasyfikacji, modeli i zakresu oszacowań; nowe kryteria sprawdzone semantycznie. Kontrola strukturalna: 35 niezmienionych etykiet, 16 rozwiązywalnych odsyłaczy, poprawne zagnieżdżenie środowisk. [Przebieg 45405221487](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45405221487) wersji po piątej iteracji zakończył się sukcesem wszystkich kroków, w tym testów, kompilacji i diagnostyki. Przebieg 45405581130 wersji po szóstej iteracji był w kolejce podczas kontroli; nie potwierdzono jeszcze wizualnie ostatnich zmian rysunków. Wyniki CI wcześniejszych wersji nie zastępują weryfikacji nowego źródła. Lean nie uruchomiono. Rozdział otwarty.

## Ósma iteracja — 2026-11-24
Przejrzano ponownie dziewięć sekcji, 13 dowodów i źródła trzech rysunków. Uściślenie 070: commit 0a8317a2cb7e7e50c5ff312c11dce61da22aca7d. Przed poprawką sprawdzono automatycznie 69 unikalnych ID kryteriów i ich przypisanie do istniejących etykiet; po poprawce zachowano 35 etykiet, wszystkie 16 wystąpień odsyłaczy rozwiązywalne, środowiska zgodnie zagnieżdżone. Ujednolicono treść kryterium 017 z zespoloną wersją tożsamości Greena (045–046). Najnowsze przebiegi 45405542870, 45405581130, 45405754612 i 45405788704 pozostawały w kolejce podczas kontroli. Nie uruchomiono lokalnie testów Python ani Lean; aktualna kompilacja i kontrola nowych renderów pozostają niepotwierdzone. W tej iteracji nie rozszerzano zakresu tematycznego. Rozdział pozostaje otwarty.

## Dziewiąta iteracja — 2026-11-24
Kontrola bez zmiany treści rozdziału (blob aeea9d0a8c39cb2a2049d0cd982688dd370fc874). Ponowny przegląd zakresu ostatniego kontrprzykładu, argumentów energetycznych, charakterystyk, normalizacji jądra ciepła i wzoru d'Alemberta nie ujawnił nowych istotnych błędów matematycznych. Kontrola strukturalna wykonana na aktualnym źródle: 35 unikalnych etykiet, 16 rozwiązywalnych odsyłaczy, 13 dowodów, trzy środowiska TikZ, poprawne zagnieżdżenie środowisk. Wszystkie 70 kryteriów ma unikalne, ciągłe ID oraz istniejącą etykietę źródłową. Lokalnie wykonano test_energy_hadamard.py po sprawdzeniu zgodności SHA blob 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2 z repozytorium: Python 3.13.5, 3/3 unittest, OK. Przebieg 45406319616 na commicie 9006c80 pozostawał w kolejce. Próba pobrania identycznego źródła do lokalnego środowiska kompilacji przez raw.githubusercontent.com nie powiodła się (brak rozwiązywania DNS). Nie wykonano kompilacji aktualnej wersji ani wizualnej kontroli aktualnych renderów; Lean nie uruchomiono. Bez nowych poprawek treści, ale stabilizacja niepotwierdzona z powodu otwartych kontroli kompilacji i grafiki. Nie uznawać 70 kryteriów za 70 testów automatycznych.
