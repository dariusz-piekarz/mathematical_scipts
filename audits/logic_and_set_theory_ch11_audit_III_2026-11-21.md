# Audyt III — rozdział 11 „Dowody formalne i dedukcja naturalna”

**Data:** 21 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/11-dowody-formalne-i-dedukcja-naturalna.tex`.  
**Kontrolowany blob Git:** `21f1ddd49d26d6d42e26cb5495d0d79a9a7c65b9` (po audycie II).  
**Zakres:** trzeci niezależny audyt istniejącej treści — bez nowych twierdzeń, lematów, definicji lub przykładów.

## Konkluzja matematyczna

**Audyt III jest czysty.** Nie wykryto nowego błędu matematycznego, wadliwego kroku dowodu, błędnie użytego kwantyfikatora ani niejawnego założenia wymagającego poprawki w pliku źródłowym. **Nie zmieniono pliku `.tex`.**

Ponownie sprawdzono cały materiał: **5 twierdzeń z 5 dowodami, 7 definicji, 16 przykładów i 8 uwag**. Zachowano 21 etykiet i 7 odsyłaczy rozdziału.

## Ponowna analiza istniejących dowodów

1. **Twierdzenie o dedukcji (`thm:nd-deduction`).** Sprawdzono oba kierunki, ponowne użycie otwartych założeń i dopuszczalność rozładowania zerowej liczby wystąpień. Dla nieskończonego zbioru `Γ` konkretne drzewo nadal korzysta tylko ze skończonego zbioru założeń.
2. **Prawo wyłączonego środka (`thm:nd-lem`).** Skontrolowano zagnieżdżone założenia, dwa użycia reguł wprowadzania alternatywy, `¬I`, `¬E` oraz końcowe `RAA`. Wszystkie istotne założenia są prawidłowo rozładowywane.
3. **Twierdzenie o łańcuchu uniwersalnym (`thm:nd-univ-chain`).** Poprawka z audytu I podstawia `x:=x`, zawsze dopuszczalne także w formułach z wewnętrznymi kwantyfikatorami. Końcowa `∀I` jest uzasadniona, ponieważ `x` nie występuje wolno w obu otwartych przesłankach.
4. **Projekcja egzystencjalna (`thm:nd-exists-projection`).** Świeża nazwa `y` jest nieobecna w obu formułach i pozostałych otwartych założeniach, zatem poprawne są podstawienie, `∧E`, `∃I` i końcowe rozładowanie `∃E`.
5. **Skończone użycie przesłanek (`thm:nd-finite-support`).** Dowód opiera się wyłącznie na skończoności drzewa dedukcji; zbiór `Γ` nie musi być skończony.

## Pozostałe definicje, reguły i przykłady

- Sprawdzono schematy `∧I/E`, `∨I/E`, `→I/E`, `↔I/E`, `¬I/E`, `⊥E`, `RAA`, reguły `∀E/I`, `∃E/I`, a także `=I/E`, ich semantyczny sens oraz indeksowane rozładowywanie założeń.
- W `∃E` warunki świeżości odnoszą się do rzeczywiście użytych otwartych założeń obu gałęzi (nie do całego potencjalnie nieskończonego `Γ`), formuły kwantyfikowanej i wniosku. Warunek gwarantuje brak przemycenia wartości zmiennej świadka do wyniku.
- Ponownie skontrolowano oba kontrmodele z przykładu `ex:nd-exists-major-premise-fresh-46`: naruszenie świeżości w innym otwartym założeniu oraz w samej przesłance głównej.
- **Symetria równości po audycie II.** Dla dowolnych termów `t,u` dobieramy `z` niewystępującą w żadnym z nich i bierzemy `θ(z):=z=t`. Wówczas `θ[z:=t]=(t=t)`, `θ[z:=u]=(u=t)`, więc reguła `=E` z `t=u` i `t=t` daje `u=t`. Brak niejawnego przestawienia podstawienia wewnątrz `t` (problem wykryty w audycie II).
- Przykłady tłumaczące wielokropki i zakres założeń zachowują prawidłowe rozróżnienie pomiędzy metajęzykiem dowodu a formułami logiki.

## Niezależne testy falsyfikacyjne audytu III

Przygotowano dodatkową, niezależną enumerację składni i semantyki dla **102 formuł** oraz **7 termów** na **78 strukturach skończonych** (uniwersa 1-, 2- i 3-elementowe) i **1038 wartościowaniach**. Wyniki:

| Kontrola | Sprawdzenia | Kontrprzykłady |
|---|---:|---:|
| Interpretacyjny lemat o podstawieniu | 1 965 972 | 0 |
| Zależność wartościowania formuły tylko od zmiennych wolnych | 105 876 | 0 |
| Schemat dowodu symetrii równości ze świeżą zmienną | 50 862 | 0 |
| Zachowanie spełniania przy zastępowaniu równych | 50 862 | 0 |
| Łańcuch kwantyfikatorów uniwersalnych | 1038 | 0 |

Wcześniejsza próba szerszej enumeracji przekroczyła limit wykonania i **nie została zaliczona**. W powyższej, mniejszej i niezależnej enumeracji wszystkie kontrole wykonano do końca. Takie testy nie zastępują dowodów ogólnych.

## Integralność i walidacja

- Rozdział 11 pozostał bez zmian źródłowych: 5 twierdzeń, 5 dowodów, 7 definicji, 16 przykładów, 8 uwag, **21 etykiet** i **7 odsyłaczy**.
- Książka obejmująca rozdziały 01–11 ma **309 unikatowych etykiet**, **119 wystąpień odsyłaczy** i jeden udokumentowany przyszły cel `ch:zf-axioms`.
- Ostatnia kontrola przed audytem III przeszła pomyślnie: dedykowany workflow [44929204034](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929204034) z kompilacją **103 stron PDF**, **19 testami regresyjnymi**, kontrolą CLI, referencji i przepełnionych wierszy oraz globalny workflow [44929204096](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44929204096), obejmujący testy przeglądarkowe.
- Bieżący raport wyzwala ponowny dedykowany workflow. **Dopiero pozytywny wynik na commicie raportu formalnie domyka rozdział.**

## Status i następna iteracja

**Audyt III zakończono bez poprawek. Rozdział 11 jest stabilny merytorycznie**, a jego formalne zamknięcie zależy od zielonego CI na commicie raportu. Kolejny rozdział do audytu I: **12 — „Poprawność logiki pierwszego rzędu”**. Zgodnie z globalną zasadą nie dodawać nowych wyników bez wyjątkowego uzasadnienia.
