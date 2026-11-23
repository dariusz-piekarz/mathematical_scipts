# Algebra abstrakcyjna — audyt przekrojowy AA-X27: noetherowskość a wymiar Krulla (AA-13/AA-39)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **HEAD przed zapisem:** `719a01df197324b8f3a0ec13fbdd59544c8251b8`.

## Weryfikacja stanu i niepowtarzalności

Odczytano pełne drzewo GitHub (nieucięte), listę 50 źródeł `chapters/pl/abstract_algebra`, listę raportów `audits/abstract_algebra` (ostatni numer AA-X26), `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md` i `catalog/books.json`. W źródłach i katalogu istnieją AA-01–AA-50; AA-51 nie istnieje. Ten audyt bada *nowe powiązanie* między AA-13 (warunek łańcuchów wstępujących, twierdzenie Hilberta o bazie) a AA-39 (łańcuchy **ideałów pierwszych** i wymiar Krulla). Nie powtarza audytu AA-X06 (AA-09/12/13/14) ani AA-X07 (AA-37–40).

Źródła: AA-13 blob `548155ff626fd172691bd241c1240015edae197a` (493 wiersze); AA-39 blob `1b8990241d26cbf461a0e7b4a07546a3ef77fa9e` (565 wierszy). Brak zmian źródłowych.

## Kontrola matematyczna

1. **Nie mylić ACC z wymiarem skończonym.** AA-13:26–35 definiuje noetherowskość przez skończone generowanie wszystkich ideałów i równoważny ACC dla *wszystkich* ideałów. AA-39:15–27 definiuje wymiar jako supremum długości *skończonych ściśle rosnących łańcuchów ideałów pierwszych*. ACC nie zapewnia wspólnego skończonego ograniczenia długości wszystkich łańcuchów; rozdziały nie wyprowadzają błędnej implikacji. Wymiar nieskończony AA-39:515–535 jest wykazany dla pierścienia nieskończenie wielu zmiennych, a AA-13:199–213 wykazuje jego nienoetherowskość. Przykład nie rozstrzyga odwrotnej implikacji w ogólności.
2. **Ilorazy i lokalizacje.** AA-13:56–96 dowodzi zachowania noetherowskości przez iloraz i lokalizację, AA-39:78–153 i 154–238 podaje odpowiednio bijekcje ideałów pierwszych, które zachowują i odzwierciedlają ścisłe inkluzje. Wynikające stąd nierówności wymiarów wymagają niezerowości ilorazu/lokalizacji; AA-39:115–120, 205–210 wyraźnie ją zapewnia. W AA-39:132–153 redukcja przez nilradykał zachowuje spektrum i wymiar.
3. **Skończone generowanie nie ogranicza wymiaru do zera ani jednego.** AA-13:258–344 dowodzi noetherowskości K[U,V] na mocy twierdzenia Hilberta. AA-39:268–336 niezależnie wyprowadza wymiar 2, używając faktoryzacji w UFD, usunięcia mianowników i skończonego wymiaru K-algebry ilorazowej przez (f,g). Sprawdzono przypadek f lub g stałego względem jednej zmiennej: w K(U)[V] taki niezerowy element jest jednostką, więc tożsamość Bézouta nadal istnieje; po usunięciu mianowników otrzymuje się niezerowy wielomian w K[U]. Przypadek stałej niezerowej h lub k jest wyodrębniony w AA-39:300–302.
4. **Kontrprzykłady do błędnych utożsamień.** AA-13:98–131 pokazuje, że lokalny pierścień K[x,y]_(x,y) jest noetherowski, lecz jego ideał maksymalny nie jest główny. AA-39:491–513 wykazuje wymiar zero pierścienia K[T]/(T²), który nie jest ciałem. AA-39:439–466 wykazuje różne wysokości ideałów maksymalnych w iloczynie K[T] × K[U,V]. Wszystkie te przykłady są zgodne z rozróżnieniem między skończonym generowaniem, głównością ideałów i wymiarem.
5. **Przypadki brzegowe.** AA-13 dopuszcza pierścień zerowy i pusty układ generatorów, AA-39:10–36 jawnie wyklucza pierścień zerowy z definicji wymiaru; nie ma sprzeczności, ale konwencje nie są identyczne. AA-39:241–266 prawidłowo wyodrębnia ciało (wymiar 0) spośród dziedzin ideałów głównych.

**Wynik tej konkretnej kontroli:** nie znaleziono sprzeczności ani koniecznej korekty w sprawdzonych twierdzeniach, dowodach i przykładach. To nie jest ponowny pełny audyt wszystkich twierdzeń AA-13 i AA-39.

## Niezależny test skończonych modeli

Lokalnie wykonano krótki skrypt Python enumerujący ideały Z/nZ jako podzbiory, sprawdzający pierwszość przez definicję i wszystkie ścisłe zawierania ideałów pierwszych, dla n=6,12,30. Wyniki: odpowiednio 4/6/8 ideałów, 2/2/3 ideały pierwsze, **0** ścisłych zawierań między ideałami pierwszymi, wymiar 0 w każdym przypadku. Trzy modele zgodne z AA-39:468–487; nie stanowią dowodu ogólnego twierdzenia. Lokalny test zakończył się bez błędu (3/3 modeli).

## Kontrola techniczna i ograniczenia

Przeczytano źródła i sprawdzono kontekst istotnych etykiet oraz odsyłaczy (m.in. `aa:tw:hilbert-basis`, `aa:lem:krull-plane-dimension`, `aa:tw:krull-localization-primes`). Zachowano wszystkie istniejące `\\label` i `\\ref`. Nie przeprowadzono pełnej automatycznej kontroli odsyłaczy całej książki, kompilacji LaTeX, wizualnej inspekcji PDF ani nowego CI: lokalny `git ls-remote` nie zadziałał z powodu DNS, a pełne środowisko repozytorium nie było dostępne lokalnie. **Brak deklaracji PASS dla LaTeX, PDF i CI.** Nie modyfikowano zatwierdzonych rozdziałów, więc nie resetowano liczników czystych audytów.

**Propozycja (bez zmiany źródeł):** przy okazji przyszłego rozszerzenia materiału warto dodać osobny, uzasadniony przykład noetherowskiego pierścienia o nieskończonym wymiarze Krulla; unaoczniłby, dlaczego ACC nie ogranicza globalnie długości skończonych łańcuchów. Wymaga zgody przed dodaniem.

**Werdykt:** AA-X27 — ukończony audyt *wybranego powiązania*, bez wykrytej koniecznej poprawki; techniczna weryfikacja całej książki nieodbyta. **Następny krok:** odczytać nowy HEAD, sprawdzić istnienie AA-51; przy jego braku wybrać inne, nieobjęte AA-X01–X27 powiązanie i przeprowadzić dokładnie jeden nowy audyt.
