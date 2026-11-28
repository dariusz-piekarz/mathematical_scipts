# Algebra liniowa — rozdział 19, audyt IV (stabilizacyjny)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/19-postac-frobeniusa-i-czynniki-niezmiennicze.tex`  
**Blob:** `230cea2d0c9e7bd616bd7f1ed9f24e0953609a7e`  
**Poprzednie audyty:** I, II, III.

## Ostatnia kontrola przed zamknięciem

1. **Warunki i kwantyfikatory.** `K` dowolne ciało, `n<∞`, `T` endomorfizm; odróżniono `n=0` i `n≥1`. Nie stosuje się rozkładu wielomianu na czynniki liniowe.
2. **Zgodność konwencji.** Macierz `C(f)` jest zorientowana zgodnie z działaniem mnożenia przez `t` w bazie potęg; blok Smitha `K[t]/(1)` jest zerowy, a najmniejszy i największy czynnik zachowują właściwy porządek.
3. **Główne dowody.** Równość jądra prezentacji ma obie inkluzje. Postać Smitha ma indukcję z argumentem zakończenia i niezmienniki jednoznaczności. Postać Frobeniusa korzysta z prezentacji, Smitha i świadomego odrzucenia jednostek; charakterystyczny i minimalny wielomian mają osobne dowody.
4. **Odsyłacze.** Odwołania do `ch:lin16-niezmiennicze`, `thm:lin16-vector-minpoly`, `def:lin16-cyclic` i `ch:lin17-jordan` dotyczą właściwych wcześniejszych rozdziałów. Nazw etykiet nie zmieniano.
5. **Rachunki.** Dzielniki Smitha `1,t,t²`, `1,t-1,(t-1)(t-2)` oraz `1,t²+1` są zgodne z niezależnym wyliczeniem NWD minorów.
6. **Warstwa techniczna.** Liczba etykiet = liczba ich unikalnych wartości = 20; pary dowodów 7/7; odsyłacze 13. Zielony przebieg GitHub Actions `44941540440` odpowiada poprawionej wersji rozdziału i zawiera artefakt bieżącego PDF.

## Decyzja

**Audyt IV czysty:** druga kolejna niezależna kontrola bez uwag po ostatniej korekcie. Rozdział 19 uznano za **STABILNY** (4 audyty, CI SUCCESS). Jego treści nie rozszerzamy przy następnych audytach. Kolejny etap: nowy rozdział 20; po jego napisaniu przeprowadzać osobne iteracyjne audyty.
