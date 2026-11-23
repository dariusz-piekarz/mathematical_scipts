# Analiza funkcjonalna — rozdział 10 — audyt 03 (niezależny przegląd stabilizacyjny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/10-przestrzenie-beczkowe-i-bornologiczne-twierdzenie-banacha-steinhausa.tex`.  
**SHA źródła:** `2ea6b36366c8ec4dc1d2ecf8192fae1054c841b0`, dokładnie ten sam co po zakończeniu audytu 10/02.  
**Testy:** `tools/tests/test_functional_analysis_ch10.py`, SHA `8bf224b484b3058694b8bc82109cbc8d78e9ee42`.  
**Werdykt matematyczno-redakcyjny:** **CZYSTY — 1/2** kolejnych czystych kontroli tego samego źródła. Nie dokonano zmian źródła, testów ani workflow. Rozdział 11 nadal zablokowany do zamknięcia 10 (2/2 + zielony CI).

## Metoda niezależnej kontroli

Pobrano ponownie pełne źródło 10, audyt 10/02, aktualne testy regresyjne, raporty stabilizacji i dziesięć plików kontekstu źródłowego 01–10. Zweryfikowano dokładnie SHA pliku, nie utożsamiając zmian w innych rozdziałach lub raportach ze zmianą w źródle 10. Niezależnie sprawdzono hipotezy twierdzeń, kompletność uzasadnień, przypadki brzegowe oraz logikę przykładów. Osobno sprawdzono strukturalnie środowiska TeX i wszystkie odsyłacze.

## Ponowny audyt 17 dowodów

1. **Polary i ograniczoność punktowa.** `H^\circ` jest przecięciem domkniętych absolutnie wypukłych przeciwobrazów przedziału/dysku. Pochłanianie pojedynczych wektorów jest równoważne punktowej ograniczoności `H` przez dodatnie skalowanie; tekst jawnie obsługuje `H=∅`.
2. **Charakteryzacja beczkowości.** Punktowa ograniczoność `H\subseteq E'` jest tym samym co ograniczoność w `\sigma(E',E)`. Jeśli `E` jest beczkowa, `H^\circ` jest otoczeniem zera; odwrotnie równociągłość `B^\circ` i twierdzenie bipolarne dla LCS Hausdorffa dają `U\subseteq B^{\circ\circ}=B`.
3. **Twierdzenie Baire'a dla zupełnej przestrzeni metrycznej.** Malejące domknięte kule, o promieniach mniejszych od `2^{-n}`, pozostają w kolejnych zbiorach otwartych gęstych. Ich środki tworzą ciąg Cauchy'ego; domkniętość i zupełność pozwalają umieścić granicę we wszystkich otwartych gęstych zbiorach oraz w początkowym otwartym `O`.
4. **Beczkowość przestrzeni Baire'a.** Z pochłaniania i zrównoważenia beczki wynika `E=\bigcup_{n\ge1}nB`. Baire daje niepuste wnętrze `B`; wypukłość i symetria pokazują, że otoczenie zera zawiera się w `B`.
5. **Beczkowość przestrzeni Frécheta i Banacha.** Zastosowanie pełności metrycznej, własności Baire'a i poprzedniego twierdzenia jest poprawne; nie przypisuje się każdej przestrzeni Frécheta normowalności.
6. **Banach–Steinhaus dla przestrzeni beczkowych.** Z lokalnej wypukłości `F` istnieje domknięte absolutnie wypukłe otoczenie `W\subseteq V`. Przecięcie `B=\bigcap_T T^{-1}(W)` jest domknięte, absolutnie wypukłe i punktowo pochłaniające dzięki ograniczoności obrazów. Beczkowość `E` daje równociągłość `\mathcal T`; zupełność `F` nie jest wymagana.
7. **Jednostajna ograniczoność norm operatorów.** Beczkowa przestrzeń Banacha jest dziedziną zastosowania punktu 6; otoczenie normowe zera daje jednolite ograniczenie norm przez skalowanie. Konkluzja nie wymaga kompletności przestrzeni wartości.
8. **Drugi dowód klasycznej zasady (Baire).** Zbiory `A_n=\{x: \sup_T\|Tx\|\le n\}` są domknięte i pokrywają Banacha. Jeden ma wnętrze; odejmując oszacowania `T(x_0+h)` oraz `Tx_0`, otrzymujemy `\|Th\|\le 2N` na kuli, a skalowanie daje wspólną granicę norm operatorów.
9. **Granica punktowa sieci operatorów.** Ograniczoność punktowa jest hipotezą jawną, zatem Banach–Steinhaus daje równociągłość. Dla dowolnego otoczenia `V` zera, domknięte `W\subseteq V` pozwala przejść do granicy po `T_i(U)\subseteq W`; liniowość granicy wynika z ciągłości działań w `F`.
10. **Granica punktowa ciągu operatorów.** Wartości zbieżnego ciągu w każdej TVS są ograniczone jako zbiór; pierwszy krok dowodu odróżnia tę własność od sytuacji dla sieci i pozwala skorzystać z punktu 9.
11. **Jednostajna zbieżność na zbiorach zwartych.** Wspólne otoczenie `U` dla rodziny równociągłej i `T`, skończone pokrycie zwartego `K` zbiorami `x_j+U` oraz jedno wspólne ograniczenie indeksu dla skończonej rodziny punktów dają rozkład błędu w `W+W+W\subseteq V`.
12. **Ograniczoność w topologiach `\tau_s` i `\tau_b`.** Topologia zbieżności jednostajnej na ograniczonych zbiorach jest silniejsza od topologii punktowej. Ograniczoność punktowa, beczkowość i pochłanianie `B\subseteq tU` przez otoczenie pokazują też odwrotną implikację ograniczoności rodzin operatorów.
13. **Funkcjonał Minkowskiego zborny.** Dla absolutnie wypukłego pochłaniającego `C`, `p_C` jest skończoną seminormą. Jej ograniczoność na danym ograniczonym `B` zapewnia wspólne `t` z `B\subseteq tC`, korzystając z `p_C(x)<t`, własności kresu dolnego i zrównoważenia `C`. Domkniętość nie jest używana.
14. **Kryteria bornologiczności.** Dla (i)⇒(ii) zbiór poziomicowy seminormy pochłania ograniczone; (ii)⇒(iii) dla każdej ciągłej seminormy `q` na `F` funkcja `q\circ T` staje się ciągła; (iii)⇒(i) identyczność do przestrzeni z dodatkową seminormą `p_C` zachowuje ograniczoność i musi być ciągła. Zawieranie `\{p_C<1\}\subseteq C` jest poprawne.
15. **Każda przestrzeń unormowana jest bornologiczna.** Absorpcja normowej kuli jednostkowej przez `C` wymusza zawieranie otwartej normowej kuli w `C`, także bez zupełności.
16. **Przestrzenie beczkowe są przestrzeniami Mackeya.** Twierdzenie Mackeya–Arensa daje `\rho\subseteq\tau(E,E')`. Słabo-* zwarty `K\subseteq E'` jest punktowo ograniczony; beczkowość implikuje równociągłość, więc każda generująca seminorma `p_K` jest ciągła dla `\rho`. Daje to przeciwną inkluzję. W odwołaniu nie ma już dawnego dubletu.
17. **Topologia Mackeya Banacha.** Przestrzeń Banacha jest beczkowa, a `\rho=\tau(E,E')` z punktu 16, przy topologii `\rho` normowej.

**Wynik:** 17/17 dowodów poprawnych przy podanych hipotezach. Nie wykryto nowego błędu wymuszającego zmianę źródła.

## Audyt czterech przykładów i ważnej uwagi o sieciach

1. `c_{00}` z normą supremum jest niezupełna. Funkcjonały `f_n(x)=n x_n` mają rosnące normy `n` i są punktowo ograniczone. Polarny zbiór `\{x:n|x_n|\le1\}` jest beczką niebędącą otoczeniem zera — kontrprzykład poprawny.
2. W nieskończenie wymiarowym Banachu z topologią słabą normowa kula jednostkowa jest słabo domkniętą beczką, ale nie otoczeniem. Skończona liczba liniowych funkcjonałów definiujących bazowe otoczenie ma wspólne niezerowe jądro, więc otoczenie zawiera całą nieograniczoną prostą. Wcześniejsza luka dowodowa została poprawiona i nie odtwarza się.
3. Niezupełne `c_{00}` jest bornologiczne jako przestrzeń unormowana i niebeczkowe na mocy przykładu 1. Uwaga o rozróżnieniu bornologiczności i beczkowości nie implikuje błędnej odwrotnej zależności.
4. Dla `C^\infty([0,1])` seminormy pochodnych dają strukturę Frécheta. Funkcjonały `T_n(\varphi)=n\int_{[0,1/n]}\varphi\,\mathrm d\lambda` są równociągłe dzięki `p_0` i punktowo zbieżne do `\varphi(0)`. Zwarte zbiory są objęte wcześniej dowiedzionym kryterium zbieżności jednostajnej.

**Dodatkowy niezależny kontrprzykład z uwagi:** sieć na skończonych podzbiorach `\mathbb N`, równa zero na zbiorach zawierających `1` i równa `|F|` poza nimi, jest zbieżna do zera, lecz ma nieograniczony zbiór wartości. Weryfikuje konieczność ograniczoności punktowej sieci operatorów. Dla ciągów sytuacja jest odmienna.

## Struktura LaTeX i zgodność z wcześniejszymi rozdziałami

Po ponownym pobraniu wszystkich dziesięciu plików źródłowych naliczono **182 etykiety w rozdziałach 01–10, bez duplikatów**, w tym **23 w rozdziale 10**, oraz **14 odsyłaczy rozdziału 10, wszystkich rozwiązywalnych** w tym kontekście. Parowanie środowisk: 5 definicji, 9 twierdzeń, 1 stwierdzenie, 2 lematy, 4 wnioski, 17 dowodów, 4 przykłady, 5 uwag, 2 listy `enumerate`. W źródle nie ma starego `\\mathbf 1_A`, `\\mathbb 1_A`, „zwartości sekwencyjnej” ani powtórzenia nazwy twierdzenia Mackeya–Arensa. Widnieje właściwe `\\ref{thm:mackey-arens}` i doprecyzowany argument wspólnego jądra skończonej rodziny funkcjonałów.

## Bramka techniczna

Dedykowany [GitHub Actions #45217695143](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45217695143) dla poprzedniego raportu 10/02 zakończył się **COMPLETED/SUCCESS**: 13/13 testów regresyjnych, przygotowanie kontekstu LaTeX 01–10, kompilacja PDF, automatyczna kontrola składu i odsyłaczy oraz artefakt — wszystkie kroki PASS. Pliki źródła i testów mają niezmienione SHA. Raport 10/02 dokumentuje osobną inspekcję wizualną stron 55–61 dokumentu, bez znalezionych kolizji i obcięć. Twierdzenia matematyczne oceniono niezależnie od testów i kompilacji; żadnego z tych działań nie przedstawiono jako formalnej weryfikacji matematycznej.

**Po zapisaniu niniejszego raportu trzeba osobno potwierdzić wynik CI wyzwolonego tym commitem.** Zielony wynik poprzedniej iteracji sam w sobie nie poświadcza przebiegu nowego workflow, mimo że źródło się nie zmieniło.

## Decyzja

**Rozdział 10 — 10/03: CZYSTY, pierwszy z dwóch wymaganych audytów stabilizacyjnych (1/2).** Brak zmian źródła LaTeX i brak nowego kontrprzykładu. Następna iteracja: **10/04**, niezależna kontrola tej samej wersji SHA `2ea6b36366c8ec4dc1d2ecf8192fae1054c841b0`. Dopiero dwa czyste przeglądy i zielony dedykowany CI zezwalają na przejście do rozdziału 11.
