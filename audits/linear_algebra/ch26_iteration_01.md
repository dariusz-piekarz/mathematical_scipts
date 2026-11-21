# Algebra liniowa — rozdział 26, audyt I

**Data:** 21 listopada 2026  
**Rozdział:** chapters/pl/linear_algebra/26-uogolnione-twierdzenia-riccatiego.tex  
**Zakres:** CARE/DARE dla stabilizowalnych i wykrywalnych par z nieujemnie określoną macierzą kosztu Q.

## Pierwsza pełna kontrola matematyczna

1. W sformułowaniach konsekwentnie stosujemy Q=Q*≥0, R=R*>0 i Q=C*C. Dowód istnienia C, niezależności warunku wykrywalności od jego wyboru i równości ker C=ker Q jest kompletny.
2. **Ograniczenie kosztu przez sprzężenie stabilizujące:** dla każdej stabilizowalnej pary istnieje K_0 z stabilną zamkniętą macierzą D=A−BK_0. Dla H=Q+K_0*RK_0≥0 zbieżny szereg lub całka daje W≥0 i skończony koszt na wszystkich horyzontach. Nie stosujemy błędnie wersji twierdzenia Lapunowa z warunkiem H>0.
3. **DARE:** P_N rośnie dzięki nieujemności kosztu etapowego, a górne oszacowanie W_d zapewnia zbieżność form. P≥0 spełnia DARE. Tożsamość P−D*PD=Q+K*RK i wykrywalność wykluczają wektor własny D o |λ|≥1; ponieważ P≥0, obie strony po przemnożeniu przez taki wektor muszą być zerowe, co daje Kv=Cv=0 i Av=λv.
4. **Jednoznaczność DARE:** dwa hermitowskie stabilizujące rozwiązania (drugie nie musi być nieujemne) spełniają E=D_1* E D_2, więc E=0 dzięki zanikowi potęg. Każde rozwiązanie nieujemne jest stabilizujące, gdy C,A wykrywalna.
5. **Ciągła DRE:** rozwinięcie pochodnej x*S(T−t)x oraz uzupełnienie kwadratu daje optymalność skończonego horyzontu; lokalną egzystencję w ODE i globalne przedłużenie uzasadniono przez koszt zerowego sterowania. Monotoniczność przez wydłużanie horyzontu, ograniczenie stabilizującym K_0.
6. **CARE:** S(T)↑P≥0, a S'=F(S) i zbieżność S implikują F(P)=0. D*P+PD=−(Q+K*RK). W przypadku niestabilnego wektora własnego znów Cv=Kv=0, co przeczy wykrywalności. Jednoznaczność stabilizującego rozwiązania CARE uzasadniono porównaniem kosztów dwóch stabilnych sprzężeń bez dodatkowego założenia dodatniości drugiego P.
7. **Skończony koszt a zanik stanu:** w czasie dyskretnym rozkład x_{k+1}=(A−LC)x_k+Bu_k+LCx_k, z wymuszeniem w l², a w ciągłym jego odpowiednik z wymuszeniem w L². Rozdzielenie splotu na skończoną część początkową i mały ogon dowodzi zaniku stanu dla dowolnego sterowania o skończonym koszcie, przy wykrywalności C,A.
8. **Optymalność nieskończonego horyzontu:** obie dokładne tożsamości z dodatkowym kwadratem zostały wyprowadzone z CARE/DARE. Zanik stanu uzasadnia pozbycie się końcowego składnika x_N*Px_N lub x(T)*Px(T). Sprzężenia stabilizujące osiągają minima, a dodatniość R i M zapewnia jednoznaczność.
9. **Przykłady:** skalarny A=2, B=1, Q=4/5, R=1, P=4, K=8/5, zamknięty współczynnik 2/5; ciągły A=1, Q=3, P=3, K=3, D=−2. Dwuwymiarowe przykłady z zerowym drugim składnikiem Q pokazują P≥0 ale P nie>0. Kontrprzykłady Q=0, A niestabilne i B=0 przedstawiają odrębne przeszkody braku wykrywalności i stabilizowalności.

## Weryfikacja techniczna

- Dodano niezależny test arytmetyki wymiernej `tools/test_linear_algebra_general_riccati.py`, obejmujący 500 dokładnych przypadków tożsamości kosztu, CARE/DARE, zbieżność skalarnej rekurencji i oba rodzaje kontrprzykładów.
- Rozdział dołączono do `books/pl/linear_algebra.tex` i `catalog/books.json`; walidator CI wymaga 26 rozdziałów i wykonuje nowy test.
- Do stabilizacji wymagane są **dwa kolejne czyste audyty** po ostatniej korekcie, zielone CI bez ostrzeżeń, kontrola wszystkich odsyłaczy i wizualnie zweryfikowany PDF wyłącznie rozdziału 26.

**Decyzja:** rozdział 26 **w audycie**, bez deklaracji stabilizacji przed pomyślnym zakończeniem testów i składu.
