# Audyt LXXXVIII (88) — rozdział 25: pierwszy przegląd i różniczkowanie względem miar Radona

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6. Rozdział 24 zamknięty w 0a4782ebc2cd8e0dae32173ee86fd136de312c04.

## Zmiany matematyczne
Commity e3ce9e1c98e3eb2fa37c353c9a3501e0cb8b203b i 54a4e8cc9ca6be881543a4f1398d3cac81702290, blob a1608ca2fc3bcdbe13b8a4b67ffa60202416bc4e.
- Uzasadniono mierzalność oscylacji w dowodzie twierdzenia Lebesgue'a przez łączną ciągłość całki względem środka i parametru wartości funkcji, a następnie przeliczalne supremum po promieniach wymiernych. Wskazano wybór skończonego reprezentanta.
- Dodano twierdzenie Lebesgue'a o gęstości z dowodem przez funkcję charakterystyczną, także dla zbioru nieskończonej miary.
- Doprecyzowano rzeczywistą dziedzinę wartości funkcji w podstawowym twierdzeniu rachunku całkowego i lokalne przedłużenie przez zero. Uściślono dowód pochodnej dystrybuanty dla obu znaków przyrostu i wyeliminowano zbędne osobne założenie braku atomu w punkcie zaniku gęstości osobliwej.
- Zastąpiono zapowiedź różniczkowania względem dowolnej miary Radona pełnym wyprowadzeniem: nierówność maksymalna z mianownikiem mu(B) i ograniczeniem 15^d na podstawie Besicovitcha; mierzalność przez promienie wymierne rosnące do zadanego promienia, bez założenia zerowej miary sfer; dowód na nośniku mu z pominięciem kul zerowej miary; aproksymacja C_c i oszacowanie zbioru wyjątkowego miarą zewnętrzną; zanik gęstości części osobliwej przez regularność i lokalizację. Dodano trzy lematy/twierdzenia (jeden lemat i dwa twierdzenia) wraz z dowodami.
- Sprawdzono pozostałe argumenty, w tym równoważność absolutnej ciągłości dystrybuanty i miary, oraz przeniesienie średnich na kostki. Wymagany niezależny drugi przegląd zwłaszcza nowego twierdzenia względnego i konwencji dla lokalnych miar ze znakiem.

## Regresje i CI
Commit 843a9ed498caae38b87f60fec64d473984d66e8e: cztery metody testowe (ilorazy atomowe, operator maksymalny na skończonej przestrzeni, dystrybuanta z atomem, struktura źródła).
Rzeczywiście wykonano niezależnie w JavaScript 1458 porównań ilorazów atomowych i 2916 oszacowań maksymalnych, dla wszystkich 729 par miar o masach 0,1,2 na trzech punktach; wszystkie przeszły. Nie są dowodem ogólnego twierdzenia ani wykonaniem testów Python.
Kontrola statyczna: 20 etykiet, 20 unikalnych, środowiska poprawnie zagnieżdżone: true. Odsyłacze zewnętrzne: thm:5r-24, def:HL-max-24, ch:regularnosc-funkcji, ch:ac-singular-17, ch:radon-nikodym-18, thm:besicovitch-24, cor:besicovitch-measure-infinite-24.
Commit bb04a807dccbdac5030a2f85f2b2583b835ac7ea: workflow testów, integralności tomu, pełnego i izolowanego PDF oraz renderowania wszystkich stron. Wynik CI niepotwierdzony, PDF nieoglądany.

## Werdykt
24/31 rozdziałów ustabilizowanych. Rozdział 25 w stabilizacji. Następna iteracja LXXXIX: niezależny szczegółowy audyt różniczkowania względem dowolnej miary Radona, przypadki zerowego mianownika, miary osobliwe i pochodna dystrybuanty; weryfikacja CI i składu przed przejściem dalej.
