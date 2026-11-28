# IT-08 — trwałe kryteria charakteryzacji ACG_*
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| IT-08-001 | it:lem:acstar-null-variation | Suma oscylacji luk skończona z AC_* i sumowalności długości | semantyczna |
| IT-08-002 | it:lem:acstar-null-variation | Rozcięcie względem min/max E w komórce, najwyżej dwa odcinki skrajne na lukę | semantyczna + Python |
| IT-08-003 | it:lem:acstar-null-variation | Oddzielny budżet dla otwartego pokrycia, skończonej rodziny luk i ogona | semantyczna + Python |
| IT-08-004 | it:cor:acgstar-null-variation | Grupowanie znaczników według pierwszego zbioru pokrycia, suma budżetów | semantyczna + Python |
| IT-08-005 | it:thm:acgstar-derivative-integrable | Pochodna poza zbiorem zerowym, wspólne cechowanie także poza zbiorem wyjątkowym, przyrosty i wartości funkcji na zbiorze wyjątkowym, teleskopowanie | semantyczna + Python |
| IT-08-006 | it:lem:acstar-affine-extension | Przedłużenie afiniczne, ciągłość, suma całek modułów nachyleń, absolutna ciągłość | semantyczna + Python |
| IT-08-007 | it:thm:acstar-ae-differentiable | Sumowalność oscylacji, pokrycia U_{k,m}, zerowy limsup, kontrola ilorazów różnicowych | semantyczna + Python |
| IT-08-008 | it:lem:kh-null-variation | Minimum cechowań, Saksa–Henstocka i nieujemna funkcja zerowa prawie wszędzie | semantyczna |
| IT-08-009 | it:lem:kh-bvstar-cover | Domknięcie A_n, rozdzielenie parzyste i nieparzyste, granica i jednolita stała | semantyczna + Python |
| IT-08-010 | it:lem:bvstar-null-to-acstar | Ograniczona wariacja przedłużenia, zaniedbywalne wahanie, pochodna L1 i niezależność dowodu od charakterystyki | semantyczna |
| IT-08-011 | it:lem:bvstar-null-to-acstar | Kontrola sum oscylacji przez AC przedłużenia i sumowalny ogon luk | semantyczna + Python |
| IT-08-012 | it:thm:kh-acgstar-characterization | Oba kierunki i różniczkowalność prawie wszędzie bez błędnego koła | semantyczna |
| IT-08-013 | it:lem:acstar-null-variation | Promień przy końcu wybranej luki mniejszy od połowy jej długości; znacznik jest końcem odcinka skrajnego | semantyczna + Python |
| IT-08-014 | it:thm:kh-acgstar-characterization | Domkniętość zbiorów lokalnych oszacowań z użyciem ścisłego promienia; równoważność AC_* i AC na całym przedziale | semantyczna |
| IT-08-015 | it:thm:ac-lebesgue-primitive (IT-11) | AC funkcji wariacji, rozkład Jordana, absolutna ciągłość miar i reprezentacja L1 niezależnie od charakterystyki ACG_* | semantyczna |
| IT-08-016 | it:thm:differentiable-acgstar, tw:denjoy-countable | Skończona pochodna we wnętrzu, jawny wybór n, pokrycie końców i przeliczalnych wyjątków zbiorami jednopunktowymi | semantyczna + Python |
| IT-08-017 | it:lem:bvstar-null-to-acstar | Ciągłość wariacji: zastąpienie skrajnego węzła podziału, nierówność z eta, obie strony; mierzalne gęstości i związek z HK | semantyczna + Python |
| IT-08-018 | Przykład rozłącznych garbów | Rozłączność przedziałów, przedłużenie C^1 przez zero, lokalna skończoność, ciągłość w 0 i rozbieżność całki modułu pochodnej | semantyczna + Python |
| IT-08-019 | it:thm:denjoy-bv-ac, it:cor:denjoy-hk | Jednoznaczność modulo stałą, AC jako przecięcie ACG_* z BV, równość wahania i całki modułu pochodnej | semantyczna |

Audyt po migracji (2026-11-25): commit f544bd309c84b25e9a94848de3699331754512f5, blob 1b3b659aea30166b8b7dd163e462f2884d9a0f53. Zachowano 25/25 starych etykiet, dodano 3; środowiska sparowane. Ponownie przeczytano wszystkie dowody IT-08: domknięcie i algebra, zaniedbywalne wahanie na zbiorach zerowych, przedłużenie afiniczne, różniczkowalność p.w. przez sumowalność oscylacji luk, pokrycie BV_* i wzmocnienie do AC_*, równoważność Denjoy=HK, sklejanie i AC=ACG_*∩BV. Rozszerzono twierdzenie o funkcjach różniczkowalnych na dowolne zachowanie pochodnej na końcach przy ciągłości F, rozpisano ciągłość wariacji, mierzalną reprezentację pochodnej i przykład z rozłącznymi nośnikami. Sprawdzono rzeczywiste cele odsyłaczy do IT-03,04,11. Ujednolicono terminologię bezwzględnej ciągłości. Testy: commit 630ecc98df32f625fac03d7d4b7aecc65edcee97 (11 metod, w tym 3 nowe skończone świadectwa, nie formalne dowody). CI po zmianach i kontrola wizualna PDF pozostają do potwierdzenia; Lean nieuruchamiany. Następny etap: audyt stabilizacyjny i kontrolny.
