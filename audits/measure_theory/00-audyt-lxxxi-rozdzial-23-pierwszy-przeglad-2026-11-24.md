# Audyt LXXXI (81) — rozdział 23: pierwszy przegląd miary Haara

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

Rozdział 22 zamknięty w audycie LXXX (84475895e41461a8941e5714b4752422d9614453). Przeczytano cały rozdział 23: konstrukcja przez liczby pokrycia, zwartość produktu, zawartość na zbiorach zwartych, miara zewnętrzna i mierzalność otwartych, jednoznaczność, przykład grupy niesigma-zwartej, modularność i przykłady.

## Poprawki matematyczne
Commit 07e9fb5ed2429b09cad155fe2e06bacc6a097817, blob be274026c04ebde5cd1814439245a916b70e4a79.
- W końcowym kroku dowodu jednoznaczności brakowało zastąpienia mu przez c*mu przed zastosowaniem równości całek. Wprowadzono właściwą przeskalowaną miarę.
- Dodano lemat o funkcji odcinającej na dowolnej lokalnie zwartej przestrzeni Hausdorffa z dowodem opartym na normalności zwartej przestrzeni Hausdorffa, lemacie Urysohna i sklejaniu funkcji.
- Doprecyzowano wybór filtru właściwego w dowodzie zwartości produktu.
- W lemacie o Fubinim dla ciągłych jąder o zwartym nośniku skonstruowano podziały jedności i uzasadniono mierzalność całek wewnętrznych przez jednostajną aproksymację; nie zakłada się sigma-skończoności.
- W dowodzie jednoznaczności wprowadzono sieć funkcji o nośnikach malejących według odwrotnej inkluzji otoczeń, wykazano jednostajną zbieżność oraz jawnie ograniczono błąd całki na wspólnym zwartym nośniku.
- Uzasadniono ciągłość funkcji modularnej przez jednostajną ciągłość translacji i skończoną miarę wspólnego zwartego nośnika.
- Poprawiono terminologię drugiego aksjomatu przeliczalności.

Sprawdzono konwencję mu(Eg)=c(g)mu(E), zgodność z wyznacznikiem Ad(g^-1), jakobiany grupy afinicznej i przykład R razy nieprzeliczalna grupa dyskretna. W tej pierwszej iteracji nie stwierdzono innych błędnych tez. Wymagany niezależny drugi przegląd konstrukcji miary z zawartości i jednoznaczności.

## Testy i CI
Commit 8c4b7f44955ff61ba0755629517002965799de18: pięć metod testowych (liczby pokrycia S3, addytywność dla otoczenia jednoelementowego, skalowanie, dokładne jakobiany, kontrola źródła).
Rzeczywiście wykonano niezależnie w JavaScript 167417 dokładnych kontroli liczb pokrycia: wszystkie 32 otoczenia elementu neutralnego S3, wszystkie 64 podzbiory, niezmienniczość, podaddytywność, monotoniczność i addytywność dla otoczenia jednoelementowego. Wszystkie przeszły. Nie jest to dowód ogólnego twierdzenia ani uruchomienie testów Pythona.
Kontrola statyczna aktualnego źródła: 24 etykiety, wszystkie unikalne, poprawne zagnieżdżenie środowisk, trzy różne odsyłacze zewnętrzne.
Commit 33b485845752c8c530fce3c6ba39f24aa725b2ca: nowy workflow testów, integralności 31 rozdziałów, kompilacji pełnego tomu i samodzielnego rozdziału 23 z selektywnym importem odsyłaczy oraz renderowaniem każdej strony. Statusy przy odczycie: [].

## Werdykt
Rozdział 23 w stabilizacji. Nie przechodzić do 24 przed drugim audytem matematycznym, potwierdzeniem testów i kompilacji oraz oględzinami wszystkich stron izolowanego PDF. Nie oglądano PDF ani nie uruchamiano testów Python lokalnie w tej iteracji.
