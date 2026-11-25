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
