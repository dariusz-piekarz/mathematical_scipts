# Analiza funkcjonalna — rozdział 05 — audyt 02 (niezależna kontrola)

**Data:** 23 listopada 2026 r.
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Źródło:** `chapters/pl/functional_analysis/05-przestrzenie-lokalnie-wypukle-i-seminormy.tex`.
**SHA źródła:** `8f2a545cccf5e47395ded3d8f321e1574c916ce9`.
**Werdykt:** **CZYSTY 05/02; 1/2 czystych audytów po ostatniej poprawce. Rozdział 05 NIESTABILNY.**

## Weryfikacja punktu startowego

Na aktualnej gałęzi istnieją raporty 01–03 dla rozdziałów 01–04; rozdział 04 jest stabilny (raport `04-audyt-3.md`). Najnowszy raport rozdziału 05 przed niniejszą iteracją to `05-audyt-1.md`, dokumentujący poprawki źródła, 13 dowodów, 5 przykładów i końcowy CI. Nie powtarzano audytu rozdziału 01.

Odczytano również pełny aktualny plik AA/FA-05, test `tools/tests/test_functional_analysis_ch05.py` i workflow `.github/workflows/functional-analysis-ch05.yml`.

## Niezależna kontrola wszystkich 13 dowodów

1. **Absolutna wypukłość:** przypadek zerowych współczynników rozpatrzony osobno, dla niezerowych normalizacja przez sumę modułów i zrównoważenie są poprawne.
2. **Baza absolutnie wypukłych otoczeń:** otoczka wypukła otwartego zrównoważonego O pozostaje w wypukłym V; otwartość wynika z perturbacji jednego składnika o dodatniej wadze. Brak błędnego użycia zawierania `conv(O)+O⊂conv(O)`.
3. **Topologia seminorm:** skończone przecięcia i zmniejszanie promieni, ciągłość działań, minimalność oraz warunek Hausdorffa przez wspólne jądro; bez dodatkowych ukrytych założeń.
4. **Funkcjonał Minkowskiego:** przy A pochłaniającym i absolutnie wypukłym otrzymuje się seminormę; dla otwartego A zachodzi dokładnie `A={p_A<1}`; nie stwierdza się, że zawsze jest normą.
5. **Charakteryzacja lokalnej wypukłości:** funkcjonały Minkowskiego otwartych absolutnie wypukłych otoczeń generują wyjściową topologię; Hausdorff zapewnia rozdzielanie punktów.
6. **Ciągłość operatora:** przypadek zerowego maksimum seminorm wymaga skalowania przez dowolne t>0 i został obsłużony; dla dodatniego maksimum stała 2/δ jest prawidłowa.
7. **Ograniczoność przez seminormy:** oba kierunki, wspólna kontrola skończonej liczby seminorm i konwencja dla zbioru pustego są poprawne.
8. **Otoczki ograniczone:** podaddytywność i jednorodność seminorm dają kontrolę wszystkich skończonych kombinacji absolutnie wypukłych.
9. **Normowalność Kolmogorowa:** ograniczone otoczenie i lokalna wypukłość dają otwarte absolutnie wypukłe ograniczone U; argument `p_U(x)=0 => x∈sU` dla każdego s>0 wraz z Hausdorffem daje dodatnią określoność, homotetie U generują topologię.
10. **Metryzowalność:** `min(1,p_n)` jest podaddytywne; suma dyadyczna rozdziela punkty, ogon szeregu jest jednostajnie mały, a przeliczalna baza daje przeliczalną rodzinę seminorm.
11. **Kryterium Cauchy'ego:** przejście od pojedynczych seminorm do skończonego maksimum korzysta z kierowania zbioru indeksów; oba kierunki są poprawne.
12. **Zupełność C∞([0,1]):** granice jednostajne pochodnych i podstawowe twierdzenie rachunku całkowego dają `g_j'=g_{j+1}`; metryzowalność pozwala z zupełności ciągowej wywnioskować zupełność.
13. **Podprzestrzenie, produkty, ilorazy:** wypukłość zachowana przez przecięcie, produkt i otwarte liniowe odwzorowanie ilorazowe; Hausdorff ilorazu równoważny domkniętości M.

**Wynik kontroli dowodów: 13/13 bez wykrytej usterki** (kontrola tekstu i argumentów; nie jest to wynik testów automatycznych).

## Pięć przykładów i przypadki brzegowe

1. Seminormy współrzędnych, pochodnych i supremum na zbiorach zwartych — poprawne.
2. Pasek w R²: `p_A(x,y)=|x|`, więc brak dodatniej określoności — poprawne.
3. `c_00`: `p_A(x)=sup n|x_n|` nie jest ciągły w normie supremum, bo `e_n/n→0` — poprawne.
4. Produkt K^N: zupełny, metryzowalny, lokalnie wypukły i nienormowalny — poprawne.
5. C∞([0,1]): dla N≥2π sinusoidy o amplitudzie δ/(2N^m) mają `p_m≤δ/2` i `p_{m+1}=δN/2`, co wyklucza ograniczone otoczenie — poprawne.

**Wynik przykładów: 5/5 bez wykrytej usterki.** Dodatkowo sprawdzono argument dla 0<p<1 i nieatomowej miary: oszacowanie `n^(1-1/p)→0` jest prawidłowe.

## Struktura, odsyłacze i walidacja

Źródło ma **13** środowisk `proof`, **5** środowisk `przyklad`, **19** etykiet. Dedykowany test zawiera 12 metod kontrolujących m.in. etykiety i odsyłacze do rozdziałów 01–05. Nie wykryto sprzeczności z przyjętą terminologią „zupełność ciągowa”, „przestrzeń sprzężona” i oznaczeniem `\\chi_A`.

**Zweryfikowany historyczny CI:** [GitHub Actions 45160591150](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160591150), `completed/success`, head SHA `51ca83764f44bcdc0fce6cfbfbddd15cd4eec84a`, aktualizacja 23.11.2026 10:57:53 UTC. Raport 05/01 dokumentuje w tym przebiegu 12/12 testów, kompilację PDF i wizualną inspekcję stron 27–33. W **tej** iteracji nie uruchomiono nowego CI, nie pobrano ani nie obejrzano ponownie PDF; nie przypisuje się nowego PASS dla tych operacji.

## Decyzja

**05/02 CZYSTY, pierwszy z dwóch kolejnych czystych audytów.** Nie zmieniono źródła ani testów; nie resetowano licznika. Następny krok: niezależny audyt **05/03** na tym samym źródle, ponowne potwierdzenie stanu CI i wizualnego PDF. Dopiero po drugim czystym audycie można uznać rozdział 05 za stabilny i otworzyć 06.
