# Audyt 182 — drukowany rozdział 19, etap A (PDF i Kirchhoff)

Data: 2026-11-25. Kontynuacja 181, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/12-wielomian-tutte-a-kolorowania-i-dualnosc-algebraiczna.tex.
Wejściowy commit 5d73e8551540197863a55a3ff15d5c96784eb15b, blob de9b618fe643ca945ea98c644ee12b843fff916e.
Korekta c6e414ee83436b8c819ae1aa6a59550197f9a554, blob 777cd22e94d442434277ccf2351df76795c3e9e7.

## CI i oględziny poprzedniego PDF
Dla wejściowego SHA: pełny audyt 45568916810, algorytmy 45568916798, terminologia 45568916770, aplikacja 45568916763 — wszystkie SUCCESS przy końcowej kontroli.
Pobrano ZIP 15001097501, wydobyto PDF (341 stron) i logi (plik ostrzeżeń 0 bajtów). Rozdział 19: PDF 165–171, druk 155–161, 7 stron, 9 adnotacji odsyłaczy. Wyrenderowano wszystkie 7 stron w skali 1.5, obejrzano dwa arkusze kontaktowe i powiększoną stronę z rysunkiem. Nie zauważono obcięć ani przecięć w samych grafach. Schemat rekurencji miał strzałkę usunięcia, znak plus i brak oznaczenia gałęzi kontrakcji; zmieniono na równość wielomianów z podpisami C3\setminus e i C3/e. Ostatnia strona zawiera kilka wierszy bibliografii (nie usterka matematyczna; rozważyć łamanie w następnej kontroli). W poprawionym źródle nie oglądano jeszcze PDF.

## Kontrola semantyczna
Sprawdzono rekurencję, wykładniki, specjalizacje, dualność Tutte'a i przepływy z uwzględnieniem pętli, mostów, grafu zerowego i złożonych q. Doprecyzowano zdanie o ważonym Kirchhoffie: każdemu drzewu prostemu odpowiada iloczyn wag różnych drzew multigrafu, a nie iloczyn wag drzew. Uściślono interpretację zamiany wykładników w przykładzie dualności. Zachowano 12 etykiet i 32 pary środowisk. Nie dodano nowych twierdzeń.

## Regresje
GKT-19-KIRCH-01 (test_gkt19_kirchhoff.js, commit b13dffe013bf11617495b1978f06e616f3dc2159): PASS, 3527 multigrafów z 1–4 wierzchołkami i maks. 5 krawędziami, 954 spójne, 3532 dokładne wyznaczniki minorów (BigInt); wśród spójnych 667 z pętlami i 542 z równoległymi krawędziami. Porównano z bezpośrednim liczeniem drzew multigrafu, ważonym liczeniem drzew grafu prostego i macierzami laplasjanu. 
GKT-19-REC-01: PASS 3528 grafów, 89217 podzbiorów, 15855 rekurencji i 14112 porównań kolorowań.
GKT-19-DUAL-01: PASS 747 układów, 453 sferyczne, 3533 par podzbiorów, 1812 porównań przepływów i kolorowań (906 dla złożonego q).
Wszystkie trzy zapisane skrypty odczytano i ponownie wykonano w izolacie JS, nie w procesie Node. Próby skończone, częściowo pokrywające się, nie formalizacja Lean.

## Bramka
Dla nowego SHA: terminologia 45569309717 SUCCESS; pełny audyt 45569308284, aplikacja 45569308418, algorytmy 45569308187 w toku przy kontroli. Nie przenosimy PASS PDF na nowy blob. Etap A nadal otwarty. Następnie audyt 183: CI, ponowna kontrola PDF z poprawionym schematem, regresje i ewentualne zamknięcie A, potem niezależny B.
