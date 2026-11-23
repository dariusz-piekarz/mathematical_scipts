# Analiza funkcjonalna — rozdział 13 — audyt 01 (matematyka, redakcja, testy)

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6 (istniejąca).  
**Źródło:** chapters/pl/functional_analysis/13-przestrzenie-hilberta-reprezentacja-riesza-i-formy-poltoraliniowe.tex.  
**SHA źródła przed audytem:** e8e9e0080bcbee8f2eba9eda7176d616600dc542.  
**SHA po poprawkach:** 1ca8b2ee077f558e50412c5d74e116779ab44f31.  
**SHA testów:** fa97449adfca69de43e80540613bc5fa1763ff14.  
**Werdykt:** **AUDYT Z POPRAWKAMI — STABILIZACJA 0/2.** Rozdział 14 pozostaje zablokowany.

## Punkt kontynuacji

Sprawdzono stan gałęzi i audytów przed działaniem. Rozdział 12 ma już dwa niezależne czyste audyty identycznego źródła, formalną decyzję STABILNY i potwierdzone najnowsze zielone [CI #45252138762](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45252138762). Audytu 13 dotąd nie zapisano; przygotowano nową jednostkę 13/01, bez dublowania istniejącego raportu.

## Kontrola wszystkich 14 dowodów

1. **Cauchy–Schwarz.** Wybór \(\alpha=\langle x,y\rangle/\|y\|^2\) dla \(y\ne0\) daje resztę ortogonalną i właściwą nierówność, przypadek równości oraz nierówność trójkąta; znaki są zgodne z konwencją liniowości w pierwszym argumencie.
2. **Tożsamość równoległoboku i polaryzacja.** Zweryfikowano znak części urojonej: \(\|x+iy\|^2-\|x-iy\|^2=4\operatorname{Im}\langle x,y\rangle\). Wzór zespolony i rzeczywisty pozostają prawidłowe.
3. **Rzut metryczny na domknięty zbiór wypukły.** Dla ciągu minimalizującego tożsamość równoległoboku daje Cauchy'ego, a zupełność wraz z domkniętością istnienie minimizatora. Wariacja na odcinku w C daje warunek \(\operatorname{Re}\langle x-p,z-p\rangle\le0\), od którego dowodzi się również jednoznaczność i 1-lipschitzowskość.
4. **Rozkład ortogonalny.** Dla zespolonego H konieczne są perturbacje \(tv\) i \(itv\); źródło stosuje obie. Ortogonalność, jednoznaczność, samosprzężoność rzutu, Pitagoras oraz \(M^{\perp\perp}=M\) mają poprawne uzasadnienie.
5. **Reprezentacja Riesza w Hilbercie.** Dla F różnego od zera wykorzystano domknięte jądro i niezerowy element ortogonalnego dopełnienia. Przy naszej konwencji poprawnym reprezentantem jest \(y=\overline{F(z)}z/\|z\|^2\), a izometria reprezentacyjna jest antyliniowa dla ciała zespolonego.
6. **Nierówność Bessela.** Wykorzystano ortogonalność reszty i skończonej sumy współczynników; bez wymagania przeliczalności całej rodziny.
7. **Przeliczalność nośnika Fouriera.** Dla progu \(1/n\) Bessel daje ograniczenie liczby indeksów przez \(n^2\|x\|^2\); suma przeliczalnej liczby skończonych zbiorów obejmuje wszystkie niezerowe współczynniki.
8. **Parseval i zbieżność bezwarunkowa.** Dla sieci sum po skończonych zbiorach supremum sum kwadratów daje warunek Cauchy'ego. Granica ma resztę w \(M^\perp\), więc jest rzutem \(P_Mx\). Dla bazy M=H; numeracja niezerowego, przeliczalnego nośnika jest współkońcowa i nie zmienia sumy.
9. **Istnienie bazy ortonormalnej.** Lemat Zorna daje maksymalną rodzinę, której dopełnienie ortogonalne jest zerowe. Ośrodkowość jest równoważna przeliczalności bazy przez wymierne kombinacje lub rozłączne otwarte kule.
10. **Moc bazy Hamela.** Konstrukcja \(v_t=\sum_{n\ge1}t^{n-1}e_n\), \(0<t<1\), daje rodzinę mocy continuum, z której każda skończona podrodzina jest niezależna przez wyznacznik Vandermonde'a. Osobny argument Baire'a dowodzi słabszej nieprzeliczalności w dowolnym nieskończenie wymiarowym Banachu.
11. **Współrzędne w \(\ell^2(I)\).** Parseval daje liniową izometrię, a dla dowolnego układu współczynników kwadratowo sumowalnych sieć skończonych kombinacji jest Cauchy'ego, zatem operator współrzędnych jest surjektywny.
12. **Operator sprzężony.** Riesz dla liniowych funkcjonałów \(x\mapsto\langle Tx,y\rangle\), zgodność konwencji zespolonej, normy i tożsamości \((T^*)^*=T\), \((ST)^*=T^*S^*\) są sprawdzone.
13. **Reprezentacja form półtoraliniowych.** Zastosowanie Riesza do \(y\mapsto\overline{a(x,y)}\) daje \(a(x,y)=\langle Ax,y\rangle\). Sprawdzono liniowość A, równość norm i równoważność hermitowskości oraz samosprzężoności.
14. **Twierdzenie Laxa–Milgrama.** Koercywność zapewnia ograniczenie od dołu, iniektywność i domkniętość obrazu; \(\ker A^*=\{0\}\) z tej samej koercywności daje jego gęstość. Dla antyliniowego \(\Lambda\) reprezentant \(f\) spełnia \(\Lambda(v)=\langle f,v\rangle\), więc \(u=A^{-1}f\) jest jednoznaczny z oszacowaniem \(\|u\|\le\|\Lambda\|/\alpha\). Nie założono niepotrzebnie hermitowskości formy.

**Werdykt dowodowy:** 14/14 sprawdzonych, bez znalezionej fałszywej tezy. Weryfikacja matematyczna jest odrębna od kompilacji LaTeX i nie jest formalnym dowodem Lean.

## Pięć przykładów

1. \(\ell^2\), \(L^2\), kontrprzykład \(C([0,1])\): dla \(f=1\), \(g(t)=t\) strony tożsamości równoległoboku wynoszą 5 i 4, więc norma supremum nie pochodzi od iloczynu skalarnego.
2. Rzut na stałe w \(L^2([0,1])\): całkowa średnia reprezentuje poprawny rzut na \(\K\chi_{[0,1]}\), ponieważ masa całego przedziału wynosi 1.
3. Szereg \(\sum2^{-n}e_n\): wektor należy do domkniętego rozpięcia ortonormalnego ciągu, lecz nie do jego algebraicznego rozpięcia, ponieważ ma nieskończenie wiele niezerowych współczynników.
4. Gram–Schmidt: poprawnie odejmuje rzuty na wcześniej zbudowane wektory, a znormalizowane eksponenty \((2\pi)^{-1/2}e^{int}\) są ortonormalne w \(L^2([0,2\pi])\). Źródło nie zakłada ich zupełności bez osobnego dowodu.
5. **Słabe zagadnienie brzegowe Poissona:** funkcje absolutnie ciągłe z zerowymi wartościami brzegowymi i pochodną w \(L^2\) tworzą Hilberta izometrycznie identyfikowanego z domkniętą podprzestrzenią \(L^2_0\). Rozpisano oszacowanie \(\|u\|_2\le\|u'\|_2/\sqrt2\) oraz \(|\Lambda(v)|\le\|f\|_2\|v\|_H/\sqrt2\). **Usunięto nieuzasadnione wyprowadzenie regularności z samej słabej postaci:** najpierw konstruuje się funkcję \(w(x)=\int_0^x g(t)\,\mathrm d\lambda(t)\), gdzie \(g(t)=c-\int_0^t f(s)\,\mathrm d\lambda(s)\) i \(c=\int_0^1(1-s)f(s)\,\mathrm d\lambda(s)\). Twierdzenie Fubiniego zapewnia \(w(1)=0\); \(w''=-f\) prawie wszędzie. Całkowanie przez części, gęstość gładkich funkcji o zerowych wartościach brzegowych i ciągłość obu stron gwarantują słabą tożsamość. Na końcu jednoznaczność Laxa–Milgrama daje \(u=w\) i jawny wzór na pochodną rozwiązania. Nie zakłada się regularności przed jej udowodnieniem.

**Werdykt przykładów:** 5/5 zweryfikowanych, jedno istotne doprecyzowanie dowodu w przykładzie Poissona.

## Zmiany faktycznie wprowadzone

- Dwa niepożądane wyrażenia „przestrzeń dualna” zastąpiono „przestrzeń sprzężona”; dwa zapisy „injektywny/injektywność” zmieniono na „iniektywny/iniektywność”.
- Rozbudowano dowód ciągłości funkcjonału, oszacowanie normowe oraz poprawną konstrukcję i identyfikację rozwiązania słabego zagadnienia brzegowego.
- Dodano dedykowane **21 testów** w tools/tests/test_functional_analysis_ch13.py: matematyczne modele zespolonej polaryzacji, rzutów, Riesza, Bessela, Parsevala, Gram–Schmidta, operatora sprzężonego, Laxa–Milgrama i zagadnienia Poissona oraz kontrakty terminologii, środowisk i odsyłaczy.
- Dodano workflow .github/workflows/functional-analysis-ch13.yml: uruchamia testy, kompiluje realne rozdziały 01–13 z głównego pliku i kontroluje PDF, diagnostykę LaTeX oraz odsyłacze. Pierwsze uruchomienia ujawniły zbyt dosłowne asercje tekstowe w teście Poissona, które skorygowano na jawne wymagania konstrukcji \(w\) i identyfikacji \(u=w\). Nie zmieniono testów numerycznych w celu wymuszenia PASS.

**Końcowy blob źródła:** 1ca8b2ee077f558e50412c5d74e116779ab44f31. **Końcowy blob testów:** fa97449adfca69de43e80540613bc5fa1763ff14.

## Struktura i referencje

Pobrano ponownie źródła rozdziałów 01–13. W sumie jest **251 etykiet, bez duplikatów**, a sam rozdział 13 zawiera **30 etykiet oraz 13 odsyłaczy do istniejących celów**. Środowiska są sparowane: 14 proof, 10 twierdzenie, 2 stwierdzenie, 2 lemat, 4 definicja, 5 przyklad i 5 uwaga. Nie ma środowisk TikZ. W źródle nie znaleziono niewłaściwej terminologii, starych zapisów funkcji charakterystycznych ani niezbilansowanych znaczników matematycznych.

## Decyzja

**13/01: AUDYT Z POPRAWKAMI, 0/2.** Warunkiem następnej niezależnej kontroli 13/02 jest potwierdzenie ukończonego zielonego CI i kontrola rzeczywistego PDF dla wskazanego SHA. Następnie obowiązują dwie niezależne czyste kontrole identycznego źródła. Do chwili ich spełnienia rozdział 14 pozostaje zablokowany.
