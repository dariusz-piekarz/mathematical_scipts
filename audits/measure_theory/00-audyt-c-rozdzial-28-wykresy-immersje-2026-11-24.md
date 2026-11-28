# Audyt C (100) — rozdział 28: wykresy, immersje i hipotezy
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy 1e99579a51ec14ef07f48a3ab2b57cdde6945cf6. Pełny odczyt 1266 wierszy rozdziału 28; główny zakres pierwszej iteracji: sekcje do zastosowania coarea, dodatkowo wykryte usterki w dalszej części.

## Poprawki
- W lemacie o wykresie dowiedziono borelowskości obrazów przez rzut i borelowskość wykresu oraz addytywności miary. Poprawiono rozróżnienie odwzorowania afinicznego i liniowego; jawne oszacowanie dwulipschitzowskie i rachunek Grama przez izometrię i liniową zamianę zmiennych.
- Samodzielne hipotezy twierdzenia o wykresie. Dla immersji C^1 wybrano odwracalny minor, zastosowano twierdzenie o odwzorowaniu odwrotnym, sprecyzowano zmianę parametrów i tożsamość wyznaczników; zbiór A musi leżeć w E, gdzie zdefiniowano f.
- Normalny jakobian: dziedzina otwarta; submersja: włókno klasy C^1, może być puste; funkcja lokalna znika poza V, nie musi mieć tam domkniętego nośnika.
- Lemat Łuzina–Whitneya: pokrycie zwartymi fragmentami tylko prawie wszędzie, nie całe U. W lemacie o zerowych włóknach wybrano dodatnią stałą Lipschitza także dla funkcji stałej i margines dla kostek pokrywających.
- Doprecyzowano dziedziny funkcji w głównym twierdzeniu, w tym k>=1.
- Zachowano wszystkie 28 etykiet w tej samej kolejności; 20 celowanych zamian.

## Otwarte
Kolejna iteracja: dokładny audyt Rademachera, przedłużenia Whitneya, oszacowań krytycznych i mierzalności włókien (w szczególności treści Hausdorffa dla ustalonej średnicy), wersji dla funkcji mierzalnych w sensie Lebesgue'a, dowodu na rozmaitościach i identyfikacji miary Hausdorffa z riemannowską. Sprawdzić normalizację w 26, odsyłacze, testy i kompilację. Brak dedykowanej bramki CI dla 28; nie wykonano kompilacji ani oględzin PDF w tej iteracji. Nie przechodzić do 29. Nie rozszerzano zakresu.
