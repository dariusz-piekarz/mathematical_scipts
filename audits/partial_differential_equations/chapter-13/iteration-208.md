# RRC 13 — iteracja 208: pierwsza lektura 041–054

Źródło przed 5316cd389e8b023a74ea42de61776ce22fff1885, po 63ec3fa62b8867d120a9873b8672e90110bbb40e. Commity a828aa7c6781c2caa0ace29d497fae91b32551eb i a344b6ff71fa01fd8e28fa0042591bd917d430bf. Odczytano pełne sekcje Neumanna i Robina.

| Kryterium | Wynik |
|---|---|
| PDE-13-041 | Ujednolicono termin jednostajnej eliptyczności; nierówność Poincarégo–Wirtingera jest dokładnie przypadkiem p=2 zweryfikowanego wniosku RRC 10. Zamiast powielać dowód wykorzystano odsyłacz. |
| PDE-13-042 | Jawnie odnotowano spójność obszaru, wniosek o stałej funkcji i kontrprzykład na dwóch składowych. |
| PDE-13-043 | Konieczność warunku zgodności z testu 1; istnienie rozwiązania o średniej zero wyraźnie uwarunkowano zgodnością danych. |
| PDE-13-044 | Domkniętość podprzestrzeni o średniej zero, pełny iloczyn skalarny Sobolewa i jawna stała koercywności lambda/(1+C_W²). |
| PDE-13-045 | Ograniczoność formy i funkcjonału brzegowego z dokładną stałą śladu; zastosowanie Laxa–Milgrama. |
| PDE-13-046 | Rozkład dowolnego testu na część o średniej zero i stałą; jawnie sprawdzono obie strony na stałej. |
| PDE-13-047 | Oszacowanie rozwiązania, jednoznaczność modulo stałe w obu kierunkach i normalizacja średniej. |
| PDE-13-048 | Uporządkowano wzór Gaussa–Greena z miarami, hipotezy gładkości oraz rozróżnienie znaku pochodnej konormalnej od strumienia fizycznego -A∇u. |
| PDE-13-049 | Zdefiniowano słaby strumień q_nu na H^{1/2}(∂Ω), wykazano niezależność od przedłużenia i ciągłość. |
| PDE-13-050 | Obie implikacje równoważności wariacyjnego Neumanna z równaniem wewnętrznym i słabym warunkiem konormalnym. |
| PDE-13-051 | Nierówność z członem brzegowym: konstruktywny dowód z rozkładu na średnią i resztę zamiast powtarzania argumentu zwartości; jawna stała oraz dodatnia skończona miara brzegu. |
| PDE-13-052 | Robin: jawne stałe ciągłości i koercywności, oszacowanie przez Laxa–Milgrama. |
| PDE-13-053 | Równoważność słabego Robina z równaniem wewnętrznym i konormalnym warunkiem brzegowym. |
| PDE-13-054 | Bilans całkowy Robina przez test 1; nie jest warunkiem zgodności danych jak dla Neumanna. |

10 zamian blokowych i 3 doprecyzowania w następnym commicie. Zachowano kolejność wszystkich 39 etykiet, w tym 38 pierwotnych. 78/78 wystąpień odsyłaczy (43 różne cele) rozwiązanych jednoznacznie w RRC 06,07,09,10,11,12,13. Stos środowisk poprawny. Odczytano tezy o Poincarém, śladzie, normie ilorazowej i prawym odwrotnym śladu z RRC 10. 72/72 pomocnicze skończone kontrole rozwiązania na odcinku z jednorodnym Robinem (36 par warunków brzegowych oraz 36 bilansów całkowych). Nie zastępują dowodów. Źródło 1095 wierszy.

Pierwsza lektura: 54 kryteria, 7/9 sekcji. Następny etap: transmisja, wyprowadzenie wzoru na rozwiązanie, weryfikacja warunków brzegowych i skoku strumienia, obie implikacje równoważności, rysunek, podsumowanie. Nie wykonano kompilacji, dedykowanego CI, inspekcji PDF ani Lean. Stabilizacja niepotwierdzona.


## Uzupełnienie po uzgodnieniu równoległych zmian

Pierwsza próba zapisu w drugim przebiegu została odrzucona przez GitHub (409), ponieważ aktualizowano tę samą sekcję. Odczytano ponownie bieżące źródło i istniejący raport; zachowano wszystkie równoległe poprawki. W commicie cc1145bb02b235b722073659cfab6d123684170c (blob 3fa8b39ed9e7f7bff9f7e5e4dd8ca2550d325b40) dodano wniosek cor:pde13-robin-partial: dla nieujemnego ograniczonego współczynnika beta wystarcza dodatnia całka B_beta po brzegu. Udowodniono ważone oszacowanie normy pełnej H¹ przez gradient i ważoną normę śladu, wyprowadzono stałą koercywności min(lambda,1)/(D_beta²+r_beta²) oraz wskazano, że przy B_beta=0 wracamy do Neumanna. Jest to rozszerzenie kryterium 052, bez zmiany dotychczasowej numeracji kryteriów.

Po rozszerzeniu: 1148 wierszy, 40 etykiet (39 zachowanych i 1 nowa), 82/82 wystąpienia odsyłaczy (44 różne cele) rozwiązane jednoznacznie w RRC 06,07,09,10,11,12,13. Stos środowisk poprawny. Dodatkowo 60/60 pomocniczych skończonych kontroli ważonej nierówności dla funkcji afinicznych na przedziale z dodatnią wagą tylko na jednym końcu. Kontrole nie są dowodem ani testami CI. Nie przeprowadzono kompilacji, kontroli PDF ani formalizacji. Następny zakres pozostaje bez zmian.
