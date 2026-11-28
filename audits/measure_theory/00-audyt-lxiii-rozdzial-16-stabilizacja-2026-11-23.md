# Audyt LXIII (63) — rozdział 16: pełna druga kontrola, regresje i PDF

Data: 2026-11-23. Repozytorium: `dariusz-piekarz/mathematical_scipts`. Istniejąca gałąź: `biblioteka-matematyczna-iteracja-6`.
Rozdział: `chapters/pl/measure_theory/16-miary-ze-znakiem-miary-zespolone-i-wariacja-calkowita.tex`.
**Zweryfikowany końcowy SHA rozdziału:** `f1c561ae62cd770886e0ce09a27b2b64bb53134b`.
Pierwszy przegląd rozdziału 16: audyt LXII (62), commit `3d3039691859a2ebe59e9f1ff5ece328fb07c465`.

## 1. Przegląd matematyczny i faktyczne korekty

Po ponownym przeczytaniu całego rozdziału skontrolowano definicję skończonej miary ze znakiem, ograniczoność, konstrukcję Hahna przez supremum, jednoznaczność rozkładu Jordana, normę wariacji przez podziały, miary zespolone, wariację całkowitą, miary o gęstości, zupełność przestrzeni miar i opis dualny normy. Zrewidowano też dowód zbieżności miar o oscylujących gęstościach.

Z uwzględnieniem równoległego commitu poprawiającego zapis całki w rozdziale 16 (bez nadpisywania pracy drugiego zadania) naniesiono trzy dalsze zmiany w istniejącym źródle:
1. W definicji wariacji zespolonej jawnie określono `m\ge1` w supremum po skończonych podziałach, tak jak w wariacji miary ze znakiem.
2. W dowodzie przeliczalnej addytywności wariacji uzasadniono monotoniczność `|\eta|` przez przedłużenie dowolnego skończonego podziału `A\subseteq B` o `B\setminus A`; poprzednio własność była użyta bez dowodu.
3. Przykład `\nu_n(E)=\int_E\sin(nx)\,\mathrm d\lambda_1(x)` rozszerzono o dowód **zbieżności na każdym zbiorze mierzalnym**, a nie tylko zbieżności całek dla funkcji ciągłych: dokładny wzór na całkę po przedziale, gęstość skończonych funkcji schodkowych na przedziałach w `L^1((0,2\pi))`, oszacowanie `|\int(g-s)\sin(nx)|\le\|g-s\|_1`, zastosowanie do `g=\chi_E`. Jednocześnie `\|\nu_n\|_{\mathrm{TV}}=4`, więc zbieżność na zbiorach nie implikuje zbieżności w wariacji całkowitej.

**Commit korekt źródłowych:** `2dc6b7eec2393b89378b27956826cb727d663438`.
**Struktura po korekcie:** 40 par `begin/end` bez złego zagnieżdżenia; 20 unikalnych etykiet; 8/8 odsyłaczy rozwiązanych lokalnie; 0 wystąpień wcześniejszej błędnej notacji całki `\mathrm d\nu(x)_n`.

## 2. Niezależne kontrole numeryczne

Przed uruchomieniem CI wykonano w Pythonie deterministyczne skończone sprawdzenia:
- 12 800 porównań na podzbiorach atomowych w modelach Hahna–Jordana;
- 500 zespolonych modeli wariacji i osiągania normy parowaniem;
- 200 przykładów oscylujących funkcji schodkowych z jawnym oszacowaniem `2/n` dla całek po przedziałach.
Wszystkie zakończyły się bez naruszeń. Modelowe obliczenia nie zastępują ogólnych dowodów.

Dodano trwały plik `tools/tests/test_measure_theory_ch16.py`, **8 przypadków**: Hahn/Jordan, wariacja rzeczywista, wariacja zespolona, najmniejsza miara dominująca, wariacja gęstości i test dualny, przybliżenia w normie TV, oscylacje i kontrola etykiet/kluczowych wzorów. Commity `b15388ec9c73fad688b72b6cf0a9d2bac53b3c06` i korekta brzegu `n=1` `05daa80ddacaa5b6700d092a8ed5cd7dadee65f4`. Zweryfikowany SHA testu: `b25742511c844f87aa64ff4cdfaf264f3ab6ed8c`.

## 3. Rzeczywiste wykonanie GitHub Actions

Nowy workflow: `.github/workflows/measure-theory-ch16.yml` (commit `6fd9d6d5caf456484f6067d5fc4f13673cc648ed`, blob `1476fa073c2217d6b46c0dc7f90736c36fab6c9e`). Uwzględnia 8 nowych regresji i 4 przekrojowe testy integralności pełnego tomu, pełny PDF książki, osobny PDF rozdziału 16 z numeracją 16, walidację końcowych logów i obrazy stron.

**Konkretny potwierdzony przebieg:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45253108348 na commicie `6fd9d6d5caf456484f6067d5fc4f13673cc648ed`, który zawiera wszystkie powyższe korekty źródła i testu.

Bezpośrednio odczytano dwa klasyczne statusy commitu:
- `measure-theory/ch16-regressions = success`;
- `measure-theory/ch16-pdf = success`;
oba kierują do wskazanego przebiegu.

Odczytano też trzy konkretne joby z `completed/success`:
- testy, ID `137967703770`: **8/8 testów `OK`**, następnie **4/4 testy `OK`**, potwierdzone pełnym logiem;
- PDF, ID `137967703090`: pełny skrypt **258 stron, 1 890 958 bajtów**, osobny rozdział 16 **7 stron**; końcowe logi bez nierozwiązanych referencji, wielokrotnie zdefiniowanych etykiet lub przepełnionych wierszy;
- raportowanie statusów, ID `137968743030`: `success`.

**Artefakt rzeczywiście pobrany:** ID `14857395521`, ZIP `measure-theory-ch16-pdf-and-logs` (2 639 048 bajtów); zawiera rzeczywiste oba PDF-y i logi oraz PNG stron 1, 4 i 7. W aktualnie dostępnej kopii sprawdzono także stronę 2 i 6, wyrenderowane z PDF. Finalne logi: dla osobnego rozdziału 0 `Underfull \\hbox`, 0 `Overfull \\hbox` i 0 brakujących odsyłaczy; w pełnej książce występują ostrzeżenia `Underfull \\hbox`, ale brak przepełnień i niepoprawnych referencji (występujące w trakcie wcześniejszych przebiegów ostrzeżenia są usunięte w logach finalnych).

## 4. Inspekcja wizualna i werdykt

**Obejrzane strony osobnego rozdziału: 1, 2, 4, 6, 7.** Rysunek rozkładu Hahna, nagłówki, wzory, tekst i końcowy przykład są czytelne. Nie wykryto na tych stronach nakładających się napisów ani wyjścia poza margines. Strona 7 jest krótka, ponieważ zawiera kompletną, niepodzieloną uwagę o miarach ze znakiem przyjmujących wartości nieskończone; nie jest przypadkowo osieroconym dwuwierszowym fragmentem i nie ma uciętego tekstu. Nie stosowano sztucznego ściskania strony kosztem czytelności.

**Rozdział 16: STABILNY / ZAMKNIĘTY w zakresie przeprowadzonych dwóch iteracji, testów i PDF.** Materiał matematyczny po korekcie przeszedł powtórny merytoryczny przegląd oraz udokumentowaną kompilację i testy. Jest to werdykt o tym konkretnym blobie, nie formalny dowód automatyczny wszystkich twierdzeń i nie certyfikat całej książki.

**Następny rozdział, dopiero po tym zamknięciu:** 17 — `17-bezwzgledna-ciaglosc-osobliwosc-i-rozklad-lebesguea-miar.tex`. Rozpocząć osobny szczegółowy audyt założeń, dowodów, przykładów, zależności od rozdziału 16 i technicznego CI.
