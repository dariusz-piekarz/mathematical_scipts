# Audyt CXLII (142) — wariacja, jednoznaczność, Hilbert
Data: 2026-11-24; gałąź biblioteka-matematyczna-iteracja-6.

## Korekty
Commit fefa985b4ffd1cb3ea33bf513fdd6c4a1592e91a; blob fdff83a91f283617abc6deb27262e5115ba9c298; 942 → 1056 wierszy; 28 etykiet bez zmian.
- Wariacja: wartość na zbiorze pustym, przykład l2 (addytywność w normie, podział skończony z dopełnieniem, funkcjonał realizujący półwariację).
- Wariacja gęstości Bochnera: skończona i przeliczalna addytywność, pełny podział dla prostych, oszacowanie obu różnic wariacji i przejście do granicy.
- Jednoznaczność: krótki dowód przez wariację oraz zachowany, rozwinięty dowód przez przeliczalną rodzinę normującą, bez separowalności X.
- Całka po krzywej: konstrukcja mierzalnego przedstawiciela pochodnej przez proste aproksymacje; jawne zastosowanie rzeczywistego lematu z rozdziału 28 do obu części w przypadku zespolonym.
- RNP w H: jawne założenia o miarze, zupełność L2, słaba zwartość i własność podsieci, testowanie przez chi_A h, osadzenie L2 w L1.
- Gęstość polarna BV: norma 1 z jednoznaczności skalarnej gęstości.

## Kontrole
Dodano MT30-009–011 (de064c4128b9114735d14539cbd678d9c840492d). Niezależne kontrole JS: 16 podzbiorów (różnica wariacji), 3 podziały (tożsamość energii Hilberta), 6 kroków źródłowych, 28 unikatowych etykiet. Wszystkie zaliczone. Testów Python nie uruchamiano lokalnie.
Statusy poprzedniego commitu testów: [{"context":"measure-theory/ch30-regressions","state":"success","target_url":"https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45375359419"},{"context":"measure-theory/ch30-pdf","state":"error","target_url":"https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45375359419"}].
Statusy aktualnego commitu testów: [].

## Następny krok
Kontrola przekrojowa hipotez, przykładów i języka oraz niezależne potwierdzenie CI i oględziny PDF; bez rozbudowy tematycznej. Stan 29/31; rozdział 30 pozostaje otwarty.
