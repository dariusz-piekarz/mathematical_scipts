# Audyt 169 — drukowany rozdział 17, etap B

Data: 2026-11-24. Plan 118, poprzedni raport 168.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Blob: cb06ea9d5c73fc5b1b9e0d3d3517a10b573f5d89 (bez zmian).
Punkt odniesienia: d92a7cab8a3c6035a3aa614627021c75b8b65e4a.

## Niezależny przegląd
- Definicje subdywizji, minora, modelu; operacje zachowujące planarność; rozłączność i spójność zbiorów rozgałęzienia.
- Drzewa z etykietami: przypadki 3 i 4, wielokrotne etykiety, rozłączność ścieżek; przejście od K5 do modelu K3,3.
- Trójspójność: kryterium kontrakcji i ścisłe zejście, w tym t=x,y oraz jednoelementowa składowa; przykład koła.
- Sklejanie osadzeń i proste cykle brzegowe: zgodność łuków, rozdzielenie Jordana, zastosowanie regularnych otoczeń i Schoenfliesa jako jawnych przesłanek.
- Dowód Kuratowskiego: minimalność, redukcje łączności, wybór krawędzi, rozcięcie dysku, naprzemienne końce i dziewięć ścieżek subdywizji K3,3. Wagner jako konsekwencja, bez kolistości.
- Zewnętrzna planarność: stożek, minory, uzupełnienie do triangulacji, przypadek równości, drzewo dualne i trzykolorowalność.
- Pięć kolorów: oba przypadki zamiany Kempego, rozłączność krzywych, przypadki początkowe i rysunek.
Nie stwierdzono istotnych błędów wymagających zmiany źródła. Nie rozszerzano materiału. Kontrola LaTeX: 22 etykiety, 58 prawidłowo zagnieżdżonych par środowisk, 37 wystąpień odsyłaczy (16 różnych celów, wszystkie odnalezione).

## Regresje ponowione w tej iteracji: 12/12
Python/NetworkX 3.6.1, rzeczywiście uruchomione pliki o hashach zgodnych z repozytorium:
- outerplanar adc59d4ba9a10116cd48747424de9c9021446879: PASS 3288,22,2650. Początkowo uruchomiono starszy lokalny plik, następnie właściwy plik o zgodnym hashu; oba dały ten sam wynik.
- kempe d497c7b896d58892865146b343d502e53faf2baf: PASS 1016,750,377.
- kuratowski 55974646d55f3dd1a38a1df0755a5478fe84047f: PASS 79471 konfiguracji, 156 grafów trójspójnych, 2196 kontrakcji.
- outer_criteria 12e7ca27476b6a337e2f84a635f505eed97dbc65: PASS 209 grafów, 123 zewnętrznie planarne, 453 dodatkowe sprawdzenia krawędzi.
- tree_minors 7e2e6423cb6df21146c15cfea637e92ee575205c: PASS 148264 konfiguracji etykiet, 361 par grafów.
- separator 8e50d95b82e230af42ebec16e488e2182363facd: PASS 335 separatorów, 2097 incydencji, 444 zejścia.
- gluing_faces 9b1bb85463efe7875978df670e9d81263d433634: PASS 2172 ścian, 3721 sklejeń w wierzchołku, 6400 wzdłuż krawędzi.
- wagner_bounds bbf69d196f167abb20c4c8b4a8135fce779d49d8: PASS 209 grafów.
JavaScript: pobrano aktualne pliki i wykonano ich funkcje run, zastępując wyłącznie końcowe console.log przez return run():
- contraction_descent: PASS 3902 grafy, 48996 krawędzi, 15449 zejść.
- face_boundaries: PASS 27959 systemów rotacji, 2397 osadzeń sferycznych, 13989 kontroli mostów.
- minor_subdivision: PASS 3372 modele.
- tree_terminals: PASS 249963 konfiguracje.
Nie sumowano nakładających się prób; nie jest to formalizacja Lean.

## PDF i CI
Porównano SHA wszystkich 44 plików rozdziałów oraz pliku głównego książki z commitem 5467adfb381183eb3a9cf0d92895bd0d234ef5cf: wszystkie identyczne. Ponownie obejrzano wszystkie 14 stron rozdziału 17 z rzeczywistego artefaktu 14963446684, PDF A4, strony drukowane 132–145; brak zauważonych usterek składu, plik ostrzeżeń 0 bajtów.
Zgodnie z bramką etapu B uruchomiono ponownie zadanie full-book-pdf z przebiegu https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45483300188 (wcześniej SUCCESS, próba 1). API potwierdziło przyjęcie ponowienia; próba 2, job 138777047954, status queued, bez końcowego wyniku.
To nie jest jeszcze nowa udana kompilacja. Nie deklarujemy zamknięcia B.

## Wznowienie
Sprawdzić wynik próby 2, pobrać nowy PDF i logi, skontrolować rozdział 17 oraz zgodność źródeł. Jeśli bez usterek, zamknąć etap B i rozdział 17. Dopiero wtedy etap A drukowanego rozdziału 18 (plik 11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex). Zachować gałąź i wszystkie regresje.
