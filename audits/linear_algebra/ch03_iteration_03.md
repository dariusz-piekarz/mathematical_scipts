# Algebra liniowa — rozdział 03, audyt 3

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/03-odwzorowania-liniowe-jadro-i-obraz.tex`  
**Commit zmiany w rozdziale:** `22de35f6e6461be45cb1254d033c4bad5fe1f042`

## Kryterium audytu

Trzeci audyt obejmuje wyłącznie **poprawność już istniejących twierdzeń, dowodów i przykładów**: kompletność założeń i kwantyfikatorów, typowanie odwzorowań, przypadki wymiaru zero i nieskończonego, zależność od aksjomatu wyboru, język matematyczny, rysunki, etykiety i kompilację. Nie dodano żadnych nowych twierdzeń, definicji, lematów ani przykładów.

## Poprawka

### Definicja rzędu i wymiaru jądra — niepełne założenia

W definicji `def:lin3-rzad-nullity` występowało:

`Niech \(T\colon V\to W\) będzie liniowe.`

Nie było tu jawnego wskazania, że \(V,W\) są przestrzeniami nad tym samym ciałem \(K\), choć następnie używano symbolu \(\dim_K\). Zmieniono zdanie na:

`Niech \(V,W\) będą przestrzeniami wektorowymi nad \(K\), a \(T\colon V\to W\) odwzorowaniem liniowym.`

Definicja stała się samodzielna. Nie zmieniono równości \(\operatorname{rk}T=\dim_K(\operatorname{im}T)\) i \(\operatorname{null}T=\dim_K(\ker T)\), założenia AC dla dowolnych wymiarów ani zastrzeżenia o skończonych wymiarach bez AC.

## Powtórna analiza matematyczna

- **Liniowość i wartości na bazie:** poprawne są kryterium zachowywania kombinacji \(av+bw\), zachowywanie wektora zerowego i skończonych kombinacji, istnienie i jednoznaczność przedłużenia wartości zadanych na bazie Hamela oraz zgodność odwzorowań na zbiorze rozpinającym. Rozpatrzono również \(V=\{0_V\}\), pustą bazę i ciała dowolnej charakterystyki.
- **Jądro i obraz:** sprawdzono kryterium podprzestrzeni, równość \(T(\operatorname{span}(A))=\operatorname{span}(T(A))\), przeciwobraz podprzestrzeni, charakterystykę iniektywności i surjektywności. Rozkłady wielomianów oraz operatory \(T(p)=Xp\) i \(R(p)=(p-p(0))/X\) są poprawne.
- **Wzór na wymiar jądra i obrazu:** rozszerzenie bazy \(\ker T\) do bazy \(V\) i przeniesienie pozostałych wektorów na bazę obrazu są uzasadnione. W wersji kardynalnej używa się aksjomatu wyboru, w wersji skończonej wystarczają skończone konstrukcje; nieskończonych liczb kardynalnych nie odejmuje się.
- **Pierwsze twierdzenie o izomorfizmie:** powtórnie zweryfikowano dobrą określoność, liniowość, iniektywność i surjektywność \(\widetilde T\colon V/\ker T\to\operatorname{im}T\). Poprawione w audycie 2 rozróżnienie \(\widehat T\colon V\to\operatorname{im}T\) i \(\iota\colon\operatorname{im}T\hookrightarrow W\) poprawnie typuje oba złożenia.
- **Składanie i odwrotność:** przeanalizowano liniowość złożenia, zawierania dla jądra i obrazu, liniowość odwrotności izomorfizmu oraz skończenie wymiarowe kryterium równoważności iniektywności, surjektywności i bijektywności.
- **Przestrzenie \(\operatorname{Hom}\) i \(\operatorname{End}\):** dowód \(\dim_K\operatorname{Hom}_K(V,W)=mn\) poprawnie konstruuje bazę z odwzorowań \(E_{ji}\) i obejmuje przypadki \(m=0\), \(n=0\). Składanie endomorfizmów jest łączne i dwuliniowe; przypadek przestrzeni zerowej został wyjaśniony w pierwszym audycie.
- **Projekcje:** zachowano istotne założenie \(P|_{\operatorname{im}P}=\operatorname{id}\) w równoważności dla dowolnego \(P\); przeanalizowano obydwa kierunki oraz jednoznaczne odtworzenie projekcji ze wskazanego rozkładu \(V=U\oplus W\).

Nie wykryto fałszywego twierdzenia, niepoprawnego kontrprzykładu ani nowej zasadniczej luki dowodowej. Wprowadzona korekta dotyczy jedynie samodzielności istniejącej definicji.

## Niezależne testy skończone

Wykonano wszystkie mapy liniowe \(\mathbb F_2^n\to\mathbb F_2^m\) dla \(0\leq n,m\leq3\), czyli **689 odwzorowań**; każda z \(16\) par wymiarów ma poprawną liczność przestrzeni \(\operatorname{Hom}\), równą \(2^{nm}\).

Dla wszystkich 689 map przetestowano:
- \(2^n=|\ker T|\cdot|\operatorname{im}T|\), odpowiadające wzorowi \(\dim\ker T+\dim\operatorname{im}T=n\);
- wzajemnie jednoznaczne przyporządkowanie klas \(V/\ker T\) do elementów obrazu.

Dla map o \(n\leq2\) zweryfikowano dodatkowo **459 przypadków** par \(T,U\), gdzie \(U\subseteq\mathbb F_2^n\) jest podprzestrzenią. Stwierdzono, że wzór \(S(v+U)=T(v)\) jest dobrze określony dokładnie wtedy, gdy \(U\subseteq\ker T\).

**Liczba rozbieżności: 0.** Testy nie zastępują dowodów matematycznych.

## Weryfikacja struktury repozytorium

- Rozdziały 01–03 zawierają **150 unikalnych etykiet**, bez duplikatów.
- Sprawdzono wszystkie **62 wystąpienia `\\ref`/`\\eqref`**; brak nierozwiązanych odsyłaczy.
- Wszystkie `\\begin` i `\\end` są poprawnie zagnieżdżone.
- Nie ma niepożądanych form „unia” ani „relacja liniowa” w prozie matematycznej.
- Zachowano stabilne identyfikatory wszystkich twierdzeń i rysunków.
- Nie dodano nowych plików graficznych ani zależności zewnętrznych.
- GitHub Actions dla zmian: [44903957413](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44903957413) — wynik końcowy do uzupełnienia.

## Status

**Audyt 3 zakończony z jedną poprawką formalną. Rozdział 03 pozostaje otwarty.** Następna iteracja powinna nadal weryfikować wyłącznie obecną treść. Nie należy sztucznie dopisywać materiału tylko w celu uzyskania zmian w kolejnych audytach.
