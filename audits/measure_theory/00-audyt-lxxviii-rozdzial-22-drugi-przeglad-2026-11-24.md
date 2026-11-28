# Audyt LXXVIII (78) — rozdział 22, drugi przegląd matematyczny

Data: 2026-11-24. Gałąź: biblioteka-matematyczna-iteracja-6.

## Stan wejściowy
Poprzedni commit CI 33dc92c2c938304592337f17c133e79ff5750cfa ma oba klasyczne statusy success (regressions i pdf), przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45283559941. To potwierdzenie dotyczy wyłącznie poprzedniej wersji. Nie przeprowadzono w tej iteracji oględzin artefaktu.

## Wyniki drugiego przeglądu
Rozdział 22, commit 465de7592ad0b5ce5898fb6d45c4525365792891, blob df7a09f46b6b6a7de0aa1f04f901bd95c49ad77f.
- W dowodzie odwrotnego kierunku Prochorowa brak osiągania infimum uniemożliwiał wybór miary o wartości nie większej od progu. Wprowadzono dwa progi a=1-epsilon*2^(-m-1) i b=1-epsilon*2^(-m-2), a<b; wybór wartości <b wynika z infimum <=a, a Portmanteau prowadzi do sprzeczności dla b.
- W obu dowodach ciasności jawnie zapisano wspólne ograniczenie masy dopełnienia epsilon/2, dzięki czemu infimum mas zwartego K jest ściśle większe od 1-epsilon.
- W Portmanteau uzasadniono przesunięcie i obcięcie dowolnej funkcji dolnie półciągłej ograniczonej z dołu, również ograniczonej z góry, z jawnie zapisanymi nierównościami.
- W przykładzie ucieczki masy zastąpiono niewystarczający argument testem stałym 1 przez zwarte funkcje odcinające f_R, które wymuszają zerową masę każdego [-R,R], a zatem całej prostej.
- Ponownie prześledzono konstrukcję granicy na separowalnej przestrzeni metrycznej: borelowskość obrazów na każdym zwartym K_m, pełna masa ich sumy, addytywność i oszacowania przy przedłużaniu funkcji testowych. Nie znaleziono kolejnej luki w tej konstrukcji.

## Regresje i CI
Commit 6932c096dd9a129bae9a6bcc35a27361ac4eb022 dodaje dwa testy: dokładny model wymierny nieosiąganego infimum oraz zwarte funkcje odcinające wraz z kontrolą źródła. Łącznie 10 metod. Commit a90443dc4daeba784e10d1dfc14957a3b0de7328 aktualizuje nazwę kroku CI oraz renderuje każdą stronę rozdziału, nie tylko trzy wybrane.
Kontrola rzeczywiście wykonana na aktualnych plikach: 22 etykiety, wszystkie unikalne; poprawne zagnieżdżenie środowisk LaTeX; 10 metod testowych; wszystkie cztery nowe wzorce źródłowe obecne w źródle oraz testach. Nie uruchamiano lokalnie Pythona ani LaTeX-a w tej iteracji. Klasyczne statusy commitu a90443dc4daeba784e10d1dfc14957a3b0de7328 były jeszcze puste podczas odczytu.

## Werdykt
Rozdział 22 nadal w stabilizacji. Następna iteracja: odczytać faktyczne wyniki nowych 10+4 testów, pełnej i izolowanej kompilacji, skontrolować wszystkie strony PDF oraz ponownie sprawdzić poprawione dowody. Nie przechodzić do 23 przed spełnieniem tych warunków.
