# Analiza funkcjonalna — 15A/04 — pierwszy czysty audyt po poprawce

**Data:** 24 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/15A-calkowanie-funkcji-w-przestrzeniach-lokalnie-wypuklych.tex`.  
**SHA źródła:** `afe39ee7e7d189d2d15bbf4a81457cc57c63be7a`.  
**SHA regresji:** `6f44e390ea07e2e5593c8a0a246fd4060355f727`.  
**Werdykt matematyczno-redakcyjny:** **CZYSTY, pierwszy z dwóch wymaganych (1/2)** po poprawkowym audycie 15A/03; źródła i testów nie zmieniano.

## Weryfikacja stanu wejściowego

Odczytano bieżące źródło i test, raporty 15A/01–03 oraz rzeczywisty plik główny `books/pl/functional_analysis.tex`. SHA źródła i testu nie zmieniły się od audytu poprawkowego 15A/03. Wcześniejszy dedykowany przebieg [#45291010134](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45291010134) na commicie `d77b73db592a63620a23bdc9f43762d15555c5ce` ma status **completed/success**; dotyczy aktualnych blobów źródła i testów. Drugi przebieg po zapisie niniejszego raportu wymaga osobnego potwierdzenia, ponieważ zielone CI nie zastępuje drugiego niezależnego audytu matematycznego.

## Kontrola wszystkich dziesięciu dowodów

1. **Istnienie sum Riemanna.** Dla ciągłej f na zwartym [a,b] moduł `omega_p(r)` dąży do zera dla każdej seminormy, zaś wspólne rozdrobnienie daje `p(S_P-S_Q) <= 2(b-a)omega_p(r)`. Zupełność ciągowa jest zastosowana tylko do wybranego ciągu podziałów dyadycznych; nierówność przenosi limit na wszystkie sumy, także bez metryzowalności E. Zbieżność jest w topologii E, nie wyłącznie po funkcjonałach.
2. **Liniowość i nierówności seminormowe.** Liniowość otrzymujemy z sum, ciągłość seminorm daje `p(int f) <= int p(f)`. Własność addytywności na [a,c] i [c,b] wymaga istnienia każdej z tych całek, co źródło po 15A/01 jawnie formułuje; bez tego warunku w przestrzeniach niezupełnych implikacja jest fałszywa.
3. **Przemienność z ciągłym operatorem.** Dokładna równość sum `S(Tf,P)=T(S(f,P))` i ciągłość T nie wymagają zupełności F. Funkcjonały ciągłe rozdzielają punkty lokalnie wypukłej przestrzeni Hausdorffa; po scałkowaniu wartości skalarne określają jednoznacznie wektor.
4. **Środek ciężkości.** Normalizacja każdej sumy przez dodatnie b-a tworzy kombinację wypukłą wartości f; granica należy do domkniętej otoczki wypukłej, bez zakładania jej zwartości.
5. **Całka w uzupełnieniu.** Kanoniczne zanurzenie topologiczne `j:E->Ehat` zachowuje sumy. Istnienie granicy w `j(E)` jest równoważne zbieżności oryginalnych sum w E.
6. **Całka niewłaściwa.** W każdej seminormie ogon jest oszacowany ogonem skalarnej całki `int p(f)`, co daje ciąg Cauchy'ego `int_a^{a+n} f`; jego granica istnieje dzięki zupełności ciągowej. Kontrola wszystkich rzeczywistych R dowodzi pełnej granicy.
7. **Podstawowe twierdzenie rachunku.** Dla ilorazu różnicowego pierwotnej nierówność `p(h^{-1}int_x^{x+h}(f(t)-f(x))dt)<=sup p(f(t)-f(x))` pozostaje poprawna przy h<0 po odwróceniu orientacji. Tożsamość `G(b)-G(a)=int G'` można uzasadnić po wszystkich `ell in E'`, ponieważ pochodna jest ciągła, a E' rozdziela punkty.
8. **Całka zależna od parametru.** Dla ustalonej ciągłej seminormy p wzór na różnicę ilorazu i pochodnej wynika z oszacowań skalarnych po odpowiednich funkcjonałach zdominowanych przez p (Hahn–Banach). Jednostajna ciągłość `partial_s f` na zwartym prostokącie zapewnia przejście do granicy jednostajnie po t. Nie jest potrzebne wektorowe twierdzenie o wartości średniej.
9. **Twierdzenie Fubiniego.** Funkcje całek wewnętrznych są ciągłe w parametrach; wspólna podwójna suma Riemanna aproksymuje obie kolejności z kontrolą przez moduły ciągłości względem odpowiednich zmiennych. Granice są równe dzięki hausdorffowskości E.
10. **Silna całka rodziny operatorów.** Punktowa ciągłość t↦T(t)x na zwartym odcinku daje ograniczenie `sup_t ||T(t)x||`; Banach–Steinhaus zapewnia skończone `M=sup_t||T(t)||`. Wektorowa całka w Y istnieje, jest liniowa i ma normę operatorową co najwyżej `(b-a)M`. Tekst prawidłowo nie wnioskuje o normowej ciągłości t↦T(t).

**Wynik: 10/10 dowodów przejrzanych; brak nowych luk lub fałszywych hipotez.**

## Cztery przykłady i przypadki graniczne

- **Niezupełne `c_{00}`.** Składniki krzywej są osadzone na rozłącznych podprzedziałach, amplitudy maleją jak `2^{-n}`, więc krzywa jest ciągła także w t=0. Każda współrzędna całki w `ell^2` jest dodatnia (`2^{-2n-1}int eta`), zatem całka nie należy do `c_{00}`. Po odbiciu ujemnym na [1,2] całka całej krzywej jest zerem w `c_{00}`, choć połowa nie ma całki; ten przypadek rzeczywiście uzasadnia precyzyjny warunek addytywności.
- **`C^infty(Omega)`.** Kompletność, ciągłość różniczkowania i ewaluacji zapewniają przemienność pochodnych z całkowaniem wektorowym. Nie jest tu potrzebne nieuprawnione zastosowanie całki Bochnera.
- **Przestrzeń Schwartza.** Seminormy `q_{m,k}` kontrolują każdą pochodną przez `q_{m,k+|alpha|}` i zachowują oszacowanie pod całką. Ciągłość krzywej jest założona w topologii przestrzeni Schwartza, nie tylko punktowo.
- **Modulacja na `L^2`.** Po korekcie z audytu 15A/03 jawnie `H=L^2(R,lambda_1;C)`. Operator `U_t` jest zespolono-liniowy i unitarny, ciągłość silna wynika ze zbieżności zmajoryzowanej; `||U_t-I||=2` dla każdego t≠0 wynika z supremum istotnego ciągłego mnożnika. Próby w teście numerycznym jedynie kontrolują wzór w wybranych punktach, nie stanowią dowodu równości supremum istotnego.

**Wynik: 4/4 przykłady poprawne, w tym przypadki graniczne.**

## Redakcja, LaTeX i kontrole techniczne

Bezpośrednia analiza źródła: **443 wiersze, 16 etykiet, 8 wystąpień odsyłaczy** (`ref`/`hyperref`). Zliczono sparowane środowiska: `twierdzenie` 7/7, `stwierdzenie` 2/2, `wniosek` 1/1, `definicja` 1/1, `przyklad` 4/4, `uwaga` 2/2, `proof` 10/10. Moduł nie zawiera rysunków TikZ. Istniejący główny plik książki zawiera moduły **15A i 15B przed 16 i 17**; odniesienia 15A do rozdziałów 14, 16, 17 oraz 15B mają istniejące cele. Nie wprowadzano nowych definicji ani zmian w rozdziałach stabilnych.

Zapis [GitHub Actions #45291010134](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45291010134) potwierdza zielony przebieg dla tej samej wersji. W audycie 15A/03 zweryfikowano artefakt PDF **109 stron A4**, w tym poprawioną stronę 95 z jawnie zespolonym `L^2`; nie stwierdzono błędów składu w 15A. Ostrzeżenie `Underfull \hbox` z rozdziału 16 pozostaje do przeglądu przy rozdziale 16.

## Decyzja

**Audyt 15A/04: CZYSTY, 1/2 na niezmienionej po poprawce wersji źródła i testu.** Wymagany jeszcze osobny **15A/05** z drugim niezależnym czystym przeglądem, zielonym CI i walidacją gotowego PDF. Do tego momentu moduł 15A pozostaje **NIESTABILNY**, a audyt 15B nie jest odblokowany.
