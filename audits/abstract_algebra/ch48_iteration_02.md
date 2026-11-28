# AA-48 — audyt II: niezależna kontrola kompletności pierwszej gałęzi Kovacica

**Data:** 23 listopada 2026 r. **Status: AUDYT — NIE STABILNY.**
**Źródło:** chapters/pl/abstract_algebra/48-wymierna-galaz-kovacica-dla-potencjalow-wymiernych.tex.
**Zakres:** tylko wymierne rozwiązania r'+r²=q przy q∈C(x); nie całość algorytmu Kovacica.

## 1. Przeliczenie lokalnej klasyfikacji

W punkcie a z=x−a. Jeśli r=c_{-m}z^{-m}+... i m≥2, w r² pojawia się c_{-m}² z^{-2m}; r' ma co najwyżej z^{-m-1}. Ponieważ 2m>m+1, biegun q ma dokładnie rząd 2m. Przy m=1 w q współczynnik z^{-2} wynosi c(c−1), zatem jeśli q regularna i c≠0, c=1. Przy biegunie q rzędu 1 jedyny dopuszczalny biegun r jest prosty z c=1; w tym przypadku q_{-1} może wynikać z regularnej części r i nie jest z góry zerowe.

Dla q rzędu 2m≥4, u=∑_{j=1}^m c_{-j} z^{-j}. Ponieważ r−u jest regularna, q oraz u'+u² muszą mieć identyczne współczynniki przy potęgach -2m do -m−1. Wiodący warunek daje dwa znaki c_{-m}=±√q_{-2m}, a każdy kolejny współczynnik c_{-j}, j=m−1,...,1, występuje liniowo z mnożnikiem 2c_{-m}≠0. To zamyka listę lokalnych kandydatów. Nieprzysty rząd q≥3 odrzucany przed innymi krokami.

## 2. Rozkład globalny i pierwiastki wielokrotne

Niech S będzie zbiorem biegunów q. Dla każdego rozwiązania r wszystkie części główne r w S są ustalone przez wybraną gałąź lokalną. Pozostałe bieguny leżą w punktach regularności q, mają rząd 1 i residuum 1. Stąd r=ω+R+P'/P, ω wielomian, R suma ustalonych części głównych, P unormowany, bezkwadratowy i P(a)≠0 przy a∈S.

Z r'+r²=q wynika P''+2uP'+(u'+u²−q)P=0 dla u=ω+R. Równanie jest **liniowe względem współczynników P**. Jeśli q i u są regularne w b, a P ma tam zero wielokrotne m≥2, to P'' ma rząd m−2 i nie znika jego wyraz wiodący, podczas gdy pozostałe dwa składniki mają rząd co najmniej m−1 i m. W źródle jawnie poprawiono hipotezę regularności **obu** funkcji (sam warunek u regularna nie wystarcza).

## 3. Nieskończoność — rozdzielenie trzech przypadków

Pisząc R=ρ/x+O(x^-2), P'/P=n/x+O(x^-2):
- Jeśli polynomial part(q) ma dodatni stopień 2d, koniecznie deg ω=d i dwa znaki wiodącego współczynnika. Wysokie współczynniki przy x^{2d},...,x^d wyznaczają jednoznacznie ω dla danego znaku. Pozostały współczynnik przy x^{d−1} wymusza n = [x^{d−1}]∞(q−u'−u²)/(2a_d), u=ω+R. Część właściwa R wpływa na ten wzór przy x^{d−1}; pominięcie R prowadziłoby do błędu przy biegunach q.
- Jeśli polynomial part(q)=c≠0, ω jest jedną z dwóch stałych ±√c, a n = [x^-1]∞(q−u'−u²)/(2ω). Sprawdzenie: q=1+2/x, u=1+1/x i n=0.
- Jeśli q=O(x^-1), to ω=0 i w rzeczywistości q=O(x^-2). Przy β=[x^-2]∞q test kwadratowy (ρ+n)(ρ+n−1)=β daje co najwyżej dwie nieujemne całkowite wartości n. Sprawdzenie: q=2/x², R=2/x, ρ=2, β=2 daje n=0; q=0, R=0 daje n=0 lub n=1. W szczególności q=1/x ma być odrzucone.

Te przypadki wyczerpują wszystkie możliwe części wielomianowe r. Skończoność liczby gałęzi jest niezależna od potencjalnie nieograniczonej liczby pierwiastków P.

## 4. Odrzucanie rozwiązań P mających zera w S

Warunek P(a)≠0 dla biegunów q jest istotny. Dla q=2/x² i u=−1/x równanie P''+2uP'=0 ma rozwiązanie P=x³, ale P(0)=0: formalnie otrzymuje się r=−1/x+3/x=2/x, a zatem zmienia się wybrana gałąź residuum. Takie P musi zostać odrzucone w danej gałęzi, mimo że końcowa funkcja r jest poprawna (i powinna pojawić się w gałęzi R=2/x, P=1).

Rozwiązania liniowego układu współczynników P tworzą afiniczną przestrzeń V. Warunek P(a)=0 jest podprzestrzenią afiniczną lub całym V. Jeżeli żaden ze skończenie wielu warunków P(a)=0 nie obejmuje całego V, to nad nieskończonym ciałem C istnieje wspólne P spełniające wszystkie nierówności P(a)≠0. Aby to rozstrzygnąć, można sprawdzić, czy każdy liniowy funkcjonał P↦P(a) znika identycznie na V. W ten sposób nie trzeba wybierać arbitralnego rozwiązania układu, które może przypadkiem być niedopuszczalne.

## 5. Przeliczone przykłady

- q=x²+3+2/(x−1): r=x+1/(x−1) daje r'=1−1/(x−1)², r²=x²+2x/(x−1)+1/(x−1)²; suma=x²+3+2/(x−1). Z=x? Dokładne rozwiązanie z=(x−1)e^{x²/2}; z''/z=q.
- q=2/x²: r=2/x i r=−1/x, w obu przypadkach r'+r²=2/x²; rozwiązania x² oraz x^-1.
- q=x^-4−2x^-3: r=x^-2, r'+r²=x^-4−2x^-3.
- q=1/x³: r wymierna nie istnieje z powodu bieguna nieparzystego rzędu 3.
- q=x+5/(16x²): brak wymiernego r z powodu dodatniego nieparzystego stopnia części wielomianowej, mimo algebraicznego r=√x−1/(4x). Jest to kontrola ograniczenia zakresu testu.
- q=x²+3: r=x+1/x, P=x ma zero ruchome w punkcie regularności q. Weryfikuje, że zmienna P nie może być w ogóle pominięta.

## 6. Status wykonania

Pierwszy audyt sprawdził definicje i dowód lokalny. Drugi niezależnie przeliczył wszystkie rodzaje biegunów, trzy formuły przy nieskończoności oraz warunek P(a)≠0. Należy jeszcze:
- uzyskać wyniki obu zestawów regresji AA-48 na GitHub Actions;
- potwierdzić pełną integralność AA-01–AA-48, PDF i log;
- wyrenderować i przejrzeć każdą nową stronę AA-48;
- dopiero potem wystawić audyt III i ewentualny werdykt STABILNY.

**AA-48 NIE STABILNY**, AA-49 nieotwarty.


## Uzupełnienie po drugim audycie

Dopisano przykład z **jednoczesnym biegunem ustalonym i ruchomym**: q=x²−8x+23−16/(x−1)+2/(x−1)², u=x−4+2/(x−1), P=x−2, r=u+P'/P. Sprawdzono q=u'+u²+2u P'/P+P''/P i P(1)≠0. Dodano test do zestawu SymPy. Przykład wyklucza potencjalnie błędny wniosek, że dla q z biegunami zawsze można przyjąć P=1.
