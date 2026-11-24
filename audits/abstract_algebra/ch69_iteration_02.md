# AA-69 — audyt II, etap P otwarty

24 listopada 2026 r. Kontynuacja audytu I na istniejącej gałęzi biblioteka-matematyczna-iteracja-6.

## Niezależna kontrola pięciu dowodów
1. Permutacja korzeni dodatnich: w układzie zredukowanym korzeń dodatni różny od α_i ma dodatnią współrzędną poza i; odbicie ją zachowuje. Zmiana znaku w słowie zachodzi tylko dla α_{i_k}, więc sprzężenie odbicia przez ogon słowa daje usunięcie jednego czynnika. Z minimalności słowa w=u s_j wynika dodatniość u α_j i ujemność w α_j. Argument nie zakłada swobodnego działania na komorach.
2. Orbity: maksymalizacja wysokości daje dominację; regularność jest zachowana przez W. Dla dwóch ściśle dominujących reprezentantów w jednej orbicie iloczyn skalarny z każdym dodatnim korzeniem wymusza, by w^-1 zachowywał dodatnie korzenie, więc w=1. Stabilizatory są sprzężone.
3. Waga rho: porównanie dwóch wzorów na s_i rho daje rho(h_i)=1, a całkowitość zapewnia przesunięcie P_+ o rho.
4. Alternanty: zmiana zmiennej w sumie jest bijekcją grupy; współczynniki na ścianach znikają nad Z (nie zakładamy tego nad ciałem charakterystyki 2). Regularna orbita ma dokładnie jeden reprezentant dominujący i każdy element pojawia się raz. Rozłączne nośniki dają niezależność.
5. Mianownik: pojedynczy czynnik zmienia znak; pozostałe są permutowane. Każda waga w nośniku jest <=rho i współczynnik rho=1. Waga ściśle dominująca z nośnika musi być rho+lambda, lambda dominująca. Ścisła dodatniość wysokości dla niezerowej lambda wynika z AA-67; dlatego lambda=0. Przykład A2: rozwinięcie i wszystkie sześć znaków zgodne.

## Korekta
W sformułowaniu lematu aa:lem:weyl-regular-orbits warunek ścisłej dominacji błędnie oznaczono przez μ(h_i)>0, choć μ jest dowolną regularną wagą wejściową. Wprowadzono nazwę ν dla jedynego reprezentanta dominującego i warunek ν(h_i)>0. Dowód już poprawnie używał ν. Commit 67a19da16eaf4f8e20c445d18a1e840459526a85; aktualny blob 73550fe9088795bb4735414200fcc0ffde4120e0. Nie rozszerzano zakresu.

## Regresje wykonane
Ponownie wykonano AA-69-DEN-01 (9 układów, 344 elementy grup, 52 korzenie dodatnie, 58 regularnych orbit, 22 singularne alternanty, 1341 kontroli odbić): PASS. Dodano AA-69-DEN-02 w tym samym skrypcie, źródła aa:lem:weyl-positive-permutation i aa:lem:weyl-regular-orbits. BFS w współrzędnych korzeni daje najkrótsze słowa; dla każdego przedłużenia przez odbicie sprawdzono zmianę długości i w przypadku skrócenia odtworzono konkretny usunięty czynnik na podstawie zmiany znaku. Sprawdzono również, że obrazy rho inne niż rho są regularne niedominujące, oraz jedyność elementu zachowującego dodatnie korzenie. Rozszerzony skrypt rzeczywiście wykonano: DEN-02 PASS (344 elementy, 1190 przedłużeń, 595 usunięć, 335 regularnych wag niedominujących, 9 trywialnych stabilizatorów). Commit 7f2f83b974febddc78e6190d44667d70176d50bf; blob bcfedaeb9c032d16659b9a28e381ad48d81baa84. Nie jest to formalizacja Lean.

## CI
Run 45483592633, job 138762944461, head 9cbed348e5744f632fc65f506c25bc511b7fe555, success 148/148, 4791 testów, globalna bramka PASS (69 rozdziałów, 586 dowodów, 309 twierdzeń, 175 lematów, 356 przykładów, 1264 etykiety, 0 nierozwiązanych odsyłaczy i duplikatów). PDF 431 stron, artefakt 14963962306. Dotyczy źródła sprzed korekty. Nowy run 45487432900 dla rozszerzonego testu queued przy sprawdzeniu; 45487391481 dla korekty in_progress. Nie przeprowadzono oględzin PDF; wymagany nowy pełny CI i kontrola wszystkich stron AA-69 po korekcie. AA-69 pozostaje w stabilizacji, AA-70 nieotwarty.
