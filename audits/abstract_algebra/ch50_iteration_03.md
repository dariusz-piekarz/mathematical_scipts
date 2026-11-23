# AA-50 — audyt III: stabilizacja trzeciego przypadku algorytmu Kovacica

**Data:** 23 listopada 2026 r.
**Werdykt:** **AA-50 STABILNY w jawnie określonym zakresie**, z wyraźnym wskazaniem cytowanych twierdzeń klasycznych.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/abstract_algebra/50-trzeci-przypadek-kovacica-i-skonczone-grupy-galois.tex.
**Blob SHA finalnego rozdziału:** 4661b8577ed96b126a2fa8e5be8e7004c31d572c.
**Blob SHA regresji SymPy:** 0896a46103c51c69b3ee82901699f9675e97d1cd.
**Blob SHA niezależnych regresji Fraction:** 47d089b74f174be7876225e5e9ea1a0b4c38fa19.
**Dokument zakresu:** docs/pl/zakres_aa50_kovacic_skonczone_grupy.md.
**Poprzedni etap:** AA-49 STABILNY.

## 1. Trzy rzeczywiście wykonane audyty

- Audyt I: audits/abstract_algebra/ch50_iteration_01.md; sprawdzono budowę działu, model obliczeń, definicje i klasyczne granice kompletności trzeciej gałęzi.
- Audyt II: audits/abstract_algebra/ch50_iteration_02.md; niezależnie wyprowadzono równanie transportu i odzyskanie pierwiastków Riccatiego; przeliczono przykłady czworościenny, ośmiościenny i dwudziestościenny oraz przypadki graniczne. Po tym audycie dodano definicję prymitywnej dwuwymiarowej reprezentacji i osobny dowód wzoru na różnice wykładników indycjalnych.
- Audyt III: końcowa kontrola wszystkich 25 testów, pełnego CI i ostatecznej 322-stronicowej książki, po ostatniej korekcie językowej i aktualizacji front matter.

**Substancjalna rozbudowa:** pierwotny rozdział zawierał jeden przykład dodatni (n=4); dodano modele typu ośmiościennego (n=6) i dwudziestościennego (n=12). W obu przypadkach dokładne rozwinięcie wszystkich kroków rekurencji daje P_{−1}=0. Udokumentowano listy E0,E1,E∞, Sθ i S²q.

**Korekty po CI:** pierwszy test stopnia potencjału uruchamiał SymPy.degree na niesprowadzonym wyrażeniu wymiernym i rzucał PolyError; następnie poprawiono analogiczny test w drugim miejscu. W niezależnym teście liczono błędnie liczbę indeksów rekurencji: od P_{n+1} do P_{−1} włącznie są n+3 elementy, czyli 9 dla n=6 i 15 dla n=12. Poprawiono **testy**, nie tożsamości matematyczne. Commity d3bab28670b5a9b0d26dab9be3197de2900b099c, dcb08ced549da4e1d2a7910e8d35ba64887baf9f i e352973ce00948876f325f899867186b9cf47147.

**Korekta językowa i metadanych:** „Lemma” zamieniono na polskie „Lemat” oraz wpisano ukończenie AA-01–AA-50 na stronie tytułowej. Commit 4103a830163f9abcebca492d26e58f33e9784f82.

## 2. Ostateczne sprawdzenie matematyczne

1. **Skończone grupy.** Dla skończonej prymitywnej różniczkowej grupy Galois równania z''=qz projektowe typy A4, S4, A5 i odpowiadające im parametry n=4,6,12 są **wynikiem klasycznym cytowanym z Kovacica (1986)**. Samodzielnie zdefiniowano prymitywność dwuwymiarowej reprezentacji, lecz nie przypisano sobie dowodu klasyfikacji skończonych podgrup PSL2(C).
2. **Listy lokalne.** Warunki dla q (bieguny rzędu 1 lub 2, ord∞ q≥2) i listy E_c(n), E∞(n) są jawnie cytowanymi twierdzeniami klasycznymi. Zostały dokładnie przepisane, w tym osobny przypadek ord∞>2. Testy weryfikują dokładną całkowitość, nie przybliżenia.
3. **Stopień i rekurencja.** Dla każdej kombinacji e_c,e∞ oblicza się d=(n/12)(e∞−Σe_c) i θ=(n/12)Σe_c/(x−c). Przy skończonych biegunach q rzędu najwyżej 2 funkcje Sθ i S²q są wielomianami. Rekurencja P_{n+1}=0, P_n=−P, P_{i−1}=−SP_i'+((n−i)S'−Sθ)P_i−(n−i)(i+1)S²qP_{i+1} jest liniowa w P. Warunek P_{−1}=0 daje dokładny skończony układ równań liniowych.
4. **Równanie transportu z pełnym dowodem.** Dla F(x,T)=Σ_{i=0}^{n} S^iP_i T^i/(n−i)! oraz D=∂_x+(q−T²)∂_T z rekurencji i warunku końcowego wynika D F=(-nT+nS'/S−θ)F. Wprost porównano każdy współczynnik T^i, włącznie z potęgą T^{n+1}. Jest to dowód pełnej poprawności części algebraicznej.
5. **Odzyskiwanie Riccatiego.** Dla D F=HF każdy nierozkładalny czynnik f|F spełnia f|Df, nawet jeśli F nie jest bezkwadratowy. W charakterystyce 0 f jest separowalny; z pochodnej f(x,w)=0 i równania D f(x,w)=0 wynika w'+w²=q. Otrzymany pierwiastek algebraiczny daje z=exp∫w i lokalne z''=qz.
6. **Przykłady dodatnie.** Schwarzowskie lokalne różnice wykładników (1/2,1/3,1/m) dla m=3,4,5, wprost wynikające z indycjalnego α(α−1)=b, dają n=4,6,12. Trzy pełne testy symboliczne i niezależne obliczenia Fraction potwierdzają P_{−1}=0; dla n=4 wszystkie wielomiany P_i są wypisane w rozdziale. Sama dodatnia rekurencja nie dowodzi prymitywnego typu grupy, gdy wcześniej istnieje rozwiązanie wymierne lub kwadratowe.
7. **Granice.** Zupełność algorytmu i brak liouvillowskich rozwiązań po odrzuceniu trzech gałęzi są **warunkowe od cytowanej klasyfikacji Kovacica**, nie od skończonej liczby regresji. W szczególności nie należy uogólniać pozytywnego wyniku dla q=2/x² na skończoną prymitywną grupę, bo rozwiązanie wymierne istnieje.

Finalny AA-50 ma **25 unikatowych etykiet, 4 dowody, 5 przykładów**. Wszystkie twierdzenia są opatrzone jawnymi hipotezami, a zasady terminologiczne zastosowano konsekwentnie.

## 3. Końcowa bramka CI

**GitHub Actions:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45184219678
**Head SHA zweryfikowanego commita:** 4103a830163f9abcebca492d26e58f33e9784f82.
**Werdykt wykonania:** completed / success — **92/92 kroki zakończone sukcesem**.
- Testy AA-50 SymPy: **13/13 PASS**.
- Testy AA-50 niezależne Fraction: **12/12 PASS**.
- Bramka AA GLOBAL: **PASS** — 50 rozdziałów, 1042 unikatowe etykiety, 0 duplikatów, 564 wystąpienia odsyłaczy, 336 odrębnych celów, 0 brakujących; 450 środowisk dowodów, 316 przykładów, 242 twierdzenia.
- Poprzednie audyty AA-01–AA-42 pozostają oddzielną historyczną kontrolą z 11 raportami; dla AA-43–AA-50 wymagane indywidualne raporty.
- Kompilacja latexmk, weryfikacja odsyłaczy, archiwizacja: PASS.

**Zastrzeżenie o pozostałej części repozytorium:** w logach diagnostycznego walidatora zależności innych książek nadal pojawiają się komunikaty o brakujących zagnieżdżonych importach (2) i rozbieżnych kopiach źródeł (11). Te wyniki dotyczą innych skryptów i nie są dowodem błędu AA-50; nie wolno ich jednak pomijać, uznając całe repozytorium za globalnie idealne. Specyficzna bramka integralności algebry oraz końcowy job CI są zielone. Nie zmieniano obcych materiałów.

## 4. Ostateczny PDF i kontrola wszystkich stron

**Artefakt końcowego GitHub Actions:** abstract-algebra-aa01-aa50, ID **14822108410**.

- abstract_algebra.pdf: **322 strony**, **2 309 663 B**, SHA-256 **61a914afe05a5bdbbdb907723e353c0d67144905960a1ad9e2148596c5aa0f7e**.
- abstract_algebra.log: **46 740 B**, SHA-256 **84290af0556dcabd3306c0bba23c93a5b0b9074accaa7c778da858e1d7d41373**.
- Końcowy log: 0 LaTeX Error, 0 LaTeX Warning, 0 hyperref Warning, 0 Overfull, 0 Underfull, 0 nierozwiązanych odsyłaczy.
- AA-50 zajmuje **6 stron PDF: 317–322** (drukowane 307–312). W końcowym artefakcie wyrenderowano każdą stronę (dwukrotna rozdzielczość) i obejrzano w układzie całościowym oraz w renderach. Brak obcięć, nałożeń tekstu, wadliwych wzorów i nieczytelnych rysunków.
- W całej książce skontrolowano bounding boxy **164 548 wyrazów**, **zero** poza granicami stron.
- W porównaniu z wersją PDF przed ostatnią korektą tylko strony **1 i 320** różnią się tekstowo (strona tytułowa oraz korekta „Lemat”); wszystkie pozostałe 320 stron są identyczne tekstowo.
- W porównaniu z poprzednim stabilnym tomem AA-01–AA-49 (316 stron) **314/316** starych stron zachowały identyczną warstwę tekstową; zmieniły się jedynie strona tytułowa i spis treści.

## 5. Werdykt

**AA-50 STABILNY** w jawnie ograniczonym zakresie algorytmu Kovacica opartym na klasycznej klasyfikacji lokalnej. Wykonano realne korekty, dwa niezależne zestawy testów, audyty I–III, końcowy zielony CI i oględziny każdej nowej strony.

**AA-51 NIEOTWARTY.** Dalsze rozwinięcia wymagają nowego, osobnego zakresu. Nie zmieniać historycznych statusów AA-01–AA-49.
