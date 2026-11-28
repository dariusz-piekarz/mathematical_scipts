# Teoria miary / Miara i całka — audyt XXXIX: rozdział 10, audyt II — stabilizacja

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (wyłącznie istniejąca).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/10-regularnosc-funkcji-mierzalnych-i-aproksymacja-funkcjami-ciaglymi.tex.  
**Niezmieniony blob R10 przed i po audycie:** 2a5db02f83ae41a6ebabe30547d47080a75004cd.  
**W tej iteracji nie zmieniano źródła R10, testów ani workflow.**

## 1. Wznowienie na rzeczywistym stanie repozytorium

Na początku audytu porównano istniejącą gałąź względem commitu poprzedniego raportu 26661af2c0ad70f152ae382ab2f0ed151b0b7f25: brak nowszych commitów, brak raportu XXXIX. Ponownie odczytano raport XXXVIII: audits/measure_theory/38-rozdzial-10-audyt-I-2026-11-23.md (blob fbdb201d8a90e06bb468b58411e620d596cbb80e). Dokumentuje on cztery poprawki matematyczno-redakcyjne, faktyczny przebieg CI 2/2 SUCCESS i status „R10 w stabilizacji”, prawidłowo nieogłoszony stabilnym w iteracji z modyfikacjami źródła.

Kontrolę przeprowadzono na **niezmienionym po poprawkach źródle R10**, z ponownym sprawdzeniem AGENTS.md, docs/pl/standardy_terminologiczne.md, testu tools/test_measure_theory_ch10.py, workflow .github/workflows/measure-theory-ch10.yml, preambuły books/pl/measure_theory.tex i raportu XXXVIII. Rozdziały R01–R09 oraz R12 odczytano wyłącznie jako kontekst definicji i celów odsyłaczy, **bez audytowania ani edycji** ich treści. Rozdziału 11 nie otwierano do audytu, nie zmieniano żadnych innych rozdziałów ani nie scalano skryptów.

## 2. Niezależny przegląd matematyczny: 16/16 dowodów

Źródło R10 po poprawkach liczy **742 wiersze, 9 sekcji, 5 twierdzeń, 5 lematów, 6 wniosków, 16 środowisk dowodu, 1 przykład, 6 uwag i 1 diagram TikZ**. Ponownie skontrolowano wszystkie istotne argumenty i warunki:

1. **Regularność miary:** zbiory zwarte K⊆A⊆O z miarą O\K mniejszą od ε; addytywność dla rozłącznych O\A i A\K, warunek λ_d(A)<∞ oraz możliwość ograniczenia otoczenia kompaktu.
2. **Konstrukcja gładkiej funkcji odcinającej:** funkcja płaska η(t)=e^{-1/t} dla t>0 i 0 dla t≤0, dodatniość mianownika we wszystkich punktach, wartość 1 na zamkniętej połowie promienia kuli, znikanie poza kulą, dodatniość i zwartość nośnika. Osobno sprawdzono przypadek pustego K.
3. **Aproksymacja funkcji charakterystycznej:** funkcje χ_A i ϑ zgadzają się na K i poza O, a na O\K ich różnica ma moduł ≤1. Błąd w L^p ogranicza λ_d(O\K), również przy p=1 i przy A=∅.
4. **Łuzin dla funkcji prostych:** po poprawce XXXVIII przypadek E=∅ jest obsługiwany bez dzielenia przez liczbę poziomic m=0; dla E≠∅ m>0. Zwarte K_j są parami rozłączne i jednocześnie otwarte i domknięte we względnej topologii ich skończonej sumy K.
5. **Twierdzenie Łuzina:** aproksymacja prostymi na E, zastosowanie twierdzenia Jegorowa przy λ_d(E)<∞, kompakt K_0 i kompaktowe poziomice ciągłości K_n; przecięcie jest zwarte, a budżet wyjątków ε/4+ε/4+ε/4 jest ściśle mniejszy od ε. Jednostajna granica ciągłych s_n|_K jest ciągła.
6. **Funkcje skończone prawie wszędzie:** jawne założenia śladu L_d|_E, measurability i zbioru E skończonej miary, usunięcie mierzalnego zbioru wartości ±∞, zastosowanie Łuzina do E\N i otrzymanie funkcji rzeczywistej ciągłej na K.
7. **Jednoczesny Łuzin dla rodziny przeliczalnej:** suma tolerancji ε2^{-(j+1)}<ε; przecięcie wszystkich kompaktów jest domkniętym podzbiorem K_1, a każde ograniczenie pozostaje ciągłe.
8. **Przybliżenie Lipschitzowskie:** inf-splot U_L(x)=inf_{y∈K}(h(y)+L|x−y|) jest L-Lipschitzowski; przy L>2M/δ uzyskuje się |H−h|<ε na K. Obcięcie do [-M,M] nie powiększa błędu ani stałej Lipschitza.
9. **Przedłużenie funkcji ciągłej z kompaktu:** rekurencja z resztami M_{n+1}≤M_n/2 zapewnia jednostajną zbieżność szeregu na całej przestrzeni. Na K suma zgadza się z h; końcowe obcięcie zachowuje tę własność i ograniczenie normy. Dla K=∅ jawnie wybrano H=0 i nie wyznacza się nieokreślonego rzeczywistego supremum pustego.
10. **Wersja Łuzina z przedłużeniem do całej przestrzeni:** zastosowanie Łuzina, a następnie przedłużenia f|_K z kompaktu; żadne dodatkowe założenie o ograniczoności f na E nie jest potrzebne.
11. **Przybliżanie w mierze funkcjami C_c:** najpierw duży kompakt K, potem ograniczone otoczenie O o λ_d(O\K)<ε/2, gładki cutoff wsparty w O i funkcja ϕ=ϑH. Obszar rozbieżności zawarty w (E\K)∪(O\K), bez błędnego wymogu O⊇E.
12. **Wygładzanie przez splot:** istnienie nieujemnej, niezerowej funkcji ρ∈C_c^∞ z nośnikiem w B(0,1), normalizacja całki, gładkość po różniczkowaniu pod całką, zwartość nośnika h_t oraz jednostajna zbieżność wynikająca z jednostajnej ciągłości h∈C_c.
13. **Gładka aproksymacja w mierze:** niezależnie sformułowane hipotezy E, f i przedłużenia \widetilde f; dokładny dobór progu δ/2 i nierówność trójkąta dla zbiorów przekroczeń.
14. **Gęstość C_c^∞ w L^p:** ucięcie wartości i nośnika, dominacja |f−f_{R,M}|^p≤2^p|f|^p, kwantyzacja także liczb ujemnych, gładkie aproksymacje wszystkich mierzalnych poziomic skończonej miary oraz końcowe oszacowanie z p≥1. Argument nie odwołuje się do nieudowodnionej jeszcze nierówności Minkowskiego.
15. **Prawie wszędzie gładkie przybliżenie dowolnej funkcji rzeczywistej mierzalnej:** przybliżanie na kulach B_n, błędy >1/n na zbiorach o miarach <2^{-n}, pierwsza część lematu Borela–Cantellego i fakt, że każdy punkt należy do B_n dla dostatecznie dużego n.
16. **Borelowski przedstawiciel:** zbiór D, na którym ciąg funkcji gładkich zbiega do skończonej wartości, jest borelowski dzięki kryterium Cauchy'ego; granica na D przedłużona zerem poza D jest borelowska i równa f prawie wszędzie.

**Werdykt matematyczny: 16/16 PASS**, a także **1/1 przykładu i 6/6 uwag — bez nowych wykazanych usterek**. Sprawdzono w szczególności przykład braku gęstości funkcji ciągłych w normie L^∞: użycie ścisłej granicy błędu q<1/2 pozwala otrzymać sprzeczność przez ciągłość w zerze.

## 3. Nowe, rzeczywiście wykonane niezależne regresje

Uruchomiono osobny lokalny skrypt **/mnt/data/r10_audit39_independent.py**, nieimportujący testów repozytoryjnych:

- **55296/55296 PASS:** wielowartościowa dokładna nierówność |χ_A−ϑ|^p≤χ_{O\K} na skończonych przestrzeniach z wagami nieujemnymi, dla K⊆A⊆O i p=1,2,3,4;
- **6875/6875 PASS:** dokładna inf-obwiednia Lipschitzowska na trzech punktach z różnymi danymi h, obcięcie do [-M,M], równość na K i oszacowania Lipschitzowskie na siatce;
- **267/267 PASS:** dokładne sumy tolerancji wyjątków w dowodzie Łuzina i przeliczalnej wersji wniosku;
- **1503/1503 PASS:** numeryczne przypadki gładkiej funkcji radialnej, wartości 1 na mniejszej kuli i 0 na zewnątrz większej, przy dodatnim mianowniku;
- **PASS:** osobno przypadki E=∅, K=∅ i pusta suma.

Regresje skończone stanowią **dodatkowy test**, nie zastępują dowodów ogólnych na dowolnych przestrzeniach z miarą.

## 4. Ponowna kontrola LaTeX, odsyłaczy i terminologii

Pobrano aktualne źródła R01–R10 oraz etykiety R12 jako **wyłącznie kontekst** odsyłacza do przyszłego rozdziału o produktach miar. Automatyczna niezależna kontrola wykazała:

- **24 etykiety R10, 21 odsyłaczy — wszystkie 21 rozwiązane**;
- **0 zduplikowanych etykiet** w kontekście R01–R10 i R12;
- **0 niezamkniętych środowisk i 0 błędnie dopasowanych \begin/\end**;
- brak terminów „sekwencji”, „unia zbiorów”, „zbieżność zdominowana”, „pierwszoprzeliczal”, „drugoprzeliczal”;
- konsekwentną konwencję **\chi_A** i brak zabronionych zastępczych oznaczeń funkcji charakterystycznych;
- utrzymanie wszystkich czterech poprawek z audytu XXXVIII.

Nie modyfikowano ani nie przemianowywano etykiet.

## 5. Niezależne oględziny prawdziwego PDF i potwierdzenie CI

W tej iteracji **otwarto i obejrzano każdą z siedmiu stron osobno w pełnym podglądzie**, nie tylko planszę kontaktową. Szczegółowo zweryfikowano diagram na stronie 2, ilustrujący K⊆A⊆O: trzy obszary są prawidłowo zagnieżdżone, etykiety K, A i O czytelne i bez kolizji. Na stronach 1 oraz 3–7 nie stwierdzono uciętych wzorów, nakładających się podpisów lub niedopasowania tekstu do ram strony.

Podstawą jest **rzeczywisty PDF** /mnt/data/measure_ch10_audit38/measure_theory_ch10_ci.pdf, pozyskany z artefaktu **14808807520**, a nie hipotetyczna kompilacja. Niezależny od Popplera odczyt lokalny PyMuPDF zweryfikował **7 stron, 3368 słów według własnej tokenizacji, 0 wyrazów wychodzących poza granice stron**. Poppler w workflow podał **4267 słów**, również wszystkie w granicach; różnica wynika ze sposobu wydzielania słów.

Ponownie sprawdzono GitHub Actions **[run 45157663182](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45157663182)** na commicie 1c89b0996a2ba3e095f899e0743f243a5cfdb45a: **2/2 joby completed SUCCESS**, odpowiednio testy regresyjne i kompilacja PDF. Workflow wykonał dwa przebiegi izolowanego LaTeX rozdziału i trzy przebiegi całej książki (257 stron), zweryfikował 7/7 podglądów oraz brak nierozwiązanych odsyłaczy i przepełnionych wierszy w pełnym dokumencie. Po tym commicie, mimo nowszych zmian innych projektów i raportu XXXVIII, ponowne porównanie gałęzi wykazało **0 zmian w źródle R10, jego teście i workflow oraz głównej książce**; wynik CI obowiązuje dla aktualnego źródła.

Z pobranych logów: izolowany R10 — **0 Overfull hbox, 0 Underfull hbox**, pojedyncza informacja o nierozwiązanych odsyłaczach międzyrozdziałowych (spodziewana przy samodzielnej kompilacji fragmentu); pełna książka — **0 Overfull hbox, 0 unresolved references, 14 globalnych nieblokujących Underfull hbox**.

## 6. Werdykt formalny

**ROZDZIAŁ 10 — STABILNY / FORMALNIE ZATWIERDZONY.**

R10 przeszedł audyt XXXVIII, w którym wykryto i poprawiono cztery nieścisłości, a potem pozytywnie zweryfikowano CI i PDF. Obecny **drugi, pełny, niezależny i czysty audyt XXXIX po ostatnich poprawkach** ponownie objął 16/16 dowodów, 1 przykład, 6 uwag, wszystkie hipotezy, dwie konwencje pustej przestrzeni, 21 odsyłaczy, terminologię, 7-stronicowy PDF i oba rzeczywiście udane zadania CI. **Nie znaleziono nowych błędów wymagających zmian źródłowych**, dlatego niniejsza iteracja nie edytowała rozdziału 10 ani nie resetowała stabilizacji.

**R01–R09 — STABILNE**, nieedytowane i nieaudytowane ponownie w tej iteracji. **R11–R31 — nietknięte**.

**Następna odrębna iteracja:** audyt globalny XL / R11 I („Całki zależne od parametru”). Rozdziału 11 nie rozpoczynano w bieżącym audycie.