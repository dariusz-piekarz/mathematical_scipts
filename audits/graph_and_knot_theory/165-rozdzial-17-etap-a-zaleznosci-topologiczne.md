# Audyt 165 — drukowany rozdział 17, etap A (kontynuacja)

2026-11-24. Plan 118, poprzedni raport 164.
Źródło: chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex.
Commit źródłowy: c7403649f43a7694cbc4a235b7936a365d33f7c9.
Commit regresji: b1bc49005f5722078e1586b6d0dc256babb7ed9d.

## Zmiany
- Osiem punktowych korekt: jawne ograniczenie lematu sklejania do grafów prostych (wszystkie zastosowania spełniają warunek), odsyłacz do regularnych otoczeń, konstrukcja równoległego łuku także przy moście, konkretne sklejanie wzdłuż średnicy dysku z przedłużeniem homeomorfizmu brzegów.
- Dowód braku mostów dla grafu dwuspójnego i jawne odsyłacze do wzoru Eulera oraz wniosku o mostach i ścianach; wyłączenie powtórzenia wierzchołka wynikającego wyłącznie z zamknięcia obchodu.
- Uzasadnienie istnienia prostego łuku w ścianie i wyboru chwil przecięcia dwóch promieni; wskazanie automorfizmu dysku przenoszącego punkt do środka.
- Urealnienie listy zależności topologicznych dowodu Kuratowskiego: twierdzenie Jordana–Schoenfliesa, lokalne prostowanie, regularne otoczenia i własności spójnych otwartych podzbiorów płaszczyzny. Lokalnego prostowania nie dowodzono na nowo — to jawnie przyjęty wynik poprzedniego rozdziału.
- 31 wystąpień odsyłaczy do 15 różnych etykiet rozstrzygnięto w bieżącym i poprzednim rozdziale. Zachowano 22 etykiety, poprawne zagnieżdżenie 57 par środowisk. Ponowny odczyt źródła potwierdził zapis.

## Regresje rzeczywiście wykonane
- GKT-17-FACES-01: test_gkt17_face_boundaries.js. Funkcja run wykonana przed zapisaniem identycznej funkcji. PASS: 770 spójnych grafów etykietowanych na 3–5 wierzchołkach, 27959 układów cyklicznych incydencji, 2397 układów sferycznych wybranych według charakterystyki Eulera 2, w tym 700 dwuspójnych, 6867 obchodów, 13989 kontroli mostu/ściany, 1877 obchodów z powtórzonymi wierzchołkami w całej próbie. W przypadku dwuspójnym każdy obchód jest cyklem prostym. Test kombinatoryczny, nie dowód lokalnego prostowania ani formalizacja Lean.
- GKT-17-CONTRACT-02: ponownie wykonano lokalną kopię końcowego kodu z asercją outside===0 przez node. PASS: 3902 wystąpienia grafów, 48996 kontrakcji, 15449 zejść; overlap=13261, inside=2188, outside=0. Domknięto brak odnotowany w raporcie 164.
- Pozostałych wcześniejszych regresji nie uruchamiano ponownie w tej iteracji.

## Stabilizacja
CI: dla commitu źródłowego dostępne zapytania zwracają puste listy statusów i przebiegów. Lokalnie pdflatex i node dostępne; ponowne git ls-remote zakończyło się błędem Could not resolve host: github.com. Pełna kompilacja i kontrola PDF nie zostały wykonane. Etap A OTWARTY.
Wznowienie: kontrola spójności dowodów planarności i zewnętrznej planarności oraz terminologii, uruchomienie pozostałych regresji, pełny skład PDF i CI przed zamknięciem A; dopiero potem niezależny etap B rozdziału 17.
