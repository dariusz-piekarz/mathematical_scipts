# Teoria grafów i węzłów — audyt 02 rozdziału 38

## Stan po pierwszym przebiegu CI
- [GitHub Actions — przebieg 45140098472](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45140098472): testy enumeracyjne i kompilacja PDF zakończone sukcesem.
- Testy: 4113 grafów skierowanych o nieujemnych wagach, 1750 grafów z wagami ujemnymi, 1190 przypadków heurystyk A* (również niespójnych), 760 niewielkich grafów nieskierowanych dla CH, przy wszystkich kolejnościach rang; dodatkowo historyczne testy BFS/DFS.
- PDF fragmentu 00–05+37+38: 45 stron, log bez przepełnień \`Overfull\`; rysunek drogi ważonej czytelny.

## Wykryte poprawki merytoryczne i składu
1. Poprzedni dowód kryterium zatrzymania Dijkstry dwukierunkowej był zbyt skrótowy. Zastąpiono go jawnym rozumowaniem z ustalonymi zbiorami $S_F,S_B$ i pierwszym/ostatnim nieustalonym wierzchołkiem najkrótszej ścieżki.
2. Uzupełniono pełne twierdzenie i dowód A* przy heurystyce dopuszczalnej, lecz niespójnej, z możliwością ponownego otwierania oraz kontrprzykład wersji bez ponownego otwierania.
3. Tabela porównawcza miała zbyt wąskie kolumny i ciasne łamanie wierszy, mimo braku technicznych przepełnień. Zastąpiono ją czytelną listą.
4. Wprowadzono przypadek testowy, w którym brak ponownego otwierania daje błędną długość 14 zamiast 13.

## Status
**W trakcie stabilizacji**, do ponownej weryfikacji składu, etykiet i regresji po tych zmianach. Nie stwierdzać ostatecznej stabilności przed pozytywnym nowym CI.
