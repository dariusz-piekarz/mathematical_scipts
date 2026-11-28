# Algebra liniowa — rozdział 01, audyt 5

Data: 2026-11-21  
Gałąź docelowa: `biblioteka-matematyczna-iteracja-6`  
Rozdział: `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`  
Commit rozdziału po poprawkach: `4b446539bc2e199dddd2f5d3ba75a3a4146ef81d`

## Zakres przeglądu

Ponownie przeanalizowano wszystkie części rozdziału, szczególnie: operacje na rodzinach podprzestrzeni, bazę i rozpinanie w dowolnym wymiarze, zależność liniową dla rodzin indeksowanych, przypadki zerowe, istnienie bazy przez lemat Zorna, wybór bazy z generatorów oraz kwantyfikatory w przykładach. Utrzymano rozdzielenie teorii wymagającej jedynie aksjomatów ciała od argumentów korzystających z aksjomatu wyboru.

## Znalezione braki matematyczne

### 1. Unia rodziny podprzestrzeni skierowanej w górę

Dodano twierdzenie `thm:lin-unia-skierowana`. Dla niepustej rodziny podprzestrzeni \((W_i)_{i\in I}\), w której dla dowolnych \(i,j\) istnieje \(k\) z \(W_i\cup W_j\subseteq W_k\), unia jest podprzestrzenią. Udowodniono osobno istnienie zera (niepustość rodziny jest konieczna) oraz domknięcie na kombinacje \(au+bv\), stosując skierowanie do wyboru wspólnej podprzestrzeni. Uwzględniono rodzinę liniowo uporządkowaną przez zawieranie jako szczególny przypadek.

Dodano przykład `prz:lin-unia-wielomiany`:
\(K[X]=\bigcup_{n\ge0}K[X]_{\le n}\), wraz z wyjaśnieniem, dlaczego każdy wielomian ma skończony stopień i dlaczego unia rosnących podprzestrzeni jest podprzestrzenią.

### 2. Wybór bazy z dowolnego zbioru generatorów

Istniejące twierdzenie o przedłużaniu dowolnej rodziny niezależnej do bazy całej przestrzeni nie gwarantowało, że nowa baza pozostanie we wskazanym zbiorze generatorów. Dodano twierdzenie `thm:lin-baza-z-generatorow-zorn`: przy założeniu aksjomatu wyboru, jeśli \(S\subseteq V\) rozpina \(V\), \(S_0\subseteq S\) jest niezależny, to istnieje baza Hamela \(B\) z \(S_0\subseteq B\subseteq S\).

Dowód stosuje lemat Zorna do zbioru niezależnych podzbiorów \(S\) zawierających \(S_0\); rozdzielono puste i niepuste łańcuchy. Wykazano, że brak rozpinania przez maksymalny zbiór \(B\) wymusza istnienie elementu \(s\in S\setminus\operatorname{span}(B)\), którym można powiększyć \(B\).

Dodano przykład `prz:lin-dwie-bazy-z-generatorow`: z zależnego zbioru \(S=\{1,1+X,X,X^2,\ldots\}\subset K[X]\) można wybrać zarówno \(B_1=\{1,X,X^2,\ldots\}\), jak i \(B_2=\{1,1+X,X^2,\ldots\}\). Dla \(B_2\) uzasadniono rozpinanie przez odtworzenie \(X=(1+X)-1\) oraz niezależność z porównania współczynników.

### 3. Brak domknięcia przypadku \(W=\{0\}\) w twierdzeniu o wymiarze podprzestrzeni

W dowodzie `thm:lin-wymiar-podprzestrzeni` po wyprowadzeniu \(\dim_KW=0\leq\dim_KV\) argument przechodził do \(W\neq\{0\}\), nie dowodząc dla zera osobno części „równość wymiarów wtedy i tylko wtedy, gdy \(W=V\)”. Uzupełniono to: \(\dim_K W=\dim_K V\) przy \(W=\{0\}\) zachodzi dokładnie gdy \(\dim_K V=0\), co oznacza \(V=\{0\}=W\).

### 4. Precyzja kwantyfikatorów i terminologii

- Definicja bazy określa explicite, co znaczy, że \emph{rodzina indeksowana} \((b_i)_{i\in I}\) rozpina przestrzeń: \(\operatorname{span}\{b_i:i\in I\}=V\).
- W przykładzie niezależności \(B_2\) sprecyzowano \(d\geq2\) w skończonej kombinacji potęg \(X^j\), zamiast używać niezwiązanego zmiennego \(d\).

## Kontrola techniczna

Po poprawkach w aktualnym pliku:
- 64 unikalne etykiety `\\label`; brak duplikatów.
- Wszystkie lokalne `\\ref` i `\\eqref` mają istniejące cele.
- Zgodne i domknięte środowiska `\\begin`/`\\end`.
- Dwa rysunki TikZ; brak nowych zależności od zewnętrznych obrazów.
- Kontrola CI przed audytem 5: [44891361530](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44891361530) — zaliczona.
- CI dla końcowej wersji audytu 5: [44891689186](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44891689186) — **zaliczone (success)**. Wszystkie kroki dotyczące rozdziału, kompilacji LaTeX, weryfikacji PDF i eksportu artefaktu zakończyły się pomyślnie. W końcowym pliku `linear_algebra.log` nie znaleziono `Overfull`, `Underfull`, `LaTeX Warning`, `Undefined control sequence` ani `Missing character`. Ostrzeżenia o niezdefiniowanych odsyłaczach widoczne w zbiorczym logu zadania pochodziły z pierwszego przebiegu LaTeX i zostały rozwiązane w kolejnych przebiegach.

Wcześniejsze błędy całej Biblioteki (globalne kopie źródłowe, importy w innych skryptach) pozostają osobne od niniejszego audytu. Samo zaliczenie CI algebry liniowej nie oznacza ich naprawienia.

## Status

**Audyt 5 zakończony z poprawkami. Rozdział 01 pozostaje otwarty.** Następny audyt 6 powinien ponownie ocenić wszystkie wyniki i wskazane przykłady, zweryfikować najnowszy skład LaTeX oraz szukać dalszych luk przed jakąkolwiek decyzją o zamknięciu rozdziału. Rozdziału 02 jeszcze nie tworzymy.
