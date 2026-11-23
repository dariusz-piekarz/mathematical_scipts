# AA-47 — audyt I: struktura, zakres, poprawność algorytmiczna

**Data:** 23 listopada 2026 r.
**Status:** AUDYT W TOKU — NIE STABILNY.
**Źródło:** chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex.
**Zależności:** stabilne AA-43–AA-46; oświadczenie zakresu docs/pl/zakres_aa47_risch_kovacic.md.

## Kontrola I — główne zobowiązania matematyczne

1. Wybór modelu obliczeń: współczynniki powinny być reprezentowane efektywnie, z testem równości i operacjami algebraicznymi. Twierdzenia nad C nie stają się automatycznie programem działającym na nieznanych danych transcendentalnych.
2. Algorytm wymierny: rozkład na wielomian i części główne; wymierna pochodna usuwa bieguny rzędu ≥2, a proste reszty prowadzą do logarytmów. Warunek na istnienie **wymiernej** pierwotnej: wszystkie reszty zero. Elementarna pierwotna istnieje zawsze lokalnie.
3. Rothstein–Trager: przy unormowanym, bezkwadratowym mianowniku B, Res_x(B,A-z B') jest iloczynem (A(a)-z B'(a)); jego pierwiastki to residua c_a. GCD(B,A-c B') odtwarza grupy biegunów z równym residuum; wzór A/B=Σ c P'_c/P_c wynika z jednoznaczności części głównych.
4. Wykładnicza część algorytmu Rischa: redukcja przez AA-45 do r'+hr=s dla h wielomianowego. Przy h regularnym każde pole r rzędu j daje pole s rzędu j+1. Z biegunów s wyliczamy deterministycznie części główne r; pozostałość S jest wielomianem.
5. Ostatnie równanie P'+hP=S: dla deg h≥1 i S≠0 musi być deg P=deg S-deg h, dla h stałego ≠0 istnieje zamknięty wzór teleskopowy. To zamyka obie strony poprawności algorytmu nad tą klasą.
6. Redukcja y''+ay'+by=0 do z''=qz: q=a'/2+a²/4-b, poprawna reguła łańcuchowa i obustronna implikacja Riccatiego.
7. Test wymiernego Riccatiego dla q wielomianowego: każdy skończony biegun r jest prosty z residuum 1, więc r=ω+P'/P. W nieskończoności deg q parzysty 2d, dla dwóch znaków wiodących wyznaczamy ω przez dopasowanie q-ω² stopni ≥d; n=deg P jest jednoznaczny z współczynnika przy x^{d-1}; liniowe równanie na P weryfikuje wynik.
8. Granica: wykluczenie wymiernego r nie wyklucza algebraicznego stopnia 2 (q=x+5/(16x²), r=√x-1/(4x)); algorytm Kovacica w całości obejmuje również przypadki 2,4,6,12. Ich kompletność jest oznaczona jako **cytowana**, nie dowiedziona.
9. Przykład Airy'ego: brak wymiernego Riccatiego wynika z nieparzystego stopnia q=x, a brak wszystkich rozwiązań liouvillowskich z wcześniej udowodnionego silniejszego AA-46, nie z samego testu wymiernego.

## Kontrola redakcyjna i strukturalna

Ciała i obszary opisano jawnie, nie wprowadzono nowej symboliki bez definicji, zachowano standard językowy użytkownika. Wszystkie równania mogą być porównane w SymPy oraz w niezależnych modelach wymiernych; testy obliczeniowe nie zastępują ogólnych dowodów. Planowany drugi audyt skupi się na stopniu P w Riccatim, biegunach i hipotezach kompletności.

## Do zakończenia

Weryfikacja integralności AA-01–AA-47, obu testów, pełnego CI i PDF na aktualnym commicie. Dopiero wtedy możliwa decyzja o stabilizacji. Historyczne raporty przekrojowe AA-01–AA-42 nie ulegają zmianie. AA-48 nieotwarty.
