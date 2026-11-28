# Topologia ogólna — audyt 65: zamknięcie CI audytu 64 i niezależna kontrola artefaktu

**Data:** 23 listopada 2026 r. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Powód i zakres

[Audyt 64](00-globalny-audyt-64-pelna-kontrola-wizualna-188-stron.md) zamknął przegląd wszystkich stron i wszystkich 27 ilustracji, ale jego commit `ed0cdbf1da1094c7c540d82c8000fb520743e6f0` miał w chwili publikowania raportu niezakończone CI. Niniejszy audyt niezależnie sprawdza **rzeczywisty wynik tego konkretnego CI** i porównuje **faktycznie pobrany artefakt** z poprzednią zieloną wersją. Nie wprowadza fikcyjnych zmian redakcyjnych tylko po to, by uzyskać kolejny numer audytu.

## Kontrola CI

**[Run 45146664507](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146664507)** na dokładnym SHA commitu audytu 64:
- `status: completed`, `conclusion: success`;
- zadanie `validate`: `completed/success`;
- **0 kroków z `conclusion: failure`**;
- artefakt `general-topology-ch01-ch26`, **ID 14804531538**, pobrany i otwarty, nie tylko zidentyfikowany na liście.

Kontrolną wersją porównawczą jest [run 45145462325](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145462325), commit `5623a2ce38bfe4ac87e71ef7d0b8735fc12dfed5`, artefakt **14804570320**. Oba przebiegi zakończyły się sukcesem.

## Niezależny test regresji rzeczywistych plików PDF

Wyodrębniono z obu ZIP-ów `general_topology.pdf` i wykonano bezpośrednie porównanie stron z użyciem PyMuPDF. W przeciwieństwie do audytu 64 nie opierano się na samej zgodności logów lub wyników wcześniejszego oglądania.

| Badany aspekt | Kontrola | Wynik |
|---|---|---|
| Długość pełnego skryptu | liczba stron PDF | **188 stron w obu** |
| Obraz strony | bajty rastra każdej strony, RGB, 72 dpi | **188/188 IDENTYCZNE** |
| Treść tekstowa | tekst wyodrębniony oddzielnie dla każdej strony | **188/188 IDENTYCZNE** |
| Elementy graficzne | liczba ścieżek rysunkowych na każdej stronie | **188/188 IDENTYCZNE** |
| Linki | kolejność, typ, cel i położenie docelowe odsyłaczy na każdej stronie | **188/188 IDENTYCZNE** |
| Geometria | prostokąty stron PDF | **188/188 IDENTYCZNE** |
| Odsyłacze | liczba i granice celów wewnętrznych | **440 łącznie; 0 poza zakresem** |
| Położenie tekstu | prostokąty wszystkich wyodrębnionych słów | **0 poza stroną** |
| Oddzielne PDF-y | `general_topology_ch02.pdf`–`general_topology_ch26.pdf` | **25/25 obecne** |
| Logi rozdziałów | obecność logów TeX dla tych samych 25 plików | **25/25 obecne** |
| Logi kompilacji | `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence`, `Fatal error` | **0 dopasowań w 26 logach** |

Dokładne sumy kontrolne (SHA-256 pełnych plików PDF):
- CI audytu 63: `9d2b76edaa0726e3fd237725a08d7a614dc1aa3cc31ef61cf6011cb99ce8ae49`;
- CI audytu 64: `205262161ed945f940a1a294e38875dd77b19efd3aaf31f2d83dd0ce1bf87aa8`.

Oba pliki mają dokładnie **1 419 603 bajty**, lecz nie są binarnie identyczne (np. metadane kompilacji). Różnica binarna **nie oznacza** regresji: niezależne sprawdzenie obrazu, wyodrębnionego tekstu, odsyłaczy, rysunków i wymiarów pokazało brak różnic na każdej ze 188 stron.

Dodatkowo sprawdzono wynik `pdfinfo`: PDF jest niezaszyfrowany, A4, bez aktywnego JavaScript. Wszystkie **27 pozycji fontów** z `pdffonts` mają `emb=yes`; ich tekst jest poprawnie wyodrębnialny.

## Końcowy werdykt

**PASS — kontrolowana wersja „Topologii ogólnej” jest stabilna również po commicie audytu 64 i jego pełnym CI.**

Połączone, rzeczywiście wykonane kontrole z audytów 01–65 obejmują indywidualne rejestry **325/325 dowodów**, **26/26 rozdziałów**, wizualną kontrolę **188/188 stron**, powiększony przegląd **27/27 rysunków** i niezależny test regresji 188/188 stron między kolejnymi zielonymi artefaktami. Uwaga kosmetyczna z raportu 64 dotycząca kontrastu linii na rysunku 26.1 jest nadal nieblokująca.

**Dalsze bezwarunkowe dopisywanie audytów o identycznym zakresie nie zwiększa jakości wyniku.** Dalsze prace należy otwierać po rzeczywistej zmianie źródła, wykryciu błędu, wymianie zależności lub świadomej decyzji o rozszerzeniu skryptu.

Niniejszy raport jest dokumentacją końcowej weryfikacji, nie modyfikuje rozdziałów `.tex`, testów ani rysunków. Samo dodanie raportu uruchamia nowe CI; wynik tego nowego przebiegu należy odnotować osobno, nie twierdzić z góry, że przeszedł.
