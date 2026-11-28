# Topologia ogólna — audyt globalny 28: rejestr rozdziałów 07–12

**Data kontroli:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD odczytany przed kontrolą:** `c731c7cd70ae35ef309fee49c75893eaf8f1f6f1`.

## Metoda i ograniczenia

Odczytano bezpośrednio z GitHub API **wszystkie sześć pełnych źródeł LaTeX** na wskazanej gałęzi, policzono dokładne wystąpienia środowisk `proof` i `tikzpicture`, etykiet `\\label`, odsyłaczy `\\ref`, `\\eqref`, `\\pageref`, `\\autoref` oraz środowisk `figure`. Sprawdzono parowanie początków i końców środowisk, duplikaty etykiet w obrębie plików i pomiędzy sześcioma plikami oraz rozwiązywalność odsyłaczy wewnątrz tego bloku. Przeszukano pełne źródła pod kątem zabronionych form `zwartościowani*`, `zbieżności zwartej`, `pierwszo-przeliczaln*`, `drugoprzeliczaln*`, `sekwencyjn*`. To **audyt inwentarzowy**, nie nowy niezależny dowód matematycznej poprawności wszystkich stwierdzeń ani wizualna inspekcja PDF.

| Rozdział | SHA bloba | Proof | TikZ | Figure | Labels | Refs |
|---|---|---:|---:|---:|---:|---:|
| 07 — Zwartość | `0c31028e8fd301d805781b676c6713a2572501cf` | 18 | 2 | 2 | 37 | 23 |
| 08 — Spójność | `51b5cd2adf19a0345510bd14d5c0ac318cef3ae1` | 15 | 2 | 2 | 42 | 19 |
| 09 — Aksjomaty przeliczalności | `f483271af93842198c094c95f73a68584e835215` | 10 | 2 | 2 | 33 | 10 |
| 10 — Metryzowalność | `1bc0fb72953cb70bcec7c60d3c2fc222ba1851c6` | 14 | 1 | 1 | 29 | 11 |
| 11 — Zupełność i Baire | `8f13420add065dca19d2653c86b0e5781aef2fe7` | 8 | 1 | 1 | 21 | 4 |
| 12 — Przestrzenie jednostajne | `13597073db07742089b82ae3fc9878733dea5e88` | 14 | 1 | 1 | 34 | 12 |
| **Suma 07–12** | — | **79** | **9** | **9** | **196** | **79** |

## Wynik kontroli

- Początki i końce wszystkich 79 środowisk `proof` są sparowane (18+15+10+14+8+14).
- Początki i końce wszystkich 9 środowisk `tikzpicture` są sparowane. Liczba `figure` także wynosi 9.
- Nie wykryto powtórzonych etykiet w żadnym pliku ani pomiędzy plikami 07–12.
- Wszystkie 79 odsyłaczy z sześciu plików wskazują na etykiety z tego samego bloku 07–12; **nie** jest to jeszcze dowód poprawności odsyłaczy całego tomu.
- W badanych sześciu plikach nie znaleziono żadnej z pięciu wyszukiwanych klas niedopuszczalnych form terminologicznych. To nie wyklucza innych usterek językowych.
- Liczba 79 jest **liczbą środowisk `proof`**, nie wszystkich twierdzeń ani certyfikatem 79 poprawnych dowodów.
- Historyczny raport 27 policzył 87 dowodów i 13 TikZ dla 01–06. Sumarycznie **01–12: 166 środowisk proof i 22 TikZ**, ale wartości 01–06 pochodzą z poprzedniej iteracji; przed ostatecznym wydaniem należy uzgodnić je na jednym SHA.

## CI i stan globalny

Przed zapisem raportu odczytano aktualny HEAD `c731c7cd70ae35ef309fee49c75893eaf8f1f6f1` i historię workflow na gałęzi. Najnowszy ukończony przebieg `General topology chapter validation` to [45123000603](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45123000603): **completed/success**, commit `5eaf08271765581d3cff9ffa2c9c78363f2aae48` (raport 27), a nie aktualny HEAD. Nie twierdzimy, że CI na HEAD lub na nowym commicie zakończyło się sukcesem. W tej iteracji nie wykonano nowej lokalnej kompilacji ani inspekcji stron PDF.

**Otwarte:** rejestr 13–18 i 19–23 na aktualnych źródłach; pełny wspólny rejestr wszystkich twierdzeń, dowodów i rysunków 01–23 na jednym SHA; niezależne oględziny czytelności wszystkich ilustracji (w tym rozbieżności historycznych liczników 27 vs 24); pełne odsyłacze i kompilacje; końcowy audyt matematyczny i wydawniczy, CI nowego commitu i końcowe 2+1 dla zmienionych źródeł.

**Następny krok:** rejestr 13–18, z osobnym sprawdzeniem historii rozdziału 16 i zgodności raportu 18 z aktualnym blobem; potem 19–23. Automatyzacja pozostaje aktywna.
