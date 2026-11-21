# Audyt IV — rozdział 05 „Relacje równoważności i zbiory ilorazowe”

**Data:** 21 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/05-relacje-rownowaznosci-i-zbiory-ilorazowe.tex` na gałęzi `biblioteka-matematyczna-iteracja-6`, po audycie III, blob Git `5725745406d3344a76f9e904c8939c6acd9707cb`.  
**Cel:** czwarta niezależna kontrola istniejącego materiału, bez jego rozszerzania. **Wynik: nie znaleziono kolejnych usterek. Plik `.tex` pozostaje bajtowo niezmieniony.**

## I. Ponowny audyt matematyczny

Sprawdzono wszystkie **11 twierdzeń, 1 wniosek i 12 dowodów**, 6 definicji, 18 przykładów oraz 5 uwag. W szczególności:

1. Definicję równoważności, klasy, ilorazu i podziału, wraz z pustym zbiorem `X` i jednoznacznością pustego podziału; dowody kryterium równości klas i wzajemnej odpowiedniości między relacjami równoważności a podziałami.
2. Drobniejsze i grubsze relacje, przecięcia rodzin równoważności (przy niepustym zbiorze indeksów), równoważność generowaną i kryterium łańcucha dopuszczające ścieżkę długości zero. Zweryfikowano największość przecięcia i minimalność wspólnego rozszerzenia, w tym kontrprzykład dla sumy relacji.
3. Definicję nasycenia, równoważność jego charakterystyk, zamkniętość pod względem sum, przecięć i dopełnień (w tym pustych rodzin), minimalność operatora `Sat_E`, jego monotoniczność, idempotentność oraz kontrprzykład dla przecięć.
4. Kryterium dobrze określonego działania na ilorazie oraz wszystkie przykłady zgodności i niezgodności. Własność uniwersalną `q:X→X/E` sprawdzono w obu kierunkach, z jednoznacznością faktoryzacji i przypadkiem `X=∅`, także przy `Y=∅`. W dowodzie nie jest potrzebny aksjomat wyboru.
5. Równoważność par opisujących ułamki przy niezerowych mianownikach, ich dodawanie i mnożenie oraz niezależność działań od przedstawicieli, również przy ujemnych mianownikach.

Nie stwierdzono błędu w żadnej tezie ani dowodzie. **Nie dodano nowych twierdzeń, lematów, przykładów ani sekcji; nie zmieniono żadnego wzoru lub oznaczenia.**

## II. Niezależne kontrole automatyczne

Ponownie uruchomiono trzy zestawy testów z audytu III na aktualnej, niezmienionej wersji:

- `independent_check.py`: **23 542** poprawne przypadki, obejmujące podziały, klasy, relacje generowane, działania na ilorazach, nasycenie i rachunek ułamków.
- `extra_check.py`: **280** poprawnych przypadków odpowiedniości podziałów i równoważności oraz porównań klas.
- `new_independent_check.py`: **2713** poprawnych przypadków własności uniwersalnej ilorazu, nasyconych dopełnień i przecięć oraz alternatywnych reprezentantów ułamków.

**Razem: 26 535/26 535 przypadków zaliczonych.** Testy skończone nie zastępują analizy dowodów w sytuacji ogólnej, którą wykonano osobno.

Weryfikacja struktury potwierdziła: **11 twierdzeń, 1 wniosek, 12 dowodów, 6 definicji, 18 przykładów, 5 uwag i 29 oryginalnych, niezmienionych etykiet**. SHA bloba Git niezmienione: `5725745406d3344a76f9e904c8939c6acd9707cb`.

## III. Kompilacja, odsyłacze i skład

- Cały skrypt (44 rozdziały): świeża kompilacja `latexmk -g -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`, **kod 0, 376 stron**. W całym skrypcie **1075 unikatowych etykiet, 869 odsyłaczy, 0 zdublowanych etykiet, 0 niezdefiniowanych celów, 0 ostrzeżeń `Overfull \hbox`**. Trzy nieblokujące `Underfull \hbox` nie dotyczą zmienianego rozdziału.
- Częściowa książka repozytorium z rozdziałami 01–05: świeża kompilacja `latexmk -g` zakończona **kodem 0, 50 stron**, bez `Overfull \hbox`. Odsyłacze do rozdziałów 06, 07, 09, 10 i 25 pozostają nierozwiązane tylko w częściowym imporcie, a w pełnym skrypcie istnieją poprawne cele. Nie zmieniano etykiet.
- Z pełnego PDF wyodrębniono dokładnie **9 stron rozdziału 05, tj. strony 52–60 pełnego składu**. Ponownie wyrenderowano i obejrzano wszystkie strony, w tym rysunek klas równoważności i dowody o ilorazach. Nie stwierdzono nakładania się napisów, obciętych elementów ani defektów rysunku TikZ.

## IV. Decyzja

**Audyt IV zakończony bez poprawek. Rozdział 05 uznaje się za stabilny i zamknięty po czterech audytach.** Raport można opublikować bez zmiany źródła rozdziału i bez ingerencji w inne skrypty. Ostatnie GitHub Actions dotyczące zawartości rozdziału (`44911622292`) zakończyło się sukcesem; ewentualny commit zawierający sam raport nie wymaga ponownego przerabiania źródła. Następnym etapem jest audyt I rozdziału 06.
