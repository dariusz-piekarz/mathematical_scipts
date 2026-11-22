# Logika matematyczna i teoria mnogości — rozdział 30, audyt VII

**Data:** 22 listopada 2026 r.  
**Rozdział:** „Gry nieskończone i aksjomat determinacji”.  
**Źródło:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Tryb:** pełne niezależne przejście przez istniejące definicje, twierdzenia, dowody, przykłady, odsyłacze i zależności aksjomatyczne. Bez dodawania twierdzeń.

## Audyt matematyczny

1. **Gra, strategie i kodowania:** sprawdzono naprzemienność tur, formalizację strategii na skończonych historiach i różnicę między jedną wygrywającą rozgrywką a strategią wygrywającą. W grach pomocniczych nielegalne ruchy są jawnie określone.
2. **Gale–Stewart dla gier otwartych:** definicja monotonicznej rekurencji `W_α`, jej stabilizacja przez twierdzenie Hartogsa dla `P(ω^{<ω})` oraz konstrukcje strategii przez wybór najmniejszego ruchu są poprawne w ZF. Ścisły spadek rang uzasadnia zakończenie części wymuszającej. Przez zamianę ról uzyskano poprawnie przypadek wypłat zamkniętych.
3. **AC kontra AD:** konstrukcja przekątniowa tworzy w ZFC grę niezdeterminowaną, przypisując każdej strategii rozgrywkę, którą przegrywa. Nie zakłada regularności continuum: dla `α<𝔠` mamy `|α|·ℵ₀<𝔠`; każda strategia dopuszcza `𝔠` odpowiedzi przeciwnika. W konsekwencji `ZF ⊢ ¬(AC∧AD)`. Mocniejszy argument z selektorem klas `ℝ/ℚ` wyklucza dobre uporządkowanie `ℝ` w ZF+AD.
4. **AD i wybór przeliczalny dla liczb rzeczywistych:** wygrywająca strategia II w grze indeksowanej przez `n∈ω` wyznacza kanoniczną funkcję wyboru z `X_n⊆ω^ω`. Nie przeniesiono wniosku na pełny AC.
5. **Pierwsza kategoria i własność Baire'a:** kodowanie domkniętych zbiorów nigdziegęstych za pomocą drzew, wybór kodów świadectw przy AD, konstrukcja Baire'a przez najmniejsze prefiksy i gra Banacha–Mazura dają właściwe implikacje bez ukrytego DC. Przejście z `ω^ω` do podprzestrzeni niewymiernych i następnie do `ℝ` zachowuje argument o małości zbiorów.
6. **Własność zbioru doskonałego:** w grze z binarnymi blokami strategia II wymusza przeliczalność poprzez rodzinę `E_h` o co najwyżej jednym punkcie. Strategia I wyznacza ciągłą iniekcję `2^ω→A`. Zwartość przestrzeni Cantora sprawdzono w ZF za pomocą jawnego wyboru lewego dziecka, co daje zwarty zbiór doskonały. Przeniesienia do `ω^ω` i `ℝ` opierają się na jawnych kodowaniach.
7. **Mierzalność:** policzono budżety przedziałów w lemacie `lem:ad-null-cover-coding`: dla pierwszego bloku `ε/6<ε/4`, a na kolejnych etapach kontrolę zapewnia ogon o długości `< ε4^{-(n+1)}`; łączna suma kosztów ruchów II to `∑_{n≥0}2^{n+1}ε4^{-(n+1)}=ε`. Argument przytoczony w rozdziale wymaga **ZF+DC+AD** i zewnętrznego twierdzenia o mierzalności zbiorów analitycznych. Klasyczny wynik z samego ZF+AD jest prawdziwy, lecz nie został tutaj udowodniony tą drogą.
8. **Regularyzacja projektywna z PD — rzeczywiste uzupełnienie luki wyjaśnienia:** przy przenoszeniu argumentów z AD należy sprawdzić, że pomocnicze gry mają *projektywne* wypłaty. W dowodzie własności Baire'a zbiór `U` zdefiniowany przez warunek małości jest otwarty, więc `A\setminus U` jest projektywny dla projektywnego `A`. Gra pokryciowa składa warunek `x(a)∈A` z warunkami borelowskimi. Co więcej, wcześniejszy dowód wykorzystuje wybór przeliczalny wynikający z AD; w **ZFC+PD** dostępny jest on z samego AC, więc nie można bez wyjaśnienia wymagać od PD determinacji gier kodujących arbitralne rodziny podzbiorów liczb rzeczywistych. Uzupełniono ten krok jawnie.
9. **Duże liczby kardynalne i `L(ℝ)`:** poprawnie oddzielono definicję liczb kardynalnych Woodina od nieudowadnianych tutaj twierdzeń Martin–Steel i Martin–Steel–Woodin. Zaznaczono różnicę między `L(ℝ)⊨AD` a `V⊨AD`, kompatybilną z AC w otaczającym modelu. Dowód absolutności zdań projektywnych korzysta z tych samych liczb rzeczywistych i rzeczywistych kodów borelowskich w obu modelach.
10. **Gry Wadge'a:** kodowanie pominięcia ruchu daje projektywną wypłatę; strategia II wyznacza ciągłą redukcję, a strategia I ciągłą redukcję do dopełnienia `A`. Dowód odwrotnego kierunku „ciągła redukcja ⇒ zwycięska strategia II” opiera się na rosnącej informacji o wspólnych prefiksach. Sprawdzono jawne funkcje wykazujące zupełność dla zbiorów otwartych i domkniętych oraz warunki samodualności i niesamodualności.

## Wykonane poprawki źródła

- Doprecyzowano uwagi `rem:ad-deep-regularity` i `rem:ad-analytic-input`: klasyczny wniosek z samego AD różni się zakresem założeń od przedstawionego dowodu używającego DC.
- Rozbudowano dowód `thm:pd-regularity`, jawnie uzasadniając projektywność pomocniczych zbiorów wypłat i wykazując, dlaczego w ZFC+PD nie należy zastępować AC przez domniemaną nieograniczoną konsekwencję PD.
- Rozszerzono `tools/tests/test_logic_and_set_theory_ch30.py` o regresję tych zależności. Pierwsza wersja regresji ujawniła błędy w dosłownych porównaniach ciągów (podwójne ukośniki i podział wierszy); zostały poprawione przed zamknięciem iteracji. Nie przedstawiam nieudanych przebiegów jako testów matematycznych skryptu.

**SHA źródła:** `2f45abf617fb2f84fa01f1a0acf7db5c1de131fd`.  
**SHA regresji:** `a0bc924666a1ec91ce7d32d6854903937001f103`.

## Kontrola techniczna

- Rozdział 30: **57 różnych etykiet i 49 odsyłaczy**, bez zmian w liczbie i nazwach celów.
- Inwentarz środowisk niezmieniony: **12 definicji, 7 przykładów, 15 twierdzeń, 9 lematów, 4 wnioski, 15 uwag, 26 dowodów i 1 rysunek**.
- Poprzednia wersja po audycie VI przeszła pełne CI: [GitHub Actions #45012535817](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45012535817) — `SUCCESS`.
- **Bieżąca wersja VII:** [GitHub Actions #45013045512](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45013045512) — uruchomiona dla poprawionej wersji regresji; jej końcowy status należy sprawdzić po zakończeniu (nie utożsamiać z poprzednim sukcesem).
- Ten audyt jest matematyczno-redakcyjny oparty na źródle, wynikach regresji i kontroli CI. Osobnej ręcznej inspekcji wszystkich stron nowo wyrenderowanego PDF nie wykonano podczas tej iteracji; nie przypisujemy jej statusu `PASS`.

## Werdykt

**Audyt VII: dwa uzupełnienia dotyczące założeń i zależności dowodowych; brak wykrytych kontrprzykładów dla pozostałych twierdzeń.** Status techniczny najnowszej wersji zależy od końcowego wyniku aktualnego przebiegu CI. Dalsza iteracja powinna być ponownym niezależnym przejściem, nie powtórzeniem tego raportu.
