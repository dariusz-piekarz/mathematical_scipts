# Algebra liniowa — rozdział 14, audyt III (poprawność, przypadki graniczne, PDF)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/14-wartosci-wlasne-diagonalizacja-i-twierdzenie-spektralne.tex`  
**Sprawdzony blob tekstu:** `09fda2f083ad5fbd752699606d42862eb7022987`  
**Poprzednie audyty:** `ch14_iteration_01.md`, `ch14_iteration_02.md`.

## Założenia i samodzielność matematyczna

W trzecim audycie sprawdzono rozdział bez dodawania twierdzeń i bez zmieniania jego zawartości. Kontrola objęła niezależnie: źródła przyjętych założeń, brak błędnego koła we wnioskowaniu, rzeczywiste i zespolone przestrzenie iloczynu skalarnego, ciała dowolnej charakterystyki w części algebraicznej, przypadek zerowego wymiaru, przykłady oraz wynik drukarski.

1. **Wielomian charakterystyczny.** Zmiana bazy `A' = P^{-1}AP` nie zmienia `det(tI-A)`; argument używa wyłącznie skończonego wymiaru i własności wyznacznika. W wymiarze zero przyjęto moniczny wielomian stały `1`, bez pierwiastków i bez wektorów własnych. Zależność `g_T(λ)≤a_T(λ)` pochodzi z bloku `λI_g` w macierzy po uzupełnieniu bazy przestrzeni własnej.
2. **Diagonalizacja.** Niezależność różnych przestrzeni własnych wynika z zastosowania wielomianu `∏_{j≠k}(T-λ_jI)`, bez założenia istnienia odpowiedniego iloczynu skalarnego. Kryterium krotności wymaga jawnie rozszczepienia `χ_T` nad rozważanym ciałem. Wykazano różnicę między krotnościami w przykładzie bloku Jordana; w szczególności diagonalizacja nad `C` nie musi wynikać z postaci Schura.
3. **Twierdzenie Schura.** Indukcja działa na `S=P_W T|_W` przy `W=e_1^⊥`, nie na `T|_W`, gdy `T` jest dowolny. Nie przypisano kompresji własności, której nie wymaga indukcja. Fakt, że początkowy wektor własny ma długość jeden, jest użyty prawidłowo.
4. **Normalność.** Równość `||Nv||=||N^*v||` i normalność `T-λI` są dowiedzione `przed` twierdzeniem spektralnym. Stąd `Tv=λv⇒T^*v=conj(λ)v`, a w dalszym dowodzie `W=e_1^⊥` jest niezmiennicza zarówno dla `T`, jak i `T^*`. Ograniczenie pozostaje normalne. Nie wykryto rozumowania kołowego.
5. **Rzeczywisty przypadek symetryczny.** Po zespoleniu macierzy `A=A^T` otrzymujemy `A=A^*`, więc wszystkie zespolone wartości własne są rzeczywiste. Z `A(x+iy)=λ(x+iy)`, `λ∈R`, dostajemy rzeczywisty niezerowy wektor własny (część rzeczywista lub urojona). Indukcja na jego rzeczywistym dopełnieniu ortogonalnym jest poprawna. Przeciwprzykład rotacji `[[0,-1],[1,0]]` wyjaśnia różnicę z ogólnymi rzeczywistymi operatorami normalnymi.
6. **Rzuty spektralne.** Dla normalnego `T` różne przestrzenie własne są ortogonalne. Wielomiany interpolacyjne `q_j` spełniają `q_j(λ_i)=δ_{ij}`, co dowodzi tożsamości `P_j=q_j(T)` na każdej składowej ortogonalnego rozkładu. Zastosowanie do `tr T`, `det T`, `T^{-1}` i `p(T)` jest zgodne z krotnościami własnymi; pusta suma w przestrzeni zerowej jest zerowym operatorem, będącym też identycznością tej przestrzeni.
7. **Iloraz Rayleigha.** Współczynniki `|c_j|²/Σ|c_j|²` są nieujemne i sumują się do `1`, dlatego iloraz jest średnią ważoną rzeczywistych wartości własnych. Warunki równości wymagają zaniku współrzędnych spoza odpowiedniej skrajnej przestrzeni własnej i pozostają poprawne przy wielokrotnej skrajnej wartości własnej.
8. **Określoność i norma.** `h(u,Tv)` jest hermitowska przy `T=T^*`, a jej określoność jest równoważna znakom wartości własnych. W niezerowym skończonym wymiarze norma operatora normalnego jest maksimum modułów wartości własnych; dla `V=0` odrębnie unika się maksimum pustego zbioru.
9. **Przemienne operatory samosprzężone.** Każda przestrzeń własna `S` jest niezmiennicza dla przemiennego `T`; ograniczenie `T` jest samosprzężone. Ortogonalne połączenie baz własnych ograniczeń daje wspólną bazę, również przy powtórzonych wartościach własnych.
10. **Weryfikacja przykładów.** Dla `H=[[2,i],[-i,2]]` wartości własne są `1,3`, a zespolone wektory własne `(-i,1)/sqrt(2)` i `(i,1)/sqrt(2)` są ortonormalne. Dla `A=[[2,1],[1,2]]` rzuty `(A-I)/2` i `(3I-A)/2` są ortogonalnymi idempotentami sumującymi się do identyczności.
11. **Język i typografia.** Zweryfikowano czytelność wszystkich 12 stron pojedynczego rozdziału w wyrenderowanych obrazach; nie widać uciętych wzorów, kolizji tekstu ani pustych ram. Pełny PDF ma 151 stron. Log kompilacji nie zawiera ostrzeżeń o nierozwiązanych odsyłaczach, `Overfull`, `Underfull`, brakujących znakach ani błędach LaTeX.

## Wzmocnienie regresji i stała zasada dostarczania PDF

Dotychczasowe testy obliczeniowe obejmowały głównie macierze `2×2`. Do `tools/test_linear_algebra_spectral.py` dodano niezależne kontrole dla `3×3`: powtórzone wartości własne, przestrzenie własne wymiaru większego niż jeden, odtwarzanie projekcji za pomocą wielomianów interpolacyjnych, wzajemną ortogonalność rzutów, sumę rzutów, rekonstrukcję operatora i rachunek wielomianowy. **Nie wprowadzano nowych twierdzeń do tekstu rozdziału.** Regresje zakończyły się sukcesem w [GitHub Actions 44928372100](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44928372100).

W repozytorium dodano `tools/export_linear_algebra_chapter_pdf.py` i etap `Export latest audited chapter as a standalone PDF` w `.github/workflows/linear-algebra-chapter.yml`. CI publikuje osobny artefakt `linear-algebra-current-chapter`, który obejmuje tylko bieżący rozdział i zachowuje oryginalne numery stron książki. Eksport przeszedł już kompletny CI [44928270945](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44928270945); otrzymany plik ma **12 stron i zaczyna się od rozdziału 14**.

**Zasada prezentowania wyników ustalona przez użytkownika:** jednorazowo pokazujemy PDF całej dotychczasowej książki. W następnych iteracjach audytów pokazujemy użytkownikowi wyłącznie **PDF aktualnie audytowanego rozdziału**, nie cały tom. Pełną książkę nadal kompiluje CI i pozostaje ona w repozytorium.

## Podsumowanie

**Audyt III — czysty.** Nie znaleziono podstaw do matematycznej poprawki w rozdziale 14; jego tekst pozostaje niezmieniony (blob wskazany powyżej). Wzmocniono testy 3×3 i sposób dostarczania PDF. Rozdziały **01–14 pozostają stabilne**. Następny etap tworzenia materiału to rozdział 15; przyszłe audyty mają udostępniać wyłącznie jego samodzielny PDF.
