# Topologia algebraiczna — TOP-24: audyty I–V

**Data:** 21 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian na `main`).  
**Źródło:** `chapters/pl/algebraic_topology/24-homologia-przeciec-snopy-perwersyjne-i-twierdzenie-o-rozkladzi.tex`.  
**Blob źródła końcowego:** `95344b2f8a1bb6cb5ed60a848cf09cd93d904600`.  
**Zasada:** audyt istniejącej treści, bez dodawania nowych twierdzeń, lematów i sekcji merytorycznych; pełne hipotezy, dokładność dowodów, matematyka i język według wzorca DG-01; chart = mapa, mapping = odwzorowanie.

## Audyt I — wzory, kategorie i ilustracje

1. Uściślono użycie łańcuchów o nośniku zwartym na przestrzeniach niezwartych: nie należy tego mylić z brakiem lokalnej skończoności samej przestrzeni.
2. Uściślono warunek parzystości kowymiarów *osobliwych* warstw w samodualności środkowej teorii.
3. W stwierdzeniu porównawczym zapisano samodualność `D_X IC_X(k) ≅ IC_X(k)` dla stałego ciała współczynników, z orientacją zespoloną i przesunięciem perwersyjnym, zamiast nieobjaśnionego `k^vee`.
4. Nie rozszerzono nieuprawnienie konkluzji twierdzenia o rozkładzie poza jego hipotezę projektowości.
5. W przykładzie normalizacji węzła rozdzielono użycie wniosku dla `Q` i niezależnego rachunku dla dowolnego `k`.
6. Dowód rozkładu dla rozdmuchania początku `C^2` uzupełniono: półmałość, perwersyjność obrazu, półprostota z przyjętego twierdzenia o rozkładzie, jedyny składnik pełnego nośnika, wymiar kiełka w zerze, krotność punktowego składnika równa jeden.
7. Zmieniono mylący nagłówek sekcji odnoszący się do „rozdziału XIII” na „Zakres uzasadnień i przyjętych twierdzeń”.
8. Poprawiono rysunek normalizacji węzła: dwa odrębne przeciwobrazy punktu osobliwego `p_+` i `p_-` na dwóch gałęziach.

Commity: `ef5ae1237d0b5011205f1ec365078815d234b3bd` (źródło), `c91a6c483d8f853d5d99cfef7bb86b9c9086c3fa` (regresje).

## Audyt II — precyzyjny zakres twierdzenia o rozkładzie

Konkluzję sprecyzowano jako rozkład konkretnego obiektu `Rf_*Q_Y[d]` na przesunięte kompleksy przecięcia w przypadku projektowego `f`. Nie dodano nowego wyniku. Commit: `aa790110c64b369c31b2310c3b48b3e1e06b16db`.

## Audyt III — samodzielność sformułowań

Poprawiono dziewięć miejsc w definicjach, stwierdzeniach i wniosku, gdzie brakowało jawnej deklaracji `X`, `n`, `k`, `p`, `i_x`, `j`, `nu`, `f`, `d` lub nierówności małości. Szczególnie definicja łańcuchów dopuszczalnych jawnie podaje perwersyjność i współczynniki; wniosek o małych rozdzielczościach podaje warunek `codim X_r>2r` zamiast wskazania „definicja powyżej”.

Commity: `6eaa1bfc8377f8088e845ce66de8fb82cd47a672` (źródło), `1a4502655fda857cfba0b80c15c0184c53d0f45c` (regresje).

## Audyty IV–V — ponowna kontrola stabilności

- Ponownie zweryfikowano rachunki dla stożka i zawieszenia torusa, normalizacji krzywej węzłowej, dokładnego ciągu kiełków, perwersyjności snopu stałego, małości/półmałości i rozkładu rozdmuchania.
- Niezależny zestaw **82 kontroli** przeszedł: 26 unikatowych etykiet, 14 odsyłaczy rozdziału do etykiet z TOP-23 i TOP-24, rachunek diagonalny w charakterystykach 2, 3, 5, 7, 11, dualne rangi homologii przecięć, zgodność z formułą stożkową i lokalną geometrią rysunku.
- Sprawdzono również 10 zamkniętych środowisk dowodu, 7 definicji, 6 twierdzeń, 3 stwierdzenia, 9 przykładów, 1 wniosek, 7 uwag, 2 rysunki TikZ i brak słowa „karta” w znaczeniu chart.
- **3 przebiegi pdfLaTeX zakończone sukcesem; 20 stron dla TOP-23+24, 10 stron TOP-24 w wydzielonym pliku.** Bez błędów LaTeX i bez przepełnionych wierszy. Trzy ostrzeżenia o brakujących odsyłaczach pochodzą z TOP-23 wskazującego niezałączony do *pomocniczej* kompilacji TOP-22; żaden odsyłacz TOP-24 nie pozostał nierozwiązany.
- Nie stwierdzono dalszych usterek wymagających poprawek TOP-24. Źródło ma status **stabilny matematycznie i lokalnie skompilowany**, bez deklarowania samodzielnego dowodu twierdzeń głębokich.

### GitHub Actions

- [LaTeX TOP-23/24 — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943304038) dla commitu `1a450265`.
- [Kontrola AT–DG–AG — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943264044) dla commitu `6eaa1bfc`, przy tym samym końcowym blobie TOP-24.
- [Kontrola aplikacji — failure](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943304024), **niezwiązana z TOP-24**: brak nieklasyfikowanego odsyłacza `ch:arithmetization` w LST-16, wiersz 476, w ogólnym rejestrze pochodzenia odsyłaczy. Nie modyfikowano innego skryptu w ramach audytu TOP-24.

### Świadomie przyjęte zależności matematyczne

Pełne twierdzenie Goresky'ego–MacPhersona o dualności, porównanie teorii łańcuchowej i snopowej, perwersyjna struktura `t`, własności małych i półmałych odwzorowań, twierdzenie BBDG o rozkładzie oraz względne twarde Lefschetz pozostają **jawnie przyjętymi twierdzeniami**. Dowody przykładowych rachunków odnoszą się do tych wyników i nie roszczą sobie samodzielnego ich dowodzenia.

**Wynik:** TOP-24 — audyty I–V zakończone, stabilny. Następny do szczegółowego audytu: TOP-25.
