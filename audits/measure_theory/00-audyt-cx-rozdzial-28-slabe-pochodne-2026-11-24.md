# Audyt CX (110) — słabe pochodne i Rademacher
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 0c18b021eba0b2c41e8e5f0d7497c898023a6001, blob aa60f0af2f22ae958372ec832120de11d82323c9. Commit źródłowy b48ac30be2516120b2caf96177bda678d8203d23, blob 78ffeae8625569ea3a21fc85a045e4eb0536737a.

## Wyniki matematyczne
- Dziesięć celowanych zmian, wszystkie 28 etykiet zachowane.
- Jawne wymiary i zakres przyrostów w definicji różniczkowalności Frécheta.
- W jednowymiarowym lemacie sprawdzono hipotezy twierdzenia Radona–Nikodyma dla miar skończonych, dowiedziono ograniczenia gęstości przez 2L i rozpisano reprezentację całkową z uwzględnieniem końców przedziału.
- Całkowanie przez części na przekrojach wyprowadzono bezpośrednio przez reprezentację całkową, z dwoma zastosowaniami Fubiniego i sprawdzeniem bezwzględnej całkowalności.
- Jednoznaczność funkcji reprezentującej słabą pochodną udowodniono za pomocą gładkich funkcji testowych o całce 1 i twierdzenia o punktach Lebesgue'a. Nie korzysta się z twierdzenia Rademachera w tym argumencie.
- Rozpisano przejście od różniczkowalności wszystkich składowych do różniczkowalności wektorowej i oszacowanie normy różniczki.
- Ujednolicono zapis Łuzina zgodnie z rozdziałem 10 i wskazano etykietę jego twierdzenia.
- Ponownie sprawdzono dowód zerowości włókien krytycznych: skale, borelowskie funkcje dominujące, kolejność kwantyfikatorów i wyjątki miary zero; nie stwierdzono nowej luki w tym argumencie.

## CI
Przebieg 45351526792 dla poprzedniego commitu cd628415d3a9bbc56b11dae97ef7af0f475bba0e: wszystkie trzy zadania sukces. Artefakt 14901215102 dostępny, nie pobierano i nie oglądano PDF w tej iteracji. Terminologia nowej wersji przeszła; dedykowana bramka 45351767462 trwa.
## Otwarte
Kontrola najnowszego CI i PDF, niezależna kontrola pozostałych szczegółów Whitneya i wersji rozmaitościowej, końcowa stabilizacja. Stan 27/31; rozdział 28 otwarty. Nie przechodzić do 29.
