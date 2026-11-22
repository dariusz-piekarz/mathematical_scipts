# Logika matematyczna i teoria mnogości — audyt II rozdziału 33

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Rozdział:** `chapters/pl/logic_and_set_theory/33-relacja-wymuszania-i-twierdzenie-o-wymuszaniu.tex`.  
**Przedmiot:** ponowna niezależna kontrola matematyczna relacji wymuszania, lematu prawdy, twierdzenia o wymuszaniu oraz konstrukcji zapewniających spełnianie ZFC przez rozszerzenie generyczne.

## Najważniejszy wynik: doprecyzowanie dowodu zastępowania

Pierwszy audyt nie zauważył dużego przeskoku w dowodzie schematu zastępowania. Wcześniej tekst przechodził od `minimalnej rangi` kandydatów $(q,\rho)$, przy czym $\rho$ przebiegał właściwą klasę nazw, bez wystarczającego uzasadnienia, że **jednoczesny wybór świadków** można wykonać za pomocą aksjomatu wyboru **wewnątrz $M$**.

W audycie II rzeczywiście poprawiono dowód, wyprowadzając po kolei:

1. `J` — zbiór par $(\sigma,t)\in A_\tau\times\mathbb P$, dla których istnieje kandydat; wyróżnianie w $M$ zapewnia $J\in M$.
2. Dla każdej pary z $J$ istnieje najmniejsza dopuszczalna ranga $\alpha_{\sigma,t}$: bierzemy jednego istniejącego kandydata o randze $\beta$ i minimalizujemy po zbiorze liczb porządkowych nie większych niż $\beta$.
3. Zastępowanie w $M$, zastosowane do *zbioru* $J$, daje zbiór rang $\{\alpha_{\sigma,t}:(\sigma,t)\in J\}$ i wspólne ograniczenie porządkowe $\gamma$.
4. Wszystkie potrzebne kandydatury minimalnej rangi można teraz rozpatrywać w **jednym zbiorze** $\mathbb P\times N_{\gamma+1}^M$. Dopiero w nim stosuje się aksjomat wyboru do niepustych zbiorów kandydatów odpowiadających parom z $J$.
5. Zastępowanie buduje nazwę $R=\{(\rho_{\sigma,t},q_{\sigma,t}):(\sigma,t)\in J\}\in M$, a ograniczenie rang gwarantuje, że rzeczywiście jest nazwą.

Następna część oryginalnego dowodu: gęstość wybranych warunków poniżej $p\in G$, lokalna generyczność i jednoznaczność wartości z formuły $\chi$, pozostała poprawna i nie wymagała zmiany. Wprowadzona poprawka usuwa `niejawny wybór z klasy właściwej`.

## Pozostałe dwie poprawki

**Nazwa sumy.** Doprecyzowano, że pierwszy krok konstruuje zbiór $B_\tau$ wszystkich pierwszych współrzędnych par z nazw składowych $\tau$ przez sumę i zastępowanie w $M$; następnie nazwa $U_\tau$ powstaje **przez wyróżnianie z $B_\tau\times\mathbb P\in M$**. Uzasadniono ponownie wspólne ograniczenie rang. W szczególności nie używa się nieograniczonej operacji rozdzielenia na klasie wszystkich nazw.

**Aksjomat wyboru.** Rozszerzono wyjaśnienie nazwy $\dot f$ w postaci grafu funkcji $f:\kappa\to M[G]$: ponieważ $1_{\mathbb P}\in G$, dla każdego $\xi<\kappa$ para $\bigl(\check\xi,e(\xi)\bigr)$ rzeczywiście występuje w interpretacji; stąd $f(\xi)=e(\xi)^G$. Surjektywność $e:\kappa\to A_\tau$ zapewnia, że każdy element $a=\tau^G$ ma przeciwobraz przez $f$; nie zakłada się, że $f$ ma wartości wyłącznie w $a$. Poprzez wybór **najmniejszego** indeksu i wcześniej wykazane wyróżnianie oraz zastępowanie otrzymujemy dobre uporządkowanie $a$.

## Ponownie skontrolowane argumenty bez wykrytych błędów

- **Klauzule atomowe.** Wymuszanie przynależności i równości jest definiowane jednoczesną rekurencją po naturalnej sumie rang nazw. Zależności rekurencyjne zmniejszają co najmniej jeden argument; porządek jest dobrze ufundowany.
- **Monotoniczność i regularność.** Definicje negacji i egzystencji używają odpowiednio braku silniejszego wymuszenia i lokalnej gęstości nazwanych świadków. W klauzulach nie zamienia się kierunków porządku.
- **Lemat definiowalności.** Dotyczy każdej *ustalonej* formuły, nie jednego wewnętrznego predykatu prawdy. Używa rekurencji na zbiorze nazw dziedzicznie występujących w argumentach, później zwykłej indukcji po składni.
- **Lemat prawdy.** Sprawdzono oba kierunki przynależności i równości. Dla $\sigma^G=\tau^G$ gęsty definiowalny zbiór $E$ wykrywa wszystkie ewentualne świadectwa niewymuszania równości. Pozostałe przypadki indukcji wykorzystują zbiór rozstrzygnięć i lokalną generyczność.
- **ZFC w $M[G]$.** Skontrolowano zbiór potęgowy przez ograniczenie nazw do $T=A_\tau\times\mathbb P$, schemat wyróżniania, sumę, podstawowe aksjomaty i minimalność rozszerzenia. Wyróżnianie i zastępowanie są wykazane przed użyciem ich w dowodzie aksjomatu wyboru.
- **Granice metamatematyczne.** W rozdziale nie wnioskuje się, że samo $\operatorname{Con}(\mathrm{ZFC})$ zapewnia przeliczalny tranzytywny model ZFC; także dowód CH/negacji CH wymaga osobnych rozdziałów.

## Regresje i kompilacja

- Rozdział zachowuje **25 etykiet, 26 odsyłaczy, 4 definicje, 6 lematów, 6 twierdzeń, 3 przykłady, 5 uwag i 12 dowodów**.
- Testy regresyjne w `tools/tests/test_logic_and_set_theory_ch33.py` rozszerzono z **11 do 14**: dodano sprawdzanie wartości nazwy sumy na dwóch gałęziach skończonego wymuszania, konstrukcję $\theta_\rho$ dla wszystkich ośmiu nazw zbudowanych z nazwy pustej i trzech warunków w prostym modelu i kontrolę argumentu ograniczania rang w schemacie zastępowania.
- Pierwsze dwie próby CI po korekcie dowodu nie powiodły się **wyłącznie z powodu nieaktualnej asercji tekstowej w teście** (`najmniejszą rangę` zamiast `\emph{najmniejsza ranga}`). Dostosowano asercję do poprawionego dowodu; nowa wersja nie usuwa matematycznych kontroli.
- [GitHub Actions #45020300332](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020300332): **SUCCESS**, po poprawkach matematycznych i aktualizacji testów. Wszystkie 14 testów rozdziału 33 oraz pozostałe testy rozdziałów 1–32 przeszły. Struktura i inwentarz: **828 etykiet i 616 odsyłaczy**, bez nierozwiązanych odsyłaczy.
- [GitHub Actions #45020385031](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45020385031): **SUCCESS**, dodatkowo po zapisaniu niniejszego raportu audytu II.
- **Kontrola PDF:** pełna książka liczy **288 stron**; rozdział 33 zajmuje strony PDF **281–288** (drukowane strony 272–279). Wszystkie osiem stron wyrenderowano i obejrzano; równości, wzory, nagłówki, odstępy i przyporządkowanie tekstu są czytelne. Nie stwierdzono nachodzenia napisów na wzory ani uciętego tekstu.
- **Log LaTeX:** 0 błędów, 0 niezdefiniowanych odsyłaczy, 0 ostrzeżeń o niezdefiniowanych cytowaniach, 0 `Overfull \\hbox`; 1 `Underfull \\hbox` w całej książce.

## Werdykt po audycie II

**Audyt II znalazł istotną lukę uzasadnienia zbiorowego w dowodzie zastępowania i dwie inne nieścisłości argumentacyjne; poprawiono wszystkie trzy.** Wersja po poprawkach ma **PASS** testów regresyjnych, pełnej kompilacji CI i wizualnego audytu ośmiu stron PDF. Z tego powodu rozdział pozostaje **poprawiony po audycie II, lecz jeszcze nie ostatecznie stabilny matematycznie**. Kolejny krok to niezależny **audyt III**, przy szczególnej uwadze na rangę nazw i schematy aksjomatów ZFC. Testy Python i kompilacja LaTeX nie zastępują formalnej weryfikacji matematycznej.
