# Rozdział 19 — audyt 64 (2/4, pierwszy przegląd, 0/2 stabilizacji)

24 listopada 2026. Istniejąca gałąź biblioteka-matematyczna-iteracja-6.

## Zakres
Podsekcje 1–2: definicja i pierwsze przykłady, nośnik i lokalność.

## Poprawki
Doprecyzowano założenia i rząd na zbiorze zwartym, skalowanie w kryterium ciągłości, odsyłacze do wcześniejszych twierdzeń. Uzupełniono poprawność całki dystrybucji regularnej oraz dowód injektywności: lokalny splot, zwartość otoczenia, dodatnią odległość od dopełnienia, podstawienie, Tonellego i przeliczalne wyczerpanie. Zastąpiono notację funkcji charakterystycznej przez chi. Rozpisano konstrukcję funkcji testowej z niezerową pochodną, nieregularność także dla delty, dokładny rząd i skalowanie pochodnych. W wartości głównej Cauchy'ego uzasadniono podstawienie, całkowalność różnicy i ciągłość także nad C. Zdefiniowano ograniczenie dystrybucji wraz z ciągłością przedłużenia zerem. W lemacie o lokalności zastąpiono nieuzasadnione użycie podziału jedności jawną konstrukcją z funkcji odcięcia i dzieleniem przez dodatnią sumę na otoczeniu nośnika; wykazano istnienie największego otwartego zbioru zerowania. Rozpisano nośniki przykładów, przypadek pustego nośnika i oszacowanie globalne dla dystrybucji o zwartym nośniku oraz ciągłość jej przedłużenia do C^infty. Ujednolicono p_{K,m} z rozdziałem 17.

## Weryfikacja
Źródło fb18163c070970bf6561c725a932a23229cb0362, blob dc0359dc27dbec109bb985be1c09718fef05c693, 678 wierszy, 27/27 unikatowych etykiet, 19/19 odsyłaczy ref rozwiązanych w 17–19, poprawne środowiska. 14/14 warunków tekstowych. Dodano trzy metody regresyjne w 76cd4d797470c5b6b4be5368f11d67fc52bd8d56 oraz workflow kontekstowy 01–19 w 26df6f99256c5563a02aee3bff8cc00f72b6e6c3. Statusy CI przy odczycie: [{"id":45388150602,"sha":"26df6f99256c5563a02aee3bff8cc00f72b6e6c3","status":"queued","conclusion":null},{"id":45387870213,"sha":"cc596b2f0277fbebf3572bb3be28ed1986d03dc5","status":"in_progress","conclusion":null}]. Brak potwierdzenia pełnej kompilacji nowej wersji.

## Następny audyt 65
Podsekcje 3–4: słaba-* i silna topologia, beczkowość, równociągłość, zbieżność ciągów i sieci, regularizacja i przykłady. Kontrola CI. Po pierwszym przeglądzie ocena zakresu i stabilizacja.
