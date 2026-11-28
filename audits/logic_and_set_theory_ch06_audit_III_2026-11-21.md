# Audyt III — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Źródło:** kanoniczny rozdział 06 po audycie II, plik `chapters/pl/logic_and_set_theory/06-relacje-porzadku-od-porownywania-do-kresow.tex`, blob Git `358d3243c1b345d731613127d1aff44a1977fdcf`.  
**Zakres:** niezależny audyt obecnych 15 twierdzeń, 1 wniosku, 16 dowodów, 12 definicji, 21 przykładów i 7 uwag; bez nowych wyników i bez rozbudowy materiału.

## Poprawione nieścisłości

1. **Samodzielność twierdzenia o diagramie Hassego** (`thm:hasse-paths-xliii`): w samej tezie zdefiniowano `$x\prec y$` jako `$x\preceq y$` przy `$x\ne y$` oraz pokrywanie `$x\lessdot y$` jako brak elementu ściśle pomiędzy `$x$` i `$y$`. Poprzednio oba symbole występowały w tezie bez przypomnienia znaczenia. Drogi, kwantyfikatory i dowód pozostały bez zmian.
2. **Samodzielność twierdzenia o leksykograficznym iloczynie dobrych porządków** (`thm:lex-well-orders-xliii`): sformułowanie „opisany powyżej porządek leksykograficzny” zastąpiono jego dokładnym wzorem, z jawnym wprowadzeniem porządków czynników. Zachowano przypadek pustego czynnika. Nie zmieniono tezy.
3. **Ujednolicenie symbolu w dowodzie twierdzenia leksykograficznego:** w miejscu, gdzie wystarcza relacja nieostra, zapisano `\preceq_{\rm lex}` zamiast nieobjaśnionego w tym miejscu `\prec_{\rm lex}`. Wynik wniosku jest ten sam; jest to doprecyzowanie notacji, nie zmiana argumentu.
4. **Samodzielność twierdzenia o indukcji w dobrym porządku** (`thm:well-order-induction`): wprowadzono jawnie `$v\prec w$` jako `$v\preceq w$` i `$v\ne w$`. Treść zasady najmniejszego kontrprzykładu oraz jej dowód pozostają takie same.

Nie dodano ani nie usunięto żadnego środowiska LaTeX. Wszystkie **42 etykiety** mają niezmienioną treść i kolejność. Nie zmieniono twierdzeń w sensie matematycznym.

## Weryfikacja matematyczna

Ręcznie skontrolowano definicje preporządku, porządku ostrego i liniowego, łańcuchy i pokrywanie, diagramy Hassego, rozróżnienie elementów minimalnych i najmniejszych, istnienie elementów ekstremalnych w skończonych porządkach, kresy górne i dolne, zupełność krat, podstawowe prawa krat, kontrprzykład `$M_3$`, porządki iloczynowe i leksykograficzne, gęstość porządku, indukcję w dobrym porządku oraz iloraz preporządku. Sprawdzono również przypadki pustych zbiorów i ich iloczynów. W istniejących tezach i dowodach nie znaleziono błędów matematycznych.

- `independent_check.py` — **30 665** niezależnych kontroli, wszystkie zaliczone (wszystkie porządki częściowe i preporządki na zbiorach do czterech elementów, kresy, minimalność, kraty, odtwarzanie z diagramów Hassego i ilorazy).
- `extra_check.py` — **215 552** dodatkowe kontrole, wszystkie zaliczone (dowolne porządki częściowe i liniowe na zbiorach do trzech elementów, iloczyny także z pustymi czynnikami, wszystkie podzbiory badanych iloczynów, porządek leksykograficzny i dobre uporządkowanie).
- **Łącznie 246 217 kontroli**. Testy skończone nie zastępują dowodów dla zbiorów dowolnych; dowody weryfikowano osobno.

## Kompilacja, spójność i oględziny

- Pełny skrypt: `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0, 44 rozdziały, 376 stron**; **1075 unikatowych etykiet, 869 odsyłaczy, 0 duplikatów i 0 brakujących celów**, bez `Overfull \hbox`.
- Książka repozytoryjna obejmująca rozdziały 01–06: analogiczna kompilacja `latexmk` — **kod 0, 62 strony**, bez `Overfull \hbox`. W częściowym imporcie pozostają cztery oczekiwane odsyłacze do jeszcze niezaimportowanych rozdziałów 07, 09, 10 i 25; wszystkie mają poprawne cele w pełnym skrypcie.
- Zachowano **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów, 7 uwag i 42 etykiety**.
- Wyrenderowano i obejrzano wszystkie **12 stron rozdziału 06**, w tym diagramy Hassego, `M_3`, nieskończony porządek oraz zmienione fragmenty. Nie stwierdzono obcięć, nachodzenia napisów ani usterek układu.

## Status

**Audyt III zakończony pozytywnie, z czterema lokalnymi doprecyzowaniami.** Rozdział 06 pozostaje otwarty do audytu IV po tej korekcie. Po publikacji na GitHubie należy sprawdzić końcowy wynik GitHub Actions; publikacja nie może naruszyć prac równoległych na wspólnej gałęzi.
