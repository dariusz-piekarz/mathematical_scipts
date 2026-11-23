# Lean / Atlas — L1.1: walidacja optymalizacji .olean i bramka stabilizacji

**Stan końcowy (2026-11-23): L1.1 ZAMKNIĘTY dla commita
`95508306b8bd0a07eb2c3ea05c8fc732ebb2980b`.** Zakończono rygor
stabilizacji 2+1: trzy niezależne, udane pełne kontrole tego samego SHA,
dwa udane przebiegi realnego Lean/Mathlib oraz osobny przegląd dowodów z CI.
Dotyczy to wyłącznie infrastruktury fingerprintu, nie semantycznej zgodności
twierdzeń Lean z LaTeX-em.

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

## Bramka stabilizacji 2+1 — ZALICZONA

Dla dokładnego SHA `95508306b8bd0a07eb2c3ea05c8fc732ebb2980b`
ten sam workflow [Mathematical library application checks
#45147764748](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147764748)
uruchomiono trzykrotnie bez zmian kodu:

| Próba | Zakończenie | Testy Pythona | Pominięte / nieprzejrzane | Przeglądarka | Rozdziały |
|---|---|---:|---:|---|---:|
| `run_attempt=1`, job `137601180297` | `completed/success` | 709 | 10 / 0 | `passed`, brak błędów JS | 499 |
| `run_attempt=2`, job `137605576100` | `completed/success` | 709 | 10 / 0 | `passed`, brak błędów JS | 499 |
| `run_attempt=3`, job `137607935928` | `completed/success` | 709 | 10 / 0 | `passed`, brak błędów JS | 499 |

Dodatkowo na tym samym SHA [Lean kernel + axiom audit
#45147764790](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147764790)
zakończył się sukcesem, a szybki workflow
[Linux/Windows #45147764722](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45147764722)
również `completed/success`.

**Przegląd sceptyczny po trzecim przebiegu:** sprawdzono logi każdej próby,
identyczność pełnego SHA checkoutu, liczbę i klasyfikację pominięć,
rzeczywisty test przeglądarkowy i wynik kontroli odsyłaczy. Nie zauważono
regresji w podsystemie Lean ani w kontrakcie API/Czytnika/Explorera.
`unreviewed_skips=0` nie oznacza zerowej liczby pominięć: każda próba
miała dokładnie 10 oznaczonych przypadków zależnych od dostępności
środowiska; odrębny workflow wymaga rzeczywistego Lean.

**Decyzja:** zamknąć **L1.1 — optymalizacja tworzenia względnych nazw
i diagnostyka fingerprintu .olean**. Uznane kryteria są ograniczone do
wskazanego SHA. Nie przypisywać tym wynikom certyfikatu zgodności
semantycznej twierdzeń; `certificate=false` pozostaje bez zmian.
Kolejne prace można prowadzić jako **nową jednostkę architektury**,
z odrębną stabilizacją, bez ponownego otwierania L1.1 bez nowej regresji.
