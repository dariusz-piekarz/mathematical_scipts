# Topologia algebraiczna — TOP-25: pięć audytów szczegółowych

**Data:** 21 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`; gałąź `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/algebraic_topology/25-kategorie-pochodne-struktury-hodge-a-cykle-zanikajace-i-monodr.tex`.  
**Ostatni skontrolowany blob źródła:** `ee73c4fe52c7520a101a151f5473062b71dd4bd4`.  
**Reguła:** sprawdzenie już istniejących definicji, lematów, twierdzeń, dowodów, przykładów, odsyłaczy, ilustracji i LaTeX; bez dodawania nowego materiału. Wzorzec szczegółowości: DG-01. Osobno określono zakres przyjętych twierdzeń głębokich.

## Audyt I — krytyczne kwestie matematyczne

1. **Twierdzenie Picarda–Lefschetza:** poprzednia hipoteza o jednym zwyczajnym węźle we włóknie szczególnym była niewystarczająca. Rodzina `zw=s^m` ma centralne włókno z jednym węzłem, ale monodromia jest `T^m`, a nie pojedyncza transwekcja `T`. Uściślono gładkość przestrzeni całkowitej, submersyjność poza punktem krytycznym i lokalną postać `π(z,w)=zw` przy parametrze podstawy. Wyjaśniono znaczenie hipotezy przez bazową zmianę `t=s^m`, bez dodawania nowego twierdzenia.
2. **Filtracje Hodge'a:** w dowodzie odtworzenia rozkładu z przeciwstawnych filtracji zastąpiono argument „indukcyjnie” jawnym rozkładem `F^p=F^{p+1}⊕(F^p∩G_p)` dla `G_p=\overline{F^{m-p}}`, włącznie z uzasadnieniem jedyności i sprzężenia.
3. **Wagi krzywej węzłowej:** precyzyjnie wskazano, że izomorfizm wagi zerowej w `H¹(C;Q)` korzysta z dokładności długiego ciągu w kategorii mieszanych struktur Hodge'a dla algebraicznego kwadratu normalizacji; **sama** funktorialność grup kohomologii nie uzasadniała przeniesienia wag.
4. **Pochodne snopy:** dla obiektu pochodnego `K` zastąpiono nieprecyzyjne `R^q f_* K` przez `\mathcal H^q(Rf_*K)`; definicję obrazu pochodnego uściślono przez kompleksy `K`-iniektywne, a nie dowolną rezolucję kompleksu.
5. **Mieszane struktury Hodge'a:** dopisano jawny wzór filtracji indukowanej na `Gr_m^W`.
6. **Dokładność perwersyjna cykli:** jawnie określono morfizm `f:X→C`, `X_0`, współczynniki `Q`, obiekt `P`, dziedziny i przeciwdziedziny funktorów `Rψ_f[-1]` oraz `Rφ_f[-1]`, konwencję przesunięcia i wniosek o perwersyjności wyniku.

Commit: `80749a8ff48a7903ec91fdb7ff306c3efd62f341`.

## Audyt II — hipotezy i terminologia

Uściślono, że odwzorowanie rodziny jest submersją poza węzłem w otoczeniu włókna szczególnego, a przestrzeń całkowita jest gładka. Pozostałe dwa wystąpienia „rezolwent” w sensie homologicznym zastąpiono „rezolucjami”. Bez nowych wyników matematycznych. Commit: `5890d7547832abd31d140c786e83c66e7a69943b`.

## Audyt III — testy regresyjne i niezależny rachunek

Dopisano regresje dotyczące lokalnego modelu Lefschetza i zachowania macierzy transwekcji przy zmianie bazy, rekonstrukcji filtracji Hodge'a, dokładności mieszanego ciągu oraz właściwej notacji pochodnych. Wykorzystano prosty rzeczywisty przykład struktury Hodge'a wagi jeden, dla którego przestrzenie rozpięte przez `(1,i)` i `(1,-i)` mają niezerowy wyznacznik `-2i`. Commit: `3f89cc2a49e1c8b00f17783c84e07e58948ddd84`.

## Audyt IV — samodzielne sformułowania

Uzupełniono dziewięć istniejących stwierdzeń i definicji o jawne dane, w szczególności kategorię abelową w lemacie o stożku i jego długim ciągu, przestrzeń racjonalną i wagę w kryterium filtracyjnym, definicję liczby Bettiego, wyraz `E_1` ciągu Hodge'a–de Rhama, punkt węzłowy `x`, włókno `F=p^{-1}(b)` w twierdzeniu Ehresmanna i `C_t=π^{-1}(t)` w twierdzeniu Picarda–Lefschetza. Commity: `df6bcbd0ddcb8d83ed5cc376902d6e7226943a20` (źródło), `a3cef48bf0737b628ff71af654b32453bfdb35e5` (regresja).

## Audyt V — matematyka, etykiety, LaTeX i PDF

- Ponownie sprawdzono stożek kompleksu i znaki długiego ciągu, brak rozszczepienia `K_e`, filtracje Hodge'a i przykład krzywej węzłowej, płaską monodromię węzła, kwadrykę `A_1`, cykliczną monodromię `z^m`, wzór Picarda–Lefschetza oraz dokładność perwersyjną jako przyjęte twierdzenie.
- **Monodromia `z^m`:** dla `2≤m≤15` niezależnie sprawdzono `T^m=I`, `det(I-T)=m` i całkowitą postać Smitha `diag(1,…,1,m)` dla `I-T`; potwierdza to `coker(T-I)≅Z/mZ`. Dla `1≤m≤19` sprawdzono `[[1,1],[0,1]]^m=[[1,m],[0,1]]`.
- **Struktura pliku:** 15 unikatowych etykiet, trzy docelowe odsyłacze (`def:nearby-vanishing-xiv`, `prop:milnor-stalk-xiv` i wcześniejszy `ch:ih-perverse-xiii`), poprawny stos środowisk, brak słów zabronionych i brak niedomkniętych konstrukcji LaTeX.
- **PDF:** kontrolna kompilacja z dołączonym TOP-24, trzy przebiegi `pdflatex`, bez błędów TeX i bez `Overfull \hbox`; wydzielony, obejrzany PDF TOP-25 — **9 stron A4**. W pomocniczym dokumencie pozostają odsyłacze z TOP-24 do niewłączonego TOP-23, ale wszystkie odsyłacze TOP-25 się rozwiązują. Osadzony rysunek monodromii nie koliduje z tekstem.
- Użyte głębokie wyniki (twierdzenie Hodge'a, Deligne'a, Ehresmanna, Milnora, Picarda–Lefschetza, perwersyjna dokładność cykli) zachowano jawnie jako **zależności dowodowe**, a nie przedstawiono ich jako udowodnionych od podstaw.

### Wynik GitHub Actions

- [AT-25/26 LaTeX — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944162229) dla źródła `df6bcbd0`.
- [AT–DG–AG dependency / label audit — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944162249) dla tego samego źródła.
- [Aplikacja biblioteki — failure](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944162227): odsyłacz `ch:arithmetization` w **LST-16 wiersz 476**, niezwiązany z TOP-25. Weryfikację ogólnego CI należy traktować jako nieukończoną niezależnie od poprawnego audytu TOP-25.
- [Najnowszy przebieg AT-25/26 z testami samodzielnych sformułowań — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944339880), commit `a3cef48b`. [Kontrola aplikacji — failure](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44944339911) z powodu tego samego niezależnego brakującego odsyłacza LST-16.

**Decyzja:** TOP-25 stabilny merytorycznie i redakcyjnie po pięciu audytach; nie dodano nowych twierdzeń ani przykładów. Zatwierdzone poprawki są na aktualnej gałęzi. Kolejny rozdział w procedurze: TOP-26.
