# Topologia algebraiczna — TOP-17, audyty stabilizacyjne I–IV

**Data:** 21 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`; bez aktualizacji `main`.  
**Rozdział:** `chapters/pl/algebraic_topology/17-konstrukcja-pontriagina-thoma-i-podstawy-teorii-kobordyzmow.tex`.  
**Źródło końcowe:** blob `1eb91926f588918e884ad76e8922d32e9b2ca22e`, 1021 wierszy.  
**Zasada:** kontrola istniejącego materiału i poprawki bez wprowadzania nowych twierdzeń, lematów czy podrozdziałów.

## Audyt I — pełna kontrola matematyczna i konstrukcja Pontriagina–Thoma

Przeczytano cały rozdział i wcześniejszy raport `TOP_17_18_ITERACJA_19_2026-11-21.md`. Skontrolowano: wyznaczanie uramowania normalnego przez różniczkę regularnej wartości, przestrzenie i klasy Thoma, konstrukcję ściągającą, obie strony bijekcji Pontriagina–Thoma, jej zgodność z zawieszeniem, odpowiadanie uramowanego kobordyzmu stabilnym grupom homotopii, dualność Poincarégo i klasę Eulera, strukturę pierścieni kobordyzmu, rachunki dla torusa i butelki Kleina, liczby Stiefela–Whitneya i Pontriagina, obliczenie Ω₂ᴼ oraz modele widm MO i MSO. Zachowano twierdzenia, przykłady i diagramy.

Uściślono etap, w którym `Q_+` jest zastępowane przez sferę z wyróżnionym punktem nieskończoności. Mapa ściągająca wysyła zarówno dodany rozłączny punkt, jak i `∞`, na punkt bazowy, toteż przechodzi przez iloraz utożsamiający te dwa punkty. Tym samym otrzymujemy **punktowane** odwzorowanie `S^{n+k}→S^k`, a nie tylko mapę z `Q_+`.

W przejściu od homotopii odwzorowań do uramowanego kobordyzmu doprecyzowano względną aproksymację i transwersalność **z ustalonymi kołnierzami obu końców oraz otoczeniem `{∞}×[0,1]`**, co zapewnia produktową strukturę normalną przy brzegu otrzymanego kobordyzmu. Usunięto archiwalny komentarz „Iteracja X”.

**Commit:** `f4bfd1b1f03f788fdcc7e310a2b1b5c9efa5fc67`.

## Audyt II — kwantyfikatory, przestrzeń Thoma i puste zbiory zer

W samodzielnych sformułowaniach lematów i definicji dopisano jawne hipotezy `n≥0`, `k≥1` oraz zamieniono niepoprawny zwrot „odpowiednio wiązkę dysków” na precyzyjne nazwy obu wiązek.

W twierdzeniu o klasie Thoma i dualności Poincarégo przyjęto jawnie `m≥1`, `1≤k≤m`. W twierdzeniu o zerach przekroju **rozdzielono dwa przypadki**: dla `k≤m` przeciwobraz zerowy jest gładką podrozmaitością kowymiaru `k` i reprezentuje dualną Poincarégo do klasy Eulera; dla `k>m` transwersalny zbiór zer jest pusty, a klasa Eulera zanika ze względów wymiarowych. Bez tego rozróżnienia zdanie o „podrozmaitości wymiaru `m−k`” mogłoby wprowadzać ujemny wymiar.

Rozbudowano regresje o rachunek klas `w(T RPⁿ)=(1+t)^{n+1}` w wymiarach 1–32, kontrolę parzystości Eulera i faktyczne obliczenie `(w₂²,w₄)` dla `RP⁴` i `RP²×RP²` z wielomianów nad `F₂`, bez tautologicznych porównań wpisanych wyników.

**Commity:** `438bcd4ae5aba5b8a317ef1d607d549d5a4ed390`, `c96bf59e2a6e9b49f0a4801b6e2907ee292589ff`.

## Audyt III — terminologia, testy regresji i odsyłacze

Ujednolicono w całym rozdziale polską terminologię `odwzorowanie`, `odwzorowanie klasyfikujące`, `odwzorowanie ściągające`, `odwzorowania przejścia` zamiast potocznego słowa „mapa” w znaczeniu matematycznym. Nie zmieniono nazw istniejących etykiet ani oznaczeń `MO`, `MSO`.

Dodano regresje w `application/tests/test_topology_chapters_17_18.py` sprawdzające:
- punktowane przejście `Q_+→S^{n+k}` i kołnierze względnej transwersalności;
- przypadki wymiarowe klasy Eulera;
- terminologię całego TOP-17;
- pełne i jednowierszowo domknięte odsyłacze w TOP-17 i TOP-18;
- rachunki liczb Stiefela–Whitneya, różnicujące `RP⁴` i `RP²×RP²`.

**Commity:** `4688d77edc7e0a5f30b36198c9c87cd1d97e3b56`, `340e7b5a21551c4b3f0052d80732af3ca1ae5f8b`, `95a1cf38eb2649bbc339b16ee249b0d40d6e843c`.

## Audyt IV — niezależna lektura ostatniej wersji

Ponownie pobrano źródło i testy z GitHuba po ostatniej poprawce. Wyniki:
- **1021 wierszy** źródła.
- **18 etykiet LaTeX, wszystkie unikalne**, 10 poprawnych, jednowierszowych odsyłaczy; wszystkie cele zdefiniowano w rozdziale.
- **2 diagramy TikZ** zachowane.
- Wszystkie środowiska `\begin{...}` / `\end{...}` właściwie zagnieżdżone i domknięte.
- Brak zabronionej terminologii „mapa”, „tensorowanie”, „sekwencja”, „injekcja” oraz nieaktualnych komentarzy iteracyjnych.
- Zależności od głębokich wyników (Whitney, Ehresmann, otoczenia tubularne, transwersalność względna, klasyfikacja powierzchni, twierdzenie Thoma) są jawnie wskazane i nie są przedstawione jako udowodnione niezależnie w TOP-17.
- Wcześniejsze rozbieżności między źródłami GitHub i Biblioteki zostały zrekoncyliowane w iteracji 19; aktualny audyt nie usuwa treści historycznej.

## Kontrole GitHub Actions

Przebiegi wcześniejszego commita źródłowego `438bcd4a`:
- [Kompilacja LaTeX TOP-01–18](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932018851) — **success**.
- [Testy aplikacji i regresji](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932018840) — **success**.
- [Kontrola międzytomowa AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932018875) — **success**.

Końcowe przebiegi po zmianach źródła (`340e7b5a`) i dodatkowych regresjach (`95a1cf38`):
- [Kompilacja TOP-01–18 z nowymi regresjami](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932121133) — **completed / success**, commit `95a1cf38` (źródło niezmienione od `340e7b5a`).
- [Testy aplikacji i nowa regresja TOP-17](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932120969) — **completed / success**, commit `95a1cf38`.
- [Audyt zależności AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932089693) — **completed / success**, commit źródłowy `340e7b5a`.
- [Specjalny audyt TOP-17 ↔ DG-19, porównanie dowodów i kompilacja obu książek](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44932089662) — **completed / success** w obu zadaniach: pełny kontekst AT-01–30 i DG-01–20. Commit źródłowy `340e7b5a`.

**Decyzja końcowa:** **TOP-17 stabilny po audycie IV**, bez nowych twierdzeń czy lematów, 18 etykiet i dwa diagramy bez naruszeń, wszystkie istotne CI zakończone sukcesem. Następnym rozdziałem do stabilizacji jest TOP-18. Nie włączono automatyzacji.
