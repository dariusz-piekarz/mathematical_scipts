# Audyt XC (90) — rozdział 25: trzeci przegląd i niezależne modele 2D

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6. Aktualny blob rozdziału d74356d24685f8e5d6f3395e83c72a96b65da921, zgodny z audytem LXXXIX. W tej iteracji bez zmian źródła.

## Przegląd matematyczny
Ponownie prześledzono mierzalność oscylacji w dowodzie względnego twierdzenia o różniczkowaniu: dla ustalonej stałej c półciągłość z dołu licznika, lokalnie skończona masa kuli gwarantująca ciągłość względem c, podstawienie borelowskiego reprezentanta przez przeliczalnie wartościowe przybliżenia; dodatni mianownik na nośniku. Dla promieni rosnących do r otwarte kule rosną do B(x,r), więc iloraz przy dodatnim mianowniku jest granicą ilorazów o wymiernych promieniach, również dla miar z atomami na sferach. W dowodzie oszacowania maksymalnego ponownie zweryfikowano wybór kul na ograniczonych zbiorach poziomicowych, brak powiększania, zliczanie z krotnością 15^d i przejście przez rosnącą rodzinę zbiorów. W dowodzie zaniku części osobliwej zwarty K zawiera się w nośniku koncentracji zerowej miary odniesienia, małe kule poza K go nie przecinają, a pozostała masa jest dowolnie mała. Lokalizacja zachowuje ilorazy dla małych promieni. W przypadku miar ze znakiem i zespolonych nierówność z wariacją całkowitą daje zanik składnika osobliwego. Nie stwierdzono nowych luk wymagających zmiany treści.

## Niezależne dokładne obliczenia
Rzeczywiście wykonano w JavaScript 6561 par miar atomowych na czterech wierzchołkach jednostkowego kwadratu, z masami 0,1,2. Siedem środków (w tym trzy poza kwadratem) oraz sześć kwadratów promieni, z dokładnymi porównaniami liczb dwójkowych i całkowitych ilorazów przez mnożenie krzyżowe:
- 32805 oszacowań słabego typu dla pięciu dodatnich progów (stała 15^2).
- 87642 przypadki zerowej masy odniesienia, pomijane przy obliczaniu supremum.
- 375840 porównań mas kul przy dwóch promieniach o kwadratach zbliżających się do wybranych wartości od dołu, w tym atomy na sferach.
Wszystkie kontrole poprawne. Są to testy skończonych modeli, a nie dowód ogólnego twierdzenia.

## CI i oględziny
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45299484681 dla f8b77ef7dabadce80a84f81923e2138589605cc9: job 138128746064 success. Rzeczywiste logi potwierdzają 7 testów rozdziału i 4 testy integralności tomu. Przy ostatnim odczycie job PDF 138128745663 in_progress, nie poświadczono jego wyniku.
Pobrano i sprawdzono poprzedni artefakt 14877492754 (3873361 bajtów, SHA256 bc0145fea377ccd5c3e35f1c5011c63e8060365edaed42a9c7f2a57a700d8a10 zgodny z metadanymi). Rozpakowano oba PDF i logi, niezależnie wyrenderowano i obejrzano wszystkie 7 stron poprzedniego samodzielnego rozdziału. Brak uciętych wzorów, kolizji, nieczytelnych oznaczeń; odczyt tekstu 0 wystąpień ??. Log rozdziału 0 Overfull, 0 Underfull, 0 ostrzeżeń o nierozwiązanych odsyłaczach. Pełny tom 265 stron, log 0 Overfull, 14 Underfull i 0 nierozwiązanych odsyłaczy; nie oglądano całego tomu. Oględziny odnoszą się do bloba a1608ca2fc3bcdbe13b8a4b67ffa60202416bc4e sprzed audytu LXXXIX, nie zastępują kontroli najnowszego PDF.

## Werdykt
24/31 ustabilizowanych. Rozdział 25 pozostaje w stabilizacji do potwierdzenia aktualnego PDF i obejrzenia wszystkich stron. Następna iteracja XCI (91): zamknięcie bramki najnowszej wersji, o ile wynik i skład pozwolą.
