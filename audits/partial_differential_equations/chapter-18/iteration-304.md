# RRC 18 — iteracja 304: konstrukcja operatora i zasada min–max

Commit źródła: bf1103b094db1647bf23b27e37feea2f26287095. Pierwsza szczegółowa lektura sekcji 18.1–18.3.

- Uzasadniono zwartość zanurzenia H_0^1 do L^2 dla dowolnego ograniczonego zbioru otwartego przez przedłużenie zerowe na kostkę i twierdzenie Rellicha–Kondrachova; usunięto zbędną lipschitzowskość w konstrukcji operatora Dirichleta. Uogólniono monotoniczność Dirichleta na niepuste ograniczone zbiory otwarte, również niespójne, co jest konieczne w późniejszym rozdzielaniu na sześciany.
- Ustalono rzeczywisty charakter form i zespolenie przy rozpatrywaniu widma.
- Uzasadniono jednoznaczność reprezentanta f w definicji operatora, ciągłość i koercywność przesuniętej formy oraz trywialność jądra operatora rozwiązującego.
- Rozpisano identyfikację dziedziny z obrazem T, opis współrzędnych dziedziny, samosprzężoność operatora diagonalnego i brak innych punktów widma przez konstrukcję rezolwenty.
- Naprawiono lukę w dowodzie min–max: wykazano, że przeskalowane funkcje własne są zupełnym układem ortonormalnym w przestrzeni Hilberta z iloczynem skalarnym przesuniętej formy. Parseval daje zbieżność rozwinięcia w normie formy oraz tożsamość dla energii. Uzasadniono osiąganie ekstremów.
- Przykłady i skalowanie w sekcji 18.3 odczytano, lecz wymagają jeszcze szczegółowej kontroli w następnej iteracji; dalsze sekcje nie są odebrane.

Kontrola zapisanego źródła: 790 wierszy (wcześniej 699), 42 unikatowe zachowane etykiety, 31 wystąpień odsyłaczy, brak niezgodności begin/end. Nowy cel thm:pde10-Rellich-p potwierdzony w rozdziale 10. Brak dedykowanej kompilacji rozdziału 18; przy odczycie API brak przebiegów dla commitu źródła.

Rozdział 17: audyt kontrolny 303 nie wykrył usterek; końcowy dedykowany run 45981760560 nadal in_progress przy ostatnim odczycie. Nie modyfikowano rozdziału 17. Rozpoczęto pracę merytoryczną nad rozdziałem 18 równolegle z oczekiwaniem na techniczne potwierdzenie rozdziału 17; nie jest to deklaracja pełnego odbioru.

Następny etap: odbiór końcowego CI rozdziału 17, domknięcie sekcji 18.3 i szczegółowy audyt prawa Weyla, w tym dyskretnego zliczania punktów kratowych, rozdzielania Dirichleta–Neumanna i odwracania asymptotyki.
