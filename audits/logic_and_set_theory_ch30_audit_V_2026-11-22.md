# Logika matematyczna i teoria mnogości — rozdział 30, audyt V (stabilizacyjny)

**Data:** 22 listopada 2026 r.  
**Źródło:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Zakres:** wyłącznie rozdział 30, bez wprowadzania nowych twierdzeń lub zmian do pliku TeX w tej iteracji.

## Niezależny przegląd matematyczny

1. **Gra i strategie.** Zweryfikowano definicję gry `G(A)` na `ω^ω`, poprawność parzystości tur, strategii dla obu graczy, otwartych i zamkniętych zbiorów wypłat, przykładu dwuruchowego oraz podpisu rysunku. Rozróżniono istnienie korzystnej pary ruchów od strategii obejmującej odpowiedzi na każdy ruch przeciwnika.
2. **Gale–Stewart w ZF.** Przy indukcyjnej konstrukcji `W_α` wszystkie etapy należą do `P(ω^{<ω})`; operator dodaje pozycji gracza I przy istnieniu wygrywającego następnika, gracza II przy wszystkich wygrywających następnikach. Stabilizację zapewnia twierdzenie Hartogsa i rekurencja na ustalonym ordynale, bez AC. Rangi są najmniejszymi etapami wejścia pozycji do `W`, maleją pod właściwą strategią; strategia przeciwnika spoza `W` wybiera kanonicznie najmniejszego odpowiedniego następnika. Dla gier zamkniętych poprawnie zamieniono warunki kwantyfikatorowe. Oba wyniki są twierdzeniami ZF.
3. **AC a AD.** Skontrolowano przekątną konstrukcję gry niezdeterminowanej przy AC: wszystkie strategie można dobrze uporządkować, a na każdym etapie wyznaczyć świeżą rozgrywkę z ustalonego dobrego porządku `ω^ω`. Następstwa AD nie są błędnie przypisywane teorii ZFC.
4. **AD i wybór dla zbiorów rzeczywistych.** Strategia gracza II w grze, w której I wskazuje indeks `n`, wyznacza jedną funkcję `n↦x_n∈X_n` bez ogólnego aksjomatu wyboru. Kodowanie domkniętych zbiorów nigdziegęstych przez drzewa pozwala następnie dowieść, że przy AD przeliczalna suma zbiorów pierwszej kategorii w `ω^ω` pozostaje pierwszej kategorii; jest to wyraźna hipoteza użyta w twierdzeniu o własności Baire'a.
5. **Gra Banacha–Mazura i własność Baire'a.** Skontrolowano konstrukcję gęstych zbiorów otwartych z ustalonej strategii, wyznaczanie legalnych historii, rekursję opartą na najmniejszym kodzie ruchu i domknięcie argumentu. W dowodzie dla całej prostej uściślono wykorzystanie homeomorfizmu `ω^ω` i zbioru liczb niewymiernych.
6. **Własność zbioru doskonałego.** Zweryfikowano nowo uzupełniony dowód istniejącego w planie twierdzenia `thm:ad-perfect-set`: strategia II definiuje przeliczalne pokrycie przeciwnych wypłat za pomocą zbiorów `E_h` o co najwyżej jednym elemencie; przy braku strategii II wygrywająca strategia I daje ciągłą iniekcję `2^ω→A`, której obraz jest niepusty, zwarty i bez punktów izolowanych. Przeniesienie do `ω^ω` i `R` odbywa się za pomocą jawnego kodowania ciągów i odpowiednich homeomorfizmów. Zwartość `2^ω` uzasadniono argumentem na skończenie rozgałęzionym drzewie, bez AC.
7. **AD wyklucza dobre uporządkowanie `R`.** Ustalono jedno świadectwo małości hipotetycznego selektora klas `R/Q`, z którego wszystkie wymierne przesunięcia wyznacza jedna formuła ZF. Osobna konstrukcja kanonicznych zagnieżdżonych przedziałów o wymiernych końcach dowodzi w ZF, że `R` nie jest pierwszej kategorii. Drugi przypadek wykorzystuje otwarty zbiór aproksymujący hipotetyczny zbiór o własności Baire'a i niepusty przedział, na którym zbiór jest współpierwszej kategorii. Nie zakładano nieudowodnionego DC.
8. **Mierzalność i PD.** Skontrolowano założenia przy kodowaniu pokryć miary zero, grze pokryciowej, użyciu zewnętrznego twierdzenia o mierzalności zbiorów analitycznych oraz warunek DC w twierdzeniu o mierzalności. Głębokie twierdzenia Martin–Steel oraz Martin–Steel–Woodin są przedstawione jako przywołane rezultaty ze źródłami; nie przypisuje się im własnego dowodu w skrypcie. Wyraźnie odróżniono `L(R)⊨AD` od `V⊨AD`.
9. **Redukcje Wadge'a.** Zweryfikowano poprawność kodowania gry redukcyjnej, półliniowość pod PD, ciągłość funkcji generowanej przez strategię II, konstrukcje zbiorów zupełnych dla otwartych i domkniętych, przykłady samodualności oraz dowód ogólnego kryterium niesamodualności zbiorów otwartych niedomkniętych. Przykładowy alternatywny zbiór otwarty zupełny ma jawną redukcję `U₀=f⁻¹[U]`, a nie domniemaną zupełność.

**Wynik audytu matematycznego V:** nie wykryto dalszych błędów, nieuzasadnionych wzorów lub braków warunków wymagających modyfikacji. Nie zmieniono źródła rozdziału w tej iteracji.

## Inwentarz i walidacja

- Inwentarz: **12 definicji, 7 przykładów, 15 twierdzeń, 9 lematów, 4 wnioski, 15 uwag, 26 dowodów i 1 rysunek**. **57 unikatowych etykiet i 49 odsyłaczy**, wszystkie z rzeczywistymi celami w 30 rozdziałach.
- Testy strukturalne i regresyjne `tools/tests/test_logic_and_set_theory_ch30.py` obejmują przypadki gier, formalne konstrukcje przy AD, brak ukrytego wyboru i jawne redukcje Wadge'a: **PASS**.
- GitHub Actions [45010414553](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45010414553): **SUCCESS**, w tym pełny skład PDF i kontrola referencji. **SHA bloba źródła rozdziału jest identyczny** w zakończonym przebiegu i na gałęzi roboczej: `e95478921826b8b05d6f16daae95a8a3c236eaf4`.
- Pełny PDF `logic_and_set_theory.pdf`: **247 stron**. Rozdział 30: **20 stron**, strony PDF 228–247. Wyodrębniono osobny plik PDF rozdziału.
- Wszystkie 20 stron wyrenderowano i sprawdzono wizualnie, w tym drzewo gry i formuły w ostatniej sekcji. Nie zaobserwowano nachodzenia napisów, uciętych wzorów lub naruszonych marginesów.
- Log: **0** `Overfull \\hbox`, **0** niezdefiniowanych odsyłaczy, **0** niezdefiniowanych cytowań, **0** błędów TeX. Jeden niegroźny `Underfull \\hbox` w całym skrypcie.

## Werdykt końcowy

**ROZDZIAŁ 30 — STABILNY po audycie V.** Audyty I–IV wprowadziły rzeczywiste poprawki i uzupełnienia uzasadnień; audyt V jest niezależną iteracją bez nowych usterek, z zielonym CI oraz kontrolą PDF. Rozdział 31 nie był przedmiotem tej iteracji.
