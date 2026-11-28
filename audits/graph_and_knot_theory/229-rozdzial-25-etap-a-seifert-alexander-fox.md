# Audyt 229 — drukowany rozdział 25, etap A: Seifert, Alexander, Fox

Data: 2026-11-25. Kontynuacja 228.
Źródło: chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex; blob wejściowy 8aacf564a731d3388e33cb0f773663daef4ccba4.

## Kontrola i poprawki
Odczytano obie sekcje w całości. Rozpisano niezależność formy Seiferta od reprezentantów homologii, przesunięcie dwóch rozłącznych krzywych i obliczenie znaku przecięcia przez cylinder z brzegiem alpha_i^+ minus alpha_i^-. W dowodzie z nakrycia cyklicznego poprawiono mapę Mayera–Vietorisa: sklejenie F_+ w Y_j z F_- w Y_(j+1) daje t i_- minus i_+. W konwencji kolumnowej i_+ ma macierz V^T, i_- ma V, więc otrzymujemy tV-V^T. Doprecyzowano spójność Y przez dualność Alexandera, identyfikację przez funkcjonały splecenia oraz skończone nośniki łańcuchów. Numeracja kopii odpowiada ujemnemu meridianowi; przy dodatnim generatorze podstawiamy t^-1 i dostajemy równoważną prezentację dla tej odwróconej akcji, tV^T-V. Nie utożsamiamy modułów na podstawie samej transpozycji. Porównanie wielomianów z algorytmu Foxa korzysta z symetrii wyznacznika.
Rozpisano istnienie i jednoznaczność pochodnej Foxa przez sumę prefiksów, niezmienniczość po skasowaniu pary odwrotnych liter i regułę Leibniza z augmentacją. Wyjaśniono, że do identyfikacji H1 nakryć wystarcza abelianizacja tej samej podgrupy ker phi z działaniem przez sprzężenie. Zastąpiono nieuzasadnione określenie niezależnych relacji wyborem po usunięciu relatora redundantnego. Sprawdzono rachunki przykładowych macierzy i stabilizacji. Twierdzenie o S-równoważności i dualność Alexandera pozostają przywołanymi wynikami.
Commity b1af6e38bf5a8b9fc02e48cb9c0ca27bfc25ad2c i ccee86755188f7bd79bec8fce10fc85094906fe9; końcowy blob b634aa684ddf601ad570feadfaebfd4c50bf5195. Konflikt równoległego przesunięcia gałęzi rozwiązano ponownym odczytem i zapisem. 162 zgodne pary środowisk, 21 unikatowych etykiet, 7 odsyłaczy.

## Regresja
GKT-25-FOX-PREFIX-01: rzeczywiście uruchomiono w Pythonie w środowisku wykonawczym samodzielny model po abelianizacji. PASS: 30948 wstawień par odwrotnych liter, 1365 tożsamości fundamentalnych, 1 dokładne obliczenie dla trójlistnika. Kod zapisany w tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py, commit a0678b73e7ad8e3d2f4f4cf5795ec924b0830978, blob e5a1ccabcecefc4a450ceda41a56e4c6b2c83915, potwierdzono wywołanie w __main__. Test skończony, nie Lean ani dowód pełnego rachunku nieprzemiennego.

## CI i decyzja
Run 45593499698 z poprzedniego etapu: full-book-pdf success, structural-audit queued przy ostatnim odczycie. Nie jest to kompilacja bieżącej wersji. Nowy globalny run 45594206845 dla a0678b73 queued. Nie wykonano oględzin PDF ani pełnego zintegrowanego testu lokalnie. Etap A otwarty. Postęp 24/44.
Następny audyt 230: Conway, Arf i sygnatura; sprawdzić też wcześniejsze regresje oraz później Jonesa, warkocze i końcowe sekcje, bez przedwczesnego zamykania rozdziału.
