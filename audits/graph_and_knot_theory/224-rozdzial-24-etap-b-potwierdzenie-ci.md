# Audyt 224 — drukowany rozdział 24, potwierdzenie regresji w CI

Data: 2026-11-25. Kontynuacja 223, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.

## Wyniki rzeczywistej kontroli
- W procesie Python ponownie uruchomiono samodzielny model GKT-24-BS12-PY-01 z Fraction. PASS: 6534 reprezentantów, 594 odwrócenia, 26730 translacji, 4602 incydencje, 1534 wierzchołki i 1533 krawędzie. 38460 iteracji kontrolnych.
- GitHub Actions run 45591196612, SHA fcce40f7b25b4aa8db9b7f75974a2986330d33dc, job structural-audit 139125555479: completed/success. Odczytano rzeczywisty log. Wiersz PASS GKT-24-BS12-PY-01 potwierdza dokładnie powyższe liczniki. W tym samym logu PASS Cayley free balls [(1,7),(2,53),(3,187)] oraz PASS C2*C3 Bass--Serre truncated coset tree (35,34). Wszystkie kroki zadania strukturalnego przeszły. Artefakt strukturalny 15011536173 jest przypisany do właściwego SHA.
- Porównanie commitów 6c9722cee627b211ac5b4a5aa35df48560ce1a73 i fcce40f7b25b4aa8db9b7f75974a2986330d33dc: 53 commity, 44 zwrócone zmienione pliki, brak zmian w katalogu rozdziałów teorii grafów i w pliku głównym tomu. Test hodge_bass_serre_knot.py: +57/-0. Nie zmieniono źródeł w niniejszym audycie.
- Regresja zintegrowana z CI: PASS potwierdzony logiem, nie deklaracją; nie jest formalizacją Lean ani dowodem twierdzenia ogólnego.

## Bramka PDF
Job full-book-pdf 139125556040 dla tego samego run: in_progress, instalacja pakietów TeX. Przy ostatnim odczycie dostępny tylko artefakt strukturalny. Nie wykonano nowych oględzin PDF. Nie przenoszono PASS z poprzedniej kompilacji. Etap B pozostaje otwarty wyłącznie do zakończenia kompilacji i kontroli PDF. Postęp 23/44. Następny audyt 225: sprawdzić wynik tego jobu, artefakt pełnego tomu i zamknąć B po spełnieniu bramki; nie rozszerzać zakresu.
