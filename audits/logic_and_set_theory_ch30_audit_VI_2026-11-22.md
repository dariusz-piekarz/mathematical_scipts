# Logika matematyczna i teoria mnogości — rozdział 30, audyt VI (kontrola założeń i styku z rozdziałem 31)

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródła:** `chapters/pl/logic_and_set_theory/30-gry-nieskonczone-i-aksjomat-determinacji.tex`, `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex`.  
**Zakres:** kolejny audyt rozdziału 30, ze szczególnym naciskiem na aksjomaty bazowe i odniesienie do teorii modeli wewnętrznych w rozdziale 31. Nie tworzono rozdziału 32.

## Kontrola matematyczna

1. **AC a AD.** Twierdzenie `thm:ac-not-ad` rzeczywiście dowodzi w ZFC istnienia gry niezdeterminowanej. Dobrze uporządkowuje strategie i przez rekurencję przypisuje każdej strategii przegrywaną przez nią rozgrywkę. Na etapie `α<𝔠` liczba wcześniejszych wskazanych rozgrywek jest `<𝔠`, a każda strategia dopuszcza `𝔠` rozgrywek, więc można wybrać świeżą; nie trzeba zakładać regularności `𝔠`. Wynik daje `ZF ⊢ ¬(AC∧AD)`, równoważnie `ZF+AD ⊢ ¬AC` i `ZF+AC ⊢ ¬AD`.
2. **Silniejsza przeszkoda dla wyboru.** Twierdzenie `thm:ad-no-wellorder-reals` dowodzi w ZF+AD, że `ℝ` nie ma dobrego uporządkowania. Analiza selektora klas modulo `ℚ` korzysta z własności Baire'a udowodnionej wcześniej pod AD, a konstrukcja wymiernych przedziałów nie wymaga AC ani DC. Jest to wynik ściśle silniejszy niż samo wykluczenie AC w tym sensie, że zaprzecza konkretnej słabszej zasadzie dobrego porządkowania `ℝ`.
3. **Warianty determinacji.** Zachowano rozgraniczenie otwartej determinacji Gale'a–Stewarta (dowód w ZF), pełnego AD (niezgodny z AC) i PD (rozważanego z ZFC). Przywołane twierdzenia Martin–Steel i Martin–Steel–Woodin pozostają wynikami zewnętrznymi, nie dowodami własnymi.
4. **Wybór przeliczalny.** Lemat `lem:ad-countable-choice-reals` daje wybór przeliczalny z rodzin niepustych podzbiorów `ω^ω` bez założenia DC. Nie wolno utożsamiać go z pełnym AC.
5. **Mierzalność.** Zdanie twierdzenia `thm:ad-measurability` i jego dowód używają **ZF+DC+AD** oraz przywołanego twierdzenia o mierzalności zbiorów analitycznych. Starszy tytuł „AD implikuje mierzalność…” oraz tytuł sekcji nie ujawniały dodatkowej hipotezy DC, mimo że była ona jawna w treści. **Poprawiono oba nagłówki**, bez zmieniania twierdzenia, dowodu, etykiet ani referencji. Mocniejszy, klasycznie znany wynik z samego AD nie jest tutaj prezentowany jako udowodniony tą wersją argumentu.
6. **Relacja z rozdziałem 31.** Twierdzenie `thm:l-gch` dotyczy `L ⊨ ZFC+GCH` dowodzonego w metateorii ZF. Wniosek `cor:l-relative-consistency` daje `Con(ZF) ⇒ Con(ZFC+GCH)`. Nie wolno z tego wyprowadzać `Con(ZF+AD)`, której żaden z tych rozdziałów nie udowadnia. Gdy pracujemy w modelu ZF+AD, jego wewnętrzna klasa `L` nadal spełnia AC; brak tu sprzeczności, ponieważ `AD` nie musi zachodzić w `L`.
7. **Granice argumentu z konstrukcją L.** Ponownie sprawdzono rozróżnienie zbiorowych `L_α` i klasy właściwej `L`, absolutność formuł `Δ₀`, opis historii poziomów i użycie kondensacji do GCH. Nie znaleziono przy tej *celowanej kontroli styku* nowych usterek wymagających modyfikacji rozdziału 31; nie przedstawia się jej jako kolejnego pełnego audytu wszystkich ~2500 linii tego rozdziału.

## Kontrola struktury i zmian

- Rozdział 30: **57 unikatowych etykiet i 49 odsyłaczy**; rozdział 31: **68 etykiet i 87 odsyłaczy**.
- W rozdziałach 25–31 razem: **256 etykiet bez powtórzeń**. Wszystkie 226 odsyłaczy mają cele w rozdziałach 1–31 (pięć celów spoza zakresu 25–31 sprawdzono osobno w rozdziałach 4, 5, 6, 23, 24).
- Zmiana w `30-gry-nieskonczone-i-aksjomat-determinacji.tex`: **wyłącznie** tytuł sekcji i tytuł istniejącego twierdzenia o mierzalności; liczby środowisk i odsyłaczy nie zmieniły się.
- Nowy SHA źródła po poprawce: `d21195aa957db2e43e6bd4f27b6c11ccc9d123bb`. Commit źródła: `7fa11ddbdfeabefd7fd21397cd0aa5e249535e77`.
- Poprzednie pełne przebiegi CI dla rozdziałów 30 i 31 były zielone dla **wcześniejszych** SHA. Dla aktualnego SHA wynik nowego CI należy sprawdzić osobno; nie przypisujemy nowej zmianie wcześniejszego statusu SUCCESS.

## Werdykt

**Audyt VI: jedna rzeczywista poprawka redakcyjno-logiczna w nagłówkach twierdzenia, bez zmiany jego hipotez ani dowodu.** Twierdzenia o sprzeczności AC z AD i o niemożliwości dobrego uporządkowania liczb rzeczywistych pozostają poprawnie wyodrębnione. Rozdział 31 zachowuje status stabilny po wcześniejszym audycie V, z zastrzeżeniem, że przeprowadzona teraz kontrola nie zastępuje niezależnego audytu VI tego rozdziału.
