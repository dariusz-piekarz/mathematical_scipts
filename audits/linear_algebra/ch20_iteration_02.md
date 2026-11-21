# Algebra liniowa — rozdział 20, audyt II

**Data:** 21 listopada 2026  
**Gałąź:** \`biblioteka-matematyczna-iteracja-6\`  
**Rozdział:** \`chapters/pl/linear_algebra/20-dzielniki-elementarne-i-bloki-pierwotne.tex\`  
**Poprzedni audyt:** \`ch20_iteration_01.md\`.  
**Kontrola niezależna:** matematyczna, przykładów, typografii i odsyłaczy.

## Kontrola dowodów

1. **Jednoznaczność rozkładu wielomianu.** Indukcja po stopniu uzasadnia istnienie rozkładu monicznych wielomianów, a lemat Euklidesa dla \`K[t]\` jego jednoznaczność. Nie zakłada się domknięcia algebraicznego.
2. **Chińskie twierdzenie o resztach.** Dobrze określoność, liniowość, różnowartościowość i surjektywność \`Φ\` mają oddzielne uzasadnienia. Bezoutowe \`e_i=u_i h_i\` spełniają kongruencje \`e_i≡δ_ij (mod f_j)\`, co daje surjekcję.
3. **Klasyfikacja przez bloki \`C(p^a)\`.** Rozkład czynników niezmienniczych \`f_i\` na potęgi wielomianów nierozkładalnych i CRT daje istnienie. Przy dowolnym konkurencyjnym rozkładzie pierwotnym dopełnienie list wykładników zerami z lewej i ponowny CRT prowadzą do kanonicznych \`g_1|...|g_r\`. Ich jednoznaczność wynika z Frobeniusa z rozdziału 19.
4. **Wymiar i wielomiany operatora.** Wymiar każdego \`K[t]/(p^a)\` to \`a deg p\`; \`χ\` jest iloczynem wielomianów blokowych, a \`m\` ich moniczną NWW. Zastosowano również konwencję \`n=0\`.
5. **Formuła na jądra.** Na składniku \`K[t]/(p^a)\` jądro mnożenia przez \`p^k\` jest izomorficzne do \`K[t]/(p^k)\` dla \`k<a\`, a dla \`k≥a\` jest całym modułem. Na pozostałych blokach mnożenie jest odwracalne przez Bézouta. Różnice pierwsze i drugie wymiarów jąder liczą odpowiednio bloki długości co najmniej \`k\` i dokładnie \`k\`.
6. **Związek z Jordanem.** W bazie \`u^{a-1},...,1\`, gdzie \`u=t-λ\`, mnożenie przez \`t\` ma macierz Jordana z jedynkami na nadprzekątnej. Działa w dowolnej charakterystyce.
7. **Przykłady.** Sprawdzono liczby bloków dla \`J_3(0)⊕J_1(0)\`, przypadek \`diag(1,1,2)\`, \`q=t²+1\` nad \`R\`, blok \`(t²+t+1)^2\` nad \`F2\`, a także przykład dwóch niepodobnych macierzy o tych samych \`χ,m\`.

## Usterka przykładu i korekta

W przykładzie \`diag(1,1,2)\` zdanie, że niedozwolone \`p²,q\` „mają nieodpowiednie stopnie”, było mylące: suma stopni wynosi \`3\`, tak jak wymiar. Poprawiono argument: \`p²,q\` nie tworzą łańcucha podzielności, a ich najmniejsza wspólna wielokrotność \`p²q\` nie jest właściwym wielomianem minimalnym \`pq\`. **Nie dodano twierdzeń.**

## Kontrola techniczna

- GitHub Actions [44942425770](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44942425770): wszystkie testy matematyczne zaliczone; pierwszy błąd LaTeX dotyczył niezabezpieczonego zapisu \`K[t]\` w opcjonalnym tytule twierdzenia; poprawiono.
- GitHub Actions [44942613171](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44942613171): **SUCCESS** — testy, książka, eksport PDF.
- Zatwierdzony eksport PDF sprzed aktualnej korekty przykładu obejmował 7 stron; wszystkie niepuste, 0 bloków tekstu poza granicami stron, obejrzano całość na zestawieniu.
- Rozdział: 22 unikatowe etykiety, 23 odsyłacze, 7 par środowisk \`proof\`.
- Po zmianie uzasadnienia należy ponownie sprawdzić CI i PDF.

## Decyzja

Audyt II wykrył **jedną nieprecyzyjną przesłankę w przykładzie** i ją usunął. Rozdział pozostaje w audycie, wymagane kolejne czyste odczyty i kontrola ostatecznego PDF.
