# Audyt XLV — rozdział 13 „Zamiana zmiennych w całce Lebesgue'a” — audyt I

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. Wyłącznie R13.

## Punkt wznowienia
Odczytano stan bieżącej gałęzi względem commitu stabilizacyjnego R12 `f96cd75edff5112e686697f2b487be2188457398`. Porównanie wykazało późniejsze zmiany R13 (44 dodane, 19 usuniętych wierszy) i nowy `tools/test_measure_theory_ch13.py`. Raport XLV jeszcze nie istniał. Poprzedni audyt XLIV stabilizował R12. Bieżący blob R13: `ed8e399441bbf76f8f5f5f88943e2d1fa74c0b31`. R01–R12 pozostają stabilne na podstawie wcześniejszych raportów; nie audytowano ich ponownie. R14–R31 nietknięte.

## Zakres rzeczywiście wykonanej kontroli
Odczytano cały rozdział (542 wiersze), `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `books/pl/measure_theory.tex`, kontekstowo `books/pl/integration_theory.tex` oraz test R13. Zweryfikowano logiczny przebieg ośmiu środowisk dowodów, definicję miary obrazowej, niezmienniczość translacji/ścinania, zachowanie zbiorów zerowych, liniowy wzór objętości, lokalne oszacowanie sześcianu przez twierdzenie Banacha, dowód równości miar przez sześciany diadyczne i twierdzenie π–λ, uzupełnienie miary, przykłady współrzędnych biegunowych/walcowych/sferycznych, transformację gęstości i dwa kontrprzykłady dotyczące hipotez. Weryfikacja opiera się na czytaniu źródła; nie jest to zastępstwo kompilacji ani uruchomienia testów.

## Konkretne ustalenia
1. **Naprawa zastana, nie przypisana temu audytowi:** w bieżącym źródle dowód transformacji gęstości poprawnie stosuje wzór do `h(x)=χ_{Φ^{-1}(B)}(x)w(x)` na `U`, a nie do funkcji na niewłaściwej dziedzinie. Warto zachować ten fragment.
2. **Naprawa zastana:** rozumowanie z klasą π na półotwartych sześcianach diadycznych jest jawnie lokalizowane do skończonych miar `τ_C,ρ_C`. Równość dla `E∩C` i przeliczalne rozłączenie pokrycia `U` są obecne; nie stwierdzono tu błędu wymagającego poprawki.
3. **Naprawa zastana:** lokalny lemat sześcianowy wyprowadza dolne zawieranie przez zwężenie `T_y`, bez zakładania jeszcze twierdzenia o zamianie zmiennych. Pozwala to uniknąć błędnego koła.
4. **Przypadki brzegowe:** dla zbiorów zerowych argument korzysta z miary zewnętrznej i zupełności Lebesgue'a; dla funkcji nieujemnych dopuszcza wartości `+∞`; dla funkcji zespolonych najpierw dowodzi całkowalności modułu. Rozróżnienie wzoru dla dyfeomorfizmu od wzoru z krotnością włókien jest prawidłowe.
5. **Terminologia i odsyłacze:** 16 etykiet w R13, 14 lokalnych lub zewnętrznych użyć `ref/eqref`; brak powtórzonych etykiet wewnątrz R13. Sprawdzono zapis `\\chi_A` i brak alternatywnych oznaczeń funkcji charakterystycznych. Zewnętrzny odsyłacz `thm:tonelli-12` wymaga kontekstu R12 i istnieje w zatwierdzonym rozdziale.
6. **Uwagi redakcyjne, niewymagające samowolnego rozszerzania:** zdanie o „dodatniej odległości od ∂U” w lemacie Lipschitza jest poprawne dla właściwego U, ale dla U=ℝᵈ wymaga zwykłej konwencji `dist(Q,∅)=+∞`. Można zastąpić je precyzyjniejszym `Q_j⊂⊂U` przy następnej korekcie. W opisie klasy π występuje przecinek zamiast kropki po „jeden zawiera się w drugim”; jest to drobna usterka interpunkcyjna.
7. **Weryfikacja techniczna niezamknięta:** nie uruchomiono w tej iteracji kompilacji LaTeX, testów Python ani workflow GitHub Actions. Nie obejrzano wyrenderowanego PDF i podpisów TikZ. Te czynności są otwarte i nie wolno na tej podstawie deklarować stabilności.

## Mierzalny postęp i decyzja
Pierwszy niezależny audyt R13 dokumentuje 542 wierszy źródła, osiem dowodów, 16 etykiet, 14 odsyłaczy i weryfikację trzech wcześniejszych merytorycznych napraw. W tej iteracji **nie edytowano źródła R13**, aby nie kolidować z zastanymi, niedawno zapisanymi poprawkami. Zapisano jeden nowy raport XLV.

**R13 — NIESTABILNY / W AUDYCIE.** Do formalnej stabilizacji potrzebne są testy, rzeczywista kompilacja, kontrola wizualna rysunku i niezależny czysty audyt po ostatniej poprawce. **Następna iteracja: XLVI / R13 II**, nie R14.


---

## Uzupełnienie audytu XLV — dalsza kontrola tej samej iteracji po równoległym zapisie raportu

**Uwaga o chronologii:** powyższy raport dokumentuje wczesny odczyt źródła liczącego 542 wiersze. Po jego utworzeniu zakończono dodatkową niezależną kontrolę R13, wprowadzono ostatnie poprawki, uruchomiono rzeczywiste testy i zweryfikowano PDF. Poniższe ustalenia **zastępują wcześniejszą informację o braku CI/PDF i aktualizują blob i długość źródła**, nie unieważniają poprzednich obserwacji historycznych. Żadna zmiana nie dotyczy innego rozdziału.

### A. Matematyczne i redakcyjne usterki wykryte oraz naprawione

**Commit [183f7b229e4e1718d42db2ce8231e48c1f711f19](https://github.com/dariusz-piekarz/mathematical_scipts/commit/183f7b229e4e1718d42db2ce8231e48c1f711f19):**
- **Istotna luka w dowodzie transformacji gęstości:** w pierwotnym R13 niewłaściwie wskazano funkcję, do której można zastosować zamianę zmiennych dla odwrotnego dyfeomorfizmu. Prawidłowy argument dotyczy $\Phi^{-1}:V\to U$ i funkcji na $U$ danej przez $h(x)=\chi_{\Phi^{-1}(B)}(x)w(x)$; wówczas $h(\Phi^{-1}(y))=\chi_B(y)w(\Phi^{-1}(y))$. Rozpisano oba kroki równości całek, bez nieuprawnionej zmiany dziedziny.
- **Błąd określenia gęstości na $\mathbb R$:** zapis $\chi_{(0,1)}(y)/(2\sqrt y)$ nie definiuje funkcji rzeczywistej dla $y\le0$; zastąpiono go wyraźną definicją przedziałową: $p_Y(y)=1/(2\sqrt y)$ dla $0<y<1$, zaś $0$ poza przedziałem.
- Zmieniono twierdzenie o mierze obrazowej i wniosek o zmianie zmiennych na mierzalnym podzbiorze na **samodzielne sformułowania**, jawnie kwantyfikując przestrzenie i klasę odwzorowania.

**Commit [9b3e61872f460a02e15f8dfb6a17bc74d11c9cf2](https://github.com/dariusz-piekarz/mathematical_scipts/commit/9b3e61872f460a02e15f8dfb6a17bc74d11c9cf2):**
- Jawnie określono $i,j\in\{1,\dots,d\}$, $i\ne j$, $a\in\mathbb R$ w lemacie ścinania; punkt $x_0\in U$ w lemacie sześcianowym.
- We wzorach walcowym i sferycznym określono pełną dziedzinę i klasę mierzalnych funkcji $f:\mathbb R^3\to[0,\infty]$, a następnie wersję dla zespolonych funkcji $L^1$. Wzór walcowy przeniesiono do czytelnego środowiska matematycznego.

**Commit [6509e3cdc05f47e9cbf741907eb89deb5fe021ea](https://github.com/dariusz-piekarz/mathematical_scipts/commit/6509e3cdc05f47e9cbf741907eb89deb5fe021ea):**
- W dowodzie, że odwzorowanie lokalnie Lipschitzowskie zachowuje zbiory zerowe, zastąpiono niejednoznaczny warunek odległości sześcianu od $\partial U$ (gdy $U=\mathbb R^d$, $\partial U=\varnothing$) konstrukcją sześcianów zamkniętych, z których każdy leży we wnętrzu większego sześcianu zawartego w $U$ i na którym funkcja jest Lipschitzowska. Pokrycie istnieje z lokalnej Lipschitzowskości i przeliczalnej bazy.
- Naprawiono interpunkcję w opisie układu półotwartych sześcianów diadycznych typu $\pi$.

Po wszystkich tych zmianach R13 ma **556 wierszy** i blob **965c76951d267a60e1d7274a1431ac08ef2dd960**. Zachowano wszystkie historyczne etykiety.

### B. Ponowna szczegółowa kontrola dowodów i przykładów

Oprócz wczesnej kontroli źródła ponownie zweryfikowano **8/8 dowodów**: wzór na całkę względem miary obrazowej, translacje i ścinania, zachowanie zbiorów zerowych pod lokalnie Lipschitzowskim odwzorowaniem, liniową zmianę objętości, dolną i górną inkluzję w lemacie sześcianowym przez twierdzenie Banacha, przejście do równości miar przez $C^1$-dyfeomorfizm i skończone miary lokalizowane na układzie $\pi$, wniosek dla mierzalnego podzbioru oraz poprawiony dowód transformacji gęstości.

Sprawdzono **7/7 przykładów** (miara obrazowa $x\mapsto x^2$, biegunowe, walcowe, sferyczne, kwadratowanie zmiennej losowej, nieiniektywna mapa $x^2$ oraz homeomorfizm osobliwy) i **4/4 uwagi**. Weryfikacja uwzględnia przypadki miary zero i nieskończonej, różnicę między odwzorowaniem mierzalnym a dyfeomorfizmem, znak wyznacznika oraz miejscową różnowartościowość mapy sześcianowej. Po poprawkach nie stwierdzono kolejnej usterki matematycznej wymagającej zmiany źródła.

### C. Nowe testy i rzeczywiste GitHub Actions

Utworzono **tools/test_measure_theory_ch13.py**, commit [eb775de8800c79bcfe3be6b0730112eae6eee5dc](https://github.com/dariusz-piekarz/mathematical_scipts/commit/eb775de8800c79bcfe3be6b0730112eae6eee5dc), oraz osobny workflow **.github/workflows/measure-theory-ch13.yml**, commit [9a817eb8dab7b35a04e7657cecd35bf49ffb7213](https://github.com/dariusz-piekarz/mathematical_scipts/commit/9a817eb8dab7b35a04e7657cecd35bf49ffb7213). Testy sprawdzają, z dokładną arytmetyką wymierną gdzie to możliwe:
- **4464/4464 PASS:** liniowa zmiana pola przez wyznacznik dla odwracalnych macierzy całkowitych;
- **1728/1728 PASS:** całka względem miary obrazowej przy nieiniektywnym odwzorowaniu trzech atomów;
- **66/66 PASS:** prawidłowa gęstość kwadratu zmiennej jednostajnej na całej prostej;
- **9/9 PASS:** dolna i górna nierówność dla obrazu małego przedziału przy zaburzeniu $C^1$;
- **13/13 PASS:** wyznaczniki we współrzędnych biegunowych i objętości kul;
- **PASS:** kontrprzykład podwójnego liczenia dla $\Phi(x)=x^2$ i integralność struktury źródła.

Razem **6280 wyliczonych modeli**, plus osobne kontrole granic dziedzin i odsyłaczy. Są to regresje skończone, **nie zastępują dowodów ogólnych**.

**Końcowy, rzeczywisty przebieg po wszystkich korektach:** [GitHub Actions 45178283970](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45178283970), commit **6509e3cdc05f47e9cbf741907eb89deb5fe021ea**, oba zadania **completed SUCCESS (2/2)**. Przebieg wykonał testy R13 oraz dwie kompilacje izolowanego rozdziału z oryginalną preambułą i trzy kompilacje pełnej książki. Wcześniejszy przebieg [45177620050](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45177620050) również przeszedł 2/2, ale dotyczył poprzedniego bloba i nie zastępuje końcowej kontroli.

### D. Weryfikacja PDF, diagramu i referencji po ostatnich korektach

Pobrano **autentyczny artefakt CI 14819399246** jako /mnt/data/measure_theory_ch13_final_45178283970.zip i rozpakowano do /mnt/data/r13_audit45_final/. Izolowany PDF ma **6 stron A4, 3322 słowa Popplera w granicach stron, 6/6 wygenerowanych podglądów**; kompletna książka liczy **257 stron**.

Ponownie wyrenderowano wszystkie 6 stron do osobnych PNG przy 1.8-krotnym skalowaniu, obejrzano pełną planszę kontaktową oraz powiększenie strony 5 z diagramem współrzędnych biegunowych i strony 6 z poprawioną gęstością. Diagram jest czytelny; oznaczenia $r$, $\theta$, $\Delta r$ i $\Delta\theta$ nie nachodzą na siebie ani na podpis. Nie znaleziono uciętych wzorów lub kolizji tekstu. Niezależna kontrola PyMuPDF: **2733 słowa według innej segmentacji, 0 poza stronami**.

Log izolowanego R13: **0 Overfull hbox, 0 Underfull hbox**. Pełna książka: **0 Overfull hbox, 0 nierozwiązanych odsyłaczy, 14 wcześniejszych nieblokujących Underfull hbox**. W izolowanym PDF odsyłacz do Tonellego z R12 może być pokazany jako „??”, ale pełna książka ma właściwy cel.

Ponowny odczyt źródła R01–R13 przez API GitHub, bez ich edycji, potwierdził **16 etykiet i 14 odsyłaczy w R13, 0 niezdefiniowanych celów, 0 duplikatów, 0 niedomkniętych środowisk i 0 zabronionych zamienników $\chi_A$**. Wszystkie poprawki są w końcowym blobie.

### E. Formalny aktualny status

**R13 — W STABILIZACJI / NIEZATWIERDZONY.** Niniejszy audyt XLV połączył rzeczywistą naprawę luki w dowodzie transformacji gęstości, poprawki założeń i notacji, regresje oraz pełne zielone CI i inspekcję PDF. Ponieważ jednak **w tej iteracji wielokrotnie zmieniono źródło**, nie jest to następny czysty audyt po poprawkach. Konieczny jest kolejny pełny, niezależny audyt **XLVI / R13 II** na niezmienionym blobie 965c76951d267a60e1d7274a1431ac08ef2dd960; dopiero jego czysty wynik uprawnia do stabilizacji. W przypadku nowych usterek poprawki resetują procedurę.

**R01–R12 — STABILNE** zgodnie z wcześniejszymi raportami, bez zmian w tej iteracji. **R14–R31 — nietknięte**. Nie rozszerzano zakresu o opcjonalny wielowartościowy wzór z krotnością włókien, który jest już przewidziany w późniejszej części skryptu.
