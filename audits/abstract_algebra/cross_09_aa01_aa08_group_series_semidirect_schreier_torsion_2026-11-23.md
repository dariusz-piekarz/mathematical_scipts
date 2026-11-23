# Algebra abstrakcyjna — AA-X09: przekrojowy audyt AA-01–AA-08

**Data:** 23 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Cel:** weryfikacja zależności matematycznych między podstawami teorii grup, działaniami, twierdzeniami Sylowa, szeregami kompozycyjnymi, iloczynami półprostymi, twierdzeniem Nielsena–Schreiera oraz torsją i iloczynami tensorowymi grup abelowych.

## 1. Nieredundantny zakres kontroli

W repozytorium jest już osobny, węższy raport `audits/abstract_algebra/cross_08_aa01_aa04_group_actions_sylow_2026-11-23.md` (AA-01–AA-04, bez deklaracji przejścia pełnego CI). AA-X09 **nie powtarza** tamtej kontroli w tej samej postaci: uwzględnia niezależne testy ogólnych zależności AA-01–AA-08, rozszerza model o wszystkie podgrupy \(A_5\), wszystkie dostępne szeregi kompozycyjne i działania nienormalnych podgrup grup wolnych, a także testuje połączenia z modułami abelowymi.

Badane źródła TeX (bez zmian matematycznych):

| Rozdział | Temat | Git blob SHA |
|---|---|---|
| AA-01 | Grupy, podgrupy, grupy cykliczne | `0e731cc5ef69286f613babc46920cf615f9fef65` |
| AA-02 | Warstwy, twierdzenie Lagrange’a, grupy ilorazowe | `36efd06e0da961cc60dadc061ebc43122e4f14f2` |
| AA-03 | Działania grup, orbity i równanie klas | `b817e09694997218ab1933bc9c7e9972e1274173` |
| AA-04 | Cauchy i trzy twierdzenia Sylowa | `503c8fa744e5d5e943c263426d29fa8964038c4d` |
| AA-05 | Szeregi podnormalne, rozwiązalność, nilpotentność | `92637c6195a534178e977a16e5541266b074dad5` |
| AA-06 | Iloczyny proste, półproste i rozszerzenia grup | `e504d9d70bc66e0307c466e4be1a0fb2d33dfe30` |
| AA-07 | Grupy wolne, prezentacje, Nielsen–Schreier | `931eb83323a543e55cc9e4c439ab864111d65264` |
| AA-08 | Grupy abelowe, torsja, iloczyn tensorowy | `d6de6b6cb0e01449c8f976b662960cd0425abd90` |

## 2. Niezależna kontrola przejść dowodowych

### AA-01–AA-04 → AA-05: Lagrange, Cauchy, Sylow, szeregi normalne

Przejścia od podgrup normalnych i twierdzeń o izomorfizmie do szeregów kompozycyjnych wymagają rozróżnienia „\(G_i\) jest normalna w \(G_{i-1}\)” od silniejszego „\(G_i\) jest normalna w \(G\)”. Twierdzenie Jordana–Höldera w AA-05 poprawnie używa **dwóch różnych maksymalnych właściwych podgrup normalnych** \(N,M\triangleleft G\), ich przecięcia \(L=N\cap M\) i izomorfizmów \(N/L\cong G/M\), \(M/L\cong G/N\). W dowodzie nie zakłada się zachowania kolejności czynników.

Porównano dwa szeregi: pochodny \(G^{(i+1)}=[G^{(i)},G^{(i)}]\) i dolny centralny \(\gamma_{i+1}(G)=[\gamma_i(G),G]\). Dla nilpotentności liczy się koniec szeregu dolnego, podczas gdy dla rozwiązalności — koniec szeregu pochodnego. Sprawdzono w konkretnych grupach \(S_3,S_4,A_4,D_8,A_5\), że rozwiązalność nie implikuje nilpotentności, a \(D_8\) jest nilpotentna klasy dwa.

Wykorzystanie faktu, że **każda skończona \(p\)-grupa jest nilpotentna**, opiera się na niebanalnym centrum dowolnego niebanalnego ilorazu będącego \(p\)-grupą. To twierdzenie jest powiązane z równaniem klas w AA-03 i stanowi podstawę dowodu AA-06, że nilpotentność skończonej grupy jest równoważna normalności wszystkich jej podgrup Sylowa.

### AA-04/AA-05 → AA-06: półproste i klasyfikacja grup rzędu \(pq\)

W twierdzeniu o iloczynie półprostym normalność jądra jest konieczna, ale sama normalność nie wystarcza do rozszczepienia: potrzebna jest podgrupa dopełniająca. AA-06 odróżnia rozszczepione rozszerzenia od nierozszczepionych (np. \(C_4\) nie jest \(C_2\rtimes C_2\)). W klasyfikacji grup rzędu \(pq\), przy \(p<q\), Sylow daje jedyną normalną podgrupę rzędu \(q\), a działanie \(C_p\to\operatorname{Aut}(C_q)\) może być nietrywialne tylko gdy \(p\mid(q-1)\).

Nowy test konstruuje bezpośrednio iloczyny półproste \(C_q\rtimes C_p\), sprawdza **łączność dla każdej trójki elementów**, jednoznaczność odwrotności i nieprzemienność wynikającą z nietrywialnego działania. Przypadki: \((p,q)=(2,3),(2,5),(2,7),(2,11),(3,7),(3,13)\).

### AA-01/AA-02 → AA-07: grafy warstw i Nielsen–Schreier

Dla dowolnej podgrupy \(H\le F(S)\) graf Schreiera ma wierzchołki będące **prawymi warstwami** \(Hg\). Nie wolno przypisywać im struktury grupy ilorazowej, jeśli \(H\) nie jest normalna. Dla każdego \(s\in S\) trzeba ponadto rozróżnić skierowaną krawędź dodatnią od odwrotnego przejścia po tej samej krawędzi; dwa przeciwne łuki dodatnio oznaczone przez \(s\) mogą być różnymi krawędziami.

Dowód AA-07 wykorzystuje spójność grafu Schreiera, drzewo rozpinające i pętle powiązane z każdą krawędzią spoza drzewa. Skreślanie kolejnych odwrotnych liter wolnego słowa odpowiada usuwaniu natychmiastowego powrotu tą samą krawędzią grafu. Ten mechanizm zapewnia nie tylko generowanie podgrupy przez elementy \(h_e\), lecz również **brak dodatkowych relacji**, co jest niezbędne dla wniosku o wolności \(H\). W przypadku indeksu skończonego \(d\) i rangi \(r\), graf ma \(dr\) krawędzi dodatnich i \(d-1\) krawędzi drzewa, więc ranga \(H\) wynosi \(1+d(r-1)\).

### AA-04/AA-06/AA-07 → AA-08: grupy abelowe i iloczyny tensorowe

W AA-08 każda skończona grupa abelowa rozkłada się kanonicznie na części \(p\)-pierwotne, będące zarazem jedynymi podgrupami Sylowa dla poszczególnych \(p\). Dowód wykorzystuje projekcje z chińskiego twierdzenia o resztach (tożsamość Bézouta), a nie klasyfikację wszystkich skończenie generowanych modułów; tym samym nie ma niejawnej zależności od późniejszego rozdziału o postaci Smitha.

Własność uniwersalna iloczynu tensorowego opiera się na **dwuliniowości** odwzorowań grup abelowych; iloczynu tensorowego nie można utożsamiać z iloczynem prostym. Sprawdzono kolejno \((\mathbb Z/m\mathbb Z)\otimes_\mathbb Z B\cong B/mB\), \(C_m\otimes_\mathbb Z C_n\cong C_{\gcd(m,n)}\), a także charakter odpowiadających odwzorowań dwuliniowych.

## 3. Test A — dokładne modele grup skończonych

**Repozytorium:** `tools/tests/test_abstract_algebra_cross_aa01_08_groups.py`.

Test samodzielnie reprezentuje permutacje, wyznacza wszystkie podgrupy \(S_3,S_4,A_4,D_8,A_5\) jako domknięcia podgrup generowanych, wylicza ich normalizatory, obrazy sprzężone, ciągi pochodne i centralne, wszystkie dostępne szeregi kompozycyjne oraz sprawdza twierdzenia o liczbie podgrup Sylowa.

| Grupa | Rząd | Wszystkie podgrupy | Liczności podgrup Sylowa |
|---|---:|---:|---|
| \(S_3\) | 6 | 6 | \(n_2=3,\ n_3=1\) |
| \(S_4\) | 24 | 30 | \(n_2=3,\ n_3=4\) |
| \(A_4\) | 12 | 10 | \(n_2=1,\ n_3=4\) |
| \(D_8\) | 8 | 10 | \(n_2=1\) |
| \(A_5\) | 60 | 59 | \(n_2=5,\ n_3=10,\ n_5=6\) |

Oprócz tego sprawdzono działanie na wszystkich warstwach każdego podgrupowego \(H\), równość Burnside’a, prawo Lagrange’a, jedyność podgrup Sylowa tam, gdzie jest ona wymagana, prostotę \(A_5\) oraz normalizatory właściwych podgrup \(D_8\). To są **rzeczywiste obliczenia na wszystkich podgrupach wskazanych modeli**, a nie tylko sprawdzenia tekstu źródłowego.

## 4. Test B — niezależne grafy Schreiera, torsja i tensor

**Repozytorium:** `tools/tests/test_abstract_algebra_cross_aa05_08_schreier_tensor.py`.

Nie korzysta z permutacyjnych implementacji grup i enumeracji podgrup Testu A. Operuje bezpośrednio na grafach o wierzchołkach związanych z działaniami generatorów grup wolnych oraz na niezależnej arytmetyce grup abelowych.

Szczegóły:
- pięć grafów Schreiera z rangą początkową \(2\) albo \(3\) i indeksem \(d\in\{2,3,4\}\); wybrane działania dają zarówno podgrupy normalne, jak i **nienormalne**;
- automatyczna konstrukcja drzewa rozpinającego i generatorów \(h_e=t_vet_w^{-1}\), a następnie potwierdzenie rangi \(1+d(r-1)\);
- bezpośrednie przepisanie wszystkich rozpatrywanych słów zredukowanych w starych generatorach (długość do \(6\)) na nowe generatory oraz sprawdzenie, że rozwinięcia nie zmieniają słowa w grupie wolnej;
- sprawdzanie niezależności wszystkich zredukowanych słów w nowych generatorach do długości \(3\);
- jawne projekcje CRT i części \(p\)-pierwotne dla wszystkich grup \(C_m\oplus C_n\), \(1\le m,n\le20\), łącznie ze wszystkimi elementami;
- biliniowe odwzorowania \(C_m\times C_n\to C_k\), \(1\le m,n\le60,\ 1\le k\le12\), poprzez rzeczywistą listę dopuszczalnych obrazów pary generatorów. Ich liczba musi wynosić \(\gcd(m,n,k)\).

Oba testy uruchomiono lokalnie na oddzielnych, rozwiniętych prototypach oraz dodano w wersji repozytoryjnej do GitHub Actions. Faktyczny wynik obu kroków CI należy potwierdzić osobno.

## 5. Struktura LaTeX

| Rozdział | Unikatowe etykiety | Wystąpienia odsyłaczy | Dowody | Przykłady |
|---|---:|---:|---:|---:|
| AA-01 | 24 | 0 | 12 | 8 |
| AA-02 | 33 | 1 | 23 | 13 |
| AA-03 | 21 | 4 | 11 | 11 |
| AA-04 | 18 | 2 | 12 | 8 |
| AA-05 | 27 | 16 | 14 | 6 |
| AA-06 | 21 | 20 | 11 | 8 |
| AA-07 | 28 | 9 | 15 | 6 |
| AA-08 | 31 | 4 | 12 | 8 |
| **Razem** | **203** | **56** | **110** | **68** |

**Wszystkie 203 etykiety są unikatowe.** Wszystkie 56 odsyłaczy wskazuje na istniejące definicje, twierdzenia i przykłady. Jedyny cel poza AA-01–AA-08 to `aa:ch:module-tensor-product` z AA-18, którego obecność zweryfikowano w oryginalnym źródle. Składnia środowisk LaTeX `\begin`/`\end` jest zagnieżdżona poprawnie. Pełna książka `books/pl/abstract_algebra.tex` uwzględnia wszystkie osiem rozdziałów w poprawnej kolejności.

## 6. Podgląd składu

Z ostatniego **wcześniej zakończonego z sukcesem** artefaktu PDF wyrenderowano i przejrzano komplet **61 stron** AA-01–AA-08:
- AA-01: strony PDF **10–16** (7);
- AA-02: **17–26** (10);
- AA-03: **27–33** (7);
- AA-04: **34–41** (8);
- AA-05: **42–48** (7);
- AA-06: **49–56** (8);
- AA-07: **57–63** (7);
- AA-08: **64–70** (7).

Uwzględniono rysunki działań grup, grafy warstw i graf Schreiera. W tak przeprowadzonych oględzinach nie stwierdzono widocznych kolizji, ucięć ani przepełnień. **Wydanie z nowego workflow** wymaga osobnego potwierdzenia i porównania stron z obejrzaną wersją.

## 7. Warunek końcowego zamknięcia

Należy potwierdzić rzeczywisty sukces GitHub Actions dla dwóch nowych testów i pełnej kompilacji AA-01–AA-42, pobrać nowy artefakt PDF, przejrzeć log LaTeX i porównać strony AA-01–AA-08 pikselowo z opisanym wyżej PDF. **AA-X09 nie jest jeszcze oznaczony jako zamknięty**, jeśli te czynności nie zostały potwierdzone. Samo dodanie kroków do CI nie oznacza ich przejścia.
