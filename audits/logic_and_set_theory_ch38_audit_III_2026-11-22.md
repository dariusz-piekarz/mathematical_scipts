# Logika matematyczna i teoria mnogości — audyt III rozdziału 38

**Data:** 22 listopada 2026 r.  
**Źródło:** chapters/pl/logic_and_set_theory/38-kardynaly-mahla-i-slaba-zwartosc.tex.  
**Blob:** d0d176bf1d4cbb8426cedcf02fbbd3a28510a152, niezmieniony od audytów I i II.  
**Werdykt matematyczno-redakcyjny:** czysty. Kandydat na **drugi czysty audyt (2/2)** po ukończonym CI.

## 1. Odwrócony audyt implikacji od wniosków do założeń

**Mierzalny ⇒ słabo zwarty.** W kroku końcowym użyto faktu, że wybrany zbiór węzłów s_α ma element na każdym poziomie α<κ i jest łańcuchem. Aby wykazać istnienie s_α, nie wystarczyłaby elementarność j sama w sobie: konieczny jest fakt |T_α|<κ, który daje j(T_α)=j obraz elementów T_α. Wymaga to oddzielnego lematu o małych zbiorach i ustalenia j(α)=α. Węzeł t na poziomie κ istnieje z wysokości j(κ)>κ; elementarność i definicja wysokości drzewa uzasadniają poprzednika na każdym mniejszym poziomie. Dowód nie przyjmuje właściwości drzewa dla κ jako ukrytej przesłanki.

**Mierzalny ⇒ Mahlo.** Krok Iκ∈W wynika z κ∈j(Iκ); jego uzasadnienie wymaga zarówno elementarności j, jak i nieosiągalności κ w M. Przeanalizowano potencjalną różnicę P^M(λ) od P^V(λ): iniekcja κ→P^M(λ) w M byłaby nadal iniekcją do P^V(λ) w V, więc silna graniczność w V ją wyklucza. Regularność i kardynalność κ w M dziedziczą te same negatywne argumenty. Z drugiej strony sama przynależność Iκ do W nie wystarczyłaby bez wiedzy, że każdy klub należy do W. Lemat o klubach wykorzystuje pełną normalność W, a nie tylko jej niegłówność.

**Mierzalny ⇒ relacja podziałowa.** Dla każdego α ogon nad α jest U-duży i rozpada się na dwa rozłączne B_{α,i}. Dokładnie jedna część należy do ultrafiltru. W dalszym kroku dobór jednego i jest uzasadniony decyzją ultrafiltru dla podziału na zbiory X_0 i X_1. Konstrukcja indeksowana ξ<κ korzysta z κ-zupełności przy każdej liczbie wybranych dotąd indeksów; nie stosuje κ-zupełności do przecięcia rodziny o długości κ. Uniformność U zapewnia nieograniczoność i możliwość następnego wyboru. Dowód nie wymaga normalności, co stanowi istotne rozróżnienie.

## 2. Ponowna kontrola schematu Fodora

Przy zaprzeczeniu stacjonarności wszystkich włókien funkcji regresywnej otrzymujemy rodzinę klubów Cξ, z której diagonalne przecięcie jest klubem. Uzasadnienie nieograniczoności przecięcia diagonalnego korzysta z wyboru γ_{n+1} ponad γ_n we wspólnym przecięciu rodziny indeksowanej ξ≤γ_n, liczącej <κ elementów. Regularność κ zapewnia sup_nγ_n<κ. Dla ξ<sup_nγ_n istnieje N, od którego wszystkie późniejsze γ_{n+1} należą do Cξ; domknięcie daje żądany punkt.

Osobno kontrolowano przypadek funkcji regresywnej na S zawierającym 0: usunięcie 0 zachowuje stacjonarność, gdyż zbiór wszystkich α>0 zawiera klubowy ogon. Definicja nie żąda nieistniejącego warunku f(0)<0.

## 3. Kontrola terminologii i pliku

Źródło nadal ma 641 wierszy, 26 unikalnych etykiet, 19 odsyłaczy, 8 definicji, 4 lematy, 5 twierdzeń, 1 wniosek, 5 uwag, 2 przykłady i 10 dowodów. Sparowanie środowisk jest poprawne. Nie wykryto niepożądanych zwrotów terminologicznych ani niedostatecznie sformułowanych hipotez.

**Zielony CI po poprawce testu:** [45068706353](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068706353). Pobrano jego rzeczywisty artefakt 14772308141: pełna książka ma 331 stron A4; rozdział 38 obejmuje strony PDF 327–331. Wszystkie pięć stron wyrenderowano i obejrzano w układzie kontaktowym; brak obciętych wzorów i kolizji. Log: 0 błędów LaTeX, 0 overfull, 0 niezdefiniowanych referencji i 0 brakujących znaków; jedno underfull w całej książce.

## 4. Werdykt i następny etap

**Audyt III matematycznie czysty, bez edycji źródła.** Po ukończeniu CI dla audytu II i III można zaliczyć 2/2 czyste audyty. Dodatkowy audyt IV musi potwierdzić stabilność na identycznym blobie. Poprawność Python i LaTeX nie stanowi dowodu w Lean.
