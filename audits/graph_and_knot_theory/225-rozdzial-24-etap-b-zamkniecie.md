# Audyt 225 — drukowany rozdział 24, zamknięcie etapu B

Data: 2026-11-25. Kontynuacja 224, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex. Blob 6aaca3436174ab0b28de4f43218d2c2f8dd0a830. W poprzedniej kontroli 225 potwierdzono zgodność 44/44 blobów rozdziałów i pliku głównego między 6c9722ce, fcce40f7 i gałęzią roboczą. Nie zmieniono źródeł.

## CI i PDF
Run 45591196612, SHA fcce40f7b25b4aa8db9b7f75974a2986330d33dc: structural-audit 139125555479 i full-book-pdf 139125556040 completed/success. Z rzeczywistego logu: trzy kompilacje, 354 strony A4, 0 ostrzeżeń. Regresja GKT-24-BS12-PY-01 potwierdzona logiem w audycie 224. Pobrano artefakt 15011067107 dla dokładnego SHA, otwarto ZIP i PDF przez PyMuPDF. Plik ostrzeżeń ma 0 bajtów. Rozdział 24 na stronach fizycznych 200–206 (druk 190–196), kolejny zaczyna się na 207. Pięć adnotacji odsyłaczy w badanym rozdziale.

Wyrenderowano wszystkie siedem stron w skali 1.6; obejrzano trzy arkusze kontaktowe i pełne strony 201 i 204.
- GKT-24-FIG-CAYLEY-01 PASS: rozdzielone węzły, czytelne etykiety, przerywane przedłużenia i cykl.
- GKT-24-FIG-GROUP-01 PASS: podpisy amalgamacji i HNN nie kolidują z oznaczeniami grup; pętla czytelna.
- Brak istotnych kolizji, obcięć i problemów składu w oglądanym rozdziale. Ostatnia strona w dużej części pusta, bez korekty kosmetycznej.

## Decyzja
Etap B zamknięty. Kontrole matematyczne 222–223, zintegrowana regresja 224 i nowa kompilacja wraz z oględzinami 225 przeszły pomyślnie. Fundamentalne twierdzenie Bassa–Serre'a pozostaje wynikiem przyjętym z literatury, testy nie są formalizacją Lean. Nie wykonano ponownych oględzin pozostałych 347 stron tomu. Postęp 23/44, rozdział 24 wymaga jeszcze etapu C. Następny audyt 226: końcowa kontrola matematyczna i regresyjna rozdziału, bez rozszerzeń; zamknięcie rozdziału tylko po spełnieniu bramki.
