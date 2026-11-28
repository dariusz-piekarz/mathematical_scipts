# Topologia ogólna — rozdział 19, audyt iteracja 01

Data: 2026-11-22. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło: chapters/pl/general_topology/19-przestrzenie-polskie-i-zbiory-borelowskie.tex.
Zbadany blob TeX: 6296e0559f0bc9a0d10690b6064374927ad83d36.
Test: tools/tests/test_general_topology_ch19.py.

## Zakres i zależności

Rozdział 19 przedstawia definicję przestrzeni polskiej; drugi aksjomat przeliczalności; przykłady R^m, (0,1), przestrzeni Cantora 2^N i przestrzeni Baire'a N^N; przeliczalne iloczyny; definicje F_sigma i G_delta; pełną charakterystykę podprzestrzeni polskich przez G_delta; przykłady Q i R\Q; sigma-algebrę borelowską, jej ślad, przeliczalne generatory, borelowskość odwzorowań; skończone i pozaskończone poziomy hierarchii oraz wyczerpanie całej sigma-algebry borelowskiej indeksami α<ω_1.

Wykorzystywane wcześniejsze wyniki: rozdział 07 (zwartość, twierdzenie Tychonoffa), 09 (drugi aksjomat przeliczalności i ośrodkowość), 10 (metryzowalność), 11 (zupełność i twierdzenie Baire'a), 12–13 (struktury jednostajne i zupełność). Rozdział 20 zachowuje dla siebie zbiory analityczne i dalszą opisową teorię mnogości. Nie powtórzono istniejących pełnych dowodów tych wyników.

## Audyt matematyczny

1. **Definicja przestrzeni polskiej.** Wymagana jest istnienie zgodnej metryki zupełnej oraz ośrodkowość, nie zupełność każdej metryki. Drugi aksjomat przeliczalności wyprowadzono przez bazę kul B_d(a,r) dla a z przeliczalnego zbioru gęstego i dodatniego promienia wymiernego, z jawnym wyborem d(x,a)<ε/2.
2. **Przykład (0,1).** Metryka d_*(s,t)=|log(s/(1−s))−log(t/(1−t))| jest przeniesieniem zwykłej metryki prostej przez homeomorfizm, stąd jest zupełna i zgodna. To odróżnia polskość od zupełności naturalnej metryki euklidesowej na przedziale.
3. **Cantor i Baire.** Ultrametryka 2^{-k}, gdzie k to pierwszy indeks różnych współrzędnych, wyznacza topologię produktu. Dla ciągu Cauchy'ego każda początkowa skończona grupa współrzędnych jest ostatecznie stała; granica jest określona współrzędnie i wyrazy do niej zbiegają. Ciągi o ostatecznie stałym ogonie tworzą przeliczalny zbiór gęsty. 2^N jest zwarta przez Tychonoffa, N^N nie jest zwarta przez ciągły, surjektywny rzut na nieskończoną dyskretną N.
4. **Przeliczalne iloczyny polskich.** Suma D(x,y)=Σ2^{-n}min(1,d_n(x_n,y_n)) definiuje zgodną metrykę. Zwarta kontrola ogona i finitarnych współrzędnych daje topologię produktu i zupełność. Separowalność: ciągi o skończenie wielu współrzędnych różnych od punktu bazowego, z tymi współrzędnymi w D_n, tworzą przeliczalny zbiór gęsty. Iloczyn z pustym czynnikiem jest pusty i polski.
5. **Otwarte F_sigma i domknięte G_delta.** Dla niepustego dopełnienia F=X\U funkcja d(x,F) jest ciągła, a U=⋃_n{x:d(x,F)≥1/n}; przypadek U=X rozważono oddzielnie. Dualność dla zbiorów domkniętych wynika przez dopełnienia.
6. **Podprzestrzenie polskie = G_delta.** Dla A=⋂U_n w polskiej X z metryką zupełną d zdefiniowano h_n=1/d(x,X\U_n) na A, przy U_n=X ustalając h_n=0, oraz ρ=d+Σ2^{-n}min(1,|h_n(x)−h_n(y)|). Metryka ρ jest zgodna; jeśli x_j jest w niej Cauchy'ego, granica w d nie może leżeć poza żadnym U_n, gdyż odpowiednia h_n(x_j) dążyłaby do ∞. Zatem granica leży w A i ciąg zbiega do niej w ρ. Ośrodkowość jest dziedziczona przez podprzestrzeń metryczną dzięki przeliczalnej bazie.
7. **Odwrotny kierunek G_delta.** Jeśli A ma zgodną zupełną metrykę σ, dla każdego a∈A oraz n wybiera się promień r_n(a)<2^{-n}, aby średnica w σ zbioru B_d(a,2r_n(a))∩A była <2^{-n}. Otwarte V_n=⋃_a B_d(a,r_n(a)) zawierają A. Dla x∈⋂V_n dobrano a_n∈A z d(x,a_n)<r_n(a_n). Ciąg a_n dąży do x w d. Dla ustalonego n późne a_m należą do B_d(a_n,2r_n(a_n))∩A, co daje oszacowanie Cauchy'ego w σ; kompletność σ daje granicę a∈A i jednoznaczność granicy d wymusza x=a. Tym samym A=⋂V_n.
8. **Q i niewymierne.** Q jest F_sigma jako przeliczalna suma singletonów, ale nie jest G_delta: byłaby wtedy polska, co przeczy twierdzeniu Baire'a, bo Q jest przeliczalną sumą nigdziegęstych singletonów w swojej topologii. Dopełnienie Q jest G_delta i polskie, a nie jest F_sigma.
9. **Borel i ślad.** Sigma-algebra B(X) jest generowana przez otwarte zbiory. Równość B(A)={A∩B:B∈B(X)} udowodniono przez dwa zawierania i dwa sigma-algebry. Gdy X spełnia drugi aksjomat przeliczalności, jej B(X) jest generowana przez przeliczalną bazę; dla R wystarczą przedziały o wymiernych końcach. Odwzorowanie jest borelowskie wtedy i tylko wtedy, gdy przeciwobrazy wszystkich otwartych są borelowskie; dowiedziono też tego dla ciągłości i składania.
10. **Hierarchia borelowska skończona.** Klasy Σ^0_n i Π^0_n mają jawne definicje, dualność przez prawa de Morgana, a domknięcie na przeliczalne sumy i przecięcia przez dwuwskaźnikowe przeliczalne rodziny. Dla X metryzowalnej otwarte są F_sigma i domknięte G_delta, co zapewnia rosnącość poziomów i zawieranie Σ_n∪Π_n⊂Σ_{n+1}∩Π_{n+1}.
11. **Istotna korekta wykryta w audycie 01.** Definicja hierarchii Σ^0_{n+1} jako sum klas Π^0_n i definicja dla ordinalnego α>1 jako sum wcześniejszych Π^0_β wymagają osobnego sprawdzenia zgodności. W przestrzeniach metryzowalnych są zgodne, ponieważ poziomy Π są rosnące. Nie wolno bez dowodu przenosić tej zgodności na wszystkie przestrzenie topologiczne. Dlatego obie definicje hierarchii i twierdzenia o niej mają obecnie jawne założenie metryzowalności, wraz z wyjaśnieniem zgodności na poziomach skończonych. Ogólne pojęcie B(X) i lemat o śladzie pozostają poprawnie sformułowane dla dowolnych przestrzeni topologicznych.
12. **Hierarchia pozaskończona.** Dla α<ω_1 używa się klas Σ^0_α otrzymywanych przez przeliczalne sumy zbiorów Π^0_{β_n} z β_n<α. Każdy poziom leży w B(X). Suma C wszystkich Σ^0_α zawiera otwarte i jest zamknięta na dopełnienia, bo Π^0_α⊂Σ^0_{α+1}. Ponadto A∈Σ^0_α implikuje A∈Π^0_{α+1}, ponieważ jego dopełnienie z Π^0_α należy do Σ^0_{α+1}; zatem dla przeliczalnej rodziny A_n wybieramy γ=sup_n(α_n+2)<ω_1 i otrzymujemy ⋃A_n∈Σ^0_γ. To dowodzi, że C jest sigma-algebrą i C=B(X), a równość z sumą poziomów Π uzyskuje się przez dopełnienia. Wcześniejsze mylące przejście o dwa poziomy zastąpiono przejściem o jeden.
13. **Poziomy skończone nie wystarczają.** Rozdział nie twierdzi fałszywie, że B(X)=⋃_{n<ω}Σ^0_n; wprowadza wszystkie przeliczalne ordinalne indeksy. Twierdzenie o ścisłości hierarchii jest odłożone do narzędzi opisowej teorii mnogości.
14. **Terminologia, przykłady i struktura.** Zachowano poprawne nazwy „przestrzeń polska”, „przestrzeń Cantora”, „przestrzeń Baire'a”, „zbiór typu F_sigma/G_delta”, „sigma-algebra borelowska”, „odwzorowanie borelowskie” oraz użytkowe konwencje dotyczące ciągów, sieci, aksjomatów przeliczalności i uzwarceń. Twierdzenia mają jawne hipotezy i oznaczenia, bez niejawnego kontekstu.

## Integracja i testy

Zapisano standalone books/pl/general_topology_ch19.tex, wpis do books/pl/general_topology.tex i catalog/books.json, plan docs/pl/plan_topologii_ogolnej.md i rozszerzony workflow .github/workflows/general-topology-chapter.yml. Test rozdziału 18 zachowuje swoją pozycję przy powiększeniu książki.

Nowy tools/tests/test_general_topology_ch19.py kontroluje 29 topologii na trzyelementowym zbiorze, 232 ślady sigma-algebr borelowskich w podprzestrzeniach, ultrametrykę słów binarnych długości 4 (4096 trójek), strukturalne etykiety, zamknięcie odsyłaczy i zakazaną terminologię. Modele skończone są testami regresji, nie formalizacją twierdzeń o przeliczalnych ordinalnych rangach.

## Walidacja techniczna

Workflow [45018362870](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45018362870), obejmujący aktualne źródło i testy rozdziału 19, zakończył się **completed/success**, bez nieudanych kroków. Oddzielnie potwierdzono zielony test rozdziału 19, kompilację pełnej książki, samodzielnego rozdziału 19 i kontrolę logów. Artefakt \`14753160560\` pobrano do \`/mnt/data/topologia19_audyt01\`. Plik \`general_topology_ch19.pdf\` ma **6 stron A4**. Wyrenderowano i obejrzano wszystkie sześć stron, w tym wszystkie wzory w dowodzie twierdzenia o G-delta oraz hierarchii borelowskiej. Brak nachodzącego tekstu, uciętych wzorów lub problemów z numeracją. Strona końcowa ma mniej tekstu, ale nie zawiera usterek typograficznych. Dwa logi — \`general_topology_ch19.log\` i \`general_topology.log\` — nie zawierają \`Overfull\`, \`Underfull\`, \`LaTeX Warning\`, \`Missing character\`, \`Undefined control sequence\` ani \`Fatal error\`.

| Obszar | Stan |
| --- | --- |
| Dowody o przestrzeniach polskich | PASS w audycie 01 |
| Twierdzenie o podprzestrzeniach G_delta | PASS w audycie 01 |
| Borel, ślady, generatory i odwzorowania | PASS w audycie 01 |
| Skończona i pozaskończona hierarchia | PASS po korekcie hipotez |
| Kompilacja, testy i PDF | **PASS — run 45018362870, 6 stron A4** |
| Stabilizacja | W AUDYCIE — wymaga kolejnych niezależnych iteracji |

Źródła dodatkowej weryfikacji: David Marker, Descriptive Set Theory, twierdzenie o polskich podprzestrzeniach G_delta; Alexander S. Kechris, Classical Descriptive Set Theory, §3; standardowa definicja hierarchii borelowskiej dla przeliczalnych liczb porządkowych. Dowody w rozdziale zapisano od podstaw, nie są kopiami wskazanych opracowań.
