# Algebra abstrakcyjna — audyt przekrojowy 18 (AA-X18): Nakayama × rzutowość × płaskość

**Data:** 2026-11-23. **Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.
**Poprzedni audyt:** AA-X17 zamknięty, 7/7 testów, 95/95 ukończonych kroków i zielona kompilacja tomu, [CI 45206650247](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45206650247).
**Zakres:** AA-14 (pierścienie lokalne, lemat Nakayamy), AA-16 (moduły wolne i rzutowe, rozszczepienia) oraz AA-18 (płaskość i iloczyn tensorowy).
**Źródła odczytane bezpośrednio:** AA-14 \`bd327c84847088000195270dab35e40daa2b73a6\`, AA-16 \`319cbac9af83a819e0d375fc282284c62638c3ac\`, AA-18 \`faaa972f8d1a7625d42c856d78c6f58ee7ad3564\`.

## 1. Nowe powiązanie teoretyczne — pełny dowód z hipotezami

**Twierdzenie (konsekwencja AA-14 i AA-16).** Niech \`(R,\mathfrak m)\` będzie niezerowym **przemiennym pierścieniem lokalnym z jedynką**, a \`P\` skończenie generowanym **rzutowym** \`R\`-modułem. Wtedy \`P\` jest wolny i ma rangę \`r=\dim_{R/\mathfrak m}(P/\mathfrak m P)\`. Jeśli \`P=0\`, przyjmujemy \`r=0\`.

**Dowód.** Niech \`K=R/\mathfrak m\`. Z twierdzenia AA-14 o minimalnej liczbie generatorów wybieramy elementy \`p_1,\ldots,p_r\in P\`, których klasy tworzą bazę \`P/\mathfrak m P\` i generują \`P\`. Wyznaczają one surjekcję \`f:R^r\to P\` daną przez \`f(e_i)=p_i\`. Rzutowość \`P\` (AA-16) daje przekrój \`s:P\to R^r\` spełniający \`f\circ s=\operatorname{id}_P\`, a więc rozkład \`R^r\simeq\ker f\oplus P\`. Jądro \`N=\ker f\` jest skończenie generowane: jako składnik sumy prostej \`R^r\` jest obrazem rzutowania \`R^r\to N\`, więc obrazy standardowych \`r\` generatorów generują \`N\`. Po przejściu modulo \`\mathfrak m\` rozkład daje \`K^r\simeq N/\mathfrak m N\oplus P/\mathfrak m P\`. Drugi składnik ma wymiar \`r\`; zatem \`N/\mathfrak m N=0\`, czyli \`N=\mathfrak m N\`. Lemat Nakayamy z AA-14 dla **skończenie generowanego** \`N\` daje \`N=0\`. Zatem \`f\` jest izomorfizmem \`R^r\to P\`. Koniec dowodu.

Z AA-18 wynika ponadto, że taki \`P\` jest płaski, jako moduł wolny. Nie zachodzi ogólna odwrotność „płaski ⇒ rzutowy”; AA-18 zawiera kontrprzykład \`\mathbb Q\` nad \`\mathbb Z\` (nie jest to pierścień lokalny). Nie zastępujemy powyższego argumentu stwierdzeniem, że wszystkie płaskie moduły są rzutowe.

## 2. Trzy niezależne przypadki brzegowe

1. **Rzutowy, wolny lokalnie w przykładzie:** \`R=\mathbb F_p[t]/(t^k)\`, gdzie \`p=2,3\` i \`k=2,3\`. Jedynym ideałem maksymalnym jest \`\mathfrak m=(t)\`, o \`t^k=0\` i \`t^{k-1}\ne0\`. Endomorfizm \`R^2\` o macierzy \`P=\begin{psmallmatrix}1&t\\0&0\end{psmallmatrix}\` ma \`P^2=P\`, obraz \`R(1,0)\`, jądro \`R(-t,1)\`, przecięcie \`0\` i sumę \`R^2\`. Wartości są sprawdzane dokładnie (skończona arytmetyka wielomianów).
2. **Liczba generatorów nie oznacza rzutowości:** \`M=R\oplus R/(t)\` ma \`M/\mathfrak m M\simeq\mathbb F_p^2\`, więc potrzeba dokładnie dwóch generatorów. Natomiast \`R/(t)\` jest cykliczny, lecz nie jest wolny, a z powyższego twierdzenia nie jest rzutowy. Bezpośrednia przeszkoda płaskości: iniekcja \`(t)\hookrightarrow R\` po wzięciu iloczynu tensorowego z \`R/(t)\` nie pozostaje iniekcją. Istotnie \`(t)\otimes_R R/(t)\simeq(t)/(t^2)\simeq\mathbb F_p\ne0\`, lecz obraz w \`R\otimes_R R/(t)\simeq R/(t)\` jest zerowy. To sprawdza także wymóg z AA-18.
3. **Dlaczego pierścień musi być lokalny:** dla \`R=\mathbb F_p\times\mathbb F_p\` idempotent \`e=(1,0)\` daje rozkład \`R=eR\oplus(1-e)R\`. Moduł \`eR\` jest rzutowy, ale nie jest wolny: ma \`p\` elementów, zaś dowolny niezerowy wolny \`R\`-moduł skończonej rangi ma \`p^{2r}\` elementów. Jest to poprawny kontrprzykład do zbyt szerokiej wersji twierdzenia bez założenia lokalności.

## 3. Nowe testy, odsyłacze i bramki

Dodano \`tools/tests/test_abstract_algebra_cross_aa14_16_18.py\` — **6 nowych testów jednostkowych**:
- kryterium jednostek w lokalnych pierścieniach obciętych;
- minimalne generatory sumy modułu wolnego i ciała reszt;
- idempotent i rozkład \`R^2\` na obraz i jądro;
- utrata iniektywności po iloczynie tensorowym z ciałem reszt;
- rzutowy niewolny moduł nad iloczynem dwóch ciał;
- kontrola etykiet i odsyłaczy w źródłach (AA-14, AA-16, AA-18).

Odczytano **71 etykiet** (25 + 26 + 20), bez duplikatów, i istniejące odsyłacze. Jedyny cel występujący w AA-18 poza trzema rozdziałami to prawidłowa etykieta \`aa:ch:grupy-abelowe\` w AA-08. Nie zmieniano treści wcześniejszych rozdziałów.

Workflow \`.github/workflows/abstract-algebra-chapter.yml\` rozszerzono o osobny krok \`Run AA-X18 Nakayama local-projective-flat crosschecks\` i wyzwalacz nowego testu.

**Nowe CI**: [45210323226](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45210323226), commit \`22b9f898be49e7c3437f7c12790077a0954337af\`. W chwili zapisu raportu: \`queued\`; **nie potwierdzono jeszcze wyniku testów i kompilacji**.

**AA-X18: W STABILIZACJI.** Po ukończeniu workflow zweryfikować: 6/6 testów \`ok\` z logu, brak błędów całego CI, kompilację AA-01–AA-50 i kontrolę PDF. Dopiero wtedy oznaczyć AA-X18 jako zamknięty. Nie przedstawiać testów przykładów jako formalnego dowodu wszystkich twierdzeń.

## 4. Granice i dalszy plan

Przeprowadzony dowód łączy trzy rozdziały i podkreśla konieczne założenia: przemienność, lokalność i skończone generowanie modułu rzutowego. W zatwierdzonych rozdziałach nie znaleziono sprzeczności wymagającej natychmiastowej korekty. Dodanie powyższego twierdzenia jako materiału wzbogacającego AA-16 wymaga osobnej decyzji użytkownika — **nie wstawiano go automatycznie**. Zachowano statusy AA-01–AA-50; AA-51 nie został otwarty.

## 5. Wynik końcowy — AA-X18 ZAMKNIĘTY / PASS

Zweryfikowano ostateczny wynik [GitHub Actions 45210323226](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45210323226) na \`22b9f898be49e7c3437f7c12790077a0954337af\`: **completed/success**, job \`validate-cli\`, **96/96 kroków ukończonych**, zero kroków błędnych. Odczytano rzeczywiste logi i potwierdzono wszystkie **6/6 testów AA-X18 = ok**, zarówno jako część globalnego odkrywania testów, jak i w samodzielnym kroku \`Run AA-X18 Nakayama local-projective-flat crosschecks\`.

Krok \`Compile AA-01 to AA-50 book with latexmk\`: **success**; \`Verify PDF and references (no undefined refs)\`: **success**; publikacja artefaktu także **success**. Artefakt \`abstract-algebra-aa01-aa50\`, ID \`14835854098\`, ZIP 2 289 388 bajtów. **Nie deklaruje się niezależnej wizualnej inspekcji stron PDF.**

Dodatkowa, odrębna kontrola arytmetyczna (poza skryptem Pythona, kod JS) dla trzech par \`(p,k)=(2,2),(2,3),(3,2)\` wykazała prawdziwość wszystkich pięciu sprawdzanych warunków: rozmiary ideałów \`(t)\` i \`(t^2)\`, nilpotentność o właściwym wykładniku, kryterium odwracalności, niezerowy moduł \`(t)/(t^2)\` oraz rozmiar i postać obrazu/jądra rozważanego idempotentu. Nie przenosi się tych testów przykładów na formalną weryfikację twierdzenia ogólnego; osobny dowód opisano w punkcie 1.

**Werdykt:** niezależna kontrola logiczna, źródłowa i testowa AA-14 × AA-16 × AA-18 zamknięta bez koniecznych poprawek zatwierdzonych źródeł. Dotychczasowe statusy stabilności rozdziałów AA-01–AA-50 pozostają nienaruszone. AA-51 nie otwierano.
