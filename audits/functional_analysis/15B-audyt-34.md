# Moduł 15B — audyt 34 (blok 1/12, poprawkowy, 0/2)

Data: 24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: stabilizacja 15A w raporcie 33, a3e9d1d30a941669fe80b714edffb0b9b969fb5c. Źródło wejściowe 5ee3e1bab6a7aa5104b6f7ae290ff8fa389fffcb, 2838 wierszy.

## Zakres iteracji
Pierwsza z 12 podsekcji: mierzalność silna i słaba, twierdzenie Pettisa o mierzalności, konstrukcja całki Bochnera, kryterium całkowalności, zbieżność zmajoryzowana, Fubini, zgodność z całką Riemanna. Nie zaliczamy audytu całego modułu na podstawie jednego bloku.

## Matematyka i redakcja
15 celowanych zamian fragmentów: doprecyzowano kwantyfikatory, rolę zupełności miary przy zmianach na zbiorach zerowych, ośrodkowość domkniętej otoczki liniowej, mierzalne rozłączne zbiory pierwszego wyboru, kontrolę ogonów i argument Borela–Cantellego. Jawnie uzasadniono mierzalność normy, liniowość klasy całkowalnej, oszacowanie funkcji prostych, konieczność całkowalności normy, przemienność z operatorami dla każdego zbioru A, wybór aproksymacji diagonalnej oraz wszystkie kroki twierdzenia o zbieżności zmajoryzowanej. W Fubinim rozpisano całki prostokątne, przejście od skalarnej aproksymacji charakterystyk do funkcji wektorowych, mierzalność przekrojów i zbieżność ich całek poza wspólnym zbiorem wyjątkowym. Zgodność z Riemannem: jawne półotwarte odcinki i wartość na prawym końcu, przybliżenie jednostajne i L1, odwołanie do 15A bez powtarzania dowodu istnienia całki Riemanna.

Stwierdzono brak dowodu zupełności L1(S,mu;X), używanej później w charakteryzacji własności Radona–Nikodyma przez różniczkowalność krzywych. Rozdział 12 dowodzi zupełności skalarnego Lp, nie wektorowego L1. Uzupełniono konieczny argument z podciągiem, sumowalnymi różnicami, Tonellim, zupełnością X, mierzalnością granicy oraz zbieżnością całego ciągu. Nie jest to rozszerzenie uzgodnionego zakresu, lecz uzupełnienie zależności dowodowej.

## Technika
Commity źródła a8b08f0d5ad517f07d72560ff5976809db75e9cc i 6d90e2aae6c3342f59374e049ff7aae9c90ba025, końcowy blob 3e46beb1a16ced194eae2a0a72095e04fa14ab43. 2965 wierszy, 59 etykiet zachowanych, poprawne zagnieżdżenie środowisk. Testy zwiększono z 21 do 23: kontrakty źródłowe oraz dokładne rachunki teleskopowych ogonów w ważonej wektorowej normie L1 na trzech atomach (commit 04574778f4dd5a446e3d404160dadba947386816, blob b04eeef118b7acd3357c0244756abf27e45400e6). Statycznie potwierdzono obecność kontraktów; status nowych przebiegów przy odczycie: [{"id":45363478216,"sha":"04574778f4dd5a446e3d404160dadba947386816","status":"in_progress","conclusion":null}]. Nie deklarować zaliczenia testów i oględzin PDF przed uzyskaniem wyników.

## Decyzja i kolejka
15B: 0/2, pierwszy blok poprawiony. Audyt 35: kontrola CI i blok 2, całki wyznaczane przez wartości skalarne (Dunford i Pettis), od bieżącej podsekcji o tej nazwie. Dalej Gelfand i miary wektorowe; własności i zależność od zbioru; Vitali; relacje całek; Fubini; RNP; różniczkowanie Bochnera i krzywe bezwzględnie ciągłe; różniczkowanie całek słabych; różniczkowanie pod całką; Sobolew. Po kontroli wszystkich 12 bloków i niezbędnych poprawkach dwa pełne czyste audyty modułu. 14, 15, 15A stabilne. Nie dodawać opcjonalnych zagadnień.