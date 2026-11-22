# Geometria algebraiczna — rejestr statusów audytów

**Ostatnia aktualizacja:** 2026-11-22, audyt ALG-01 nr 1.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Następny przebieg:** **ALG-01, audyt nr 2** — kontynuować iteracje aż do osobnego audytu bez nowych usterek; ALG-00 pozostaje stabilny.

| ID | Rozdział | Iteracja zakończona | Status | Raport / czynność |
| --- | --- | ---: | --- | --- |
| ALG-00 | Teoria pierścieni — od arytmetyki do geometrii równań | **15** | **STABILNY / ZAMKNIĘTY** | [Audyt 15](2026-11-22-ALG-00-iteration-15.md) — brak nowych usterek, PDF i CI PASS |
| ALG-01 | Geometria afiniczna — równania, ideały i twierdzenie Hilberta o zerach | **1** | **OTWARTY** | [Audyt 1](2026-11-22-ALG-01-iteration-01.md) — poprawki matematyczne, 10 testów, nowy workflow i przegląd PDF; następnie audyt 2 |
| ALG-02 | Geometria rzutowa | 0 | Oczekuje | Po ALG-01 |
| ALG-03 | Punkty osobliwe i geometria lokalna krzywych | 0 | Oczekuje | Po ALG-02 |
| ALG-04 | Algebra przemienna, snopy i krzywe algebraiczne | 0 | Oczekuje | Po ALG-03 |
| ALG-05 | Rozdmuchania i rozwiązywanie osobliwości | 0 | Oczekuje | Po ALG-04 |
| ALG-06 | Powierzchnie algebraiczne | 0 | Oczekuje | Po ALG-05 |
| ALG-07 | Teoria przecięć, grupy Chowa i klasy Cherna | 0 | Oczekuje | Po ALG-06 |
| ALG-08 | Geometria biwymierna i modele minimalne | 0 | Oczekuje | Po ALG-07 |
| ALG-09 | Geometria algebraiczna a analiza zespolona | 0 | Oczekuje | Po ALG-08 |
| ALG-10 | Geometria algebraiczna a topologia | 0 | Oczekuje | Po ALG-09 |

## Metodologia

Audyt pojedynczego rozdziału powtarzać do osobnej, sceptycznej iteracji bez nowych usterek. Oprócz matematyki i języka należy sprawdzić dowody, odsyłacze, testy, kompilację LaTeX co najmniej dwukrotnie, CI oraz skład PDF i rysunki. Używać zweryfikowanych fragmentów stabilnych AA-09–AA-12 jako bazy, bez ponawiania ich pełnych audytów. Nie usuwać unikalnych przykładów, dowodów i etykiet. Aktualne wpisy w tej tabeli mają odzwierciedlać *faktycznie wykonane* audyty, nie planowane działania.

Stabilne ALG-00: blob `ef3bb9cec13784d3bef6ae47de69d3a5bfd09d8b`, źródłowy commit `8fcdb668a81fc575c6b9ae11367ea93be39cade2`. 25 etykiet, 15 odsyłaczy, 6/6 regresji, 22-stronicowy PDF, 4/4 workflows PASS na tym commicie. Osobna stabilizacyjna iteracja 15 nie wprowadzała zmian w źródle.
