# Globalny audyt 36 — przekroje, skojarzenia i przepływy

2026-11-24. Baza 44f113d8f688b9016811c9725b7e5268794571d0. Przejrzano powiązania 04, 05, 11, 12 i 40. Najważniejsza korekta dotyczy dowodu rozkładu dowolnego przepływu całkowitoliczbowego (40), nie samego twierdzenia: w obecności cyrkulacji przez s,t minimum przepływu na ścieżce może przekroczyć wartość przepływu. Kontrprzykład: f(s,t)=2, f(t,s)=1, wartość 1. Stary krok odejmował 2, uzyskując wartość -1. Poprawny krok odejmuje minimum bieżącej wartości i minimum na ścieżce. Albo kończy fazę ścieżkową, albo zeruje co najmniej jeden łuk. Pozostałość o wartości zero jest cyrkulacją. Dodano przykład do tekstu.

04: dopisano argument identyfikujący minimalny przekrój i separator krawędziowy s,t. Rozkład w dowodzie Mengera usuwa cykle przed odejmowaniem jednostek i nie ma powyższej luki. 05: cykl naprzemienny ma parzystą długość, lecz niekoniecznie parzystą liczbę krawędzi każdego typu (np. cykl długości 6); doprecyzowano. We wzorze deficytu Halla suma |N(S)|+d dotyczy wyłącznie niepustego S. 12: wyraźnie odróżniono cyrkulacje modulo q od przepływów z przepustowościami i powiązano q=2 z przestrzenią cykli. Dowód dualności kolorowań na sferze wykorzystuje zerowanie bilansu na przekrojach, nie twierdzenie o maksymalnym przepływie; przypadki mostów i krawędzi równoległych są uwzględnione. 

Dodano niezależne regresje dokładne: wszystkie dopuszczalne przepływy na pełnych grafach skierowanych o 2–3 wierzchołkach z wartościami łuków 0–3 i nieujemną wartością netto (rekonstrukcja ścieżek i cykli); wszystkie grafy dwudzielne o obu częściach 0–3, porównanie skojarzeń, pokryć, deficytu i przekrojów sieci. Strażnik poprawionej formuły źródłowej. Włączono do CI.

Status: korekty zapisane; nie deklarujemy sukcesu testów ani kompilacji przed odczytem przebiegów. Audyt 36 otwarty.

## Stabilizacja — wynik pierwszego CI i korekta składu

Dla SHA 49f90b2ffa5560b4cf2de6f75e4ed3dae4a5fb75: workflow globalny 45297375724, job structural-audit 138121086189 success. Rzeczywisty log potwierdza PASS dla 430 dopuszczalnych przepływów całkowitoliczbowych oraz 689 grafów dwudzielnych. Osobny workflow algorytmiczny 45297375815, terminologia i aplikacja: success. Job full-book-pdf 138121085812: failure wyłącznie przez jedno Underfull hbox (badness 1609). Trzy przebiegi wygenerowały 298 stron. Pobrano artefakt 14877097750 i odczytano pełny log: ostrzeżenie w rozdziale 40, akapit 178–196, linia kończąca się „Kładziemy”. Przyczyna: skład rozbudowanego akapitu z długą formułą śródtekstową.

Skrócono zdania i wyodrębniono wzór na q do osobnego wiersza matematycznego, bez zmiany rozumowania, hipotez i strażnika regresyjnego. Nie zmieniano progów ostrzeżeń ani workflow. Konieczne ponowne przejście globalnego i algorytmicznego CI oraz kontrola wizualna PDF. Audyt 36 pozostaje otwarty.

## Zamknięcie audytu 36

Dla SHA 3641e789674bc74450165accc04f802abecd8977 wszystkie cztery workflow success: globalny 45299795206 (full-book-pdf 138129146559 oraz structural-audit 138129146932), algorytmiczny 45299795315, aplikacja 45299795303 i terminologia 45299795267. Odczytano logi: 298 stron, 0 ostrzeżeń, 0 nierozwiązanych odsyłaczy i ręcznych numerów rozdziałów, 430 przepływów i 689 grafów dwudzielnych PASS. Pobrano PDF z artefaktu 14877802452 i porównano tekst wszystkich 298 stron z artefaktem 14875698541 (audyt 35). Zmiany tekstu wystąpiły na stronach fizycznych 4, 33–34, 38–41, 66–70, 127–128 (14 stron); wyrenderowano i obejrzano wszystkie 14, nie stwierdzono obcięcia ani kolizji. Strona 66 zawiera poprawiony wzór, argument i nowy przykład. Porównanie certyfikowanej rewizji z bieżącą gałęzią nie wykazało innych zmian grafowych.

**Audyt 36 zamknięty.** Następny blok 37: zgodność konwencji topologicznych, homologicznych i algebraicznych. Globalny audyt tomu pozostaje otwarty.
