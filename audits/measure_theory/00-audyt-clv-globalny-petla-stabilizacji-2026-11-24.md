# Audyt CLV (155) — wspólna pętla składu, regresji i PDF
Data 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6. Trzy etapy są jedną pętlą; nie zamykać książki bez pełnej zgodności ostatniej wersji.

## Przejście 1
Poprzedni PDF (run 45386640177, SHA-256 3260e64c0279a09097a3aa4814446cc2245d0f90075232f15ed934ea7cf76ee9): 308 stron. Przegląd 13 arkuszy kontaktowych obejmujący wszystkie strony; sprawdzenie 146849 wydobytych słów, 1506 odsyłaczy nazwanych (wszystkie istnieją i prowadzą do istniejących stron), 289 zakładek (cele poprawne), brak słów poza fizycznymi granicami stron. Wykryto samotną pozycję spisu treści na stronie fizycznej 10.
Globalna bramka po zmianach CLIV: job 138423906287, 156/156 unittest i 16/16 samodzielnych skryptów; job PDF anulowany przez nowszy commit.
Zmniejszono lokalnie parskip spisu treści do 2pt (7d74b72b9b7e972869155229970c4a23467c242b).

## Przejście 2
Run 45388618286, artefakt 14916664794, ZIP SHA-256 e393092e5290807eb9fcbf8b39a7aa6ef6766f8ef8a56043360e813689a0a3a0 zgodny z metadanymi.
Pełny PDF 307 stron; wszystkie 286 stron treści rozdziałów po przesunięciu o jedną stronę są piksel w piksel identyczne z poprzednią wersją przy renderowaniu 72 dpi. Obejrzano nowy spis treści i oznaczeń (11 stron frontmatter) oraz wszystkie 10 stron indeksu. Samotna pozycja zniknęła. Poprawne zakładki zawierają L^p, C_c^∞, σ-skończoność. Log: hyperref 54→0, Underfull 13→0, Overfull 0, nierozwiązane odsyłacze 0, wielokrotne etykiety 0; pozostało 10 infinite glue shrinkage.
Globalny job regresji 138426192554 z tego samego commitu: 156/156 unittest, 16/16 samodzielnych skryptów, sukces.
Kontrola drukowanych numerów i celów indeksu: 495/495 unikatowych celów, 494/495 zgodnych par numer–strona; Definicja 29.17 ma właściwy cel na stronie drukowanej 233, ale wydrukowany numer strony 232.

## Przejście 3 — korekty
- 916c161bf8bb6b63635ab8f4df419c93c71aec2b: przesunięto istniejącą etykietę def:measure-boundary-29 do pierwszego wiersza definicji, bez zmiany jej identyfikatora ani treści. Wszystkie 39 etykiet rozdziału 29 pozostają.
- 33df7aa4310f301bc6aaedf5b8979e04c51376f7: trwały preflight PDF (PyMuPDF), lokalnie uruchomiony na dwóch poprzednich pełnych PDF, w obu wykrywa dokładnie wyżej opisaną rozbieżność. 17938175b8a778a58acbb64543df763c64608c5c: włączenie do globalnego workflow z przypiętą wersją PyMuPDF 1.26.7.
- caed1dccef72566ca74157ab1a3e9e90e4c2aed8: kompatybilność z nowszym kernelem LaTeX od 2025-11-01; ograniczona podmiana dwóch vss na vfil w wyjściu longtable. Jest to hipoteza naprawy źródła nieskończonej kurczliwości, nie wyciszenie komunikatu. Lokalny eksperyment z vsplit i wewnętrznym vss reprodukuje 1 ostrzeżenie/error, vfil daje 0 i kod wyjścia 0; obie podmiany w lokalnym longtable dopasowane. Lokalny kernel 2024-11 nie odtwarza konkretnego błędu nowszego pełnego skryptu. Wymagana ponowna kompilacja aktualnego commitu.

## Bramka zamknięcia
Aktualny globalny run 45389442662, chapter29 45389442747, chapter31 45389442815: w chwili zapisu nie zakończone. Nie przedstawiać ostatnich poprawek jako zweryfikowanych. Po uzyskaniu artefaktu sprawdzić 0 ostrzeżeń, preflight 495/495 zgodnych pozycji, regresje, porównanie wszystkich stron i oględziny zmienionych stron. W razie niepowodzenia wrócić do odpowiedniego etapu w tej samej pętli. Nie rozszerzać zakresu. 31/31 rozdziałów ustabilizowanych merytorycznie; książka jeszcze niezamknięta technicznie.
