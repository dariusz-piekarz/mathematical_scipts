# Rozdział 22 — audyt 86 (3/4 podsekcji, etap poprawkowy)

24 listopada 2026. Wyłącznie istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Zmiany
Przejrzano trzecią podsekcję. Uściślono definicję transformaty dystrybucyjnej przez transpozycję (nie przez sprzężenie ani odwrotność), jej ciągłość i wzajemną odwrotność operatorów, kwantyfikatory i argumenty zmiennych testowych w tożsamościach operatorowych, oba znaki oraz odbicie i F^4=Id. W przykładach delty i wielomianów rozróżniono funkcję od dystrybucji regularnej i jawnie wyprowadzono stałe normalizacyjne. W dowodzie Plancherela wykazano najpierw zgodność transformaty klasycznej i dystrybucyjnej na S przez Fubiniego z całkowalną majorantą, następnie zachowanie iloczynu skalarnego ze wzoru odwrotnego, konstrukcję przedłużenia na L2 (Cauchy, niezależność przybliżenia, liniowość, domkniętość obrazu i surjektywność), a na końcu zgodność w silnej topologii S' przez jednostajne oszacowanie po zbiorach ograniczonych. Commit 08fb46530a181ec9c69477d60732e5095810ac22, blob 1da8a1ba245a2a00077082b008f83cbc6d8ece77. Nie zmieniano ostatniej podsekcji.

## Kontrole
Bieg 45428674204 z audytu 85 zakończony sukcesem. Dodano piątą metodę FA22_fourier_plancherel_01 w trwałym pliku tools/tests/test_functional_analysis_ch22.py (7a0d0023d2122ed5ae420d8561a265c75a81196d). Lokalnie uruchomiono część obliczeniową w Pythonie: 9 przypadków przeniesienia pochodnej, 9 mnożenia przez zmienną, 9 odbicia, 9 czwartej potęgi, 81 tożsamości iloczynu skalarnego — 117/117. Modele wielomian razy exp(-x^2/2); współczynniki całkowite zespolone małego modułu dokładnie reprezentowalne w użytej arytmetyce complex, momenty całkowe przeskalowane wspólnym czynnikiem 2^8/sqrt(pi). Nie jest to formalizacja ogólnego twierdzenia. Kontrola aktualnego źródła: 16/16 unikatowych etykiet, 20/20 odsyłaczy rozwiązanych w kontekście 17–22, 34/34 fragmentów regresyjnych, poprawne zagnieżdżenie środowisk. Bieg 45429602040 dla najnowszych testów w toku przy kontroli. Pełne nowe CI i oględziny aktualnego PDF niepotwierdzone. Lean nie uruchamiano.

## Decyzja
3/4 podsekcji pierwszego przeglądu, 0/3 stabilizacji. Następny audyt 87: splot z funkcją szybko malejącą i transformata dystrybucji o zwartym nośniku, ze szczególnym uwzględnieniem zamiany działania dystrybucji z całkowaniem i zgodności stałej splotowej z rozdziałem 17. Następnie pełna stabilizacja.
