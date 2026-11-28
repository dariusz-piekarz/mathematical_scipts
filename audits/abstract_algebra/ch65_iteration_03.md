# AA-65 — audyt III etapu D: kontrola zgodności i niezależny sprawdzian charakteru

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Aktualne źródło rozdziału 6684195ce7fe803d679ccd1628a06f7bee9dc512 bez zmian od audytu II.

Ponownie wykonano oba zapisane zestawy JS z aktualnej gałęzi. Blob a0fce07fd80a9c1a9d00510a46ccded0eb2bcc06: 32 modele, 1278 wektorów monomialnych, 4434 odbicia, 16158 relacji komutatorowych, 32 najwyższe monomy; PASS. Blob 7efca378ef42de9d915fd5936a526f50e2d27880: 9 modeli tensorowych typu A, 169 wektorów, 138 kontroli krotności po odbiciu, 676 komutatorów, 20 przestrzeni najwyższych wag o łącznym wymiarze 26; oraz 4 modele symplektyczne, 112 przestrzeni wagowych, 94 wpisy Cartana, 462 odbicia, 3912 relacji, 12 jednowymiarowych przestrzeni najwyższych wag; PASS.

Niezależnie od macierzowych implementacji wykonano pomocniczy sprawdzian kombinatoryczny charakteru kwadratu tensorowego reprezentacji naturalnej typu C_n dla n=2..5. Wagi naturalnej reprezentacji to +/- epsilon_i; zliczono wszystkie uporządkowane pary. Krotność zera wynosi 2n, krotność +/-2epsilon_i wynosi 1, krotność +/-epsilon_i +/-epsilon_j dla i!=j wynosi 2. Sprawdzono wszystkie 112 różnych wag w czterech modelach oraz wszystkie 4280 permutacji ze znakami (łącznie dla czterech rang), w sumie 209496 równości krotności. Wszystkie zaliczone. Kontrola pomocnicza nie wymaga zmiany trwałej regresji i nie jest formalizacją Lean.

Kontrola źródła: 19 wystąpień odsyłaczy, 8 różnych celów, wszystkie znalezione bezpośrednio w AA-65, AA-60 lub AA-61. Pięć środowisk proof, bilans początku i końca wszystkich środowisk poprawny. Sprawdzono zgodność pliku głównego i bramki integralności z 65 rozdziałami. Nie stwierdzono nowych usterek wymagających zmiany źródła.

CI 45425552893, job 138556424573, obejmujący rozszerzoną regresję typu C, w trakcie wykonywania. Ostatni sprawdzony stan: 7 kroków zakończonych sukcesem, 1 wykonywany, 132 oczekujące; wcześniejszy przebieg 45425125425 również w toku. Nie uznajemy CI ani PDF za zweryfikowane przed ich ukończeniem. Etap D pozostaje otwarty, etap P i AA-66 nieotwarte.
