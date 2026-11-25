# PDE I — rozdział 09: trwały rejestr regresji matematycznych

Źródło: `chapters/pl/partial_differential_equations/09-przestrzenie-sobolewa.tex`. Kryteria semantyczne sprawdza się przez lekturę twierdzeń i dowodów, nie przez samą obecność kotwicy. Testy wykonywalne zostaną przygotowane dla konkretnych przykładów; formalizacja Lean stanowi oddzielny etap i nie jest zastępowana tym rejestrem.

| ID | Kotwica | Kryterium | Metoda |
| --- | --- | --- | --- |
| PDE-09-001 | chap:pde-sobolev | Jawne d>=1, k>=0, 1<=p<=infty, niepusty otwarty Omega bez automatycznej spójności; rozróżnienie klas a.e., pochodnych dystrybucyjnych i reprezentantów; konwencja miary. | semantyczna |
| PDE-09-002 | def:pde9-Wkp | L^p zawiera się lokalnie w L¹ przez Höldera, osobno oba końce zakresu; tożsamość testowa dla wielowskaźnika ze znakiem (-1)^abs(alpha), jednoznaczność reprezentanta a.e., alpha=0 daje u. | semantyczna |
| PDE-09-003 | def:pde9-Wkp | Liniowość, iniektywne odwzorowanie do skończonego produktu L^p; norma dla p skończonego i maksimum dla p=infty, trójkąt, jednorodność i dodatnia określoność, W^0,p=L^p. | semantyczna |
| PDE-09-004 | def:pde9-local-zero | W^k,p_loc przez U relatywnie zwarte, ograniczenie słabych pochodnych do otwartych podzbiorów przez przedłużenie testu przez zero; norma nie rośnie, włożenie globalnej przestrzeni w lokalną. | semantyczna |
| PDE-09-005 | def:pde9-local-zero | Sklejanie lokalnych reprezentantów na przeliczalnym pokryciu, zgodność a.e. na przecięciach, skończone pokrycie zwartego podzbioru, również p=infty; tożsamość na każdym teście globalnym. | semantyczna |
| PDE-09-006 | def:pde9-local-zero | W_0^k,p jako domknięcie C_c^infty dla p<infty w tym rozdziale; brak założenia istnienia śladu i brak przenoszenia gęstości na p=infty. | semantyczna |
| PDE-09-007 | sec:pde9-def | Porównanie norm sumy, l^p i maksimum przez skończone M, poprawne stałe M^(1-1/p) i M; równość norm W^1,2 oraz Bessela H^1 przez Plancherela i transformatę pochodnej, także k=0. | semantyczna |
| PDE-09-008 | sec:pde9-def | abs(x) należy do W^1,p na (-1,1) dla całego zakresu p, H nie należy do W^1,p; druga pochodna abs(x)=2 delta_0 wyklucza W^2,p; poprawne odesłanie do dowodów rozdziału 07. | semantyczna |
| PDE-09-009 | ex:pde9-power | Funkcja odcinająca psi, wartość u w zerze jawna, próg ap<d z całki radialnej, rozbieżność logarytmiczna na granicy i brak L^infty przez zbiory dodatniej miary. | semantyczna |
| PDE-09-010 | ex:pde9-power | Jawny gradient poza zerem, norma gradientu blisko zera, równoważność całkowalności składowych i modułu, próg (a+1)p<d z całki radialnej. | semantyczna |
| PDE-09-011 | ex:pde9-power | Wystarczalność: całkowanie przez części na pierścieniu z poprawną normalną wewnętrznej sfery, granica wyrazu brzegowego przez eps^(d-1-a), zbieżność obu całek objętościowych przez lokalną całkowalność. | semantyczna |
| PDE-09-012 | ex:pde9-power | Konieczność: zgodność słabej i klasycznej pochodnej poza zerem, singleton miary zero, wszystkie składowe muszą być w L^p, co wymusza próg gradientu. | semantyczna |

| PDE-09-013 | thm:pde9-banach | Cauchy w każdej składowej L^p, granice f_alpha, oba oszacowania Höldera z testem i pochodną w L^p', również końce p=1 i p=infty; identyfikacja słabych pochodnych. | semantyczna |
| PDE-09-014 | thm:pde9-banach | Zbieżność w normie Sobolewa przez skończoną sumę lub maksimum; przypadek k=0; iloczyn skalarny H^k, całkowalność, hermitowskość, dodatnia określoność i zupełność. | semantyczna |
| PDE-09-015 | cor:pde9-closed | Naturalna dziedzina pojedynczego D_alpha, obie granice w L^p dają zamknięty wykres przez tożsamość testową; brak wymagania pozostałych pochodnych. | semantyczna |
| PDE-09-016 | sec:pde9-complete | Kontrprzykład na (0,1)^2: skok zależny tylko od y, pochodna x zerowa, pochodna y nieregularna przez testy na zwężających się pasach, wszystkie p; dla p skończonego gładka aproksymacja z błędem (2/n)^(1/p) i zerową pochodną x. | semantyczna |
| PDE-09-017 | thm:pde9-ac | Na skończonym przedziale g w L¹ dla wszystkich p; pierwotna U od a, absolutna ciągłość i pochodna g a.e.; całkowanie przez części przez iloczyn z testem, stałość u-U z rozdziału 07, jednoznaczność regularnego reprezentanta. | semantyczna |
| PDE-09-018 | thm:pde9-ac | Odwrotna implikacja z absolutnej ciągłości przez całkę z pochodnej iloczynu i zerowe wartości brzegowe testu; wzór przyrostów; jedyny ciągły reprezentant na całym domkniętym przedziale, również na końcach. | semantyczna |
| PDE-09-019 | cor:pde9-trace-oneD | Supremum ciągłego reprezentanta na [a,b] równe istotnemu supremum na (a,b); minimum modułu, Hölder i jawne stałe L^(-1/p), L^(1-1/p); liniowość i ograniczoność śladów, osobno p=infty. | semantyczna |
| PDE-09-020 | sec:pde9-oneD | Dla 1<p<infty oszacowanie przyrostu z wykładnikiem 1-1/p; dla p=infty równoważność z reprezentantem lipschitzowskim oraz dokładna stała Lipschitza; dowód przez absolutną ciągłość i ilorazy różnicowe. | semantyczna |
| PDE-09-021 | sec:pde9-oneD | Dla p=1 absolutna ciągłość całki kontroluje moduł ciągłości, ale brak wspólnego dodatniego wykładnika Höldera: dla dowolnego gamma>0 przykład x^theta z 0<theta<min(1,gamma), całkowalna pochodna i rozbieżny iloraz. | semantyczna |
| PDE-09-022 | sec:pde9-oneD | Funkcja Cantora: miara zbioru Cantora zero przez (2/3)^n, pochodna klasyczna zero poza nim, sprzeczność z reprezentacją absolutnie ciągłą i przyrostem 1; wykluczenie W^1,p dla wszystkich p przez włożenie w W^1,1. | semantyczna |

| PDE-09-023 | thm:pde9-mollify | Lokalna definicja splotu na Omega_epsilon, również Omega=R^d; bez przedłużania u przez zero; gładkość i tożsamość pochodnych przez twierdzenie 07; każda pochodna w lokalnym L^p i zbieżność na K przez przybliżoną jedynkę. | semantyczna |
| PDE-09-024 | thm:pde9-mollify | Skończona suma norm pochodnych ograniczonych do K, przypadek pustego K, zbieżność na relatywnie zwartym otwartym U; nie definiować przestrzeni Sobolewa na dowolnym zwartym K. | semantyczna |
| PDE-09-025 | lem:pde9-compact-product | Przedłużenie iloczynu psi u przez zero: test psi phi na Omega, dokładna reguła Leibniza pierwszego rzędu i indukcja do wielowskaźników, wszystkie składowe z ustalonym zwartym nośnikiem w L^p, także p=infty i k=0, bez kołowego użycia W_0. | semantyczna |
| PDE-09-026 | lem:pde9-compact-product | Splot funkcji o zwartym nośniku: wspólny zwarty nośnik wszystkich różnic pochodnych, zbieżność lokalna daje globalną dla p skończonego, nośnik wewnątrz V przy promieniu mniejszym od odległości do dopełnienia. | semantyczna |
| PDE-09-027 | sec:pde9-mollify | Kontrprzykład dla p=infty: każda ciągła pochodna v' ma odległość co najmniej 1 od sgn na (-r,r), przez granice jednostronne; lokalne włożenie W^k,infty w W^k,q dla skończonego q i zbieżność wygładzania w tych normach. | semantyczna |
| PDE-09-028 | sec:pde9-mollify | Rysunek lokalności: x w K, kula promienia epsilon zawarta w U, poprawny warunek odległości i nośnik jądra, zgodność podpisu z definicją. Kontrola wizualna przy kompilacji. | semantyczna |
| PDE-09-029 | thm:pde9-MeyersSerrin | Wyczerpanie K_j zwarte, K_j zawarte we wnętrzu K_(j+1), każdy punkt i każdy zwarty podzbiór objęty; Omega=R^d i początkowe puste zbiory. | semantyczna |
| PDE-09-030 | thm:pde9-MeyersSerrin | Jawna konstrukcja eta_j przez splot funkcji charakterystycznej zwartego otoczenia K_j; kontrola nośnika, wartości 0–1 i równość 1 w otoczeniu K_j; monotoniczność, teleskopowanie psi_j i suma 1. | semantyczna |
| PDE-09-031 | thm:pde9-MeyersSerrin | V_j=int K_(j+2) minus K_(j-2), relatywna zwartość i zawieranie supp psi_j; lokalna skończoność przez wyczerpanie, w tym małe indeksy i puste zbiory. | semantyczna |
| PDE-09-032 | thm:pde9-MeyersSerrin | Odcięte w_j, wybór promieni wygładzania i błędów delta*2^(-j) w globalnej normie, lokalnie skończona gładka suma g, bez przedwczesnego założenia g w W^k,p. | semantyczna |
| PDE-09-033 | thm:pde9-MeyersSerrin | Zupełność W^k,p, zbieżność szeregu błędów przez oszacowanie ogona, identyfikacja granicy jako g-u przez testy i lokalną skończoność oraz iniektywność dystrybucji regularnych; globalny błąd i g w W^k,p. Nie wymagać zbieżności szeregu w_j w globalnej normie. | semantyczna |
| PDE-09-034 | sec:pde9-density | Gęstość C_c^infty na całej R^d dla p skończonego: odcięcie psi_R, ogon każdej pochodnej i czynniki R^(-abs(beta)), następnie wygładzenie o zwartym nośniku, dwa niezależne błędy. | semantyczna |
| PDE-09-035 | sec:pde9-density | Rozróżnienie C^infty i C_c^infty, brak ogólnej gęstości dla p=infty przez przykład abs(x), brak narzucenia warunku zerowego brzegu przez Meyersa–Serrina. | semantyczna |
| PDE-09-036 | ex:pde9-constant | Stała 1 w W^1,p(0,1), ale nie w W_0^1,p; ciągłość śladu, jawne oszacowanie wartości w zerze i sprzeczność z zerowaniem funkcji testowych. | semantyczna |

## Iteracja 128 — 2026-11-25

Pierwsza lektura wprowadzenia i sekcji 9.1. Uszczegółowiono definicje, normy, lokalizację i sklejanie, wykorzystano sprawdzone wyniki rozdziałów 07–08. Dodano konsekwencję abs(x) nie należy do W^2,p i przypadek p=infty w istniejącym przykładzie potęgowym, bez rozbudowywania odrębnego działu. Rozpisano obie implikacje kryterium całkowalności słabego gradientu oraz normalizację normy H¹.

Źródło commit 031906d40233c0c0ed86b992c7144c651eec8d57, blob 9ec0dff354ae3ee8375c680d966f39683ae3e372. Zachowano 36 unikatowych etykiet; 28 wystąpień odsyłaczy, 10 zewnętrznych celów odnalezionych w rozdziałach 07–08 i 10. Stos środowisk poprawny; dalszy tekst identyczny z poprzednim. Rejestr 12 kryteriów, kotwice w źródle. Nie uruchamiano kompilacji, testów wykonawczych ani Lean.

Następna iteracja 129: pierwsza lektura 9.2 (zupełność i zamkniętość) oraz 9.3 (wymiar jeden), o ile zakres dowodów pozwoli na rzetelną kontrolę obu sekcji. Przed zakończeniem pierwszej lektury sprawdzić zasadność dodatkowych przykładów, w tym różnicy pomiędzy gęstością dla p skończonego i p=infty; nie dublować teorii z rozdziałów 07, 08, 10.

## Iteracja 129 — 2026-11-25

Pierwsza lektura sekcji 9.2–9.3. Rozpisano pełne dowody zupełności i aksjomatów iloczynu skalarnego, identyfikację granic słabych pochodnych we wszystkich przypadkach p, poprawiono sformułowanie zamkniętości pojedynczej pochodnej przez naturalną dziedzinę. Dodano kontrprzykład pokazujący, że kontrola jednej pochodnej nie wystarcza do przynależności do pełnej przestrzeni Sobolewa. Rozpisano obie implikacje jednowymiarowej charakterystyki przez absolutną ciągłość, jednoznaczność reprezentanta i ciągłość śladów. Dodano moduł ciągłości, przypadek Lipschitza i kontrprzykład dla wspólnego dodatniego wykładnika Höldera przy p=1. Uzasadniono nieprzynależność funkcji Cantora bez powoływania się na nieudowodnione twierdzenie o mierze singularnej.

Źródło commit 1552d31d45037df0535e81c10847783905016caa, blob 927ddb6e50308f795b1798af5e796a0ab7dd6682; 36 zachowanych etykiet, 30 wystąpień odsyłaczy, 11 zewnętrznych celów (nowy odsyłacz thm:pde7-constant sprawdzony w rozdziale 07). Poprawny stos środowisk; pozostały tekst identyczny. Dodano 10 kryteriów, łącznie 22. Nie wykonano kompilacji, testów numerycznych ani Lean.

Następna iteracja 130: pierwsza lektura sekcji 9.4–9.5, sploty i aproksymacja wewnętrzna oraz twierdzenie Meyersa–Serrina. Szczególnie sprawdzić lokalnie skończony rozkład jedynki, kontrolę błędów i odrębność p=infty.

## Iteracja 130 — 2026-11-25

Pierwsza lektura sekcji 9.4–9.5. Zastąpiono nieprecyzyjną normę W^k,p(K) na dowolnym zwartym zbiorze sumą norm ograniczeń pochodnych i wykorzystano sprawdzone twierdzenia 07 o wygładzaniu oraz przybliżonej jedynce. Dodano lemat o iloczynie z funkcją odcinającą i jego przedłużeniu przez zero z pełnym dowodem reguły Leibniza; z niego wynika globalna aproksymacja funkcji o zwartym nośniku. Rozpisano konstrukcję rozkładu jedynki z wyczerpania K_j, jawnie kontrolując lokalną skończoność rozszerzonych nośników i identyfikację granicy szeregu błędów w przestrzeni Banacha. Dodano dowód gęstości C_c^infty na całej R^d dla p skończonego oraz ilościowy kontrprzykład dla p=infty. Poprawiono istniejący rysunek lokalności splotu; nie sprawdzano jeszcze renderu.

Źródło commit 1bd6861738b6e0d711d066764500b66bf84ff86e, blob 73e0f31b6407eb2c9ee084707d8ba6a5a48c0f50. Zachowano wszystkie 36 etykiet i dodano lem:pde9-compact-product, łącznie 37 unikatowych. 42 wystąpienia odsyłaczy, 15 różnych celów zewnętrznych sprawdzonych w rozdziałach 07, 08 i 10. Stos środowisk poprawny; tekst poza 9.4–9.5 identyczny. Dodano 14 kryteriów, łącznie 36. Nie wykonywano kompilacji, testów numerycznych ani Lean.

Następna iteracja 131: pierwsza lektura sekcji 9.6–9.7, przestrzeń W_0 i przedłużenie przez zero oraz nierówność Poincarégo na kostce; wykorzystać już udowodniony lemat odcięcia.
