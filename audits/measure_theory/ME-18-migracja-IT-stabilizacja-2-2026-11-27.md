# ME-18 — drugi czysty przebieg stabilizacji merytorycznej

27.11.2026. Źródło niezmienione: blob 2f5328d2bbe1bfd6ed5d9b53349a5317dada30c8 (994 wiersze).

Sprawdzono rozkład funkcji BV prawostronnie ciągłych i odpowiadających im miar ze znakiem, w tym skok w b i brak masy w a. Porównano pełne twierdzenie o konstrukcji miary w ME-16 oraz twierdzenie o pochodnej dystrybuanty w ME-25. Współczynniki atomowe są bezwzględnie sumowalne; bezatomowa część osobliwa ma zerową pochodną prawie wszędzie; wariacja jest addytywna dzięki rozłącznym zbiorom skupiającym. Sprawdzono kierunek zależności ME-25 (twierdzenia o różniczkowaniu miar i całek) od podstawowej teorii RN; żaden z trzech sprawdzonych dowodów ME-25 nie odwołuje się do rozkładu generatora Stieltjesa w ME-18. Nie stwierdzono nowej usterki matematycznej wymagającej zmiany źródła.

Dodano test regresyjny g(t)=t-2C(t)+3 chi_[1/2,1](t)-chi_{1}(t), commit 17227447a132119289b27f8af2a5e3748805e3b8. Trzy składniki mają wariacje 1, 2 i 4. Lokalnie wykonano obliczenia Python Fraction odpowiadające nowemu testowi: 10/10 poziomów podziałów, z maksymalnie 2049 punktami, dokładne sumy wahań 7-2(2/3)^n rosną do 7. Sprawdzono także masę ze znakiem równą 1 i całkę t względem miary równą 0. Nie uruchomiono całej suity repozytorium.

CI na poprzednim commicie testowym 6686534: ME-18 #45995643214 pending, globalny ME #45995643218 queued. Nowy test nie ma potwierdzonego wykonania CI. PDF i odbiór techniczny pozostają otwarte. Dwa czyste przebiegi merytoryczne, kolejny krok: audyt kontrolny ME-18, następnie ME-20.
