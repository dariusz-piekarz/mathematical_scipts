# RRC 17 — iteracja 300: drugi audyt stabilizacyjny

Commit źródła: bcd6faf0343d2ba23493a2db7fb104afc1e4788d.

Ponowna lektura dowodów, zwłaszcza iteracji i pokrycia w lemacie Johna–Nirenberga:
- Doprecyzowano oznaczenia miary i średniej oraz rzeczywisty charakter pod- i nadrozwiązań.
- Rozpisano normalizację rekurencji De Giorgiego i indukcję.
- Uzasadniono przejście od norm L^p do kresu istotnego w iteracji Mosera bez pomijania argumentu na zbiorach nadpoziomowych.
- Uzasadniono istnienie maksymalnych kostek dyadycznych, pominięcie brzegów miary zero, indukcję dla miar kolejnych pokoleń i teleskopowanie różnic średnich.
- Sprawdzono geometryczne zawieranie kul opisanych na podkostkach w większej kuli.

Kontrola zapisanego źródła: 935 wierszy (wcześniej 895), 36 etykiet zachowanych w tej samej kolejności, 36 unikatowych, 40 wystąpień odsyłaczy i te same cele zewnętrzne co w iteracji 299, brak niezgodności begin/end.

Dedykowany przebieg 45978707543 na commicie b31abec2bc6a310fefd90e9de803670d8f7af54a zakończył się SUCCESS: kompilacja zależności, rzeczywiste numery odsyłaczy, kompilacja rozdziału, diagnostyka logu, renderowanie i publikacja artefaktu 15189020464 (3363282 bajty). Dotyczy źródła sprzed korekt w iteracji 300. Nie wykonano samodzielnej kontroli wizualnej artefaktu. Nowy commit wymaga ponownego CI; przy odczycie API widoczne przebiegi terminologii 45980459455 i rozdziału 16 45980459484 w kolejce, jeszcze bez dedykowanego runu rozdziału 17.

Następny etap: kolejna stabilizacyjna lektura po zmianach, sprawdzenie CI aktualnego źródła i odbiór wizualny PDF, potem niezależny audyt kontrolny. Nie deklarować stabilizacji przed odbiorem.
