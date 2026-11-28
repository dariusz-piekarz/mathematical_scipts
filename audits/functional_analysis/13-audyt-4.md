# Analiza funkcjonalna — rozdział 13 — audyt 04 (drugi niezależny czysty przegląd)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Źródło:** chapters/pl/functional_analysis/13-przestrzenie-hilberta-reprezentacja-riesza-i-formy-poltoraliniowe.tex.  
**Niezmieniony blob źródła 13/03 i 13/04:** 1ca8b2ee077f558e50412c5d74e116779ab44f31.  
**Niezmieniony blob regresji po poprawce w 13/02:** ea8ea6a5b82596705f5f717c57317a6a06268369.  
**Ocena matematyczno-redakcyjna:** **CZYSTY — 2/2**, po czystym audycie 13/03. Formalne zamknięcie rozdziału wymaga ponadto zakończonego sukcesem CI dla niniejszego raportu (lub innego potwierdzonego przebiegu tej samej wersji źródła/testów).

## Punkt kontynuacji i identyczność badanej wersji

Przed rozpoczęciem odczytano raporty 13/01, 13/02 i 13/03. Audyt 13/01 był z poprawkami do źródła, 13/02 wykrył i naprawił test, który porównywał to samo wyrażenie pochodnej z samym sobą; oba miały status 0/2. Audyt 13/03 był pierwszą niezależną kontrolą źródła bez dalszych zmian (1/2). Ponownie odczytane źródło i testy mają dokładnie te same blob SHA co w 13/03. Nie tworzono kolejnej gałęzi, nie poprawiano źródła na siłę.

Przy najnowszej kontroli GitHub Actions [#45268726941](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45268726941), uruchomione po raporcie 13/03 na commicie a4eb80dbff7da27a19358612a1d3e71ccc95470a, miało status **COMPLETED / SUCCESS**. Bezpośrednio pobrane kroki: **21/21 testów regresyjnych PASS**, przygotowanie kontekstu 01–13 PASS, rzeczywista kompilacja LaTeX PASS, kontrola PDF i odsyłaczy PASS, publikacja artefaktu PASS. Tym samym problem niepotwierdzonego CI odnotowany w raporcie 13/03 został rozstrzygnięty.

## Niezależna kontrola 14 dowodów

1. **Nierówność Cauchy'ego–Schwarza.** Dla y różnego od zera współczynnik ortogonalizacji \(\alpha=\langle x,y\rangle/\|y\|^2\) jest prawidłowy przy liniowości iloczynu skalarnego w pierwszym argumencie; dodatniość normy reszty daje nierówność i charakterystykę równości.
2. **Polaryzacja i równoległobok.** Sprawdzono znaki części urojonej: \(\|x+iy\|^2-\|x-iy\|^2=4\operatorname{Im}\langle x,y\rangle\). Odtworzenie części rzeczywistej i urojonej z normy zgadza się z przyjętą konwencją.
3. **Rzut na niepusty, domknięty i wypukły zbiór.** Rozwinięcie normy względem środka odcinka zapewnia Cauchy'ego ciągu minimalizującego. Warunek wariacyjny i jego implikacja odwrotna są poprawne. Suma dwóch warunków wariacyjnych prowadzi do \(\|P_Cx-P_Cy\|^2\le\operatorname{Re}\langle x-y,P_Cx-P_Cy\rangle\) i nieekspansywności.
4. **Rozkład ortogonalny.** Perturbacje zarówno rzeczywiste, jak i urojone w przypadku zespolonym są jawnie wymagane. Rozkład i jego jednoznaczność prowadzą do liniowego, samosprzężonego rzutu, Pitagorasa, równania \(M^{\perp\perp}=M\) i rozróżnienia normy projekcji zerowej.
5. **Reprezentacja Riesza w Hilbercie.** Po ortogonalnym rozkładzie względem zamkniętego jądra F prawidłowy reprezentant to \(y=\overline{F(z)}z/\|z\|^2\). Jest to konsekwencja antyliniowości drugiego argumentu. Izometria i antyliniowość identyfikacji przy \(\K=\C\) są odrębnie uzasadnione.
6. **Nierówność Bessela.** Reszta po odjęciu skończonej sumy współczynników Fouriera jest ortogonalna do jej każdego składnika, więc Pitagoras daje dokładną tożsamość i ograniczenie sumy kwadratów.
7. **Przeliczalność niezerowego nośnika Fouriera.** Dla każdego n zbiór współczynników o module co najmniej 1/n ma moc co najwyżej \(n^2\|x\|^2\). Zawieranie nośnika w przeliczalnej sumie takich zbiorów jest poprawne bez założenia ośrodkowości H.
8. **Zbieżność bezwarunkowa i Parseval.** Dla sieci skończonych sum przy porządku inkluzji supremum sum kwadratów pozwala znaleźć wspólny skończony zbiór kontrolujący wszystkie ogony. Granica należy do domkniętego rozpięcia i ma resztę ortogonalną do wszystkich wektorów ortonormalnych, więc jest rzutem P_Mx. Dla bazy \(M=H\), a każda enumeracja przeliczalnego niezerowego nośnika jest współkońcowa w rodzinie zbiorów skończonych. Wzór na błąd wykorzystuje warunek bazy, nie jest mylnie stosowany do niezupełnej rodziny.
9. **Istnienie bazy ortonormalnej.** Zorn stosuje się do rodzin ortonormalnych uporządkowanych przez rozszerzenie; suma łańcucha zachowuje ortonormalność. Maksymalność daje gęstość rozpięcia. Dla ośrodkowości rozłączne kule wokół elementów rodziny i gęsty zbiór przeliczalny dowodzą ograniczenia mocy bazy.
10. **Wymiar Hamela i macierz Vandermonde'a.** Dla nieskończonego ortonormalnego ciągu szeregi \(\sum t^{n-1}e_n\) są zbieżne dla \(0<t<1\). Każdy skończony podzbiór różnych parametrów jest liniowo niezależny, gdyż determinant \(\prod_{j<k}(t_k-t_j)\) jest niezerowy. To daje continuum wektorów niezależnych; uwaga o Bairze poprawnie podaje alternatywny dowód słabszej nieprzeliczalności.
11. **Izomorfizm z \(\ell^2(I)\).** Parseval daje liniowość i izometrię mapy współrzędnych; supremum skończonych sum kwadratów wystarcza do zbudowania zbieżnej sieci w H dla dowolnego elementu \(\ell^2(I)\), także przy nieprzeliczalnym I.
12. **Operator sprzężony.** Funkcjonał \(x\mapsto\langle Tx,y\rangle\) jest liniowy w x; jednoznaczność jego reprezentanta i antyliniowość drugiego argumentu dają liniowość \(T^*\). Sprawdzono normę, podwójne sprzężenie i odwróconą kolejność przy składaniu.
13. **Formy półtoraliniowe.** Dla ustalonego x sprzężenie wartości formy daje liniowy funkcjonał w y, który reprezentuje się przez Rieszowskiego wektora Ax. Otrzymano \(a(x,y)=\langle Ax,y\rangle\), liniowość A, izometrię norm i kryterium hermitowskości.
14. **Twierdzenie Laxa–Milgrama.** Koercywność daje \(\|Ax\|\ge\alpha\|x\|\) i domknięty obraz. Z \(\ker A^*=(\operatorname{ran}A)^\perp\) oraz \(\operatorname{Re}\langle Ay,y\rangle\ge\alpha\|y\|^2\) wynika gęstość obrazu, a więc surjektywność A. Nie zakłada się symetrii formy. Antyliniowy funkcjonał prawej strony ma reprezentację \(\langle f,v\rangle\) i otrzymuje się normowe oszacowanie rozwiązania.

**14/14 dowodów:** bez nowej luki wymagającej poprawki. Powyższe są kontrolami matematycznymi, nie formalizacją w Lean.

## Niezależny przegląd 5 przykładów

1. \(\ell^2\) i \(L^2\) z normami od iloczynu skalarnego oraz kontrprzykład \(C([0,1])\), gdzie dla funkcji 1 i t strony równoległoboku wynoszą 5 i 4.
2. Rzut ortogonalny na funkcje stałe w \(L^2([0,1])\): normalizacja przez miarę całego przedziału jest równa 1 i reszta ma całkę zerową.
3. Szereg \(\sum 2^{-n}e_n\): normowa zbieżność bez skończonego rozpięcia, ponieważ wszystkie współczynniki Fouriera są niezerowe.
4. Gram–Schmidt zachowuje rozpięcie i daje normowane wektory ortogonalne; eksponenty \((2\pi)^{-1/2}e^{int}\) są ortonormalne, a ich zupełność nie jest bezpodstawnie zakładana.
5. **Jednowymiarowe zagadnienie Poissona:** przestrzeń funkcji absolutnie ciągłych z zerowymi danymi brzegowymi i pochodną w \(L^2\) jest izometryczna z domkniętym \(L^2_0\). Oszacowanie \(\|u\|_2\le\|u'\|_2/\sqrt2\) daje ciągłość \(\Lambda\). Konstruuje się najpierw niezależnego kandydata \(g(t)=c-\int_0^t f\), \(w(x)=\int_0^xg\), z \(c=\int_0^1(1-s)f(s)\,\mathrm d\lambda(s)\). Sprawdzono \(w(0)=w(1)=0\), \(w''=-f\) prawie wszędzie, całkowanie przez części, korektę średniej przy gładkiej aproksymacji i użycie jednoznaczności Laxa–Milgrama dopiero po stwierdzeniu słabej tożsamości. Nie ma założenia \(u\in H\Rightarrow u''\) istnieje.

**5/5 przykładów:** bez nowej usterki. Po 13/02 test jawnego rozwiązania \(f=1\) sprawdza centralnymi różnicami zarówno pierwszą, jak i drugą pochodną w dziewięciu punktach, a nie tautologiczną równość.

## Struktura LaTeX, odniesienia i terminologia

Ponownie pobrano wszystkie źródła rozdziałów **01–13** z istniejącej gałęzi. Łącznie **251 etykiet bez duplikatów**, w tym **30 etykiet w rozdziale 13**; **13 odsyłaczy rozdziału 13, wszystkie rozwiązane**. Parowanie środowisk rozdziału 13: 14 proof, 10 twierdzenie, 2 stwierdzenie, 2 lemat, 4 definicja, 5 przyklad i 5 uwaga; każde ma dopasowane zakończenie. Brak rysunków TikZ. Wszystkie akapity mają parzystą liczbę nieescapowanych znaczników matematyki inline. Nie znaleziono niedopuszczonych zapisów funkcji charakterystycznej, terminów „sekwencyjny”, „wskaźnik” i „przestrzeń dualna” w źródle ani niepoprawnego „injektywny”. Konwencja liniowości iloczynu skalarnego w pierwszym argumencie jest jednolita.

Poprzedni audyt 13/01 dokumentuje pobranie 78-stronicowego PDF oraz wizualną inspekcję stron 72–78 wraz z kontrolą położenia bloków. Przy niezmienionym źródle nie stwierdzono podstaw do nowych poprawek graficznych. Dedykowane CI na commicie a4eb80dbff7da27a19358612a1d3e71ccc95470a: **21/21 PASS**, kompilacja i kontrola PDF PASS.

## Decyzja

**13/04: drugi CZYSTY audyt źródła, 2/2; bez zmian LaTeX, testów lub workflow.** Raport ma jedynie utrwalić niezależną kontrolę obecnego bloba. **Po jego zapisaniu należy odczytać końcowy status nowego dedykowanego CI.** Po zielonym CI na tej samej wersji zostanie spełniony warunek oznaczenia rozdziału 13 jako STABILNEGO i odblokowania audytu 14/01. Nie należy przedstawiać nieukończonego CI jako wyniku PASS.

## Ostateczne potwierdzenie stabilizacji 13

Przebieg [GitHub Actions #45270797207](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45270797207), uruchomiony po zapisaniu drugiego niezależnego czystego audytu 13/04 na commicie 023dd1159ed39df13295b7b9857994a7ee3438ae, zakończył się **COMPLETED/SUCCESS**. Z osobnego odczytu kroków wynikają: **21/21 testów regresyjnych PASS**, przygotowanie kompletnego kontekstu źródłowego 01–13 PASS, kompilacja LaTeX PASS, weryfikacja PDF i odsyłaczy PASS, przesłanie artefaktu PASS.

Zweryfikowano, że źródło rozdziału 13 ma nadal blob SHA **1ca8b2ee077f558e50412c5d74e116779ab44f31**, a testy mają SHA **ea8ea6a5b82596705f5f717c57317a6a06268369**, identyczne jak przy audycie 13/03 oraz wcześniejszym zielonym CI #45268726941. Wizualną inspekcję PDF tej samej wersji źródła udokumentowano w 13/01.

**KOŃCOWA DECYZJA: ROZDZIAŁ 13 — STABILNY (2/2 CZYSTYCH AUDYTÓW + ZIELONE CI).** Można rozpocząć audyt **14/01**. Niniejsze uzupełnienie zmienia tylko plik dokumentacji, bez zmian w LaTeX, testach lub workflow. Ewentualny kolejny workflow uruchomiony samym zapisem niniejszego raportu nie jest dodatkowym niezależnym audytem matematycznym ani nie narusza identyczności sprawdzonego źródła.
