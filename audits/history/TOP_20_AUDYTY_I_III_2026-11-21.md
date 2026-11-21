# Topologia algebraiczna — TOP-20, audyty I–III

**Data:** 21 listopada 2026.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`. **Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Źródło:** `chapters/pl/algebraic_topology/20-zwartosc-i-sklejanie-trajektorii-morse-a-podstawy-analityczne.tex`.  
**Końcowy blob źródła:** `d88f4fd92a37b3d41638c6adcb3703ed44441575`, **638 wierszy**.  
**Zakres:** audyt już istniejącego rozdziału, bez dopisywania nowych twierdzeń, lematów i przykładów. Punkt wyjścia: `TOP_19_20_ITERACJA_20_2026-11-21.md`.

## Audyt I — kontrola twierdzeń, dowodów i samodzielności sformułowań

Cały rozdział ponownie przeczytano, obejmując równanie energii, zbiory graniczne, ograniczenie czasu pobytu z dala od punktów krytycznych, granice ciągów trajektorii, skończoność trajektorii sztywnych, zanik wykładniczy na rozmaitościach stabilnych, skalarny operator Greena, konstrukcję sklejania i orientacje.

Wprowadzono 10 korekt bez zmiany tez matematycznych:
- W lemacie energii dodano jawne `M,f,g,X,γ,a,b` i ich warunki.
- W lemacie czasu przebywania z dala od zer jawnie zadano `M,f,g,U,K`, `Crit(f) ⊂ U`.
- Definicja trajektorii łamanej zawiera teraz `p,q∈Crit(f)`, `ℓ≥1`, źródło pola `X` i dziedziny krzywych.
- Twierdzenie o zwartości wprost określa zwartą rozmaitość, parę `f,g`, różne punkty `p,q` oraz iloraz `M(p,q)=(W^u(p)∩W^s(q))/R`.
- Wniosek o skończoności trajektorii sztywnych zawiera wszystkie potrzebne hipotezy oraz kwantyfikatory.
- Lemat zaniku wykładniczego ma własne hipotezy dotyczące `M,f,g,q`.
- Twierdzenie o sklejaniu jawnie wprowadza `M,f,g,p,q,r`, poprawiono zgodność rodzaju gramatycznego i sformułowanie zbieżności.
- Poprawiono składnię przy „kierunku związanym z długością szyjki”.
- Usunięto przestarzały komentarz roboczy.

**Commit źródła:** `91da2953f97be008deaabfd69c1956e9eadfcaf4`.

W `application/tests/test_topology_chapters_19_20.py` dodano regresję chroniącą hipotezy, definicje, wybrane warunki operatora sklejania i obowiązującą terminologię: **commit** `dd7149c5d75a37ecfdb239bd4917b8f08f33d3bd`.

## Audyt II — ponowny rachunek i terminologia

Niezależnie sprawdzono:
- Połączenie monotoniczności `f∘γ`, skończoności punktów krytycznych i zwartości zbiorów granicznych.
- Użycie regularnych poziomów i translacji czasu w zwartości z dokładnością do trajektorii łamanych, przy jawnej zależności od teorii ODE i lokalnych rozmaitości stabilnych.
- Poprawny znak jądra dla `Q_λh` przy `λ>0` i `λ<0`, jedyność ograniczonego rozwiązania na całej prostej oraz oszacowanie `||Q_λh||∞≤||h||∞/|λ|`.
- W modelu torusa `θ'=sinθ`, `φ'=sinφ`, cztery składowe przestrzeni `M(p,r)`, parametr `s=b−a`, końce `s→±∞`, oraz gładkie jednostronne parametry `ρ+=e^{-s}` i `ρ−=e^s`.
- Bezpośrednie sprawdzenie równań ODE dla obu znaków i różnych przesunięć czasu: największy błąd różniczkowania numerycznego ok. `2.48×10^-11`; reszty tożsamości sklejania poniżej `4.45×10^-16`. Numeryczne całki energii dla czterech par przesunięć dały `4` z błędem poniżej `10^-15`, zgodnie z `f(p)−f(r)=4`.
- W ogólnym twierdzeniu odróżniono jawnie wykazaną konstrukcję przybliżonego rozwiązania od **przyjętego zewnętrznego lematu analitycznego** o jednostajnie ograniczonym prawym odwrotnym operatora linearyzacji oraz od **zewnętrznej reguły orientacji sklejania**. Nie wolno uznać obu za wyprowadzone ze skalarnego lematu Greena.

Cztery angielskie wystąpienia słowa „gluing” w zwykłej polskiej prozie oraz tytule twierdzenia zastąpiono odpowiednio „sklejaniem”; historyczne etykiety `\\label` zachowano. **Commit źródła:** `0b1157d1756ab619064c7d3bd43c882d8789f633`.

## Audyt III — struktura, PDF i kontrola CI

Ponownie pobrano końcowe źródło i niezależnie porównano etykiety z rozdziałami TOP-18 oraz TOP-19. Wyniki:
- **12 różnych etykiet**, **10 odsyłaczy**, wszystkie cele dostępne i poprawnie domknięte;
- **2 rysunki TikZ**, **0 niedomkniętych środowisk**, **0 błędów kolejności zagnieżdżania**;
- brak zakazanej terminologii i nieaktualnego komentarza roboczego;
- pełna kompilacja TOP-01–20: **236 stron**, TOP-20 strony **230–236**, wydzielony osobny PDF **7 stron**;
- obejrzano arkusz wszystkich siedmiu stron oraz stronę 235 w dużej rozdzielczości, w tym oba diagramy: bez kolizji podpisów i obciętych elementów;
- log końcowej kompilacji: **0 błędów TeX**, **0 niezdefiniowanych odsyłaczy**, **0 Overfull \\hbox**. Trzy ostrzeżenia `Underfull \\hbox` dotyczą wcześniejszych rozdziałów 11, 12, 15.

### GitHub Actions — najnowszy commit źródła `0b1157d1`

1. [TeX TOP-19–20 z zależnościami TOP-01–18](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44937075013): **completed / success**.
2. [Testy aplikacji, budowanie indeksu CLI, regresje i testy przeglądarki](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44937074933): **completed / success**.
3. [AT–DG–AG: zależności między skryptami i kompilacja AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44937074917): **completed / success**.

**Decyzja:** TOP-20 **STABILNY PO AUDYCIE III** (oprócz wcześniejszej iteracji TOP-19/20). Status matematyczny: konstrukcja sklejania ogólnego pozostaje **warunkowa względem jawnie wymienionych zewnętrznych twierdzeń analitycznych i orientacyjnych**; nie przedstawia się jej jako niezależnie wykazanej w rozdziale. Żaden nowy wynik nie został dodany. Następny rozdział: **TOP-21**. Automatyzacji nie uruchomiono.
