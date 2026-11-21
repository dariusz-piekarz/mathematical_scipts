# Topologia algebraiczna — TOP-26, audyty I–V

**Data:** 21 listopada 2026.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmiany `main`).  
**Rozdział:** `chapters/pl/algebraic_topology/26-wariacje-struktur-hodge-a-koneksja-gaussa-manina-i-degeneracje.tex`.  
**Zweryfikowany końcowy blob źródła:** `b1448a445e5f0d158ad469fab16f57e9894a59e8`.  
**Standard:** kontrola istniejącego materiału na poziomie DG-01, bez dodawania nowych twierdzeń. Każdy istotny wzór w dowodzie ma wyprowadzenie albo jawnie wskazaną zależność.

## Audyt I: geometryczne hipotezy i konwencje

- **Quasi-unipotencja:** zastąpiono niewystarczający opis „rodziny algebraicznej nad przebitym dyskiem” samodzielnymi założeniami: gładka krzywa algebraiczna `S`, punkt `p` w gładkim zwartym uzupełnieniu, projektowa gładka rodzina nad `S`, lokalny parametr `t`, monodromia `R^k f_*Q` wokół `p`. Nie przedstawiono ogólnego twierdzenia jako konsekwencji samej płaskiej koneksji.
- **Graniczna mieszana struktura Hodge'a:** jawnie zapisano konwencję `F(z+1)=T F(z)`, indeksowanie `W(N,k)` i warunki `NW_j⊆W_{j-2}`, `N^r:Gr_{k+r}^W→Gr_{k-r}^W` będące izomorfizmami. Usunięto dwuznaczne `W(N)[-k]`.
- **Polaryzowana wariacja:** doprecyzowano `(-1)^m`-symetrię płaskiego parowania i warunki dodatniości Hodge'a.
- **Wiązka Gaussa–Manina:** zapisano związek lokalnego systemu całkowitego z zespolonym i uściślono, że różniczkowanie okresu stosuje się do holomorficznego przekroju.
- Skorygowano nazewnictwo przestrzeni stopniowanych filtracji i domenę zmiennej `q` w podstawieniu rozgałęzionym.

Commit `f4fbb5b892605b8c63c1f8834893419ec9742604`.

## Audyt II: samodzielność sformułowań

W dziewięciu fragmentach dopisano jawne przestrzenie, współczynniki, parametry lub morfizmy: lokalny system z płaską koneksją, definicję Gaussa–Manina, różniczkowanie okresów, wariację z rodziny projektowej, ogólną konstrukcję Picarda–Fuchsa, okres rzeczywisty Legendre'a, równanie okresów oraz filtrację monodromiczną w rzędzie dwa. Rozróżniono holomorficzną wiązkę z lokalnego systemu i algebraiczną wiązkę de Rhama `H^k_dR(𝓧/S)`. Ustalone w rozdziale symbole nie są już pozostawione bez określenia w kluczowych wynikach.

Commit `ce26a541457e156cff6a933cf7c961dca1e21457`.

## Audyt III: testy chroniące poprawki

Dodano regresje brzegowej hipotezy twierdzenia o monodromii, przesunięcia wag o centrum `k`, zgodności `R^k f_*C` z lokalnym systemem zespolonym, polaryzacji i jawnych danych rodziny i okresów. Niezależnie zweryfikowano na przykładzie Legendre'a dla `1≤q≤39` wzory `T_q=I+qN` i `N_q=qN`, dla `0≤n≤35` rekurencję współczynników hipergeometrycznych oraz wrońskian przy `λ=1/2`.

Commit `d99e0adecabf51cd364db1b9aab721516fa30f6e`.

## Audyt IV: usunięcie przeskoków dowodowych

1. W różniczkowaniu okresów zaznaczono, że bazą jest krzywa, więc lokalny dysk ma rzeczywiście jeden parametr.
2. Wyprowadzono rekurencję całek beta z `u=sin²θ`, `I_0=π/2` i `I_n=(2n−1)I_{n−1}/(2n)` zamiast samego przywołania „klasycznej rekurencji”.
3. W dowodzie równania Picarda–Fuchsa jawnie powołano się na `dim_C H_1(E_λ;C)=2`, co uzasadnia, że dwie liniowo niezależne funkcje okresowe rozpinają wszystkie lokalne funkcje okresowe.
4. W twierdzeniu o granicznej mieszanej strukturze Hodge'a jawnie wybrano punkt bazowy i zdefiniowano `V_Q=V_{Z,t0}⊗Q`.

Commit `909824266588cc0464702d1d13e5780a09d0f786`.

## Audyt V: kontrola stabilności, matematyką i PDF

- Ponowne sprawdzenie 15 etykiet (15 unikatowych), 11 odsyłaczy (wszystkie rozwiązane przez TOP-25 lub TOP-26), środowisk LaTeX (47 rozpoczęć i 47 zakończeń), dwóch rysunków TikZ, ograniczeń terminologicznych: 0 starych „rezolwent”, nieużywanych „tensorowań”, „sekwencji”, „kart” jako chart ani „map” jako odwzorowań.
- Niezależne sprawdzenie rekurencji beta dla `1≤n≤60`; wszystkie 60 zgodne. Dwa wykresy/diagramy i wszystkie strony wynikowego PDF obejrzane wizualnie: bez obcięć i nakładania tekstu.
- **PDF:** pomocniczy dokument z TOP-25 i TOP-26 kompilowany trzykrotnie (`pdflatex`); 18 stron łącznie, wyodrębniony TOP-26 ma 9 stron. **0 błędów TeX, 0 przepełnionych wierszy.** Trzy ostrzeżenia o referencjach dotyczą TOP-25 i wskazują niezałączony do kompilacji pomocniczej TOP-24. Wszystkie 11 odsyłaczy TOP-26 są rozwiązane.
- Zewnętrzne wyniki pozostają jawnie wskazane: twierdzenie o wariacjach Hodge'a z rodzin projektowych, twierdzenia o bazowej zmianie i regularności, quasi-unipotencja monodromii, twierdzenie Schmida o granicznej mieszanej strukturze Hodge'a.
- Dodano regresję rekurencji beta, niezależności okresów i jawnej definicji `V_Q`. Commit `77031a68a161ef49bf712d21024acad091e054fd`.

### GitHub Actions i zakres statusu

- [AT-25/26 LaTeX — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44945029706), commit `90982426`: ta sama końcowa wersja źródła TOP-26.
- [AT–DG–AG odsyłacze — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44945029690).
- [Audyt TOP-27/28 — success](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44945029695).
- [Ogólna kontrola aplikacji — failure](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44945029710). Z logu wynika **niezaklasyfikowany brakujący odsyłacz `ch:representability-diagonal` w LST-17, wiersz 335**. Nie jest związany z TOP-26. Nie należy nazywać całego CI zielonym.
- Wynik uruchomienia po dodaniu samej regresji `77031a68` należy sprawdzić niezależnie; matematyka oraz końcowy blob źródła nie zmieniły się.

**Wynik:** TOP-26 po pięciu audytach stabilny matematycznie i redakcyjnie; nie dodano nowych twierdzeń, lematów ani przykładów. Następny w kolejności TOP-27.
