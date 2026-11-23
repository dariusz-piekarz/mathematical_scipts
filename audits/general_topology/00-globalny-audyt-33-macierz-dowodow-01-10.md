# Topologia ogólna — globalny audyt 33: indeks wszystkich 144 dowodów rozdziałów 01–10

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Zamrożony punkt źródeł:** `c75d73d091d7967487c221724cb76db3c1bc288e`.

**Cel i metoda:** Odczytano każdy pełny plik LaTeX rozdziałów 01–10. Każde z 144 rzeczywistych wystąpień `\\begin{proof}` powiązano z bezpośrednio poprzedzającym zamkniętym środowiskiem twierdzenia, stwierdzenia, lematu, wniosku lub definicji, etykietą i numerem linii źródła. W tej iteracji dodatkowo **zweryfikowano kryptograficzny SHA-256 pełnej aktualnej zawartości źródeł 01–10** względem historycznych raportów 2/2 oraz przeczytano aktualne commity zmieniające 03, 04, 06 i 08. To rejestr *pochodzenia dokumentacji*, **nie 144 nowe niezależne dowody matematycznej poprawności**.

## Kontrola wersji starych raportów

- Rozdziały **01, 02, 05, 07, 09, 10**: obliczony z aktualnych bajtów SHA-256 **identyczny** z raportem lokalnym zakończonej stabilizacji.
- Rozdział **03**: historyczny lokalny SHA-256 **inny**; dopiero nowy audyt globalny 17 ponownie przeanalizował wszystkie 15 dowodów przy blobie `b571753b5ab9a8777424fc32f6c4a54a4048af77`, a audyt globalny 14 dokumentuje siedmiostronicowy PDF tego samego źródła. Nie przypisujemy dawnego audytu do nowego bloba.
- Rozdział **04**: historyczny SHA-256 **inny**; audyty globalne 12 i 13 przeanalizowały źródło o aktualnym blobie `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` i 17 dowodach; globalny 14 potwierdza wizualnie wydanie.
- Rozdziały **06, 08**: historyczny SHA-256 **inny**, lecz po bezpośrednim przeczytaniu patcha `5461638e212bb0efcb60e7cf136fea65bae84b8f` potwierdzono **wyłącznie zmianę sformułowań o pierwszym aksjomacie przeliczalności** (w 06: 17 dodanych i 14 usuniętych linii w patchu; w 08: 3 dodane, 2 usunięte). Nie zmieniono przesłanek logicznych, działań matematycznych ani kroków dowodowych. Historyczne 2/2 odnoszą się do wersji *sprzed* tej korekty; ciągłość matematyczna jest potwierdzona przez ręczną kontrolę patcha, **nie** przez równość SHA-256.

## Raporty referencyjne i wersje źródeł

| Rozdział | Blob bieżący | Dobrany raport | Rodzaj zgodności | Liczba dowodów |
|---|---|---|---|---:|
| 01 | `1e8ee853eb9915d96913e5a0a8cdb5e32f2ec5f6` | [`01-audyt-11.md`](01-audyt-11.md) | SHA-256 bieżącego źródła = SHA-256 raportu lokalnego; 2/2 | 9 |
| 02 | `53a8dc7e62590a9011bd5858eedb4141c5f38162` | [`02-audyt-5.md`](02-audyt-5.md) | SHA-256 bieżącego źródła = SHA-256 raportu lokalnego; 2/2 | 12 |
| 03 | `b571753b5ab9a8777424fc32f6c4a54a4048af77` | [`00-globalny-audyt-17-potwierdzenie-03.md`](00-globalny-audyt-17-potwierdzenie-03.md) | nowszy pełny audyt 15/15 na bieżącym blobie (nie starszy SHA-256) | 15 |
| 04 | `a7c1dac3b2f9dcc709a6f47bc4566d9740ef2081` | [`00-globalny-audyt-13-korekta-03-04-iteracja-02.md`](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) | nowsze czyste audyty globalne 12–13 na identycznym bieżącym blobie | 17 |
| 05 | `462acd8f3e1e350478d921429118ec19ac7f4ca8` | [`05-audyt-7.md`](05-audyt-7.md) | SHA-256 bieżącego źródła = SHA-256 raportu lokalnego; 2/2 | 16 |
| 06 | `365204000d0d5b21f213132e58b71aa48db3910e` | [`06-audyt-6.md`](06-audyt-6.md) | raport sprzed wyłącznie terminologicznego commitu 5461638e (patch ręcznie zweryfikowany) | 18 |
| 07 | `0c31028e8fd301d805781b676c6713a2572501cf` | [`07-audyt-6.md`](07-audyt-6.md) | SHA-256 bieżącego źródła = SHA-256 raportu lokalnego; 2/2 | 18 |
| 08 | `51b5cd2adf19a0345510bd14d5c0ac318cef3ae1` | [`08-audyt-5.md`](08-audyt-5.md) | raport sprzed wyłącznie terminologicznego commitu 5461638e (patch ręcznie zweryfikowany) | 15 |
| 09 | `f483271af93842198c094c95f73a68584e835215` | [`09-audyt-5.md`](09-audyt-5.md) | SHA-256 bieżącego źródła = SHA-256 raportu lokalnego; 2/2 | 10 |
| 10 | `1bc0fb72953cb70bcec7c60d3c2fc222ba1851c6` | [`10-audyt-4.md`](10-audyt-4.md) | SHA-256 bieżącego źródła = SHA-256 raportu lokalnego; 2/2 | 14 |

## Macierz pojedynczych środowisk dowodowych

Każdy wiersz odpowiada dokładnie jednemu środowisku `proof` z aktualnego źródła. Pole „raport” oznacza **odniesienie rozdziałowe**, nie gwarancję, że istnieje oddzielny protokół matematyczny tego konkretnego kroku. Numer linii jest na zamrożonym commitcie.

### Rozdział 01 — 9 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 01-01 | 180 | `stwierdzenie` | `prop:topog-kule-otwarte-sfery-domkniete` | [audyt 01](01-audyt-11.md) |
| 01-02 | 244 | `stwierdzenie` | `prop:topog-topologia-metryczna` | [audyt 01](01-audyt-11.md) |
| 01-03 | 319 | `stwierdzenie` | `prop:topog-zbiory-domkniete` | [audyt 01](01-audyt-11.md) |
| 01-04 | 475 | `stwierdzenie` | `prop:topog-otoczenia` | [audyt 01](01-audyt-11.md) |
| 01-05 | 548 | `twierdzenie` | `thm:topog-kryterium-bazy` | [audyt 01](01-audyt-11.md) |
| 01-06 | 593 | `stwierdzenie` | `prop:topog-otwartosc-przez-baze` | [audyt 01](01-audyt-11.md) |
| 01-07 | 681 | `twierdzenie` | `thm:topog-podbaza-konstrukcja` | [audyt 01](01-audyt-11.md) |
| 01-08 | 759 | `stwierdzenie` | `prop:topog-porownanie-bazy` | [audyt 01](01-audyt-11.md) |
| 01-09 | 812 | `twierdzenie` | `thm:topog-przeciecia-topologii` | [audyt 01](01-audyt-11.md) |

### Rozdział 02 — 12 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 02-01 | 63 | `stwierdzenie` | `prop:topog-ekstremalne` | [audyt 02](02-audyt-5.md) |
| 02-02 | 95 | `twierdzenie` | `thm:topog-punktowa-charakteryzacja` | [audyt 02](02-audyt-5.md) |
| 02-03 | 156 | `twierdzenie` | `thm:topog-rachunek-wnetrz-domkniec` | [audyt 02](02-audyt-5.md) |
| 02-04 | 212 | `stwierdzenie` | `prop:topog-dualnosc-wnetrze-domkniecie` | [audyt 02](02-audyt-5.md) |
| 02-05 | 260 | `twierdzenie` | `thm:topog-charakteryzacja-brzegu` | [audyt 02](02-audyt-5.md) |
| 02-06 | 356 | `stwierdzenie` | `prop:topog-brzeg-sumy` | [audyt 02](02-audyt-5.md) |
| 02-07 | 404 | `twierdzenie` | `thm:topog-domkniecie-pochodny` | [audyt 02](02-audyt-5.md) |
| 02-08 | 447 | `stwierdzenie` | `prop:topog-pochodny-monotoniczny` | [audyt 02](02-audyt-5.md) |
| 02-09 | 468 | `twierdzenie` | `thm:topog-pochodny-t1` | [audyt 02](02-audyt-5.md) |
| 02-10 | 543 | `twierdzenie` | `thm:topog-gesty-kryteria` | [audyt 02](02-audyt-5.md) |
| 02-11 | 599 | `stwierdzenie` | `prop:topog-nigdziegesty-sumy` | [audyt 02](02-audyt-5.md) |
| 02-12 | 690 | `twierdzenie` | `thm:topog-kuratowski` | [audyt 02](02-audyt-5.md) |

### Rozdział 03 — 15 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 03-01 | 93 | `twierdzenie` | `thm:topog-ciaglosc-kryteria-globalne` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-02 | 131 | `stwierdzenie` | `prop:topog-ciaglosc-wnetrze` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-03 | 162 | `twierdzenie` | `thm:topog-ciaglosc-punktowa-globalna` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-04 | 197 | `twierdzenie` | `thm:topog-ciaglosc-eps-delta` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-05 | 259 | `twierdzenie` | `thm:topog-ciaglosc-bazy-podbazy` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-06 | 305 | `stwierdzenie` | `prop:topog-porownanie-przez-ciaglosc` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-07 | 334 | `twierdzenie` | `thm:topog-skladanie-ciaglych` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-08 | 366 | `stwierdzenie` | `prop:topog-ograniczanie-ciaglosci` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-09 | 388 | `twierdzenie` | `thm:topog-ciaglosc-lokalna-pokrycie` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-10 | 410 | `twierdzenie` | `thm:topog-sklejanie-domkniete` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-11 | 472 | `stwierdzenie` | `prop:topog-otwarte-domkniete-kryteria` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-12 | 518 | `stwierdzenie` | `prop:topog-skladanie-otwartych-domknietych` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-13 | 549 | `twierdzenie` | `thm:topog-homeomorfizm-kryteria` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-14 | 591 | `stwierdzenie` | `prop:topog-homeomorfizm-operacje` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |
| 03-15 | 648 | `stwierdzenie` | `prop:topog-zanurzenie-kryterium` | [audyt 03](00-globalny-audyt-17-potwierdzenie-03.md) |

### Rozdział 04 — 17 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 04-01 | 32 | `stwierdzenie` | `prop:topog-podprzestrzen-topologia` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-02 | 85 | `stwierdzenie` | `prop:topog-podprzestrzen-domkniecie` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-03 | 112 | `stwierdzenie` | `prop:topog-podprzestrzen-wnetrze` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-04 | 142 | `stwierdzenie` | `prop:topog-podprzestrzen-przechodniosc` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-05 | 159 | `twierdzenie` | `thm:topog-do-podprzestrzeni` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-06 | 200 | `twierdzenie` | `thm:topog-iloczyn-baza` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-07 | 263 | `twierdzenie` | `thm:topog-iloczyn-uniwersalnosc` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-08 | 282 | `stwierdzenie` | `prop:topog-rzutowania-otwarte` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-09 | 305 | `stwierdzenie` | `prop:topog-iloczyn-domkniecie` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-10 | 355 | `stwierdzenie` | `prop:topog-suma-rozlaczna-topologia` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-11 | 382 | `twierdzenie` | `thm:topog-suma-uniwersalnosc` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-12 | 432 | `twierdzenie` | `thm:topog-poczatkowa-uniwersalnosc` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-13 | 473 | `stwierdzenie` | `prop:topog-koncowa-topologia` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-14 | 493 | `twierdzenie` | `thm:topog-koncowa-uniwersalnosc` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-15 | 554 | `stwierdzenie` | `prop:topog-iloraz-nasycone` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-16 | 574 | `twierdzenie` | `thm:topog-iloraz-uniwersalnosc` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |
| 04-17 | 592 | `stwierdzenie` | `prop:topog-otwarta-surjekcja-iloraz` | [audyt 04](00-globalny-audyt-13-korekta-03-04-iteracja-02.md) |

### Rozdział 05 — 16 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 05-01 | 87 | `stwierdzenie` | `prop:topog-t2-t1-t0` | [audyt 05](05-audyt-7.md) |
| 05-02 | 108 | `twierdzenie` | `thm:topog-t1-singletony` | [audyt 05](05-audyt-7.md) |
| 05-03 | 129 | `wniosek` | `cor:topog-skonczone-t1` | [audyt 05](05-audyt-7.md) |
| 05-04 | 156 | `stwierdzenie` | `prop:topog-przekatna-hausdorff` | [audyt 05](05-audyt-7.md) |
| 05-05 | 181 | `twierdzenie` | `thm:topog-rownosc-na-gestym` | [audyt 05](05-audyt-7.md) |
| 05-06 | 221 | `stwierdzenie` | `prop:topog-regularnosc-zwezanie` | [audyt 05](05-audyt-7.md) |
| 05-07 | 239 | `wniosek` | `cor:topog-t3-t2` | [audyt 05](05-audyt-7.md) |
| 05-08 | 313 | `stwierdzenie` | `prop:topog-calkowita-regularnosc-regularna` | [audyt 05](05-audyt-7.md) |
| 05-09 | 511 | `stwierdzenie` | `prop:topog-normalnosc-zwezanie` | [audyt 05](05-audyt-7.md) |
| 05-10 | 529 | `twierdzenie` | `thm:topog-urysohn` | [audyt 05](05-audyt-7.md) |
| 05-11 | 600 | `wniosek` | `cor:topog-t4-tych` | [audyt 05](05-audyt-7.md) |
| 05-12 | 641 | `twierdzenie` | `thm:topog-tietze` | [audyt 05](05-audyt-7.md) |
| 05-13 | 790 | `twierdzenie` | `thm:topog-metryczne-t4` | [audyt 05](05-audyt-7.md) |
| 05-14 | 826 | `stwierdzenie` | `prop:topog-oddzielanie-dziedziczenie` | [audyt 05](05-audyt-7.md) |
| 05-15 | 875 | `twierdzenie` | `thm:topog-sorgenfrey-plane` | [audyt 05](05-audyt-7.md) |
| 05-16 | 947 | `stwierdzenie` | `prop:topog-oddzielanie-hierarchia` | [audyt 05](05-audyt-7.md) |

### Rozdział 06 — 18 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 06-01 | 37 | `stwierdzenie` | `prop:topog-ciag-baza` | [audyt 06](06-audyt-6.md) |
| 06-02 | 53 | `stwierdzenie` | `prop:topog-ciag-metryka` | [audyt 06](06-audyt-6.md) |
| 06-03 | 104 | `stwierdzenie` | `prop:topog-ciag-podciag-ciaglosc` | [audyt 06](06-audyt-6.md) |
| 06-04 | 118 | `twierdzenie` | `thm:topog-ciag-hausdorff` | [audyt 06](06-audyt-6.md) |
| 06-05 | 156 | `stwierdzenie` | `prop:topog-ciagi-domkniecie` | [audyt 06](06-audyt-6.md) |
| 06-06 | 197 | `twierdzenie` | `thm:topog-pierwsza-przeliczalnosc-domkniecie` | [audyt 06](06-audyt-6.md) |
| 06-07 | 225 | `twierdzenie` | `thm:topog-ciagowe-kryterium-ciaglosci` | [audyt 06](06-audyt-6.md) |
| 06-08 | 351 | `stwierdzenie` | `prop:topog-siec-ciaglosc-jeden-kierunek` | [audyt 06](06-audyt-6.md) |
| 06-09 | 373 | `twierdzenie` | `thm:topog-siec-domkniecie` | [audyt 06](06-audyt-6.md) |
| 06-10 | 418 | `twierdzenie` | `thm:topog-siec-kryterium-ciaglosci` | [audyt 06](06-audyt-6.md) |
| 06-11 | 441 | `twierdzenie` | `thm:topog-sieci-hausdorff` | [audyt 06](06-audyt-6.md) |
| 06-12 | 541 | `stwierdzenie` | `prop:topog-podsiec-granica` | [audyt 06](06-audyt-6.md) |
| 06-13 | 564 | `twierdzenie` | `thm:topog-punkt-skupienia-podsiec` | [audyt 06](06-audyt-6.md) |
| 06-14 | 614 | `twierdzenie` | `thm:topog-siec-iloczyn` | [audyt 06](06-audyt-6.md) |
| 06-15 | 657 | `definicja` (nazwany: Uzasadnienie konstrukcji filtru z bazy) | `def:topog-filtr` | [audyt 06](06-audyt-6.md) |
| 06-16 | 693 | `twierdzenie` | `thm:topog-filtr-domkniecie` | [audyt 06](06-audyt-6.md) |
| 06-17 | 731 | `twierdzenie` | `thm:topog-sieci-filtry` | [audyt 06](06-audyt-6.md) |
| 06-18 | 784 | `wniosek` | `cor:topog-filtr-ciaglosc-hausdorff` | [audyt 06](06-audyt-6.md) |

### Rozdział 07 — 18 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 07-01 | 44 | `stwierdzenie` | `prop:topog-zwartosc-wzgledna` | [audyt 07](07-audyt-6.md) |
| 07-02 | 106 | `twierdzenie` | `thm:topog-zwartosc-odcinek` | [audyt 07](07-audyt-6.md) |
| 07-03 | 148 | `twierdzenie` | `thm:topog-zwartosc-fip` | [audyt 07](07-audyt-6.md) |
| 07-04 | 179 | `twierdzenie` | `thm:topog-zwartosc-trwalosc` | [audyt 07](07-audyt-6.md) |
| 07-05 | 200 | `twierdzenie` | `thm:topog-zwartosc-hausdorff-domkniete` | [audyt 07](07-audyt-6.md) |
| 07-06 | 243 | `twierdzenie` | `thm:topog-weierstrass-kresy` | [audyt 07](07-audyt-6.md) |
| 07-07 | 289 | `twierdzenie` | `thm:topog-zwartosc-hausdorff-normalna` | [audyt 07](07-audyt-6.md) |
| 07-08 | 334 | `wniosek` | `cor:topog-zwartosc-bijekcja-homeomorfizm` | [audyt 07](07-audyt-6.md) |
| 07-09 | 376 | `stwierdzenie` | `prop:topog-zwartosc-podsiec` | [audyt 07](07-audyt-6.md) |
| 07-10 | 426 | `twierdzenie` | `thm:topog-zwartosc-sieci` | [audyt 07](07-audyt-6.md) |
| 07-11 | 496 | `lemat` | `lem:topog-zwartosc-ultrafiltr-alternatywa` | [audyt 07](07-audyt-6.md) |
| 07-12 | 523 | `lemat` | `lem:topog-zwartosc-ultrafiltr-zorn` | [audyt 07](07-audyt-6.md) |
| 07-13 | 545 | `twierdzenie` | `thm:topog-zwartosc-ultrafiltry` | [audyt 07](07-audyt-6.md) |
| 07-14 | 606 | `twierdzenie` | `thm:topog-tychonoff-iloczyny` | [audyt 07](07-audyt-6.md) |
| 07-15 | 657 | `stwierdzenie` | `prop:topog-zwartosc-iloczyn-skonczony` | [audyt 07](07-audyt-6.md) |
| 07-16 | 674 | `twierdzenie` | `thm:topog-heine-borel` | [audyt 07](07-audyt-6.md) |
| 07-17 | 757 | `twierdzenie` | `thm:topog-zwartosc-zanurzenie-kostka` | [audyt 07](07-audyt-6.md) |
| 07-18 | 856 | `wniosek` | `cor:topog-zwartosc-uzwarcenie` | [audyt 07](07-audyt-6.md) |

### Rozdział 08 — 15 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 08-01 | 40 | `twierdzenie` | `thm:topog-spojnosc-charakteryzacje` | [audyt 08](08-audyt-5.md) |
| 08-02 | 88 | `twierdzenie` | `thm:topog-spojnosc-przedzialy` | [audyt 08](08-audyt-5.md) |
| 08-03 | 135 | `twierdzenie` | `thm:topog-spojnosc-obraz-ciagly` | [audyt 08](08-audyt-5.md) |
| 08-04 | 157 | `wniosek` | `cor:topog-spojnosc-wartosci-posredniej` | [audyt 08](08-audyt-5.md) |
| 08-05 | 174 | `wniosek` | `cor:topog-spojnosc-zwarty-przedzial` | [audyt 08](08-audyt-5.md) |
| 08-06 | 194 | `twierdzenie` | `thm:topog-spojnosc-suma` | [audyt 08](08-audyt-5.md) |
| 08-07 | 233 | `twierdzenie` | `thm:topog-spojnosc-domkniecie` | [audyt 08](08-audyt-5.md) |
| 08-08 | 267 | `twierdzenie` | `thm:topog-spojnosc-iloczyn` | [audyt 08](08-audyt-5.md) |
| 08-09 | 353 | `twierdzenie` | `thm:topog-spojnosc-skladowe` | [audyt 08](08-audyt-5.md) |
| 08-10 | 487 | `lemat` | `lem:topog-spojnosc-skladanie-drog` | [audyt 08](08-audyt-5.md) |
| 08-11 | 512 | `twierdzenie` | `thm:topog-spojnosc-droga-implikuje` | [audyt 08](08-audyt-5.md) |
| 08-12 | 562 | `stwierdzenie` | `prop:topog-spojnosc-skladowe-drogowe` | [audyt 08](08-audyt-5.md) |
| 08-13 | 718 | `twierdzenie` | `thm:topog-spojnosc-lokalna-komponenty` | [audyt 08](08-audyt-5.md) |
| 08-14 | 754 | `wniosek` | `cor:topog-spojnosc-lokalna-drogowa` | [audyt 08](08-audyt-5.md) |
| 08-15 | 775 | `wniosek` | `cor:topog-spojnosc-euklidesowe` | [audyt 08](08-audyt-5.md) |

### Rozdział 09 — 10 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 09-01 | 44 | `twierdzenie` | `thm:topog-druga-pierwsza` | [audyt 09](09-audyt-5.md) |
| 09-02 | 80 | `twierdzenie` | `thm:topog-przeliczalnosc-dziedziczenie` | [audyt 09](09-audyt-5.md) |
| 09-03 | 105 | `twierdzenie` | `thm:topog-druga-iloczyn-przeliczalny` | [audyt 09](09-audyt-5.md) |
| 09-04 | 177 | `twierdzenie` | `thm:topog-druga-osrodkowa-lindelof` | [audyt 09](09-audyt-5.md) |
| 09-05 | 229 | `twierdzenie` | `thm:topog-osrodk-lindelof-zachowanie` | [audyt 09](09-audyt-5.md) |
| 09-06 | 304 | `twierdzenie` | `thm:topog-metryczne-trzy-warunki` | [audyt 09](09-audyt-5.md) |
| 09-07 | 351 | `wniosek` | `cor:topog-osrodkowa-metryczna-baza` | [audyt 09](09-audyt-5.md) |
| 09-08 | 406 | `twierdzenie` | `thm:topog-sorgenfrey-wlasnosci-przeliczalnosc` | [audyt 09](09-audyt-5.md) |
| 09-09 | 477 | `wniosek` | `cor:topog-sorgenfrey-trzy-nie-druga` | [audyt 09](09-audyt-5.md) |
| 09-10 | 617 | `stwierdzenie` | `prop:topog-przeliczalnosc-hierarchia` | [audyt 09](09-audyt-5.md) |

### Rozdział 10 — 14 dowodów

| ID | Linia początku | Środowisko | Etykieta twierdzenia / definicji | Raport źródłowy |
|---|---:|---|---|---|
| 10-01 | 45 | `stwierdzenie` | `prop:topog-baza-kul` | [audyt 10](10-audyt-4.md) |
| 10-02 | 90 | `stwierdzenie` | `prop:topog-metryka-t3-pierwszy` | [audyt 10](10-audyt-4.md) |
| 10-03 | 135 | `stwierdzenie` | `prop:topog-min-metryka` | [audyt 10](10-audyt-4.md) |
| 10-04 | 155 | `twierdzenie` | `thm:topog-metryzowalnosc-podprzestrzenie` | [audyt 10](10-audyt-4.md) |
| 10-05 | 173 | `stwierdzenie` | `prop:topog-metryzowalnosc-homeo` | [audyt 10](10-audyt-4.md) |
| 10-06 | 197 | `lemat` | `lem:topog-t3-lindelof-normalna` | [audyt 10](10-audyt-4.md) |
| 10-07 | 245 | `wniosek` | `cor:topog-drugi-t3-t4` | [audyt 10](10-audyt-4.md) |
| 10-08 | 261 | `twierdzenie` | `thm:topog-urysohn-metryzowalnosc` | [audyt 10](10-audyt-4.md) |
| 10-09 | 413 | `wniosek` | `cor:topog-drugi-metryzowalna-iff-t3` | [audyt 10](10-audyt-4.md) |
| 10-10 | 433 | `twierdzenie` | `thm:topog-metryka-kostka-przeliczalna` | [audyt 10](10-audyt-4.md) |
| 10-11 | 484 | `wniosek` | `cor:topog-urysohn-kostka-hilberta` | [audyt 10](10-audyt-4.md) |
| 10-12 | 518 | `twierdzenie` | `thm:topog-przeliczalny-iloczyn-metryzowalny` | [audyt 10](10-audyt-4.md) |
| 10-13 | 578 | `wniosek` | `cor:topog-zwarta-hausdorff-metryzowalna` | [audyt 10](10-audyt-4.md) |
| 10-14 | 737 | `stwierdzenie` | `prop:topog-metryzowalnosc-zestawienie` | [audyt 10](10-audyt-4.md) |

## Wynik i następne kroki

- **144/144 dowodów** mają pozycję, linię, otaczający wynik, etykietę i wskazanie właściwego raportu, a każdy z 10 rozdziałów jawny blob.
- Uważnie rozróżniono SHA-256 plików użytkownika od SHA-1 blobów Git: nie wolno ich porównywać bezpośrednio. Rozbieżności SHA-256 03/04/06/08 są wyjaśnione konkretną historią lub nową kontrolą na aktualnym blobie.
- **Dowód 06-15** jest nazwanym „Uzasadnieniem konstrukcji filtru z bazy” po środowisku `definicja`; nie należy go przypisywać omyłkowo do poprzedniego twierdzenia o zbieżności w iloczynie.
- **Konieczne do pełnego globalnego PASS:** analogiczny indeks 11–26, niezależna kontrola *zakresu matematycznego* każdego raportu, szczególnie tych opisujących tylko próbki lub selekcję wyników, i końcowe sprawdzenie PDF/CI. Sama macierz 144 wierszy nie oznacza 144 nowych pełnych audytów.
