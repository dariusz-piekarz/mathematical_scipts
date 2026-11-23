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
