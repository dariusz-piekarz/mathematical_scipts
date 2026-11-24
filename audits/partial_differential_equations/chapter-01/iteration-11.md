# PDE-01 — iteracja 11, 2026-11-24

Aktualne źródło rozdziału: blob aeea9d0a8c39cb2a2049d0cd982688dd370fc874 (52409 bajtów), bez zmian od dwóch czystych przebiegów kontrolnych. Nie ponawiano zmian merytorycznych tylko po to, by utworzyć commit.

## Kontrola integracji skryptu

Wykonano kontrolę na rzeczywistych plikach pobranych z gałęzi biblioteka-matematyczna-iteracja-6 i pełnym drzewie Git (head podczas kontroli f50e781045b26c12b18f6ace479c620d862e95fb, wynik drzewa nieobcięty).

| Kontrola | Wynik |
|---|---|
| Liczba wejść rozdziałów w books/pl/partial_differential_equations.tex | 33 |
| Liczba wpisów w catalog/partial_differential_equations_manifest.json | 33 |
| Kolejność ścieżek manifestu i wejść książki | identyczna |
| Istnienie plików rozdziałów w drzewie Git | 33/33, brak nadmiarowych plików numerowanych |
| Globalny blok listings w preambule książki | dokładnie jeden, identyczny z latex/pl/code-listings.tex |
| Globalny blok listings w application/config/preambles/PDE.tex | dokładnie jeden, identyczny z plikiem kanonicznym |
| Lokalne nadpisania listings poza blokiem kanonicznym w obu preambułach | brak |

Kontrolę bloków wykonano przez bezpośrednie porównanie tekstu i sprawdzenie wyrażeń regularnych na dwóch plikach PDE, nie przez uruchomienie globalnego tools/sync_code_listings.py --check na całym repozytorium.

Manifest podaje dla rozdziału 01 38861 bajtów, natomiast obecny blob ma 52409 bajtów. Manifest opisuje rekonstrukcję pierwotnego pliku z podziału na rozdziały (pole reconstruction i source_sha256); historycznych metadanych nie nadpisano. Nie należy traktować zapisanych w nim sum jako aktualnych sum kontrolnych po audytach.

## Testy i blokada zamknięcia

Ponownie uruchomiono lokalną kopię test_energy_hadamard.py, po potwierdzeniu SHA blob 1d8609e78e4887cde7164a5a65d65d9d7db6cdd2. Wynik: 3/3 unittest OK. Próba pobrania pełnego źródła do kompilacji przez raw.githubusercontent.com zakończyła się błędem rozwiązywania DNS.

Przebiegi CI 45406285231 i 45406319616 nadal queued, a także 45406654400. Nie potwierdzono pełnej kompilacji aktualnego źródła ani układu jego stron. Izolowane rysunki i dwa czyste audyty opisano w iteration-10.md; Lean nie uruchomiono. Nie rozpoczęto zmian rozdziału 02. Raport zapisano poza ścieżkami wyzwalającymi workflow PDE.

Nie przypisywać przyczyny kolejki do limitów konta ani konfiguracji runnera bez osobnych danych.
