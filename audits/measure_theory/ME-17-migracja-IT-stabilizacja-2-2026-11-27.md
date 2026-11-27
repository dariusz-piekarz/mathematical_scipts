# ME-17 — drugi czysty przebieg stabilizacji merytorycznej

27.11.2026. Źródło: niezmieniony blob 1acd91a40cf69b7250d5008a76c18da57f815f5f (674 wiersze).

Ponownie sprawdzono dowody kryterium epsilon–delta, rozkładu Lebesgue'a w przypadku skończonym i sigma-skończonym oraz zespolonym. W szczególności sprawdzono twierdzenie Hahna i skończoność wariacji w ME-16 oraz kierunek zależności ME-18 od twierdzeń o rozkładzie ME-17. Konstrukcja rozkładu nie korzysta z twierdzenia Radona–Nikodyma. Porównano konstrukcję funkcji Cantora z ME-04 i twierdzenie o funkcji pierwotnej w AM1-37. To ostatnie korzysta z RN, ale służy wyłącznie przykładowi Cantora, nie dowodowi rozkładu. Nie wykryto nowej usterki matematycznej wymagającej zmiany źródła.

Rozszerzono trwały test tools/tests/test_measure_theory_ch17.py (commit 6643c1e7273abd94bad74e98d05fb3f1633d1206) o dokładne momenty miary Cantora, symetrię względem 1/2 oraz dolne i górne sumy na przedziałach podstawowych. Niezależnie odtworzono te rachunki w JavaScript przy użyciu wymiernych liczb reprezentowanych przez BigInt: 4/4 początkowych momentów, 9/9 tożsamości odbicia, 48/48 par oszacowań (stopnie 1–8, poziomy 1–6). Wszystkie zaliczone; nie uruchomiono oryginalnego testu Python.

Stan CI na odczytanym commicie 822419c: ME-17 #45994705116 pending, globalny ME #45994705091 queued. Nowa wersja testu nie ma potwierdzonego wykonania CI. Odbiór PDF i wizualna kontrola rysunku pozostają otwarte. Dwa czyste przebiegi merytoryczne, kolejny krok: audyt kontrolny ME-17 przed ME-18.
