# Audyt CVIII (108) — Whitney i przejście do wzorów Lipschitzowskich
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 21cc62dd2564044cc1966431e9645e150a876be6.
Commit źródła 9b41bb602aee7f73222b1584f9b9424b2aba276d (blob 28034caf65c2721e46f320a978609f38b672ae3e).

## Kontrola matematyczna
Osiem celowanych poprawek, bez rozszerzania zakresu.
- Jawna definicja standardowej siatki diadycznej, uzasadnienie zagnieżdżenia kostek o przecinających się wnętrzach i rozłączności wnętrz maksymalnych kostek.
- Oszacowanie 21 sqrt(n) razy bok zapewniające dopuszczalność małej kostki; monotoniczność niespełniania warunku dla przodków i pokrycie dopełnienia.
- W zastosowaniu Łuzina jawnie wybrano zwarty podzbiór G przez regularność, zweryfikowano skończoność i regularność ograniczonej miary oraz skończony wymiar przestrzeni macierzy; oszacowano obie straty miary.
- Sprawdzono wszystkie hipotezy przy stosowaniu area do fragmentów C^1 oraz równość jakobianów i dokładną tożsamość włókien na K_j.
- Udowodniono obie nierówności w rozkładzie sumy po dowolnym włóknie na przeliczalną sumę sum po rozłącznych częściach, z uwzględnieniem wartości nieskończonej.
- Dla coarea jawnie skonstruowano fragmenty K_j i A_j, rozpisano ograniczenie funkcji borelowskiej do submersji F_j oraz tożsamość włókien i jakobianów na fragmentach.
- Dla części krytycznej zweryfikowano domkniętość warunku rangi przez minory i zastosowanie lematu do F_j, a nie do F, które jest tylko lokalnie Lipschitzowskie.
Zachowano wszystkie 28 etykiet. Rozdział ma 2056 wierszy.

## CI
Przebieg 45350940849 dla poprzedniego commitu fcbbc9fc4c7c053d20753513a5171ac726bd59d6: wszystkie trzy zadania zakończone sukcesem. Artefakt 14900735684 dostępny, nie pobierano go ani nie oglądano PDF w tej iteracji. Nowy commit wymaga osobnego CI; w chwili sprawdzenia lista przebiegów dla niego była pusta.

## Otwarte
Kontrola CI i PDF najnowszej wersji, niezależna kontrola rozdziału i ewentualne konieczne korekty. Stan 27/31; rozdział 28 pozostaje otwarty. Nie przechodzić do 29.
