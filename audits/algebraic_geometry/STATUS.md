# Geometria algebraiczna — rejestr statusów audytów

**Ostatnia aktualizacja:** 2026-11-22, audyt ALG-02 nr 2.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Następny przebieg:** **ALG-02, audyt nr 3** — niezależny przegląd po ujednoliceniu homogenizacji z konwencją [X:Y:Z]. ALG-00 i ALG-01 pozostają stabilne.

| ID | Rozdział | Iteracja zakończona | Status | Raport / czynność |
| --- | --- | ---: | --- | --- |
| ALG-00 | Teoria pierścieni — od arytmetyki do geometrii równań | **15** | **STABILNY / ZAMKNIĘTY** | [Audyt 15](2026-11-22-ALG-00-iteration-15.md) — brak nowych usterek, PDF i CI PASS |
| ALG-01 | Geometria afiniczna — równania, ideały i twierdzenie Hilberta o zerach | **5** | **STABILNY / ZAMKNIĘTY** | [Audyt 5](2026-11-22-ALG-01-iteration-05.md) — niezależna iteracja bez usterek, 30 dodatkowych kontroli, 11 regresji PASS, 23-stronicowy PDF PASS |
| ALG-02 | Geometria rzutowa | **2** | **OTWARTY** | [Audyt 2](2026-11-22-ALG-02-iteration-02.md) — poprawiono ogólną homogenizację i domknięcie rzutowe, przypadki brzegowe; 12 testów; następnie audyt 3 |
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

ALG-02 po audycie 1 (historia): źródłowy blob `4c122514238f4cb0de7188c18f3b36e569e00552`, 12 unikalnych etykiet, 9 rozwiązanych odsyłaczy, 11/11 regresji, osobny 11-stronicowy PDF. [Dedykowany CI 45012542403](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45012542403): **success**. Następny jest audyt **ALG-02/2**, nie ALG-03.

ALG-02 po audycie 2: blob `e589cf3b4f42008ae280a2cfab582db2c3fb9e24` (ostatni źródłowy commit `317f754ccb6115a54df4ffaf9f34d3d770ce21e9`), 12 etykiet, 9 poprawnych odsyłaczy, 12/12 testów regresyjnych; PDF 11 stron po końcowej kompilacji trzech rozdziałów, kontrola wizualna PASS. [Audyt 2](2026-11-22-ALG-02-iteration-02.md). Dedykowany [CI 45013432718](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013432718): **success**. Następny krok — **ALG-02/3**, rozdział pozostaje otwarty.
