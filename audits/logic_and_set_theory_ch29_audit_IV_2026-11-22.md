# Logika matematyczna i teoria mnogości — rozdział 29, audyt IV

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/29-slabsze-zasady-wyboru-i-ich-ograniczenia.tex`.

## Kontrola definicji i algebraicznych implikacji

W definicji algebry Boole'a występował tylko opis „ideał pierwszy to dopełnienie ultrafiltru”, pomijający standardową niezależną definicję ideału oraz jego pierwszości. W ramach audytu zapisano pełne warunki: `0_B∈I`, `1_B∉I`, domknięcie ku dołowi, domknięcie na sumę boolowską, a dla pierwszości implikację `a∧b∈I ⇒ (a∈I lub b∈I)`.

Następnie w dowodzie kryterium ultrafiltru dopisano **obie implikacje**:
- dla ideału pierwszego `I`, dopełnienie `U=B\I` jest filtrem (domknięcie ku górze oraz na iloczyn), a warunek pierwszości i `b∨¬b=1_B` sprawiają, że ultrafiltrowe rozstrzyganie `b` lub `¬b` jest zupełne;
- dla ultrafiltru `U`, zbiór `I=B\U` jest właściwym ideałem, domkniętym ku dołowi i na sumę, a pierwszość wynika ze sprzeczności z domknięciem `U` na iloczyn, jeśli obydwa czynniki leżą poza `I`.

Nie dodano nowych twierdzeń ani lematów; uzupełniono definicję i istniejący dowód. Testy dla skończonej algebry `P({0,1,2})` sprawdzają zgodność standardowych warunków pierwszości z warunkami dopełnienia ultrafiltru oraz nie mylą ultrafiltrowego rozstrzygania dopełnień z całym zestawem warunków filtru.

## Ponowna kontrola matematyczna

Weryfikacja konstrukcji skończenie generowanego filtru i ultrafiltru, rozstrzygnięcia atomu w skończonej podalgebrze, zwartości `2^B` z UF, obydwu wersji Tychonoffa oraz równoważności lematu Tukeya i AC nie wykazała dodatkowych braków. Wyniki te były również porównywane z zewnętrznymi referencjami o równoważnikach aksjomatu wyboru.

**Inwentarz niezmieniony:** 6 definicji, 7 twierdzeń, 1 lemat, 5 przykładów, 7 uwag, 8 dowodów, 24 etykiety, 11 odsyłaczy.

**Werdykt:** audyt IV uzupełnił standardową definicję matematyczną i jej równoważność z dotychczasowym opisem. Przed oznaczeniem rozdziału jako stabilnego wymagany jest czysty audyt V, aktualne zielone CI i kontrola wizualna PDF.
