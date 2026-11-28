# PDE-06 — iteracja 82: domknięcie drugiej lektury 6.7–6.9

Data: 2026-11-25. Odczytane źródło 4adf037b29fc0e09a95fb435557bde958b761d09; rejestr 6293e2798c2b66b9a7fd126670bea0988b76ba00. Druga lektura bez rozszerzenia materiału.

| ID | Wynik | Uzasadnienie |
|---|---|---|
| PDE-06-034 | PASS | Dla nietrywialnego iloczynu można wybrać niezerowe wartości każdego czynnika, otrzymując dwa równania Dirichleta bez dzielenia w zerach. Suma dodatnich wartości jednowymiarowych daje lambda_mn, a bezpośrednie różniczkowanie sprawdza odwrotną implikację. |
| PDE-06-035 | PASS | Iloczyn unormowanych funkcji ma czynnik 2/sqrt(L_1 L_2); Fubini daje ortonormalność. Mierzalność współczynników przekrojów wynika z całkowalności iloczynu f i funkcji bazowej w pierwszej zmiennej na prostokącie. Oszacowanie Cauchy–Schwarza daje ich przynależność do L². Przeliczalność indeksów pozwala wybrać wspólny zbiór pełnej miary i zastosować obie bazy jednowymiarowe. |
| PDE-06-036 | PASS | Dwa całkowania przez części w każdej zmiennej eliminują wyrazy brzegowe, ponieważ obie funkcje znikają na bokach. Niezerowy współczynnik wymusza lambda=lambda_mn, a skończone ograniczenia na indeksy dają skończoną przestrzeń własną, rozpiętą dokładnie przez pasujące mody. Równość L² przechodzi na punktową przez ciągłość. |
| PDE-06-037 | PASS | Dla kwadratu jedyne dodatnie pary dające sumę kwadratów 5 to (1,2),(2,1). Przy niewymiernym stosunku kwadratów boków niezerowa całkowita różnica kwadratów w drugiej zmiennej wymuszałaby wymierność; zatem oba indeksy są identyczne. |
| PDE-06-038 | PASS | Parseval daje ograniczoność P_T z poprawnym czynnikiem e^(-kappa lambda_1 T); wszystkie mnożniki są niezerowe, więc P_T jest iniektywny. |
| PDE-06-039 | PASS | Współczynniki g_n muszą wynosić e^(kappa lambda_n T)h_n. Kwadratowa sumowalność jest konieczna przez Parsevala i wystarczająca przez zupełność przestrzeni Hilberta; działanie P_T na skonstruowany szereg odtwarza h. |
| PDE-06-040 | PASS | Każda skończona kombinacja należy do obrazu. Dane h_* mają sumowalne kwadraty współczynników gaussowskich, ale po odwróceniu każdy współczynnik ma wartość 1, więc nie należą do obrazu. Gęsty właściwy obraz nie jest domknięty. |
| PDE-06-041 | PASS | Ciąg osiągalnych danych P_T e_n dąży do zera, lecz normy odwrotnych obrazów wynoszą 1; liniowość daje nieciągłość wszędzie w dziedzinie odwrotności. |
| PDE-06-042 | PASS po korekcie | Podsumowanie rozróżnia rodzaje zbieżności, zachowuje zakres danych cieplnych i falowych oraz odsyła do definicji Sturma–Liouville'a. Doprecyzowano brakujące w skrótowym podsumowaniu założenie gładkich danych początkowych o zwartym nośniku w (0,L) dla zasady Duhamela; jest to założenie już istniejące w 6.5, nie nowa treść. |

Korekta podsumowania: commit 4647cf25e044a36438f81cc9add2b3165900740b, blob ed1b662b3f324d0efca35e7a77e9729217b125f1. Zachowano dokładnie listy 38 etykiet i 52 odsyłaczy. Nie wykryto innych błędów matematycznych ani istotnych luk w kontrolowanym zakresie. Rejestr i testy pozostawiono bez zmian.

Druga lektura zakończona: 9/9 sekcji, 42/42 kryteriów po korekcie. Poprzedni CI 45572681202 (10/10, kompilacja i diagnostyka PASS) oraz oględziny PDF z iteracji 78 dotyczą wcześniejszego bloba źródła; wymagane ponowne potwierdzenie dla poprawionej wersji. Nie uruchomiono lokalnie nowych testów ani Lean, nie kompilowano całego tomu. Rozdział pozostaje otwarty. Następna iteracja 83: niezależny audyt kontrolny, ponowna weryfikacja CI i PDF dla aktualnego źródła oraz decyzja o stabilizacji wyłącznie po zaliczeniu bramek.
