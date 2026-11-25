# IT-06 — całka Kurzweila–Stieltjesa: kryteria regresji

| ID | Etykieta / zakres | Kryterium | Metoda |
|---|---|---|---|
| IT-06-001 | tw:ks-cauchy, it:thm:ks-locality | Minimum cechowań, wspólne dopełnienie, rozcięcie w znaczniku i addytywność | semantyczna |
| IT-06-002 | it:lem:ks-saks-henstock | Dowolne podrodziny, dopełnienie luk i suma modułów błędów | semantyczna |
| IT-06-003 | it:lem:ks-bv-regulated | Rozkład Jordana, addytywność wahania, granice jednostronne; jednostajna aproksymacja schodkowa | semantyczna + Python |
| IT-06-004 | lem:ks-point, lem:ks-indicators, tw:ks-step | Oba rodzaje skoków, oba końce, wymuszenie znaczników i niepusty blok komórek | semantyczna + Python |
| IT-06-005 | tw:ks-reg-bv, tw:ks-bv-reg | Osobne hipotezy, jednostajna aproksymacja i kontrola błędów | semantyczna |
| IT-06-006 | tw:ks-bv-split, tw:ks-measure | Sumowalność skoków, rozkład Jordana, miary dodatnie na [a,b], masa w a i b, jednoznaczność i oszacowanie wariacji | semantyczna + Python |
| IT-06-007 | tw:ks-decomp, wn:ks-ac-jumps | Rozkład miary ze znakiem, część osobliwa, atomy i ogon szeregu | semantyczna + Python |
| IT-06-008 | tw:ks-ibp, wn:ks-ibp-ac | Znaki obu poprawek skokowych, granice przybliżeń i całka Riemanna przy C^1 | semantyczna + Python |
| IT-06-009 | tw:ks-primitive | Jednostronne granice bez BV integratora, wahanie przy dodatkowych hipotezach | semantyczna |
| IT-06-010 | tw:ks-substitution, tw:ks-chain | Przenoszenie cechowań w obie strony, nieograniczony mnożnik, grupowanie błędów | semantyczna + Python |
| IT-06-011 | tw:ks-quadrature | Addytywność i kontrola modułem ciągłości | semantyczna |
| IT-06-012 | it:thm:ks-uniform, it:thm:ks-equiintegrability, it:ex:ks-atom-convergence | Zbieżność jednostajna i wspólne cechowanie, atom nie jest pomijany przez zbieżność Lebesgue'a p.w. | semantyczna |

Audyt po migracji: commit 74391b67e42d0ae88babcf2fd9fd1cdf417858a2 (blob f33a77b6ac90809fda799969fb60778414cd6efc). Zachowano 24/24 etykiet, dodano jedną; środowiska sparowane. Rozpisano jednostronne kryterium Cauchy'ego, konstrukcję przybliżeń schodkowych, BV => regulowana, wzory dla funkcji charakterystycznych przedziałów i konstrukcję miary ze znakiem z dwóch miar dodatnich. Wyprowadzono oszacowanie wahania miary bez pomijania atomu w a. Doprecyzowano całkowalność Riemanna w formule AC/C^1. Skontrolowano wcześniejsze dowody lokalności, Saks–Henstocka, podstawienia i zbieżności; nie zastąpiono ich. Testy: commit f5e28fb54c8f52de4b742daf4db41a226533e5ee (6 metod, świadkowie skończeni, nie dowody). Wykonanie nowych testów i CI po poprawkach do potwierdzenia, PDF rozdziału 06 niekontrolowany wizualnie. Nie uruchamiano Lean. Następny krok: audyt kontrolny, w szczególności konstrukcji miary i skoków.
