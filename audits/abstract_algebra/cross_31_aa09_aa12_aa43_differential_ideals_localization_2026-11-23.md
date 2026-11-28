# Algebra abstrakcyjna — AA-X31: ideały różniczkowe, ilorazy i lokalizacje (AA-09 × AA-12 × AA-43)

**Data:** 23 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Etap przed stabilizacją CI.**

## 1. Źródła i wyłączony zakres powtórzeń

Przed rozpoczęciem tej iteracji zamknięto AA-X30 po potwierdzeniu rzeczywistego przebiegu [GitHub Actions #45283034330](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45283034330), commit b2d7c2b82784d7606e56b25ea4e6691f3ba7c427, 7/7 nowych testów, sukces kompilacji AA-01–AA-50 i kontroli logu PDF. Raport AA-X30 uzupełniono i oznaczono jako zamknięty.

Źródła AA-X31 odczytane na bieżącej gałęzi:
- AA-09: chapters/pl/abstract_algebra/09-pierscienie-idealy-i-homomorfizmy.tex, blob c6a5ac5d6f8f067a051c49860eae815915bff7d0 (756 wierszy), definicja aa:def:ideal i twierdzenie aa:tw:ring-quotient;
- AA-12: chapters/pl/abstract_algebra/12-pierwiastniki-idealow-i-lokalizacja-pierscieni.tex, blob f64ec91a7fcc58557dba8b13f75b74f6b2ca788d (905 wierszy), definicja aa:def:localization i twierdzenie aa:tw:localization-universal;
- AA-43: chapters/pl/abstract_algebra/43-ciala-rozniczkowe-derywacje-i-rozszerzenia.tex, blob c6563f402b7890e5e0c8f02796ebf649f4336906 (540 wierszy), definicja aa:def:differential-field oraz reguły różniczkowania ilorazów.

AA-X31 dotyczy zachowania **derywacji na ogólnych pierścieniach** przy dwóch konstrukcjach algebraicznych. Nie powtarza AA-X06 (ideały, noetherowskość i lokalizacja), AA-X12 (całkowanie elementarne) ani AA-X29 (bazy transcendencji i derywacje ciał). Nie poszerzono wcześniej zatwierdzonych źródeł.

## 2. Twierdzenie: dokładny warunek na derywację ilorazu

**Twierdzenie.** Niech R będzie przemiennym pierścieniem z jedynką (dowolnej charakterystyki), D:R→R derywacją addytywną spełniającą D(ab)=aD(b)+D(a)b dla wszystkich a,b∈R, a I ideałem R. Istnieje derywacja \(\overline D:R/I\to R/I\) spełniająca
\[
\overline D(a+I)=D(a)+I\quad(a\in R)
\]
wtedy i tylko wtedy, gdy \(D(I)\subseteq I\). Jeśli istnieje, to jest jedyna.

**Dowód.** Jeżeli \(\overline D\) istnieje, dla a∈I mamy a+I=0 i stąd D(a)+I=\overline D(0)=0, więc D(a)∈I. Odwrotnie, załóżmy D(I)⊆I. Jeśli a+I=b+I, to a−b∈I, a zatem D(a)−D(b)=D(a−b)∈I; wobec tego podany wzór nie zależy od reprezentanta. Addytywność wynika z addytywności D. Dla iloczynu korzystamy z Leibniza: \(\overline D((a+I)(b+I))=D(ab)+I=(a+I)(D(b)+I)+(D(a)+I)(b+I)\). Jednoznaczność jest wymuszona surjektywnością projekcji R→R/I. Koniec dowodu.

**Kontrprzykład konieczny.** W R=Q[x], D=d/dx, I=(x), elementy x i 0 są równymi klasami w R/I, ale ich pochodne 1 i 0 są różnymi klasami. Nie wolno więc mówić, że dowolna derywacja przechodzi do ilorazu.

## 3. Twierdzenie: jednoznaczne przedłużanie przez lokalizację

**Twierdzenie.** Niech R,D będą jak wyżej, a S⊆R zbiorem multiplikatywnym zawierającym 1 i niezawierającym 0. Wtedy istnieje dokładnie jedna derywacja \(\widetilde D:S^{-1}R\to S^{-1}R\), dla której \(\widetilde D(a/1)=D(a)/1\) dla wszystkich a∈R. Jest określona wzorem
\[
\widetilde D(a/s)=\frac{sD(a)-aD(s)}{s^2}.
\]
Nie zakłada się, że R jest dziedziną całkowitości; wolno mieć dzielniki zera, przy czym w konstrukcji relacji ułamków należy stosować poprawny warunek z AA-12.

**Dowód niezależności od reprezentanta.** Jeśli a/s=b/t w S^{-1}R, to istnieje u∈S z \(u(at-bs)=0\). Po zastosowaniu D dostajemy \(D(u)(at-bs)+uD(at-bs)=0\). W lokalizacji u/1 jest jednostką, zaś \((at-bs)/1=0\), stąd \(D(at-bs)/1=0\). Oznaczmy q=at−bs. Po sprowadzeniu wzorów na pochodne obu reprezentacji do mianownika s²t² różnica ich liczników ma postać
\[
(st)D(q)-qD(st).
\]
Jej obraz w lokalizacji znika, bo q/1=0 oraz D(q)/1=0. To właśnie uzasadnia, że wzór jest dobrze określony także przy dzielnikach zera.

**Dowód pozostałych własności.** Addytywność po sprowadzeniu do wspólnego mianownika wynika z addytywności i reguły Leibniza w R; dla iloczynu otrzymuje się zwykły wzór \(D((ab)/(st))\) przez zastosowanie Leibniza do licznika i mianownika. Dla s∈S mamy \(\widetilde D((s/1)^{-1})=-\widetilde D(s/1)(s/1)^{-2}\), więc każda derywacja przedłużająca D musi spełniać formułę ilorazu. Ponieważ każdy element lokalizacji ma postać (a/1)(s/1)^{-1}, wynik jest jedyny. Koniec dowodu.

## 4. Zgodność operacji: iloraz, a następnie lokalizacja

**Twierdzenie.** Przy założeniach poprzednich wyników niech dodatkowo I będzie ideałem D-stabilnym: D(I)⊆I. Załóżmy S∩I=∅. Wtedy S^{-1}I jest ideałem \(\widetilde D\)-stabilnym w S^{-1}R i kanoniczny izomorfizm pierścieni
\[
\frac{S^{-1}R}{S^{-1}I}\ \cong\ \bar S^{-1}(R/I),
\qquad \bar S=\{s+I:s\in S\},
\]
jest zgodny z derywacjami indukowanymi po obu stronach.

**Dowód.** Jeśli a∈I, s∈S, to D(a)∈I oraz \(sD(a)-aD(s)\in I\), co pokazuje \(\widetilde D(a/s)\in S^{-1}I\). Na R/I istnieje derywacja \(\overline D\) z poprzedniego twierdzenia, a ponieważ \(\bar S\) jest zbiorem multiplikatywnym i 0∉\bar S (S∩I=∅), jej lokalizacja jest określona. Izomorfizm wysyła \((a/s)+S^{-1}I\) na \((a+I)/(s+I)\). Dwie reprezentacje mają zgodny obraz przez uniwersalną własność ilorazu i lokalizacji; analogicznie odwrotne odwzorowanie jest dane przez tę samą formułę w przeciwnym kierunku. W obu porządkach pochodna klasy a/s ma obraz \((sD(a)-aD(s)+I)/(s^2+I)\), co dowodzi zgodności derywacji. Koniec dowodu.

**Przykład.** R=Q[x,y], \(D=x\partial_x+2y\partial_y\), \(I=(y-x^2)\), \(S=\{1,x,x^2,\ldots\}\). Mamy \(D(y-x^2)=2(y-x^2)\in I\). Obydwa sposoby przejścia do ilorazu i lokalizacji dają Q[x,x^{-1}] z derywacją \(x\,d/dx\). Równość można sprawdzić na każdym ułamku P(x,y)/x^k po podstawieniu y=x².

## 5. Charakterystyka dodatnia i elementy nilpotentne

Niech p będzie liczbą pierwszą, R=F_p[x], D=d/dx. Ideał \(I=(x^p)\) jest D-stabilny, ponieważ dla każdego P∈R zachodzi \(D(x^pP)=x^pD(P)+p x^{p-1}P=x^pD(P)\in I\). Zatem D przechodzi na F_p[x]/(x^p), mimo obecności niezerowych elementów nilpotentnych.

Dla p=2 otrzymujemy R/I=F_2[ε]/(ε²) oraz \(\overline D(ε)=1\); rzeczywiście \(D(ε²)=2ε=0\). W charakterystyce 0 derywacja d/dx **nie** przechodzi na Q[x]/(x²), bo D(x²)=2x∉(x²). Kontrast ten dotyczy konkretnej derywacji, nie zakazu istnienia wszystkich innych derywacji na tym ilorazie.

## 6. Regresje, LaTeX i granice weryfikacji

Utworzono trwały test tools/tests/test_abstract_algebra_cross_aa09_12_43.py z **7 funkcjami**:
1. stabilność ideału (y−x²) i niezależność od reprezentantów;
2. jawne niepowodzenie przy ideałach niedopuszczających derywacji ilorazu;
3. formuła pochodnej w lokalizacji i równoważne reprezentacje ułamków;
4. zgodność derywacji przy zamianie kolejności ilorazu i lokalizacji;
5. ideały (x^p) dla p=2,3,5,7 oraz pełna kontrola 16 par elementów F_2[ε]/(ε²);
6. zachowanie D-stabilności po lokalizacji ideału (xy);
7. aktualna liczba 50 plików AA oraz podstawowe etykiety i odsyłacze w AA-09/12/43.

Testy rachunkowe używają dokładnej arytmetyki SymPy i małych pierścieni skończonych; nie są dowodem ogólnych twierdzeń. Brak automatycznego założenia, że wszystkie testy przeszły w CI.

**Commit utworzenia regresji:** 50e67c0ed7ed7222e689dbbf4a7c2d99b734ca3a. **Commit CI:** 00e7e546c17fa4dea58c459da70f9887f1a9d212, krok „Run AA-X31 differential ideals and localization checks” i nowy wyzwalacz. Cały workflow nadal sprawdza AA-01–AA-50.

**Werdykt po analizie matematycznej:** w opisanym interfejsie między rozdziałami nie znaleziono koniecznej korekty; AA-X31 **W STABILIZACJI CI**. Do zamknięcia potrzebne są wszystkie 7/7 testów w rzeczywistym logu, zielony pełny workflow, kompilacja AA-01–AA-50, automatyczna kontrola odsyłaczy i logu PDF. Osobna wizualna inspekcja stron nie została przeprowadzona.

**Propozycja opcjonalna (nie dodana automatycznie do źródeł):** po definicji rozszerzenia różniczkowego w AA-43 umieścić krótki podrozdział „Derywacje pierścieni, ideały różniczkowe i lokalizacje”, zawierający powyższe twierdzenia. Jest to rozbudowa treści zatwierdzonego rozdziału i wymaga osobnej zgody zgodnie z AGENTS.md.

**Następny etap:** stabilizacja AA-X31, a dopiero po jej zamknięciu niezależny AA-X32.


## Niezależny rachunek kontrolny (poza workflow)

Po dodaniu testów do GitHub wykonano osobną serię **560 dokładnych kontroli SymPy**, niezależną od pliku regresyjnego: 100 wybranych wielomianów w Q[x,y] sprawdzono pod kątem zgodności derywacji D=x∂_x+2y∂_y z podstawieniem y=x²; dla każdego wykonano cztery dodatkowe kontrole po lokalizacji przez x^k, k=1,2,3,4; ponadto sprawdzono D-stabilność (x^p) dla pochodnych 12 jednomianów przy p=2,3,5,7,11 (60 przypadków). **560/560 PASS**. Są to sprawdzenia przykładów, nie formalizacja ani dowód ogólnego twierdzenia. Wynik CI pozostaje oddzielną bramką, której status należy odczytać z rzeczywistego przebiegu.


## Pierwsze CI: wykryty błąd testu i rzeczywista poprawka

**Pierwszy przebieg:** [45284141975](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45284141975), SHA **00e7e546c17fa4dea58c459da70f9887f1a9d212**, wynik **completed / failure**, job **138075940293**. W kroku ogólnego odkrywania testów wykonano 4533 testy i otrzymano **4 błędy** w podprzypadkach nowej funkcji `test_stable_ideal_and_quotient_derivation` dla stałego wielomianu `P=1`. Przyczyną był wyłącznie błąd programu testowego: Python `int` nie ma metody `.subs`; nie była to błędna równość matematyczna. Wszystkie pozostałe sześć funkcji testowych nowego modułu miały wynik `ok`, lecz wydzielony krok AA-X31 oraz kompilacja pełnej książki nie zostały uruchomione z powodu wcześniejszego zakończenia jobu.

**Rzeczywista poprawka:** commit **8955f12205028cae869fceb0cbe3d92e197fafd8** zmienił podstawienie `P.subs(...)` na `sp.sympify(P).subs(...)`, tak aby stała `P=1` również była prawidłowym obiektem SymPy. Nie zmieniono źródeł LaTeX ani twierdzenia. Workflow został ponownie wyzwolony przez poprawkę pliku testowego, ale jego wynik wymaga dalszej weryfikacji. Wcześniejszy zielony CI AA-X30 nie jest dowodem poprawności AA-X31.

Diagnostyka globalnego repozytorium raportuje również wcześniejsze błędy brakujących zagnieżdżonych importów i rozbieżności kopii źródeł w *innych skryptach*; workflow ma dla niej `continue-on-error: true`. W odczytanym logu przyczyną przerwania kroku blokującego były wspomniane cztery błędy nowego testu. Dalszy werdykt AA-X31 pozostaje w stabilizacji.
