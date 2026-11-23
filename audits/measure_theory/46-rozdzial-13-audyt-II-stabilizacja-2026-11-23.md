# Miara i całka — audyt XLVI: rozdział 13, audyt II — niezależna stabilizacja

**Data:** 2026-11-23. **Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Jedyny audytowany rozdział:** chapters/pl/measure_theory/13-zamiana-zmiennych-w-calce-lebesguea.tex.  
**Niezmieniony blob źródła przed i po audycie:** 965c76951d267a60e1d7274a1431ac08ef2dd960.  
**Liczba zmian R13, jego testów oraz workflow w audycie XLVI:** **zero** — jest to niezależna kontrola po ostatnich poprawkach.

## 1. Rzeczywisty punkt wznowienia

Na początku porównano istniejącą gałąź z commitem **fc4c134d3306beb5e68a11cac84fdabcb571a97a**. Późniejsze commity dotyczyły innych skryptów i aplikacji, **bez zmian w R13**. Odczytano poprzedni raport audits/measure_theory/45-rozdzial-13-audyt-I-2026-11-23.md, blob **cf9b2b8b76b5e25c450b504a63a74e4c85d6f8ca**, wraz z uzupełnieniem. Raport XLV udokumentował usunięcie błędu dziedziny w dowodzie transformacji gęstości, poprawę gęstości kwadratu zmiennej jednostajnej, doprecyzowanie hipotez, wykonanie testów i zielony CI, ale prawidłowo pozostawił rozdział **w stabilizacji**, gdyż źródło było wówczas zmieniane. Raport XLVI nie istniał w chwili niniejszego audytu.

Odczytano R13, jego test i workflow, zasady AGENTS.md oraz docs/pl/standardy_terminologiczne.md. R01–R12 pobrano **wyłącznie jako kontekst źródeł definicji i celów odsyłaczy**. Nie prowadzono ich audytów ponownie i nie zmieniano żadnego innego rozdziału. Nie rozpoczęto R14 ani nie scalano materiałów.

## 2. Ponowny niezależny przegląd całych ośmiu dowodów

Aktualny R13 ma **556 wierszy, 8 sekcji, 4 twierdzenia, 3 lematy, 1 wniosek, 8 dowodów, 7 przykładów, 4 uwagi i 1 rysunek TikZ**. Ponownie skontrolowano kompletne rozumowania, ich założenia, przypadki zerowe i zależności logiczne:

1. **Całkowanie względem miary obrazowej:** równość dla $\chi_B$ wynika z definicji $T_\#\mu$. Liniowość daje ją dla nieujemnych funkcji prostych, Beppo Levi dla dowolnych mierzalnych $h\ge0$, a przypadek $h$ zespolonej całkowalnej przechodzi przez całkowalność $|h|\circ T$ i cztery nieujemne części. Nie jest potrzebna iniektywność $T$, topologia ani sigma-skończoność miary.
2. **Translacje, permutacje i ścinania:** translacje i permutacje zachowują Lebesgue'a-mierzalną objętość; w ścinaniu przekrój po zmiennej $x_j$ jest translacją o stałą zależną od pozostałych współrzędnych. Tonelli (zatwierdzony R12) i niezmienniczość $\lambda_1$ uzasadniają niezmienniczość $\lambda_d$. Wymienione po XLV indeksy $i\ne j$ i współczynnik $a\in\mathbb R$ są wystarczające.
3. **Odwzorowania lokalnie Lipschitzowskie zachowują zbiory zerowe:** zastosowano przeliczalne pokrycie otwartego $U$ przez domknięte sześciany w większych sześcianach, na których $F$ ma stałą Lipschitza. Dowolną część $N\cap Q_j$ można pokryć sześcianami zawartymi w odpowiednim obszarze Lipschitzowskości o dowolnie małej łącznej objętości; obrazy mają miary zewnętrzne ograniczone przez $C_dL_j^d\varepsilon$. Ich miara zewnętrzna jest zerowa, a zupełność miary Lebesgue'a zapewnia mierzalność. Argument działa także dla $U=\mathbb R^d$, bez odwołania do odległości od pustego brzegu.
4. **Liniowa zmiana objętości:** elementarne przekształcenia liniowe realizują permutacje, skalowanie jednej współrzędnej i ścinania. Ich wpływ na objętość jest dokładnie równy modułowi wyznacznika; eliminacja Gaussa oraz multiplikatywność wyznacznika obejmują każde $A\in\mathrm{GL}(d,\mathbb R)$. Obrazy i przeciwobrazy zerowych zbiorów przez $A$ oraz $A^{-1}$ mają miarę zero, co rozszerza wzór z borelowskich na dowolne zbiory Lebesgue'a-mierzalne.
5. **Deformacja małego sześcianu:** po normalizacji przez $A^{-1}$ funkcja $H(z)=z+R(z)$ ma pochodną identycznościową w $0$; $\delta(r)=\sup_{Q_r}\|DR\|\to0$. Otrzymano inkluzję górną $H(Q_r)\subset Q_{(1+\delta)r}$. Dla każdego $y\in Q_{(1-\delta)r}$ odwzorowanie $T_y(z)=y-R(z)$ jest zwężeniem $Q_r$ w siebie, więc twierdzenie Banacha daje dolną inkluzję. Mnożenie przez $A$ i wzór liniowy kończą oszacowanie bez błędnego koła. Jawne założenie $x_0\in U$ zostało utrzymane.
6. **Główne twierdzenie dla dyfeomorfizmu $C^1$:** miary $\tau(E)=\lambda_d(\Phi(E))$ i $\rho(E)=\int_E|\det D\Phi|\,\mathrm d\lambda_d$ są dobrze określone i sigma-skończone na zbiorach borelowskich $U$. Dla domkniętego sześcianu $Q\Subset U$ równość uzyskano przez podział na małe sześciany, kontrolę obrazów ich brzegów przez lemat Lipschitza, jednostajne oszacowania lokalne oraz sumy Riemanna ciągłego jakobianu. Rodzina półotwartych **sześcianów diadycznych z domknięciami zawartymi w $U$** jest układem typu $\pi$ generującym $\mathcal B(U)$. Poprawnie ograniczono obie miary do pojedynczego sześcianu $C$ o skończonych wartościach, zastosowano twierdzenie $\pi$–$\lambda$, a następnie rozłączne pokrycie $U$. Lokalna Lipschitzowskość $\Phi$ i $\Phi^{-1}$ rozszerza równość na Lebesgue'a-mierzalne zbiory. Równość całek dla $\chi_B$, funkcji prostych, nieujemnych i zespolonych całkowalnych wynika w ustalonej kolejności.
7. **Wniosek dla mierzalnego podzbioru:** przy jawnie zapisanych $U,V,\Phi,E$ i $g$, funkcja przedłużona zerem z $\Phi(E)$ na $V$ jest mierzalna, a twierdzenie o zamianie zmiennych daje równość odpowiednich całek. Dla funkcji zespolonych warunek całkowalności na $\Phi(E)$ jest wystarczający.
8. **Transformacja gęstości:** dla $\mu(E)=\int_Ew\,\mathrm d\lambda_d$, $w\ge0$, miara obrazowa spełnia $(\Phi_\#\mu)(B)=\int_{\Phi^{-1}(B)}w$. Poprawiony w XLV dowód prawidłowo stosuje zamianę zmiennych do **$\Phi^{-1}:V\to U$ i funkcji na $U$**
   $h(x)=\chi_{\Phi^{-1}(B)}(x)w(x)$, więc $h(\Phi^{-1}(y))=\chi_B(y)w(\Phi^{-1}(y))$. Całkowanie ma właściwe dziedziny; $0\cdot\infty$ jest określone jako zero i pozwala rozpatrywać wagi o wartościach rozszerzonych.

**Wynik matematyczny: 8/8 dowodów PASS.** W ponownym niezależnym przeglądzie nie wykryto nowego błędu wymagającego zmiany źródła. Poprawki z XLV są zachowane i nie naruszają innych argumentów.

## 3. Przykłady, uwagi i geometryczny diagram

**7/7 przykładów i 4/4 uwagi — PASS.** Przegląd obejmował miarę obrazową $x\mapsto x^2$ na $(0,1)$, biegunowe (jakobian $r$), walcowe (jakobian $r$), sferyczne (jakobian $r^2\sin\vartheta$), gęstość $Y=X^2$, dwukrotne liczenie dla nieiniektywnego $x^2:\mathbb R\to\mathbb R$ oraz istnienie homeomorfizmów osobliwych z pochodną zerową niemal wszędzie. Gęstość $Y$ jest obecnie prawidłowo zdefiniowana przez formułę przedziałową z zerem poza $(0,1)$, także przy $y\le0$; nie dzieli się tam przez nieokreślony pierwiastek. Wzory walcowe i sferyczne mają jawnie określone funkcje nieujemne mierzalne i zespolone funkcje całkowalne.

Uwagi o różnicy między miarą obrazową a jakobianem, wymiarze, jednostajnych oszacowaniach na zwartym zbiorze i roli orientacji są zgodne z twierdzeniami. Diagram ma czytelne oznaczenia $r,\theta,\Delta r,\Delta\theta$.

## 4. Nowe, niezależnie wykonane regresje

Utworzono i uruchomiono **lokalnie**, bez importowania testu repozytoryjnego, skrypt **/mnt/data/r13_audit46/independent_regression.py**. Zawiera dokładną arytmetykę wymierną i niezależne całkowanie numeryczne o wysokiej precyzji tam, gdzie jest pomocne:

- **32000/32000 PASS** — całki funkcji względem dyskretnej miary obrazowej nieiniektywnego odwzorowania czterech atomów na trzy atomy;
- **7936/7936 PASS** — zmiana pól przez moduł wyznacznika $2\times2$ dla **496** odwracalnych macierzy całkowitych i 16 wymiernych prostokątów każdej z nich;
- **100/100 PASS** — ścisłe ograniczenia objętości obrazu sześcianu przy dwuwymiarowym nieliniowym zaburzeniu $H(x,y)=(x+ax^2,y+by^2)$;
- **248/248 PASS** — funkcja $X^2$, dokładne prawdopodobieństwa przedziałów przez pierwotną gęstości oraz niezależne kwadratury 17 momentów;
- **30/30 PASS** — dwukrotne liczenie w przykładzie nieiniektywnego kwadratowania dla różnych funkcji $y^k\chi_{(0,1)}$;
- **125/125 PASS** — multiplikatywność wyznacznika dla złożeń trzech macierzy elementarnych;
- **29/29 PASS** — jakobiany biegunowe i objętości koła i kuli.

**Łącznie 40468/40468 PASS.** Regresje dotyczą konkretnych modeli i **nie są dowodem** twierdzenia dla dowolnego dyfeomorfizmu, które przejrzano osobno w punkcie 2.

## 5. Statyczna integralność R13 i odsyłaczy

Ponownie pobrano przez GitHub API źródła R01–R13 wyłącznie dla zidentyfikowania celów odsyłaczy R13. Wyniki:
- **556 wierszy, 16 etykiet i 14 użyć $\backslash$ref/$\backslash$eqref/$\backslash$pageref w R13**;
- **0 brakujących odsyłaczy** względem R01–R13, w tym zewnętrznego odsyłacza do thm:tonelli-12;
- **0 powtarzających się etykiet** w skontrolowanym kontekście;
- **0 niedopasowanych i 0 niezamkniętych środowisk** $\backslash$begin/$\backslash$end;
- brak samodzielnego zabronionego słowa „sekwencja” i niezgodnych oznaczeń funkcji charakterystycznych; stosowana jest $\chi_A$.

Niniejszy audyt **nie aktualizował ani źródła R13, ani testu tools/test_measure_theory_ch13.py, ani workflow**.

## 6. Rzeczywiste CI i niezależna kontrola PDF

Ponownie odczytano [GitHub Actions run 45178283970](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45178283970) na commicie 6509e3cdc05f47e9cbf741907eb89deb5fe021ea. Oba zadania mają status **completed SUCCESS (2/2)**: niezależny job testów oraz job kompilacji PDF i odsyłaczy. Porównanie aktualnej gałęzi z commitem runu wykazało **zero zmian** w R13, jego teście i workflow oraz w głównym pliku books/pl/measure_theory.tex. Wynik CI obejmuje zatem dokładnie wersję audytowaną tutaj.

W rzeczywistym CI: izolowany R13 **6 stron A4**, 2 kompilacje pdflatex, **3322 słowa Popplera w granicach stron, 6/6 podglądów PNG**; pełna książka — 3 kompilacje, **257 stron**, brak nierozwiązanych odsyłaczy. Artefakt **14819399246** jest dostępny i nieprzeterminowany. Oryginalny PDF tego artefaktu: /mnt/data/r13_audit45_final/measure_theory_ch13_ci.pdf.

Niezależnie od poprzedniej inspekcji ponownie wyrenderowano PDF do katalogu **/mnt/data/r13_audit46/pages/** (170 dpi). Obejrzano pełną planszę wszystkich **sześciu stron**, a powiększenia stron 4 (główny dowód z układem diadycznym), 5 (diagram biegunowy, wzory cylindryczne i sferyczne) i 6 (poprawiony dowód o gęstości) skontrolowano osobno. Diagram nie ma kolidujących oznaczeń, a wszystkie widoczne wzory i wiersze mieszczą się w szerokości kolumny. Również pozostałe strony nie wykazują usterek na planszy kontaktowej.

Niezależna analiza PyMuPDF: **6 stron, 2733 słowa według własnej segmentacji, 0 poza prostokątami stron**; inna liczba słów niż w Popplerze wynika z innej tokenizacji. Na podstawie autentycznych logów PDF wyodrębnionych z ZIP:
- izolowany R13: **0 Overfull hbox, 0 Underfull hbox**;
- pełna książka: **0 Overfull hbox, 0 nierozwiązanych odsyłaczy, 14 wcześniejszych globalnych nieblokujących Underfull hbox**.

Odsyłacz międzyrozdziałowy wyświetlany w izolowanym składzie jako „??” jest spodziewany; w pełnym skrypcie zostaje rozwiązany.

## 7. Formalna decyzja

**ROZDZIAŁ 13 — STABILNY / FORMALNIE ZATWIERDZONY.**

Audyt XLV usunął rzeczywistą lukę w dowodzie transformacji gęstości, błędny zapis gęstości na całej prostej i kilka niejawnych założeń, a następnie potwierdził kompletne CI **2/2 SUCCESS** i sześciostronicowy PDF. Niniejszy **drugi, pełny, niezależny i czysty audyt XLVI** po poprawkach objął 8 dowodów, 7 przykładów, 4 uwagi, 16 etykiet, 14 odsyłaczy, 40468 niezależnych regresji, autentyczny PDF i jego składowe. **Nie wykryto nowych usterek wymagających zmiany źródła**, a blob pozostaje **965c76951d267a60e1d7274a1431ac08ef2dd960**. Spełniono zasadę stabilizacji.

**R01–R12 — STABILNE**, nieaudytowane ponownie ani nieedytowane w tej iteracji. **R14–R31 — nietknięte**.

**Następny osobny etap:** audyt globalny **XLVII / R14 I**; rozdział 14 można rozpocząć dopiero jako kolejną, odrębną iterację.
