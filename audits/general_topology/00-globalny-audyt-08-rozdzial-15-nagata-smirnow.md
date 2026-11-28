# Topologia ogólna — globalny audyt 08: twierdzenie Nagaty--Smirnowa

**Data:** 2026-11-22.
**Źródło:** `chapters/pl/general_topology/15-parazwartosc-i-podzialy-jednosci.tex`.
**Niezmieniony blob:** `82e0fb5be75489017c8ea1844c698c87ce580901`.
**Zakres:** ponowne niezależne sprawdzenie
dowodu twierdzenia Nagaty--Smirnowa,
ze szczególnym naciskiem na
nieprzeliczalny zbiór indeksów
i ciągłość odwzorowania w normie supremum
(linie 496–752).
Nie powtarzano wszystkich innych
dowodów parazwartości i twierdzenia Stone'a.

## Hipotezy twierdzenia

Założenie regularności i T1 jest
jawnie potrzebne w kierunku (ii)⇒(i).
Baza jest **przeliczalną sumą
rodzin lokalnie skończonych**,
ale każda taka rodzina może być
nieprzeliczalna. Dowód nie zakłada,
że suma całej bazy jest przeliczalna.
Przypadek pustej przestrzeni
jest rozważony osobno.

## Konieczność

Dla przestrzeni metrycznej X
i każdego n wybieramy pokrycie
kulami o promieniu 2^-n.
Twierdzenie Stone'a daje
lokalnie skończone rozdrobnienie
V_n tego pokrycia.
Dla x∈O z B(x,ε)⊂O i
2^{1-n}<ε element V∈V_n
zawierający x mieści się
w pewnej kuli B(y,2^-n).
Wówczas każdy z∈V spełnia
d(x,z)<2^{1-n}<ε.
Stąd suma rodzin V_n
jest bazą topologii.
Nie potrzeba separowalności
ani ośrodkowości X.

## Wystarczalność, etap 1: normalność

Dla dwóch rozłącznych
domkniętych A,C definiujemy
P_n jako sumę zbiorów B∈B_n,
których domknięcia nie spotykają C.
Analogicznie Q_n dla A.
Lokalna skończoność B_n
zapewnia równość
cl P_n = ∪_{B∈P_n} cl B;
dlatego domknięcie P_n omija C,
a domknięcie Q_n omija A.
Regularność i własność bazy
wymuszają, że P_n pokrywają A,
a Q_n pokrywają C.
Zbiory
P=∪_n(P_n\∪_{j≤n}cl Q_j)
oraz
Q=∪_n(Q_n\∪_{j≤n}cl P_j)
są otwarte, zawierają odpowiednio
A,C i są rozłączne.
Dla członkostwa jednocześnie
w n-tym i m-tym składniku
przypadki n≥m i m≥n
prowadzą do sprzeczności.
Zatem X jest normalna.

## Wystarczalność, etap 2: dokładne zbiory dodatniości

Dla dowolnego otwartego G⊂X
rodziny B_n lokalnie skończone
dają domknięte zbiory
F_n(G) = ∪{cl B: B∈B_n,cl B⊂G}.
Mamy F_n(G)⊂G i
G=∪_n F_n(G): w każdym x∈G
regularność pozwala wybrać
otwarte H o cl H⊂G,
a baza zawiera B z x∈B⊂H.
Normalność i lemat Urysohna
dają ciągłe funkcje g_n,
równe 1 na F_n(G) i 0 na X\G.
Jednostajnie zbieżny szereg
g_G=Σ2^-n g_n jest ciągły
i ma zbiór dodatniości
dokładnie G.

## Wystarczalność, etap 3: metryzacja

Dla B∈B_n definiujemy
f_{n,B}=2^-n g_B.
Zbiór indeksów
J={(n,B)} może być
nieprzeliczalny.
Współrzędne odwzorowania
F:X→ℓ^\infty(J) są ograniczone,
więc F jest dobrze określone.

**Ciągłość w normie supremum.**
Dla zadanych x,ε wybieramy N
tak, że 2^-N<ε/2.
Wszystkie indeksy n≥N
dają różnice funkcji
mniejsze od ε/2.
Dla skończenie wielu n<N
lokalna skończoność B_n
daje otoczenia x,
które przecinają tylko
skończenie wiele B;
poza tymi B odpowiednie
f_{n,B} są identycznie zerowe
wystarczająco blisko x.
Dla pozostałych skończenie
wielu funkcji ciągłość
daje wspólne otoczenie
z różnicami <ε/2.
Przez przecięcie skończenie
wielu otoczeń dostajemy
\|F(y)-F(x)\|_\infty<ε.
Nie zastosowano błędnego
argumentu, że
nieskończony (być może
nieprzeliczalny) zbiór
ciągłych funkcji ma
automatycznie ciągłe
odwzorowanie do ℓ^\infty.

**Iniektywność.**
Dla x≠y z T1 wybieramy
otwarty G z x∈G,y∉G.
Baza daje B∈B_n
z x∈B⊂G.
Wtedy f_{n,B}(x)>0,
f_{n,B}(y)=0,
zatem F(x)≠F(y).

**Ciągłość odwrotności.**
Dla otwartego G i x∈G
wybieramy B∈B_n
z x∈B⊂G
i δ=f_{n,B}(x)/2.
Jeżeli
\|F(y)-F(x)\|_\infty<δ,
to f_{n,B}(y)>0, więc
y∈B⊂G.
Zatem F(G) jest otwarty
w F(X), a F stanowi
homeomorfizm na podprzestrzeń
metrycznej przestrzeni
ℓ^\infty(J).
Metryka
d(x,y)=sup_{(n,B)∈J}
|f_{n,B}(x)-f_{n,B}(y)|
jest zgodna z topologią X.

## Ocena i ograniczenie zakresu

W przytoczonych krokach
nie znaleziono luki matematycznej.
Konstrukcja działa również
dla nieprzeliczalnych przestrzeni
dyskretnych i innych
przestrzeni o
nieprzeliczalnej bazie
będącej przeliczalną
sumą rodzin lokalnie skończonych.
Nie wprowadzono modyfikacji
stabilnego źródła rozdziału 15.

Jest to niezależna
**kontrola konkretnego
twierdzenia**, nie ponowny
audyt wszystkich dowodów
z rozdziału 15. Pozostałe
kontrole globalne 01–26
są nadal otwarte.
