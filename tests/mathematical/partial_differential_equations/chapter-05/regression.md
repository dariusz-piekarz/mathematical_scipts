# PDE-05 — rejestr kryteriów regresyjnych

Rozdział: Równanie falowe. Źródło: chapters/pl/partial_differential_equations/05-rownanie-falowe.tex.

Kryteria semantyczne służą trwałej ponownej kontroli dowodów; sam zapis kryterium lub sprawdzenie kotwicy nie stanowi wykonania dowodu ani formalizacji Lean.

| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| PDE-05-001 | chap:pde-wave | Całkowite n≥1, c>0, rzeczywiste funkcje skalarne, definicja operatora falowego i danych początkowych; miary Lebesgue'a i powierzchniowa, przypadek n=1, pochodne jednostronne na końcach czasu; kontrast z ciepłem ograniczony do właściwych klas danych. | semantyczna |
| PDE-05-002 | sec:pde5-dalembert | Współrzędne xi=x-ct, eta=x+ct, jawna odwrotność, obraz t>0 to xi<eta, operator -4c² U_xi eta. Globalna reprezentacja poprzez stałość pochodnych na spójnych włóknach, funkcje a,b klasy C¹, funkcje pierwotne F,G klasy C², stałość reszty na wypukłym D, przejście do t=0 przez ciągłość. | semantyczna |
| PDE-05-003 | thm:pde5-dalembert | Konieczność wzoru z F+G=g oraz -cF'+cG'=h; układ dla F',G', pierwotna H z orientowaną całką, stałe A+B=0; istnienie z g w C² i h w C¹, jawne pochodne u_t,u_x,u_tt,u_xx, zgodność z równaniem i oboma danymi, jednoznaczność bez warunków wzrostu. | semantyczna |
| PDE-05-004 | sec:pde5-dalembert | Dokładny zakres zależności: g w końcach odcinka, h na całym odcinku; zmiana h o nieujemną niezerową funkcję o nośniku w dowolnym podprzedziale wnętrza zmienia wartość u. Dwa przesuwające się profile dla h=0; dla g=0 i nieujemnego niezerowego h w C_c¹ dodatnia całka i stała wartość dla t≥(|x|+R)/c, brak silnej zasady Huygensa w n=1. | semantyczna |

## Iteracja 55 — 2026-11-24

Preflight: pierwotny blob 1c33d4af1690ebb5797eddc8babcc095f317898c, 8 sekcji, 30 unikatowych etykiet, 17 odsyłaczy; oba cele zewnętrzne (thm:dalembert w rozdziale 01 i chap:pde-heat w rozdziale 04) występują dokładnie raz w odpowiednich rozdziałach. Zagnieżdżenie środowisk poprawne. Pierwsza lektura struktury pozostałych sekcji wskazuje dalsze zakresy audytu: 5.2 energia globalna i lokalna, ruchoma kula, wymuszenie, zerowanie energii; 5.3 średnie sferyczne i Kirchhoff; 5.4 redukcja wymiaru i Huygens; 5.5 Duhamel (w tym stara notacja ds w całkach); 5.6 warunki brzegowe; 5.7 CFL i zasięg numeryczny; 5.8 podsumowanie. Są to punkty do sprawdzenia, nie stwierdzone błędy. Rysunek stożka wstecznego wymaga późniejszej kontroli rzeczywistego renderu.

Poprawki wprowadzenia i 5.1: commit f85f84634b6673f79646ee68f2489c88463f3a4b, blob 941de8859c5516d226458473db6361932098842f. Usunięto lukę między lokalnym rozkładem fal a globalnym wnioskiem o jednoznaczności. Uzupełniono jawny rachunek pochodnych, oba dane początkowe i argument o wnętrzu obszaru zależności. Zachowano 30 etykiet, 18 odsyłaczy i poprawne zagnieżdżenie środowisk. Pierwszy audyt: 1/8 sekcji. Bez kompilacji, wykonania testów, oględzin PDF i Lean. Następny zakres: 5.2.
