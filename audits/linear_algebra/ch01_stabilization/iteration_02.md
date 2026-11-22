# Algebra liniowa — rozdział 01, audyt stabilizacyjny II (pierwszy czysty przegląd źródła)

**Data:** 22 listopada 2026.  
**Weryfikowana wersja:** `chapters/pl/linear_algebra/01-przestrzenie-wektorowe.tex`, Git blob `374e74dfa46f72597abcb8f5721268fed2245c4a`; źródło niezmienione w tym audycie.

## Niezależna kontrola drugiej iteracji
1. **Aksjomaty i przykłady:** wszystkie własności z Lematu `lem:lin-aksjomaty-konsekwencje` wynikają z aksjomatów przestrzeni; weryfikacja nad ciałem \(\mathbb F_2\) nie korzysta z podziału przez 2. Przykłady \(K^0\), \(K^\varnothing\), wielomianów, funkcji i zmiany ciała skalarów mają rozdzielone założenia.
2. **Podprzestrzenie:** kryterium podprzestrzeni działa również dla zbioru pustego (nie jest podprzestrzenią), rodziny z pustym zbiorem indeksów i rodziny skierowanej. Dowód pokrycia przestrzeni przez skończoną liczbę właściwych podprzestrzeni nad ciałem nieskończonym poprawnie wykorzystuje minimalne podpokrycie, rodzinę \(x+ty\) i skończoność wykluczonych skalarów. Nad \(\mathbb F_2\) podano prawidłowy kontrprzykład dla trzech podprzestrzeni.
3. **Niezależność:** w rozdziale konsekwentnie oddzielono podzbiory \(S\) od rodzin indeksowanych \((v_i)_{i\in I}\), co zapobiega błędowi przy powtórzonym wektorze. W dowodach jednoznaczności współczynników występuje tylko skończony nośnik; suma pusta i baza zerowa są uwzględnione.
4. **Steinitz i skończony wymiar:** niezależność \(v_{k+1}\) zapewnia niezerowy współczynnik któregoś niewymienionego generatora w każdym kroku; wyprowadzenie wzoru na ten generator i argument \(r\le m\) są poprawne również dla zerowych i powtarzających się początkowych generatorów. Dowody równości liczby elementów baz, charakteryzacji skończonej wymiarowości i równości \(\dim W=\dim V\iff W=V\) są kompletne, także dla \(n=0\).
5. **Nieskończony wymiar:** lemat o łańcuchu niezależnych zbiorów uzasadnia skończony charakter warunku, w tym łańcuch pusty; obie konstrukcje Zorna wyjaśniają ograniczenie górne i sprzeczność z maksymalnością. Istnienie bazy nieskończonej jest wyraźnie oparte na aksjomacie wyboru. Izomorfizm \(V\cong K^{(I)}\) jest dowiedziony z dwóch stron i sprawdza pusty zbiór indeksów.
6. **Wyprowadzenia i przykłady:** niezależność \((1,i)\) nad \(\mathbb R\), wyprowadzenie współrzędnych w niestandardowej bazie, bazy wielomianów oraz konstrukcja dwuwymiarowej przestrzeni rozwiązań rekurencji Fibonacciego są poprawne.
7. **Weryfikacja po korekcie:** w przykładzie ciągów skończonego nośnika sprawdzono od nowa wzór \((ax+by)_n=ax_n+by_n=0\) dla indeksów poza sumą nośników. Dopisane rozumowanie wyczerpuje warunki kryterium podprzestrzeni.

## Testy, odsyłacze i układ
- Samodzielne testy przeszły: 125 par podprzestrzeni nad małymi ciałami, 12 000 skończonych nośników, 323 rodziny w kryteriach baz; **40 884 przypadki wymiany Steinitza** z powtarzanymi/zerowymi generatorami również **PASS**.
- Dokładnie 24 środowiska twierdzeń/lematów/stwierdzeń/wniosków i 24 dowody, bez wiszących twierdzeń. 69 różnych etykiet, wszystkie 27 odsyłaczy rozdziału wskazują na lokalne etykiety. Żadne dopasowanie zakazanego słowa „unia” nie występuje poza utrwalonymi etykietami \(\LaTeX\).
- CI dla wersji bez zmian semantycznych poza dostosowaniem delimitatorów matematyki: [45003215772](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45003215772) **SUCCESS**. CI dla dokładnie aktualnego SHA po zmianie delimitatorów [45003380934](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45003380934) pozostaje do potwierdzenia.
- PDF skompilowanego rozdziału po merytorycznej korekcie to 16 stron A4 (strony 6–21 książki), bez pustych stron i tekstu poza formatem. Obejrzano montaż wszystkich 16 stron oraz powiększenia obu diagramów ze stron 9 i 13 książki, bez kolizji tekstu z rysunkami.

## Decyzja
**Audyt II: pierwszy czysty audyt matematyczny i redakcyjny źródła** — żadnych poprawek ani rozszerzeń w tej iteracji. Formalne nadanie statusu stabilnego wymaga drugiego czystego audytu niezmienionego pliku i pozytywnego CI dokładnie najnowszego źródła.
