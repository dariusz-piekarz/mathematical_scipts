# Rozdział 15 — audyt 27 (poprawkowy, 0/2)

Data: 24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia raport 26 f2a8f7fba468e92acaf4d9b1e0acf0c6b69b891a, źródło 637eab7b6f13e150ac3f208fc0ab92d80a314010.

## Matematyka i redakcja
Ponownie sprawdzono wszystkie siedem podsekcji, zwłaszcza kolejność argumentów w dowodzie symetrii, indukcję całkową Taylora, oszacowanie minimum, kontrakcję i otwartość obrazu, odwracanie między różnymi przestrzeniami, wybór prostokątów w twierdzeniu uwikłanym, różniczkowanie szeregu eksponenty w normie operatorów wieloliniowych. Wzory i tezy są poprawne.
12 zamian źródłowych: ujednolicono definicję operatorów wieloliniowych, kryterium zupełności, utożsamienie izometryczne i definicję klasy C^m nad R oraz C (konieczne dla już istniejących zespolonych pochodnych operatorowych); jawny zakres j; poprawiono tytuł przykładu hesjanu i literówkę; uściślono kwantyfikator H i stałą w oszacowaniu reszty odwracania; uzupełniono składnię twierdzenia o pochodnych odwrotności; sprecyzowano całkę po sympleksie i rozpisano rekurencję beta oraz krok indukcyjny z jakobianem i skróceniem silni. Nie dodano nowych tematów.

## Technika
Dedykowany workflow na raporcie 26: 45356976835, job 138317107880, 9/9 etapów, 8/8 testów, trzy przebiegi pdflatex, 138 stron, PDF 1357393 bajtów, artefakt 14902858623. Pobrano i rozpakowano, sprawdzono log: jedno znane underfull hbox 1127, brak overfull, brakujących znaków, niezdefiniowanych odsyłaczy i poleceń. Obejrzano render stron 87–94 (w tym przejście do 15A), bez widocznych kolizji lub obcięć; oględziny wersji przed korektą. Źródło po korekcie commit 76d2dcfbbb5e62891931ae08dbcb810715d11895, blob 66074009c8c4be39f19659ca126940ec03e3326b, 361 wierszy, 25 etykiet, 14 dowodów, 6 przykładów. Zagnieżdżenie środowisk i wszystkie 10 wystąpień odsyłaczy sprawdzone. Testy bez zmian, 8. CI po zmianie 45357544052 było w toku przy odczycie.

## Decyzja
15: 0/2. Audyt 28 nadal rozdział 15, ze sprawdzeniem skorygowanych definicji, indukcji beta, CI i składu PDF. 14 stabilny. Następnie 15A, 15B, 16 itd. Zakres zamknięty.