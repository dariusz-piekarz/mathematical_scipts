# Topologia ogólna — audyt globalny 17: niezależne potwierdzenie rozdziału 03

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Badany blob:** `b571753b5ab9a8777424fc32f6c4a54a4048af77`.
**Stan gałęzi przy odczycie:** `6a2dddc55aa14a7186773cec4c488e28c097a168`.
**Źródło:** `chapters/pl/general_topology/03-odwzorowania-ciagle.tex`.

## Zakres niezależnej kontroli aktualnego źródła

Przeczytano aktualny tekst rozdziału 03, w tym wszystkie 15 środowisk dowodowych, oraz porównano otwarte zagadnienie po korekcie z raportami globalnymi 11–14. Weryfikacja nie polegała na automatycznym przepisaniu werdyktu starszego raportu: raport 13 odnosił się do innego bloba `021f4f843b26e90dca57b3e38b33e95cd0c03a5b`.

- Globalne kryteria ciągłości: (i)→(ii) przez dopełnienia, (ii)→(iii) przez najmniejszy zbiór domknięty zawierający obraz, (iii)→(iv) po podstawieniu przeciwobrazu, (iv)→(ii) przez domknięcie, a (ii)→(i) ponownie przez dopełnienia. Żaden krok nie wymaga T1.
- Ciągłość punktowa i otoczeniowa: otoczenie nie musi być otwarte, ale zawiera otwarty zbiór obejmujący punkt; dowód stosuje to prawidłowo. Pusta dziedzina jest uwzględniona.
- Kryterium ε–δ: w obu kierunkach użyto baz kul dla odpowiednich topologii metrycznych.
- Kryteria bazy i podbazy: uwzględniono pustą sumę oraz puste skończone przecięcie podbazy (całe Y).
- Składanie, ograniczenie dziedziny i przeciwdziedziny: sprawdzono tożsamości przeciwobrazów, w szczególności `f(X)⊆B` w przypadku przeciwdziedziny.
- Sklejanie na otwartym pokryciu: otwartość `U_i` w X pozwala przejść od otwartości względnej do otwartości w X. Dla pustej rodziny pokrycie wymusza `X=∅`.
- Sklejanie na skończonym pokryciu domkniętym: domkniętość względna w `F_j` i domkniętość `F_j` w X dają domkniętość w X; skończoność rodziny jest niezbędna.
- Kryteria odwzorowań otwartych i domkniętych: sprawdzono oba kierunki i użycie ekstensywności wnętrza/domknięcia.
- Składanie odwzorowań otwartych i domkniętych: zastosowano definicje do obrazu odpowiedniego zbioru.
- Kryterium homeomorfizmu: dla bijekcji `h=f^{-1}`, `h^{-1}(U)=f(U)`; analogicznie dla zbiorów domkniętych.
- Zachowanie wnętrza, domknięcia, brzegu i zbioru pochodnego przez homeomorfizm: sprawdzono oba kierunki, bijektywność oraz usunięcie pojedynczego punktu bez ukrytego T1.
- Kryterium zanurzenia: otwartość względna obrazów otwartych zbiorów i ciągłość do `f(X)` zapewniają homeomorfizm na obraz.

**Kontrprzykłady:** dyskretna→antydyskretna identyczność, odwrotność Sorgenfreya, funkcja skokowa, nieciągła funkcja z ciągłymi ograniczeniami do singletonów, przestrzeń Sierpińskiego — wszystkie zgodne z tezą, dla której zostały użyte. Końcowy przykład zanurzenia korzysta z istniejącej etykiety `ex:topog-bijekcja-niehomeomorfizm`; korekta redakcyjna nie usuwa argumentu.

## Wydanie i CI — granice potwierdzenia

Raport globalny 14 dokumentuje **rzeczywisty** przebieg CI [45068776546](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068776546), artefakt [14771719456](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068776546/artifacts/14771719456) i wizualną kontrolę siedmiostronicowego wydania 03 na **tym samym blobie** `b571753b5ab9a8777424fc32f6c4a54a4048af77`. Poprawka `\\enlargethispage{1\\baselineskip}` nie spowodowała kolizji ze stopką ani osieroconego podsumowania według tamtej rzeczywistej inspekcji. W tej iteracji nie uruchamiano nowej kompilacji ani nie wykonywano ponownego renderingu; nie należy oznaczać ich jako nowego testu.

## Werdykt i następny krok

**PASS matematyczny na aktualnym blobie 03** — niezależna kontrola potwierdzająca po dwóch wcześniejszych czystych audytach matematycznych i udokumentowanym wydaniu PDF. Nie zmieniono treści matematycznej. W zakresie całej książki **nie ma jeszcze podstaw do globalnego PASS**: raport 16 kończy kontrolę wszystkich siedmiu dowodów rozdziału 15; następny audyt powinien sprawdzić wszystkie dowody rozdziału 16 (nie tylko wybrane wyniki raportu 10), potem kontynuować po kolei i uzgodnić sumaryczny rejestr dowodów. Weryfikować na nowo bloby i statusy CI przy każdej iteracji.
