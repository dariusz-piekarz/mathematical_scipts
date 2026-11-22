# Algebra liniowa — rozdział 03: ponowny audyt stabilizacyjny II (drugi czysty)

**Data:** 22 listopada 2026. **Źródło:** \`chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex\`.
**Nieprzerwany SHA pliku w audytach I–II:** \`7ee828f8438e6030cb7f47685433aa3639220ab7\`.

## Druga kontrola, niezależne podejście przez przypadki brzegowe i warunki konieczne

1. Sprawdzono niezmienność własności liniowych w charakterystyce 2; w przykładzie \(2_Kx=0\) skalar 2 jest jawnie zależny od \(K\), a wszystkie definicje działają dla dowolnego ciała.
2. Dla bazy pustej \(I=\varnothing\), \(V=\{0\}\) i dowolnego \(W\) jedyne odwzorowanie liniowe jest zerowe. Dowód przedłużenia odwzorowania z wartości na bazie nie zakłada niejawnie niezerowości przestrzeni.
3. Przy \(A=\varnothing\) oba zbiory w \(T(\operatorname{span}A)=\operatorname{span}(T(A))\) są przestrzenią zerową. Z definicji obrazu i jądra wynika poprawnie kryterium iniektywności i surjektywności także dla zerowej przestrzeni.
4. Ponownie zweryfikowano niezależność zbioru \(T(D)\) w rank–nullity: każda zależność prowadzi do wektora z \(\operatorname{span}(D)\cap\operatorname{span}(C)=\{0\}\), a następnie do zerowych współczynników. Wersja nieskończona korzysta tylko z dodawania kardynalnego i AC przy wyborze baz; wariant skończony nie potrzebuje AC.
5. Dla pierwszego twierdzenia o izomorfizmie sprawdzono dokładne przeciwdziedziny \(V/\ker T\), \(\operatorname{im}T\), \(W\) oraz składania z włożeniem \(\iota\). Równanie \(\widehat T=\widetilde T\circ\pi_{\ker T}\) jest poprawnie ilustrowane diagramem, a kryterium faktoryzacji zachowuje obie implikacje \(U\subseteq\ker T\).
6. Rozpatrzono granice stosowalności kryterium iniektywność \(\Leftrightarrow\) surjektywność: wymagana jest *skończona równość wymiarów*; kontrprzykłady \(T(p)=Xp\) i \(R(p)=(p-p(0))/X\) dowodzą, że samo równe \(\aleph_0\) nie wystarcza.
7. Wartości odwzorowań \(E_{ji}\) na bazie dowodzą niezależności i rozpinania \(\operatorname{Hom}\) także w przypadkach \(n=0\) lub \(m=0\); składanie w \(\operatorname{End}\) jest dwuliniowe, a przykład \(P,Q\) ma nieprzemienne złożenia przy każdym \(1_K\ne0_K\).
8. Projekcja z rozkładu \(V=U\oplus W\) jest poprawnie jednoznaczna, bez założenia \(\dim V<\infty\). Dla \(P^2=P\) rozkład \(v=P(v)+(v-P(v))\) ma drugi składnik w jądrze, a pierwszy w obrazie; identyczność \(P|_{\operatorname{im}P}=\operatorname{id}\) jest istotnym warunkiem odwrotnej implikacji.

## Kontrole formalne, PDF i CI

- Ponownie odczytano niezmienione **1019 wierszy**, **17 pełnych dowodów**, **8 przykładów**. Zliczono **19 odsyłaczy** i potwierdzono każde miejsce docelowe w rozdziałach 01–03. Łącznie 150 etykiet bez duplikatów; wszystkie środowiska LaTeX zagnieżdżone prawidłowo.
- Ponownie skontrolowano układ **10 stron A4** wydzielonych z PDF pełnej książki: diagram pierwszego twierdzenia o izomorfizmie, podsumowanie i brak kolizji, ucięć czy pustych stron. Log nie wykazał \`Overfull\`, \`Underfull\` ani niezdefiniowanych odsyłaczy.
- Weryfikacja pełnego CI [45005167546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45005167546) jest **SUCCESS**, 39 kroków zakończonych sukcesem. Log nowego kroku: **593 odwzorowania**, **72 projekcje**, **8678** wariantów faktoryzacji, **172544** tożsamości dotyczących przestrzeni rozpiętej — wszystkie PASS.
- Raport I odnotowuje odrębny czysty przebieg matematyczny na *tym samym* SHA źródła. Podczas żadnego z audytów I–II nie wprowadzono zmiany do rozdziału.

**Wniosek:** dwa kolejne czyste audyty źródła na niezmienionej wersji, pełne testy i zweryfikowany PDF uzasadniają status **STABILNY**. Uruchomienia CI wywołane wyłącznie zapisaniem raportów wymagają osobnego potwierdzenia dla końcowego SHA gałęzi.
