# AA-52 — audyt V: niezależna kontrola charakterów obrotów

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Weryfikacja matematyczna
Sprawdzono dowód identyfikacji obrazów rzutowych przez charaktery. Przy zmianie znaku kwaternionu q=(a,b,c,d) ślad reprezentacji naturalnej t=2a zmienia znak, a ślad obrotu trójwymiarowego t²-1 pozostaje bez zmian. Wynika to też ze wzoru macierzy obrotu: ślad wynosi 3-4(b²+c²+d²)=4a²-1. W A5 dwie klasy cykli długości pięć dają dwa różne ślady, zamieniane przez automorfizm z nieparzystej permutacji. Argument o równoważności zespolonej i rzeczywistej jest poprawny. W dowodzie minimalnego stopnia półniezmiennika sprawdzono również przypadek F(x,y)=c y^d, dla którego dehomogenizacja jest stała, a czynniki y odpowiadają punktowi w nieskończoności.

## Niezależne obliczenia
Uruchomiono skrypt Python/SymPy 1.14.0 w kontenerze. Domknięto generatory kwaternionowe z AA-52 w ciałach QQ(sqrt(2)) i QQ(sqrt(5)) przez BFS po prawostronnych iloczynach. Sprawdzono normę 1 każdego elementu, obecność -1 i zamknięcie na zmianę znaku. Iloraz skonstruowano jako zbiór frozenset({q,-q}). Histogram śladów 4a²-1 dla klas ilorazu:
- 2T: 24 elementy, iloraz 12; ślad 3:1, -1:3, 0:8.
- 2O: 48 elementów, iloraz 24; ślad 3:1, -1:9, 0:8, 1:6.
- 2I: 120 elementów, iloraz 60; ślad 3:1, -1:15, 0:20, (1+sqrt(5))/2:12, (1-sqrt(5))/2:12.
We wszystkich trzech przypadkach średnia charakteru = 0, norma kwadratowa charakteru = 1 (dokładna arytmetyka). Potwierdza to nieprzywiedlność trójwymiarowej zespolonej reprezentacji obrotów w konkretnych modelach, dla A5 także poprawność dwóch wartości śladów.
Ponownie obliczono wymiary przestrzeni niezmienników potęg symetrycznych dla d=0..12, zliczając ślady 2a wszystkich kwaternionów i sprawdzając całkowitość oraz nieujemność średnich. 2T [1,0,0,0,0,0,1,0,1,0,0,0,2], 2O [1,0,0,0,0,0,0,0,1,0,0,0,1], 2I [1,0,0,0,0,0,0,0,0,0,0,0,1]. Asercje minimalnych dodatnich stopni 6,8,12 przeszły 3/3. Proces zakończony kodem 0. To sprawdzian modeli, nie zastępstwo dowodu ogólnego ani CI.
Reprodukcja: K=QQ.algebraic_field(radical); konwersja wpisów przez K.from_sympy; BFS od (1,0,0,0) z mnożeniem Hamiltona; Q={frozenset((q,tuple(-x for x in q))) for q in G}; Counter((2*next(iter(q))[0])**2-K.one for q in Q); sprawdzić sum(t*n)=0 oraz sum(t*t*n)=len(Q). Dla potęg symetrycznych uśrednić rekurencję s0=1,s1=t,sd=t*s_(d-1)-s_(d-2) po histogramie t=2a w G.

## CI
Aktualny blob rozdziału a151f25b5b4e083cf39621c34fb0bca6af3948fc zgodny z commitem 52acf372ac64229c8f13fc20b6f62c88377c5b95. Run 45304703515, job 138145565432: przy ostatnim odczycie 50 kroków success, jeden in_progress i 62 pending; krok testów repozytorium success, brak artefaktu. Nie przeprowadzono jeszcze oględzin aktualnego PDF. Nie zmieniono źródła ani konfiguracji workflow. Pierwszy zapis raportu odrzucono z powodu konfliktu 409; ponowiono po potwierdzeniu braku pliku.

## Werdykt
AA-52 W AUDYCIE do potwierdzenia końcowego CI oraz oględzin PDF. AA-53 nieotwarty.
