# Topologia ogólna — rozdział 26, audyt 07 (pierwszy czysty na nowym blobie)

**Data:** 2026-11-22.
**Źródło:** `chapters/pl/general_topology/26-twierdzenie-hahna-mazurkiewicza.tex`.
**Blob:** `161d04d779ae86554f81c11bb24daa842c8dd363`.
**Wynik:** CZYSTY 1/2. Źródła nie zmieniono.

## Niezależna kontrola dowodu konstrukcyjnego

1. Dla dowolnego ε>0 lokalna spójność
   daje spójne otwarte V_x
   w kulach promienia ε/3.
   Zwartość umożliwia wybór
   skończonego podpokrycia
   B(x_i,r_i) i δ=min r_i.
   Każda para odległa o mniej niż δ
   mieści się we wspólnym V_{x_i}
   o średnicy <ε.
2. Spójny zbiór metryczny
   ma dla każdej δ>0
   tylko jedną klasę osiągalności
   przez skończone δ-łańcuchy.
   Klasy są otwarto-domknięte,
   co dowodzi istnienia łańcucha
   bez założenia spójności drogowej.
3. Rekurencja małych dróg
   zachowuje stare końce i
   na poziomie n dzieli
   każdy odcinek w co najmniej dwie
   części. Nowe wierzchołki
   leżą w spójnym zbiorze
   o średnicy <ε_n,
   więc błąd w zagnieżdżonym
   odcinku jest kontrolowany
   przez ogony S_n=Σ_{k≥n}ε_k.
   Dla dostatecznie bliskich
   parametrów odległość wartości
   jest ≤4S_n. Powstaje
   jednostajnie ciągła funkcja
   na zbiorze gęstym w [0,1].
4. Zwartość metryczna daje
   zupełność, a ta zapewnia
   ciągłe przedłużenie
   do całego [0,1].
   Zachowano wartości końcowe;
   średnica drogi jest
   ≤2S_0<η.
5. Z małych dróg wynika
   otwartość składowych
   drogowych w każdym
   zbiorze otwartym.
   Rozdział 08 daje
   lokalną spójność drogową,
   a spójność X daje
   spójność drogową X.
6. Skończenie wiele celów
   nowej δ_{n+1}/2-sieci
   jest osiągane przez
   krótkie pętle o wspólnych
   końcach h(t_i).
   Grupy jednakowych t_i
   są obsłużone na jednym
   krótkim przedziale,
   a odległość nowej i starej
   drogi jest <2ε_n.
7. Krzywe f_n mają
   δ_n/2-gęste obrazy
   oraz spełniają
   \(\sup d(f_{n+1},f_n)\le2ε_n\).
   Szereg ε_n jest zbieżny,
   więc granica f istnieje
   jednostajnie i jest ciągła.
   Dla każdego x∈X odległość
   od f([0,1]) jest ograniczona
   przez δ_n/2+sumę ogonową,
   a ta dąży do 0.
   Obraz f([0,1]) jest
   zwarty i domknięty,
   czyli równy X.

## Zmiany wydawnicze

Względem audytów 04–05
nie zmieniono żadnej części
powyższych dowodów.
Usunięto wyłącznie
powtórzony przykład grafów
i sześcianów, obecny wcześniej
w stabilnym rozdziale 25.
Zachowano wszystkie etykiety
wyników potrzebne w dalszej książce.
Sprawdzono 22 unikatowe etykiety,
19 odsyłaczy i 9 poprawnie
zamkniętych środowisk proof.

**Wynik:** czysty 1/2 na blobie 161d04d779.
Kontrola PDF oraz kolejny niezależny
audyt są jeszcze wymagane.
