# Audyt VI — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/06-relacje-porzadku-od-porownywania-do-kresow.tex`, blob Git `8c42c1c7e94dc267fed34b7d911254226fca9026` (po audycie V).  
**Cel:** szósta, niezależna kontrola istniejącego rozdziału — bez nowych twierdzeń, definicji i przykładów.

## Wynik audytu matematycznego

**Nie stwierdzono nowego błędu matematycznego ani nieścisłości wymagającej zmiany źródła.** Treść kanonicznego rozdziału pozostawiono bez zmian. Sprawdzono wszystkie 15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów i 7 uwag; zwracano uwagę na jawność założeń, kwantyfikatorów, zakresu porządkowania, przechodniość relacji i przypadki puste.

Szczególnie ponownie zweryfikowano:

1. Korespondencję ostrego i nieostrego porządku oraz odrębność porządku częściowego i liniowego.
2. Różnicę między minimalnością i najmniejszością, w tym dowody dla niepustych skończonych podzbiorów i kontrprzykład nieskończony.
3. Odczytywanie relacji z diagramu Hassego **wyłącznie** w przypadku skończonym oraz kontrprzykład oparty na gęsto uporządkowanych liczbach wymiernych.
4. Definicje `\sup` i `\inf` względem porządku otaczającego, kraty i kraty zupełne, w tym pusta rodzina, `\mathcal P(X)`, `M_3` i `\N`.
5. Porządek współrzędny oraz leksykograficzny, w tym dowód dobrego uporządkowania iloczynu z pustymi czynnikami.
6. Gęstość porządku, gęstość podzbioru, konstrukcję liczby wymiernej w zadanym przedziale.
7. Indukcję w dobrym porządku, jawny opis funkcji wybierającej minimum w ustalonym dobrym porządku (bez niejawnego aksjomatu wyboru), porządek na ilorazie preporządku.

## Niezależne kontrole skończonych modeli

W bieżącej iteracji przeprowadzono nowy niezależny przegląd enumeracyjny relacji na zbiorach mających od 0 do 4 elementów:

- **390 preporządków** i **243 porządki częściowe** rozpoznane i sprawdzone;
- **3428** niepustych podzbiorów tych porządków: istnienie elementów minimalnych i maksymalnych, równoważność jedyności minimum/minimalności w skończonym przypadku;
- **2748** uporządkowanych par różnych elementów: zgodność porządku ostrego z osiągalnością po krawędziach pokrywania;
- **5958** par w analizie ilorazów preporządków, z dodatkową kontrolą niezależności od reprezentantów;
- **65 814** rodzin podzbiorów dla zbiorów podstawowych mających co najwyżej cztery elementy: poprawność sumy i przecięcia jako kresów (w tym rodzin pustych);
- **25** iloczynów skończonych porządków liniowych, z kontrolą najmniejszego elementu każdego niepustego podzbioru.

Wynik wszystkich kontroli: **0 wykrytych kontrprzykładów**. Kontrole skończonych modeli **nie zastępują dowodów** dla zbiorów dowolnej mocy.

## Źródło, etykiety i odsyłacze

- Struktura środowisk `\begin` / `\end` w rozdziale 06 jest poprawnie zagnieżdżona.
- Rozdział 06 zachowuje **42 etykiety** i niezmienioną liczbę środowisk.
- Rozdziały 01–06 mają łącznie **209 unikatowych etykiet**, bez duplikatów, i **80 odwołań** do etykiet.
- Cztery nierozwiązane odsyłacze w obecnie częściowo zaimportowanej książce wskazują rozdziały nieobecne jeszcze w `books/pl/logic_and_set_theory.tex`: `ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`. Nie są błędnymi etykietami rozdziału 06. Przyszłe importy muszą je rozwiązać; nie usuwamy poprawnych odsyłaczy.
- Poprzedni audyt V dokumentował kompilację 62-stronicowej książki 01–06 i przegląd diagramów, ale jego wyniku nie przedstawiamy jako nowo wykonanej kompilacji w audycie VI.

## Walidacja techniczna i zamknięcie

Do repozytorium dodano dedykowany workflow `.github/workflows/logic-and-set-theory-chapter.yml`. Weryfikuje on z poziomu CLI: kolejność importów, strukturę środowisk, inwentarz środowisk, unikatowość etykiet, odsyłacze, kompilację `latexmk` i log składu (bez nieudokumentowanych brakujących celów, cytowań oraz `Overfull \\hbox`). Wynik GitHub Actions należy odczytać **po wypchnięciu** raportu; samo dodanie workflow nie jest dowodem, że kompilacja przeszła.

**Wniosek merytoryczny:** szósta iteracja jest czysta. Rozdział 06 można uznać za stabilny merytorycznie, bez kolejnych zmian źródłowych. **Domknięcie techniczne:** po potwierdzonym zielonym przebiegu dedykowanego CI. Następny rozdział do audytu: 07, bez poszerzania istniejącego materiału.
