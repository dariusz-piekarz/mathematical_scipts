# Audyt 223 — drukowany rozdział 24, stabilizacja etapu B

Data: 2026-11-25. Kontynuacja 222 bez rozszerzania zakresu matematycznego.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Blob 6aaca3436174ab0b28de4f43218d2c2f8dd0a830 bez zmian. Plik główny tomu: blob 9298d7d95e1787db19382449018320ac3cb91a79. Kontrola strukturalna źródła: 30 zgodnie zagnieżdżonych par środowisk, 5 etykiet, 5 odsyłaczy do 4 różnych celów sprawdzonych w 222. Brak zmian matematycznych i graficznych.

## Regresja
Odtworzono kod GKT-24-BS12-PY-01 z audytu 222 w rzeczywistym procesie Python, z Fraction. PASS: 6534 reprezentantów, 594 odwrócenia, 26730 translacji, 4602 incydencje (38460 iteracji kontrolnych), 1534 wierzchołki, 1533 krawędzie. Ograniczony model afiniczny, nie dowód twierdzenia ani formalizacja Lean.

Wykryta luka organizacyjna: test z 222 nie był wykonywany przez CI. Włączono go jako check_bs12_cosets() do tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py i wywołano w bloku __main__. Dodano kontrolę oczekiwanych liczników. Commit fcce40f7b25b4aa8db9b7f75974a2986330d33dc; potwierdzono ponownym odczytem blob b01851e33633381568d88ecd3d41660022a31a44 i obecność wywołania. Istniejący globalny workflow obserwuje tę ścieżkę i uruchamia ten plik. Nie tworzono nowego workflow. Lokalnie wykonano samodzielny model, a nie pełny plik testowy po integracji.

## Bramka
Przebieg algorytmiczny 45590640493 dla raportu 222 (c0c7a0ce) zakończył się success; nie obejmuje jednak nowo podłączonej regresji. Pełny workflow 45591196612 dla fcce40f7 został uruchomiony i był queued przy odczycie. Nie przypisano mu PASS. Nie oglądano ponownie PDF. Etap B pozostaje otwarty do sprawdzenia faktycznego wyniku zintegrowanej regresji i kompilacji pełnego tomu, a następnie kontroli końcowej. Postęp 23/44. Następny audyt 224: weryfikacja logu GKT-24-BS12-PY-01 w przebiegu 45591196612 i artefaktu PDF, zamknięcie B wyłącznie po spełnieniu bramki.
