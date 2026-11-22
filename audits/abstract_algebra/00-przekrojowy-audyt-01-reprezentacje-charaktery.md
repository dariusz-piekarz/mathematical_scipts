# AA — audyt przekrojowy 01: zgodność teorii reprezentacji (AA-41–AA-42)

Data: 2026-11-23. Rodzaj: **nowa kontrola przekrojowa**, nie audyt nowego rozdziału ani kolejna iteracja stabilizacyjna AA-42.

## Baza źródłowa
- HEAD odczytany bezpośrednio przed zapisem: `ef71d9d89f4b482f5de371be1c9241b3fc4a507d`.
- AA-41: `chapters/pl/abstract_algebra/41-reprezentacje-grup-i-twierdzenie-maschkego.tex`, Git blob `05d87a9b95117069879b58e5c6ea40d71ad4a29c`.
- AA-42: `chapters/pl/abstract_algebra/42-lemat-schura-charaktery-i-ortogonalnosc.tex`, Git blob `f7b662c41bf51d05c03613c879c74b9a7e30040d`.
- Katalog `catalog/books.json`: 42 rozdziały, ostatni AA-42.
- Sprawdzono `AGENTS.md`, `docs/pl/standardy_terminologiczne.md` oraz `/Biblioteka matematyczna/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`.

## Zakres i kontrola matematyczna
1. Zweryfikowano zgodność hipotezy Maschkego (charakterystyka nie dzieli rzędu grupy) w AA-41 z użyciem tego twierdzenia dla zespolonych reprezentacji w AA-42.
2. Sprawdzono zgodność definicji nieprzywiedlności i działania grupy oraz zastosowań lematu Schura do operatorów uśredniających.
3. Prześledzono zależność: Maschke → rozkład regularny → ortogonalność współczynników → ortogonalność charakterów → krotności → baza funkcji klasowych → ortogonalność kolumn.
4. W AA-42 zidentyfikowano 21 deklaracji `\\label` i 9 użyć `\\ref`; jedyny odsyłacz poza AA-42 (`aa:ch:representations`) ma cel w AA-41. Nie jest to pełny test wszystkich odsyłaczy książki.
5. Niezależne testy numeryczne (Python/NumPy): tablice charakterów C3 i S3, ortogonalność wierszy, kolumn, wzór sumy kwadratów wymiarów i ważona macierz Grama (8 kontroli); kontrprzykład Maschkego dla C2 nad F2 (2 kontrole). **10/10 PASS**. Tolerancja zmiennoprzecinkowa dotyczy wyłącznie C3.
6. Sprawdzono przypadki brzegowe: nieodwracalność |G| w F2[C2], poprawne zastosowanie Maschkego nad C i odróżnienie reprezentacji rzeczywistych od zespolonych w lemacie Schura.

## Wynik i ograniczenia
Nie wykryto sprzeczności między kontrolowanymi wynikami AA-41 i AA-42. **Nie zmieniono żadnego zatwierdzonego źródła**. Kontrola ta nie jest ponownym pełnym audytem każdego twierdzenia w AA-01–AA-42.
W tym uruchomieniu nie wykonano kompilacji całej książki, wizualnej inspekcji nowego PDF ani zdalnego GitHub Actions: **status kompilacji i CI — niezweryfikowany**. Nie należy interpretować 10/10 testów jako PASS CI.
Nie odnaleziono AA-43 w aktualnym katalogu; nie tworzono rozdziału zastępczego.

## Postęp
| Zakres | Stan |
|---|---|
| AA-01–AA-42 | 42 pozycje w katalogu; wcześniejsze raporty stabilizacji pozostają odrębną dokumentacją |
| AA-41–AA-42 | audyt przekrojowy 01: brak wykrytych kolizji, 10/10 niezależnych kontroli |
| AA-43 | brak w katalogu; nie rozpoczynać audytu bez źródła |

Następny krok: sprawdzić ponownie HEAD i obecność AA-43; jeśli nadal brak źródła, wybrać **inny**, dotychczas niebadany problem przekrojowy (np. globalne kolizje etykiet), nie powtarzając niniejszej kontroli.
