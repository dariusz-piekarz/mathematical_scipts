# Topologia algebraiczna — TOP-18, audyty VI–VII

**Data:** 21 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`, bez zmian w `main`.  
**Źródło:** `chapters/pl/algebraic_topology/18-homologia-morse-a-od-punktow-krytycznych-do-homologii-singular.tex`.  
**Końcowy blob źródła:** `65fd043a9535a1f99c6639bca00a9c3262b4d44f`.  
**Zakres:** audyt istniejącego rozdziału, bez dokładania twierdzeń, lematów, nowych tematów lub przykładów. Punkt wyjścia: audyty I–V, których wyniki zostały porównane z bieżącą wersją.

## Audyt VI — jawność hipotez i kwantyfikatorów

Ponownie przeczytano cały TOP-18, od lematu Morse'a do przykładu `RP²`, włącznie z dowodem `∂²=0`, lematem kilku punktów krytycznych o tej samej wartości i porównaniem kompleksu Morse'a z singularnym.

Zidentyfikowano trzy miejsca, w których twierdzenia korzystały z domyślnie ustalonego kontekstu zamiast explicite wprowadzić wszystkie obiekty:
1. Lemat Morse'a: jawnie wpisano gładką rozmaitość `M` o wymiarze `n≥0`, funkcję `f`, punkt krytyczny `p` i indeks `λ∈{0,…,n}`.
2. Lemat o energii i rozmaitościach stabilnych: jawnie wpisano zwartość, bezbrzegowość, funkcję Morse'a, metrykę, przepływ ujemnego gradientu, `p∈Crit(f)` i założenia `p,q∈Crit(f)` w tezie o ścisłym spadku wartości.
3. Stwierdzenie o wymiarze przestrzeni trajektorii: jawnie wpisano parę Morse'a–Smale'a, różne punkty krytyczne `p,q` i definicję ilorazu `M(p,q)=(W^u(p)∩W^s(q))/R`.

Poprawki nie zmieniły treści matematycznej wyników ani sposobu ich dowodzenia. **Commit źródła:** `ba6105c301763a322f119bb18d1d70c0fb3d119d`.

Do `application/tests/test_topology_chapters_17_18.py` dodano test chroniący samodzielność tych sformułowań (**commit** `1fb8f03f500c27c56e79e701834178e1007d4868`).

Podczas testu po zapisie wykryto błąd domknięcia `\\end{lemat>` wprowadzony podczas edycji; poprawiono go jeszcze przed zatwierdzeniem statusu stabilnego (**commit** `2f0730ed916dac2be73062d457c9ad752d5b5005`). Przebiegi CI dla przejściowej wadliwej wersji odnotowały błąd, a najnowsze pełne testy już go nie wykazują.

## Audyt VII — niezależne ponowne sprawdzenie

- **695 wierszy**, **13 różnych etykiet LaTeX**, **6 poprawnie domkniętych odsyłaczy**.
- **36 par** otwartych i zamkniętych środowisk, poprawna kolejność zagnieżdżenia, brak niedomkniętych `\\begin` i `\\end`.
- Dwa lokalne diagramy TikZ zachowane. Przejrzano wszystkie **8 stron** PDF kontrolnego oraz schemat przepływu na okręgu i kompleks łańcuchowy `RP²`.
- Sprawdzono, że wartości własne macierzy hesjanu wyznaczają indeks i że dopełnienie Schura w dowodzie lematu Morse'a ma właściwe znaki.
- Sprawdzono przekrój `f=c` działania translacji na nietrywialnych trajektoriach i wymiar `λ(p)−λ(q)−1`.
- Różniczka Morse'a: znak liczby trajektorii, jej niezależność (na poziomie homologii) od zmiany orientacji generatorów oraz argument `∂²=0` z sumy znaków punktów brzegowych zwartej zorientowanej jednowymiarowej rozmaitości.
- Zależności analityczne pozostawiono jawnie: twierdzenie o rozmaitościach stabilnych, kompaktyfikacja i sklejanie trajektorii, zgodność liczb incydencji z różniczką komórkową, teoria uchwytów i konstrukcja kontynuacji. Nie przedstawiono tych głębokich twierdzeń jako samodzielnie udowodnionych na podstawie samego oszacowania energii.
- Sprawdzono kilka punktów krytycznych o wspólnej wartości, skrajne przypadki `k=0,n` oraz identyfikację różniczki komórkowej z liczeniem trajektorii.
- Zachowano rachunek `RP²`: punkty krytyczne indeksów 0,1,2; `n(p₂,p₁)=−2` po zadaniu orientacji, `n(p₁,p₀)=0`, w konsekwencji `H_1(RP²;Z)=Z/2Z`.
- Silne nierówności Morse'a: przeliczenie `m_k=b_k+r_k+r_{k+1}` nad `Q`, rozdzielenie homologii całkowitej od wymiernej, charakterystyka Eulera oraz trzy przykłady.
- Kontrola terminologii: bez nieuzasadnionych anglicyzmów ani zakazanych polskich wariantów.
- Do dalszych zmian w dotychczasowej treści matematycznej nie znaleziono przesłanek.

## Weryfikacja GitHub Actions po końcowym commicie `2f0730ed`

1. [TeX TOP-01–18: dwie kompilacje i kontrola odsyłaczy](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935201417): **completed / success**.
2. [Aplikacja, indeksowanie i testy regresyjne](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935201402): **completed / success**.
3. [AT–DG–AG: kontrola etykiet i zależności](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935201422): **completed / success**.
4. [AT18–DG18: porównanie homologii Morse'a, uchwytów i grafu Reeba](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44935201395): **completed / success**, oba zadania (AT i DG).

Końcowa kompilacja TOP-01–18 wygenerowała **221 stron**; TOP-18 obejmuje strony **214–221** i udostępniono go również jako osobny, ośmiostronicowy PDF. Log drugiego przebiegu nie wykazuje przepełnień `Overfull hbox` ani nierozwiązanych odsyłaczy. **Nie** jest to weryfikacja pełnej 31-rozdziałowej książki.

**Decyzja:** TOP-18 **STABILNY PO AUDYCIE VII**. Wcześniejsze pięć audytów zachowuje ważność, poprawki i raport są na dotychczasowej gałęzi. Następny rozdział do niezależnej ponownej kontroli: TOP-19. Automatyzacje pozostają wyłączone.
