# AA-59 — audyt V: kontrola poprawionej wersji i wag wielokrotnych

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Sprawdzony blob 80070ac0fa8356846c254e0bc9e5b3478c1f5fe1, commit źródłowy 6f47ab4095e78dba45fe4d692ad50edb4f068119.

## Dowody
Ponownie sprawdzono wszystkie definicje i twierdzenia. W lemacie o derywacji wykładnik p+q-1 jest wystarczający, również gdy suma wartości własnych nie występuje w widmie; jądra potęg są rosnące. W rozkładzie Jordana sprawdzono nilpotentność N na skończonej sumie przestrzeni uogólnionych, derywacyjność S i N, obie inkluzje przestrzeni W i V oraz komutowanie z ad_y. Przypadek g=0 jest objęty pustym rozkładem i zerowym centrum. W lemacie wagowym sprawdzono zachowanie przestrzeni własnych przez komutujące operatory i kryterium wielomianu minimalnego ograniczenia; dla t=0 jedyną możliwą wagą jest zero, a zbiór wag może być pusty gdy g=0. Nie wymaga się, aby różne wagi miały różne wartości na jednym ustalonym elemencie.

W dowodzie maksymalnej toralnej podalgebry sprawdzono centralizator jako podalgebrę, niezdegenerowanie ograniczenia formy całej g, rozszerzenie h+Ks, nilpotentność ograniczenia ad_n do centralizatora i obie inkluzje centralizatora. Wybór x jest dowolny, więc Engel stosuje się do całej c. Wspólna postać trójkątna dotyczy reprezentacji c na g, nie tylko reprezentacji dołączonej c na sobie. W dowodzie normalizatora wybór t zależy od niezerowej wagi i nie jest potrzebna regularność t. Sprawdzono argument anihilatora korzeni, oba jądra parowania, znak kappa(x,[y,t]), niezerowość t_alpha, ślad komutatora na każdej niezerowej przestrzeni własnej i normalizację trójki. W sl3 współczynniki 6, 1/3 oraz znak h_alpha są poprawne; oznaczenia rysunku odpowiadają kątom między korzeniami. Nie użyto własności wymagających późniejszej teorii reprezentacji sl2. Nie znaleziono usterek wymagających zmiany treści.

## Niezależna regresja jednorazowa
Dokładne obliczenia całkowite w JavaScript: 3276 modeli sl_n, n=2,...,7, wszystkie uporządkowane wektory współczynników z {-1,0,1} oraz druga przekątna według parzystości indeksu, po usunięciu śladu przez przemnożenie przez n. Sprawdzono 3276 wymiarów wspólnej przestrzeni zerowej (porównanie liczby jednostek macierzowych o wadze zero z sumą kwadratów rozmiarów bloków minus 1), 119736 zgodności krotności wag przeciwnych, 4623840 uporządkowanych par jednostek pozadiagonalnych dla wzoru na nawias i jego wagę, 119736 niezerowych par śladowych i zgodność ich wag przeciwnych. PASS. Uwzględniono powtarzające się wspólne wartości własne i niezerowe przestrzenie zerowe poza samą przekątną, więc nie zakładano maksymalności toralnej. Obliczenia nie zastępują dowodu; trwałe zestawy testów z audytu III pozostają bez zmian.

## CI
Run 45376432928: 128/128 kroków success, w tym oba zestawy regresji AA-59, globalna bramka integralności, latexmk i kontrola odsyłaczy. Dotyczy poprzedniego źródła. Run 45377157158 dla aktualnego źródła w toku podczas kontroli (50 success, 1 in_progress, 76 pending). PDF aktualnego źródła nie został obejrzany.

## Werdykt
Pierwszy czysty audyt matematyczny po korektach IV: 1/2. AA-59 W AUDYCIE. Zakres bez zmian, AA-60 nieotwarty.
