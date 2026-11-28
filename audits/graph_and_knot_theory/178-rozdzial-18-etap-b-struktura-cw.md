# Audyt 178 — drukowany rozdział 18, niezależny etap B

Data: 2026-11-25. Wejściowy blob po zamknięciu A: b1a926c25e6eb8dea68f79eef1322ea76f10f580.
Korekta: 744631c9cede6046a594bdd0d36b289736984624, blob 93a01f499f7072022f2fa51805bb81add999da19.
Źródło: chapters/pl/graph_and_knot_theory/11-grafy-na-powierzchniach-grafy-dualne-i-homologia-komorkowa.tex.

## Ustalenia niezależnej kontroli
- B-01: brak uzasadnienia przejścia od dowolnego komórkowego zanurzenia do struktury CW i modelu dysków oraz pasów. Uzupełniono argument odwołujący się do lokalnego prostowania i regularnego otoczenia z twierdzenia thm:tg-euler-plane: składowa dopełnienia otoczenia jest zwartą powierzchnią z brzegiem; dołączenie półotwartych kołnierzy daje ścianę, która retraktuje się na tę składową. Kontraktowalność i klasyfikacja powierzchni wymuszają dysk; odwzorowania charakterystyczne otrzymujemy przez domknięcie kołnierza i rzutowania na szkielet. Jest to audyt semantyczny, a nie wykonany test formalny. Trwałe kryterium ponownej kontroli GKT-18-CW-01: sprawdzić oba rodzaje powierzchni, wielokrotne wystąpienia wierzchołka, izolowany wierzchołek, brak założenia o prostocie brzegu i własność ilorazu zwartego w przestrzeń Hausdorffa.
- B-02: definicja grafu dualnego nie wymagała jawnie rozłączności wnętrz krawędzi dualnych i używała słowa łuk także dla pętli. Doprecyzowano definicję.
- B-03: jawnie dodano przypadek m=0 do definicji operatorów brzegu: n=f=1, C1=0, oba operatory zerowe, jedna ściana nie jest cyklem permutacji pustego zbioru. Kryterium GKT-18-EMPTY-01: w tym przypadku H0=H2=Z, H1=0, T i T* mają pusty zbiór krawędzi; nie liczyć f przez cykle pustej permutacji. Kontrola semantyczna.
- B-04: w dowodzie homologii rzeczywistej zastąpiono powtórzony argument o spójności grafu dualnego bezpośrednim odwołaniem do thm:tg-cellular-dual.
- B-05: uzasadniono prezentację grupy fundamentalnej torusa przez twierdzenie van Kampena i izomorfizm z Z² przez postać a^p b^q.
- Ponownie przejrzano ograniczenia rodzaju, przykład theta, jawne rotacje K5 i K3,3, wzory dualizacji, rozkład drzewo–drzewo dualne oraz całkowitą redukcję homologii. Nie zmieniono ich twierdzeń. Nie dodano nowego zakresu. Sprawdzono powiązania z rozdziałami źródłowymi 02, 06, 07, 09. Wszystkie 14 etykiet zachowano, 43 pary środowisk poprawnie zagnieżdżone.

## Regresje wykonane ponownie po korekcie
Pięć istniejących skryptów JS wykonanych w izolacie JS z równoważnymi asercjami Node (nie proces Node): BRIDGE-01 PASS 1067, ROT-01 PASS 7776+64, TC-01 PASS 2546 układów/4442 rozkłady/8996 elementów bazy/12354 relacje, ORIENT-01 PASS 6177 kontroli znaków, FIG-01 PASS (42.501011 stopnia > 24 stopnie). Nie są to dowody topologiczne ani formalizacja Lean. Nowe kryteria semantyczne zapisano w tym raporcie, nie oznaczamy ich jako automatycznych testów.

## Bramka
CI dla nowej korekty w chwili kontroli: Graph and knot theory - full book global audit 45567894109 in_progress; Graph and knot theory - algorithms audit 45567894177 in_progress; Mathematical library application checks 45567894113 in_progress; Polish mathematical terminology 45567894098 success.
PDF po zmianie nie został skompilowany lokalnie ani obejrzany. Audyt B pozostaje otwarty; po zmianie wymagana ponowna stabilizacja, weryfikacja nowych dowodów i PDF dla nowego blobu. Nie przechodzimy do rozdziału 19.
