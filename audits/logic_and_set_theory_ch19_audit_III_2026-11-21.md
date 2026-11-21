# Logika matematyczna i teoria mnogości — rozdział 19, audyt III

**Przedmiot:** „Pierwsze twierdzenie Gödla o niezupełności”, w tym wzmocnienie Rossera.  
**Podstawa:** pełna wersja `logika_rozdzial_19_audyt_II.tex`.  
**Werdykt:** **audyt III czysty; nie wprowadzono poprawek do tekstu**. Wymagana kolejna niezależna kontrola stabilizacyjna IV przed formalnym zamknięciem.

## 1. Kontrola matematyczna

Sprawdzono ponownie dokładnie istniejące 2 twierdzenia, 2 lematy, 2 wnioski, 6 dowodów, 3 definicje, 3 przykłady i 6 uwag. Nie dodano żadnego nowego wyniku.

- **Własności predykatu dowodu.** Porównano Lemat 19.5 z konstrukcją `Prf_T` z rozdziału 18 i z lematu o dowodliwości w `Q` prawdziwych zamkniętych formuł `Δ₀` w rozdziale 17. Nie występuje niejawne utożsamienie standardowej prawdziwości z ogólnym twierdzeniem dowodliwym w `Q`.
- **Pierwsze twierdzenie Gödla.** W punkcie (a) niesprzeczność wystarcza do wykluczenia dowodu `G_T`; w punkcie (b) oddzielne negatywne instancje `Prf_T` razem z hipotetycznym dowodem `¬G_T` naruszają dokładnie definicję `ω`-niesprzeczności. Rozdział poprawnie odróżnia te założenia.
- **Relacja Rossera.** Ustalony kod `r` i pierwotnie rekurencyjna funkcja negacji mają poprawne numerały; silna reprezentacja `N` umożliwia usunięcie świadka `z` w obrębie `Q`.
- **Pierwsza gałąź Rossera.** Z rzeczywistego dowodu `R_T` o kodzie `a` i niesprzeczności wynika brak wszystkich dowodów `¬R_T` o kodach `q<a`. Lemat o skończonych odcinkach w `Q` uzasadnia ich zebranie w jedną formułę z ograniczonym kwantyfikatorem. Oddzielnie obsłużono `a=0`.
- **Druga gałąź Rossera.** Z kodu `b` rzeczywistego dowodu `¬R_T` i wcześniej wykluczonego dowodu `R_T` otrzymujemy w `Q` rozbicie `p≤b` albo `b<p`; w drugiej gałęzi `b` jest świadkiem obalającym minimalność. Pozwala to uzyskać jedno uniwersalne zdanie o wszystkich `p` bez indukcji i bez `ω`-niesprzeczności.
- **Wnioski o obliczalności.** Zbadano totalność funkcji rozstrzygającej `D` także poza kodami zdań, poprawność argumentu diagonalnego oraz zastosowanie twierdzenia Rossera do prawdziwej arytmetyki.
- **Modele i niezależność.** Istnienie modeli `T+ρ` i `T+¬ρ` opiera się poprawnie na niesprzeczności obu rozszerzeń oraz na twierdzeniu o pełności pierwszego rzędu.

Nie znaleziono brakującego założenia ani luki wymagającej zmiany istniejącego tekstu. Dokonano niezależnego odczytu przywołanych lematów `res:4:4`, `res:4:7`, `res:7:2`, `res:7:6`, `res:7:7` i `res:8:1`.

## 2. Kontrola techniczna

- Źródło po audycie III jest **bajtowo identyczne** z wersją po audycie II; SHA-256 `ebcb83f4782778a1f4288078ec66f22983627c2cdd9d8e61f34e325aedb98c74`.
- Wszystkie **10 etykiet** pozostaje unikatowych, a wszystkie **22 odsyłacze** rozdziału mają istniejące cele w lokalnym zestawie 01–19.
- Testy z audytu II (13) i nowe testy niezależne (11): **24/24 PASS**. Testy skończonych kodów pełnią funkcję regresyjną i nie zastępują dowodu w `Q`.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`: **PASS**; 0 przepełnionych pudełek `hbox` i `vbox`.
- PDF samego rozdziału: **6 stron**, wszystkie strony wyrenderowane i ocenione wizualnie, brak tekstu nachodzącego na wzory lub marginesy; 0 znaczników `??`.
- W starszych lokalnych kopiach innych rozdziałów występują ostrzeżenia `ch:zf-axioms` oraz `thm:ls-second-order-categorical`; nie dotyczą 22 odsyłaczy rozdziału 19. Ostateczną zgodność z najnowszą gałęzią trzeba sprawdzić w CI.

## 3. Decyzja

Audyt III jest czysty. Uruchomić audyt stabilizacyjny IV na niezmienionym źródle. Po potwierdzeniu stabilności można zintegrować rozdział 19 na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6`, zaktualizować katalog, główny `\\input`, testy i workflow oraz zweryfikować wynik GitHub Actions. Do zakończenia CI nie deklarować formalnego zamknięcia rozdziału.