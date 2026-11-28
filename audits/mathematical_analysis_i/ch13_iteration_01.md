# MA1-13 — iteracja rozwojowo-stabilizacyjna 01
Rozdział 41bd49a, integracja tomu 32b3eaa i katalogu 70029c0, testy dad18e1, kryteria 8d59da1. Dodano 166 wierszy źródła, 15 etykiet, 10 trwałych kryteriów i 8 metod testowych.
## Audyt semantyczny
001–004: indeksy od zera, waga a_j liczona z n-j+1 wystąpień; podział średniej na skończony początek i ogon. Przykłady Grandiego i szeregu jedynek oraz tożsamość s_n=(n+1)c_n-nc_(n-1) poprawne. Warunek a_n/n -> 0 nie jest wystarczający.
005–008: r=0 jawnie uwzględnione; drugi szereg geometryczny wyprowadzony z iloczynu Cauchy'ego, bez przedwczesnego użycia pochodnych. Wagi sumują się do 1, ustalone wagi zanikają, ograniczoność daje zbieżność bezwzględną. Dwukrotne sumowanie przez części dopiero po uzasadnieniu zbieżności wszystkich trzech szeregów. Oszacowania b_n,s_n,a_n poprawne również dla n=0.
009: sumy częściowe m+1 i -(m+1), średnie (m+1)/(2m+1) i 0; iloczyn Cauchy'ego daje 1/(1+r)^2, granica 1/4. Schemat implikacji z odsyłaczami do obu kontrprzykładów.
010: liniowość obu metod, wzór przesunięcia Cesàro i jego odwrócenie, r^m niezerowe dla r>0, r=0 osobno, m=0 trywialne. Rozróżniono grupowanie od sumowalności pierwotnego szeregu.
## Kontrole
Sprawdzono unikalność 15 etykiet i lokalne odsyłacze nowego rozdziału oraz poprawność JSON katalogu. Zbiorczy zapis GitHub nie powiódł się; zapisano pliki kolejno na istniejącej gałęzi, bez wymuszania aktualizacji ref. CI, skład PDF i kontrola Atlasu po publikacji wymagają potwierdzenia. Lean nieuruchomiony. Status: w stabilizacji.
