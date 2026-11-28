# Topologia ogólna — rozdział 06 „Zbieżność topologiczna” — audyt 3

**Data:** 21 listopada 2026 r.  
**Wersja:** 0.3.  
**Status:** audyt z zatwierdzonym uzupełnieniem; **0/2 kolejnych czystych audytów**.  
**SHA-256 źródła:** `fb55259a21f57d7b35dcb48252da4ddb32bb17bbfdd2380ed12c22631435c2d6`.

## Zakres i korekty

Przeprowadzono szczegółowy audyt dotychczasowego rozdziału (definicje, założenia, dowody, przykład topologii koprzeliczalnej, zbieżność sieci/podsieci i filtrów, odsyłacze, skład LaTeX i grafiki). W wyniku zgody użytkownika dodano **jeden przykład** `ex:topog-siec-koprzeliczalna-bez-ciagu`, bez nowych twierdzeń.

W topologii koprzeliczalnej na $X=\mathbb R$ dla $A=(0,\infty)$ skonstruowano skierowany zbiór $D=\{(C,a): C\subseteq A\text{ co najwyżej przeliczalny},\ a\in A\setminus C\}$, uporządkowany przez $C\subseteq E$. Sieć $x_{(C,a)}=a$ zbiega do zera, ale żaden ciąg o wyrazach w $A$ nie zbiega do zera. Dowód jawnie wykazuje: niepustość $D$, zwrotność i przechodniość relacji, skierowanie (dzięki nieprzeliczalności $A$), dokładny zbiór wartości sieci równy $A$, kontrolę każdego otwartego otoczenia i niezbieżność ciągów. Konstrukcja nie wymaga arbitralnego wyboru po jednym elemencie dla każdej rodziny.

Dla czytelności przeniesiono początek nowego przykładu na kolejną stronę. Nie stwierdzono dodatkowego błędu w dotychczasowych definicjach ani dowodach wymagającego zmian.

## Walidacja

- `bash tools/validate_general_topology_ch06.sh` — **PASS** (rozdziały 01–06).
- Testy sieci nad skierowanymi przedporządkami — **41 350 przypadków PASS**.
- Nowy niezależny test skończonych modeli uporządkowania indeksów i unikania zadanych wyjątków — **4448 sprawdzeń PASS**. Jest to regresja skończonych analogów konstrukcji, a nie dowód twierdzenia o zbiorze nieprzeliczalnym.
- Testy filtrów/domknięcia — **21 934 przypadki PASS**.
- Testy ciągłości przez filtry — **24 907 przypadków PASS**.
- LaTeX: unikatowe etykiety, rozwiązywalne odsyłacze, spójna terminologia — **PASS**.
- Kompilacja osobnego rozdziału — **9 stron**, całej książki 01–06 — **55 stron**, bez ostrzeżeń LaTeX.
- Kontrola wizualna wszystkich 9 stron po finalnej kompilacji, ze szczególną uwagą na strony 5 i 6 — **PASS**.

## Propozycje — bez zmian treści

Pozostaje do decyzji na etapie zwartości wcześniej wskazana charakterystyka zwartości przez ultrafiltry i punkty skupienia sieci. Nie dodano jej do bieżącego rozdziału.

## Decyzja

Audyt 3 wymagał zatwierdzonego wcześniej rozszerzenia. Zgodnie z procedurą licznik czystych audytów wynosi **0/2**. Rozdział 06 nie jest stabilny i nie został przesłany na GitHuba. Następny audyt 4 powinien obejmować niezmienioną wersję 0.3.
