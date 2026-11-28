# Logika matematyczna i teoria mnogości — audyt VII rozdziału 35

**Data:** 22 listopada 2026.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Blob źródła przed audytem:** 53b8d212d00a6f92e710d91fb35b6a7805eb5388.  
**Blob źródła po audycie:** 89cdd6dcb3e77889b0b7ca67f0b8765f3940bdea.  
**Testy:** tools/tests/test_logic_and_set_theory_ch35.py, 20 metod.  
**Werdykt:** **audyt VII nie jest czysty**: konieczne było rozwinięcie kluczowej części argumentu dotyczącej wartości boolowskich CH i jej zaprzeczenia. Po poprawkach wszystkie testy i kompilacja PDF zakończyły się sukcesem. Licznik niezależnych czystych audytów: **0**.

## 1. Zakres niezależnego audytu

Na źródle z audytu VI ponownie przeanalizowano całość dowodu: zupełność RO(P), gęstość i(P), definicję klas nazw boolowskich, wartości formuł i podstawianie, lemat mieszania i pełności, argumenty dla wszystkich aksjomatów ZFC, iloraz przez **dowolny** zewnętrzny ultrafiltr, dokładność przekładu między porządkiem a algebrą oraz końcowy wniosek Con(ZFC) ⇒ Con(ZFC+CH) i Con(ZFC) ⇒ Con(ZFC+¬CH). Potwierdzono rozróżnienie między wewnętrzną zupełnością B w dowolnym M\models ZFC a zupełnością względem zewnętrznych rodzin. Iloraz nie musi być zewnętrznie dobrze ufundowany.

Niezależnie porównano strukturę dowodu z opisem pełnych modeli boolowskich i ilorazów przez ultrafiltry (https://jdh.hamkins.org/a-gentle-introduction-to-boolean-valued-model-theory/) oraz formalnym dowodem niezależności CH bez założenia przeliczalnego modelu tranzytywnego (https://florisvandoorn.com/papers/flypitch-cpp-2020.pdf). Takie porównanie stanowi kontrolę merytoryczną, nie weryfikację źródła w Lean.

## 2. Uzupełnienie dowodu wartości boolowskiej zaprzeczenia CH

W poprzedniej wersji wykazanie zachowania kardynałów przez ccc ograniczało się do streszczenia metody antyłańcuchów. To nie wystarczało dla rygoru rozdziału, który ma uzasadniać **syntaktyczne** twierdzenia ZFC, niezależnie od istnienia modelu tranzytywnego i zewnętrznego filtru generycznego.

Teraz dowód jawnie konstruuje:
1. Przeniesienie ccc z P_C=Add(ω,ω₂) do B_C=RO(P_C) przez wybór warunków 0<i(p_a)≤a dla elementów każdego antyłańcucha A.
2. Redukcję potencjalnego zmniejszenia kanonicznych ω₁ i ω₂ do surjekcji check β→check λ na niezerowym fragmencie, z β<λ, λ∈{ω₁,ω₂}. Uzasadnienie redukcji: wartość „τ∈check λ” jest supremum wartości „τ=check β”, β<λ.
3. Na dodatnim fragmencie b dla funkcji f:check β→check λ wybór nazw wartości v_ξ dzięki pełności, następnie maksymalnych antyłańcuchów A_ξ pod wartościami „v_ξ=check η”. Każdy jest przeliczalny na mocy ccc, więc zbiór S wszystkich dopuszczalnych wartości ma moc ≤max(ℵ₀,|β|)<λ. Wybranie η∈λ\S przeczy surjektywności. Jest to bezpośredni argument boolowski w ZFC.
4. Jawne sprawdzenie, że check ω₁ i check ω₂ są pierwszymi dwoma nieprzeliczalnymi kardynałami także w uniwersum boolowskim: wszystkie nazwy liczb porządkowych mniejszych od check ω₂ są na odpowiednich fragmentach równoważne pewnym kanonicznym check α; stare bijekcje nie przestają świadczyć o nie-kardynalności.
5. Zbudowanie nazw Cohenowskich podzbiorów ω ze współczynnikami b_{α,n}=∨{i(p):p(α,n)=1}; wykazanie [[c_α≠c_β]]=1 dla różnych α,β za pomocą zbioru gęstego warunków rozdzielających współrzędne. Nazwa grafu iniekcji check ω₂→Π_{check ω} odwołuje się już do **faktycznie skonstruowanej** w rozdziale nazwy zbioru potęgowego, nie do nieformalnego wyrażenia P(check ω). Wynika stąd wartość 1 zaprzeczenia CH.

## 3. Uzupełnienie dowodu wartości boolowskiej CH

Zastąpiono ogólne stwierdzenie o braku nowych funkcji ω→Ord precyzyjnymi argumentami wystarczającymi do CH, które nie zakładają istnienia filtru generycznego ani modelu tranzytywnego.

Dla przeliczalnie domkniętego P_H=Coll(ω₁,λ), λ=2^{ℵ₀}, i dowolnej nazwy x będącej na fragmencie i(p) podzbiorem check ω, rozpatrujemy b_n=[[check n∈x]]. Poniżej każdego r≤p konstruujemy ciąg p₀=r≥p₁≥… decydujący b_n; przeliczalna domkniętość daje wspólne wzmocnienie q. Definiujemy **w zbiorze wyjściowym** x₀={n∈ω:i(q)≤b_n} i otrzymujemy i(q)≤[[x=check x₀]]. W konsekwencji dla każdej nazwy x:
[[x⊆check ω]] = ∨_{x₀⊆ω} [[x=check x₀]] = [[x∈check P(ω)]].
Jest to ścisły argument braku nowych podzbiorów ω.

Dla dowolnej nazwy funkcji check ω→check ω₁ stosujemy pełność oraz rozdzielność wartości przynależności do check ω₁. Kolejno wybieramy wzmocnienia rozstrzygające wszystkie jej wartości, korzystając z przeliczalnej domkniętości, i otrzymujemy starą funkcję g:ω→ω₁. Nie może ona być surjekcją, więc check ω₁ pozostaje pierwszą nieprzeliczalną liczbą porządkową.

Surjekcję check ω₁→check λ opisują jawne współczynniki d_{ξ,η}=∨{i(p):p(ξ)=η}. Dla każdego ξ są parami rozłączne, a ich supremum po η wynosi 1. Dla każdego η supremum po ξ również wynosi 1, gdyż każdy przeliczalny warunek można przedłużyć na świeżej współrzędnej. Graf z tych współczynników jest zatem nazwą surjekcji o wartości 1. Łącznie z poprzednimi własnościami daje to [[CH]]=1.

Dodatkowo poprawiono ścisły zapis check(ω₁), check(ω₂) przez klamry wokół indeksowanych symboli, aby akcent \check obejmował całą liczbę porządkową, oraz doprecyzowano różnicę pomiędzy funkcją binarną a reprezentującym ją podzbiorem ω.

## 4. Testy, LaTeX i CI

W pliku tools/tests/test_logic_and_set_theory_ch35.py dodano **test_three_atom_decision_of_finite_named_real**, który w algebrze P({0,1,2}) rozpatruje wszystkie 8⁴=4096 czterowspółrzędne nazwy podzbiorów i trzy atomy, dając **12 288** weryfikacji jednoznacznego rozstrzygnięcia przez nazwę kanoniczną, wszystkich PASS. Łącznie **20 metod** rozdziału 35. Nadal obowiązują testy z poprzednich iteracji: 40 446 porównań przynależności i równości w małych preorderach, wszystkie 388 preorderów na co najwyżej czterech punktach i sprawdzenia trójatomowe.

Struktura po zmianach: **8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 różnych etykiet, 32 odsyłacze**. Brak niedomkniętych środowisk; zgodny inwentarz odsyłaczy książki.

**Pełna GitHub Actions [45053454090](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45053454090): SUCCESS**, commit 7779da912108dd876a2dbefa050ffb37adcb11a1, obejmujący ostatnią zmianę źródła. Wszystkie kroki testowe, kompilacja książki i kontrola PDF przeszły. Pobrano faktyczny artefakt końcowego przebiegu, książka ma **310 stron**, rozdział 35 obejmuje PDF **strony 296–310 (15 stron)**. Wyrenderowano i przejrzano montaż wszystkich 15 stron oraz powiększone strony 307–309 z nowym argumentem. Brak wizualnych kolizji i ucięć. Log: **0 błędów LaTeX**, **0 przepełnionych wierszy**, **1 underfull hbox** w całej książce, **0 nierozwiązanych odsyłaczy**.

## 5. Status stabilności

Audyt VII ujawnił faktyczny niedostatek dowodu i doprowadził do znaczącej rozbudowy części dotyczącej obydwu rozstrzygnięć CH. **Nie wolno zaliczać audytu VII jako czystego; licznik czystych audytów nadal wynosi 0.** Następny etap: niezależny audyt VIII na blobie 89cdd6dcb3e77889b0b7ca67f0b8765f3940bdea, bez opierania się na wnioskach audytu VII. Po uzyskaniu stabilności — dodatkowy audyt potwierdzający na identycznej wersji. Żaden z testów, ani sam zielony CI/PDF, nie stanowi formalizacji tych twierdzeń w Lean.
