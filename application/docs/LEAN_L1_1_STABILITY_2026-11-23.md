# Lean / Atlas — L1.1: walidacja optymalizacji .olean i bramka stabilizacji

**Stan na 2026-11-23:** produkcyjna optymalizacja przechodzi aktualne regresje
oraz rzeczywiste Lean 4 i Mathlib; dodatkowy rygor 2+1 na jednym niezmiennym
commicie jest jeszcze w toku. Nie przedstawiać go jako zaliczonego.

## Zakres i niezmienniki

- Gałąź: `biblioteka-matematyczna-iteracja-6`.
- Zakres: `application/backend/lean_environment.py`, wyłącznie wydajność
  budowania względnych nazw artefaktów `.olean`; reszta zmian to diagnostyka,
  testy i CI.
- Zachowane: wykrywanie symlinków, limit `MAX_OLEAN_FILES=120000`,
  globalny budżet `MAX_OLEAN_HASH_BYTES=67108864`, kontrola typu pliku,
  tożsamości otwartego deskryptora i `stat/fstat/stat`, niepowielanie danych
  zależności oraz rozłączne `before/locked/after` podczas wykonywania Lean.
- Żaden raport diagnostyczny nie nadaje statusu dowodowi matematycznemu.
  `certificate=false`; rzeczywista kompilacja i kontrola aksjomatów nie
  oznaczają automatycznej zgodności twierdzenia z kanonicznym LaTeX-em.

## Kontrole poprawności

1. Commit optymalizacji `b1bd6db7` zamienia wywołanie
   `artifact.relative_to(root)` dla każdego kandydata na jedno
   `base.relative_to(root)` na katalog zawierający kandydata.
2. `5cf01379` sprawdza liczby wywołań i zgodność nazw;
   `4aa3f8fd` zawiera niezależnie budowany SHA256 wielokatalogowego drzewa
   projektu i pakietu przy wspólnym budżecie.
3. `95508306` utrzymuje pełną kontrolę pochodzenia zależności oraz odrzucanie
   sfałszowanych raportów benchmarku. Pierwszy test z fikcyjnym katalogiem
   Mathlib bez Git prawidłowo kończył się błędem; poprawiono fiksturę, nie
   rozluźniono kontrolę produkcyjną.
4. Szybkie [Lean Linux+Windows #45147764722](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147764722)
   i pełne [CI aplikacji #45147764748](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147764748)
   na `95508306`, pierwsza próba — `completed/success`. Dodatkowe
   [CI aplikacji #45147874243](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147874243)
   na `bae43f59` — `completed/success`.
5. Dwa niezależne pełne wykonania przypiętego Lean 4.26.0 i Mathlib
   `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`:
   [#45146914480](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146914480)
   (SHA `1a7b9e9a`) oraz
   [#45147764790](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147764790)
   (SHA `95508306`). Obydwa `completed/success`, łącznie z rzeczywistą
   kompilacją, kontrolą aksjomatów, introspekcją MetaM, pomiarem trzech
   pełnych fingerprintów, porównaniem sposobów konwersji nazw i profilerem.
   W każdym z tych przebiegów SHA256 drzewa artefaktów zgadza się pomiędzy
   pełnym benchmarkiem a profilerem CPU.

## Parowany pomiar jednego komponentu

W obu przebiegach na **tym samym runnerze wewnątrz danego przebiegu**
porównano 7732 nazwy kandydatów `.olean` z 1105 katalogów zawierających
kandydatów. Stara i nowa metoda zwróciły identyczny ciąg względnych nazw i
identyczny SHA256 tego ciągu
(`0862e88cbe354381fbf00938cb3242d9068158d59fee1fd4807bfab736f8d45c`).

| Workflow | Stara konwersja, mediana | Nowa konwersja, mediana | Próbek na metodę |
|---|---:|---:|---:|
| `45146914480` | 232,374 ms | 20,834 ms | 5 |
| `45147764790` | 179,671 ms | 16,371 ms | 5 |

W obu próbach nowa konwersja jest około **11 razy szybsza** dla samej
operacji tworzenia nazw. Nie jest to 11-krotne przyspieszenie całego
fingerprintingu, uruchomienia Lean ani przetwarzania PDF.

Mediana pełnego fingerprintu wyniosła odpowiednio `0.513824 s` i
`0.402389 s`. Ponieważ to odrębne runnery, sam stosunek tych liczb nie
jest kontrolowanym porównaniem przed/po.

## Niezależny przegląd sceptyczny

- Porównanie nazw sprawdza faktycznie te same obiekty i nie modyfikuje plików.
- Liczba wywołań `relative_to` nie przekracza 1105 na próbkę nowej metody
  wobec 7732 starej na tej samej populacji.
- Nie wykonano pomiaru „całego świata”: materiał Mathlib jest zainstalowany
  i przypięty, a dowody są testowane osobnym narzędziem.
- Błędy wcześniejszych fikstur zostały odnotowane, nie zamienione w PASS.
- Status `verified` w aplikacji nie wynika z tych pomiarów.

## Niezamknięta bramka 2+1

Rygor stabilizacji 2+1 wymaga trzech udanych pełnych kontroli **tego samego
niezmiennego SHA** oraz osobnego przeglądu. Dla `95508306`:
- Pierwsza pełna próba `#45147764748`: sukces.
- Drugie uruchomienie tego samego joba i SHA zostało uruchomione przez
  GitHub Actions (`run_attempt=2`), ale przy tym zapisie nie było
  końcowego `success`.
- Trzeciej próby **nie** zalicza się, dopóki faktycznie nie zostanie
  zakończona.
- Jeśli wystąpi regresja, poprawić przed akceptacją; nie deklarować
  ukończenia 2+1 ani nie przechodzić do następnego modułu.

Decyzja: **podsystem optymalizacji jest zweryfikowany funkcjonalnie i
mierzalnie, lecz formalne zamknięcie 2+1 jest nadal warunkowe**.
