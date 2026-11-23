# Teoria grafów i węzłów — audyt globalny 19: rozdziały 22–24, drugie przejście

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.  
Kontynuacja [audytu 18](39-globalny-audyt-18-rozdzialy-22-24-pierwsze-przejscie.md).
Przedmiot: ponowna, niezależna kontrola historycznych rozdziałów 22, 23 i 24.

## Zakres szczegółowej rewizji

Ponownie sprawdzono: konstrukcję uchwytów indeksu dwa,
formę przecięcia i macierz całkowitej chirurgii,
metabolizery i nierówność Murasugiego,
Foxa–Milnora, rozdzielenie kategorii TOP/DIFF,
plumbing ujemny, rekurencje krat `A_n,D_n,E_8`,
formę splecenia torsyjnego, twierdzenia
Donaldsona i Freedmana, prezentacje grup
Seiferta, dopełnienia Schura, jądra
macierzy i pierwsze homologie.

Kontrola zwraca szczególną uwagę
na **różnicę pomiędzy zmianą bazy nad `R`/`Q`
a zmianą unimodularną nad `Z`**.
Pierwsza zachowuje bezwładność i rząd,
ale nie wyznacza samodzielnie torsji
całkowitej grupy `coker Q`.

## Rozdział 22 — użycie obstrukcji sygnaturowej

Dodano szczegółowy przykład
`ex:kt-trefoil-four-genus-signature`.
Dla standardowej symetryzacji formy
Seiferta prawoskrętnego trójlistnika,
`V+V^T=[[2,-1],[-1,2]]`,
wartości własne to `1,3`;
zatem `|σ(T)|=2`.
Nierówność Murasugiego z wcześniejszego
lematu izotropowego daje
`g4^sm(T)≥1`, a zwykła powierzchnia
Seiferta rodzaju jeden daje
`g4^sm(T)≤1`. Stąd `g4^sm(T)=1`
i trójlistnik nie jest gładko slice.
Przykład pokazuje, co wynika z elementarnej
obstrukcji oraz które wyniki dla ogólnych
węzłów torusowych wymagają twierdzeń
zaawansowanych.

Granica dowodu jest jawna:
istnienie podprzestrzeni izotropowej
pochodzącej z powierzchni w `B^4`
pozostaje klasycznym lematem Murasugiego,
którego nie utożsamia się z samodzielnym
rachunkiem wartości własnych.

## Rozdział 23 — forma splecenia łańcuchów i orientacje E8

Dodano stwierdzenie i dowód
`st:tg-plumbing-An-linking`.
Dla ujemnie określonego łańcucha
`A_n` z wagami `-2`,
z generatorem `x=[x1]` brzegu
`H1(∂P_{A_n})≅Z/(n+1)Z`,
otrzymano
`(Q_{A_n}^{-1})_11=−n/(n+1)`;
w konsekwencji przy przyjętej
orientacji brzegu
`λ(x,x)=n/(n+1) mod Z`.
Sprawdzono jawnie `n=1,2,3`;
wyniki to `1/2,2/3,3/4`.
Dowód używa dopełnienia
algebraicznego i determinantów
`det Q_{A_n}=(-1)^n(n+1)`.
Nie pomija znaku wynikającego
z `λ=-Q^{-1} mod Z`.

W dowodzie nieistnienia gładkiego
kontraktywnego wypełnienia sfery
homologicznej Poincarégo
dodano **brakujący krok orientacyjny**:
po wykazaniu, że nie istnieje
gładka kontraktywna rozmaitość
o brzegu `-Y`, odwrócenie
orientacji ewentualnego wypełnienia
`Y` daje zakazane wypełnienie
`-Y`. Dlatego sprzeczność
z twierdzeniem Donaldsona dotyczy
obu orientacji, a nie jedynie
orientacji wynikającej z
ujemnego plumbingowania.

Wciąż jasno odróżnia się:
- gładkie plumbingowanie `P_{E8}`
  z **niepustym brzegiem**;
- topologiczne kontraktywne wypełnienie
  brzegu o przeciwnej orientacji
  (zewnętrzny wynik Freedmana);
- zamkniętą topologiczną
  czterorozmaitość o formie `-E8`,
  która nie może być gładka
  (zewnętrzny wynik Donaldsona).

## Rozdział 24 — jądro macierzy i torsja Seiferta

Dodano samodzielne stwierdzenie
`cor:tg-star-nullspace-boundary`
dla ważonego drzewa gwiaździstego
o `N=1+Σk_i` wierzchołkach.
Gdy `s=b+Σβ_i/α_i=0`,
macierz przecięcia po rozdzieleniu
centrum od ramion ma postać
`Q=[[A,v],[vᵀ,b]]`.
Z równości `Ay+vc=0`
wynika `y=−A^{-1}vc`;
druga relacja redukuje się do
`s c=0` i jest w tym
przypadku tożsamością.
Dlatego
`ker_Q(Q)=Q·(-A^{-1}v,1)`
ma wymiar jeden, a po
sprowadzeniu do pierwotnego
wektora całkowitego
`ker_Z(Q)≅Z`.
Z twierdzenia o brzegu
plumbingowania otrzymujemy
`H2(∂P_Γ;Z)≅Z`.

Dodano niezależny przykład
`ex:tg-star-zero-e-kernel`:
macierz z centrum o wadze `-1`
i trzema liśćmi o wadze `-3`
ma pierwotny wektor jądra
`(3,1,1,1)`.
Dla tego samego brzegu
`H1(∂P_Γ;Z)≅Z⊕Z/3Z`.
Obecność torsji pomimo istnienia
jednowymiarowego jądra wyjaśnia,
dlaczego z samej `R`-kongruencji
do `diag(A,s)` nie wolno
wyciągać wniosków o całkowitej
postaci Smitha.

## Niezależne nowe testy

Rozszerzono
`tools/tests/test_graph_and_knot_four_dim_plumbing_seifert.py`
o **trzy nowe rodziny**:

- **60** kontroli formy splecenia
  brzegu `A_n` dla `1≤n≤20`,
  z niezależnym rozwiązaniem
  układów liniowych nad `Q`
  metodą Gaussa–Jordana i
  weryfikacją niezmienniczości
  klasy modulo `Z`;
- **5** przykładów zerowej
  wymiernej liczby Eulera z
  ramionami `(3,3,3)`,
  `(2,3,6)`, `(2,4,4)`,
  `(2,2)`, `(2,2,2,2)`:
  weryfikacja wymiernego
  warunku `s=0`,
  pierwotnych wektorów jądra
  i porównanie gcd maksymalnych
  minorów dwóch **różnych**
  prezentacji całkowitych;
- **24** sprawdzenia dodatniej
  określoności macierzy
  symetryzacji trójlistnika
  dla niezerowych wektorów
  o współrzędnych od `−2` do `2`,
  oraz rachunku sygnatury.

Łącznie **89 dodatkowych przypadków**,
co razem z poprzednimi **66 778**
daje **66 867** dokładnych testów
w dziesięciu grupach wykonania.
Podczas testowania wykryto i
poprawiono **rzeczywisty błąd
oczekiwanej wartości**:
dla gwiazdy z czterema ramionami
o wagach `−2` i centralnym
wierzchołku o wadze `−2`
rząd torsji wynosi `4`,
a nie `8`. Poprawka została
potwierdzona niezależnymi
maksymalnymi minorami
i porównaniem z macierzą Seiferta.

Wyniki te dotyczą konkretnych
skończonych rachunków, a nie
poświadczenia dowodów twierdzeń
Freedmana czy Donaldsona.

## Kontrola strukturalna

W przebiegu
[GitHub Actions 45210934282](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45210934282)
`structural-audit=success`:
`44/44` pliki rozdziałowe,
`0` duplikatów etykiet,
`0` niezwiązanych odsyłaczy,
`0` błędów środowisk i
`0` terminów zakazanych.
Wszystkie **66 867** przypadków
nowego testu zakończyły się sukcesem.

## Status końcowej stabilizacji

Pozostało potwierdzić po ostatnim
commicie źródłowym:
pełną trzykrotną kompilację
44-rozdziałowego PDF,
zero ostrzeżeń, wizualną inspekcję
rozdziałów 22–24 i ich
nowych wzorów oraz rysunków.
Dopiero po tych bramkach
można uznać blok 22–24
za **lokalnie stabilny**.
Globalny audyt wszystkich
44 rozdziałów pozostaje otwarty.
