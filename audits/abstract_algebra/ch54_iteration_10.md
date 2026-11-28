# AA-54 — audyt X: wspólne regresje i weryfikacja propozycji algebr Jacobiego

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło AA-54: blob b6ab66f51c6275b75758f17409d2d27894279d38, bez zmian.

## Wykonana kontrola dodatkowa
W kontenerze uruchomiono Python/SymPy, dokładne obliczenia nad QQ, porządek leksykograficzny X>Y>Z. Dla trzech znormalizowanych równań powierzchni wyznaczono bazy Gröbnera ideałów pochodnych i normalne monomy:
- E6: X²+Y³+Z⁴, baza Gröbnera X,Y²,Z³; monomy 1,Z,Z²,Y,YZ,YZ²; wymiar 6.
- E7: X²+Y³+YZ³, baza X,Y²+Z³/3,YZ²,Z⁵; monomy 1,Z,Z²,Z³,Z⁴,Y,YZ; wymiar 7.
- E8: X²+Y³+Z⁵, baza X,Y²,Z⁴; monomy 1,Z,Z²,Z³,Y,YZ,YZ²,YZ³; wymiar 8.
We wszystkich przypadkach sprawdzono zero-wymiarowość ideału, liczbę normalnych monomów, przynależność odpowiednich potęg zmiennych do ideału oraz redukcję wielomianu definiującego do zera. Niezależnie potwierdzono ważoną tożsamość Eulera sum(w_i X_i ∂_i f)=d f dla wag (12,8,6), (18,12,8), (30,20,12) i stopni 24,36,60. Stąd ideał Tjuriny (f,∂f) jest równy ideałowi Jacobiego, a z uwagi na jedyny punkt krytyczny w początku wymiar algebry lokalnej pokrywa się z obliczonym wymiarem globalnym. Liczby Milnora i Tjuriny 6,7,8. Wszystkie trzy zestawy asercji zakończone pomyślnie, proces exit 0. To weryfikacja propozycji rozszerzenia z audytu IV; nie dodano materiału do rozdziału bez zatwierdzenia zakresu.

## CI
Run 45353008192, job 138303851854, commit 6f6d1c0c902b3abe081613b5a81f3b43f12f6fd3: in_progress, conclusion brak, kroki {"success":41,"in_progress":1,"pending":75}. Wspólny zestaw Run repository tool tests: success. Artefakty: brak. Nie potwierdzono oględzin nowego PDF.

## Werdykt
Dwa czyste audyty matematyczne III–IV pozostają ważne. X jest kontrolą techniczną i weryfikacją propozycji, nie zmianą zatwierdzonego zakresu. AA-54 W AUDYCIE do pełnego CI i oględzin aktualnego PDF. AA-55 nieotwarty.
