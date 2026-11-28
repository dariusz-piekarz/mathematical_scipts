# RRC 17 — iteracja 301: trzecia lektura stabilizacyjna

Commit źródła: 603465f1c6ebaead49e244c7839313584a04d730.

- Rozróżniono porównania wartości prawie wszędzie od słabych nierówności testowych.
- Uzasadniono regułę łańcuchową dla potęg, odwrotności i logarytmu za pomocą przedłużeń klasy C^1 o ograniczonych pochodnych oraz twierdzenia rozdziału 9; stosowanie lokalne na zbiorach ograniczonych pozwala pominąć F(0)=0.
- Uzupełniono różniczkowanie średnich po kostkach dyadycznych na podstawie różniczkowania po kulach, oraz sumowanie oszacowań wykładniczych po pokryciu.
- Rozpisano algebraiczną redukcję oscylacji.
- Uzasadniono globalne sklejenie reprezentanta Hölderowskiego przez przeliczalne podpokrycie, aby zachować równość prawie wszędzie.
- W kontrprzykładzie radialnym rozpisano wartości własne macierzy, mierzalność i gradient.

Kontrola źródła: 970 wierszy (wcześniej 935), 36 zachowanych unikatowych etykiet, 42 wystąpienia odsyłaczy, brak niezgodności begin/end. Nowy cel thm:pde9-chain istnieje dokładnie raz w rozdziale 9 i jego hipotezy sprawdzono. Pozostałe cele jak w iteracji 300.

Dedykowany run 45980459437 dla źródła po iteracji 300: completed/success. Dla aktualnego commitu run 45980972970 jest queued; kompilacja obecnej wersji i odbiór wizualny nadal niepotwierdzone. Nie oznaczać rozdziału jako ustabilizowany, ponieważ trzecia lektura przyniosła korekty. Następny etap: lektura stabilizacyjna po zmianach, sprawdzenie CI aktualnego źródła, odbiór wizualny i niezależny audyt kontrolny.
