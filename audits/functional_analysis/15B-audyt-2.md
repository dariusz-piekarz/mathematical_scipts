# Analiza funkcjonalna — 15B/02 — audyt poprawkowy Fubiniego i całkowitej wariacji

**Data:** 24 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (istniejąca).  
**Źródło:** `chapters/pl/functional_analysis/15B-calki-bochnera-pettisa-dunforda-i-gelfanda-oraz-miary-wektorowe.tex`.  
**Źródło przed iteracją:** blob `78680e4099da22d4394c3b2944001f3c29a59b1a`.  
**Źródło po iteracji:** blob `89cc07f494e18ab0d4eba2a7e588c7cec2176de3`.  
**Test przed iteracją:** blob `688fb39f272b62be6c161dbf25b57ddafcd5f8e4`.  
**Test po iteracji:** blob `f151fd30e4dd415695444a454462497569fcb852`.  
**Decyzja:** **audyt poprawkowy, 0/2 czystych przeglądów** po aktualizacji źródła; nie przechodzić do rozdziału 16.

## Usterki i wykonane poprawki

### 1. Fubini dla funkcji Bochnerowskich

W dotychczasowym dowodzie `thm:bochner-fubini15b` po przybliżeniu funkcjami prostokątnymi stwierdzano w jednym kroku istnienie całek po przekrojach i ich identyfikację z granicą funkcji przybliżających. W szczególności brakowało uzasadnienia dla funkcji silnie mierzalnej względem **uzupełnienia** miary produktowej: przekroje dowolnej funkcji mierzalnej względem uzupełnienia nie muszą być mierzalne dla *każdego* punktu parametru, a jedynie dla prawie wszystkich.

Rozwinięto dowód następująco:
1. Skoro silna mierzalność oznacza granicę **ciągu** funkcji prostych prawie wszędzie, każdy zbiór występujący w tych prostych funkcjach można zastąpić przedstawicielem z nieuzupełnionej produktowej `sigma`-algebry. Po odrzuceniu wspólnego produktowego zbioru miary zero otrzymuje się produktowo silnie mierzalnego przedstawiciela `\widetilde f`.
2. Skalarne twierdzenie Tonellego zapewnia, że przekroje odrzuconego zbioru są zerowe dla prawie wszystkich wartości każdego parametru. W tezie jawnie zaznaczono konwencję całkowania względem **uzupełnionej** miary produktowej.
3. Skończone kombinacje prostokątnych funkcji wskaźnikowych z wartościami wektorowymi są gęste w `L^1(S\times T;X)` dla miar skończonych; jest to skutek argumentu klasy monotonicznej i aproksymacji funkcji prostych.
4. Wybieramy `g_n` z błędem `\int\|f-g_n\|<4^{-n}`. Po zastosowaniu Tonellego sumy błędów po przekrojach są skończone dla prawie każdego parametru; stąd istnieją całki Bochnera przekrojów i `g_n(s,\cdot)\to f(s,\cdot)` w `L^1(T;X)` dla prawie każdego `s`.
5. Funkcje `F_n(s)=\int_Tg_n(s,t)\,d\nu(t)` są proste, `F_n\to F` prawie wszędzie oraz w `L^1(S;X)`, z oszacowaniem `\int_S\|F-F_n\|\le\int_{S\times T}\|f-g_n\|`. Pozwala to legalnie zidentyfikować całki iterowane i powrócić do pierwotnej funkcji z dokładnością do zbiorów miary zero.

**Wynik:** brakujący argument o przekrojach oraz całkach iterowanych został zapisany w źródle; nie przypisujemy prawdziwości bez dowodu każdemu przekrojowi funkcji z uzupełnionej przestrzeni produktowej.

### 2. Całkowita wariacja miary wektorowej

Definicja `def:vector-measure15b` określała `|m|` słowem „miara” bez podania uzasadnienia jej przeliczalnej addytywności. Dodano oddzielne `stwierdzenie`, `prop:variation-measure15b`, obejmujące również wartości nieskończone, z dowodem:
- dla rozłącznych `A_n`, zestawienie partycji skończenie wielu `A_n` w partycję ich sumy (z dodanym dopełnieniem) daje `|m|(\bigcup_nA_n)\ge\sum_n|m|(A_n)`;
- dla dowolnej partycji `B_j` ich sumy, rozkład `B_j=\bigcup_n(B_j\cap A_n)`, przeliczalna addytywność wektora `m` w normie i nierówność trójkąta dają `\sum_j\|m(B_j)\|\le\sum_n|m|(A_n)`;
- supremum po partycjach daje nierówność przeciwną.

W konsekwencji użycie `|m|` w twierdzeniu `thm:bochner-measure15b` i definicji RNP ma pełne uzasadnienie w tekście.

## Kontrola pozostałej matematyki i czterech przykładów

1. Twierdzenie Pettisa o mierzalności: przeliczalna rodzina funkcjonałów normujących ośrodkową podprzestrzeń, mierzalne kule, truncacja ogonów i Borel–Cantelli są poprawne; uwzględniono bezpośrednio przypadek zerowej podprzestrzeni.
2. Kryterium całki Bochnera: aproksymacja `L^1`, szacowanie przez `3\|f\|` oraz ciągłość całki względem operatorów ograniczonych są poprawne.
3. Zbieżność zmajoryzowana dla Bochnera: podwójna aproksymacja funkcji prostych i oszacowanie miar błędów `2^{-n}` daje zbieżność prawie wszędzie zgodnie z Borel–Cantellim.
4. Zgodność Riemanna i Bochnera: funkcja ciągła na odcinku jest jednostajnie aproksymowana funkcjami prostymi; `\chi_{\mathbb Q\cap[0,1]}x_0` dla `x_0\ne0` ilustruje brak implikacji odwrotnej.
5. Dunford: `Q_f:X'\to L^1` ma domknięty wykres, dzięki czemu element `D_A\in X''` istnieje i ma żądane oszacowanie. Różnica między reprezentacją w `X` a `X''` jest zachowana.
6. Hierarchia Bochner–Pettis–Dunford: przejście przez każdy `x'\in X'` jest legalne, a `J_X` zachowuje sens dla niekoniecznie refleksywnej `X`.
7. Zbieżność dla Pettisa: refleksywność zapewnia reprezentację Dunforda w `X`, a jawna mierzalność norm różnic umożliwia skalarne twierdzenie o zbieżności zmajoryzowanej. Nie wnioskujemy nielegalnie o silnej mierzalności.
8. Całka Gelfanda: domknięty wykres operatora `Q:Y\to L^1` daje element `Y'`; addytywność przeliczalna jest gwarantowana w topologii słabej-*, niekoniecznie w normie.
9. Wariacja miary generowanej przez Bochnera: równość dla funkcji prostych otrzymuje się z partycji przez zbiory poziomicowe, a przejście do `f\in L^1` z oszacowania różnicy wariacji przez `\int_A\|f-g\|`.
10. Przykład `c_0`: `f(n)=2^ne_n` przy `\mu(\{n\})=2^{-n}` ma Dunforda `(1,1,\dots)\notin c_0` i nieskończoną całkę normy.
11. Przykład `\ell^2([0,1])`: dla `f(t)=e_t` skalaryzacje znikają poza przeliczalnym nośnikiem, a obraz poza zbiorem miary zero nie mieści się w ośrodkowej podprzestrzeni.
12. Przykład Gelfanda w `\ell^\infty`: ogony `\chi_{\{m,m+1,\ldots\}}` zbiegają słabo-* do zera, mimo normy równej 1.
13. Przykład bez RNP: dla `m(A)(t)=\mu(A\cap[0,t])` uzyskuje się `|m|(A)=\mu(A)`, lecz istnienie pochodnej Bochnera w `C([0,1])` prowadziłoby do skokowej funkcji wartości na gęstym zbiorze argumentów, sprzecznej z ciągłością.

## Regresje i stan techniczny

Rozszerzono `tools/tests/test_functional_analysis_ch15b.py` z dwóch do **pięciu** testów: zachowano kontrolę relacji LaTeX i budżetu błędu diagonalnego, dodano dokładne całkowanie wektorowe na skończonej przestrzeni produktowej (obie kolejności i całka produktowa), test wariacji przez enumerację partycji czterech atomów w normie `\ell^1` oraz kontrakt obecności dowodu o przekrojach i stwierdzenia o wariacji. Takie skończone testy są świadkami regresyjnymi, nie dowodami twierdzeń ogólnych.

Dodano dedykowany workflow `.github/workflows/functional-analysis-ch15b.yml` w commicie [d2915fb7d7db](https://github.com/dariusz-piekarz/mathematical_scipts/commit/d2915fb7d7dbbc57b98b5cc6e043faca9c8fd398): regresje modułu 15B, generowanie prawdziwego kontekstu 01–17 z 15A i 15B, kompilacja PDF, kontrola tekstu, diagnostyki LaTeX i odsyłaczy, upload artefaktu.

Po poprawce źródło ma **575 wierszy, 23 etykiety, 11 poprawnie sparowanych dowodów**; 9 środowisk `twierdzenie`, 2 `stwierdzenie`, 6 `definicja`, 4 `przyklad` i 3 `uwaga`. Nowa etykieta `prop:variation-measure15b` ma jedno wystąpienie. Brak nowych rysunków TikZ. Zamknięcie kontroli PDF, odsyłaczy i wyników dedykowanego workflow wymaga potwierdzenia zakończonego przebiegu po niniejszych zmianach.

## Werdykt

**15B/02 — naprawczy, 0/2.** Dwa istotne rozwinięcia dowodowe zapisano w źródle, dodano testy i bramkę CI. Nie twierdzimy, że samo uruchomienie workflow oznacza sukces. Następny audyt 15B/03 może być pierwszym czystym dopiero po kontroli niezmienionego źródła oraz potwierdzeniu działania testów, kompilacji i gotowego PDF. Nie przechodzić do rozdziału 16 przed stabilizacją 15B.
