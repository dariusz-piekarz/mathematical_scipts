# Algebra liniowa — rozdział 24, audyt III (drugi niezależny, czysty)

**Data:** 21 listopada 2026  
**Tekst:** `chapters/pl/linear_algebra/24-rownania-riccatiego-i-sterowanie-liniowo-kwadratowe.tex`.  
**Kontrolowany blob:** `ae1d94e8a95838225b254096e284f98f571cc829`.  
**Wcześniejsze iteracje:** I (uzupełnienie dowodu DARE), II (pierwszy czysty przegląd).

## Pełna kontrola twierdzeń i hipotez

1. `n,m≥1`, `A∈M_n(C)`, `B∈M_{n×m}(C)`, `Q>0` hermitowska i `R>0` hermitowska zostały wprowadzone jawnie. Każdy wyraz CARE i DARE ma rozmiar `n×n`, każda macierz `K` rozmiar `m×n`. Również przypadek `B=0` jest dopuszczalny i nie powoduje wyjątku.
2. Lemat uzupełniania kwadratu działa w przestrzeni zespolonej: człony mieszane są sprzężone, ich suma daje `2Re(u*c)`, a minimum jest osiągane tylko w `u=-M^-1c`.
3. Dyskretny koszt dla `N=0` jest zerowy; P_0=0. Krok Bellmana nie wymaga żadnych nieuzasadnionych własności wyprowadzonego ciągu; `M_N=R+B*P_NB>0` wynika indukcyjnie. Z formuły na minimum wynika zarówno hermitowskość, jak i nieujemna określoność `P_{N+1}`.
4. Monotoniczność `P_N` i górne oszacowanie `W` przy stabilnym A są poprawne: koszty nieujemne, zerowe sterowanie daje skończoną sumę niezależną od N.
5. Zbieżność `P_N` jest udowodniona przez kwadratowe formy i polaryzację, nie przez niejawne twierdzenie o monotonicznych operatorach. Macierz `P>=Q` pozostaje dodatnia. Ciągłość odwracania `M_N` jest uzasadniona jednostajnym dolnym oszacowaniem przez R.
6. CARE/DARE: oba sprzężenia zwrotne mają prawidłowy znak i kolejność czynników. Rozwinięcie `(A-BK)*P(A-BK)` w DARE oraz `(A-BK)*P+P(A-BK)` w CARE daje odpowiednie równania Lapunowa, w których prawa strona jest ściśle ujemnie określona.
7. **Kluczowa jednoznaczność DARE.** Dla *dwóch* stabilizujących rozwiązań `P_1,P_2` wystarczy odwracalność `M_i`, nie trzeba `M_i>0`. Po odjęciu równań i podstawieniu `M_i K_i=B*P_iA` otrzymujemy `D=(A-BK_1)*D(A-BK_2)`. Iteracja daje `D=(A_1*)^k D A_2^k`, zanik obydwu potęg wymusza D=0. Przypadek skalarny z P_1=1 i P_2=-7/8 niezależnie potwierdza tożsamość, choć P_2 nie jest stabilizujące.
8. W nieskończonym horyzoncie dyskretnym nie zakłada się a priori zaniku dowolnej trajektorii: wynika on z jej skończonego kosztu i `Q>0`. W czasie ciągłym użyto mocniejszego argumentu `x,u,x'∈L²`, po czym całkowanie pochodnej `||x||²` uzasadnia granicę x(t)=0. To zapewnia poprawne przejście do granicy w obu tożsamościach kosztu.
9. DRE: lokalna lipschitzowskość wielomianowego równania w współczynnikach S, niezmienniczość klasy hermitowskiej, obliczona pochodna `x*S(T-s)x`, osiągnięcie minimum przez ciągłe sprzężenie, nieujemność i ograniczenie z góry przez zerowe sterowanie gwarantują globalne rozwiązanie. Nie zakłada się stabilności A w twierdzeniu o skończonym horyzoncie.
10. Dopiero dla nieskończonego horyzontu i algebraicznych granic wymagana jest stabilność A. Zbieżność macierzy S(t) wynika z monotoniczności i ograniczenia, dodatnia określoność z osiągniętego dodatniego kosztu dla x_0≠0. Graniczna pochodna F(P)=0 jest wymuszona zbieżnością S i ciągłością F.
11. Ciągłe CARE ma jednoznaczne rozwiązanie stabilizujące w klasie Hermitowskiej, bez dodatniej określoności drugiego rozwiązania. Każde rozwiązanie nieujemne jest automatycznie dodatnio określone, gdyż istnienie niezerowego wektora w jądrze przeczyłoby równaniu Lapunowa z ujemnie określoną prawą stroną.
12. Unikalność sterowania w czasie ciągłym jest prawidłowo sformułowana jako równość **prawie wszędzie**. Przedziałami ciągłe funkcje różniące się w izolowanych punktach mają ten sam koszt i trajektorię; tekst nie twierdzi już inaczej.

## Kontrola rachunkowa

Niezależne obliczenia SymPy na arytmetyce wymiernej potwierdzają dla
`A=[[1/2,1/2],[0,1/4]]`, `B=I`, `R=I`,
`Q=[[7/8,-1/8],[-1/8,27/32]]`, `P=I`
dokładny zerowy residuum DARE i sprzężenie `K=A/2`.
Dla CARE z `A=[[-1,1/3],[0,-2]]`, `Q=I-A*-A`, `B=R=P=I` residuum także jest zerowe.
Skalarna rekurencja DARE daje kolejno `7/8, 119/120, 1911/1912, 30583/30584`, ściśle rosnąc do `1`. Zapis `8p²-p-7=0` ma pierwiastki dokładnie `1` i `-7/8`.
Dla CARE `s(t)=3(1-e^{-4t})/(3+e^{-4t})` spełnia `s'=(1-s)(s+3)`, `s(0)=0` i `s(t)→1`.

## Struktura

- 26 różnych etykiet, 31 odsyłaczy; brak niezdefiniowanych etykiet `lin24` w samym rozdziale.
- Występują 8 otwarć i 8 zamknięć środowiska `proof`, 4 twierdzenia i 4 definicje; pozycje `\index` zachowują konwencję całej książki.
- Brak zakazanych form terminologicznych z `AGENTS.md`.
- Test `tools/test_linear_algebra_riccati.py` korzysta wyłącznie z dokładnych ułamków `fractions.Fraction`; wszystkie jego kroki zostały zaliczone we wczesnej części CI. Weryfikacja końcowego PDF i logu jest osobnym wymogiem.

**Decyzja:** **Audyt III czysty** matematycznie i redakcyjnie, bez zmian w źródle; druga kolejna czysta iteracja po korekcie audytu I. Status techniczny pozostaje otwarty do zielonej pełnej kompilacji i kontroli samodzielnego PDF.
