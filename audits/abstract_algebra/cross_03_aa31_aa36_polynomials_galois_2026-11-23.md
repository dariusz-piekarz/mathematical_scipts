# Audyt przekrojowy AA-X03 — AA-31–AA-36: niezmienniki wielomianów i grupa Galois

**Data:** 23 listopada 2026 r.  
**Repozytorium:** \`dariusz-piekarz/mathematical_scipts\`  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`  
**HEAD odczytany bezpośrednio przed zapisaniem tego raportu:** \`036391a50e40d5bf8882bc187e23450728b9c4d6\`.

## Zakres i granice

Nowa, numerowana kontrola przekrojowa sześciu opublikowanych rozdziałów: AA-31 (wielomiany symetryczne i wzory Viète’a), AA-32 (wyróżnik), AA-33 (wypadkowa i macierz Sylvestera), AA-34 (rezolwenta sześcienna i grupy Galois stopnia czwartego), AA-35 (redukcja modulo p i cykle Frobeniusa), AA-36 (wielomian ogólny). Sprawdzano **zgodność zależności między rozdziałami**, a nie powtarzano pełnych historycznych audytów każdego dowodu. Nie rozszerzano treści zatwierdzonych rozdziałów.

Bloby audytowanych źródeł:

| Rozdział | Git blob |
|---|---|
| AA-31 | \`6bd3b82caaead253ff90f8e6d1826447dc6f278b\` |
| AA-32 | \`f8c525aff1093478dcd8b1083387a42a37078086\` |
| AA-33 | \`40f339a13b5890418869a12ef27881d29233ffe7\` |
| AA-34 | \`a7202801c7e5ae9d4ad202a5deceabd631512a85\` |
| AA-35 | \`345bdebd74b8190bfb04f70ac7afe56b043dcb11\` |
| AA-36 | \`4c7f5c055172ff88331978592b89d4c44d5584dc\` |

## 1. Weryfikacja matematyczna — łańcuch zależności

1. **AA-31 → AA-32.** Symetryczność iloczynu kwadratów różnic pierwiastków pozwala wyrazić wyróżnik w elementarnych funkcjach symetrycznych, a wzory Viète’a w współczynnikach wielomianu. Występowanie pierwiastków z krotnościami oraz tożsamość \`disc(f)≠0\` wtedy i tylko wtedy, gdy pierwiastki są różne, są zgodne w obu rozdziałach i nie wymagają dzielenia przez 2 ani przez stopień wielomianu.
2. **AA-32 ↔ AA-33.** Przy konwencji macierzy Sylvestera w bazach rosnących potęg źródłowa wypadkowa to \`R(f,g)=(-1)^{mn} det S(f,g)\`. Dla monicznego \`f\` stopnia \`n≥2\` zachodzi \`disc(f)=(-1)^{n(n-1)/2}R_{n,n-1}(f,f')\`; **stopień pochodnej jest formalny** także przy spadku jej rzeczywistego stopnia w dodatniej charakterystyce. Sprawdzono znak, współczynniki wiodące, występowanie pierwiastków wielokrotnych i zgodność z uniwersalnymi wzorami sześciennymi.
3. **AA-31/32/33 → AA-34.** Dla \`f=X⁴+aX³+bX²+cX+d\` rezolwenta z sum iloczynów pierwiastków ma postać \`r_f(Y)=Y³−bY²+(ac−4d)Y−(a²d+c²−4bd)\`. Potwierdzono to bez dzielenia przez 2 lub 3, a także \`disc(r_f)=disc(f)\` dla wszystkich specjalizacji wykorzystanych w testach, w tym pierwiastków wielokrotnych. Równość jest wielomianowa nad \`Z\`, więc poprawnie redukuje się modulo liczby pierwsze.
4. **AA-34 i działania permutacji.** Dla trzech podziałów zbioru czteroelementowego na pary działanie \`S₄→S₃\` jest surjektywne, ma czteroelementowe jądro \`V₄\`, jest homomorfizmem i zachowuje znak permutacji. Kontrola obejmuje wszystkie 24 permutacje oraz wszystkie 576 uporządkowanych par.
5. **AA-32/33/34 → AA-35.** Dobra redukcja całkowitego wielomianu monicznego modulo \`p\` jest równoważna niezerowości \`disc(f) mod p\` i bezkwadratowości redukcji. Stopnie nierozkładalnych czynników po dobrej redukcji wyznaczają długości cykli pewnego Frobeniusa. Dla nieparzystej dobrej liczby pierwszej dodatkowo porównano znak permutacji \`(-1)^{n-s}\` z kwadratowością \`disc(f) mod p\`. Nie przenoszono tej ostatniej równoważności na charakterystykę 2.
6. **AA-31 → AA-36.** Algebraiczna niezależność pierwiastków formalnych i jednoznaczność zapisu wielomianów symetrycznych uzasadnia identyfikację \`k(t₁,…,t_n)≅k(e₁,…,e_n)\`. Permutacje formalnych pierwiastków dają wszystkie elementy \`S_n\` jako automorfizmy ciała rozkładu. To twierdzenie, w odróżnieniu od kryterium rozwiązywalności przez pierwiastniki, nie wymaga charakterystyki 0. Przykłady AA-34/35 są konkretnymi specjalizacjami, a nie kontrprzykładami do twierdzenia ogólnego.

**Przykłady specjalizacji weryfikowane dokładnie:**

| Wielomian | Grupa Galois opisana w AA-34 | Wyróżnik | Typ rezolwenty |
|---|---|---:|---|
| \`X⁴+X³+X²+X+1\` | \`C₄\` | \`125\` | \`1+2\` |
| \`X⁴−X−1\` | \`S₄\` | \`−283\` | \`3\` |
| \`X⁴−2\` | \`D₄\` | \`−2048\` | \`1+2\` |
| \`X⁴−10X²+1\` | \`V₄\` | \`147456\` | \`1+1+1\` |

Kontrola odrębnie porównała znaki wypadkowej, wyróżnik z iloczynu Vandermonde’a, wyróżnik rezolwenty, działanie na podziałach i zgodność rozkładów modulo \`p\` z kryterium parzystości. W wynikach nie wykryto sprzeczności wymagającej korekty źródeł.

## 2. Testy rzeczywiście wykonane

**Przebieg niezależny, w sesji audytowej:** \`6921/6921\` dokładnych warunków, z podziałem:
- Viète: \`750\`,
- wypadkowe: \`196\`,
- wyróżniki: \`3371\`,
- rezolwenty: \`1875\`,
- permutacje: \`602\`,
- faktoryzacja/Frobenius: \`115\`,
- przykłady: \`12\`.

**Przebieg odtwarzalny:** \`6200/6200\` dokładnych warunków w nowym pliku \`tools/tests/test_abstract_algebra_cross_aa31_36.js\`. Test korzysta z liczb całkowitych \`BigInt\`, wyznacznika obliczanego algorytmem Bareissa, niezależnego rozkładu wielomianów modulo liczb pierwszych przez wyszukiwanie dzielników oraz kompletnego działania \`S₄\` na podziałach. Rozbicie: Viète \`125\`, wypadkowe \`108\`, wyróżniki \`3371\`, rezolwenty \`1879\`, działanie grupy \`602\`, Frobenius i przykłady \`115\`.

Oba przebiegi są wariantami weryfikującymi pokrywające się tożsamości: **nie sumujemy** ich liczników jako niezależnych twierdzeń. Wykonano test odtwarzalny bezpośrednio przed publikacją kodu i zweryfikowano obecność zapisanego pliku w repozytorium.

\`\`\`bash
node tools/tests/test_abstract_algebra_cross_aa31_36.js
\`\`\`

Plik testowy dodano w commicie \`bbd258e634c82bb9612f7d5bd96383030ebe2f64\`, a jego uruchamianie wraz z wyzwalaczem ścieżki włączono do \`.github/workflows/abstract-algebra-chapter.yml\` w commicie \`01b95efe2de566086c228e439c52b6f5e22a85af\`.

## 3. Integralność źródeł, odsyłacze, struktura

W sześciu rozdziałach zidentyfikowano łącznie **66 unikatowych etykiet**, **53 użycia odsyłaczy** (46 do etykiet wewnątrz bloku AA-31–AA-36 i siedem wystąpień odsyłaczy zewnętrznych), **26 dowodów** i **27 przykładów**. Wszystkie cele zewnętrzne znaleziono bezpośrednio w odpowiednich rozdziałach:
- \`aa:tw:orbita-stabilizator\` w AA-03;
- \`aa:tw:cyclotomic-galois\` w AA-28;
- \`aa:tw:finite-frobenius-roots\` w AA-29;
- \`aa:wn:a5-not-solvable\` w AA-05;
- \`aa:ch:radicals\` w AA-24;
- \`aa:tw:fundamental-galois\` w AA-22.

Przejrzano równowagę \`\\begin/\\end\` oraz etykiety. Środowisko \`psmallmatrix\` w AA-33 jest prawidłowym środowiskiem matematycznym, nie błędem strukturalnym. Nie zmieniono stabilnych etykiet.

## 4. Rzeczywisty PDF i ograniczenia CI

Pobrano wcześniej **artefakt oryginalnego udanego workflow AA-01–AA-42** z GitHub Actions: <https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45083652049>, commit \`8cd2bb3ed85af64e616071d6b81128f75ce7ffba\`. Plik \`abstract_algebra.pdf\` ma 269 stron. Badane AA-31–AA-36 mieszczą się na stronach PDF **207–232**. Wyrenderowano i obejrzano wszystkie 26 stron; osobno przejrzano w powiększeniu stronę 219 z rysunkiem trzech podziałów na pary. Nie stwierdzono nachodzenia tekstu na wzory, kolizji podpisów ani ucięć.

Log pobrany z tego samego przebiegu: \`0\` ostrzeżeń LaTeX, \`0\` ostrzeżeń \`hyperref\`, \`0\` \`Overfull \\hbox\`, \`0\` \`Overfull \\vbox\`, \`0\` \`Underfull \\hbox\`, \`0\` sygnalizacji nierozwiązanych odsyłaczy, \`0\` błędów LaTeX. Bloby źródeł AA-31–AA-36 są zgodne z podanymi wyżej; w tej iteracji nie zmieniano ich.

**Nowy workflow po integracji AA-X03**: <https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45084525262>, SHA \`01b95efe2de566086c228e439c52b6f5e22a85af\`. W chwili sprawdzania rozpoczął działanie, ale **nadal był \`in_progress\`** i nie wolno deklarować nowej kompilacji ani nowego CI PASS przed zakończeniem. Wcześniejszy sukces dotyczy poprzedniego SHA.

## 5. Stan i następny krok

**AA-X03 — kontrola matematyczna i źródłowa wykonana, brak wykrytych nowych usterek, testy 6200/6200 oraz 6921/6921 PASS.** Nie ma jeszcze pełnej stabilizacji tej wersji workflow: należy potwierdzić jej \`completed/success\` wraz z osobnym wynikiem testu AA-X03, pobrać ewentualne logi, a następnie przeprowadzić dodatkowy **oddzielny, sceptyczny audyt potwierdzający bez zmiany zakresu AA-31–AA-36**. W razie błędu poprawić i ponowić cykl.

Wnioski z kontroli są matematycznie ograniczone do wymienionych tożsamości, łańcuchów zależności i modeli, a nie stanowią formalnego dowodu poprawności każdego rozdziału. AA-43 nadal nie występuje w katalogu źródeł; nie tworzono jego zastępczego audytu.