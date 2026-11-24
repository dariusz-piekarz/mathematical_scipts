# MA1-15 — trwałe kryteria regresyjne
Testy Python sprawdzają skończone świadki oraz tożsamości w dokładnej arytmetyce. Nie zastępują dowodów ciągłości, zwartości ciągowej ani granic.
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| MA1-15-001 | ma1:def:continuity, ma1:ex:isolated-continuity | Punkt należy do dziedziny, przypadek izolowany, porównanie z granicą przekłutą | semantyczna + Python |
| MA1-15-002 | ma1:thm:continuity-sequential | Oba kierunki, zaprzeczenie z jednym epsilon_0, ciąg może zawierać p | semantyczna |
| MA1-15-003 | ma1:def:relative-open, ma1:ex:relative-open | Otwartość względna, równoważność domkniętości z warunkiem ciągowym | semantyczna + Python |
| MA1-15-004 | ma1:thm:continuity-preimages | Trzy równoważności, otwartość kuli, przeciwobraz dopełnienia; kontrprzykłady dla obrazów | semantyczna + Python |
| MA1-15-005 | ma1:thm:continuous-composition | Ciągłość w f(p), dobór promieni, brak warunku unikania f(p) | semantyczna |
| MA1-15-006 | ma1:thm:continuity-algebra, ma1:ex:continuous-polynomials | Rachunek ciągłości, moduł, niezerowy mianownik i dziedzina ilorazu | semantyczna + Python |
| MA1-15-007 | ma1:cor:continuous-local-bounds | Lokalne ograniczenie oraz zachowanie ścisłego znaku | semantyczna + Python |
| MA1-15-008 | ma1:def:sequentially-compact, ma1:lem:interval-seqcompact, ma1:thm:continuous-compact-image | Granica podciągu należy do zbioru, Bolzano–Weierstrass, obrazy i pusty zbiór | semantyczna |
| MA1-15-009 | ma1:thm:weierstrass-extrema, ma1:cor:interval-extrema | Niepustość, ograniczoność, wybór ciągu przy supremum, podciąg i osiąganie obu kresów | semantyczna |
| MA1-15-010 | ma1:ex:extrema-assumptions | Brak osiągania kresów na otwartym przedziale, nieograniczoność, nieciągłość na [0,1] | semantyczna + Python |
| MA1-15-011 | ma1:thm:intermediate-value, ma1:cor:continuous-interval-image | Końce, odwrócenie znaku, supremum E, f(c)<=t, wybór punktu po prawej, obraz przedziału | semantyczna + Python |
| MA1-15-012 | ma1:ex:ivt-root | Zmiana znaku wielomianu, ścisły wzrost, przedział obejmujący pierwiastek na rysunku | semantyczna + Python |
| MA1-15-013 | ma1:def:homeomorphism, ma1:thm:compact-continuous-inverse, ma1:ex:square-inverse-continuous | Kontrprzykład dyskretnej metryki, dalszy podciąg, iniektywność, odwrotność x^2 | semantyczna + Python |
| MA1-15-014 | ma1:lem:relative-open-representation | Otwartość względna jako przecięcie z otwartym zbiorem, obie implikacje, pusty zbiór, domkniętość przez dopełnienie | semantyczna + Python (test_relative_representation_and_complement) |
| MA1-15-015 | ma1:thm:compact-continuous-inverse | Jawna nierówność trójkąta dla dalszego podciągu, dolne ograniczenie odległości granicy od x | semantyczna + Python (test_distance_estimate_for_inverse) |
