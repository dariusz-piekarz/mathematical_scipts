# Topologia ogólna — rozdział 10, audyt 3

- **Rozdział:** Metryzowalność przestrzeni topologicznych.
- **Wersja źródła:** 0.2 (bez zmian względem audytu 2).
- **Status:** **pierwszy czysty audyt 1/2**.
- **Plik źródłowy:** `chapters/pl/general_topology/10-metryzowalnosc.tex`.
- **Liczba wierszy:** 768.
- **SHA-256 źródła:** `ad5de242b4dd63fdadea8eb5228e910e774147396f06dfe04611b1b150a4f088`.
- **GitHub:** brak integracji rozdziału 10 przed dwoma kolejnymi czystymi audytami.

## Niezależny audyt matematyczny

Sprawdzono kolejno wszystkie definicje, stwierdzenia, wnioski, dowody, przykłady i uwagi (768 wierszy źródła):

1. **Pseudometryki i metryki.** Bazowość kul na podstawie nierówności trójkąta, lokalna przeliczalna baza otoczeń, aksjomat T1 i regularność przestrzeni metrycznej. Osobno oceniono przypadki przestrzeni pustej i jednoelementowej.
2. **Metryki zgodne i podprzestrzenie.** Nierówność trójkąta dla obcięcia `min(1,d)`, równość baz małych kul, dziedziczenie przez podprzestrzenie, przeniesienie przez homeomorfizm. Przykład nieprzeliczalnej przestrzeni dyskretnej po korekcie z audytu 2 poprawnie stwierdza, że każda baza zawiera wszystkie singletony.
3. **Regularność i Lindelöf → normalność.** Wybór przeliczalnych rodzin otwartych, dziedziczenie Lindelöfa przez podprzestrzenie domknięte, otwartość konstruowanych sum i rozłączność uzyskanych otoczeń. Przypadki pustego F lub G są uwzględnione.
4. **Twierdzenie Urysohna o metryzowalności.** Istnienie par bazowych `(B,C)` spełniających `x ∈ B ⊆ cl B ⊆ C ⊆ O`, użycie lematu Urysohna z rozdziału 05, numeracja funkcji, zbieżność jednostajnie ograniczonego szeregu, dodatnia określoność, nierówność trójkąta oraz *oba* włączenia między topologiami. W szczególności powtórnie sprawdzono argument otwartości całej kuli, poprawiony w audycie 1.
5. **Kostka przeliczalna i iloczyny.** Kontrola zbieżności i zgodności metryk z topologią iloczynu, w tym przypadku cylindra bez ograniczeń; izometryczne zanurzenie do kostki Hilberta i warunki dla przeliczalnych rodzin czynników.
6. **Zwarte przestrzenie Hausdorffa.** Oba kierunki kryterium metryzowalności; konstrukcja zbioru co najwyżej przeliczalnego gęstego z podpokryć skończonych.
7. **Kontrprzykłady.** Prosta Sorgenfreya (bazowe zbiory domknięto-otwarte, regularność i brak metryzowalności), kostka nieprzeliczalna (brak lokalnej bazy przeliczalnej), iloraz z dwoma początkami (brak warunku Hausdorffa) i dwie metryki zgodne, z których tylko jedna jest zupełna.

Nie wykryto błędów matematycznych, brakujących wymaganych hipotez, nieuzasadnionych wzorów ani nieprecyzyjnych odwołań, które wymagałyby poprawek. Nie poszerzono zakresu rozdziału.

## Wyniki testów i kompilacji

- `bash tools/validate_general_topology_ch10.sh` — **PASS**, log: `/mnt/data/topologia_ogolna_ch10_audit03_validation.log`.
- Regresja rozdziałów 01–10 — **PASS**.
- Modele skończone: 390 topologii, 7 konstrukcji metryk rozdzielających, 1295 trójek metrycznych, 551 880 trójek dla metryk iloczynowych — **PASS**.
- Odsyłacze: 393 unikatowe etykiety, 104 rozwiązane odsyłacze — **PASS**.
- Kontrola terminologii, w tym zwrotów „spełnia pierwszy/drugi aksjomat przeliczalności” — **PASS**.
- PDF rozdziału 10 — **8 stron**, bez ostrzeżeń kompilatora.
- PDF całej książki — **88 stron**, bez ostrzeżeń kompilatora.
- Wyrenderowano i skontrolowano wizualnie wszystkie osiem stron. Diagram Urysohna, podział stron i matematyczne wzory są czytelne; brak ucięć, nachodzenia elementów i niepożądanych sierot.

## Status i następny etap

**Audyt 3 jest czysty, 1/2.** Źródło wersji 0.2 pozostało niezmienione. Następny etap to audyt 4 tego samego źródła. Jeśli również będzie czysty, rozdział 10 będzie stabilny i może zostać zintegrowany z bieżącą gałęzią oraz sprawdzony w GitHub Actions.
