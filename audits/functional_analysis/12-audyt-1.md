# Analiza funkcjonalna — rozdział 12 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/12-klasyczne-przestrzenie-banacha-i-ich-duale.tex.  
**SHA przed zmianami:** 0b858ed0ee8309ce1aa7925bfb3e4de92e71a0f3.  
**SHA po wszystkich poprawkach 12/01:** 923f7976d09f42030687a8873401cf34da4ff2fb.  
**Werdykt:** **AUDYT Z POPRAWKAMI, NIESTABILNY 0/2.** Rozdział 13 pozostaje zablokowany.

## Stan wejściowy

Bezpośrednio sprawdzono istniejącą gałąź i stan raportów: automatyzacja ukończyła audyt 11/04 ze statusem CZYSTY 2/2, źródło rozdziału 11 nie zmieniło SHA, a [CI #45237536343](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45237536343) ma zakończony status SUCCESS. Wcześniej nie istniał raport 12/01 ani dedykowany plik testów czy workflow 12; rzeczywiście otwarto nową jednostkę.

## Przegląd matematyczny: 10 dowodów

1. **Przestrzeń operatorów:** dla unormowanej E i Banacha F punktowe granice operatorowego ciągu Cauchy'ego określają operator T, a oszacowanie normowe zapewnia jego ciągłość i zbieżność w normie. E nie musi być zupełna; tak samo zawsze zupełna jest przestrzeń sprzężona E'.
2. **Hölder dla ciągów:** nierówność Younga po normalizacji, sumowanie po skończonej liczbie współrzędnych i przejście do granicy dają wynik dla $1<p<\infty$; przypadek $p=1$, $q=\infty$ jest sprawdzony bezpośrednio.
3. **Zupełność i gęstość w przestrzeniach ciągowych:** dla $\ell^p$, $p<\infty$, użycie podciągu Cauchy'ego o sumowalnych normach różnic pozwala utworzyć granicę w $\ell^p$. Dla $\ell^\infty$ wystarcza zbieżność jednostajna współrzędnych; $c_0$ jest podprzestrzenią domkniętą, a obcięcia dowodzą gęstości $c_{00}$ tylko we właściwych klasach.
4. **Przestrzenie sprzężone $\ell^p$ i $c_0$:** współczynniki $a_n=F(e_n)$ są wyznaczone jednoznacznie. Wektor testowy $\overline{a_n}|a_n|^{q-2}$ po normalizacji daje izometrię dla $p>1$, a dobór faz i skończonego nośnika daje odpowiednią normę dla $c_0$. Jawnie obsłużono przypadek $a_n=0$, w którym wykładnik $q-2$ może być ujemny.
5. **Hölder, Minkowski i zupełność $L^p$:** podciąg o sumowalnych normach różnic daje granicę prawie wszędzie i normowo przy użyciu zbieżności monotonicznej. Dla $p=\infty$ różnice są jednostajnie małe poza przeliczalną sumą zbiorów miary zero. Przed nierównością Minkowskiego dopisano dowód, że $f+g$ należy do $L^p$.
6. **Gęstość funkcji prostych:** funkcje proste rosnące do nieujemnej funkcji całkowalnej, zbieżność zmajoryzowana i rozkład na części rzeczywiste, urojone, dodatnie i ujemne dają tezę.
7. **Przestrzeń sprzężona $L^p$:** miara $\nu(A)=F(\chi_A)$ jest przeliczalnie addytywna, ma skończoną wariację i jest absolutnie ciągła względem skończonej miary $\mu$. Twierdzenie Radona–Nikodyma daje $g\in L^1$; test fazowy przy $p=1$ i obcięte testy $\overline{g_N}|g_N|^{q-2}$ dla $p>1$ dają $g\in L^q$ oraz normę. Reprezentacja rozszerza się przez gęstość funkcji prostych.
8. **Zupełność $C(K)$:** jednostajna granica ciągu Cauchy'ego funkcji ciągłych jest ciągła, a wartość graniczna istnieje punktowo dzięki zupełności $\K$.
9. **Miara reprezentująca dodatni funkcjonał:** sprawdzono funkcję $m(U)$ na otwartych zbiorach, skończoną podaddytywność przez podział jedności na zwartym nośniku, addytywność na rozłącznych otwartych, konstrukcję metrycznej miary zewnętrznej oraz mierzalność Carathéodory'ego. Dopisano brakującą identyfikację $\mu^*(U)=m(U)$ dla zbiorów otwartych i równość $\mu^*(K)=T(\chi_K)<\infty$. Regularność i warstwowy wzór całkowania prowadzą do reprezentacji; jednoznaczność wynika z regularności i całek funkcji ciągłych.
10. **Twierdzenie Riesza–Markowa:** addytywna część dodatnia funkcjonału rzeczywistego oraz część ujemna dają miarę znakowaną. Dla funkcjonałów zespolonych oddzielnie reprezentuje się rzeczywistą i urojoną część ograniczenia do funkcji rzeczywistych. Gęstość funkcji ciągłych w $L^1(|\nu|)$ i aproksymacja fazowa dają równość normy i wariacji.

**Weryfikacja:** 10/10 dowodów skontrolowanych pod kątem istotnych założeń, kwantyfikatorów i przykładów granicznych. Dowód Riesza–Markowa powołuje jawnie twierdzenia Radona–Nikodyma, Carathéodory'ego, Urysohna oraz zbieżność monotoniczną; nie przedstawia się tej inspekcji jako formalizacji w Lean.

## Dwa przykłady i uwagi

1. **Funkcjonał granicy w $\ell^\infty$:** funkcjonał $L(x)=\lim x_n$ na ciągach zbieżnych ma normę 1, a przedłużenie Hahna–Banacha znika na każdym wektorze bazowym, lecz jest równe 1 na $u=(1,1,\ldots)$. Wyklucza to reprezentację przez element $\ell^1$.
2. **Miary Diraca:** ewaluacja w dowolnym punkcie zwartego metrycznego K jest reprezentowana przez $\delta_{x_0}$ i ma normę 1; różne punkty są rozdzielane funkcjami ciągłymi.

Przejrzano też osobny przykład nadmiarowych funkcjonałów $(L^\infty)'$ oraz uwagę rozróżniającą miary od dystrybucji. Dwa środowiska przykładów są poprawne.

## Konkretne poprawki źródła

- Zamieniono **„przestrzeń dualna”, „przestrzenie dualne”** na standard **„przestrzeń sprzężona”, „przestrzenie sprzężone”** w nagłówkach i tekście. Ścieżkę istniejącego pliku zachowano ze względu na bieżące odsyłacze i główny skrypt.
- Zamieniono **15 wystąpień zapisu funkcji charakterystycznej z użyciem polecenia \mathbf1** na $\chi_A$ lub odpowiedni $\chi_B$, a zamiast „wskaźniki” użyto „funkcje charakterystyczne”. Stały ciąg jedynek w $\ell^\infty$ otrzymał osobne oznaczenie $u=(1,1,\ldots)$.
- W dowodzie reprezentacji dodatniego funkcjonału jawnie wykazano $\mu^*(U)=m(U)$ i $\mu^*(K)=T(\chi_K)<\infty$.
- Przed zastosowaniem Höldera w dowodzie Minkowskiego dopisano $\lvert f+g\rvert^p\le2^{p-1}(\lvert f\rvert^p+\lvert g\rvert^p)$, aby uzasadnić całkowalność odpowiedniej potęgi sumy.

**Commit źródła:** 9edb7d5f5eae107864f6c93cde76ede87c372971. **Blob SHA po korektach terminologii i dowodów:** 090fd502097cbc3d7531b8af95005d1525ccf019; **ostateczny blob po naprawie składni:** 923f7976d09f42030687a8873401cf34da4ff2fb.

## Struktura, odsyłacze i bramki techniczne

Pobrano wszystkie 12 plików źródłowych: **221 etykiet bez duplikatów**, w tym **19 etykiet rozdziału 12** i **5 odsyłaczy rozdziału 12, wszystkie rozwiązane**. Wszystkie środowiska 12 są sparowane: **10 proof**, **4 definicja**, **2 stwierdzenie**, **5 twierdzenie**, **3 lemat**, **2 przyklad**, **2 uwaga**. Nie ma rysunków TikZ w tym rozdziale.

Dodano początkowo **17 testów regresyjnych**, a po diagnostyce kompilacji rozszerzono zestaw do **18 testów** w tools/tests/test_functional_analysis_ch12.py, obejmujących: numeryczne modele Höldera, testy izometrii funkcjonałów, skończone modele miar i wariacji, tożsamość dyskretyzacji warstwowej, oznaczenia, strukturę środowisk i rozwiązanie odsyłaczy w kontekście 01–12. Dodano dedykowany workflow .github/workflows/functional-analysis-ch12.yml, który rzeczywiście uruchamia testy, kompiluje 12 plików LaTeX i weryfikuje PDF i logi. **Nie deklaruje się ostatecznego sukcesu CI przed bezpośrednim sprawdzeniem wyniku.**

**Decyzja:** **12/01 Z POPRAWKAMI — 0/2**. Kolejny audyt 12/02 powinien niezależnie przejrzeć ten sam blob, zweryfikować złożony PDF i usunąć ewentualne usterki. Rozdział 13 pozostaje zablokowany do zamknięcia 12.


## Uzupełnienie 12/01: diagnostyka CI, poprawka składni i faktyczny PDF

Pierwszy dedykowany przebieg [#45247874812](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45247874812) zakończył się **FAILURE**. Testy regresyjne były zielone, lecz kompilacja LaTeX zatrzymała się na wierszu 347 rozdziału 12 z komunikatem „Missing $ inserted”. Z rzeczywistego logu kompilacji (pobranego z artefaktu GitHub Actions) ustalono, że w uwadze o przestrzeni sprzężonej $(L^\infty(\mu))'$ zabrakło końcowego znacznika trybu matematycznego. Wprowadzono poprawkę składni, commit e60beaa15645dcae08b6668a9a2aaae602c8bda0. Ostateczny blob źródła to **923f7976d09f42030687a8873401cf34da4ff2fb**.

Do pliku tools/tests/test_functional_analysis_ch12.py dodano test bilansowania znaczników matematycznych w akapitach LaTeX. Nowy zestaw zawiera **18 testów**, blob SHA a3d6007eb6ded526358b5a02fccd943bd8c2f4a5, commit 567d84238ca18c6df1c5d7fdeb69586c03339c7f. Tego testu nie rozluźniano mimo nieudanego wcześniejszego CI.

Nowy rzeczywisty przebieg [GitHub Actions #45248566903](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45248566903) zakończył się **COMPLETED/SUCCESS**: **18/18 testów PASS**, przygotowanie kontekstu 01–12 PASS, kompilacja LaTeX PASS, weryfikacja PDF i odsyłaczy PASS oraz publikacja artefaktu PASS. Ukończony sukcesem jest również [przebieg #45248672491](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45248672491), wyzwolony zapisaniem późniejszego audytu 12/02 (bez zmiany LaTeX).

Pobrano faktyczny artefakt functional-analysis-ch12-pdf z runu #45248566903 i obejrzano wygenerowany dokument **72 strony**, z rozdziałem 12 na końcu strony 66 i stronach 67–72. Wykonano zbiorczy podgląd stron 61–72 z właściwym kontekstem rozdziału 11. Kontrola PyMuPDF wszystkich stron 61–72 nie wykazała żadnego bloku tekstowego wychodzącego poza prostokąt strony. Oględziny nie wskazują kolizji podpisów, obciętych wzorów ani tekstu nachodzącego na marginesy. Kontrola graficzna i techniczna nie stanowi formalnego dowodu twierdzeń.

**Ostateczny werdykt 12/01: Z POPRAWKAMI, 0/2**, przy zielonym CI po naprawie źródła. Nowy audyt 12/02 (utworzony niezależnie przez automatyzację) dotyczy ostatecznego SHA **923f7976d09f42030687a8873401cf34da4ff2fb**; nie wymagał zmian źródła i może stanowić pierwszy z dwóch czystych audytów stabilizacyjnych, o ile następny audyt potwierdzi brak nieujawnionej usterki. Rozdział 13 nadal zablokowany.
