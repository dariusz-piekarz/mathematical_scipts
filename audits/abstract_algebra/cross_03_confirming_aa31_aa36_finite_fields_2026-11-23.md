# AA-X03 — niezależny audyt potwierdzający AA-31–AA-36

**Data:** 23 listopada 2026 r.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Zakres:** AA-31 (wielomiany symetryczne), AA-32 (wyróżnik), AA-33 (wypadkowa), AA-34 (rezolwenta sześcienna), AA-35 (Frobenius), AA-36 (wielomian ogólny).

## Cel kontroli

Ten audyt jest **niezależną, sceptyczną kontrolą potwierdzającą** AA-X03. W odróżnieniu od poprzedniego audytu (wielomiany nad \(\mathbb Z\), przykłady grup Galois i permutacje), wyczerpująco testuje wszystkie moniczne wielomiany czwartego stopnia nad czterema ciałami skończonymi. Nowy program w **Pythonie bez zależności zewnętrznych** nie wykorzystuje testu JavaScript z pierwszego AA-X03.

## Rachunki matematyczne

Dla każdego wielomianu \(f=X^4+aX^3+bX^2+cX+d\) obliczono:
- rezolwentę \(r_f(Y)=Y^3-bY^2+(ac-4d)Y-(a^2d+c^2-4bd)\);
- wyróżniki \(f\) i \(r_f\) poprzez **oddzielne macierze Sylvestera i eliminację modularną**, zachowując formalne stopnie pochodnych (\(3\) dla \(f'\), \(2\) dla \(r_f'\)), również gdy charakterystyka zmniejsza ich rzeczywiste stopnie;
- niezależnie \(\gcd(f,f')\) i \(\gcd(r_f,r_f')\) za pomocą algorytmu Euklidesa;
- dla każdego rozdzielczego \(f\): \(D_k=\deg\gcd(f,X^{p^k}-X)\), \(k=1,\ldots,4\), metodą potęgowania modulo \(f\).

Sprawdzone tożsamości obejmują:
\[
\operatorname{disc}(f)=\operatorname{disc}(r_f),\qquad
\operatorname{disc}(f)\ne0\iff\gcd(f,f')=\gcd(r_f,r_f')=1.
\]
Z liczności \(D_k\) wyznaczono \(N_1=D_1\), \(N_2=(D_2-D_1)/2\), \(N_3=(D_3-D_1)/3\) i \(N_4=(D_4-D_2)/4\); sprawdzono nieujemność i \(\sum_{d=1}^4 dN_d=4\). Są to liczby czynników nierozkładalnych stopnia \(d\), czyli długości cykli Frobeniusa w AA-35.

Dla nieparzystego \(p\) dodatkowo sprawdzono kryterium parzystości
\[
\left(\frac{\operatorname{disc}(f)}p\right)=(-1)^{4-\sum_d N_d}.
\]
Wynika ono z \(\Delta^2=\operatorname{disc}(f)\) i \(\Delta^p=\operatorname{sgn}(\mathrm{Frob})\Delta\), gdzie \(\Delta\) to iloczyn Vandermonde’a pierwiastków \(f\). Nie stosowano tego kryterium w charakterystyce \(2\).

## Wyniki rzeczywiście uruchomionego testu

| Ciało | Kwartiki | Rozdzielcze | Nierozdzielcze | Testy parzystości |
|---|---:|---:|---:|---:|
| \(\mathbb F_2\) | 16 | 8 | 8 | 0 |
| \(\mathbb F_3\) | 81 | 54 | 27 | 54 |
| \(\mathbb F_5\) | 625 | 500 | 125 | 500 |
| \(\mathbb F_7\) | 2401 | 2058 | 343 | 2058 |
| **Suma** | **3123** | **2620** | **503** | **2612** |

Na wszystkich 3123 wielomianach sprawdzono równość wyróżników i zgodność testów rozdzielczości; na 2620 rozdzielczych — typ Frobeniusa; na 2612 rozdzielczych nad ciałami o nieparzystej charakterystyce — parzystość.

**Suma: \(2\cdot3123+2620+2612=11478\) sprawdzonych warunków, wszystkie PASS.** Jest to liczba wykonanych kontroli, nie liczba różnych twierdzeń.

Nowy odtwarzalny test: [\`tools/tests/test_abstract_algebra_cross_aa31_36_confirming.py\`](../../tools/tests/test_abstract_algebra_cross_aa31_36_confirming.py), uruchamiany komendą:
\`\`\`bash
python tools/tests/test_abstract_algebra_cross_aa31_36_confirming.py
\`\`\`
Plik testowy zapisano w commicie \`759b44c10e8813ddbf381ddf8906deab01fc977d\`; osobny krok CI i wyzwalacz w \`.github/workflows/abstract-algebra-chapter.yml\` w commicie \`14bc3f4ac4f76ece1b645feeaf315ae02a82a7f8\`.

## Wnioski i rygor stabilizacji

Nie wykryto błędów matematycznych w tym zakresie; szczególnie zweryfikowano przypadki charakterystyki \(2\) i \(3\), których nie wolno pomijać w AA-33/34. **Nie zmieniono źródeł LaTeX AA-31–AA-36.** Wcześniejsze AA-X03 zawiera niezależny przegląd PDF na stronach 207–232; bieżąca kontrola nie zastępuje tych oględzin.

Uruchomiono pełny zdalny workflow po integracji nowego testu:
https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45130907559

**W chwili sporządzenia tego raportu** wynik CI nie był jeszcze końcowy; jego status należy zaktualizować po zakończeniu testów, składania całej książki i weryfikacji odsyłaczy. Tylko zakończony sukcesem workflow zamyka AA-X03 jako etap stabilny.
