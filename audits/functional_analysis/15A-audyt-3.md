# Analiza funkcjonalna — moduł 15A — audyt 03 (wykryta niejawna hipoteza skalarów)

**Data:** 24 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (istniejąca, bez nowej gałęzi).  
**Źródło:** `chapters/pl/functional_analysis/15A-calkowanie-funkcji-w-przestrzeniach-lokalnie-wypuklych.tex`.  
**Źródło przed poprawką:** blob `f42bf05883d30c43cc6037ed3e78476a5bf6318f`.  
**Źródło po poprawce:** blob `afe39ee7e7d189d2d15bbf4a81457cc57c63be7a`.  
**Test przed poprawką:** blob `d9dc2437a13b441fbcaf16e3a252809529551ca0`.  
**Test po poprawce:** blob `6f44e390ea07e2e5593c8a0a246fd4060355f727`.  
**Decyzja:** audyt z rzeczywistą poprawką matematyczną, **0/2 czystych audytów** (reset licznika).

## Usterka matematyczna i naprawa

W przykładzie `ex:strong-not-norm-cont15a` zapisano `H=L^2(\R,\lambda_1)` bez określenia ciała skalarów, chociaż cały moduł dopuszcza `\K=\R` albo `\K=\C`, zaś przepis `(U_t f)(x)=e^{itx}f(x)` wymaga funkcji **zespolonych**. Dla rzeczywistego `L^2` mnożnik `e^{itx}` w ogólności nie zachowuje przestrzeni, więc `U_t` nie jest zdefiniowanym operatorem `H\to H`. Ta nieokreśloność jest istotną brakującą hipotezą przykładu, nie fakultatywnym rozszerzeniem materiału.

W źródle wprowadzono jawną zmianę: **„W zespolonej przestrzeni Hilberta `H=L^2(\R,\lambda_1;\C)`”**. Treści innych twierdzeń, przykładów i etykiet nie zmieniono. Commit [a214a045e1a5](https://github.com/dariusz-piekarz/mathematical_scipts/commit/a214a045e1a5c1705fe9fe65f088b14ece4f258a).

Dodatkowo rozszerzono `tools/tests/test_functional_analysis_ch15a.py` o drugą regresję `test_complex_modulation_not_norm_continuous`: dla reprezentatywnych rzeczywistych `t\ne0` sprawdza numerycznie `|e^{it(\pi/t)}-1|=2`. Matematyczne uzasadnienie wykracza poza same próbki: z ciągłości mnożnika istnieje dla każdego `t\ne0` otoczenie punktu `\pi/t` o dodatniej mierze, gdzie jego moduł jest dowolnie bliski `2`. Z nierówności `|e^{itx}-1|\le2` wynika więc `\|U_t-I\|=2` dokładnie; dominowana zbieżność `|e^{itx}-1|^2|f(x)|^2\to0` dowodzi zarazem silnej ciągłości. Nowa regresja jest skończenie wymiarowym świadkiem, nie formalnym dowodem supremum istotnego. Commit [2b8f08724bd1](https://github.com/dariusz-piekarz/mathematical_scipts/commit/2b8f08724bd1a78ab05110398360317ed2323aca).

## Niezależny przegląd pozostałych twierdzeń i dowodów

1. **Istnienie całki Riemanna:** oszacowanie przez moduł ciągłości każdej seminormy i wspólne rozdrobnienie zapewnia warunek Cauchy'ego dla wybranego ciągu sum dyadycznych; zupełność ciągowa wystarcza, bo później ten sam moduł kontroluje *wszystkie* drobne podziały. Nie zastępuje się sieci Cauchy'ego nieuzasadnionym ciągiem.
2. **Liniowość, addytywność, seminormy:** przejście do granicy w sumach uzasadnia liniowość; addytywność na podprzedziałach korzysta z jawnie przyjętej całkowalności obu ograniczeń. Poprawka z 15A/01 pozostaje obecna; bez niej twierdzenie byłoby fałszywe.
3. **Operatory liniowe i barycentrum:** ciągłość `T` przenosi granicę sum do przestrzeni docelowej bez wymagania jej zupełności; kombinacje wypukłe znormalizowanych sum i domknięcie otoczki dają barycentrum.
4. **Uzupełnienie:** `j:E\to\widehat E` jest zanurzeniem topologicznym; całkowalność w E jest równoważna przynależności całki w uzupełnieniu do obrazu j(E).
5. **Całka niewłaściwa:** ogony całek skalarnych seminorm kontrolują najpierw ciąg `\int_a^{a+n} f`, a następnie rzeczywisty parametr końca całkowania; zupełność ciągowa jest zastosowana dokładnie do ciągu.
6. **Newton–Leibniz:** orientacja h<0 jest uwzględniona; funkcjonały liniowe rozdzielają punkty, a ciągła pochodna krzywej jest całkowalna w E.
7. **Różniczkowanie po parametrze:** po Hahn–Banachu oszacowanie w seminormie otrzymuje się z oszacowań skalarnych; ciągłość pochodnej na zwartym prostokącie zapewnia jednostajność względem zmiennej całkowania. Nie wykorzystuje się fałszywego wektorowego twierdzenia o wartości średniej.
8. **Fubini dla funkcji ciągłych:** porównanie obu całek iterowanych z identyczną podwójną sumą Riemanna ma błąd kontrolowany przez jednostajny moduł ciągłości na prostokącie.
9. **Silna całka operatorów:** punktowe ograniczenie `\{T(t)x\}` na zwartym przedziale i Banach–Steinhaus dają wspólne ograniczenie norm operatorów. Otrzymana całka jest operatorem ograniczonym bez wymagania ciągłości rodziny w normie operatorowej.
10. **Kontrola kompletności twierdzeń:** w założeniach stosowanych do sum Riemanna, całki niewłaściwej, różniczkowania parametrycznego i iterowanego, zupełność ciągowa została zastosowana tylko tam, gdzie potrzebna; nie usunięto żadnego istotnego założenia w toku przeglądu.

**W pozostałych dziesięciu dowodach nie stwierdzono nowej luki wymagającej zmiany źródła.** Jest to audyt ręczny, nie formalizacja Lean.

## Przykłady i kontrola redakcyjna

- **`c_{00}` z normą `\ell^2`:** dodatnia każda współrzędna całki w uzupełnieniu i zerowanie po odbiciu z przeciwnym znakiem poprawnie pokazują brak automatycznej addytywności bez istnienia całek na podprzedziałach.
- **`C^\infty(\Omega)`:** ciągłość różniczkowania i ewaluacji pozwala przenieść je przez całkę dzięki zasadzie przemienności z operatorem ciągłym.
- **`\mathcal S(\R^d)`:** kontrola każdej seminormy Schwartzowskiej i `q_{m,k}(\partial^\alpha u)\le q_{m,k+|\alpha|}(u)` jest poprawna.
- **Rodzina `U_t`:** jednoznacznie określono zespolone `L^2`; udowodniono silną ciągłość i odstęp normowy równy 2. Bez tej poprawki przykład nie miał pełnych założeń.

Odczytano 443 wiersze oryginalnego źródła: 7 środowisk `twierdzenie`, 2 `stwierdzenie`, 1 `wniosek`, 1 `definicja`, 4 `przyklad`, 2 `uwaga`, 10 `proof`, 16 etykiet i 8 odsyłaczy/hyperref. Środowiska były sparowane, nie ma rysunków TikZ ani stwierdzonych naruszeń uzgodnionej terminologii. Etykiety pozostają bez zmian. Poprzedni przebieg [#45289572406](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45289572406) potwierdził zielone CI dla *starej* wersji i nie zastępuje sprawdzenia nowej.

## PDF i bramka CI nowej wersji

Przejrzano stronę 90–95 faktycznego, **109-stronicowego** PDF z poprzedniego zielonego workflow i niezależnie odczytano log: 0 niezdefiniowanych odsyłaczy, 0 `Overfull \hbox` i 0 `Missing character`. Jedno `Underfull \hbox` dotyczy rozdziału 16. **Ten PDF nie zawiera jeszcze poprawionego zapisu zespolonego `L^2`**; konieczna jest nowa kompilacja źródła z nowymi testami.

Po zmianach źródła i testów uruchomiono dedykowane workflow [#45290644408](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45290644408) oraz [#45290645512](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45290645512). Przy opracowywaniu tego raportu status końcowy **nie był jeszcze potwierdzony**; wyniku nie wolno deklarować jako PASS z wyprzedzeniem.

**Werdykt 15A/03: POPRAWKA KONIECZNA; 0/2 czystych audytów na nowym źródle.** Następna jednostka pracy to ponowny niezależny audyt 15A/04 (potencjalnie pierwszy czysty) po potwierdzeniu działania testów, kompilacji LaTeX, jakości nowego PDF i kompletności odsyłaczy. **Nie rozpoczynać 15B przed stabilizacją 15A.**

## Potwierdzenie zakończonej bramki po poprawce i kontrola PDF

Dedykowany przebieg [#45290645512](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45290645512), uruchomiony na commicie `2b8f08724bd1a78ab05110398360317ed2323aca`, zawierającym **zarówno poprawione źródło 15A, jak i nowy test**, zakończył się **completed/success**. Weryfikacja wszystkich dziewięciu kroków rzeczywistego joba: regresje **PASS**, przygotowanie kompletnego kontekstu 01–17 (z 15A i 15B) **PASS**, kompilacja LaTeX **PASS**, analiza PDF i odsyłaczy **PASS**, publikacja artefaktu **PASS**.

Pobrano i sprawdzono dokładnie ten artefakt `functional-analysis-ch15a-pdf` (ID `14873897034`). Zawiera **109 stron A4**. Tekst wyodrębniony z PDF potwierdza poprawione założenie „W zespolonej przestrzeni Hilberta ...”; osobno wyrenderowano stronę **95** i sprawdzono wizualnie, że prawidłowa notacja `L^2(\R,\lambda_1;\C)` jest czytelna, bez ucięć i nałożeń. Bezpośredni odczyt logu: **0** `Undefined control sequence`, **0** niezdefiniowanych odsyłaczy, **0** `Overfull \\hbox`, **0** brakujących glifów i ostrzeżeń `LaTeX Warning`; pozostaje **1** `Underfull \\hbox` w rozdziale 16, bez wpływu na 15A.

Ponownie odczytane bloby bieżącej gałęzi: źródło `afe39ee7e7d189d2d15bbf4a81457cc57c63be7a`, regresja `6f44e390ea07e2e5593c8a0a246fd4060355f727`. **Bramka po poprawce PASS, lecz audyt 15A/03 pozostaje poprawkowy (0/2).** Potrzebne są dwa niezależne czyste audyty nowej wersji, począwszy od **15A/04**. Nie należy interpretować zielonego CI jako substytutu tych audytów.
