# AA-X04 — niezależny audyt potwierdzający: AA-28, AA-32, AA-33

**Data:** 2026-11-23.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Badane rozdziały:** AA-28 (wielomiany cyklotomiczne), AA-32 (wyróżniki), AA-33 (wypadkowe).  
**Pierwszy audyt:** \`cross_04_aa28_aa32_aa33_cyclotomic_resultants_2026-11-23.md\`.  
**Nowy test potwierdzający:** \`tools/tests/test_abstract_algebra_cross_aa28_32_33_confirming.py\`.

## Cel: inna metoda niż w audycie pierwszym

Audyt I wykonał 602 kontrole całkowitoliczbowych wyróżników i wypadkowych oraz kryterium rozdzielczości po redukcji. W audycie potwierdzającym **nie odtwarza się ich arytmetyki wyznacznikowej**. Zamiast tego użyto:
- tożsamości iloczynowej \(\prod_{d\mid n}\Phi_d(X)=X^n-1\) w \(\mathbb Z[X]\);
- faktoryzacji \(\Phi_n\) nad \(\mathbb F_p\) i rzędu multiplikatywnego \(p\bmod n\);
- wielomianowego algorytmu Euklidesa dla par \(\overline{\Phi_m},\overline{\Phi_n}\).

Test uruchomiono na podstawie biblioteki SymPy 1.14.0 w bieżącej sesji, bez użycia wcześniejszego modułu testowego.

## 1. Integralność wielomianów cyklotomicznych — 30/30

Dla \(1\le n\le30\) zbudowano wszystkie \(\Phi_d\) i obliczono dokładny iloczyn \(\prod_{d\mid n}\Phi_d\). Za każdym razem otrzymano \(X^n-1\), zgodnie z definicją i konstrukcją w AA-28. Sprawdzenie obejmuje wartości \(n\) będące potęgami liczb pierwszych, iloczynami różnych liczb pierwszych oraz liczbami o mieszanej strukturze czynników.

## 2. Typ Frobeniusa i rozkłady — 276/276

Dla \(2\le n\le30\) i liczb pierwszych \(p<32\), \(\gcd(n,p)=1\), wykonano niezależną faktoryzację \(\Phi_n\bmod p\).
Każdy czynnik nierozkładalny miał stopień równy rzędowi elementu \(p\in(\mathbb Z/n\mathbb Z)^\times\), a liczba czynników była równa \(\varphi(n)/\operatorname{ord}_n(p)\). Wszystkie czynniki wystąpiły z krotnością \(1\).

To równocześnie kontroluje ograniczenia charakterystyki w AA-28 i zgodność wielomianów cyklotomicznych z działaniem Frobeniusa, rozwijanym w AA-35.

## 3. Wspólne pierwiastki po redukcji — 4466/4466

Dla wszystkich \(2\le n<m\le30\) i jedenastu liczb pierwszych \(p<32\) sprawdzono osobno \(\gcd(\Phi_m\bmod p,\Phi_n\bmod p)\). Dodatni stopień występował **dokładnie** wtedy, gdy \(m/n=p^a\) dla pewnego \(a\ge1\). Jest to nowa kontrola modalna zależności między wypadkowymi a wspólnymi pierwiastkami: zgodnie z AA-33, dla monicznych wielomianów podzielność całkowitej wypadkowej przez \(p\) jest równoważna istnieniu wspólnego czynnika po redukcji modulo \(p\). W audycie I ta sama zależność była sprawdzana przez wartości wypadkowych, a tutaj przez **niezależne obliczenie NWD w różnych ciałach skończonych**.

Uwaga: wynik dotyczy par różnych indeksów \(\Phi_m,\Phi_n\) i redukcji modulo wybrane liczby pierwsze; nie twierdzi się, że samo \(\Phi_n\bmod p\) jest nierozkładalne.

## Wynik i reprodukowalność

| Grupa sprawdzeń | Wynik |
|---|---:|
| Rozkład \(X^n-1\) na wielomiany cyklotomiczne | 30/30 |
| Stopnie czynników i działanie Frobeniusa | 276/276 |
| NWD po redukcji dla par indeksów | 4466/4466 |
| **Suma** | **4772/4772 PASS** |

Nie sumujemy liczników z obu audytów jako liczby różnych twierdzeń: testują wybrane konsekwencje wspólnej teorii różnymi metodami.

Odtwarzalna komenda:
\`\`\`bash
python tools/tests/test_abstract_algebra_cross_aa28_32_33_confirming.py
\`\`\`
Nowy test utworzono w commicie \`57791136733cbc6b2d26a67c287d48bc51ec6f51\`. Workflow rozszerzono o jego wyzwalacz i osobny krok w commicie \`eee72c287a91d90992994b81587e2c2bca172997\`.

## Werdykt i bramka stabilizacji

Nie znaleziono nowych błędów w badanych twierdzeniach i zależnościach. Źródła matematyczne AA-28, AA-32, AA-33 pozostawiono bez zmian. **Oba niezależne audyty matematyczne AA-X04 są ukończone**.

W chwili opublikowania tego raportu nowy pełny workflow [AA-01–AA-42, AA-X04](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45131584372) znajdował się w toku. Aby oznaczyć AA-X04 jako ostatecznie **STABILNY**, należy stwierdzić \`completed/success\` nowego testu i pełnego CI, obejmującego skład tomu, odsyłacze i pozostałe regresje, a następnie zaktualizować niniejszy raport. W tej iteracji nie wykonywano nowej odrębnej wizualnej inspekcji stron PDF; ich ocena jest udokumentowana we wcześniejszych audytach rozdziałowych.


## Dodatkowa kontrola odsyłaczy i struktury

Niezależnie pobrano aktualne źródła AA-28, AA-32 i AA-33 bezpośrednio z docelowej gałęzi. Ich bloby: AA-28 \`2e24a69608aeab7856acf40f882480a97eb455bc\`, AA-32 \`f8c525aff1093478dcd8b1083387a42a37078086\`, AA-33 \`40f339a13b5890418869a12ef27881d29233ffe7\` (bez zmian matematycznych w bieżącej iteracji).

| Rozdział | Etykiety | Odsyłacze | Dowody | Przykłady |
|---|---:|---:|---:|---:|
| AA-28 | 10 | 6 | 4 | 2 |
| AA-32 | 9 | 5 | 4 | 4 |
| AA-33 | 10 | 5 | 4 | 3 |
| **Suma** | **29** | **16** | **12** | **9** |

Wszystkie 29 etykiet są unikatowe. Każdy z 16 odsyłaczy ma istniejący cel; pięć odsyłaczy zewnętrznych wskazuje odpowiednio \`aa:ch:fields-fractions\` (AA-19), \`aa:ch:kummer\` (AA-26), \`aa:tw:fundamental-symmetric\` i \`aa:tw:vieta-general\` (AA-31), \`aa:tw:orbita-stabilizator\` (AA-03). Zweryfikowano te etykiety w źródłach docelowych. Wszystkie środowiska \`\\begin\`/\`\\end\` są poprawnie zagnieżdżone, a wszystkie trzy rozdziały występują w pliku głównym \`books/pl/abstract_algebra.tex\`.

**Weryfikacja w zdalnym CI:** oba nowo dodane kroki \`Run AA-X04 cyclotomic cross-audit\` i \`Run AA-X04 independent confirmation\` w przebiegu \`45131584372\` uzyskały status \`completed/success\`. Status końcowy całej kompilacji i kontroli odsyłaczy pozostaje odrębną bramką stabilizacji.


## Zamknięcie AA-X04 po pełnym CI i kontroli wizualnej

**Wynik końcowy:** [GitHub Actions 45131584372](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45131584372), commit \`eee72c287a91d90992994b81587e2c2bca172997\`: **completed/success**, bez nieudanych kroków.

Potwierdzono osobno sukces:
- \`Run AA-X04 cyclotomic cross-audit\`;
- \`Run AA-X04 independent confirmation\`;
- \`Run AA-X03 independent confirming audit\`;
- \`Compile AA-01 to AA-42 book with latexmk\`;
- \`Verify PDF and references (no undefined refs)\`;
- \`Archive build output\`.

Pobrano oryginalny artefakt GitHub Actions **14797877474** \`abstract-algebra-aa01-aa42\` z przebiegu \`45131584372\`, obejmujący \`abstract_algebra.pdf\` i \`abstract_algebra.log\`. PDF liczy **269 stron**. Bezpośrednia analiza finalnego logu wykazała **0** ostrzeżeń LaTeX, **0** ostrzeżeń \`hyperref\`, **0** \`Overfull \\hbox\`, **0** \`Overfull \\vbox\`, **0** \`Underfull \\hbox\`, **0** nierozwiązanych odsyłaczy i **0** błędów LaTeX.

Przeprowadzono **kontrolę wizualną 12 stron związanych z AA-X04**: PDF 193–196 (AA-28), PDF 211–214 (AA-32) i PDF 215–218 (AA-33). Wyrenderowano je, obejrzano zestawienia stron i nie stwierdzono kolizji tekstu, wzorów, rysunków ani ucięć. Ponadto porównano z najnowszym wydaniem PDF z GitHub Actions: tekst oraz obraz rastrowy **wszystkich 12 stron** były dokładnie identyczne ze skontrolowanym wydaniem, więc oględziny dotyczą także wyniku końcowego CI.

**Końcowy werdykt AA-X04: STABILNY.** Dwa niezależne audyty matematyczne (602 oraz 4772 dokładne sprawdzenia), kontrola 29 unikatowych etykiet i 16 odsyłaczy, pełny CI i kontrola PDF zakończyły się bez nowego błędu wymagającego korekty źródeł. Zatwierdzone źródła AA-28/32/33 pozostały bez zmian; przejść można do następnej niezależnej kontroli przekrojowej.
