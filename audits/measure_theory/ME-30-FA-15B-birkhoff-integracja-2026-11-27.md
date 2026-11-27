# FA-15B / ME-30 — integracja całki Birkhoffa

Stan wejściowy: 0f825e9a20a05ba81ac76d888c26160579a81014. ME-30 ma ukończone audyty stabilizacyjne i kontrolny (raport z commitu 544b91035b3b691ca9211535c7c7306d764f799f).

- Porównano definicje w FA-15B i ME-30: zupełna miara skończona, podziały skończone/przeliczalne, wszystkie rozdrobnienia, wszystkie znaczniki, bezwarunkowa zbieżność w normie. Zgodność potwierdzona.
- FA-15B zawierał odsyłacze do całki Bochnera i RNP w ME-30, lecz nie do nowej sekcji Birkhoffa. Dodano trzy odsyłacze odwrotne: sekcja, konstrukcja miary wektorowej oraz półnorma.
- Wskazano różnicę perspektyw obu skryptów, bez usuwania dotychczasowych dowodów i bez zmiany etykiet. ME-30 pozostawiono bez zmian.
- Zweryfikowano istnienie wszystkich trzech celów w źródle ME-30 i zachowanie wszystkich etykiet FA-15B. Dodano test dwukierunkowych odsyłaczy. Testy CI oraz renderowanie aplikacji po nowym commicie wymagają potwierdzenia.
