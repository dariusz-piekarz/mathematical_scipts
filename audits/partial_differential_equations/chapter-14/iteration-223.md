# RRC 14 — iteracja 223: pierwsza lektura 033–044

Źródło przed 15c669e7697a55d2d9310f0bb49b0f700c98ce25, po 99ba6a2ae7b7f04146a7b540248fea76dfd07a48; commit c6ef6ef9743f6cb1c7dc72db8a5b1536c0dcdabf. Odczytano sekcje 6–7, tezy RRC 07 o splocie i aproksymacji oraz RRC 09 o lokalnych przestrzeniach i iloczynach; ponownie użyto rachunku z dowodu średniej w RRC 03.

| Kryterium | Wynik |
|---|---|
| PDE-14-033 | Doprecyzowano rzeczywisty charakter funkcji i rozróżnienie półciągłości z góry/dół. |
| PDE-14-034 | Średnia sferyczna: skalowanie, różniczkowanie przez zbieżność zmajoryzowaną oraz hipotezy twierdzenia Gaussa. |
| PDE-14-035 | Monotoniczność średniej i granica w zerze, dodano średnią po kuli przez całkowanie we współrzędnych biegunowych, obie nierówności dla superharmonicznych. |
| PDE-14-036 | Dystrybucyjna subharmoniczność: nieujemny test, dziedzina splotu, komutacja laplasjanu i zbieżność w L¹_loc; wyraźnie wyłączono nieudowodnione przejście do wyróżnionego reprezentanta półciągłego. |
| PDE-14-037 | Mocna zasada minimum: nieujemny integrand i dodatnia miara fragmentu sfery, argument dla każdego punktu zbioru minimum oraz spójność. |
| PDE-14-038 | Analogiczna mocna zasada maksimum przez zmianę znaku. |
| PDE-14-039 | Hopf: ścisła dodatniość wewnątrz, jawna stała alpha i wybór epsilon z minimum na zwartej sferze. |
| PDE-14-040 | Oba brzegi pierścienia, sprzeczność z ujemnym minimum, nierówność granicy dolnej zamiast nieuzasadnionego twierdzenia o istnieniu granicy. Pochodna normalna od strony wnętrza. |
| PDE-14-041 | Caccioppoli: lokalne H¹ i wspólny zbiór pełnej miary, wzmocnienie przez dowolne przesunięcie u-k. |
| PDE-14-042 | Dopuszczalność testu: lokalna reguła iloczynu, przedłużenie zwartonośne przez zero, splot z zachowaniem nośnika, zbieżność w H¹, ciągłość funkcjonału na lokalnej przestrzeni. Bez globalnego H¹ dla u. |
| PDE-14-043 | Znaki równania energetycznego, Cauchy–Schwarz, przypadek X=0, stała 4 Lambda²/lambda². |
| PDE-14-044 | Jawna konstrukcja radialnego obcięcia, C=4||chi'||∞², oszacowanie względem średniej i dokładny odsyłacz do dalszego Harnacka w RRC 17. |

18 zamian blokowych, 1018 wierszy, 34 etykiety zachowane w kolejności. 45/45 wystąpień odsyłaczy (32 różne cele) rozwiązano jednoznacznie na przypiętym commicie w RRC 01,03,07,09,10,13,14,15,17; stos środowisk poprawny. Pomocnicze kontrole skończone: 108/108 znaków współczynnika laplasjanu bariery Hopfa oraz 45/45 nierówności energetycznych dla funkcji afinicznych i obcięcia kawałkami liniowego; nie są dowodem ani testami CI. Nie wykonano dedykowanej kompilacji, kontroli PDF ani Lean.

Pierwsza lektura 44/64, 7/10 sekcji. Następna: 045–058, funkcja Greena, dodatniość, konstrukcja w kuli, reprezentacja i porównanie.