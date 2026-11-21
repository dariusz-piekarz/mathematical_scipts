# Algebra liniowa — rozdział 01, audyt 8

Data: 2026-11-21  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Rozdział: `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`  
Commit rozdziału: `e560905a9679daed1d6d4da90f0dd11732193e3f`

## Zakres audytu

W ósmej iteracji ponownie przejrzano cały rozdział 01, szczególnie twierdzenia i dowody z poprzednich audytów:
- operacje na podprzestrzeniach, rodziny skierowane, skończone unie nad ciałami nieskończonymi;
- kryteria niezależności rodzin indeksowanych, reprezentacje o skończonym nośniku i przypadek rodziny pustej;
- lemat o wymianie Steinitza, kryteria bycia bazą i wymiar podprzestrzeni;
- twierdzenia o bazach Hamela, lemat Zorna (także dla pustego łańcucha), wybór bazy ze zbioru generatorów;
- izomorfizm współrzędnych \(V\cong K^{(I)}\), łącznie z \(I=\varnothing\);
- różnicę między bazą algebraiczną a szeregiem oraz przykład przestrzeni ciągów rekurencyjnych.

Zwrócono uwagę na jawność wszystkich założeń, logiczną kolejność wprowadzania definicji, przypadki zerowe, kwantyfikatory i uzasadnienia w dowodach.

## Znalezione braki i dokonane poprawki

### 1. Brak twierdzenia o równoważnych kryteriach skończonej wymiarowości

Istniały już definicja przestrzeni skończenie wymiarowej i lemat o usuwaniu zbędnych generatorów, ale brakowało samodzielnego, kompletnego sformułowania równoważności trzech kryteriów. Dodano **`thm:lin-skonczona-wymiarowosc`**:

Dla dowolnej przestrzeni wektorowej \(V\) nad ciałem \(K\) następujące warunki są równoważne:
1. \(V\) posiada skończoną bazę;
2. \(V\) jest rozpięta przez skończoną rodzinę wektorów;
3. istnieje \(n\in\mathbb N_0\) takie, że każda liniowo niezależna rodzina wektorów w \(V\) ma co najwyżej \(n\) elementów.

Dowód wszystkich kierunków jest samodzielny. Implikacja (ii)\(\Rightarrow\)(iii) wykorzystuje lemat Steinitza, również do wykluczenia \emph{nieskończonej} niezależnej rodziny, z której można wybrać \(n+1\) różnych indeksów. Implikacja (iii)\(\Rightarrow\)(ii) jest konstrukcyjna: zaczyna się od rodziny pustej, dołącza wektory spoza rozpiętej podprzestrzeni i dowodzi zakończenia procedury najpóźniej po \(n\) dołączeniach. Dla \(n=0\) otrzymujemy \(V=\{0\}\).

### 2. Doprecyzowanie przypadku \(n=0\) w dowodzie wymiaru podprzestrzeni

W dowodzie **`thm:lin-wymiar-podprzestrzeni`** argument po rozpatrzeniu \(W=\{0\}\) rozpoczynał wybór \(w_1\neq0\), nie wyjaśniając jawnie, że w pozostałym przypadku \(n=\dim V\) musi być dodatni. Dopisano: przy \(n=0\) pusta baza rozpięłaby wyłącznie przestrzeń zerową, więc nie może istnieć niezerowa podprzestrzeń \(W\). Odtąd \(n\geq1\), a konstrukcja \(w_1\) jest poprawna.

### 3. Dodatkowe wyjaśnienie na przykładzie rekurencji

W przykładzie podprzestrzeni ciągów Fibonacciego uzupełniono podsumowanie: przestrzeń wszystkich ciągów może zawierać właściwą podprzestrzeń dwuwymiarową, mimo że sama jest nieskończenie wymiarowa. Oddzielono wymiar przestrzeni od liczby wyrazów składających się na pojedynczy ciąg.

## Kontrole jakości

- Statycznie w poprawionym rozdziale: **69 unikalnych etykiet `\\label`**, bez powtórzeń.
- Wszystkie lokalne cele `\\ref` i `\\eqref` odnalezione.
- Brak niedomkniętych lub niezgodnych środowisk `\\begin` / `\\end`.
- Zachowano oba rysunki TikZ, bez wprowadzania zewnętrznych plików graficznych.
- Poprzednie CI, audyt 7: [44892390182](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44892390182) — zaliczone.
- CI bieżącej wersji: [44892908046](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44892908046) — wynik do aktualizacji po zakończeniu.

## Zakres odpowiedzialności

W globalnej walidacji Biblioteki nadal raportowane były wcześniejsze błędy związane z importami oraz niezgodnością kopii źródłowych w innych skryptach. Nie włączamy ich do sukcesu ani do zakresu napraw audytu rozdziału 01. Audyt nie obejmował innego rozdziału algebry liniowej.

## Status

**Audyt 8 ujawnił i naprawił luki; rozdział 01 pozostaje otwarty.** Następna iteracja to audyt 9 tego samego rozdziału, do czasu uzyskania audytu bez istotnych nowych usterek i braków. Rozdziału 02 nadal nie tworzymy.
