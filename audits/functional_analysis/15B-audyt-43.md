# Moduł 15B — audyt 43 (stabilizacyjny, czysty 1/2)

Data: 24 listopada 2026. Wyłącznie gałąź biblioteka-matematyczna-iteracja-6. Punkt wyjścia: raport 42 d039e6c5e61e3b0fdf7d21d03ff7f90ec87bd14b. 

## Kontrola merytoryczna i spójność
Ponowna kontrola stanu po audycie 42, ze szczególnym uwzględnieniem zależności między 12 podsekcjami. Zweryfikowano poprawność zmian w definicji wariacji, jawność skalarów w liniowości Bochnera, zakres oznaczenia lambda, rozróżnienie założeń o dominacji w różniczkowaniu całek, sformułowanie wniosku o wyższych pochodnych, ponowne użycie konstrukcji rodziny normującej w twierdzeniu Sobolewa i warunek całkowalności w uwadze o przestrzeniach lokalnie wypukłych. Zachowano szczegółowy dowód rodziny normującej w twierdzeniu Pettisa o mierzalności oraz argument wspólnego zbioru wyjątkowego w Sobolewie. Przejrzano powiązania mierzalności, hierarchii całek, wariacji i półwariacji, Fubiniego, Vitaliego, reprezentacji krzywych oraz różniczkowania w normie i w topologiach słabych. Nie wykryto nowych koniecznych poprawek. Nie rozszerzano zakresu, nie zmieniano źródła ani testów.

## Kontrola strukturalna
Źródło f5d1b39e48918066e8a1bf9dc5460058ef10366f (commit 856b4ca97bfe3f1591cb1243dca7d95ca51b081f), 3420 wierszy, 12 podsekcji, 37 dowodów, 59 unikalnych etykiet, 27 wystąpień odsyłaczy, poprawne zagnieżdżenie środowisk. Bez zmian względem audytu 42. Potwierdzono wszystkie pięć etykiet zewnętrznych bezpośrednio w źródłach: thm:dual-sequences12 i thm:lp-banach12 (rozdział 12, blob 923f7976d09f42030687a8873401cf34da4ff2fb), def:weak-curve-derivative14 (rozdział 14, blob 49b8c98236e924281d4b7ee756bbe6213025f165), sec:integral-lcs15a i thm:parametric-integral15a (15A, blob 79f8ffe796145ff69103479a4153c906cbbb0fb7).

## CI i PDF
Run 45370676513, head 46cad6af4463e0356e478128e729e565208ff925, job 138363838585: 36/36 testów, 9/9 etapów sukces, trzy przebiegi pdflatex, 145 stron, 1419798 bajtów. Artefakt 14908133399 pobrany, log zweryfikowany: brak overfull, niezdefiniowanych poleceń i odsyłaczy oraz brakujących znaków; jedyne znane underfull hbox 1127 (wiersze 336–342). Wygenerowano i obejrzano cztery arkusze renderów wszystkich stron 102–136 z 15B, w tym stronę współdzieloną z początkiem 16. Brak dostrzeżonych obcięć i kolizji. Testy blob 6345dc13ad8355a26bd81caa9d5e5a2ca53541c5 bez zmian.

## Decyzja
Pierwszy czysty audyt 1/2. Kolejna iteracja 44: niezależna końcowa kontrola, w szczególności szczegółów założeń i wniosków oraz aktualnego CI. Przy braku koniecznych zmian 2/2 i przejście do 16; przy zmianach reset do 0/2. 14, 15, 15A pozostają stabilne. Zakres zamknięty.
