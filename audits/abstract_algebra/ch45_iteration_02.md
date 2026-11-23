# AA-45 — audyt II: niezależna kontrola dowodów i przypadków brzegowych

**Data:** 23 listopada 2026 r. **Etap: audyt w toku — NIE STABILNY** (weryfikacja ostatecznego CI/PDF osobno).

## 1. Kryterium hiperwykładnicze (przeprowadzone rachunki niezależne od audytu I)

- **Przestępność:** dla niezerowej funkcji wymiernej u nad C(x), pochodna logarytmiczna u'/u to skończona suma m_a/(x-a) z m_a całkowitymi. Nie może być niezerowym wielomianem. Dla t=e^{p(x)}, p niestały, algebraiczność t wymuszałaby przez normę w skończonym rozszerzeniu równość N(t)'/N(t)=d p'(x), sprzeczność.
- **Stałe:** dla hipotetycznego nowego elementu stałego w C(x,t), z AA-43 wynika u'/u=-m p' dla pewnego m≠0 i u wymiernego. Sprzeczność z poprzednim rachunkiem. Warunek p niestały jest konieczny dla tej konstrukcji.
- **Kryterium st:** istotna jest wyłącznie część wielomianowa rozwinięcia w nieskończoności. W przypadkach Dt=ht wszystkie pochodne logarytmiczne mają pp_t niezależne od t. Z koniecznego kierunku Liouville'a i współczynnika przy t w Dv wynika r'+hr=s. Odwrotnie, D(rt)=(r'+hr)t. Nie założono, że funkcja ma wymierną funkcję pierwotną w C(x).
- **Sumy Laurenta:** dla k>0 rozpatrujemy współczynnik przy t^k, dla k<0 przy w^{-k}, gdzie w=t^{-1}, Dw=-hw. Zmiana generatora jest niezbędna: D(t-1)/(t-1)=ht/(t-1) ma ujemne potęgi t w rozwinięciu w nieskończoności. Wkład k=0 jest wymierny, ma zawsze elementarną funkcję pierwotną nad C (przez ułamki proste).
- **Brzegowy kontrprzykład:** przestępny t z Dt=t/x, przy którym t/x jest nową stałą, nie spełnia hipotezy kryterium. Nie należy w żadnym punkcie stosować testu st do niego bez sprawdzenia stałych.

## 2. Równania wymierne, testy biegunów i stopni

- Jeśli h regularne w a, s ma biegun prosty, a r ma biegun rzędu m≥1, to dominująca część r'+hr ma rząd -(m+1) ze współczynnikiem -mc≠0. Nie można osiągnąć prawej strony z biegunem rzędu 1. Dla r regularnej lewa strona jest regularna. Obie możliwości wykluczone.
- Jeśli h i s są wielomianami, każda wymierna r spełniająca r'+hr=s musi nie mieć skończonych biegunów, a więc jest wielomianem. Jeśli deg h≥1 i 0≠s ma deg s<deg h, stopień r'+hr wynosi deg r+deg h, co wyklucza r. Dla r=0 i s≠0 też sprzeczność.
- Nie należy stosować przeszkody bieguna prostego, gdy h sama ma biegun w tym miejscu. Przykład r=1/x, h=1/x daje r'+hr=0.

## 3. Cztery całki

1. **Gaussa:** t=e^{-x²}, h=-2x, s=1. Deg s=0<deg h=1, więc brak rozwiązania r'-2xr=1. Obliczenie dodatniej całki oznaczonej przez biegunowe jest osobnym stwierdzeniem i nie przeczy nieelementarności funkcji pierwotnej.
2. **Sinusowa:** jeden generator t=e^{ix}, t^{-1}=e^{-ix}, nie dwie niezależne zmienne. Dodatnia potęga wymusza r'+ir=1/(2ix). Pomnożenie przez 2i redukuje do R'+iR=1/x, co wyklucza lemat lokalny. Wartość w x=0 funkcji sin(x)/x jest regularna, ale narzucone równanie na R ma biegun. Dla całki Dirichleta kontrola ogonów jest jednostajna względem ε≥0: |∫_A^B e^{-εx} sin(x)/x dx|≤2/A, a część [0,A] przechodzi jednostajnie do granicy.
3. **Logarytm całkowy:** brak elementarnej pierwotnej e^u/u wynika z równania r'+r=1/u. Podstawienie x=e^u w hipotetycznej pierwotnej 1/log x jest dopuszczalne lokalnie, z prawidłową regułą łańcuchową. Osobliwość u=0 nie musi leżeć w obrazie wyjściowego przedziału, bo równanie r'+r=1/u jest tożsamością wymierną.
4. **Eliptyczna:** sprawdzono niezależnie wszystkie punkty krzywej y²=1-x⁴: nad każdym skończonym x dwie gałęzie lub jeden punkt rozgałęziony; nad nieskończonością dwa punkty w=(±i) po podstawieniu s=1/x, w=y/x². W punkcie rozgałęzionym x-a ma rząd 2 w zmiennej y; przy s=0 mamy rząd y równy -2. Forma ω=dx/y ma lokalnie współczynniki 1/y, -1/(2x³) lub -1/w, więc nie ma biegunów.
   - Jeśli v=A+By bez biegunów, to także A i By bez biegunów. A musi być wielomianem bez bieguna w nieskończoności (czyli stałą), a B wielomianem, dla którego By miałoby biegun przy s=0, chyba że B=0.
   - Dla lokalnego u=z^m g(z), g(0)≠0, du/u=m dz/z+dg/g. Pochodne logarytmiczne mają najwyżej biegun prosty, więc nie mogą skasować bieguna dv rzędu ≥2. Stąd v jest stała.
   - Reszty ∑ c_j ord_P(u_j)=0. Rozłożenie c_j nad bazą przestrzeni wymiernej i usunięcie mianowników pozwala utworzyć elementy U_ν=∏ u_j^{N q_νj}. Każdy ma rząd zero we wszystkich punktach, więc jest stały. Wynika ∑ c_j du_j/u_j=0. Forma ω byłaby zerowa, sprzeczność.
   - Dowód nie korzysta z błędnego wniosku, że zerowe reszty dowolnej formy wymuszają jej zerowość.

## 4. Edycja testów

Usunięto tautologiczne porównania w testach rzędów i zastąpiono je bezpośrednią granicą ((1-y²)^(1/4)-1)/y²→-1/4, kontrolą potęg dodatnich i ujemnych oraz tożsamościami w obu punktach nad nieskończonością. Osobny model wymierny kontroluje pary współczynników względem niezależnych stałych 1 i sqrt(2), również dla kombinacji mających zerowe residua.

## 5. Otwarta bramka stabilizacji

Przed werdyktem STABILNY wymagane są: zielony CI na **ostatniej zmianie źródła/testów**, pozytywne dwa zestawy testów matematycznych, integralność książki i katalogu, log końcowego LaTeX, artefakt PDF oraz wizualna kontrola każdej strony AA-45. Nie rozpoczęto AA-46.
