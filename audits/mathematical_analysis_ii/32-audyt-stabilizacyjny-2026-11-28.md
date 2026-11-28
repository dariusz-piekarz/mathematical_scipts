# AM II 32 — audyt stabilizacyjny

Data: 2026-11-28. Źródło: commit 47d2db49bee58638282f6c4162f6fb5e5e28c266, blob 6490d5c79dadc4c1fd64cd6cac9367a1c50c034f (571 wierszy).

## Kontrola merytoryczna
- Cavalieri: mierzalność przekrojów prawie wszędzie i konwencja na zbiorze wyjątkowym; objętości stożka i przecięcia walców odpowiednio AH/3 i 16R³/3.
- Masa i środek masy: warunki 0<M<∞ i skończony pierwszy moment, kontrprzykład z gęstością x⁻²; podstawienie afiniczne najpierw dla funkcji nieujemnych, następnie dla całkowalnych funkcji ze znakiem.
- Półkula: 3R/8; trójkąt o gęstości 1+x: masa 2/3, momenty 1/4 oraz 5/24, środek (3/8,5/16).
- Steiner: rzut ortogonalny, zanik wyrazu mieszanego, skończoność momentów. Macierz bezwładności w kontekście skończonej masy i drugiego momentu; walec i kula: poprawne współczynniki.
- Pappus–Guldin: ograniczenie do jednej strony osi, pominięcie zbiorów miary zero, jakobian r; torus 2π²Ra².
- Drut: zwarty obraz, całkowalność momentów, rozróżnienie krotności i miary Hausdorffa; półkolisty drut 2R/π, płyta 4R/(3π). Praca pola potencjalnego: znak i założenie C¹.
- Rysunek półkuli: parametry przekroju (z=3/5, r=4/5) i położenie środka masy 3/8 zgodne z rachunkiem. Kontrola dotyczy źródła, nie renderu najnowszego PDF.

## Kontrola statyczna
18 etykiet; 19 odsyłaczy wewnętrznych i 3 zewnętrzne, wszystkie cele znalezione w AM II 30–32 i AM I 33. Brak duplikatów etykiet rozdziału w kontrolowanych plikach. Bilans klamer 0, minimalny bilans 0, środowiska poprawnie zagnieżdżone, 370 delimiterów dolara. Rozdział 32 włączony po 31, przed 36; luka 33–35 celowa.

## CI
Terminologia dla 47d2db4: success (46158750845). Dedykowana kompilacja 46158750841: pending w momencie kontroli. Przebieg 46158759103: skipped. Najnowszy PDF niezweryfikowany; wcześniejszy artefakt 15259954848 dotyczy c3bfb77.

Wynik: zero nowych uwag merytorycznych i statycznych w tym przebiegu; bez zmian źródła. Następny etap: niezależny audyt kontrolny. Odbiór techniczny pozostaje otwarty do potwierdzenia aktualnej kompilacji.
