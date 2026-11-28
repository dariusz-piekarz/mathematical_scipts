# Audyt 211 — drukowany rozdział 23, pierwszy etap A

Data: 2026-11-25. Rozdział 22 zamknięto w 210.
Źródło: chapters/pl/graph_and_knot_theory/16-od-triangulacji-do-topologii-i-geometrii-rozmaitosci.tex.
Blob wejściowy 6db9e2d84940dfb8655db7e1c4e22e9a3600e8d2.
Korekta ad6fca178446a04f724e6236bb35b603b87f9c46, blob b5d0b9c783dde066355ab85dde1eb038bf26c84e.

## Usterki i poprawki
- GKT-23-GLUE-01: jawne dane sklejenia dwóch trójkątów dające sferę i torus, w tym mapa ilorazu kwadratu do S1 x S1; wszystkie trzy pary boków łączą w obu przykładach różne trójkąty. Rozróżniono kompleksy typu Delta od abstrakcyjnych kompleksów symplicjalnych.
- GKT-23-QUOTIENT-01: rozpisano domkniętość relacji równoważności (przekątna, grafy sklejeń, skończone dodatkowe pary wierzchołków), zwartość i własność Hausdorffa; udowodniono drugi aksjomat przeliczalności przez skończone sumy elementów bazy i domkniętość mapy ilorazowej.
- GKT-23-LINEAR-01: zamiast samego powołania na izotopię boków podano jawne homeomorfizmy boków sprzęgające sklejenia z liniowymi, ich promieniowe przedłużenia do trójkątów i odwrotności. Uwzględniono sklejenia dwóch boków tego samego trójkąta.
- GKT-23-LINK-01: opis sektorów barycentrycznych, parametru stożkowego i ogniwa jako grafu z odcinków narożnych; stopień dwa z krotnościami, warunek jednego okręgu, konieczność przez lokalną homologię i odsyłacz thm:tg-link-surface. W kolejnej stabilizacji doprecyzować, że przy tych szczególnych założeniach parowania wszystkich boków i relacji generowanej wyłącznie przez te pary spójność ogniwa wynika z definicji klasy wierzchołków; regresja 120 modeli to potwierdza, ale nie zastępuje dowodu ogólnego.
- GKT-23-COMPONENTS-01: składowe grafu dualnego wyznaczają spójne rozłączne zbiory domknięte i otwarte w ilorazie, ponieważ także utożsamienia wierzchołków są generowane przez sklejenia boków.
- GKT-23-HODGE-01: dowód d_{p+1}d_p=0, macierz kobrzegu w bazach dualnych, jawny wzór na sprzężenie przy dowolnych macierzach Grama: G_p^{-1}D_p^TG_{p+1}. Rozpisano identyfikację dopełnień ortogonalnych i rozkład Hodge'a; poprawiono termin samosprzężony.
- GKT-23-TRIANGLE-01: jawna macierz incydencji dla orientacji cyklicznej, jądro B^TB rozpięte przez (1,1,1), po wypełnieniu trójkąta laplasjan stopnia jeden wynosi 3I_3. Sprawdzono konwencję znaków macierzy B w źródle 06.
5 etykiet zachowanych, 13 poprawnie zagnieżdżonych par środowisk, cztery wystąpienia ref. Bez zmiany innych rozdziałów.

## Regresje
GKT-23-GLUE-01, test_gkt23_glue.js, commit c414fac456a43b3e27123e3c692fd2a2b5bf8ba5. PASS: wszystkie 15 parowań sześciu wystąpień boków dwóch trójkątów i 8 wyborów bijekcji końców, łącznie 120 modeli; 222 kontrole ogniw (stopień dwa i spójność), 48 modeli z trzema krawędziami między trójkątami, wśród nich 6 z chi=2 i 3 z chi=0 i odwróceniem orientacji na wszystkich bokach. Przy dwóch trójkątach wszystkie modele mają spójny graf dualny (nieparzysta liczba boków każdego trójkąta); nie jest to test modeli niespójnych. Nie liczono klas izomorfizmu.
GKT-23-HODGE-01, test_gkt23_hodge.js, commit 9ddab83e96b2a3922852d46e00b64873b6d3e382. PASS: 196 zestawów dodatnio określonych macierzy Grama na kołańcuchach trójkąta, w każdym przypadku co najmniej jedno sprzężenie różni się od zwykłej transpozycji; 196 kontroli jednowymiarowego jądra dla cyklu i 196 kontroli odwracalności laplasjanu po wypełnieniu. Dokładna arytmetyka BigInt, sprzężenia i laplasjany skalowane przez dodatnie wyznaczniki; sprawdzono samosprzężoność względem Grama, d^2=0, wyznaczniki i minor rzędu 2 oraz nieważony przypadek 3I_3.
Oba skrypty wykonano przed zapisem i po ponownym odczycie z repozytorium w izolacie JS. Nie potwierdzono wykonania w procesie Node ani integracji z CI; nie formalizacja Lean.

## Propozycje po pierwszym audycie
Opcjonalnie: rysunek dwóch sklejeń trójkątów (sfera i torus z identycznym grafem dualnym) oraz ilustracja rozkładu Hodge'a przed i po wypełnieniu trójkąta. Nie dodano bez zgody; dalsza stabilizacja dotyczy istniejącej treści.

## Bramka
Dla ad6fca17: terminologia 45585802574 SUCCESS, algorytmy 45585802955, pełny audyt 45585802480 i aplikacja 45585802773 w toku. Najnowszy PDF nie został obejrzany.
Etap A otwarty. Następny audyt 212: doprecyzować spójność ogniw przy pełnym parowaniu boków, kontrola założeń lokalnych, rozkładu Hodge'a, odsyłaczy, regresji oraz CI/PDF. Postęp 22/44.
