# Moduł 15B — iteracja 16 (zatwierdzone rozszerzenie teorii całek)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Użytkownik po zatwierdzeniu przykładu nieskończonej wariacji poprosił o szczegółowe omówienie własności całek wektorowych, zwłaszcza Pettisa, Dunforda i Gelfanda. Punkt wyjścia raport 15 (e5a89c9177a71352fdb1f588fe7d7ef6ff1b6bd1), źródło cefc9bdb7724e7bd12cc54ab3b7704ed5fa3a9c6.

## Zakres
- Nowa podsekcja o własnościach całek po przykładzie nieskończonej wariacji; RNP w osobnej podsekcji.
- Jednostajne oszacowania skalaryzacji q_f i r_h, liniowość, niezależność od przedstawiciela, mnożenie przez L-infinity (dla Pettisa pełna konstrukcja przez normowe przybliżenia mnożnika funkcjami prostymi).
- Przechodzenie przez ograniczone operatory: T dla Pettisa, T'' dla Dunforda, R' dla Gelfanda.
- Słaba-* addytywność Dunforda i Gelfanda, kontrprzykłady normowe z istniejących przykładów, dodatkowy warunek całkowalnego majorantu normy zapewniający normową addytywność i skończoną wariację bez założenia mierzalności norm.
- Pełny dowód twierdzenia Orlicza–Pettisa: bezwzględna zbieżność wszystkich skalaryzacji, słabo ciągła mapa na przestrzeni ciągów binarnych, ośrodkowość domkniętej otoczki liniowej, Baire, cylinder o małej średnicy normowej, kryterium Cauchy'ego dla dowolnych skończonych podzbiorów ogona. Wniosek: całka Pettisa generuje miarę wektorową przeliczalnie addytywną w normie, szereg całek po zbiorach rozłącznych zbiega bezwarunkowo. Nie musi mieć skończonej wariacji.
- Półwariacja miary Pettisa: równość z q_f i normą operatora mnożnikowego, porównanie z supremum norm miary na podzbiorach, pełny dowód ciągłości dla malejących zbiorów i jednostajnej ciągłości względem mu. Obliczenie półwariacji w przykładzie atomowym.
- Zbieżność: skalarne DCT oddzielnie dla funkcjonałów, słaba i słaba-* zbieżność całek, jawny warunek jednostajnej zbieżności normowej całek po wszystkich zbiorach. Kontrprzykład z e_n na jednopunktowej przestrzeni.
- Gelfand jako ograniczenie całki Dunforda do kanonicznego obrazu Y w Y'', zgodność z Pettisem, gdy ta ostatnia istnieje. Przykład Gelfand/Dunford, lecz nie Pettis w l-infinity: funkcjonał przedłużający granicę ciągu z przestrzeni c przez Hahna–Banacha.
- Nie rozszerzano RNP ani Fubiniego poza zaakceptowany zakres. Propozycja na później: osobne omówienie warunków Fubiniego dla całek słabych, z kontrprzykładami; nie dodawać bez decyzji użytkownika.

## Technika
Commity źródłowe 93b905330b1c3bc5a58c8fa0a7b5de7f0bc099af, c70f266e29170683ffaea59c3722c7409a7663a9, 7b23ea15de5eeeb43d030609eb4e0d247e7c13d8. Końcowy blob 00d62e2ee66545c0b0ec9e5f1272729bbb932fe0. 1514 wierszy, 34 unikalne etykiety, 19 środowisk dowodów, 7 przykładów. Zachowano dotychczasową treść i etykiety. Sprawdzono zagnieżdżenie środowisk i nowe kontrakty tekstowe.
Testy: 854fb66aaf0634e8ce697329d52656ea11179746 i 01759e379f3963fac14ed27ac079ffcfc0dd9e3c, blob 05b348c91050595148104c829066e8db056a8b75; 15 testów. Nowe regresje: kontrakty dowodów i odsyłaczy, skończone rachunki półwariacji, przykład słabej zbieżności bez normowej. Nie utożsamiać kontroli tekstowej z uruchomieniem unittest lub weryfikacją matematyczną. Nowa kompilacja i oględziny PDF wymagają potwierdzenia. Odczyt statusów: [{"id":45349369767,"sha":"01759e379f3963fac14ed27ac079ffcfc0dd9e3c","status":"in_progress","conclusion":null},{"id":45349347981,"sha":"7b23ea15de5eeeb43d030609eb4e0d247e7c13d8","status":"in_progress","conclusion":null},{"id":45349282695,"sha":"854fb66aaf0634e8ce697329d52656ea11179746","status":"in_progress","conclusion":null},{"id":45349254458,"sha":"c70f266e29170683ffaea59c3722c7409a7663a9","status":"in_progress","conclusion":null},{"id":45349187375,"sha":"93b905330b1c3bc5a58c8fa0a7b5de7f0bc099af","status":"in_progress","conclusion":null},{"id":45348925378,"sha":"e5a89c9177a71352fdb1f588fe7d7ef6ff1b6bd1","status":"completed","conclusion":"success"},{"id":45348881459,"sha":"bba3a79627c6f674389b5b36b4f931a43ef6e0dc","status":"completed","conclusion":"success"}].

## Decyzja
Duże zatwierdzone rozszerzenie: 0/2. Następny audyt 17 musi niezależnie sprawdzić wszystkie nowe argumenty (szczególnie Orlicz–Pettis, półwariacja, zbieżność, zakres założeń), terminologię, CI i układ PDF. Nie przechodzić jeszcze do rozdziału 16.
