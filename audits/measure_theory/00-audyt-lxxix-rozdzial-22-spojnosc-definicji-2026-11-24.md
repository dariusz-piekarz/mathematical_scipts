# Audyt LXXIX (79) — rozdział 22, spójność definicji i ponowna kontrola dowodów

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Stan wejściowy
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289414520 dla a90443dc4daeba784e10d1dfc14957a3b0de7328 był in_progress przy końcowym odczycie. Nie stanowi jeszcze zaliczenia testów ani kompilacji. Nie oglądano PDF z tego przebiegu.

## Zmiany
Commit fe6c764d7e49ddbc5897bfdd891c09e18fe49208, blob 408b901530bd30243665f4f7f577d195b0158877:
- Rozróżniono granicę mglistą/słabą-* o utraconej masie od granicy probabilistycznej. Przy zachowaniu masy i lokalnej zwartości oraz ośrodkowości trzy rodzaje zbieżności są równoważne; dodano odsyłacz do dowodu.
- Jawnie określono odległość TV jako supremum różnic na zbiorach, połowę normy wariacji dla różnicy prawdopodobieństw. Uzasadniono współczynnik 1/2 rozkładem Jordana i Hahna.
- W Portmanteau opisano miarę obrazową na całej prostej i wybór wszystkich końców podziału poza przeliczalnym zbiorem punktów dodatniej masy, z końcami zewnętrznymi poza zakresem funkcji.
- W dowodzie zwartości probabilistycznej na zwartej przestrzeni metrycznej zastąpiono skrót o rozszerzeniu granic z gęstej rodziny (która nie musi być przestrzenią liniową) bezpośrednim kryterium Cauchy'ego dla całek z każdej funkcji, a następnie wykazano liniowość, dodatniość i normę funkcjonału.
- W dowodzie zbieżności wąskiej przy braku ucieczki masy użyto konkretnych odsyłaczy do twierdzenia o miarach Radona i lematu o funkcji odcinającej z rozdziału 20.
- Ponownie sprawdzono oba kierunki Prochorowa, w szczególności margines między progami w wyborze przy nieosiąganym infimum oraz sumę oszacowań dopełnień. Nie znaleziono nowej luki w tych argumentach.

## Niezależna kontrola skończona
Rzeczywiście wykonane obliczenia całkowitoliczbowe w JavaScript: wszystkie 45 wektorów prawdopodobieństw na trzech punktach z mianownikiem 8, wszystkie 2025 uporządkowanych par, wszystkie 125 funkcji o wartościach w {-2,-1,0,1,2}.
- 2025 porównań: dwukrotność supremum po wszystkich 8 podzbiorach równa sumie wartości bezwzględnych różnic wag.
- 253125 nierówności całkowych: różnica całek ograniczona przez dwukrotność odległości TV razy norma supremum funkcji.
- 5625 porównań reprezentacji warstwowej po przesunięciu funkcji o jej minimum, również dla funkcji ujemnych.
Wszystkie porównania zaliczone; nie są dowodami twierdzeń dla dowolnych przestrzeni ani uruchomieniem repozytoryjnych testów Python.

Kontrola źródła: 23 unikalne etykiety, poprawne zagnieżdżenie środowisk, oba nowe odsyłacze do rozdziału 20 istnieją. Statusy nowego commitu źródłowego w chwili odczytu puste.

## Werdykt
Rozdział 22 nadal w stabilizacji. Wymagane potwierdzenie CI na nowym blobie, pełnej i izolowanej kompilacji oraz oględziny wszystkich stron. Nie przechodzić do rozdziału 23 przed zamknięciem bramki.
