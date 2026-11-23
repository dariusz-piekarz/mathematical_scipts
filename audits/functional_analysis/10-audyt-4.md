# Analiza funkcjonalna — rozdział 10 — audyt 04 (drugi niezależny przegląd stabilizacyjny)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (istniejąca, bez tworzenia nowych).  
**Źródło:** `chapters/pl/functional_analysis/10-przestrzenie-beczkowe-i-bornologiczne-twierdzenie-banacha-steinhausa.tex`.  
**SHA blob źródła:** `2ea6b36366c8ec4dc1d2ecf8192fae1054c841b0` — **identyczny z audytem 10/03**, a zarazem z poprawioną wersją po audycie 10/02.  
**SHA zestawu testów:** `8bf224b484b3058694b8bc82109cbc8d78e9ee42` (13 testów).  
**Werdykt merytoryczny:** **CZYSTY — drugi kolejny audyt, 2/2**. Brak nowego błędu wymagającego zmian źródła, testów lub workflow. Zamknięcie techniczne rozdziału 10 jest uzależnione od ukończonego zielonego CI po zapisaniu niniejszego raportu.

## Niezależna procedura i jej zakres

Przed przygotowaniem raportu bezpośrednio pobrano z GitHub bieżącą gałąź, istniejące raporty 10/01–10/03, źródło rozdziału 10, plik testów i workflow. Potwierdzono, że 10/04 jeszcze nie istniał, oraz że ostatni [przebieg GitHub Actions #45222452537](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45222452537), uruchomiony po 10/03, miał **completed/success**: 13 testów, przygotowanie kontekstu, kompilacja LaTeX, kontrola PDF i odsyłaczy oraz publikacja artefaktu bez błędów. Nie jest to weryfikacja matematyczna; tę przeprowadzono niezależnie niżej.

Ponownie odczytano rozdziały 01–10 i sprawdzono ich zależności. Przeanalizowano założenia, kwantyfikatory, przypadki brzegowe oraz wnioski wszystkich **17 środowisk dowodowych**, **4 przykładów** i uwag merytorycznych. Szczególną uwagę poświęcono pominiętym w wersji historycznej hipotezom, różnicy pomiędzy ciągami i sieciami oraz kontrprzykładom na `c_{00}`.

## Kontrola wszystkich 17 dowodów

1. **Polar a ograniczoność punktowa:** `H^\circ` jest domknięty i absolutnie wypukły jako przecięcie odpowiednich domkniętych zbiorów. Punktowe ograniczenie `M_x` daje `x\in t H^\circ`, a pochłanianie przez `H^\circ` daje odwrotną nierówność; przypadek pustego `H` jest omówiony.
2. **Równoważne kryteria beczkowości:** topologia słaba `\sigma(E',E)` ma ograniczone rodziny dokładnie wtedy, gdy są punktowo ograniczone. Beczkowość daje otoczenie `H^\circ`, a odwrotnie bipolarność domkniętej absolutnie wypukłej beczki `B=B^{\circ\circ}` pozwala z `B^\circ\subset U^\circ` otrzymać `U\subset B`.
3. **Twierdzenie Baire'a dla zupełnych przestrzeni metrycznych:** ciąg zagnieżdżonych kul domkniętych o promieniach mniejszych niż `2^{-n}`, umieszczonych w kolejnych otwartych zbiorach gęstych, ma środki tworzące ciąg Cauchy'ego; granica należy do pierwotnego niepustego otwartego zbioru i do wszystkich `G_n`.
4. **Przestrzeń Baire'a jest beczkowa:** absorpcja i zrównoważenie implikują `E=\bigcup_{n\ge1}nB`, a domkniętość `nB` pozwala użyć własności Baire'a. Symetria i wypukłość beczki przesuwają niepuste wnętrze do otoczenia zera.
5. **Fréchet i Banach są beczkowe:** obie klasy są zupełnymi metryzowalnymi lokalnie wypukłymi TVS; wniosek odsyła do poprzednich dwóch twierdzeń. Nie ma założenia normowalności ogólnej przestrzeni Frécheta.
6. **Banach–Steinhaus dla przestrzeni beczkowych:** dla otoczenia `V\subseteq F` wybiera się domknięte absolutnie wypukłe otoczenie `W\subseteq V`; zbiór `\bigcap_{T\in\mathcal T}T^{-1}(W)` jest beczką z założenia punktowej ograniczoności. Beczkowość `E` daje równociągłość niezależnie od zupełności `F`.
7. **Klasyczne jednostajne ograniczenie norm:** w unormowanej przestrzeni wartości otoczenie kuli promienia 1 i wspólne małe otoczenie normowe dziedziny pozwalają uzyskać jednolite `\|T\|\le C`. Źródło poprawnie wymaga zupełności dziedziny, nie przestrzeni wartości.
8. **Drugi dowód z Baire'a:** `A_n=\{x:\sup_{T\in\mathcal T}\|Tx\|\le n\}` są domknięte i pokrywają Banacha; przesunięta kula zawarta w `A_N` daje jednolite `\|Th\|\le2N`, więc `\|T\|\le4N/r`.
9. **Punktowa granica sieci operatorów:** wymaga się punktowej ograniczoności wszystkich operatorów. Banach–Steinhaus daje równociągłość, a przejście do granicy w domkniętym `W\subseteq V` daje ciągłość operatora granicznego.
10. **Punktowa granica ciągu operatorów:** zbieżny ciąg w TVS jest ograniczony jako zbiór wartości. Zatem poprzedni wynik stosuje się bez dodatkowego założenia, w odróżnieniu od sytuacji z ogólną siecią.
11. **Jednostajna zbieżność na zbiorach zwartych:** równociągłość `\mathcal T`, ciągłość `T`, skończone pokrycie `K` translacjami wspólnego `U` i jedno ograniczenie indeksu dla skończenie wielu środków prowadzą do trójskładnikowego oszacowania w `W+W+W\subseteq V`.
12. **Topologie operatorowe `\tau_s` i `\tau_b`:** mocniejsza topologia `\tau_b` zachowuje implikację ograniczoności ku `\tau_s`; w drugą stronę Banach–Steinhaus daje równociągłość, zaś ograniczenie `B\subseteq tU` daje jednostajną ograniczoność obrazów na każdym ograniczonym `B`.
13. **Funkcjonał Minkowskiego:** absolutna wypukłość i pochłanianie zapewniają skończoną seminormę. `C` pochłania zbiory ograniczone wtedy i tylko wtedy, gdy `p_C` jest na nich ograniczona. Kierunek trudniejszy korzysta z `p_C(x)<t`, wybrania `s_x<t` i zrównoważenia `C`; domkniętość `C` nie jest wymagana.
14. **Kryteria bornologiczności:** (i)⇒(ii) przez poziomicę `\{p\le1}`; (ii)⇒(iii) przez ciągłość wszystkich `q\circ T`; (iii)⇒(i) przez odwzorowanie identycznościowe do przestrzeni z topologią generowaną pierwotnymi seminormami i dodatkową `p_C`. Rodzina seminorm nadal definiuje TVS Hausdorffa, a zachowanie ograniczoności zapewnia zastosowanie (iii).
15. **Unormowane przestrzenie są bornologiczne:** zbiór pochłaniający wszystkie ograniczone musi pochłaniać kulę jednostkową, więc zawiera pewną otwartą kulę normową; argument działa również w przestrzeni niezupełnej.
16. **Beczkowe przestrzenie są Mackeya:** `\rho\subseteq\tau(E,E')` wynika z prawidłowego `\ref{thm:mackey-arens}`. Każde absolutnie wypukłe słabo-* zwarte `K\subseteq E'` jest punktowo ograniczone, a więc równociągłe w beczkowym `E`; wszystkie seminormy `p_K` są `\rho`-ciągłe i dają inkluzję przeciwną.
17. **Topologia Mackeya przestrzeni Banacha:** korzysta bez dodatkowych niejawnych założeń z beczkowości Banacha i poprzedniego wyniku.

**Werdykt dowodowy: 17/17 poprawnych przy podanych założeniach; brak nowej poprawki.**

## Cztery przykłady oraz rozróżnienie sieci i ciągów

- **`c_{00}` niebeczkowa:** funkcjonały `f_n(x)=nx_n` są punktowo ograniczone dzięki skończonym nośnikom, ale mają `\|f_n\|=n`. Beczka `\{x:n|x_n|\le1\}` nie zawiera otoczenia zera: `n^{-1/2}e_n\to0` w normie supremum, lecz dla `n>1` te punkty nie leżą w beczce.
- **Słaba topologia nieskończenie wymiarowej przestrzeni Banacha:** kula normowa jest słabo domkniętą beczką, lecz nie słabym otoczeniem; skończona liczba ciągłych funkcjonałów ma wspólne niezerowe jądro, więc każde bazowe słabe otoczenie zera zawiera nieograniczoną prostą. Argument pozostaje rozpisany po korekcie z 10/02.
- **Bornologiczna, ale niebeczkowa:** przestrzeń `c_{00}` z normą supremum jest bornologiczna jako przestrzeń unormowana, choć niebeczkowa. Przykład odróżnia oba pojęcia.
- **Przybliżanie funkcjonału Diraca:** dla `C^\infty([0,1])`, `T_n(\varphi)=n\int_{[0,1/n]}\varphi\,\mathrm d\lambda`, mamy `|T_n(\varphi)|\le p_0(\varphi)` oraz `T_n(\varphi)\to\varphi(0)`. Punktowa zbieżność z równociągłością daje jednostajną zbieżność na zwartych podzbiorach dziedziny.

**Dodatkowo:** w uwadze o sieciach rodzina `a_F=|F|` dla `1\notin F` i `a_F=0` dla `1\in F` jest jako sieć zbieżna do 0, ale jej zbiór wartości jest nieograniczony. To poprawnie uzasadnia jawny warunek ograniczoności punktowej w twierdzeniu o granicy punktowej sieci. Dla zbieżnego ciągu zbiór jego wartości jest natomiast ograniczony.

**Werdykt przykładów: 4/4 poprawne.** Nie ma nowego, nieuzasadnionego uogólnienia.

## Struktura, odsyłacze i redakcja — kontrola z bieżących plików

Ponownie pobrano wszystkie rozdziały **01–10** i policzono **182 etykiety bez duplikatów**. Sam rozdział 10 zawiera **23 etykiety** i **14 odsyłaczy do istniejących celów**. Parowanie środowisk w pliku 10: **17 proof**, **5 definicja**, **9 twierdzenie**, **4 wniosek**, **2 lemat**, **1 stwierdzenie**, **4 przyklad**, **5 uwaga**, **2 enumerate**; brak środowiska TikZ w rozdziale 10. Usunięto zidentyfikowany wcześniej dublet nazwy Mackeya–Arensa, poprawny `\ref{thm:mackey-arens}` pozostaje. Nie ma niedozwolonych oznaczeń funkcji charakterystycznej `\mathbf 1`, `\mathbb 1`, niewłaściwych terminów „zwartość sekwencyjna” ani „zwartościowanie”.

Dedykowany plik regresyjny `tools/tests/test_functional_analysis_ch10.py` zawiera **13 testów**. Ostatni przebieg **#45222452537** (na tej samej wersji źródła i testów) przeszedł je wszystkie, a także pełną kompilację LaTeX kontekstu 01–10 i automatyczną kontrolę PDF. Poprzedni audyt 10/02 zawiera dodatkową realną inspekcję wizualną stron 55–61 PDF. Nie deklaruje się nowej wizualizacji w tej iteracji. Automatyczne narzędzia nie są formalnym poświadczeniem matematycznej treści dowodów.

## Decyzja przed ostatnią bramką CI

**Merytorycznie rozdział 10 spełnia warunek stabilizacji 2/2:** niezależne audyty **10/03 i 10/04** są czyste, wykonane na **identycznym blobie `2ea6b36366c8ec4dc1d2ecf8192fae1054c841b0`**, bez zmian źródła lub testów. **Techniczne zamknięcie 10 wymaga jeszcze potwierdzenia zielonego CI uruchomionego przez raport 10/04.** Po jego sukcesie rozdział 11 może być przedmiotem następnej iteracji, ale nie wcześniej.
