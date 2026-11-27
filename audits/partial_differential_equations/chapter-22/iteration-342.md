# RRC — iteracja 342

## Rozdział 22
Pierwszy audyt szczegółowy sekcji 22.6 (6/8). Commit 452188b1bcd4acc825a832a936da6a944fbf05ef, blob 9502e026cf6237c1e9bc452c6a8b43556e3a4095.

- Pełny dowód słabego typu (1,1) operatora maksymalnego: mierzalność, pokrycie zwartego podzbioru zbioru poziomicowego, wybór rozłącznych przedziałów i trzykrotne powiększenia, regularność miary. Rozkład na część dużą i małą, całkowanie warstwowe z Tonellim i jawna stała dla p>1.
- Rozpisano rozkład dyadyczny całki ułamkowej, oszacowanie dalekiej części przez Höldera, optymalny wybór R i przypadki zerowe. Uzyskano L^{4/3}→L^4 z pełnym uzasadnieniem całkowalności prawie wszędzie.
- W metodzie TT* nie założono z góry ograniczoności T. Skonstruowano operator S na danych gładkich, wykazano tożsamość parowań, zgodność całek Bochnera w L² i L⁴, oszacowanie TS oraz S. Dualność i identyfikacja dystrybucyjna dają jednorodne oszacowanie dla wszystkich danych L².
- Dla całki opóźnionej wykazano oszacowanie przez dodatnie jądro ułamkowe, ograniczone przedłużenie oraz jego zgodność z całką Bochnera L⁴ prawie wszędzie dla ogólnych danych. Rozpisano warunek skalowania i rozróżnienie przypadku (4,4) od par krańcowych. Ujednolicono miary całek.

Kontrola: 1351 wierszy (1163 wcześniej), 17 zachowanych unikatowych etykiet, 23 odsyłacze, sześć różnych celów zewnętrznych w rozdziałach 8,18,20,21, wszystkie jednoznaczne; brak błędów zagnieżdżenia i delimiterów. Pozostałe sekcje identyczne. Kompilacja rozdziału 22 niepotwierdzona.

## Rozdziały 20–21
Run 46001463740 rozdziału 21 SUCCESS, wszystkie kroki zaliczone; artefakt 15201399407, SHA256 d434426b6e41f23c9c9b12ce5efd631ea7c85971b4ceeb618db484cf71773cd7. Nie przeprowadzono jeszcze kontroli wizualnej PDF.
Run 46001463968 rozdziału 20: kompilacja SUCCESS, diagnostyka FAILURE z powodu overfull hbox 26.45058pt w wierszu 416. Rozbito tożsamość Galerkina na trzy wiersze środowiska split, bez zmiany matematycznej. Commit 7e2c6e4a0d50866bf1d91943603e8529944ea218, blob 5f037123b27a7c3e2603b5d44d2ecb86807addd8. Nowe runy przy odczycie: [{"name":"PDE - chapter 21 audit","id":46014171000,"status":"queued"}]. Nie potwierdzono ponownej kompilacji.

Następny etap: sekcje 22.7–22.8 (stany związane i warunki brzegowe), dedykowane CI rozdziału 22 oraz odbiór wizualny rozdziału 21.
