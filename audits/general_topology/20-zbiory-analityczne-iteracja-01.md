# Topologia ogólna — rozdział 20, audyt 01

**Data:** 2026-11-22. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Źródło:** \`chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex\`.
**Blob:** \`2de2c9a5d30952abdb726f856f9bad55dfa857d1\` (728 wierszy).
**Wynik:** pierwszy audyt matematyczny i strukturalny **CZYSTY**.
**Status stabilizacji:** **W AUDYCIE** — konieczna kolejna niezależna kontrola i pełny zielony workflow dla tego samego bloba.

## Kontrola nakładania się ze skryptem logiki

Sprawdzono tekst \`chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex\` oraz rozdziały 28–29 i 31–33. Rozdział 30 logiki zawiera definicje zbiorów analitycznych/projektywnych i ich zastosowania w determinacji, gry Banacha–Mazura, regularność i redukcje Wadge’a. Przywołuje także uniwersalną mierzalność zbiorów analitycznych jako twierdzenie **bez dowodu**. Zaplanowany rozdział 20 topologii nie był więc całkowitym duplikatem.

Nowy materiał celowo ograniczono do wciąż brakujących **dowodów topologicznych**. Nie powielono teorii gier, AD, PD i redukcji Wadge’a; nie zadeklarowano udowodnienia uniwersalnej mierzalności ani rozdzielania zbiorów analitycznych. Wspólne definicje występują tylko w zakresie koniecznym dla samodzielności tekstu.

## Audyt matematyczny rozdziału 20

1. **Przestrzeń Baire’a.** Cylindry \`[s]\` są otwarto-domknięte, a ich rodzina jest przeliczalną bazą topologii produktu. Ustalono jednoznaczne oznaczenia \`s^\frown k\` i \`\alpha|n\`.
2. **Surjekcja z Baire’a na dowolną niepustą przestrzeń polską.** Dla każdego domkniętego niepustego \`F_s\` jego przecięcia z domkniętymi kulami o środkach w przeliczalnym gęstym D i promieniach \`2^{-|s|-3}\` tworzą przeliczalne pokrycie domkniętymi zbiorami o średnicach nie większych niż \`2^{-|s|-2}\`. Powtórzenie elementów zapewnia countably many children także przy pokryciu skończonym. Na dowolnej gałęzi zbiory są malejące, niepuste, domknięte i mają średnice dążące do 0. W zupełnej metryce ich przecięcie jest singletonem. Równy prefiks długości n zapewnia odległość obrazów ≤\`2^{-n}\` (faktycznie mocniejsze oszacowanie). Wybieranie dzieci zawierających zadany punkt daje surjektywność. Nie użyto lokalnej zwartości ani niewłaściwego twierdzenia o zwartości dowolnych polskich przestrzeni.
3. **Obrazy i rzuty.** Graf ciągłego \`f:\mathcal N→X\` jest domknięty w \`X×\mathcal N\`, bo X jest Hausdorffa. Domknięty podzbiór iloczynu polskich jest polski, więc jest obrazem ciągłym przestrzeni Baire’a. Wynika poprawna równoważność: analityczny ↔ rzut domkniętego podzbioru \`X×\mathcal N\`. Przypadek pusty rozpatrzono.
4. **Przeliczalne działania.** Dla \`A_n=\pi_X(F_n)\` sumę realizuje zbiór domknięty z dyskretnym znacznikiem n w \`X×(\mathbb N×\mathcal N)\`, a przecięcie — domknięty zbiór wszystkich jednoczesnych świadków w \`X×(\mathcal N^\mathbb N)\`. Obie przestrzenie świadków są homeomorficzne z \`\mathcal N\` przez enumerację współrzędnych. Istnienie świadków dla przecięcia korzysta z przeliczalnego wyboru, dopuszczonego w zadeklarowanym ZFC. Twierdzenie obejmuje zbiory puste. Obrazy i przeciwobrazy przez odwzorowania ciągłe zachowują analityczność.
5. **Zbiory borelowskie.** Rodzina \`D=\{B:B\ \text{i}\ X\setminus B\ \text{są analityczne}\}\` jest σ-algebrą na podstawie zamknięcia analitycznych na przeliczalne sumy i przecięcia. Każdy domknięty jest analityczny jako domknięta podprzestrzeń polskiej; każdy otwarty jest F-sigma, a więc przeliczalną sumą analitycznych domkniętych. Stąd \`\mathcal B(X)⊂D\`, bez błędnego założenia, że zbiory analityczne są zamknięte na dopełnienia.
6. **Operacja Suslina.** Dla domkniętych \`F_s\` zbiór \`H=\{(x,\alpha):∀n\,x∈F_{\alpha|n}\}\` jest przecięciem domkniętych zbiorów rozdzielonych otwarto-domkniętymi cylindrami, a jego rzutem jest dokładnie \`\mathcal A(F_s)\`. W przeciwnym kierunku z domkniętego \`H⊂X×\mathcal N\` zdefiniowano \`F_s=\overline{\pi_X(H∩(X×[s]))}\`. Dla x w operacji Suslina i gałęzi α wybrano \`(x_n,u_n)∈H\` z \`d(x_n,x)<1/n\` i \`u_n∈[\alpha|n]\`. W produkcie \`(x_n,u_n)→(x,\alpha)\`, więc domkniętość daje x w rzucie. Obie implikacje dowiedzione, bez niejawnego założenia monotoniczności F_s.
7. **Uniwersalny zbiór analityczny.** Zakodowano drzewa par prefiksów jednakowej długości przez współrzędne \`c∈\mathcal N\`; zbiór wszystkich trójek \`(c,x,y)\` zgodnych na każdym poziomie jest domknięty jako przecięcie warunków cylindrycznych. Jego rzut \`U⊂\mathcal N²\` jest analityczny i uniwersalny dla wszystkich analitycznych przekrojów: dla dowolnego domkniętego \`F⊂\mathcal N²\` drzewo prefiksów przecinających F dokładnie rozpoznaje F, gdyż F jest domknięty.
8. **Nieborelowski analityczny.** Z \`D=\{x:(x,x)∉U\}\` i założenia analityczności D otrzymalibyśmy \`D=U_c\` dla pewnego c, a wtedy \`c∈D↔c∉D\`. Zatem D nie jest analityczny. Przeciwobraz U przez ciągłą przekątną \`E=\{x:(x,x)∈U\}\` jest analityczny. Nie jest borelowski, bo wtedy D byłby borelowski i tym samym analityczny. Rozróżnienie między analitycznym a borelowskim jest matematycznie ścisłe.

## Weryfikacja techniczna i testy

- Tekst rozdziału 20: **22 unikatowe etykiety**, **18 odsyłaczy**; wszystkie środowiska LaTeX są sparowane. Kontrole delimiterów: \`22\` par \`\\[\\]\` oraz \`246\` par \`\\(\\)\`. Brak terminów zabronionych i rysunków wymagających sprawdzenia układu.
- Nowe źródło jest w \`catalog/books.json\` jako rozdział nr 20, w \`books/pl/general_topology.tex\` i w samodzielnym \`books/pl/general_topology_ch20.tex\`. Dodano test \`tools/tests/test_general_topology_ch20.py\` (514 relacji na skończonych przestrzeniach dyskretnych, w tym puste i pełne) oraz włączono go do \`.github/workflows/general-topology-chapter.yml\`.
- Rozszerzono stary test rozdziału 19 tak, by wymagał co najmniej 19 rozdziałów zamiast dokładnie 19, oraz skorygowano dosłowne dopasowanie \`\\emph{nie} stanowi\` w nowym teście.
- W uruchomieniu [45022254599](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45022254599) kroki testów rozdziałów 19 i 20 zgłosiły **success**; w chwili spisania tego raportu cała walidacja i kompilacja pełnej książki były nadal **in_progress**. Nie deklarujemy jeszcze zielonego pełnego CI ani wizualnej weryfikacji nowego PDF.
- Poprzednie failed workflows uruchomione w trakcie integracji dotyczyły przejściowo niespójnych testów katalogu i sztywnego wymogu liczby rozdziałów; poprawiono przyczyny tych błędów.

## Decyzja

**Audyt 01: czysty matematycznie; rozdział 20 pozostaje w audycie** do samodzielnego ponownego przeglądu i zakończonej pomyślnie walidacji CI/PDF. Nie dodawać tu treści rozdziału 30 logiki, szczególnie determinacji i redukcji Wadge’a. Ewentualne głębsze twierdzenia o mierzalności zbiorów analitycznych wymagają osobnego dowodu i dalszego planowania między skryptami.
