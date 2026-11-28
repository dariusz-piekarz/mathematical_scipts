# Analiza funkcjonalna — rozdział 13 — audyt 03 (niezależna kontrola źródła)

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/13-przestrzenie-hilberta-reprezentacja-riesza-i-formy-poltoraliniowe.tex`.  
**SHA bloba źródła:** `1ca8b2ee077f558e50412c5d74e116779ab44f31`.  
**SHA bloba testu:** `ea8ea6a5b82596705f5f717c57317a6a06268369`.  
**Werdykt:** niezależny audyt matematyczny bez nowej poprawki; **1/2 czystych audytów źródła**, ale brak potwierdzonego zakończonego CI po zmianie testu z 13/02. Rozdział 14 pozostaje zablokowany.

## Stan zastany

Odczytano raport 13/02 i sprawdzono, że raporty 13/03, 13/04 i 14/01 nie istnieją jeszcze na wskazanej gałęzi. Odczytano źródło rozdziału 13 i test `tools/tests/test_functional_analysis_ch13.py`. W szczególności test zawiera zmianę usuwającą tautologiczną asercję opisaną w 13/02. Źródło rozdziału ma ten sam SHA co w raporcie 13/02.

Odczytane z GitHub API zadania przebiegu [#45254273546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45254273546) mają `completed/success`, w tym testy, kompilację i automatyczną kontrolę PDF. Jest to **starszy przebieg**, sprzed naprawy testu. Zapytanie o statusy commita `719a01df197324b8f3a0ec13fbdd59544c8251b8` zwróciło pustą listę, podobnie zapytanie o powiązane przebiegi PR; **nie jest to dowód ani sukcesu, ani porażki aktualnego CI**. W tej iteracji nie uruchomiono lokalnego pełnego unittest, kompilacji TeX ani inspekcji PDF.

## Niezależna kontrola matematyczna

Przejrzano **14/14 środowisk dowodowych**: nierówność Cauchy'ego–Schwarza, polaryzację (ze znakiem zgodnym z liniowością w pierwszym argumencie), rzut na domknięty zbiór wypukły i nieekspansywność, rozkład ortogonalny, reprezentację Riesza, Bessela, przeliczalność nośnika współczynników, zbieżność sieci sum Fouriera i Parsevala, istnienie baz ortonormalnych, dolne oszacowanie wymiaru Hamela przez rodzinę Vandermonde'a, izometrię z \(\ell^2(I)\), istnienie operatora sprzężonego, reprezentację form oraz twierdzenie Laxa–Milgrama. Sprawdzono w szczególności, że argument o domkniętym i gęstym obrazie operatora w dowodzie Laxa–Milgrama nie zakłada symetrii formy, a sieć sum Fouriera jest Cauchy'ego dzięki oszacowaniu ogonów sum kwadratów.

Przejrzano **5/5 przykładów**: \(\ell^2\), \(L^2\) i niehilbertowską normę supremum; rzut na stałe; szereg poza rozpięciem algebraicznym; Gram–Schmidt i układ trygonometryczny; słabe zagadnienie Poissona. Dla Poissona sprawdzono zerową średnią pochodnej, warunki brzegowe, całkowanie przez części oraz konstrukcję gładkich aproksymantów z korektą średniej. Nie stwierdzono nowej fałszywej tezy ani luki wymagającej zmiany źródła.

## LaTeX, odsyłacze i regresje

Odczytany test regresyjny zawiera kontrakty liczności: 14 środowisk `proof`, 5 `przyklad`, 30 etykiet i 13 odsyłaczy w kontekście rozdziałów 01–13, a także kontrolę polskiej terminologii i parzystości znaczników matematyki inline. Są to **oczekiwania zapisane w teście**, nie wynik jego wykonania w tej iteracji. Kontrola treści wykazała spójność notacji przestrzeni sprzężonej, form półtoraliniowych, funkcji charakterystycznej \(\chi\) oraz konsekwentną konwencję iloczynu skalarnego. Nie wykonano nowej inspekcji wizualnej PDF; raport 13/01 dokumentował strony 72–78 dla niezmienionego źródła.

## Decyzja

**13/03: czysty przegląd źródła, 1/2.** Nie zmieniano pliku rozdziału ani testów. Warunkiem dalszej stabilizacji jest niezależny audyt 13/04 i weryfikacja zakończonego CI dla commita zawierającego naprawiony test. Nie należy deklarować PASS ani otwierać rozdziału 14 bez tej weryfikacji.
