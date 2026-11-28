# Topologia ogólna — globalny audyt 05, blok 18–22

**Data:** 2026-11-22.
**Zakres:** tematyczny audyt reprezentatywnych,
ważnych matematycznie dowodów w 18–22,
sprawdzenie zależności i powtórzeń.
Nie jest to audyt wszystkich dowodów tych rozdziałów.
Źródła zatwierdzonych rozdziałów nie zostały zmodyfikowane.

## 18. Przestrzenie odwzorowań

Dla metrycznej przeciwdziedziny Y topologia zwarto-otwarta
na C(X,Y) jest równa topologii zbieżności jednostajnej
na zbiorach zwartych, również gdy X nie jest Hausdorffa.
Pierwszy kierunek używa dodatniego minimum
odległości f(K) do domkniętego Y\U;
drugi kierunek wybiera skończone pokrycie zwartego
g(K) przez małe kule, domknięte przeciwobrazy
K_j⊂K i otoczenie podbazowe
\(\bigcap_j[K_j,B(y_j,\delta/2)]\).
Dla pustego K przypadek jest rozstrzygnięty oddzielnie.
Ciągłość ewaluacji wymaga w tym rozdziale
lokalnej zwartości Hausdorffa X i odsyła do lematu 14
o otoczeniach z zwartym domknięciem.

## 19. Przestrzenie polskie i hierarchia borelowska

W charakterystyce polskich podprzestrzeni
A⊂X przez warunek G_delta
dla A=⋂U_n skonstruowano zgodną zupełną
metrykę przy pomocy ciągłych funkcji
\(h_n=1/d(\cdot,X\setminus U_n)\),
z rozróżnieniem U_n=X oraz A=∅.
Jeżeli ciąg w A jest Cauchy'ego dla nowej metryki,
nie może zbiegać w X do punktu poza dowolnym U_n,
gdyż w takim przypadku h_n dąży do ∞.
W przeciwną stronę, dla polskiej A
wybrano kule o małej średnicy w zgodnej
zupełnej metryce na A, aby otrzymać
otwarte V_n⊃A z ⋂V_n=A.
Obie części wymagają metryzowalności X,
a nie samej ogólnej topologii.

## 20. Zbiory analityczne

W lemacie o uniwersalnej analitycznej rodzinie
przekrojów kody złożone z wartości 1 dla par
dopuszczonych i 2 dla par wykluczonych
działają niezależnie od konwencji ℕ={0,1,...}
lub ℕ={1,2,...}. Predykat równości 1
nie jest zastąpiony niepoprawnym
predykatem dodatniości.
Domkniętość F zapewnia, że wszystkie
prefiksy leżące w drzewie T_F
odtwarzają dokładnie F.
Diagonala D={x:(x,x)∉U} nie może być analityczna,
a E={x:(x,x)∈U} jest analityczna i nieborelowska.
Materiał dotyczy przestrzeni Baire'a; nie ogłaszamy,
że w każdej przestrzeni polskiej istnieje
nieborelowski zbiór analityczny.
Teoria determinacji Wadge'a pozostaje w skrypcie logiki.

## 21. Vietoris i Fell

W dowodzie zwartości topologii Fella
na wszystkich domkniętych podzbiorach X,
włącznie z ∅, prześledzono dowód kryterium
Aleksandra dla pokryć podbazowych.
Z hipotetycznego braku skończonego podpokrycia
wynika dla każdego zwartego C_j
własność skończonych przecięć
\(C_j\cap\bigcap_{i\in I_0}(X\setminus U_i)\neq\varnothing\).
W konsekwencji skonstruowany domknięty
\(F=X\setminus\bigcup_iU_i\)
nie należy do żadnego elementu podbazowego pokrycia.
W szczególności dowód zwartości Fella
nie zakłada Hausdorffowości X.
Hausdorffowość topologii Fella
jest osobną tezą przy lokalnej zwartości Hausdorffa X.
Dla zwartej Hausdorffa X topologia Fella
na niepustych domkniętych jest równa
Vietorisowi, gdyż zwarte dopełnienia
otwartych zbiorów zamieniają warunki
zawierania na warunki omijania.

## 22. Kuratowski, Wijsman, Attouch–Wets

W twierdzeniu o czterech równoważnych
zbieżnościach dla właściwej przestrzeni
metrycznej sprawdzono rozdzielenie
warunków F≠∅ oraz r=d(x,F)=0 i r>0.
W przypadku r>0 zwartość domkniętej kuli
zapewnia graniczny punkt podciągu
z odległościami mniejszymi niż r,
który musiałby należeć do granicy górnej
Kuratowskiego, a więc do F, co przeczy
definicji r. Ten argument nie jest
poprawny bez zwartości kul — i
rozdział pokazuje potrzebę hipotezy
przez niezwartą, ograniczoną
zupełną przestrzeń dyskretną.
Przykład \(\{0,n\}\subset\mathbb R\)
pokazuje lokalną zbieżność AW/Fell
bez zbieżności w metryce Hausdorffa.

## Wniosek z pięciu raportów globalnych

Raporty globalne 01–05 objęły najważniejsze
zależności między wszystkimi 22 rozdziałami,
ponadto do CI dodano automatyczny test
katalogu, odsyłaczy, unikatowości etykiet,
zrównoważenia środowisk i terminologii.
Nie wykryto nowych błędów w przytoczonych dowodach.
**Nie jest to jeszcze pełny, indywidualny audyt
wszystkich 261 dowodów**, ani przegląd
wszystkich ilustracji pełnej książki;
dalsze audyty są nadal otwarte.
