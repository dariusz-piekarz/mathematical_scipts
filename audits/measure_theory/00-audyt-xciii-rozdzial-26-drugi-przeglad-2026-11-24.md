# Audyt XCIII (93) — rozdział 26: drugi przegląd

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Stan wejściowy
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45304781777 dla fb39edcb4fffb5998d669c7d5ab3b8a298518d7f zakończony success. Logi 138145831028 i 138145830527: 4 testy rozdziału i 4 integralności tomu; pełny PDF 266 stron, samodzielny rozdział 10 stron, 32 lokalne etykiety i 4 zewnętrzne. Dotyczy poprzedniego bloba 78721a925262f5438f2d9a0551b3e9c6af648dfc.

## Zmiany
Commit 0b3c25672dc67cad3580d0b509a412349e672e63; blob a1841ba4a04a5ad3f81e2cc63d162dfe65a638a0.
- Doprecyzowano borelowskie nadzbiory o tej samej mierze i odróżniono tę własność od regularności względem otwartych (kontrprzykład miary liczącej).
- Uzasadniono istnienie maksymalnych półotwartych kostek siatki diadycznej oraz ich rozłączność. Do układu pi prostokątów dodano zbiór pusty. Kalibrację rozciągnięto na wszystkie podzbiory przez borelowskie nadzbiory zachowujące miary zewnętrzne.
- W drzewie Frostmana doprecyzowano przypadek pustego przecięcia K z kostką i pokrycie korzenia, zdefiniowano miarę atomową wyłącznie przez liście dodatniej masy oraz jawnie uzasadniono równość mas kostek i węzłów. Ponownie sprawdzono poprawione kwantyfikatory oszacowania ogona ciągu i Portmanteau.
- Skonstruowano miarę Cantora bez zakładania istnienia miary o zadanych masach cylindrów: miary probabilistyczne na końcach przedziałów, zwartość wąska na C, funkcje charakterystyczne cylindrów otwartych i domkniętych w C jako funkcje ciągłe. Wykazano dodatnią skończoną miarę Hausdorffa w wymiarze krytycznym.
- Dodano twierdzenie o dodatniej mierze H^t zbioru koncentracji miary o skończonej t-energii. Dowód: ograniczenie do dodatniej miary zbioru, na którym potencjał jest ograniczony, i zasada rozkładu masy. Z twierdzeniem Frostmana daje to energetyczną charakteryzację wymiaru niepustego zwartego zbioru; uwzględniono wymiar zero.

## Regresje
Commit 871484a168a1e708e0730de7eb33066d5c3a9a59: dodano dwie metody, razem sześć. Niezależnie rzeczywiście wykonano w JavaScript enumerację 32768 podrodzin 15-węzłowego drzewa i porównano minimum kosztu pokrycia z rekurencją dla wszystkich 256 konfiguracji liści (wymierny model pojemności, nie konkretne potęgi średnic). Ponadto 1012 kontroli dokładnych mas cylindrów Cantora na poziomach do 8, z całkowitymi licznikami współrzędnych trójkowych. Wszystkie zaliczone. Nie zastępują dowodów ogólnych ani uruchomienia testów Python.
Kontrola statyczna: 34 unikalne etykiety, środowiska poprawnie zagnieżdżone, trzy zewnętrzne odsyłacze (22,28,29). Status najnowszego commitu w chwili sprawdzenia pusty; nie oglądano najnowszego PDF.

## Werdykt
25/31 ustabilizowanych. Rozdział 26 nadal w stabilizacji. Następny audyt XCIV: niezależny przegląd nowego argumentu energetycznego i kalibracji, potwierdzenie 6+4 testów i rzeczywiste oględziny wszystkich stron aktualnego rozdziału, w tym rysunku Cantora. Nie przechodzić do 27 przed zamknięciem.
