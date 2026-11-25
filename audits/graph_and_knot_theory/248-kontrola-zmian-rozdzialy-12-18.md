# Audyt 248 — kontrola zmian, rozdziały drukowane 12 i 18

Data 2026-11-25. Baza ff96b359c1cd1aba88270b77d340c844f6efc9ec, stan porównania d1542d5c4cfaa48166e8f61c76235c3db9a99f64. Dokładny diff: TG43 wyłącznie 53 dodane linie przykładu; TG11 doprecyzowanie hipotez o pętlach i krawędziach równoległych.

TG43: sprawdzono prostotę, spójność, stopnie, liczność, górną i dolną granicę średnicy, obie nierówności dla przewodności i zastosowanie Cheegera. Bez nowych błędów. TG11: dopisano wybór składowej, odwołanie do spójności grafu dualnego, definicję przekroju dla multigrafu i argument liścia niepustego lasu o parzystych stopniach (commit 9c20624fdf7b400e60234534cc19de1afecfd340). Nie zmieniono innych dowodów.

Wykonano funkcję JS GKT-12-18-DELTA-01: 5 modeli kubicznych, 486 BFS, 9907 przekrojów grafu n=14; 18596 spójnych sferycznych układów rotacji przy ustalonej inwolucji półkrawędzi i 1–4 krawędziach, 28806 par dopełniających drzew, 140830 testów parzystości przekrojów dualnych. Wszystkie asercje PASS. Wśród układów 15221 z pętlami, 12870 z krawędziami równoległymi; liczby dotyczą oznaczonych układów, nie klas izomorfizmu. Trwale zapisano wykonaną funkcję w test_gkt12_18_delta.js (375b3c19b16841f7c15d010610d6e2fa1720e4b0), włączono w istniejący workflow (b8c862de5073cc7d5b118fd829cb28ba6c9034cd). Nie uruchamiano osobno zapisanego pliku przez Node. Nie jest to formalizacja Lean.

Kontrola matematyczna zmian zakończona z poprawką TG11. Bramka aktualnego CI i wizualnej kontroli PDF otwarta; brak potwierdzonego wyniku GitHub Actions dla nowego SHA. Nie zwiększać licznika stabilizacji. Następnie niezależna kontrola poprawki TG11 i techniczne bramki dla rozdziałów 2,4,6,12,18, po czym kontynuacja rozdziału drukowanego 26 od raportu 246.
