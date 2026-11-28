# Topologia algebraiczna — TOP-17, audyty V–VII

**Data:** 21 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`, bez modyfikacji `main`.  
**Rozdział:** `chapters/pl/algebraic_topology/17-konstrukcja-pontriagina-thoma-i-podstawy-teorii-kobordyzmow.tex`.  
**Źródło końcowe:** blob `cfbbf82ad7a787d39cb1885cb0e98b40a18a94c1`, commit `12f9db2d4c870d5df0ccbd4324a63a21f099bab0`.  
**Tryb:** audyt już istniejącego materiału, bez nowych twierdzeń i lematów; względem archiwalnych audytów I–IV.

## Audyt V — ponowna lektura i niepoprawna fleksja

Zbadano kolejno: wartość regularną, uramowanie wiązki normalnej, przestrzeń Thoma, odwzorowanie ściągające, bijekcję Pontriagina–Thoma w ustalonym kowymiarze, stabilizację oraz opis `MO` i `MSO`. Porównano przykłady z wcześniejszymi audytami i zachowano wszystkie ich etykiety.

W tekście nadal znajdowały się błędne formy wynikające z automatycznej zmiany rzeczownika „mapa” na „odwzorowanie”: `odwzorowańę`, `odwzorowańą`, `otrzymana odwzorowanie`, `przybliżona odwzorowanie`. Usunięto błędy fleksyjne i dostosowano składnię w szesnastu miejscach. Doprecyzowano w szczególności, że w konstrukcji zorientowanej **przestrzenią docelową** jest `MSO(k)`, a w lemacie aproksymacyjnym **odwzorowanie** pozostaje niezmienione poza wybranym otoczeniem, w szczególności w punkcie bazowym.

**Commit źródła:** `d07475e07ef7bd732fc369d3cd9005b7ed1c1eff`.

Do `application/tests/test_topology_chapters_17_18.py` dodano regresję zakazującą wadliwych form i kontrolującą kluczowe poprawione zwroty. **Commit testów:** `8a04152bce9713e445737aead3065eb82a444335`.

## Audyt VI — rysunek otoczenia tubularnego

W lemacie istnieje otwarte otoczenie `U` z domknięciem modelowanym przez domkniętą wiązkę dysków. Dotychczasowy diagram podpisywał bezpośrednio `U ≅ D(ν)`, co nie odróżniało otwartego wnętrza od domkniętej wiązki. Zmieniono podpis rysunku na `\\overline U ≅ D(ν)`, zgodnie z tekstową konstrukcją. Nie zmieniono tezy lematu ani zależności od twierdzenia o otoczeniach tubularnych.

**Commit źródła:** `12f9db2d4c870d5df0ccbd4324a63a21f099bab0`.

## Audyt VII — niezależna kontrola matematyczna, strukturalna i wizualna

Sprawdzono ponownie:
- przedziały wymiarowe `n≥0`, `k≥1` i przypadek `k>m` w twierdzeniu o zerach przekroju;
- zgodność konwencji orientacji normalnej z klasyfikacją przez `MSO`, bez utożsamiania orientacji z uramowaniem;
- sformułowanie granicy prostej `π_{n+k}(MO(k))` i analogicznej dla `MSO`;
- dowód `Ω_2^O≅Z/2` z klasyfikacji powierzchni i niezmiennika Eulera modulo 2;
- rachunki `w_2^2=w_4=a^2b^2` dla `RP²×RP²` oraz `(w_2²,w_4)=(0,1)` dla `RP⁴`, co daje dwa niezależne elementy rzędu 2 bez wyciągania nieuprawnionego wniosku o całej grupie `Ω_4^O`;
- jawne wskazanie użycia wyników zewnętrznych: Whitneya, Ehresmanna, względnej transwersalności, konstrukcji otoczeń tubularnych, klasyfikacji powierzchni i wyników Thoma;
- strukturalnie **1021 wierszy, 18 unikalnych etykiet, 10 domkniętych odsyłaczy, dwa diagramy TikZ, zero niedomkniętych środowisk, zero błędnych form fleksyjnych**.

PDF po CI zawiera **221 stron** z rozdziałami 01–18, zaś TOP-17 zajmuje **11 stron**, strony książki 203–213. Wydzielono go jako osobny PDF. Obejrzano arkusz wszystkich 11 stron oraz w większej skali strony 204 i 210 z diagramami. W obu schematach nie wykryto kolizji podpisów ani elementów wychodzących poza stronę. Log drugiej kompilacji nie zawiera przepełnionych `Overfull hbox`, błędów TeX ani nierozwiązanych odsyłaczy; w całym 221-stronicowym dokumencie występują trzy ostrzeżenia `Underfull hbox`, z wcześniejszych rozdziałów, bez związku z TOP-17.

### Końcowe kontrole GitHub Actions (źródło `12f9db2d`)

1. [Kompilacja TeX TOP-01–18](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934374461): **completed / success**.
2. [AT17–DG19: kobordyzmy i uchwyty, kompilacja i porównanie](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934374358): **completed / success**.
3. [Testy aplikacji i regresji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934374364): **completed / success**.
4. [AT–DG–AG: kontrola etykiet i zależności](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934374361): **completed / success**.

**Decyzja:** **TOP-17 stabilny po audycie VII**, poprawki i regresje zapisane na dotychczasowej gałęzi, bez rozszerzania teorii. Następny rozdział do niezależnej ponownej kontroli: TOP-18, dla którego istnieje archiwalny cykl audytów I–V.
