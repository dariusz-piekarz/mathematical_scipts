# Topologia ogólna — globalny audyt 34: macierz 71 dowodów rozdziałów 11–18

**Data:** 2026-11-23. **Wersja odniesienia:** commit `c75d73d091d7967487c221724cb76db3c1bc288e`. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

Przeprowadzono audyt pochodzenia **każdego z 71 środowisk `proof`**. Dla każdego odczytano linię rozpoczęcia, etykietę zamkniętego bezpośrednio wcześniejszego twierdzenia/lematu/stwierdzenia/definicji, aktualny SHA pliku i właściwy istniejący raport. Raporty te dokumentują wcześniejsze rzeczywiste audyty; poniższa tabela **nie jest 71 nowymi niezależnymi matematycznymi sprawdzeniami**. Wszystkie źródła pochodzą z jednego zamrożonego commitu.

## Zgodność wersji i raportów

| Rozdział | Aktualny blob | Raport | Interpretacja zakresu | Proof |
|---|---|---|---|---:|
| 11 | `8f13420add065dca19d2653c86b0e5781aef2fe7` | [`11-zupelnosc-i-baire-iteracja-07.md`](11-zupelnosc-i-baire-iteracja-07.md) | regresja po przeniesieniu twierdzenia o lokalnej zwartości do rozdziału 14 | 8 |
| 12 | `13597073db07742089b82ae3fc9878733dea5e88` | [`12-przestrzenie-jednostajne-iteracja-04.md`](12-przestrzenie-jednostajne-iteracja-04.md) | pełny audyt 14/14 na identycznym blobie | 14 |
| 13 | `c9078636452731e42a56196e84b5ed9831120e6b` | [`13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md`](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) | po korekcie: 2 czyste 07–08 + potwierdzający 09 | 9 |
| 14 | `24ca61f0e19fe6674719fc76e53073aa82cc755c` | [`00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md`](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) | pełny audyt 7/7 | 7 |
| 15 | `82e0fb5be75489017c8ea1844c698c87ce580901` | [`00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md`](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) | pełny audyt 7/7 | 7 |
| 16 | `1c2fcb925d62120feaea468400e48842a508a062` | [`00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md`](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) | pełny audyt 7/7 | 7 |
| 17 | `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4` | [`00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md`](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) | pełny audyt 10/10 | 10 |
| 18 | `f7340514548ed3dfb5d98793bf7068fd84276c30` | [`00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md`](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) | pełny audyt 9/9 | 9 |

Rozdział 11 został wcześniej skrócony przez przeniesienie dowodu wersji lokalnie zwartej twierdzenia Baire'a do rozdziału 14, z zachowaniem etykiet. Audyt 11/07 potwierdza tę operację; dlatego **8 dowodów w 11 i 7 w 14** liczymy według obecnego położenia, bez podwójnego naliczania przeniesionego materiału.
Rozdział 13 zawiera wersję **po korekcie relacji niesymetrycznej**, aktualny blob `c9078636452731e42a56196e84b5ed9831120e6b`. Historyczne raporty na innym blobie nie stanowią dowodu na aktualnej wersji; bazą jest audyt 13/06 i osobny cykl 07–09 (2+1) oraz PASS testu asymetrii.

## Rozdział 11: 8 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 11-01 | 32 | `stwierdzenie` | `prop:topog-baire-zbiezny-cauchy` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-02 | 47 | `twierdzenie` | `thm:topog-baire-podprzestrzen-zupelna` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-03 | 152 | `stwierdzenie` | `prop:topog-baire-rownowaznosci` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-04 | 186 | `twierdzenie` | `thm:topog-baire-metryczne` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-05 | 243 | `wniosek` | `cor:topog-baire-zupelnie-metryzowalne` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-06 | 267 | `twierdzenie` | `thm:topog-baire-wymierne-nie-gdelta` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-07 | 301 | `stwierdzenie` | `prop:topog-baire-otwarte-podprzestrzenie` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |
| 11-08 | 335 | `wniosek` | `cor:topog-baire-domkniete` | [11-zupelnosc-i-baire-iteracja-07.md](11-zupelnosc-i-baire-iteracja-07.md) |

## Rozdział 12: 14 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 12-01 | 62 | `lemat` | `lem:topog-jednostajne-symetryczne` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-02 | 100 | `twierdzenie` | `thm:topog-jednostajne-topologia` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-03 | 146 | `twierdzenie` | `thm:topog-jednostajne-hausdorff` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-04 | 175 | `wniosek` | `cor:topog-jednostajne-skrajne-topologie` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-05 | 202 | `twierdzenie` | `thm:topog-jednostajne-pseudometryka` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-06 | 285 | `twierdzenie` | `thm:topog-jednostajne-podprzestrzen` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-07 | 323 | `twierdzenie` | `thm:topog-jednostajne-iloczyn` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-08 | 398 | `twierdzenie` | `thm:topog-jednostajne-ciaglosc-wlasnosci` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-09 | 436 | `lemat` | `lem:topog-jednostajne-zwarta-ciagowa` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-10 | 471 | `twierdzenie` | `thm:topog-jednostajne-heine-cantor` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-11 | 524 | `twierdzenie` | `thm:topog-jednostajne-ogony` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-12 | 549 | `twierdzenie` | `thm:topog-jednostajne-zbiezna-cauchy` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-13 | 572 | `stwierdzenie` | `prop:topog-jednostajne-f-cauchy` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |
| 12-14 | 591 | `twierdzenie` | `thm:topog-jednostajne-produkt-cauchy` | [12-przestrzenie-jednostajne-iteracja-04.md](12-przestrzenie-jednostajne-iteracja-04.md) |

## Rozdział 13: 9 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 13-01 | 39 | `twierdzenie` | `thm:topog-uzupelnienia-filtry-sieci` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-02 | 78 | `stwierdzenie` | `prop:topog-uzupelnienia-metryczna` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-03 | 133 | `twierdzenie` | `thm:topog-uzupelnienia-metryczne` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-04 | 219 | `lemat` | `lem:topog-uzupelnienia-rownowaznosc` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-05 | 258 | `lemat` | `lem:topog-uzupelnienia-minimalizacja` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-06 | 329 | `twierdzenie` | `thm:topog-uzupelnienia-istnienie` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-07 | 585 | `lemat` | `lem:topog-uzupelnienia-rozszerzenie` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-08 | 658 | `twierdzenie` | `thm:topog-uzupelnienia-uniwersalnosc` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |
| 13-09 | 689 | `twierdzenie` | `thm:topog-uzupelnienia-podprzestrzenie` | [13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md](13-zupelnosc-jednostajna-iteracja-09-audyt-potwierdzajacy.md) |

## Rozdział 14: 7 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 14-01 | 33 | `lemat` | `lem:topog-baire-zwarte-domkniecie` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |
| 14-02 | 61 | `twierdzenie` | `thm:topog-baire-lokalnie-zwarte` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |
| 14-03 | 102 | `stwierdzenie` | `prop:topog-lokalna-podprzestrzenie` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |
| 14-04 | 133 | `stwierdzenie` | `prop:topog-lokalna-iloczyny` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |
| 14-05 | 157 | `twierdzenie` | `thm:topog-lokalna-dowolny-iloczyn` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |
| 14-06 | 268 | `twierdzenie` | `thm:topog-lokalna-wyczerpanie` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |
| 14-07 | 331 | `stwierdzenie` | `prop:topog-lokalna-drugi-aksjomat` | [00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md](00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md) |

## Rozdział 15: 7 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 15-01 | 55 | `stwierdzenie` | `prop:topog-parazwartosc-domkniecia` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |
| 15-02 | 130 | `stwierdzenie` | `prop:topog-parazwartosc-jednosc-pokrycie` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |
| 15-03 | 159 | `lemat` | `lem:topog-parazwartosc-odciecia` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |
| 15-04 | 185 | `twierdzenie` | `thm:topog-parazwartosc-lindelof` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |
| 15-05 | 276 | `wniosek` | `cor:topog-parazwartosc-klasy` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |
| 15-06 | 341 | `twierdzenie` | `thm:topog-parazwartosc-stone` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |
| 15-07 | 507 | `twierdzenie` | `thm:topog-parazwartosc-nagata-smirnow` | [00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md](00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md) |

## Rozdział 16: 7 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 16-01 | 29 | `definicja` | `def:topog-uzwarcenia-topologia-poczatkowa` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |
| 16-02 | 50 | `stwierdzenie` | `prop:topog-uzwarcenia-poczatkowa-ciaglosc` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |
| 16-03 | 77 | `twierdzenie` | `thm:topog-uzwarcenia-funkcyjny-opis` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |
| 16-04 | 173 | `twierdzenie` | `thm:topog-uzwarcenia-istnienie` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |
| 16-05 | 222 | `stwierdzenie` | `prop:topog-uzwarcenia-homeomorfizm-jednoznaczny` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |
| 16-06 | 242 | `stwierdzenie` | `prop:topog-uzwarcenia-zwarta` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |
| 16-07 | 282 | `stwierdzenie` | `prop:topog-uzwarcenia-porzadek-klasy` | [00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md](00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md) |

## Rozdział 17: 10 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 17-01 | 49 | `lemat` | `lem:topog-uzwarcenia-aleksandrow-topologia` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-02 | 113 | `twierdzenie` | `thm:topog-uzwarcenia-aleksandrow-kryterium` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-03 | 179 | `twierdzenie` | `thm:topog-uzwarcenia-aleksandrow-proper` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-04 | 227 | `twierdzenie` | `thm:topog-uzwarcenia-aleksandrow-minimalne` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-05 | 283 | `wniosek` | `cor:topog-uzwarcenia-aleksandrow-jednoznacznosc` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-06 | 340 | `lemat` | `lem:topog-uzwarcenia-lokalna-tych` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-07 | 404 | `twierdzenie` | `thm:topog-uzwarcenia-cech-stone-uniwersalne` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-08 | 455 | `wniosek` | `cor:topog-uzwarcenia-cech-stone-funkcje` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-09 | 481 | `twierdzenie` | `thm:topog-uzwarcenia-cech-stone-maksymalne` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |
| 17-10 | 539 | `wniosek` | `cor:topog-uzwarcenia-krance` | [00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md](00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md) |

## Rozdział 18: 9 środowisk dowodowych

| ID | Linia | Typ | Etykieta | Audyt referencyjny |
|---|---:|---|---|---|
| 18-01 | 63 | `stwierdzenie` | `prop:topog-odwzorowania-oddzielanie` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-02 | 102 | `stwierdzenie` | `prop:topog-odwzorowania-skladanie` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-03 | 147 | `definicja` | `def:topog-odwzorowania-jednostajna-zwarte` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-04 | 180 | `twierdzenie` | `thm:topog-odwzorowania-zwarto-otwarta-jednostajna` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-05 | 276 | `wniosek` | `cor:topog-odwzorowania-sieci` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-06 | 319 | `twierdzenie` | `thm:topog-odwzorowania-ewaluacja` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-07 | 367 | `twierdzenie` | `thm:topog-odwzorowania-wykladnicze` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-08 | 491 | `twierdzenie` | `thm:topog-odwzorowania-metryka-wyczerpanie` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |
| 18-09 | 549 | `twierdzenie` | `thm:topog-odwzorowania-zupelnosc` | [00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md](00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md) |

## Wynik

**71/71** aktualnych środowisk proof zostało przypisanych do wyniku i referencyjnego raportu; nie znaleziono braku etykiety w tym bloku. Rozdział 11 ma odrębną, odnotowaną historię przeniesienia materiału do 14. Wszystkie proof i metadane pokrywają się z inwentarzem globalnym 31.

Otwarte: analogiczna macierz 19–26, pełne sprawdzenie zakresu każdego dowodu w dokumentach referencyjnych, kontrola końcowa wszystkich rysunków na pełnej rozdzielczości i niezależna końcowa kontrola matematyczna.
