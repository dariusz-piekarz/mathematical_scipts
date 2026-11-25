# IT-11 — regresje
| ID | Kryterium | Metoda |
|---|---|---|
| IT-11-001 | Deklaracja awaryjnego atlasref przed pierwszym użyciem; zachowane odsyłacze do Teorii miary | Python + kompilacja |
| IT-11-002 | Konstrukcja funkcji prostych, puste komórki, nieskończone miary i konwencja 0 razy nieskończoność | semantyczna + Python |
| IT-11-003 | Monotoniczna aproksymacja kanoniczna, definicja przez supremum, ograniczenia miary i Markow | semantyczna + Python |
| IT-11-004 | Całka ze znakiem, niezmienniczość p.w., liniowość i monotoniczność rzeczywista, liniowość zespolona | semantyczna + Python |
| IT-11-005 | MCT bez sigma-skończoności, lemat Fatou i ograniczenie od dołu, DCT i wspólne zbiory wyjątkowe | semantyczna |
| IT-11-006 | Szeregi funkcji, mierzalny zbiór Cauchy'ego, rozkład warstwowy bez Tonellego, bezwzględna ciągłość całki | semantyczna + Python |
| IT-11-007 | Definicja L1 jako ilorazu, aksjomaty normy, szereg sumowalny w normie, wybór podciągu w dowodzie Riesz–Fischera | semantyczna + Python |
| IT-11-008 | Zgodność Riemann–Lebesgue, oszacowanie zbiorów wyjątkowych, zgodność McShane–Lebesgue i kryterium bezwzględnej całkowalności HK | semantyczna + Python |

## Blok A — audyt 2026-11-25
Commit 4f240f568d6e02b28937e56073c29575db7d6fd7, blob 3cde54b0f6c934577030ea4487c912aa7ee74b51. Skontrolowano tekst od początku rozdziału do podrozdziału o całkach zależnych od parametru (wcześniej 53524 znaki). Zachowano 129/129 dawnych etykiet całego pliku, dodano trzy, poprawiono położenie dwóch istniejących etykiet. Środowiska sparowane. Pozostałe 106398 znaków źródła niezmienione. Uzupełniono definicję L1, dowód monotoniczności funkcji ze znakiem, liniowość zespoloną, mierzalność zbioru zbieżności, bezwzględną ciągłość całki, dobór podciągu Cauchy'ego i oszacowanie Borel–Cantelli. Sprawdzono podstawy MCT, Fatou, DCT i identyfikację McShane–Lebesgue. Testy: d7c2c9ac100a4c8753b69511174a216425172a29, sześć nowych metod, świadkowie skończeni. CI po zmianach niepotwierdzone; kontrola PDF i Lean niewykonane. Kolejne bloki: parametry, produkt, zamiana zmiennych, różniczkowanie miar i pozostałe porównania całek. Nie uznaje się całego IT-11 za ustabilizowany.

## Blok B — całki zależne od parametru
| ID | Kryterium | Metoda |
|---|---|---|
| IT-11-009 | Dominacja lokalna, wspólne i zależne od parametru zbiory wyjątkowe, ciągłość w L1, kontrprzykład ucieczki masy | semantyczna + Python |
| IT-11-010 | Zbieżność jednostajna całek: całkowalność wszystkich przekrojów przed odejmowaniem całek; mierzalność supremum przy ośrodkowości | semantyczna + Python |
| IT-11-011 | Pochodna zespolonej funkcji parametru rzeczywistego: projekcja na kierunek, mierzalność na niezupełnej przestrzeni, kryterium ciągowe | semantyczna + Python |
| IT-11-012 | Kontrprzykład gładkich przekrojów bez dominacji, pochodne wyższe, przeliczalne wyczerpanie zwartymi przedziałami | semantyczna + Python |
| IT-11-013 | Zmienne dziedziny, osobne wyjątki dla ciągu parametrów, całkowalność, jednostajna kontrola ogonów i jej niekonieczność | semantyczna + Python |
| IT-11-014 | Laplace: dominacja wielomianu przez wykładniczą, zespolony iloraz różnicowy, ważona całkowalność dla iteracji pochodnych | semantyczna + Python |
| IT-11-015 | Gamma: całkowalność logarytmicznych majorant, zastosowanie wyższych pochodnych, wyrazy brzegowe rekurencji | semantyczna + Python |

Audyt B: commit 6de8171519fa0981a05270f6ffe33b04d02e0523, blob 27c91e2739a4752bcc8e4b0b1d9d6025c9e61fbf. Przeczytano cały podrozdział parametryczny, zachowano 132/132 etykiet, sparowano środowiska; blok 19830 -> 24637 znaków, niezmieniony prefiks 56705 i sufiks 86568 znaków. Uzupełniono dowód całkowalności przy jednostajnej zbieżności, dowód ciągłości w L1, mierzalność pochodnej z jawną modyfikacją na mierzalnym zbiorze zerowym, argument dla wyższych pochodnych, przykłady ucieczki masy i gładkich przekrojów bez dominacji, kontrprzykład konieczności kontroli ogonów, argument Laplace'a i Gamma. Osiem nowych testów: 0959915b3a9d53ada111e21e9ab1cf5460797411. Testy stanowią skończone świadectwa, nie dowody. CI bloku A 45632808355 zakończone sukcesem. CI B, kontrola PDF i Lean jeszcze niepotwierdzone. Następny blok C: miary produktowe, Tonelli i Fubini.

## Blok C — miary produktowe, Tonelli i Fubini
| ID | Kryterium | Metoda |
|---|---|---|
| IT-11-016 | Ślad produktu, algebra prostokątów, mierzalność przekrojów, klasa monotoniczna na prostokącie skończonym | semantyczna |
| IT-11-017 | Wyczerpanie sigma-skończone, tożsamość przekrojowa i konstrukcja miary, przypadki 0 razy nieskończoność | semantyczna + Python |
| IT-11-018 | Jednoznaczność miary produktowej przez układ Dynkina na skończonym śladzie, bez koła z Tonellim | semantyczna |
| IT-11-019 | Tonelli, Fubini rzeczywisty i zespolony, mierzalność oraz całkowalność przekrojów poza wyjątkami; odejmowanie skończonych całek | semantyczna + Python |
| IT-11-020 | Kontrprzykłady braku bezwzględnej całkowalności oraz sigma-skończoności | semantyczna + Python |
| IT-11-021 | Produkt Lebesgue'a, zerowość pasów poprzez pokrycia bez twierdzenia produktowego, zgodność miar i uzupełnienie | semantyczna + Python |
| IT-11-022 | Podzbiór przekątnej, niemierzalne przekroje na wyjątkach, reprezentant produktowy przez limsup z jawnie zerowanym zbiorem wyjątkowym | semantyczna + Python |
| IT-11-023 | Tonelli i Fubini dla uzupełnienia, zgodność całek na pierwotnej sigma-algebrze, mierzalność zmodyfikowanych całek przekrojowych | semantyczna + Python |
| IT-11-024 | Łączność produktów, zgodność sigma-algebr i miar, niezależność i faktoryzacja całek zespolonych | semantyczna + Python |

Audyt C: commit 4b0d89a303bd7305db92cc3ff2fd51d94ce5e871, blob 1c2e3bd3c4b57ef38788baa689064b75fd426abd. Przeczytano cały blok, zachowano 132/132 etykiet, sprawdzono parowanie środowisk; blok 32215 -> 36596 znaków, niezmieniony prefiks 81342 i sufiks 54353 znaków. Uzupełniono algebraiczne i miarowe kroki konstrukcji, przypadki nieskończonych wartości, jawny argument pokryciowy dla pasów zerowych, konstrukcję reprezentanta w uzupełnieniu, mierzalność całek przekrojowych, zgodność miar i łączność produktów. Twierdzenia o klasie monotonicznej i pi-lambda są jawnie przywołanymi wynikami teorii miary. Sześć nowych testów: f8fd2591fadddc12ffa18236cbb9fae219a0b31c (skończone świadectwa, nie dowody). CI B 45633244985: success. CI C oraz kontrola wizualna PDF i Lean niepotwierdzone. Następny blok D: zamiana zmiennych.
