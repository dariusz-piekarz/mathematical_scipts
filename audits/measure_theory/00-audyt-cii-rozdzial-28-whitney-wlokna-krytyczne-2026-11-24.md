# Audyt CII (102) — szczegóły Whitneya i włókna krytyczne
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 3d9d4373b9a1c3e369394912a6dbdf27c752ee7d, blob 527e26c6501ee5b9467fd0e51dec0648efaca91f. Commit źródła fbff9a6aa7295b59d65de97a4cabad9a066c86bd, blob dc2bb8f2a8d3420721a40779880347158e453bec.

## Zmiany
- Whitney: jawna konstrukcja funkcji odcinających, reguła ilorazu i oszacowanie pochodnej podziału jedności. Uzasadniono wybór najbliższych punktów, odległości od nich, rozkład różnicy przybliżeń afinicznych i wszystkie trzy składniki reszty w punkcie K.
- Łuzin–Whitney: rosnąca rodzina H_{j,l}, skończoność miary Q, ciągłość miary z dołu, jawne sumowanie strat i sprawdzenie warunku Whitneya oraz ciągłości obu danych.
- Istotna luka w lemacie o włóknach krytycznych: definicja H^d_delta z rozdziału 26 dopuszcza dowolne pokrycia o średnicach <= delta. Nie wolno bez uzasadnienia utożsamiać tego infimum z pokryciami otwartymi o średnicach < delta. Usunięto nieuzasadnione twierdzenie o borelowskości na ustalonej skali i całkowanie takiej funkcji.
- Nowy dowód używa borelowskiej funkcji dominującej b_r oraz oszacowania zewnętrznej miary zbioru parametrów, na którym koszt włókna przekracza t. Dla ustalonej skali delta, dowolnej eta i odpowiednio małego r mamy całkę b_r <= C eta; nierówność Markowa i eta->0 dają zewnętrzną miarę zero. Przeliczalna suma dla delta=1/j i t=1/l daje tezę dla H^d.
- Rozpisano oszacowanie objętości obrazu kostki przez rozkład ortogonalny na obraz różniczki i dopełnienie, uwzględniono rangę zerową, pusty K, zwartość obrazów i niezależność stałych od eta oraz r. Wymiary d+m=n zapewniają skasowanie potęg r.
- 12 celowanych zamian; wszystkie 28 etykiet zachowane w tej samej kolejności. Definicję skali sprawdzono w źródle rozdziału 26, bez jego modyfikowania.

## Otwarte
Następna iteracja: niezależna kontrola niniejszych poprawek, pełne rozpisanie oszacowania obrazu przy niedostatecznej randze, lemat o zbiorach zerowych, następnie ogólne wzory i wersje na rozmaitościach. Wymagane testy, bramka CI oraz oględziny PDF. Brak kompilacji i oględzin w tej iteracji. Stan 27/31, rozdział 28 nieustabilizowany. Nie przechodzić do 29. Bez rozszerzania zakresu.
