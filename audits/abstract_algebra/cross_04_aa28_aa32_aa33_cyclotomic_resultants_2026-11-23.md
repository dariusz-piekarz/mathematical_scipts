# AA-X04 — audyt przekrojowy AA-28, AA-32, AA-33: wielomiany cyklotomiczne, wyróżniki i wypadkowe

**Data:** 23 listopada 2026 r.  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`.  
**Zakres źródeł:** AA-28 \`28-ciala-cyklotomiczne-i-wielomiany-cyklotomiczne.tex\`; AA-32 \`32-wyroznik-i-grupa-galois.tex\`; AA-33 \`33-wypadkowa-wielomianow-i-macierz-sylvestera.tex\`.

## 1. Nowa kontrola matematyczna

Po stabilizacji AA-X03 sprawdzono niezależnie zgodność konwencji i przejścia między trzema odrębnymi częściami skryptu. W AA-28 wielomian \(\Phi_n\) jest moniczny w \(\mathbb Z[X]\), nierozkładalny nad \(\mathbb Q\) i ma stopień \(\varphi(n)\). AA-32 definiuje wyróżnik jako iloczyn kwadratów różnic pierwiastków, a AA-33 stosuje \(\operatorname{disc}(f)=(-1)^{d(d-1)/2}R_{d,d-1}(f,f')\) ze świadomą konwencją znaku wypadkowej.

Wykonano następujące kontrole **dokładne** przy użyciu \`sympy\`:

1. **Wyróżnik cyklotomiczny:** dla każdego \(3\le n\le30\) sprawdzono
   \[
   \operatorname{disc}(\Phi_n)=
   (-1)^{\varphi(n)/2}
   \frac{n^{\varphi(n)}}{\displaystyle\prod_{\ell\mid n,\ \ell\ \mathrm{pierwsza}}
   \ell^{\varphi(n)/(\ell-1)}}.
   \]
   Jest to dodatkowa, znana tożsamość kontrolna; nie przypisujemy jej AA-28 jako wcześniej dowiedzionego tam twierdzenia. Uwzględniono znak, stopień oraz poprawną wykładniczą potęgę każdego czynnika pierwszego.
2. **Zgodność z wypadkową pochodnej:** dla każdego \(3\le n\le30\) bezpośrednio porównano dokładny wyróżnik z \((-1)^{\varphi(n)(\varphi(n)-1)/2}\operatorname{Res}(\Phi_n,\Phi_n')\). Obie wartości były identyczne.
3. **Wypadkowe różnych wielomianów cyklotomicznych:** dla wszystkich \(2\le n<m\le30\) (406 par) obliczono dokładnie wartość bezwzględną \(|\operatorname{Res}(\Phi_m,\Phi_n)|\). Zgadzała się ona z \(\ell^{\varphi(n)}\), gdy \(m/n=\ell^k\) dla pewnej liczby pierwszej \(\ell\) i \(k\ge1\); w innych przypadkach wynosiła \(1\). Kontrola ta uwzględnia wartości bezwzględne i nie miesza ich z konwencją znaku \(\operatorname{Res}\) oraz \(R\) z AA-33.
4. **Redukcja modulo \(p\):** dla \(3\le n\le30\) i \(p\in\{2,3,5,7,11\}\) niezależnie obliczono \(\gcd(\bar\Phi_n,\bar\Phi_n')\) i sprawdzono, czy redukcja jest rozdzielcza dokładnie wtedy, gdy \(p\nmid\operatorname{disc}(\Phi_n)\). Nie przyjęto nieprawdziwego twierdzenia, że **każda** liczba pierwsza dzieląca \(n\) musi dzielić \(\operatorname{disc}(\Phi_n)\); warunek dotyczy wyłącznie rzeczywistej wartości wyróżnika.

W badanym zakresie nie wykryto konfliktu hipotez, konwencji znaków ani nieuprawnionego przejścia z charakterystyki \(0\) do dodatniej. Wynik testów nie dowodzi ogólnych tożsamości dla wszystkich \(n\), lecz pozwala kontrolować usterki redakcyjne i matematyczne w konkretnych przykładach.

## 2. Reprodukcyjność i wynik

Nowy moduł \`tools/tests/test_abstract_algebra_cross_aa28_32_33.py\` przeprowadza **602 dokładne sprawdzenia**:
- wyróżnik cyklotomiczny: **28/28 PASS**;
- tożsamość wyróżnik–wypadkowa: **28/28 PASS**;
- wypadkowe par \(\Phi_m,\Phi_n\): **406/406 PASS**;
- kryterium rozdzielczości modulo \(p\): **140/140 PASS**.

Kod uruchomiono w bieżącej sesji, korzystając z Python/SymPy 1.14.0, i uzyskano \`AA-X04 independent checks 602\` bez błędów.

Powtórzenie:
\`\`\`bash
python tools/tests/test_abstract_algebra_cross_aa28_32_33.py
\`\`\`

Test zapisano w commicie \`0460ff4fc1d463a3995e698c3d804b2f7a3d67dd\` i podłączono do \`.github/workflows/abstract-algebra-chapter.yml\` w commicie \`78f15b3950c4a5e245b8603c33fa5426354ffd4d\` (wyzwalacz ścieżki i osobny krok). Workflow instalował już \`sympy\`; nie dodano zbędnych zależności.

## 3. Werdykt i ograniczenia

**Audyt matematyczny AA-X04 I: 602/602 PASS, bez nowo potwierdzonych błędów w sprawdzanym zakresie.** Źródła AA-28, AA-32 i AA-33 pozostają bez zmian. Audyt nie zastępuje pełnego, sceptycznego przeglądu wszystkich dowodów tych rozdziałów ani oględzin składu każdego rysunku.

**Dalsze kryterium stabilizacji:** potwierdzić \`completed/success\` workflow obejmującego nowy test oraz kontrolę całego PDF, a następnie wykonać osobny audyt potwierdzający AA-X04 na odmiennym modelu/testach, bez powielania tych samych 602 sprawdzeń. Do czasu spełnienia tych warunków AA-X04 oznaczamy jako **w trakcie stabilizacji**, nie jako zamknięty.
