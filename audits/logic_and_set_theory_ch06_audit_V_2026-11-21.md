# Audyt V — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Podstawa:** kanoniczny rozdział 06 po audycie IV na gałęzi `biblioteka-matematyczna-iteracja-6`, blob Git `c7b7b2f0bea2eb802dea2494fd77440bed2f2a3a`.  
**Zakres:** piąte samodzielne przejście istniejących definicji, twierdzeń, wniosku, dowodów, przykładów, diagramów i odsyłaczy. Bez nowych wyników matematycznych i bez rozbudowy rozdziału.

## Wykryte i poprawione nieścisłości

1. **Przykład łańcucha czterech podzbiorów** (sekcja „Łańcuchy, antyłańcuchy i diagramy Hassego”). Wyrażenie `∅⊊{1}⊊{1,2}⊊{1,2,3}` było nazwane „rodziną”, chociaż jest zapisem ciągu porównań, nie samą rodziną zbiorów. Obecnie wprowadzono `\mathcal C=\{\varnothing,\{1\},\{1,2\},\{1,2,3\}\}`, a odrębnie podano ciąg ostrych zawierań dowodzący, że `\mathcal C` jest łańcuchem. Nie zmieniono przykładu ani jego znaczenia. Po pierwszej korekcie wykryto ostrzeżenie `Overfull \hbox`, które usunięto przez lepsze rozdzielenie dwóch zapisów matematycznych; obie ostateczne kompilacje mają zero przepełnionych wierszy.
2. **Samodzielność punktu (ii) twierdzenia o przejściu między porządkami ostrym i nieostrym** (`thm:order-strict-correspondence`). Dopisano jawnie, że ostry porządek częściowy `\prec` jest relacją *na zbiorze* `P`, wprowadzonym w pierwszym zdaniu twierdzenia. Definicja relacji `\preceq`, teza i dowód nie zmieniły się.

Są to jedyne dwie zmiany w źródle rozdziału względem audytu IV. Nie dodano ani nie usunięto żadnego środowiska i nie zmieniono żadnej etykiety.

## Kontrola matematyczna

Ponownie przejrzano wszystkie **15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów i 7 uwag**. Zweryfikowano zwłaszcza: przejście między porządkiem ostrym i nieostrym; minimalność i najmniejszość; rekonstrukcję porządku z diagramu Hassego; kresy i zupełność krat z uwzględnieniem pustej rodziny; prawa działań w kracie; porządek współrzędny i leksykograficzny; gęstość; dobre porządki oraz indukcję; brak niejawnego użycia aksjomatu wyboru przy wyborze minimum z ustalonego dobrego porządku; porządek na ilorazie preporządku. Nie wykryto fałszywej tezy ani wadliwego kroku w dowodach.

Ponownie uruchomiono dwa niezależne zestawy testów semantycznych: `independent_check.py` — **30 665/30 665**, `extra_check.py` — **215 552/215 552**. Łącznie **246 217/246 217** testów zaliczonych. Testy obejmują m.in. wszystkie oznaczone porządki częściowe i preporządki na małych zbiorach, porządkowanie iloczynów, odtwarzanie porządków z relacji pokrywania, właściwości kresów i ilorazów; obejmują puste zbiory. Skończone kontrole nie zastępują dowodów dla ogólnych zbiorów.

## LaTeX, odsyłacze, wygląd

- Pełny skrypt (44 rozdziały): `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0, 376 stron, 1075 etykiet i 869 odsyłaczy; 0 brakujących odsyłaczy, 0 powielonych etykiet, 0 przepełnionych wierszy `Overfull \hbox`**.
- Częściowa książka z rozdziałami 01–06: `latexmk` — **kod 0, 62 strony, 0 `Overfull \hbox`**. Odsyłacze do rozdziałów 07, 09, 10 i 25 nadal nie są rozwiązane wyłącznie w częściowym imporcie; wszystkie cele występują w pełnym skrypcie. Nie modyfikowano oznaczeń odsyłaczy.
- Zachowano **42/42** etykiety rozdziału oraz wszystkie środowiska. Rozdział 06 obejmuje **12 stron** pełnego składu (strony PDF 61–72); ponownie wyrenderowano i obejrzano każdą stronę, w tym diagramy Hassego i kratę `M_3`, bez wykrytych problemów składu.

## Status

**Audyt V zakończony.** Dwie nieścisłości formalne poprawiono i zweryfikowano, bez zmiany treści twierdzeń, dowodów i zakresu materiału. Ze względu na ingerencję w plik źródłowy **rozdział 06 pozostaje otwarty do audytu VI**. Publikacja na dotychczasowej gałęzi powinna zachować równoległe zmiany w pozostałych plikach i być po niej zweryfikowana przez GitHub Actions.
