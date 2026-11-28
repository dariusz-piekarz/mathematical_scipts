# AA-59 — audyt I: otwarcie i kontrola konstrukcji

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Zakres w docs/pl/zakres_aa59_rozklad_korzeniowy.md.

## Kontrola matematyczna
Rozpisano indukcję wzoru dwumianowego dla derywacji i przejście do jej części półprostej i nilpotentnej. Zastosowanie wewnętrzności derywacji wymaga półprostoty; użycie zerowego centrum jest jawne. W dowodzie centralizatora toralnego sprawdzono niezdegenerowanie ograniczenia formy Killinga dzięki ortogonalności różnych wag, maksymalność toralną części półprostej, zastosowanie Engela do centralizatora, następnie Liego do jego reprezentacji na całej algebrze. Argument śladowy usuwa część nilpotentną. Normalizator wyznaczono przez bezpośrednie porównanie składowych. Dowód niezerowości alfa(t_alfa) korzysta ze śladu komutatora na każdej przestrzeni własnej, nie z dodatniej określoności formy. Przykład sl3 sprawdza rozkład i normalizację trójki.

## Integracja i regresje
Dodano testy dokładnych macierzy sl_n dla n=2,...,6, wag, nawiasów, parowania i trójek oraz rozkładu Jordana w przykładach macierzowych. Testy przygotowano do CI; nie uruchomiono ich lokalnie w tej iteracji. Zaktualizowano główny plik książki, katalog, workflow i bramkę integralności, zachowując historyczne kontrole AA-01–58. Nie oglądano PDF. Jest to pierwszy audyt autorski, nie niezależny czysty audyt. AA-59 W AUDYCIE; AA-60 nieotwarty.
