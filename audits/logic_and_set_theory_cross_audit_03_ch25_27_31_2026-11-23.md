# Logika matematyczna i teoria mnogości — audyt przekrojowy 03 (rozdziały 25, 27 i 31)

**Data:** 23 listopada 2026 r. (Europe/Warsaw).  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Zakres:** niezależne sprawdzenie dowodów; pełny diff plików przed i po korektach nagłówków, kontrola środowisk i odsyłaczy oraz rzeczywiste CI.

## 1. Kontrola pełnego diffu (4217 wierszy)

Pobrano aktualne źródła i te same ścieżki według commitu 450775573e71c504b466320fd26e9469003c037e. Porównanie każdego wiersza wykazało:

| Rozdział | Blob po korekcie | Wiersze | Jedyne zmiany |
|---|---|---:|---|
| 25 | 19c0e18ad9ced232d7346dc19302e7ab8507e2fb | 994 | nagłówek w wierszu 516 |
| 27 | e70779db56c87addcaf47d6e8e0bdec9b0a6a9d5 | 686 | nagłówek w wierszu 426 |
| 31 | 03dae2a901f115eacdff67058f96717f3323e4f8 | 2537 | nagłówki w wierszach 218, 239, 340, 540 |

Łącznie zmodyfikowano dokładnie 6/4217 wierszy. Wszystkie zmiany polegają na dopisaniu \texorpdfstring do tytułów sekcji, aby zakładki PDF miały tekstowe oznaczenia omega, N, R i L. W każdym pierwszym argumencie zachowano oryginalny wzór LaTeX, widoczny na stronie. Wszystkie twierdzenia, dowody, etykiety i odsyłacze pozostały identyczne.

## 2. Niezależny audyt I — kontrola matematyczna

### Rozdział 25: ZF, rekurencja, arytmetyka

- Rekursja na liczbach naturalnych (wiersze 518–580): dla każdego n tworzy się jedno n-przybliżenie na S(n), zaczynając od n=0. Dodatkowa para w kroku następnika dotyczy nowego argumentu S(n), który nie należy do S(n). Wykres funkcji globalnej powstaje przez jednoznacznie definiowalne przyporządkowanie i schemat zastępowania; nie jest potrzebny AC.
- Dobry porządek liczb naturalnych (827–863): relacja arytmetyczna jest porównana z przynależnością dopiero po osobnym dowodzie równoważności m<n ⇔ m∈n. Istnienie minimum niepustego podzbioru omega opiera się na ufundowaniu i liniowości.
- Dzielenie z resztą (920–961): gdy a<b, para (0,a) działa także przy a=0. W przypadku b≤a liczba t z a=b+t spełnia t<a, zatem indukcja silna stosuje się poprawnie. Przy q<q' nierówności a≥bq+b i a<bq+b wykluczają dwa rozkłady. Warunek b≠0 jest jawny.
- Schematy separacji i zastępowania są rozróżnione; nie stosuje się nieograniczonej komprehensji.

### Rozdział 27: moc zbiorów w ZF

- Cantor–Bernstein (48–77): w konstrukcji C zachodzi C=A0∪g[f[C]]. Weryfikacja rozłączności obrazów dwóch części odwzorowania i surjektywności obejmuje również przypadki pustych zbiorów; nie stosuje AC.
- Przeliczalność par (251–337): odcinki wyznaczone przez liczby trójkątne są kolejne, bez luk; enumeracja nieskończonego podzbioru omega wybiera jednoznaczne minima. Totalizacja funkcji przejścia usuwa problem niepełnej funkcji rekurencyjnej.
- Moc kontinuum i diagonalizacja (376–486): pierwsza różna cyfra kodu trójkowego dominuje ogon, dając iniektywność. Kodowanie wymiernych przez zredukowane ułamki i parowanie Cantora daje iniekcję Q→omega bez wyboru. Zastępowanie tworzy funkcję n↦S_n, bo jej wartości są jednoznaczne.
- Porównywalność mocy ⇔ AC (633–673): kierunek wstecz wykorzystuje Hartogsa H(A), dla którego H(A)→A iniektywnie nie istnieje; więc z hipotezy porównywalności otrzymuje się iniekcję A→H(A), a wraz z nią dobry porządek A.

### Rozdział 31: uniwersum L, kondensacja i GCH

- Def(M) (5–54): spełnianie odnosi się do zbiorowej struktury M; przypadek M=pusty potraktowany jest osobno. Nie ma nieuprawnionego zbiorowego predykatu prawdy dla klasy L.
- Odbicie skończonej rodziny formuł (246–338): minimalne etapy pojawienia się świadków są jednoznacznie wyznaczonymi liczbami porządkowymi. Wspólne ograniczenie powstaje przez zastępowanie, bez AC/DC. Rodzina formuł jest domknięta na podformuły.
- ZF wewnątrz L (342–499): separacja i zastępowanie wykorzystują odbicie do zadanego skończonego zestawu formuł; wewnętrzny zbiór potęgowy P^L(a) odróżniono od zewnętrznego P(a).
- Kondensacja (1593–1773): w dowodzie głównym używa się ustalonego skończonego pakietu sigma_*, a po kolapsie jego prawdziwość jest zachowana przez elementarność i izomorfizm. W wariancie rozszerzonym (2111–2275) rozróżnia się zewnętrzne relacje R,S,D i definowalność wewnętrzną w L_theta.
- GCH w L (2290–2409): kadłub zawiera kappa jako element i wszystkie xi<kappa jako oddzielne elementy. Kolaps ustala więc każdy podzbiór A⊆kappa; z |X|=kappa wynika beta<kappa^+, a z A∈L_beta otrzymuje się oszacowanie mocy. Końcowy rachunek wykonano wewnątrz L, bez utożsamiania jego kolejnych liczb kardynalnych z zewnętrznymi.

**Werdykt audytu matematycznego I:** w skontrolowanych rozumowaniach nie wykryto błędu wymagającego korekty. Ich tekst jest identyczny z wersją przed naprawą zakładek.

## 3. Niezależny audyt II — kontrola strukturalna i odsyłacze

| Rozdział | Etykiety | Odsyłacze | Znaczniki begin/end | Niezgodności |
|---|---:|---:|---:|---:|
| 25 | 46 | 25 | 162 | 0 |
| 27 | 24 | 16 | 92 | 0 |
| 31 | 68 | 87 | 218 | 0 |
| Razem | 138 | 128 | 472 | 0 |

Nie ma powtórzonych etykiet wśród tych trzech rozdziałów. Dziewięć różnych zewnętrznych etykiet, do których prowadzą odsyłacze, zweryfikowano niezależnie, pobierając ich rzeczywiste definicje:
- rozdział 4: ch:relations;
- rozdział 23: thm:downward-ls;
- rozdział 24: thm:skolem-paradox;
- rozdział 26: ch:axiom-choice, thm:choice-wellorder, lem:choice-wellorder-comparison, thm:choice-hartogs, thm:choice-equivalence;
- rozdział 28: ch:ordinals.

Przed i po poprawkach identyczne są wszystkie listy etykiet, odsyłaczy i środowisk. Nie użyto niepoprawnego skrótu rzeczownikowego „kardynał” w tekstach; historyczne nazwy plików zachowano.

**Werdykt audytu II:** czysty.

## 4. Kontrola potwierdzająca (+1): CI i rzeczywisty PDF

- [CI 45083552034 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083552034): pełne regresje oraz kompilacja książki po ostatniej z sześciu zmian w nagłówkach.
- [CI terminologiczne 45083552112 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083552112).
- [CI aplikacji 45083552179 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083552179).
- [CI 45083709897 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083709897): przejście *dodatkowych asercji* zabraniających podwójnych kotwic i niedozwolonych tokenów w zakładkach PDF.

Log ostatniego przebiegu potwierdza zero ostrzeżeń o zdublowanych celach stron i zero ostrzeżeń hyperref o nieprawidłowych tokenach zakładek; książka ma 337 stron. [Audyt techniczny 02](logic_and_set_theory_global_audit_02_pdf_bookmarks_2026-11-23.md) dokumentuje osobną analizę rzeczywistych plików PDF z 338 zachowanymi zakładkami i identycznym wyglądem stron 11–337. W tej iteracji nie udaje się nowego renderowania; przytoczono rzeczywisty, wcześniejszy audyt wizualny.

## 5. Werdykt końcowy

**Rozdziały 25, 27 i 31: status stabilny ponownie potwierdzony.** Dwa odrębne czyste przeglądy (matematyczny i strukturalny) oraz weryfikacja techniczna (+1) potwierdzają brak regresji po zmianie wyłącznie nagłówków PDF. Nie zmieniono merytorycznej treści żadnego z trzech rozdziałów ani nie dodawano nowych tematów. Testy LaTeX i Python nie oznaczają formalnego sprawdzenia dowodów w Lean.

Opcjonalne dalsze przedsięwzięcie: systematyczna formalizacja wybranych zależności kondensacji/GCH w Lean wymaga oddzielnej decyzji i nie jest warunkiem uznania tego audytu za czysty.
