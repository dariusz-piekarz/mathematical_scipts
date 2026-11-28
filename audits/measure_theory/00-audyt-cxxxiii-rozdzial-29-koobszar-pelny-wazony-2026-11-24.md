# Audyt CXXXIII (133) — pełny i ważony koobszar BV
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia a8917bded6fc0c0615b373dfe49119f345f0a538, blob 86f8d53b7090e2e2a2dfc03d6486575d2e2cd4fc. Commit źródłowy 21c29ffb7927841ff323d15a3c3a6ddff522b47c, blob 82b716648e655261fa7d39ed403e42474860df94.
## Wyniki
Dwanaście zastąpień; 3376 -> 3528 wierszy; wszystkie 37 etykiet zachowane w kolejności.
- Gładkie zbiory nadpoziomicowe: jawne hipotezy, zbieżność odcięć także na poziomicy dzięki theta(0)=0, lokalizacja koobszaru na przeliczalnym pokryciu kulami, mierzalność i całkowalność funkcji powierzchniowych, oszacowanie jednostronnych średnich w punktach Lebesgue'a, wspólny zbiór dobrych poziomów dla wszystkich testów. Wyprowadzono wektorową pochodną oraz dokładną równość obwodu i miary regularnej części poziomicy prawie wszędzie bez twierdzenia Sarda.
- Pełny koobszar: jawna sumowalność błędów aproksymacji, reprezentant borelowski, Tonelli. Naprawiono niepoprawną deklarację globalnej zbieżności w L^1 funkcji charakterystycznych, które na nieograniczonym zbiorze mogą nie należeć do L^1: zbieżność norm różnic daje lokalną zbieżność wystarczającą do półciągłości. Wykorzystano wcześniejszy lemat warstwowania, rozpisano monotoniczność obwodów na wyczerpaniu dla każdego poziomu.
- Ważony koobszar: wspólny borelowski zbiór T pełnej miary poziomów lokalnie skończonego obwodu, jawna konwencja miary zerowej na poziomach wyjątkowych. Mierzalność rodziny miar na dowolnych zbiorach borelowskich poprzez układy pi-lambda na wyczerpaniu, bez odejmowania nieskończoności. Przeliczalna addytywność całkowanej miary, jednoznaczność na zbiorach borelowskich, mierzalność całki wewnętrznej i dwa zastosowania zbieżności monotonicznej dla dowolnej nieujemnej wagi.
- Poprawiono przypadki brzegowe t=0 i t=1 w przykładzie funkcji charakterystycznej przedziału.
## Otwarte
Następny audyt: elementy teorii prądów, poprawność definicji, orientacji i znaków oraz podsumowanie zależności. Następnie kontrola terminologiczna, odsyłacze, testy, kompilacja i rzeczywiste oględziny PDF. Stan 28/31, rozdział 29 nadal otwarty. W tej iteracji nie wykonano kompilacji ani regresji.
