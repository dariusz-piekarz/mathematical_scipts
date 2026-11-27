# RRC 23 — iteracja 348

Pierwszy audyt szczegółowy sekcji 23.4 (postęp 4/8). Commit f2856668aa8d5c0852e495c18aa23bef631d44de, blob bf75718b1177ce74888dcea1ba0a5a895a34559a.

- Zdefiniowano odległość na torusie przez minimum po kracie, wykazano jednoznaczność minimalizującej różnicy dla odległości mniejszej niż pi i gładkość kwadratu odległości w lokalnych współrzędnych.
- Sprecyzowano jednostajność promienia i stałej przestrzennego warunku Lipschitza względem wszystkich p. Uproszczono podwajanie zmiennych do jednego parametru epsilon.
- Uzasadniono osiąganie dodatniego maksimum na zwartym podzbiorze odsuniętym od górnego krańca czasu, zanikanie obu odległości i obu kar przez moduł jednostajnej ciągłości oraz wykluczenie obu punktów z czasem 0 za pomocą jawnych nierówności. Wyjaśniono również przypadek naruszenia porównania w końcowej chwili T.
- Zapisano obie funkcje testowe wprost, obliczono ich gradienty oraz pochodne czasowe. Sprawdzono znaki, eliminację pochodnych czasowych i sprzeczność nawet bez ograniczoności p_epsilon.
- Rozszerzono wniosek na monotoniczność maksymalnej różnicy od dowolnej chwili s, z dowodem przesunięcia czasu, niezmienniczości na dodawanie stałej i równości supremum zwykłego z istotnym. Odróżniono jednoznaczność od istnienia.
- Dodano przykłady hamiltonianu niezależnego od x, afinicznego względem p i hamiltonianu ciągłego niespełniającego przyjętego warunku. Nie wnioskowano stąd o niejednoznaczności.

Kontrola zapisanego źródła: 888 wierszy (728 wcześniej), 25 zachowanych unikatowych etykiet, 25 odsyłaczy (wszystkie jednoznaczne, cele zewnętrzne w rozdz. 2 i 24), brak błędów zagnieżdżenia środowisk i delimiterów. Wszystkie pozostałe sekcje identyczne. Kompilacja rozdziału 23 i kontrola wizualna niepotwierdzone.

Następny etap: sekcja 23.5 — transformata Legendre'a, zasada programowania dynamicznego i dowód wzoru Hopfa–Laxa w sensie lepkościowym.
