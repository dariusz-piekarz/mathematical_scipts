# Logika matematyczna i teoria mnogości — audyt IV rozdziału 32

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/logic_and_set_theory/32-podstawy-wymuszania-i-modele-generyczne.tex`.  
**Zakres:** weryfikacja matematyczna i językowa definicji, lematów, twierdzeń, przykładów i dowodów, w szczególności rozróżnienia obiektów liczonych wewnątrz modelu $M$ i w zewnętrznym uniwersum ZFC; testy regresyjne, LaTeX, odsyłacze oraz kompilacja całego skryptu.

## Wykryte i naprawione nieścisłości

### I. Absolutność skończonych warunków Cohena

W pierwszych wersjach rozdziału zapisywano $\mathbb P_{\mathrm C}=\operatorname{Fn}(\omega,2)$ „obliczanym w $M$”, a następnie bez objaśnienia używano tych samych skończonych warunków w zewnętrznym uniwersum. Dla przeliczalnego tranzytywnego modelu ZFC jest to poprawne, ale wymaga uzasadnienia.

**Poprawka:** w przykładzie wymuszania Cohena udowodniono
\[
  \operatorname{Fn}(\omega,2)^M=\operatorname{Fn}(\omega,2).
\]
Każda zewnętrzna skończona funkcja o dziedzinie będącej skończonym podzbiorem $\omega$ jest zbudowana ze skończonej liczby obiektów należących do $M$; przez zamknięcie na pary i skończone zbiory należy do $M$. W drugą stronę każda funkcja uznana za skończoną w tranzytywnym $M$ jest skończona zewnętrznie. W ten sposób przejście między zewnętrznym i wewnętrznym zbiorem warunków jest jawne.

### II. Dlaczego filtr Cohena generyczny nad $M$ nie należy do $M$

Dotychczasowa uwaga poprawnie rozróżniała zewnętrzną enumerację gęstych podzbiorów należących do $M$ od enumeracji wewnętrznej, ale brakowało jednoznacznego przykładu wykazującego, że generyczny filtr faktycznie może leżeć poza $M$.

**Poprawka:** w istniejącej uwadze o zewnętrznej perspektywie dopisano konsekwencję twierdzenia o nowym ciągu Cohena: gdyby $G\in M$, to $\bigcup G\in M$ z aksjomatu sumy; natomiast z dowodu generyczności i gęstych zbiorów $E_x$ wynika $c_G=\bigcup G\notin M$. Jest to sprzeczność. Nie sformułowano osobnego twierdzenia, aby nie rozbudowywać niepotrzebnie inwentarza.

### III. Samodzielność przykładu nazwy $\dot C$

Przykład „Nazwa generycznego podzbioru $\omega$” rozpoczynał się nieprecyzyjnym „Niech $M$ zawiera wymuszanie Cohena”. Doprecyzowano wszystkie potrzebne obiekty i założenia: $M$ jest przeliczalnym tranzytywnym modelem ZFC, $\mathbb P_{\mathrm C}=\operatorname{Fn}(\omega,2)\in M$ jest pojęciem wymuszania Cohena, a $G\subseteq\mathbb P_{\mathrm C}$ jest filtrem $M$-generycznym. Poprawiono także sformułowanie końcowego argumentu: z przynależności $(\dot C)^G$ do $M$ wynikałaby przynależność jego funkcji charakterystycznej $c_G$ do **$M$**, a nie do samego zbioru $(\dot C)^G$.

### IV. Precyzyjny opis wyniku o $M[G]$

W końcowej uwadze zastąpiono nieprecyzyjne „zawieranie $M$ i $G$” dwoma różnymi relacjami: $M\subseteq M[G]$ oraz $G\in M[G]$. To ważne rozróżnienie logiczne: zbiór $G$ jest elementem rozszerzenia, niekoniecznie każdym swoim elementem wyznacza je jako podzbiór z tej samej przesłanki. Nie stwierdzono $M[G]\models\mathrm{ZFC}$ przed rozdziałem 33.

## Kontrola pozostałych argumentów

1. **Preporządek:** relacja $\le$ jest zwrotna i przechodnia, nie musi być antysymetryczna ani posiadać elementu największego. Zakładanie warunku $1_{\mathbb P}$ przy definiowaniu $\check x$ i $\dot G$ pozostaje jawne.
2. **Filtr i gęstość:** wszystkie implikacje respektują konwencję „silniejszy = mniejszy”. Dowód $D^\downarrow$ oraz przenoszenie przez gęsty podporządek nie odwracają kierunków.
3. **Rasiowa–Sikorski:** dla dowolnego niepustego pojęcia wymuszania i przeliczalnej rodziny gęstych zbiorów wykorzystano dobre uporządkowanie $\mathbb P$ w zewnętrznym ZFC, a nie założenie przeliczalności samego $\mathbb P$. Konstrukcja $G$ jako domknięcia malejącego ciągu ku słabszym warunkom jest poprawna.
4. **Generyczność nad $M$:** odpowiednie rodziny gęstych zbiorów należące do $M$ mogą być wyliczone zewnętrznie, skoro $M$ jest zewnętrznie przeliczalny. Nie utożsamiono tego z wyliczeniem należącym do $M$.
5. **Cohen:** gęstość $D_n$ i $E_x$, całkowitość $c_G$, jego nowość oraz odtwarzanie filtru z $c_G$ mają poprawne dowody. Wskazano dodatkowo absolutność samego zbioru skończonych warunków.
6. **Nazwy:** klasy poziomów $N_\alpha$, ograniczoność rang nazw występujących w zbiorze par i absolutność rozpoznawania nazw między $M$ i zewnętrznym uniwersum pozostają spójne. Rekurencja wyznaczająca $\tau^G$ oraz równości $(\check x)^G=x$, $(\dot G)^G=G$ są poprawne.
7. **Model rozszerzony:** wyprowadzono jedynie jego istnienie jako zbioru, tranzytywność, $M\subseteq M[G]$ i $G\in M[G]$. Do dowodu spełniania ZFC potrzebne będzie twierdzenie o wymuszaniu; nadal trafnie odłożono je do rozdziału 33.

## Kontrole regresyjne i walidacja

- Zachowano dotychczasową strukturę: **8 sekcji, 11 definicji, 7 lematów, 4 twierdzenia, 1 wniosek, 4 przykłady, 4 uwagi, 12 dowodów i 1 rysunek TikZ**.
- Zachowano **33 etykiety i 11 odsyłaczy** rozdziału, co nie zmienia zatwierdzonego inwentarza 803 etykiet i 590 odsyłaczy dla książki.
- Rozszerzono `tools/tests/test_logic_and_set_theory_ch32.py` o regresje dla poprawnego przedłużania skończonych warunków $p$ do $q$ różniącego się od ustalonego ciągu $x$ i o kontrolę jawnych hipotez przykładu $\dot C$. Testy są kontrolą regresji, **nie formalnym dowodem** twierdzeń w Lean.
- [GitHub Actions #45017199305](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017199305): **SUCCESS** dla wszystkich zmian matematycznych i nowych regresji rozdziału 32. Pełna kontrola importów, 14 testów rozdziału, pozostałe testy 1–31, kompilacja całej książki i kontrola logu PDF: PASS.
- [GitHub Actions #45017331864](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45017331864): **SUCCESS** po dodaniu i redakcji raportu audytu IV; ostatnie zmiany między przebiegami dotyczyły tylko pliku raportu.
- **Kontrola PDF:** z artefaktu przebiegu #45017199305 uzyskano książkę liczącą **280 stron**, z czego rozdział 32 zajmuje strony PDF **274–280** (drukowane numery 265–271). Wszystkie siedem stron wyrenderowano i obejrzano; drzewo Cohena, wzory, podpisy i odsyłacze są czytelne, bez nałożenia napisów na rysunki ani ucięć. Ostatnia strona pozostaje niepełna, lecz zawiera zasadniczy przykład i końcową uwagę — nie uzasadnia to agresywnego ścieśniania całej książki.
- **Kontrola logu:** **0 błędów**, **0 niezdefiniowanych odsyłaczy**, **0 ostrzeżeń o brakujących cytowaniach**, **0 przepełnień `Overfull \\hbox`**; pojedyncze `Underfull \\hbox` w całej książce.

## Werdykt audytu IV

**Audyt IV przyniósł rzeczywiste uzupełnienia matematyczne i redakcyjne bez dodawania twierdzeń.** Głównym wynikiem jest wyjaśnienie identyczności wewnętrznych i zewnętrznych warunków Cohena. **Testy regresyjne, kompilacja oraz siedmiostronicowa kontrola PDF zakończyły się powodzeniem.** Rozdział jest technicznie poprawny po audycie IV; nie został jeszcze uznany za w pełni stabilny matematycznie, ponieważ bieżący audyt wymagał korekt. Kolejny krok to audyt V, który powinien już skoncentrować się na wykrywaniu rzeczywistych kontrprzykładów i błędów logicznych, bez nadmiernego rozbudowywania tekstu.
