# Logika matematyczna i teoria mnogości — rozdział 14, audyt III

**Data:** 21 listopada 2026 r.  
**Rozdział:** „Twierdzenie o zwartości i jego zastosowania”.  
**Źródło:** poprawiona wersja po audycie II (`logika_rozdzial_14_audyt_II.tex`).  
**Zakres:** trzeci, niezależny audyt istniejącego materiału; bez rozszerzania treści i bez nowych twierdzeń, lematów, definicji ani przykładów.

## Konkluzja

**Audyt III czysty.** Nie wykryto nowej luki matematycznej wymagającej poprawki. Źródło `.tex` zachowano bez zmian względem audytu II. Formalne zamknięcie rozdziału wymaga jeszcze CI na integrującym commicie GitHub.

## Niezależna weryfikacja matematyczna

1. **Definicje spełnialności i zwartość (`thm:compactness`).** Definicja skończonej spełnialności obejmuje pusty fragment i dowolne podzbiory skończone. W dowodzie kontrapozycja twierdzenia o istnieniu modelu daje formalny dowód sprzeczności, który używa skończenie wielu zdań; poprawność wyklucza model tego fragmentu. Nie utożsamiono skończoności dowodów z pełnością.
2. **Skończone wsparcie konsekwencji (`thm:compactness-finite-entailment`).** Wykorzystana pełność dotyczy dowolnych formuł, także ze zmiennymi wolnymi. Dopiero potem stosuje się skończoność drzewa i poprawność dla skończonego zbioru przesłanek.
3. **Zdania liczności `\eta_n`, model nieskończony i brak definicji skończoności.** Dla `n=1` jawnie wprowadzono poprawny warunek; dla `n>=2` metanotacja oznacza skończoną koniunkcję. Zbiór `T\cup\{\eta_n\}` jest skończenie spełnialny i wyklucza skończony model. Argument dla pojedynczego zdania `Fin` jest poprawny.
4. **Niestandardowy model arytmetyki.** Dla skończonego fragmentu można wybrać interpretację nowej stałej `c` jako standardową liczbę większą od wszystkich wymienionych numerałów. Potencjalny izomorfizm reduktu ze standardowym modelem zachowywałby interpretacje `0`, `S` i `<`, co prowadzi do `m<m`. Rozróżniono wszystkie standardowe numerały od wszystkich elementów niestandardowego modelu.
5. **Kolorowanie grafu.** Twierdzenie samodzielnie zakłada graf nieskierowany bez pętli oraz `k>=1`. Skończony fragment aksjomatów `T_G` wymienia skończenie wiele wierzchołków; ich kolorowanie dostarcza model fragmentu. W dowolnym modelu całej teorii predykaty wyznaczają dla każdej stałej dokładnie jeden kolor, a aksjomaty krawędzi zapewniają właściwość kolorowania. Interpretacje stałych nie muszą być różne.
6. **Nieaksjomatyzowalność spójności.** Formuły `Walk_m` kodują spacery o określonej liczbie krawędzi, nie ścieżki bez powtórzeń. Każda skończona grupa zaprzeczeń `\rho_n(a,b)` jest spełnialna w odpowiednio długiej skończonej ścieżce; model całego zbioru daje sprzeczność ze spójnością. Wymóg pętli i symetrii jest przenoszony przez hipotetyczną teorię `\Sigma`.
7. **Nieskończoność nie jest skończenie aksjomatyzowalna.** Koniunkcja skończonego zbioru zdań (w tym jawny przypadek zbioru pustego) redukowałaby własność do pojedynczego zdania; zwartość wyklucza taki opis w języku z równością.

## Testy i integralność

- Inwentarz niezmieniony: **7 twierdzeń, 1 wniosek, 5 definicji, 3 przykłady, 5 uwag i 8 dowodów**.
- **20 etykiet**, unikatowych w rozdziale, oraz **7 odsyłaczy**.
- **5/5 niezależnych testów PASS**: formuły spacerów na skończonych grafach, kolorowanie w dowolnych dwulementowych interpretacjach predykatów i stałych, skończone ścieżki w twierdzeniu o spójności, warunki liczności i arytmetyki, integralność źródła.
- **Kompilacja lokalna `latexmk -pdf` PASS**: 123 strony skryptu z rozdziałami 01–14; rozdział 14 to **5 stron**, bez `Overfull \\hbox` i bez uciętych rysunków/wzorów po oględzinach wszystkich stron.
- Lokalny pełny skrypt korzysta z kilku starszych wersji wcześniejszych rozdziałów. W jego logu występują `ch:zf-axioms` oraz `thm:ls-second-order-categorical` — oba **poza rozdziałem 14**. Źródła na GitHubie należy zweryfikować niezależnie i nie zakładać, że druga referencja tam występuje.

## Decyzja

Rozdział 14 jest **stabilny matematycznie po audycie III**. Należy włączyć go do obecnej gałęzi, zaktualizować `\input`, katalog i workflow oraz sprawdzić zielony przebieg CI. Nie dodawać nowych wyników. Po pozytywnym CI można formalnie zamknąć rozdział i przejść do rozdziału 15.