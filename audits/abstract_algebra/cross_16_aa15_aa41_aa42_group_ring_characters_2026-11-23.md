# Algebra abstrakcyjna — audyt przekrojowy 16: AA-15 × AA-41 × AA-42

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Stan zastany:** AA-01–AA-50 zamknięte w dotychczasowych indywidualnych audytach; AA-X15 zamknięty przez zielony GitHub Actions 45196378758 (93/93 completed).

## 1. Nowy, niepokrywający się zakres

Przedmiotem nie jest powtórzenie audytu reprezentacji AA-41–AA-42 z `00-przekrojowy-audyt-01-reprezentacje-charaktery.md`, lecz niezależna weryfikacja **łączenia nieprzemiennego pierścienia grupowego AA-15 z lewymi modułami AA-41 i zespolonymi centralnymi operatorami AA-42**.

Odczytane źródła:
- `chapters/pl/abstract_algebra/15-pierscienie-nieprzemienne-i-algebry-grupowe.tex` (`b055965112ca86a86e6d0a88213a8274b9d09a68`);
- `chapters/pl/abstract_algebra/41-reprezentacje-grup-i-twierdzenie-maschkego.tex` (`05d87a9b95117069879b58e5c6ea40d71ad4a29c`);
- `chapters/pl/abstract_algebra/42-lemat-schura-charaktery-i-ortogonalnosc.tex` (`f7b662c41bf51d05c03613c879c74b9a7e30040d`).

## 2. Kontrola matematyczna

1. **Definicja algebry grupowej i moduły:** w AA-15 `R[G]` definiuje się nad przemiennym pierścieniem z jedynką dla dowolnej grupy, w AA-41 `K[G]` dla grupy skończonej nad ciałem. Są to zgodne definicje przy specjalizacji `R=K`. Działanie lewe `(Σ a_g[g])v=Σ a_gρ(g)v` respektuje kolejność mnożenia `[g][h]=[gh]`; nie podstawiano modułu prawostronnego.
2. **Własność uniwersalna:** `R[G]` wymaga centralnego obrazu pierścienia współczynników w pierścieniu docelowym. Dla `K\to End_K(V)` warunek zachodzi, więc reprezentacja `ρ:G\to GL_K(V)` przedłuża się do homomorfizmu `K[G]\to End_K(V)`. Rachunek jest zgodny z AA-41.
3. **Maschke i charakterystyka:** możliwość dzielenia przez `|G|` jest konieczna zarówno w uśrednianiu AA-41, jak i we wzorze na projektory izotypiczne AA-42; w AA-42 wszystkie współczynniki są zespolone. Nie przenosić tych operatorów bez zmian do charakterystyki dzielącej `|G|`.
4. **Projektory AA-42:** dla każdej nieprzywiedlnej reprezentacji `V_i`, `e_i=(dim V_i/|G|) Σ_g χ_i(g^{-1})[g]` jest centralnym idempotentem `C[G]`, a obraz w `End(V)` jest dokładnie `P_i`. Część `χ_i(g^{-1})=\overline{χ_i(g)}` dotyczy zespolonych reprezentacji grup skończonych. Sprawdzono na wszystkich elementach `S_3` mnożeniem w algebrze grupowej z dokładnymi współczynnikami wymiernymi.
5. **Reprezentacja regularna:** idempotenty `S_3` dają rangi `1,1,4` i sumę rang `6=|S_3|`. Jest to zgodne z `C[S_3]≅V_{triv} ⊕V_{sign} ⊕V_{std}^{⊕2}` jako lewym modułem i ze wzorem `Σ_i (dim V_i)^2=|G|`.
6. **Kontrprzykład modularny:** w `F_2[C_2]` niezerowy `u=[g]-[e]` spełnia `u²=0`; jedyna jednowymiarowa podprzestrzeń niezmiennicza dla lewego działania jest rozpięta przez `[e]+[g]`. Nie ma zatem dopełnienia niezmienniczego. Samo istnienie nilpotentu **nie wystarcza** w ogólnym pierścieniu nieprzemiennym do stwierdzenia braku półprostoty — ten logiczny warunek jest już poprawnie zaznaczony w AA-41.

**Wynik dotychczasowej kontroli merytorycznej:** w tych sześciu relacjach brak wykrytej sprzeczności. Nie przeglądano na nowo wszystkich dowodów trzech rozdziałów, a powyższy wynik tego nie sugeruje.

## 3. Trwała regresja AA-X16

Nowy plik `tools/tests/test_abstract_algebra_cross_aa15_41_42.py` zawiera **7 testów**:
1. grupa `S_3`, dokładna standardowa reprezentacja `2×2`, 36 par `(g,h)` i własność `ρ(gh)=ρ(g)ρ(h)` oraz homomorfizm algebry grupowej;
2. tabela charakterów `S_3`, ortogonalność wierszy/kolumn i `1²+1²+2²=6`;
3. centralność, idempotencja, wzajemna ortogonalność i suma `e_i=1` w `Q[S_3]`;
4. działanie `e_i` w reprezentacjach trywialnej, znaku i standardowej;
5. rangi i ślady lewego mnożenia przez `e_i` w `Q[S_3]`;
6. osobny model modularny `F_2[C_2]` i brak dopełnienia niezmienniczego;
7. zgodność etykiet i odsyłaczy źródłowych AA-15, AA-41, AA-42 (65 unikatowych etykiet; 21 odsyłaczy mających cele w tym zakresie).

Niezależne sprawdzenie arytmetyczne w wykonawczym kodzie JS potwierdziło bez błędów centralny blok: idempotencję, ortogonalność i `e_{triv}+e_{sign}+e_{std}=1` na wszystkich sześciu elementach `S_3`, z całkowitoliczbową skalą 6. Jest to **kontrola wycinka**, a nie deklaracja PASS całego testu Python.

Do `.github/workflows/abstract-algebra-chapter.yml` dodano wyzwalacz ścieżki i krok `Run AA-X16 S3 group algebra and exact representation projectors`; bramka obejmuje wszystkie dotychczasowe testy AA-01–AA-50, kompilację LaTeX oraz kontrolę PDF.

**Nowy przebieg CI:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45199128470 — status przy otwarciu raportu: `in_progress`, HEAD workflow `39b73c112661fbe686c50f0021557c8cf13ba53c`.

## 4. Granice i następne działania

- **AA-X16: W AUDYCIE.** Nie nadajemy statusu STABILNY przed zielonym CI i potwierdzeniem uruchomienia 7/7 testów.
- Rozdziały AA-15, AA-41, AA-42 pozostają niezmienione. Nie stwierdzono błędu wymagającego korekty ich źródeł.
- Jeżeli bieżące CI nie przejdzie, odczytać błąd testu, poprawić rzeczywistą przyczynę i powtórzyć CI. Nie traktować lokalnych testów arytmetycznych jako dowodu pełnego przebiegu CI.
- AA-51 nadal nieutworzony i nie jest automatycznie zakładany przez audyty przekrojowe.
