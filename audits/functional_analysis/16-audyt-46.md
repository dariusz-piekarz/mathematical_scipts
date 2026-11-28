# Rozdział 16 — audyt 46 (bloki 3–4/5, poprawkowy, 0/2)

Data: 24 listopada 2026. Kontynuacja audytu 45, wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Matematyka
Rozpisano dowód przynależności gradientu do subróżniczki dla funkcjonału rozszerzonego (osobno skończona dziedzina efektywna i wartość +infty). W dowodzie subróżniczki normy w zerze zastąpiono dzielenie przez normę p podstawieniem v=p, poprawnym także dla p=0; rozpisano oba kierunki i pochodną normy poza zerem. Sprawdzono charakterystykę i nieekspansywność odwzorowania proksymalnego przy przyjętym założeniu ograniczoności J z dołu. W przykładzie Dirichleta uzupełniono domkniętość jądra funkcjonału całki, bijektywność izometrii pochodnej oraz zupełność; jawnie wyprowadzono pochodną Frécheta energii i oszacowanie reszty. Bez dodawania tematów.

## Regresje i technika
Źródło: e9248957fae3c700e7112e514f673d49c1833698, blob bc20f2b5223205cd917f317e5b129ccec2f82e17. Ponowny odczyt: 19 różnych etykiet, zbilansowane środowiska i obecność trzech kontrolowanych fragmentów. Testy FA16_SUBGRAD_ZERO_01 oraz FA16_DIRICHLET_REMAINDER_01 w tools/tests/test_functional_analysis_ch16.py, commit 239cd733dc529c933540b2e8ceaa9409f7a584a2. Lokalne odtworzenie części arytmetycznej nowych testów na ułamkach: 145 przypadków zaliczonych; nie jest to uruchomienie całego pliku testowego. Poprzednie CI 45372989745 zakończone sukcesem; CI 45374623989 dla poprawionego źródła w toku przy odczycie, wynik nowych testów i PDF po zmianach niepotwierdzony. Porównanie z pełnymi źródłami PDE i 15B pozostaje do potwierdzenia. Lean nie uruchamiano.

## Decyzja
4/5 bloków przejrzanych, 0/2 czystych audytów stabilizacyjnych. Następny audyt 47: blok 5, Krein–Milman, Bauer i miary probabilistyczne, odsyłacze do 09 oraz teorii miary, kontrola CI i PDF, domknięcie porównania między skryptami. Następnie dwa czyste audyty.
