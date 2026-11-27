# RRC 19 — iteracja 319: kontrola po trzecim audycie stabilizacyjnym

Źródło: commit da99e4b5e7b28193643df991c71dc2b7bbf2d6fc, blob ed60abea34b4993769337c380d58d6046a7385e2, 1412 wierszy. Potwierdzono zgodność blobu na gałęzi roboczej.

Porównano wszystkie 9 sekcji z wersją przed korektami 318 (commit c31fb70d0a0db2896cfba4323028cf60c5c7cd35): sekcje 1,3,5,6,7,9 identyczne; zmienione sekcje 2,4,8 odczytano w zakresie korekt i ich kontekstu. W szczególności sprawdzono dowód górnej półciągłości g(t): próba gładka o zwartym nośniku pozostaje dopuszczalna dla s bliskiego t dzięki odstępowi nośnika od zewnętrznego brzegu i argumentowi zwartościowemu dla F_s. Sprawdzono skalowanie, niezależność stałej od t, całkowalność na [h_{k_0},1], indeksy dyadyczne, podaddytywność skończoną oraz geometryczne oszacowanie sumy. Zweryfikowano rozróżnienie klas dopuszczalnych od ich infimów i hipotezę d>=1 w twierdzeniu o pojemności punktu. Nie wykryto nowych usterek wymagających zmian. Nie zmieniano źródła. Nie jest to kolejna niezależna pełna lektura dowodów: wcześniejsze pełne lektury są w 316–318, a w tej iteracji przeprowadzono kontrolę różnic.

Kontrola strukturalna aktualnego źródła: 37 zachowanych unikatowych etykiet, 50 wystąpień odsyłaczy, wszystkie cele jednoznaczne w źródle i pięciu aktualnych rozdziałach zależnych (7,9,10,14,18), brak niezgodności begin/end. 

Runy 45988455742, 45988751946, 45989155792, 45989522023 przy pierwszym odczycie queued; aktualny 45989522023 przy ponownym odczycie również queued. Nie potwierdzono kompilacji, odbioru wizualnego PDF ani globalnego CI. Samo klasyczne kryterium całkowe Wienera nadal jest wynikiem przywołanym ze wskazanym źródłem, nie dowodzonym od podstaw.

Pierwsza iteracja bez nowych usterek po pełnych lekturach stabilizacyjnych. Następny etap: pełna końcowa lektura kontrolna bez zmian, sprawdzenie CI, odbiór PDF. Przy braku nowych usterek w lekturze kontrolnej można rozpocząć rozdział 20, pozostawiając ewentualnie otwarty odbiór techniczny rozdziału 19.
