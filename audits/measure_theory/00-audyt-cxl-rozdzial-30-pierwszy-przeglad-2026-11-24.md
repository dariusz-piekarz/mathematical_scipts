# Audyt CXL (140) — pierwszy przegląd rozdziału 30
Data: 2026-11-24; gałąź biblioteka-matematyczna-iteracja-6.

Źródło: b813ac6cceca6d336965a123c55dc6030fca0419 → 5c0ee4a8eb79a5bf8ccad054e6549d298be9685c, 784 → 838 wierszy. Commit korekty b6c9155f7624eb5bb45b3d03df45a7ffb8eb30f9.

## Poprawki
- Silna mierzalność na niezupełnej przestrzeni: mierzalny przedstawiciel i dowód mierzalności granicy.
- Obcinanie prostych: zachowanie zbieżności także na zbiorze, gdzie g=0.
- Zupełność L1: oszacowanie ogona i przejście od dowolnego ciągu Cauchy'ego do funkcji prostych.
- Rozszerzenie miary z przedziałów: singleton 0, rozłączne przybliżenia i dowód skończonej addytywności przed przeliczalną.
- Zmiana miary dominującej: silna mierzalność iloczynu, norma L1 i równość całek przez aproksymację.

## Regresje i CI
MT30-001–005 zapisane w tools/tests/test_measure_theory_ch30.py (2e9b55c3c58fc0918cb11ce1f26c3de98aaf1c60). Workflow pełnego i izolowanego PDF oraz regresji: a94389b0d5049afdcc4eeae76c6a818195cdac87.
Wykonano niezależne kontrole JS: 1728 przypadków rozłącznych aproksymacji, 8 podzbiorów w modelu zmiany miary, 8 poziomów dyadycznych, 7 warunków źródłowych i unikatowość 28 etykiet. Wszystkie zaliczone. Nie jest to uruchomienie pliku Python ani formalizacja Lean; wynik workflow i oględziny PDF pozostają do potwierdzenia.

## Następny audyt
Uściślić argument maksymalny w różniczkowaniu Bochnera, lemat o dzieleniu miary bezatomowej (klasy modulo zbiory zerowe), część atomową oraz kodowanie podziałów w dowodzie RNP. Sprawdzić CI i PDF. Nie rozszerzano zakresu. Stan 29/31; rozdział 30 otwarty.
