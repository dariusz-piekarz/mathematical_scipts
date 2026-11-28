# AA-52 — audyt IV: niezależna kontrola półniezmienników

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Rzeczywista kontrola lokalna
Uruchomiono Python/SymPy z dokładnymi elementami ciał QQ(sqrt(2)) i QQ(sqrt(5)). Domknięto zbiory generatorów kwaternionowych h,i,j; h,r; h,i,u według AA-52, mnożąc w kolejce przez generatory aż do stabilizacji. Potwierdzono liczności 24,48,120 oraz normę kwadratową 1 każdego elementu. Podgrupy komutatorowe wyznaczono jako normalne domknięcia komutatorów generatorów: najpierw domknięcie grupowe ich zbioru, następnie iteracja domknięcia po dołączeniu sprzężeń przez wszystkie generatory. Jest to podgrupa normalna, gdyż skończoność zamienia zawieranie obrazu przez sprzężenie w równość; iloraz jest abelowy, ponieważ obrazy generatorów komutują. Wszystkie elementy podgrup należały do odpowiednich grup. Otrzymano rzędy podgrup komutatorowych 8,24,120 i rzędy abelianizacji 3,2,1.

Dla każdego H równego grupie G lub jej podgrupie komutatorowej D zliczono dokładne ślady t=2a kwaternionów (a,b,c,d). Użyto rekurencji s_0=1, s_1=t, s_d=t*s_(d-1)-s_(d-2), wynikającej z wartości własnych lambda,lambda^(-1). Wymiar przestrzeni wektorów ustalanych przez H w d-tej potędze symetrycznej obliczono jako sumę s_d po H podzieloną przez |H|. Arytmetyka uśredniania była dokładna, bez konwersji na int: dla każdej wartości sprawdzono is_Integer i nieujemność. Reprezentacja sprzężona ma ten sam ślad, gdyż det=1. Przestrzeń ustalana przez D rozkłada się na reprezentacje jednowymiarowe G/D (skończona grupa abelowa nad C); zatem jej niezerowość odpowiada istnieniu półniezmiennika. Wyniki dla d=0,...,12:

- 2T: D-fixed [1,0,0,0,2,0,1,0,3,0,2,0,4]; G-fixed [1,0,0,0,0,0,1,0,1,0,0,0,2].
- 2O: D-fixed [1,0,0,0,0,0,1,0,1,0,0,0,2]; G-fixed [1,0,0,0,0,0,0,0,1,0,0,0,1].
- 2I: D-fixed = G-fixed [1,0,0,0,0,0,0,0,0,0,0,0,1].

Minimalne dodatnie stopnie półniezmienników: 4,6,12; niezmienników: 6,8,12. Wszystkie asercje przeszły; proces zakończył się kodem 0. To niezależna dokładna diagnostyka konkretnych modeli, a nie zastępstwo dowodu w rozdziale ani nowa trwała regresja CI. Nie zmieniono źródła matematycznego ani workflow.

## CI i stan
Aktualny blob AA-52: a151f25b5b4e083cf39621c34fb0bca6af3948fc, commit źródłowy 52acf372ac64229c8f13fc20b6f62c88377c5b95. Run 45304703515, job 138145565432, przy ostatnim odczycie in_progress: 7 kroków success, 1 in_progress, 105 pending. Lista artefaktów pusta. Terminologia run 45304703285: success. Starszy run 45304522955 dotyczy źródła sprzed audytu III i nie zastępuje bieżącego CI.
AA-52 W AUDYCIE: oczekuje na pełny aktualny CI i wizualną kontrolę wszystkich stron PDF. AA-53 nieotwarty.
