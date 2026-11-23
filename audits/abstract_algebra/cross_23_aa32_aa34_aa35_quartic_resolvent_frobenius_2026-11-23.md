# AA-X23 — rezolwenta sześcienna, wyróżnik i cykle Frobeniusa (AA-32 × AA-34 × AA-35)

**Data:** 23 XI 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Poprzednia stabilizacja:** AA-X22 zakończony sukcesem [CI 45229800650](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45229800650), 6/6 testów i 100/100 kroków.

**Sprawdzone źródła:** AA-32 (blob f8c525aff1093478dcd8b1083387a42a37078086), AA-34 (a7202801c7e5ae9d4ad202a5deceabd631512a85), AA-35 (345bdebd74b8190bfb04f70ac7afe56b043dcb11). Zasady redakcyjne: AGENTS.md. Wcześniejsze AA-X04 (cyklotomiczne wyróżniki/wypadkowe) i AA-X22 (Frobenius, Möbius, symbol Legendre’a) nie obejmowały **zgodności typów cykli na czterech pierwiastkach z typami cykli na trzech wartościach rezolwenty**. Nie wprowadzono zmian do źródeł AA-01–AA-50.

## 1. Twierdzenie przekrojowe i pełny dowód

Niech \(f(X)=X^4+aX^3+bX^2+cX+d\in\mathbb Z[X]\) będzie moniczny i będzie miał cztery różne pierwiastki nad \(\mathbb Q\). Niech \(r_f(Y)=Y^3-bY^2+(ac-4d)Y-(a^2d+c^2-4bd)\) będzie rezolwentą z AA-34. Dla liczby pierwszej \(p\) takiej, że \(p\nmid\operatorname{disc}(f)\), rozkłady \(\overline f\in\mathbb F_p[X]\) i \(\overline{r_f}\in\mathbb F_p[Y]\) na nierozkładalne czynniki są rozdzielcze. Jeżeli typ stopni czynników \(\overline f\) wynosi \(\lambda\), to typ stopni czynników \(\overline{r_f}\) jest równy \(\rho_*(\lambda)\), gdzie \(\rho:S_4\to S_3\) jest działaniem na trzech rozkładach czteroelementowego zbioru na dwie pary, a jego wartości są następujące:

| Typ \(\overline f\) | Typ \(\overline{r_f}\) | Uzasadnienie |
|---|---|---|
| \((1,1,1,1)\) | \((1,1,1)\) | identyczność działa trywialnie |
| \((1,1,2)\) | \((1,2)\) | transpozycja zamienia dwa podziały |
| \((2,2)\) | \((1,1,1)\) | podwójna transpozycja należy do \(V_4\) |
| \((1,3)\) | \((3)\) | trójcykl obraca wszystkie trzy podziały |
| \((4)\) | \((1,2)\) | czterocykl przechodzi w transpozycję |

**Dowód.** Z AA-34 mamy dla czterech pierwiastków \(\alpha_1,\ldots,\alpha_4\) trzy wyrażenia \(\beta_1=\alpha_1\alpha_2+\alpha_3\alpha_4\), \(\beta_2=\alpha_1\alpha_3+\alpha_2\alpha_4\), \(\beta_3=\alpha_1\alpha_4+\alpha_2\alpha_3\). Różnice parami wartości \(\beta_i\) są iloczynami różnic odpowiednich \(\alpha_j\), stąd tożsamość \(\operatorname{disc}(r_f)=\operatorname{disc}(f)\) (udowodniona w AA-34 również w charakterystyce \(2\)). Ponieważ \(p\) jest dobry dla \(f\), obie redukcje mają dokładnie cztery i trzy różne pierwiastki. Wybierzmy ich numerację w domknięciu algebraicznym \(\overline{\mathbb F}_p\) w sposób zgodny z definicją trzech \(\beta_i\). Frobenius \(\varphi:z\mapsto z^p\) zachowuje sumy i iloczyny oraz współczynniki całkowite po redukcji, a zatem dla każdej pary indeksów \(\varphi(\bar\alpha_i\bar\alpha_j)=\varphi(\bar\alpha_i)\varphi(\bar\alpha_j)\). W konsekwencji permutacja \(\bar\beta_1,\bar\beta_2,\bar\beta_3\) jest dokładnie obrazem przez \(\rho\) permutacji \(\bar\alpha_1,\ldots,\bar\alpha_4\). Na mocy AA-35 długości cykli tych permutacji są stopniami monicznych nierozkładalnych czynników odpowiednio \(\bar f\) i \(\overline{r_f}\). Pozostaje policzyć obrazy pięciu możliwych typów cykli w \(S_4\). Rachunek na trzech podziałach daje tabelę powyżej, przy czym całym jądrem jest \(V_4\) zgodnie z AA-34. **Koniec dowodu.**

**Istotna granica:** pojedynczy typ \((1,2)\) rezolwenty nie rozróżnia typu \((4)\) od \((1,1,2)\) wielomianu wyjściowego. Tak samo rozkładalność rezolwenty nad \(\mathbb Q\) nie rozróżnia samodzielnie grup \(C_4\) i \(D_4\). Nie wolno również odczytywać typu cykli z rozkładu \(\bar f\) przy złej redukcji.

## 2. Zgodność ze znakiem permutacji i wyróżnikiem

Jądro \(\rho\) składa się z identyczności i trzech podwójnych transpozycji, czyli wyłącznie permutacji parzystych. Z tabeli można sprawdzić, że \(\operatorname{sgn}(\rho(\sigma))=\operatorname{sgn}(\sigma)\) dla każdego z pięciu typów \(\sigma\in S_4\). Jest to także konieczne z równości wyróżników rezolwenty i oryginalnego wielomianu oraz kryterium znaku Frobeniusa przy nieparzystych dobrych \(p\). **Uwaga:** równość znaków jest własnością permutacji także przy \(p=2\), ale nie należy utożsamiać liczb \(\pm1\) w ciele \(\mathbb F_2\) ani stosować tam symbolu Legendre’a.

## 3. Niezależne modele dokładne

Sprawdzono przez SymPy (arytmetyka całkowita) następujące pary \(f,r_f\) oraz odpowiadające wyróżniki:
- \(C_4\): \(\Phi_5=X^4+X^3+X^2+X+1\), \(r_f=(Y-2)(Y^2+Y-1)\), wyróżnik \(125\).
- \(D_4\): \(X^4-2\), \(r_f=Y(Y^2+8)\), wyróżnik \(-2048\).
- \(V_4\): \(X^4-10X^2+1\), \(r_f=(Y+10)(Y-2)(Y+2)\), wyróżnik \(147456\).
- \(S_4\): \(X^4-X-1\), \(r_f=Y^3+4Y-1\), wyróżnik \(-283\).
- Przypadek rozkładalny nad \(\mathbb Q\): \(\prod_{j=1}^4(X-j)\), rezolwenta \((Y-14)(Y-11)(Y-10)\), wyróżnik \(144\).
- Przykład z pierwiastkiem wielokrotnym: \((X-1)^2(X+2)(X-3)\) — wyróżniki obu wielomianów są \(0\), niezależnie od nierozdzielczości.

Dla 5 wielomianów oraz liczb pierwszych \(p\in\{2,3,5,7,11,13,17,19,23,29\}\) trwały test porównuje niezależne rozkłady \(\bar f\) i \(\overline{r_f}\), filtrując tylko dobre redukcje na podstawie rzeczywistego wyróżnika. W szczególności \(\Phi_5\) przy \(p=2\) ma typ \((4)\), podczas gdy rezolwenta typ \((1,2)\); dla \(X^4-2\) przy \(p=3\) typ \((2,2)\) przechodzi w \((1,1,1)\); dla wielomianu o grupie \(S_4\) przy \(p=7\) typ \((1,3)\) przechodzi w \((3)\). Kontrolę złych redukcji oraz kryterium Legendre’a dla dobrych nieparzystych \(p\) wykonuje osobny test.

Niezależnie skonstruowano **wszystkie 24 permutacje \(S_4\)** i obliczono ich działanie na trzech podziałach. Sprawdzono 24 obrazy, 4 elementy jądra \(V_4\), 576 tożsamości homomorfizmu \(\rho(\sigma\tau)=\rho(\sigma)\rho(\tau)\), zgodność typów cykli i znaków. Obliczenia nie opierają się na rozkładzie wielomianu.

## 4. Integracja z repozytorium i granice

Dodano moduł tools/tests/test_abstract_algebra_cross_aa32_34_35.py z **6 testami**: (1) działanie \(S_4\) i jądro \(V_4\); (2) wzory rezolwenty i równości wyróżników; (3) typy cykli po dobrej redukcji; (4) niejednoznaczność rekonstrukcji typu i przypadki grup \(C_4,D_4,V_4,S_4\); (5) złe redukcje i symbol Legendre’a; (6) dokładne etykiety, hipotezy i odsyłacze w pełnym drzewie źródeł.

Z bezpośredniego odczytu źródeł wynika: AA-32 ma 9 etykiet i 5 odsyłaczy, AA-34 ma 14 etykiet i 14 odsyłaczy, AA-35 ma 12 etykiet i 14 odsyłaczy; łącznie **35 etykiet i 33 odsyłacze**. Test weryfikuje unikatowość etykiet w całym zbiorze 50 rozdziałów i poprawność wskazań wszystkich celów, również zewnętrznych.

Plik .github/workflows/abstract-algebra-chapter.yml otrzymał wyzwalacz nowego testu i osobny krok Run AA-X23 quartic resolvent and Frobenius quotient checks. Uruchomienie [GitHub Actions 45232861043](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45232861043), commit f36df6aecfbec499f35f98cecefd7fbee14e0b83.

**Status przy zapisaniu: W STABILIZACJI CI**. Do zamknięcia wymagane są 6/6 testów \`ok\` w rzeczywistym logu, pełny zielony workflow, kompilacja AA-01–AA-50 oraz automatyczna weryfikacja PDF i odsyłaczy. Kompilacja LaTeX nie jest osobnym wizualnym przeglądem każdej strony PDF; takiego przeglądu ta iteracja nie wykonuje. Otrzymane testy skończonych modeli nie zastępują dowodów i nie są formalizacją Lean.

**Propozycja opcjonalna:** dodać po AA-34 krótką tabelę pięciu przejść typów cykli przez \(\rho:S_4\to S_3\), łączącą rozdziały AA-34 i AA-35. Zgodnie z AGENTS.md nie wstawiano nowego materiału do zatwierdzonego rozdziału bez zgody użytkownika. Dotychczasowe źródła AA-01–AA-50 i AA-51 pozostają bez zmian (AA-51 nadal nie istnieje).

## 5. Zamknięcie AA-X23 po pełnym CI — STABILNY

**Zweryfikowany przebieg:** [GitHub Actions 45232861043](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45232861043), niezmienny commit testowo-workflowowy f36df6aecfbec499f35f98cecefd7fbee14e0b83. Status przebiegu: **completed / success**. Job validate-cli ID 137896749872 wykonał **101/101 kroków**, bez błędów. W rzeczywistym logu sprawdzono **6/6 testów AA-X23 = ok** (każdy występuje jako ok zarówno w globalnym odkrywaniu testów, jak i w odrębnym kroku Run AA-X23 quartic resolvent and Frobenius quotient checks). SymPy wypisał nieblokujące ostrzeżenie o przyszłym wycofaniu porównań elementów modularnych w sortowaniu czynników; nie stanowi ono obecnie awarii testu.

Krok Compile AA-01 to AA-50 book with latexmk: **success**. Krok Verify PDF and references (no undefined refs): **success**. Opublikowano artefakt abstract-algebra-aa01-aa50, ID 14847314501, rozmiar ZIP **2 289 387 bajtów**. Nie wykonano w AA-X23 osobnej wizualnej kontroli wszystkich stron PDF. Zakończona kompilacja, sprawdzenie odsyłaczy i brak przepełnionych pudełek w logu nie są tożsame z taką kontrolą.

**Werdykt:** audyt przekrojowy AA-X23 jest **zamknięty i stabilny** w określonym zakresie matematycznym i technicznym. Nie wykryto obowiązkowych poprawek w zatwierdzonych rozdziałach. Dowód ogólny, enumeracja grupy \(S_4\), rachunki modularne i automatyczne kontrole kodu stanowią niezależnie opisane poziomy argumentacji — testy nie są formalizacją Lean. Nie modyfikowano źródeł AA-01–AA-50 ani ich wcześniejszych statusów. AA-51 nie jest otwarty. Ewentualne dodanie tabeli cykli do AA-34 wymaga osobnej decyzji użytkownika zgodnie z AGENTS.md.
