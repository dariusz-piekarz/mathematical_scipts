# Rozdział 01 — audyt indywidualny 04

2026-11-24. Poprawki źródła: 3509732bd0f141121aed4c3baaf3978815094571. Trwałe regresje: 0276e5661433b36d3966551c4682abf5d9ba5fd2.

Znaleziono brak warunku niepustości maksymalnych zbiorów parami połączonych: dla grafu zerowego pusty zbiór byłby maksymalny, lecz nie jest klasą równoważności. Uściślono definicję i dowód w obie strony, w tym pozostawanie spacerów w klasie. Jawny przypadek dwudzielności grafu zerowego, sumowanie klas podziałów poszczególnych składowych. Usunięto przedwczesny przykład drzewa; późniejsze użycie nazwy drzewa z krótką definicją. Dopisano warunki końcowe HH, obustronną incydencję krawędzi i drobną korektę językową.

Kontrola dowodu EG: w A wybór u różnego od i,r wynika z prostoty i braku krawędzi ir; w przypadku deficytu 1 parzystość wymusza inny niedobór w ogonie. W B po usunięciu wzajemnego sąsiedztwa liczność pierwszego zbioru nadal większa; po A różnica zawarta w S. W C u=w jest dopuszczalne, bo usuwane krawędzie mają różne końce w prefiksie; stopień u maleje o 1. W każdym przypadku dodawane krawędzie wcześniej nie istnieją, nie powstaje krawędź w S. Nie znaleziono nowej luki w tych operacjach.

Rozszerzono test_graph_and_knot_foundations.py: EG i HH względem rzeczywistych realizacji dla n=0..6 (oczekiwane 33868 grafów, 50070 ciągów), ślad A^3 względem bezpośredniego liczenia trójkątów dla n=0..5, graf zerowy i ujemne stopnie. Istniejący workflow globalny zawiera wyzwalacz i uruchomienie tego skryptu; nie trzeba zmieniać workflow. Wynik nowych testów CI niepotwierdzony. Dla poprzedniego SHA 09a02e7 terminologia, aplikacja i algorytmy success; pełny audyt globalny 45347516914 w toku w chwili odczytu. Nowy SHA przy pierwszej kontroli nie miał jeszcze zwróconych przebiegów.

Status OTWARTY. Następnie: odczytać rzeczywiste logi nowych testów, potwierdzić pełną kompilację i obejrzeć strony rozdziału 01, ponownie przejrzeć źródło. Nie przechodzić do 02 przed stabilizacją.
