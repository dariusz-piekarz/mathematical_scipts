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

| PDE-09-037 | thm:pde9-zero-extension | Przedłużenie przez zero klas L^p jest dobrze określone i izometryczne; przedłużone testy są globalnie gładkie dzięki zwartemu nośnikowi wewnątrz Omega, pochodne komutują z przedłużeniem dla testów. | semantyczna |
| PDE-09-038 | thm:pde9-zero-extension | Aproksymacja u przez testy, izometria różnic w normie Sobolewa, zupełność, identyfikacja granicy i każdej pochodnej przez jednoznaczność granic L^p; równość norm dla wszystkich k włącznie z k=0. | semantyczna |
| PDE-09-039 | thm:pde9-zero-extension | Liniowość i izometryczne zanurzenie o domkniętym obrazie, dowód przez zupełność W_0^k,p i izometrię. | semantyczna |
| PDE-09-040 | sec:pde9-zero | Przedłużenie stałej 1 z (0,1) daje dystrybucyjną pochodną delta_0-delta_1 przez tożsamość testową; lokalizacja przy zerze wyklucza reprezentację regularną. | semantyczna |
| PDE-09-041 | sec:pde9-zero | Odwrotna implikacja bez dodatkowych założeń fałszywa: Omega=(-1,0) suma (0,1), ograniczenie zeta o wartości 1 w zerze, przedłużenie równe zeta a.e.; nieprzynależność W_0 przez ciągłość jednostronnego śladu po ograniczeniu aproksymantów. | semantyczna |
| PDE-09-042 | thm:pde9-cube-Poincare | Średnia dobrze określona na kostce skończonej miary; jednowymiarowe oszacowanie odchylenia od średniej przez całkę z pochodnej, jawne czynniki L^(1/p) i L^(1-1/p). | semantyczna |
| PDE-09-043 | thm:pde9-cube-Poincare | Jawna definicja A_j, Jensen dla znormalizowanej miary i Fubini dają kontrakcyjność; nierówność jednowymiarowa na przekrojach, komutowanie z pochodną innej zmiennej, teleskopowanie. | semantyczna |
| PDE-09-044 | thm:pde9-cube-Poincare | Aproksymacja lokalna na wewnętrznej kostce Q_delta, kontrola różnicy średnich przez normę L^p, przejście do granicy w nierówności przy ustalonym delta. | semantyczna |
| PDE-09-045 | thm:pde9-cube-Poincare | Przejście delta do zera: zbieżność średnich, oszacowanie różnic norm odjętych średnich, zbieżność norm przez zmajoryzowanie i stała L. | semantyczna |
| PDE-09-046 | thm:pde9-cube-Poincare | Przypadek p=infty przez włożenie w W^1,q na zbiorze skończonej miary i dowód granicy norm L^q do istotnego supremum, także M=0; zerowy gradient równoważny stałości a.e. | semantyczna |
| PDE-09-047 | cor:pde9-Poincare-zero | Wersja zerowego warunku brzegowego dla każdego kierunku j: całka od dolnego końca, Hölder z czynnikiem L^(p-1), Fubini i dodatkowe L, p=1 oraz d=1, granica w W^1,p. | semantyczna |
| PDE-09-048 | cor:pde9-Poincare-zero | Norma gradientowa na W_0^1,p, dodatnia określoność z Poincarégo, trójkąt i jednorodność, równoważność z normą Sobolewa ze stałymi 1 i (1+L^p)^(1/p). | semantyczna |

| PDE-09-049 | thm:pde9-products | Mnożnik C¹ z ograniczoną funkcją i pochodnymi: nie podstawiać iloczynu C¹ jako testu C_c^infty; lokalne wygładzenie w W^1,1, klasyczne całkowanie przez części i globalne oszacowania L^p, także p=infty. | semantyczna |
| PDE-09-050 | thm:pde9-products | Iloczyn dla sprzężonych skończonych p,q: zbieżność trzech iloczynów lokalnie w L¹ przez rozkład różnicy i Höldera, ograniczoność norm aproksymantów; globalna całkowalność i tożsamość testowa. | semantyczna |
| PDE-09-051 | thm:pde9-products | Przypadki p=1,q=infty i odwrotny: jednostajne ograniczenie wygładzeń i ich pochodnych przez nieujemność i normalizację jądra, podciąg a.e. przez sumowalne błędy i Tonellego, majoranta 2 norm(b)_infty abs(a); brak założenia zbieżności L^infty. | semantyczna |
| PDE-09-052 | thm:pde9-products | Algebra W^1,infty: lokalne zastosowanie przypadku sprzężonego 1,infty i globalna istotna ograniczoność funkcji oraz pochodnych iloczynu. | semantyczna |
| PDE-09-053 | thm:pde9-chain | Zakres F klasy C¹ o ograniczonej pochodnej, rzeczywiste u; F(0)=0 dla skończonego p na nieskończonej mierze, wyjątki dla skończonej miary lub p=infty, jawne oszacowania norm funkcji i pochodnych. | semantyczna |
| PDE-09-054 | thm:pde9-chain | Lokalna aproksymacja w W^1,p i podciąg a.e. z sumowalnych p-tych potęg błędów, zbieżność złożenia przez Lipschitza; rozkład różnicy pochodnych i majoranta (2L)^p abs(partial_j u)^p, przejście do granicy na testach. | semantyczna |
| PDE-09-055 | thm:pde9-chain | Reguła łańcuchowa dla p=infty przez lokalny przypadek p=1 na U relatywnie zwartym i globalne ograniczenia; bez nieuprawnionej aproksymacji w normie supremum. | semantyczna |
| PDE-09-056 | lem:pde9-levelsets | Jawna konstrukcja h_n przez odcięcie, F_n(0)=0, całka zorientowana dla t<0, oszacowanie błędu min(abs(t),4/n), majoranta abs(u)^p także dla nieskończonej miary. | semantyczna |
| PDE-09-057 | lem:pde9-levelsets | Granica h_n(u) partial_j u w L^p przez zmajoryzowanie i zamkniętość pojedynczej pochodnej; gradient zerowy na każdym ustalonym zbiorze poziomicowym, p=infty przez przeliczalne pokrycie i przypadek lokalny p=1. | semantyczna |
| PDE-09-058 | cor:pde9-truncation | Jawne gładkie aproksymanty G_n=eta_n*G-(eta_n*G)(0) dla dodatniej części i T_M; G_n(0)=0, 0<=G_n'<=1, błąd <=2/n, zgodność pochodnej poza skończonym zbiorem punktów załamania. | semantyczna |
| PDE-09-059 | cor:pde9-truncation | Zbieżność złożeń i pochodnych w L^p z majorantami, zanik gradientu na przeciwobrazach punktów załamania, zamkniętość pochodnej; wzory dla dodatniej i ujemnej części, modułu i T_M, także p=infty przez lokalizację. | semantyczna |
| PDE-09-060 | cor:pde9-truncation | T_M(u) zbiega do u w W^1,p dla p skończonego: oszacowania błędów funkcji i pochodnych przez ogony, zbieżność zmajoryzowana, skończona liczba składowych. Nie twierdzić tej zbieżności dla ogólnych nieskończonych wykładników przez ten argument. | semantyczna |
| PDE-09-061 | sec:pde9-calculus | Rozróżnienie udowodnionej reguły dla C¹ oraz obcięć ze skończoną liczbą punktów załamania od ogólnej reguły dla funkcji lipschitzowskich; nie podstawiać dowolnego reprezentanta pochodnej bez uzasadnienia. | semantyczna |

| PDE-09-062 | sec:pde9-extension | Przesunięcie do wnętrza, tożsamość testowa dla każdej pochodnej, osobne przedłużenia L^p bez założenia, że są pochodnymi przedłużenia u. | semantyczna |
| PDE-09-063 | sec:pde9-extension | Splot z promieniem mniejszym od h/2; lokalna identyfikacja pochodnych i globalna zbieżność norm na półprzestrzeni, wybór ciągu diagonalnego. | semantyczna |
| PDE-09-064 | thm:pde9-reflection | Odbicie dobrze określone na klasach, jawne zniesienie składników brzegowych, znaki pochodnych, przypadek d=1 i dokładny czynnik 2^(1/p). | semantyczna |
| PDE-09-065 | thm:pde9-reflection | Przeniesienie na ogólne u przez zupełność i identyfikację granicy z jawnym odbiciem L^p, bez kołowości. | semantyczna |
| PDE-09-066 | prop:pde9-highreflection | Odwracalność układu Vandermonde'a przez liczbę pierwiastków; dopasowanie pochodnych mieszanych do rzędu k-1 i indukcja całkowania przez części. | semantyczna |
| PDE-09-067 | prop:pde9-highreflection | Czynnik j^(m-1/p) z jakobianem i regułą łańcuchową; jawna stała normy oraz identyfikacja granicy L^p. | semantyczna |
| PDE-09-068 | lem:pde9-density-halfspace-slab | Rozkład warstwy dwoma odcięciami, test uzasadniający przedłużenie przez zero z dala od płaszczyzny sklejenia, zmiana s=1-t i odbicie, bez nieudowodnionego twierdzenia ACL. | semantyczna |
| PDE-09-069 | lem:pde9-density-halfspace-slab | Ograniczoność przedłużenia warstwy, gęstość C_c^infty na R^d i kontrakcyjność restrykcji; nie utożsamiać aproksymacji z zerowym śladem. | semantyczna |

| PDE-09-070 | thm:pde9-trace-slab | Jednowymiarowe oszacowanie z podstawowego twierdzenia rachunku całkowego, Tonelli i Minkowski, stała 1 przed sumą norm, przypadek d=1. | semantyczna |
| PDE-09-071 | thm:pde9-trace-slab | Ciąg Cauchy'ego śladów, niezależność od aproksymantów, liniowość, ograniczoność, zgodność z ograniczeniem klasycznym i jednoznaczność. | semantyczna |
| PDE-09-072 | sec:pde9-traces | Ślad na t=1 przez zmianę zmiennej; zerowe ślady W_0 przez gęstość, bez nieuzasadnionej odwrotnej implikacji na dowolnym zbiorze otwartym. | semantyczna |
| PDE-09-073 | ex:pde9-dirichlet | Ciągłość obu form całkowych; warunki brzegowe przez ciągłość śladów; jawna konstrukcja F, c i u, absolutna ciągłość oraz słaba druga pochodna -f. | semantyczna |
| PDE-09-074 | ex:pde9-dirichlet | Przynależność do H_0^1 niezależnie od ogólnego twierdzenia o jądrze śladu: odcięcie, oszacowanie pochodnej odcięcia razy u, zbieżność pozostałych składników i wygładzanie z zachowaniem zwartego nośnika. | semantyczna |
| PDE-09-075 | ex:pde9-dirichlet | Przejście od testów gładkich do H_0^1 z obustronnymi oszacowaniami Cauchy'ego--Schwarza. | semantyczna |
| PDE-09-076 | ex:pde9-dirichlet | Wzór Greena przez Fubiniego i rozdzielenie całek, zerowe wartości brzegowe, skok pochodnej i poprawny znak delty Diraca; przykład f=1. | semantyczna |
| PDE-09-077 | ex:pde9-dirichlet | Jednoznaczność przez różnicę rozwiązań i nierówność Poincarégo; oszacowanie energetyczne z rozróżnieniem zerowej normy pochodnej. | semantyczna |
| PDE-09-078 | sec:pde9-scaling | Jakobian skalowania i reguła łańcuchowa; przypadki p lub q równe nieskończoności przez istotne supremum. | semantyczna |
| PDE-09-079 | sec:pde9-scaling | Konieczność równości wykładników nierówności jednorodnej przez obie granice skali, bez utożsamiania konieczności z wystarczalnością. | semantyczna |
| PDE-09-080 | sec:pde9-scaling | Kontrprzykład do ciągłego zanurzenia dla q>p*: lokalizacja w kuli, ograniczoność normy Sobolewa i rozbieżność normy L^q, także q=nieskończoność; rozróżnienie braku ciągłości od braku przynależności. | semantyczna |
| PDE-09-081 | chap:pde-sobolev | Podsumowanie respektuje zakres wykładników, odróżnia W_0 od jądra śladu na dowolnym zbiorze otwartym, nie zapowiada jako udowodnionych ogólnych twierdzeń rozdziału 10. | semantyczna |

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

## Iteracja 131 — 2026-11-25

Pierwsza lektura sekcji 9.6–9.7. Uściślono izometryczne przedłużenie przez zero oraz domkniętość obrazu. Rozpisano przykład skoku i dodano kontrprzykład do odwrotnej implikacji na dowolnym zbiorze otwartym (przedział z usuniętym punktem). Doprecyzowano tytuł sekcji, aby nie utożsamiać definicji W_0 z zerowym śladem bez hipotez geometrycznych. Rozpisano dowód Poincarégo–Wirtingera: jednowymiarowe oszacowanie, operatory uśredniania, Jensen i Fubini, dwie kolejne granice przy aproksymacji wewnętrznej. Dodano przypadek p=infty przez granicę norm L^q, bez nieuprawnionej gęstości w normie supremum. Rozszerzono wersję dla W_0 na każdy kierunek współrzędnej i wyprowadzono równoważność normy gradientowej, potrzebną w metodach wariacyjnych.

Źródło commit 175a32a726a5845fd9fad7f9afa99c228b67a45a, blob f47307fde43516e321425b41c2da4078bc46c8ed. Zachowano 37 unikatowych etykiet, 46 wystąpień odsyłaczy, 15 niezmienionych celów zewnętrznych; poprawne zagnieżdżenie środowisk, tekst poza 9.6–9.7 identyczny. Dodano 12 kryteriów, łącznie 48. Nie wykonywano kompilacji, testów numerycznych ani Lean.

Następna iteracja 132: pierwsza lektura sekcji 9.8, reguły rachunkowe, iloczyn, reguła łańcuchowa, obcinanie i zbiory poziomicowe; wykorzystać lemat odcięcia, sprawdzić hipotezy dla p=infty.

## Iteracja 132 — 2026-11-25

Pierwsza lektura sekcji 9.8. Poprawiono dowód mnożenia przez współczynnik C¹ (nie jest on automatycznie gładkim testem dystrybucyjnym) przez lokalne wygładzenia. Uzupełniono dowód iloczynu dla wykładników sprzężonych, osobno oba przypadki końcowe, oraz algebrę W^1,infty. Doprecyzowano zakres reguły łańcuchowej C¹ z ograniczoną pochodną, przypadki F(0) i p=infty. Rozpisano konstrukcję i majoranty w dowodzie lematu poziomicowego oraz wygładzenia obcięć z dokładnym warunkiem G_n(0)=0. Udowodniono wzory dla modułu, dodatniej i ujemnej części oraz gradientu T_M, a także zbieżność obcięć w W^1,p dla p skończonego. Ujednolicono termin zbieżność zmajoryzowana. Nie rozszerzano dowodu na dowolne funkcje lipschitzowskie, którego dodatkowe uzasadnienie wykracza poza podane przypadki.

Źródło commit a98262681a401f0c839a10a55482b4954dc3a1e2, blob 7f6dc5f21b28925d7abd1edb20ea849bc9c29dc6. Zachowano 37 unikatowych etykiet; 56 wystąpień odsyłaczy, 15 niezmienionych celów zewnętrznych; poprawny stos środowisk, tekst poza 9.8 identyczny. Dodano 13 kryteriów, łącznie 61. Nie wykonywano kompilacji, testów numerycznych ani Lean.

Następna iteracja 133: pierwsza lektura sekcji 9.9 — przedłużanie z półprzestrzeni, odbicie wyższych rzędów i gęstość na półprzestrzeni i warstwie; zweryfikować współczynniki dopasowania pochodnych i brak kołowego rozumowania.

## Iteracja 133 — 2026-11-25

Pierwsza lektura sekcji 9.9. Rozpisano globalną aproksymację przez przesunięcie i splot niezależnie od przedłużania Sobolewa; całkowanie przez części w odbiciu pierwszego i wyższych rzędów, układ Vandermonde'a i oszacowanie norm. Zastąpiono nieuzasadnione odwołanie do absolutnej ciągłości na przekrojach warstwy konstrukcją z dwoma odcięciami i odbiciem. Źródło: commit 310737224e0de4f03f73481070ab1be91a6d3e98, blob 821e494780fd7f3de0f9fba86fbb1751aca53c4e. Zachowano wszystkie 37 etykiet; 58 wystąpień odsyłaczy, poprawny stos środowisk, tekst poza 9.9 identyczny. Dodano 8 kryteriów semantycznych (łącznie 69). Nie wykonywano kompilacji, testów wykonawczych ani Lean. Następna iteracja 134: pierwsza lektura sekcji 9.10–9.12 i podsumowania, ślad na warstwie, rozwiązanie Poissona oraz skalowanie.

## Iteracja 134 — 2026-11-25

Zakończono pierwszą lekturę sekcji 9.10–9.12 i podsumowania. Doprecyzowano oszacowanie śladu na warstwie, konstrukcję operatora przez domknięcie oraz zakres zerowych śladów. Rozpisano istnienie słabego rozwiązania Poissona na przedziale, w tym dowód przynależności do H_0^1 bez odwołania do późniejszego twierdzenia o jądrze śladu, wzór Greena, jednoznaczność i oszacowanie energetyczne. Wyprowadzono prawa skalowania, warunek konieczny wykładnika krytycznego i lokalny kontrprzykład do ciągłego zanurzenia powyżej p*. Źródło: commit 2dc4348ee1fba8d4316c687fd6ece18245304dea, blob 948b996ec7b3b5932ce01cdc7a66e7c0811383f1. Zachowano 37 etykiet; 63 wystąpienia odsyłaczy; poprawny stos środowisk; tekst przed 9.10 identyczny. Dodano 12 kryteriów semantycznych, łącznie 81. Nie wykonywano kompilacji, testów wykonawczych ani Lean. Pierwsza lektura zakończona; następna iteracja 135: druga lektura stabilizacyjna od początku rozdziału, kryteria PDE-09-001 i kolejne, bez rozszerzania zakresu tematycznego. Przed stabilizacją konieczna kontrola techniczna, rzeczywiste testy i niezależna lektura kontrolna.

## Iteracja 135 — 2026-11-25 — druga lektura, 001–022

| Kryterium | Wynik ponownej lektury |
| --- | --- |
| 001 | Uściślenie: przykład jednowymiarowy, dokładna funkcja Heaviside'a zamiast dowolnej funkcji skokowej, odsyłacz do dowodu w 07. |
| 002 | Bez zmian: lokalna całkowalność wraz z obydwoma końcami zakresu, znak i jednoznaczność dystrybucji regularnej. |
| 003 | Uściślenie: jawna równość norm dla k=0; pozostałe aksjomaty poprawne. |
| 004 | Bez zmian: przedłużenie testu przez zero, lokalność i kontrakcyjność restrykcji. |
| 005 | Uściślenie: przeliczalna baza kul, rozłączny mierzalny rozkład, konstrukcja reprezentanta i kontrola przeliczalnej sumy zbiorów wyjątkowych; identyfikacja na U zawierającym nośnik testu. |
| 006 | Bez zmian: domknięcie w normie, zakres p skończonego i brak twierdzenia o śladzie. |
| 007 | Uściślenie: dowód nierówności skończonej sumy znormalizowanych składowych; sprawdzono zgodność norm Bessela z thm:pde8-Hs, współczynnik Plancherela i k=0,1. |
| 008 | Bez zmian: przykłady abs(x), Heaviside'a i druga pochodna z czynnikiem 2, odsyłacze do 07. |
| 009 | Uściślenie: jawna wartość obciętej całki radialnej i oba rodzaje rozbieżności. |
| 010 | Uściślenie: bezpośrednie zastosowanie poprzedniego rachunku do a+1, poprawny gradient i warunek wszystkich składowych. |
| 011 | Uściślenie: jawne majoranty całek objętościowych; poprawny znak normalnej i wykładnik d-1-a dodatni. |
| 012 | Bez zmian: jednoznaczność pochodnych na zbiorze z usuniętym zerem i pomijalność singletonu. |
| 013 | Bez zmian: granice w L^p każdej składowej i Hölder także dla p=1,infty. |
| 014 | Bez zmian: skończona suma lub maksimum, zupełność i iloczyn skalarny o właściwej konwencji. |
| 015 | Bez zmian: zamkniętość wykresu na naturalnej dziedzinie, bez kontroli innych pochodnych. |
| 016 | Bez zmian: obliczenie działania pochodnej y, testy na zwężających się pasach, błąd gładkiego przybliżenia. |
| 017 | Uściślenie: pierwotna U jest ograniczona na domkniętym przedziale, zatem u-U należy do L^p; poprawne użycie stałości dystrybucji. |
| 018 | Bez zmian: obie implikacje przez absolutną ciągłość, iloczyn z testem, jednoznaczność także w punktach końcowych. |
| 019 | Bez zmian: minimum modułu, stałe zależne od długości przedziału i równość supremum z istotnym supremum. |
| 020 | Uściślenie: rozróżnienie x=y i x>y; argument Lipschitza poprawny w obie strony. |
| 021 | Bez zmian: absolutna ciągłość całki i przykład potęgowy dla dowolnego gamma>0. |
| 022 | Bez zmian: zbiór Cantora miary zero, klasyczna pochodna zero a.e. i sprzeczność z wzorem przyrostów. |

Bilans: 22/22 kryteriów poddano lekturze matematycznej, 13 bez zmian, 9 po uściśleniach; nie rozszerzano zakresu tematycznego. Źródło: commit 05846b39f611ecb181da8e4916e7be8b8a4273e6, blob ad55ea61d6296e2bfaaf2d66a1e2d7ee7360b006. Zachowano 37 etykiet, 64 wystąpienia odsyłaczy; poprawne zagnieżdżenie środowisk, tekst od sekcji 9.4 identyczny. Nie wykonywano kompilacji, testów numerycznych ani Lean. Nie jest to jeszcze stabilizacja rozdziału.

Następna iteracja 136: druga lektura 023–036 (wygładzanie lokalne, odcięcia, Meyers–Serrin, gęstość), bez rozszerzania materiału.

## Iteracja 136 — 2026-11-25 — druga lektura, 023–036

| Kryterium | Wynik ponownej lektury |
| --- | --- |
| 023 | Bez zmian: splot lokalny, pochodne dystrybucyjne, osobne zastosowanie przybliżonej jedynki do każdej składowej. |
| 024 | Bez zmian: normy ograniczeń do K, przypadek pusty i przejście do otwartego U. |
| 025 | Uściślenie: pełny krok indukcji wielowskaźnikowej z przesunięciem indeksu i konwencją zerowych współczynników dwumianowych; brak zależności od twierdzenia o W_0. |
| 026 | Bez zmian: wspólny zwarty nośnik, globalizacja zbieżności dla p skończonego, kontrola odległości od dopełnienia V. |
| 027 | Bez zmian: jednostronne granice i dolna granica 1; lokalna zbieżność w skończonych normach. |
| 028 | Kontrola źródła TikZ: środek w K, kula zawarta w U, podpis zgodny z warunkiem odległości. Kontrola renderu nadal wymagana. |
| 029 | Bez zmian: zwarte wyczerpanie, ścisłe zawieranie we wnętrzach i przypadek całej przestrzeni. |
| 030 | Uściślenie: zmiana zmiennej w splocie odcięcia, obie nierówności promieniowe, jawne uzasadnienie wartości 1 i nośnika; monotoniczność i teleskopowanie poprawne. |
| 031 | Uściślenie: zawieranie K_N w K_(j-2) i jawny wybór zwartego otoczenia każdego punktu w dowodzie lokalnej skończoności. |
| 032 | Bez zmian: wybór promieni z niezależnymi błędami, lokalna skończoność, bez założenia globalnej normy g. |
| 033 | Bez zmian: szereg błędów w przestrzeni Banacha, identyfikacja dystrybucyjna, wybór delta i brak założenia globalnej zbieżności szeregu w_j. |
| 034 | Uściślenie: jawna zbieżność ogonów L^p przez twierdzenie o zbieżności zmajoryzowanej, z całkowalną majorantą. |
| 035 | Bez zmian: różnica C_c^infty i C^infty, kontrprzykład dla p=infty, brak warunku zerowego brzegu w twierdzeniu Meyersa–Serrina. |
| 036 | Bez zmian: stała 1 i oszacowanie ciągłego śladu na końcu przedziału. |

Bilans: 14/14 kryteriów poddano ponownej lekturze źródła, 4 uściślono, 9 bez zmian, 1 kontrola źródła rysunku bez renderu. Źródło: commit 46b005597a6648b8f993f6c2a643333980b467cf, blob 3ce2b2528ea7865cc71231028088bc18f9f32545. Kontrola tekstowa w iteracji: 37 etykiet i 64 wystąpienia odsyłaczy zachowane w tej samej kolejności, stos środowisk poprawny. Nie wykonano kompilacji, testów wykonawczych ani Lean. Nie jest to jeszcze stabilizacja rozdziału.

Następna iteracja 137: druga lektura kolejnych kryteriów od PDE-09-037, zaczynając od przestrzeni W_0 i przedłużenia przez zero; bez rozszerzania zakresu.

## Iteracja 137 — 2026-11-25 — druga lektura, 037–048

| Kryterium | Wynik ponownej lektury |
| --- | --- |
| 037 | Uściślenie: niezależność przedłużenia od reprezentanta przez zbiór miary zero i liniowość punktowa; poprawne przedłużenie gładkich testów. |
| 038 | Uściślenie: pełny rachunek p-tych potęg norm wszystkich słabych pochodnych, także k=0; identyfikacja granic L^p poprawna. |
| 039 | Uściślenie: jawna iniektywność z izometrii; dowód domkniętości obrazu przez zupełność bez zmian. |
| 040 | Bez zmian: znak delta_0-delta_1, lokalizacja testów i odwołanie do nieregularności delty. |
| 041 | Bez zmian: usunięty singleton nie zmienia klasy przedłużenia, restrykcja aproksymantów i sprzeczność z jednostronnym śladem. |
| 042 | Uściślenie: czynnik L^(1-1/p) oraz osobne uzasadnienie p=1. |
| 043 | Uściślenie: różniczkowanie pod całką przez ilorazy różnicowe z całkowalną stałą majorantą; j=1 osobno. Jensen, Fubini i teleskopowanie poprawne. |
| 044 | Uściślenie: jawne oszacowanie różnicy funkcji z odjętymi średnimi przez dwukrotność błędu L^p. |
| 045 | Bez zmian: granica średnich, norm i długości boku przez zmajoryzowanie, stała L zachowana. |
| 046 | Bez zmian: przypadek p=infty przez skończone q, oba ograniczenia normy, M=0, równoważność stałości i zerowania pochodnych. |
| 047 | Bez zmian: całka od końca przedziału, czynnik L^(p-1), Fubini, p=1 i d=1, granica aproksymantów. |
| 048 | Bez zmian: dodatnia określoność, aksjomaty normy produktu i obie stałe równoważności. |

Bilans: 12/12 kryteriów poddano ponownej lekturze, 6 kryteriów uściślono w 5 zmianach tekstu, 6 bez zmian. Źródło: commit 8050925e8b328734f7efc410f95d1ba0feeea301, blob 0b1100f9c1a7cf889f3dc132111fb8c76dff9fd1. Zachowano 37 etykiet i 64 wystąpienia odsyłaczy w tej samej kolejności, stos środowisk poprawny; tekst poza sekcjami 9.6–9.7 niezmieniony. Nie wykonywano kompilacji, testów wykonawczych ani Lean. Druga lektura obejmuje dotąd 48 z 81 kryteriów; nie jest to jeszcze stabilizacja rozdziału.

Następna iteracja 138: druga lektura kryteriów od PDE-09-049 (reguły rachunkowe, iloczyny i złożenia), bez rozszerzania zakresu.
