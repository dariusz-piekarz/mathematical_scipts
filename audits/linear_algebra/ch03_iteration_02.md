# Algebra liniowa — rozdział 03, audyt 2

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex`  
**Commit poprawki rozdziału:** `e62db494e00e90dc07f1e16c54bc9a2fb2d87115`  
**Status:** audyt zakończony z jedną poprawką merytoryczną; rozdział nadal otwarty.

## Zakres

Drugą iterację ograniczono do audytu poprawności **już istniejących wyników** w rozdziale 03. Nie dodano nowych twierdzeń, definicji, przykładów ani dodatkowych tematów. Ponownie sprawdzono dowody, kwantyfikatory, poprawność formalną dziedzin i przeciwdziedzin, przypadki przestrzeni zerowych i wymiarów nieskończonych, zależności od aksjomatu wyboru, terminy matematyczne, odsyłacze i kompilację.

## Znaleziona usterka: poprawne typowanie diagramu pierwszego twierdzenia o izomorfizmie

W rozdziale deklarowano liniowe \(T\colon V\to W\), a w diagramie faktoryzacji strzałka opisana jako \(T\) prowadziła z \(V\) do \(\operatorname{im}T\). Formalnie są to różne odwzorowania z powodu odmiennych przeciwdziedzin. Również podpis
\[
 T=\widetilde T\circ\pi_{\ker T}
\]
bez rozróżnienia tych przeciwdziedzin nie był precyzyjny: prawa strona ma przeciwdziedzinę \(\operatorname{im}T\), a \(T\) pierwotnie ma przeciwdziedzinę \(W\).

**Poprawka:** po dowodzie istniejącego Twierdzenia `thm:lin3-pierwsze-izo` określono odwzorowanie z przeciwdziedziną ograniczoną do obrazu
\[
 \widehat T\colon V\to\operatorname{im}T,\qquad \widehat T(v)=T(v),
\]
oraz kanoniczne włożenie
\(\iota\colon\operatorname{im}T\hookrightarrow W\).
Równości zapisano teraz bez niezgodności typów:
\[
 \widehat T=\widetilde T\circ\pi_{\ker T},
 \qquad T=\iota\circ\widehat T.
\]
Dostosowano odpowiednio etykietę górnej strzałki w diagramie TikZ i jego podpis. Etykieta stabilna `fig:lin3-izo` pozostała niezmieniona. Sama teza pierwszego twierdzenia o izomorfizmie i jej dowód były poprawne i nie wymagały ingerencji.

## Powtórna weryfikacja matematyczna

### Odwzorowania liniowe i wartości na bazie

Sprawdzono kryterium zachowywania dwóch składników kombinacji liniowej, konsekwencje \(T(0_V)=0_W\), \(T(-v)=-T(v)\), skończone sumy oraz przypadek pustej bazy. Przedłużanie zadanej rodziny wartości na bazie Hamela jest dobrze określone, liniowe i jednoznaczne, również przy \(V=\{0_V\}\). Gdy baza jest wskazana, konstrukcja nie korzysta z aksjomatu wyboru.

### Jądro i obraz

Ponownie sprawdzono podprzestrzenność jądra i obrazu, równość \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\), podprzestrzenność przeciwobrazu oraz równoważność iniektywności z jądrem zerowym. Oba przykłady na \(K[X]\) poprawnie opisują jądro i obraz również w dodatniej charakterystyce ciała.

### Twierdzenie o wymiarze jądra i obrazu

Zweryfikowano argument przez rozszerzenie bazy \(C\) jądra do \(B=C\sqcup D\) i wykazanie, że \(T(D)\) jest bazą obrazu. Sprawdzono osobno uzasadnienie liniowego rozpinania i niezależności obrazów bazowych, w tym zero-wymiarowe przypadki. W wersji ogólnej zachodzi równość kardynalna przy AC; w wersji skończenie wymiarowej wystarczają skończone konstrukcje i nie jest używane AC. Nie wykonano nieuzasadnionego odejmowania nieskończonych liczb kardynalnych.

### Pierwsze twierdzenie o izomorfizmie

Dobra określoność mapy \(v+\ker T\mapsto T(v)\), liniowość, iniektywność i surjektywność były poprawne. Usterka dotyczyła jedynie formalnego typowania diagramu, nie samego izomorfizmu \(V/\ker T\cong\operatorname{im}T\).

### Składanie, \(\operatorname{Hom}\), \(\operatorname{End}\)

Sprawdzono liniowość złożenia, zawierania dla jądra i obrazu, liniowość odwrotności bijekcji liniowej, zachowanie baz i skończenie wymiarowe kryterium równoważności iniektywności z surjektywnością. Przykład przesunięć na \(K[X]\) prawidłowo wskazuje brak analogicznej równoważności bez wymiaru skończonego.

Dowód \(\dim_K\operatorname{Hom}_K(V,W)=mn\) obejmuje bazę z \(mn\) map \(E_{ji}\), rozpinanie i niezależność oraz przypadki \(m=0\) i \(n=0\). Działania na \(\operatorname{End}_K(V)\) spełniają założenia algebry łącznej z jedynką, z jawną uwagą o jednopunktowej algebrze endomorfizmów przestrzeni zerowej.

### Projekcje algebraiczne

Sprawdzono, że \(P^2=P\) daje \(V=\operatorname{im}P\oplus\ker P\) i identyczność na obrazie. Założenie identyczności na obrazie jest istotne dla odwrotnego kierunku w twierdzeniu sformułowanym dla dowolnego endomorfizmu; zostało poprawnie zachowane. Wykazano liniowość i jednoznaczność projekcji wyznaczonej przez wskazany rozkład \(V=U\oplus W\).

## Niezależne testy pomocnicze

Wszystkie **81 odwzorowań liniowych \(\mathbb F_3^2\to\mathbb F_3^2\)** zostały wyliczone przez wybór obrazów dwóch wektorów bazy standardowej i sprawdzone pod kątem:
- równości \(\dim\ker T+\dim\operatorname{im}T=2\);
- zgodności liczby warstw \(V/\ker T\) z mocą \(\operatorname{im}T\) i niezależności obrazu od reprezentanta warstwy;
- równoważności \(P^2=P\) z rozkładem \(V=\operatorname{im}P\oplus\ker P\) i \(P|_{\operatorname{im}P}=\operatorname{id}\).

Wynik: **0 rozbieżności**. Spośród 81 endomorfizmów wykryto **14 projekcji**. Te kontrole stanowią weryfikację pomocniczą, nie zastępują dowodów ogólnych w rozdziale.

## Walidacja techniczna

- Rozdziały 01–03: **150 unikalnych etykiet** (69+39+42), bez duplikatów.
- Zweryfikowano **62 odsyłacze** `\\ref` i `\\eqref`, brak nierozwiązanych celów.
- Brak błędnie zagnieżdżonych lub niedomkniętych środowisk `\\begin`/`\\end`.
- Zgodność terminologii z `AGENTS.md` i `docs/pl/standardy_terminologiczne.md`.
- Rysunek nadal pozostaje wewnętrznym diagramem TikZ, bez nowych zależności od obrazów zewnętrznych.
- Wpisy katalogu i kolejność `\\input` pozostają prawidłowe.

**GitHub Actions dla poprawki:** [44903404379](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44903404379), wynik końcowy do potwierdzenia. Poprzednia pełna kompilacja rozdziałów 01–03 była udana. Wcześniejsze zgłoszenia globalnego walidatora innych skryptów są rozpatrywane osobno.

## Decyzja

**Audyt 2 zakończony z poprawką formalno-matematyczną.** Rozdział 03 pozostaje otwarty. Następna iteracja ma ponownie zweryfikować obecną treść bez rozszerzania zakresu. Jeśli nie wystąpią nowe istotne błędy ani luki i CI zakończy się poprawnie, można ocenić stabilność rozdziału.
