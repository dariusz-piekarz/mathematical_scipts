# IT-03 — trwałe kryteria
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| IT-03-001 | it:thm:rs-tools | Ciągłość funkcji wariacji w punktach ciągłości integratora; skończoność D_r dla BV | semantyczna |
| IT-03-002 | it:thm:rs-tools | Pokrycie z małą wariacją lub małą oscylacją; wspólne rozdrobnienie i kryterium Cauchy'ego | semantyczna + Python |
| IT-03-003 | it:thm:rs-tools | Dyskretne części, rozłączne skoki, wspólny skok jako kontrprzykład | semantyczna + Python |
| IT-03-004 | it:thm:rs-oscillation | Domkniętość D_r, liczba Lebesgue'a pokrycia, atomy i końce, uzupełnienie miary i mierzalność | semantyczna |
| IT-03-005 | tw:rs-blad-kwadratury | Kontrola przez oscylację i wariację przy rozdrobnieniu | semantyczna + Python |
| IT-03-006 | it:thm:rs-locality | Lokalność przez wspólne dopełnienie, sklejanie przy ciągłości jednej funkcji, tożsamość błędu rozcięcia | semantyczna + Python |
| IT-03-007 | it:ex:rs-gluing-failure | Dwie całki lokalne istnieją, ale wspólny skok wyklucza całkę globalną | semantyczna + Python |
| IT-03-008 | it:def:rs-integral, it:lem:rs-variation | Jednoznaczność granicy; addytywność wahania w obie strony, końce | semantyczna + Python |
| IT-03-009 | it:thm:rs-tools(c),(d) | Jednostajny błąd zastąpienia punktu Lagrange'a znacznikiem; całkowalność iloczynu; liniowość obu zmiennych | semantyczna + Python |
| IT-03-010 | tw:rs-jeden-skok | Konstrukcja komórki zawierającej znacznik i skok także w b; granica średnic | semantyczna |
| IT-03-011 | it:thm:rs-reparametrization | Płaskie fragmenty, odwrócenie kolejności z niesymetrycznymi znacznikami | semantyczna + Python |
| IT-03-012 | it:thm:rs-integrator-substitution | Addytywność przyrostów G, kontrola wahania i jednostajnego błędu | semantyczna + Python (tools/tests/test_integration_theory_rs_substitution.py) |

Kontrola po migracji: źródło 9a39741c2269b7969ae2b20fb7fb168700953fad (commit 6a1c0ed613dc22c3adb44a25f8099a325a66bd5b), wszystkie dotychczasowe etykiety zachowane, dodano 2. Poprawiono skrótowe dowody w narzędziach, jawnie powiązano konstrukcję miary LS z IT-10, zachowano i sprawdzono istniejące dowody lokalności, kryterium oscylacyjnego i podstawienia. Nowe regresje (61b03596758b524ed0e32ab71c4926142eb61a89) oczekują na potwierdzenie wykonania. Poprzedni CI 45619331666 zaliczył 24 testy i dwie kompilacje (130 stron w drugim przebiegu), lecz dotyczy wersji sprzed tej poprawki. Kontrola wizualna nowej wersji nieprzeprowadzona. Nie uruchomiono Lean.
