# Geometria algebraiczna — rejestr statusów audytów

**Ostatnia aktualizacja:** 2026-11-22, audyt ALG-01 nr 5 — zakończenie stabilizacji.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Następny przebieg:** **ALG-02, audyt nr 1** — geometria rzutowa. ALG-00 i ALG-01 pozostają stabilne; nie wracać do nich bez nowej rzeczywistej regresji.

| ID | Rozdział | Iteracja zakończona | Status | Raport / czynność |
| --- | --- | ---: | --- | --- |
| ALG-00 | Teoria pierścieni — od arytmetyki do geometrii równań | **15** | **STABILNY / ZAMKNIĘTY** | [Audyt 15](2026-11-22-ALG-00-iteration-15.md) — brak nowych usterek, PDF i CI PASS |
| ALG-01 | Geometria afiniczna — równania, ideały i twierdzenie Hilberta o zerach | **5** | **STABILNY / ZAMKNIĘTY** | [Audyt 5](2026-11-22-ALG-01-iteration-05.md) — niezależna iteracja bez usterek, 30 dodatkowych kontroli, 11 regresji PASS, 23-stronicowy PDF PASS |
| ALG-02 | Geometria rzutowa | 0 | **DO AUDYTU** | Następny przebieg — audyt 1 |
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

Stabilne matematycznie ALG-00: ostatni bezusterkowy audyt 15; po globalnej korekcie terminologicznej w audycie ALG-01/2 aktualny blob `b1550456f2f29144e11041c65b92c0525701687c` (commit `0b2302e41e9137dd777c65600084208b71657b07`). Wcześniejszy blob z audytu 15: `ef3bb9cec13784d3bef6ae47de69d3a5bfd09d8b`, źródłowy commit `8fcdb668a81fc575c6b9ae11367ea93be39cade2`. 25 etykiet, 15 odsyłaczy, 6/6 regresji, 22-stronicowy PDF, 4/4 workflows PASS na tym commicie. Osobna stabilizacyjna iteracja 15 nie wprowadzała zmian w źródle.

Stabilne ALG-01: blob źródła `2026c006d75bebfcb3f59ccd29896ba6d631b7f8` (źródłowy commit `8ce8ddf51e596ffa304d12813760c7bd4a87dfa1`); ostatni testowy commit `b5ddb259f364f416f711dcad8ab29ce1afbb11b9`. Iteracja stabilizacyjna 5 nie modyfikowała pliku `.tex`; 29 etykiet, 21 odsyłaczy, 11/11 testów, 23-stronicowy PDF. Raport: [ALG-01 audyt 5](2026-11-22-ALG-01-iteration-05.md).
