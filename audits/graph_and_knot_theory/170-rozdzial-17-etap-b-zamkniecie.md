# Audyt 170 — drukowany rozdział 17, zamknięcie etapu B

Data: 2026-11-24. Plan 118. Kontynuacja raportu 169.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Blob: cb06ea9d5c73fc5b1b9e0d3d3517a10b573f5d89 (bez zmian).

## Bramka etapu B
- GitHub Actions run 45483300188, próba 2, commit 5467adfb381183eb3a9cf0d92895bd0d234ef5cf: status completed, conclusion success.
- Job full-book-pdf 138777047954: SUCCESS, wszystkie kroki zakończone sukcesem, w tym trzy kompilacje rzeczywistej książki i przekazanie artefaktu.
- Job structural-audit 138777051719: SUCCESS, w tym niezależne regresje Kuratowskiego i trójspójności.
- Porównano przez GitHub API wszystkie 44 pliki rozdziałów i plik główny książki z aktualną gałęzią: identyczne bloby. Nie twierdzimy, że całe repozytorium ma ten sam HEAD.
- Pobrano NOWY artefakt 14964886574 z próby 2, utworzony 2026-11-24 21:07:57 UTC. ZIP 2807146 B; PDF 2448195 B, 335 stron A4. Plik ostrzeżeń ma 0 bajtów.
- Wydzielono strony fizyczne 142–155 (drukowane 132–145), wyrenderowano i obejrzano wszystkie 14 stron. Nie zauważono kolizji, ucięć ani problemów z rysunkiem Kempego.
- Porównano obrazy wszystkich 14 stron z lokalnym PDF próby 1 za pomocą PyMuPDF: identyczne piksel po pikselu przy domyślnym renderowaniu.
- W tej iteracji nie zmieniano treści ani nie uruchamiano ponownie 12 indywidualnych regresji; ich zaliczenie w etapie B odnotowano w raporcie 169. Nowe CI wykonało własny zestaw kontroli strukturalnych i matematycznych.

## Decyzja
Etapy A i B drukowanego rozdziału 17 zamknięte dla wskazanego blobu. Bramka ponownej kompilacji i kontroli rzeczywistego PDF została spełniona. Nie oznacza to formalnego dowodu w Lean ani ukończenia całego tomu.

## Wznowienie
Etap A drukowanego rozdziału 18: Grafy na powierzchniach, grafy dualne i homologia komórkowa, plik chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex. Najpierw jeden audyt merytoryczny z oceną ewentualnych istotnych uzupełnień, potem stabilizacja bez nieuzasadnionego rozszerzania. Następnie niezależny etap B. Zachować istniejącą gałąź i wszystkie regresje.
