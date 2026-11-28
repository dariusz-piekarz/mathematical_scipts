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

## Blok D — zamiana zmiennych
| ID | Kryterium | Metoda |
|---|---|---|
| IT-11-025 | Miara obrazowa, addytywność, całkowanie funkcji nieujemnych i zespolonych, gęstość obrazu kwadratowania | semantyczna |
| IT-11-026 | Translacja, ścinanie i skalowanie, zgodność miar produktowych, wyznacznik macierzy elementarnych, rozszerzenie na zbiory Lebesgue'a-mierzalne | semantyczna + Python |
| IT-11-027 | Lokalna własność Lipschitza i obrazy zbiorów zerowych, dobór średnic pokrycia i przypadek stałej zero | semantyczna |
| IT-11-028 | Lokalny sześcian: oszacowanie reszty, zwężenie Banacha, mierzalność obrazu i jednostajny parametr na zbiorze zwartym | semantyczna + Python |
| IT-11-029 | Wzór jakobianowy dla dyfeomorfizmu: dodatniość J, miary sigma-skończone, podział i oscylacje, jednoznaczność na sześcianach diadycznych | semantyczna + Python |
| IT-11-030 | Uzupełnienie, mierzalność obrazów i przeciwobrazów, zgodność całek i ograniczanie dziedziny | semantyczna |
| IT-11-031 | Biegunowe, walcowe i sferyczne: dziedziny dyfeomorfizmów, zbiory usunięte miary zero, wyznaczniki i iterowane całki w uzupełnieniu | semantyczna + Python |
| IT-11-032 | Transformacja gęstości, brak iniektywności, konstrukcja osobliwego homeomorfizmu przez mieszaninę miar Cantora | semantyczna + Python |

Audyt D: commit 99a974e9a7cbc9cff04af9bae262c2cc3958e648, blob 80aaca7a34c72daa208e05cb3f650f14adb16b4b. Przeczytano cały blok zamiany zmiennych (21901 -> 28195 znaków), zachowano 132/132 etykiet, środowiska sparowane; pozostały prefiks i sufiks niezmienione. Rozpisano dowody miary obrazowej, zerowości obrazów Lipschitzowskich, jednostajnego oszacowania lokalnej deformacji, przejścia od skończonych miar do całej sigma-algebry, mierzalności względem uzupełnienia; doprecyzowano zastosowania Fubiniego/Tonellego w układach współrzędnych. Dodano konstrukcję ściśle rosnącego osobliwego homeomorfizmu wykorzystującą miarę Cantora (IT-10) i twierdzenie o pochodnej dystrybuanty (następny blok IT-11). Siedem nowych regresji: 25118aa2e003226a187a059b49c8cabd66547c4b, skończone świadectwa, nie dowody. CI C 45633654407: success. CI D, kontrola PDF, formalizacja Lean oczekują. Następny blok E: różniczkowanie całek i miar, w tym weryfikacja zależności nowego przykładu od twierdzenia o pochodnej dystrybuanty.

## Blok E — różniczkowanie całek i miar
| ID | Kryterium | Metoda |
|---|---|---|
| IT-11-033 | Lemat 5r, rozłączność, ograniczenie promieni, przeliczalność; objętość kuli i zerowość brzegu | semantyczna + Python |
| IT-11-034 | Maksymalna funkcja miary, półciągłość z dołu, słabe oszacowanie 5^d/t, przypadek miar zespolonych | semantyczna |
| IT-11-035 | Gęstość C_c w L1, ciągłość średnich i oscylacji, wymierne promienie, twierdzenie Lebesgue'a i lokalizacja | semantyczna + Python |
| IT-11-036 | Punkty gęstości, borelowska wersja kanoniczna, warunek Cauchy'ego, rozróżnienie granicy średnich i punktu Lebesgue'a | semantyczna + Python |
| IT-11-037 | Zanik gęstości miary osobliwej, zwarta aproksymacja, przypadek pustego zbioru zwartego, mierzalność limsup | semantyczna |
| IT-11-038 | Różniczkowanie miary Radona, lokalna całkowalność gęstości, zgodność lokalnych rozkładów, wariacja miar ze znakiem | semantyczna |
| IT-11-039 | Pochodna pierwotnej Lebesgue'a, obie strony, pochodna dystrybuanty i kryterium bezwzględnej ciągłości miary | semantyczna + Python |
| IT-11-040 | Charakterystyka AC, rozkład przez wariację i miary Stieltjesa, niezależność od charakterystyki ACG*, zgodność HK i Lebesgue'a | semantyczna + Python |

Audyt E: commit d3ed5f60070eca638e684f81b7ce946bd0990db7, blob cb27acca9c7fac6e603510c074911a2abfa9043b. Przeczytano blok od lematu 5r do twierdzenia o pierwotnych AC, zachowano 132/132 etykiet; środowiska sparowane; blok 25193 -> 28074 znaków, ostatnie 7259 znaków pozostawiono do bloku F (Alexiewicz, twierdzenia graniczne HK, przykłady). Doprecyzowano objętość i brzeg kuli, mierzalność oscylacji i kanonicznego przedstawiciela, lokalne gęstości i argument dla miar osobliwych, dwustronne ilorazy różnicowe oraz zależności od konstrukcji Stieltjesa, wariacji i pochodnej HK. Zależność przykładu osobliwego homeomorfizmu z D od thm:cdf-derivative-25 sprawdzona, nie ma koła z zamianą zmiennych (potrzebny tylko liniowy wzór na objętość). Rozkład Lebesgue'a i RN pozostają wskazanymi twierdzeniami teorii miary. Sześć nowych regresji: cfcc4580f055c27e170c640d4f1efc07ca38d850. CI D 45634139524: success. CI E i wizualna kontrola PDF niepotwierdzone; Lean nieuruchamiany. Następny blok F, a potem audyt stabilizacyjny całego rozdziału.

## Blok F — norma Alexiewicza, granice HK i przykłady
| ID | Kryterium | Metoda |
|---|---|---|
| IT-11-041 | Norma Alexiewicza na ilorazie, ciągłość pierwotnej i jądro, izometria | semantyczna + Python |
| IT-11-042 | Gęstość interpolantów liniowych, ich realizacja jako pierwotnych HK, zupełność przestrzeni zakotwiczonych funkcji ciągłych, kontrprzykład Cantora | semantyczna + Python |
| IT-11-043 | Zbieżność monotoniczna i zmajoryzowana HK przez redukcję do L1, wspólny zbiór zerowy, zbieżność w normie Alexiewicza | semantyczna + Python |
| IT-11-044 | Konieczność skończonej granicy całki obciętej także dla szerokiej całki Denjoya; osobliwość potęgowa i logarytmiczna | semantyczna |
| IT-11-045 | Oscylacja x^(-p) sin(1/x), dokładne progi Riemanna, Lebesgue'a i obu Denjoya, Hake i oszacowanie modułu przez szereg | semantyczna + Python |
| IT-11-046 | Konstrukcja dodatniej miary zbioru domkniętego o pustym wnętrzu; brak reprezentanta całkowalnego Riemanna po zmianach na zbiorze zerowym | semantyczna + Python |

Audyt F: commit 8341625818d865381f52e7829761641d849248ed, blob 9339bf6c3ae1607f8cc6544b5f41c15402a93fd5. Przeczytano ostatnie 7259 znaków, po uzupełnieniach 12398 znaków; zachowano 132/132 wcześniejszych etykiet i dodano dwie. Rozbudowano dowód uzupełnienia Alexiewicza, zastępując zewnętrzną aproksymację Weierstrassa elementarną interpolacją przedziałami liniową. Dodano wzmocnienie twierdzeń granicznych do zbieżności w normie Alexiewicza, lemat o konieczności granicy obciętych całek także dla szerokiego Denjoya, dokładne dowody progów całkowalności, konstrukcję grubego zbioru Cantora oraz odsyłacze. Sześć nowych regresji: 7444eb4f2942dae9bbb1154450d7793f32f024ee. Kontrola całego pliku w ref 5526a1d67ff568d231ba2258794eae9958e1189a: 134 etykiety, 87 różnych odsyłaczy ref/eqref z istniejącymi celami, środowiska sparowane. CI E 45635022444: success. CI F, pełna stabilizacja i niezależna kontrola matematyczna oraz wizualna PDF oczekują. Lean nieuruchamiany.
